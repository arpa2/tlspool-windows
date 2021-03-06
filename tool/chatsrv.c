/* tlspool/testsrv.c -- Exchange plaintext stdio over the network */

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdint.h>
#include <ctype.h>

#include <unistd.h>
#include <poll.h>
#include <errno.h>
#include <signal.h>

#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>

#include <tlspool/starttls.h>

#include "socket.h"
#include "runterminal.h"

// chat was removed immediately after 4af0d87c479d9eb9720f56b2fea9cfdd0d6d1fd5


static int    vhostc;
static char **vhostv;


static starttls_t tlsdata_srv = {
	.flags = PIOF_STARTTLS_LOCALROLE_SERVER
		| PIOF_STARTTLS_REMOTEROLE_CLIENT,
	.local = 0,
	.ipproto = IPPROTO_TCP,
	.localid = "testsrv@tlspool.arpa2.lab",
	.service = "generic",
};
static starttls_t tlsdata_now;


int namedconnect_vhost (starttls_t *tlsdata, void *privdata) {
	int i;
	tlsdata->localid [sizeof (tlsdata->localid)-1] == '\0';
	fprintf (stderr, "namedconnect_vhost looking for %s\n", tlsdata->localid);
	for (i=0; i<vhostc; i++) {
		char *patn = vhostv [i];
		char *mtch = tlsdata->localid;
		if (*patn == '*') {
			patn++;
			mtch = strchr (mtch, '.');
			if (mtch == NULL) {
				continue;
			}
		}
		if (strcasecmp (patn, mtch) == 0) {
#if !defined(WINDOWS_PORT)
			int soxx[2];
#else
			// https://github.com/ncm/selectable-socketpair
			extern int dumb_socketpair(SOCKET socks[2], int make_overlapped);
			SOCKET soxx[2];
#endif
			//TODO// Setup for TCP, UDP, SCTP
#ifndef WINDOWS_PORT
			if (socketpair (AF_UNIX, SOCK_SEQPACKET, 0, soxx) == 0)
#else /* WINDOWS_PORT */
			if (dumb_socketpair(soxx, 1) == 0)
#endif /* WINDOWS_PORT */
			{
				// printf("DEBUG: socketpair succeeded\n");
				/* Socketpair created */
				* (int *) privdata = soxx [1];
				return soxx [0];
			}
		}
	}
	fprintf (stderr, "No match found in namedconnect_vhost, tried %d\n", vhostc);
	return -1;
}


void sigcont_handler (int signum);
static struct sigaction sigcont_action = {
	.sa_handler = sigcont_handler,
	.sa_mask = 0,
	.sa_flags = SA_NODEFER
};

static int sigcont = 0;

void sigcont_handler (int signum) {
	sigcont = 1;
}

int exit_val = 1;
void graceful_exit (int signum) {
	exit (exit_val);
}
	

void dump_printable (char *descr, char *info, int infolen) {
	printf ("%s, #%d: ", descr);
	while (infolen-- > 0) {
		putchar (isalnum (*info) ? *info : '.');
		info++;
	}
	putchar ('\n');
}

int main (int argc, char **argv) {
	int sox, cnx, rc;
	int plainfd;
	struct sockaddr_storage sa;
	sigset_t sigcontset;
	uint8_t rndbuf [16];
	int (*namedconnect) (starttls_t *tlsdata, void *privdata) = NULL;
	char *progname = NULL;
	bool do_signum = false;
	bool do_timeout = false;
	int signum = -1;
	int timeout = -1;
	uint16_t infolen = 0;
	uint8_t info [TLSPOOL_INFOBUFLEN];

	// argv[1] is SNI or . as a wildcard;
	// argv[2] is address and requires argv[3] for port
	// argv[5+] were used for chat, but dropped after 4af0d87c479d9eb9720f56b2fea9cfdd0d6d1fd5
	if ((argc == 1) || (argc == 3) || (argc > 5)) {
		fprintf (stderr, "Usage: %s servername|. [address port [0|signum|-timeout]]\n", argv [0]);
		exit (1);
	}

	// store the program name
	/* progname = strrchr (argv [0], '/'); */
	if (progname == NULL) {
		progname = argv [0];
	}

	// process argv[1] with local identity or its overriding "."
	if (strcmp (argv [1], ".") != 0) {
		if (strlen (argv [1]) > sizeof (tlsdata_srv.localid) - 1) {
			fprintf (stderr, "Server name exceeded %d characters\n",
					sizeof (tlsdata_srv.localid) - 1);
			exit (1);
		}
		vhostc = 1;
		vhostv = argv+1;
		tlsdata_srv.localid [0] = '\0';
		tlsdata_srv.flags |= PIOF_STARTTLS_LOCALID_CHECK;
		namedconnect = namedconnect_vhost;
	}

	// process optional argv[2,3] with address and port
	memset (&sa, 0, sizeof (sa));
	char *addrstr = "::1", *portstr = "12345";
	if (argc >= 4) {
		addrstr = argv [2];
		portstr = argv [3];
	}
	if (!socket_parse (addrstr, portstr, (struct sockaddr *) &sa)) {
		fprintf (stderr, "Incorrect address %s and/or port %s\n", argv [2], argv [3]);
		exit (1);
	}

	// process optional 0|-signum|timeout
	// where 0 means nothing, -signum awaits the signal number, timeout is seconds to finish
	if (argc >= 5) {
		int parsed = atoi (argv [4]);
		if (parsed < 0) {
			do_timeout = true;
			timeout = -parsed;
		} else if (parsed > 0) {
			do_signum = true;
			signum = parsed;
		}
	}

	if (sigemptyset (&sigcontset) ||
	    sigaddset (&sigcontset, SIGCONT) ||
	    pthread_sigmask (SIG_BLOCK, &sigcontset, NULL)) {
		perror ("Failed to block SIGCONT in worker thread");
		exit (1);
	}

	// When timeout hits, we should stop gracefully, with exit(exit_val)
	if (do_timeout) {
		if (signal (SIGALRM, graceful_exit) == SIG_ERR) {
			fprintf (stderr, "Failed to install signal handler for timeout\n");
			exit (1);
		}
		alarm (timeout);
		printf ("Scheduled to exit(exit_val) in %d seconds\n", timeout);
	}

	// When the signal hits, we should stop gracefully, with exit(exit_val)
	if (do_signum) {
		if (signal (signum, graceful_exit) == SIG_ERR) {
			fprintf (stderr, "Failed to install signal handler for signal %d\n", signum);
			exit (1);
		}
		printf ("Scheduled to exit(exit_val) upon reception of signal %d\n", signum);
	}

reconnect:
	if (!socket_server ((struct sockaddr *) &sa, SOCK_STREAM, &sox)) {
		perror ("Failed to create socket on testsrv");
		exit (1);
	}
	printf ("--\n");
	fflush (stdout);
	/*
	 * During the first iteration, exit_val is 1 because a single connection
	 * should come through.  During later connections, exit_val is 0 while in
	 * accept() but it will always be 1 during active connections, including
	 * during the TLS Pool handshake.  As a result, timeout and signal may
	 * interrupt us but it will only exit(0) between connections and after at
	 * least one connection.
	 */
	while ((cnx = accept (sox, NULL, 0))) {
		if (cnx == -1) {
			perror ("Failed to accept incoming connection");
			continue;
		}
		exit_val = 1;
		tlsdata_now = tlsdata_srv;
		plainfd = -1;
		if (-1 == tlspool_starttls (cnx, &tlsdata_now, &plainfd, namedconnect)) {
			perror ("Failed to STARTTLS on testsrv");
			if (plainfd >= 0) {
				close (plainfd);
			}
			exit (1);
		}
		printf ("DEBUG: STARTTLS succeeded on testsrv\n");
		if (tlspool_prng ("EXPERIMENTAL-tlspool-test", 0, NULL, 16, rndbuf, tlsdata_now.ctlkey) == -1) {
			printf ("ERROR %d: Could not extract data with PRNG function\n", errno);
		} else {
			printf ("PRNG bytes: %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x\n",
				rndbuf [ 0], rndbuf [ 1], rndbuf [ 2], rndbuf [ 3],
				rndbuf [ 4], rndbuf [ 5], rndbuf [ 6], rndbuf [ 7],
				rndbuf [ 8], rndbuf [ 9], rndbuf [10], rndbuf [11],
				rndbuf [12], rndbuf [13], rndbuf [14], rndbuf [15]);
		}
		if (tlspool_prng ("EXPERIMENTAL-tlspool-test", 16, rndbuf, 16, rndbuf, tlsdata_now.ctlkey) == -1) {
			printf ("ERROR: Could not extract data with PRNG function\n");
		} else {
			printf ("PRNG again: %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x\n",
				rndbuf [ 0], rndbuf [ 1], rndbuf [ 2], rndbuf [ 3],
				rndbuf [ 4], rndbuf [ 5], rndbuf [ 6], rndbuf [ 7],
				rndbuf [ 8], rndbuf [ 9], rndbuf [10], rndbuf [11],
				rndbuf [12], rndbuf [13], rndbuf [14], rndbuf [15]);
		}
		infolen = 0xffff;
		if (tlspool_info (PIOK_INFO_CHANBIND_TLS_UNIQUE, info, &infolen, tlsdata_now.ctlkey) == -1) {
			printf ("ERROR %d: Could not retrieve tls-unique channel binding info\n", errno);
		} else {
			printf ("Channel binding info, tls-unique, 12 bytes of %d: "
				"%02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x\n",
				infolen,
				info [ 0], info [ 1], info [ 2], info [ 3],
				info [ 4], info [ 5], info [ 6], info [ 7],
				info [ 8], info [ 9], info [10], info [11]);
		}
		infolen = 0xffff;
		if (tlspool_info (PIOK_INFO_PEERCERT_SUBJECT, info, &infolen, tlsdata_now.ctlkey) == -1) {
			printf ("ERROR %d: Could not retrieve Subject (peer)\n", errno);
		} else {
			dump_printable ("Subject, peer", info, infolen);
		}
		infolen = 0xffff;
		if (tlspool_info (PIOK_INFO_PEERCERT_ISSUER, info, &infolen, tlsdata_now.ctlkey) == -1) {
			printf ("ERROR %d: Could not retrieve Issuer (peer)\n", errno);
		} else {
			dump_printable ("Issuer,  peer", info, infolen);
		}
		strcpy ((char *) info + 2, "testcli@tlspool.arpa2.lab");
		info [1] = strlen (info + 2);
		info [0] = 0x81;  // DER_TAG_CONTEXT(1);
		infolen = 2 + strlen ((char *) (info + 2));
		if (tlspool_info (PIOK_INFO_PEERCERT_SUBJECTALTNAME, info, &infolen, tlsdata_now.ctlkey) == -1) {
			printf ("ERROR %d: Could not retrieve SubjectAltName (peer)\n", errno);
		} else {
			dump_printable ("SubjectAltName, peer", info, infolen);
		}
		infolen = 0xffff;
		if (tlspool_info (PIOK_INFO_MYCERT_SUBJECT, info, &infolen, tlsdata_now.ctlkey) == -1) {
			printf ("ERROR %d: Could not retrieve Subject (mine)\n", errno);
		} else {
			dump_printable ("Subject, mine", info, infolen);
		}
		infolen = 0xffff;
		if (tlspool_info (PIOK_INFO_MYCERT_ISSUER, info, &infolen, tlsdata_now.ctlkey) == -1) {
			printf ("ERROR %d: Could not retrieve Issuer (mine)\n", errno);
		} else {
			dump_printable ("Issuer,  mine", info, infolen);
		}
		if (sigcont) {
			printf ("Ignoring SIGCONT received prior to the new connection\n");
			sigcont = 0;
		}
		strcpy ((char *) info + 2, "testsrv@tlspool.arpa2.lab");
		info [1] = strlen (info + 2);
		info [0] = 0x81;  // DER_TAG_CONTEXT(1);
		infolen = 2 + strlen ((char *) (info + 2));
		if (tlspool_info (PIOK_INFO_MYCERT_SUBJECTALTNAME, info, &infolen, tlsdata_now.ctlkey) == -1) {
			printf ("ERROR %d: Could not retrieve SubjectAltName (mine)\n", errno);
		} else {
			dump_printable ("SubjectAltName, mine", info, infolen);
		}
		if (-1 == sigaction (SIGCONT, &sigcont_action, NULL)) {
			perror ("Failed to install signal handler for SIGCONT");
			close (plainfd);
			close (sox);
			exit (1);
		} else if (pthread_sigmask (SIG_UNBLOCK, &sigcontset, NULL))  {
			perror ("Failed to unblock SIGCONT on terminal handler");
			close (plainfd);
			close (sox);
			exit (1);
		} else {
			printf ("SIGCONT will trigger renegotiation of the TLS handshake during a connection\n");
		}
		printf ("DEBUG: Local plainfd = %d\n", plainfd);
		runterminal (plainfd, &sigcont, &tlsdata_now,
				PIOF_STARTTLS_LOCALROLE_SERVER | PIOF_STARTTLS_REMOTEROLE_CLIENT | PIOF_STARTTLS_RENEGOTIATE,
				"testsrv@tlspool.arpa2.lab",
				NULL
		);
		printf ("DEBUG: Client connection terminated\n");
		close (plainfd);
		exit_val = 0;
		if (pthread_sigmask (SIG_BLOCK, &sigcontset, NULL))  {
			perror ("Failed to block signal handler for SIGCONT");
			close (sox);
			exit (1);
		}
	}
	return 0;
}

