# Copyright (C) 2007-2010 AG Projects. See LICENSE for details.
#

from ctypes import *


GNUTLS_AL_FATAL = 2
GNUTLS_AL_WARNING = 1
GNUTLS_A_ACCESS_DENIED = 49
GNUTLS_A_BAD_CERTIFICATE = 42
GNUTLS_A_BAD_RECORD_MAC = 20
GNUTLS_A_CERTIFICATE_EXPIRED = 45
GNUTLS_A_CERTIFICATE_REVOKED = 44
GNUTLS_A_CERTIFICATE_UNKNOWN = 46
GNUTLS_A_CERTIFICATE_UNOBTAINABLE = 111
GNUTLS_A_CLOSE_NOTIFY = 0
GNUTLS_A_DECODE_ERROR = 50
GNUTLS_A_DECOMPRESSION_FAILURE = 30
GNUTLS_A_DECRYPTION_FAILED = 21
GNUTLS_A_DECRYPT_ERROR = 51
GNUTLS_A_EXPORT_RESTRICTION = 60
GNUTLS_A_HANDSHAKE_FAILURE = 40
GNUTLS_A_ILLEGAL_PARAMETER = 47
GNUTLS_A_INNER_APPLICATION_FAILURE = 208
GNUTLS_A_INNER_APPLICATION_VERIFICATION = 209
GNUTLS_A_INSUFFICIENT_SECURITY = 71
GNUTLS_A_INTERNAL_ERROR = 80
GNUTLS_A_NO_RENEGOTIATION = 100
GNUTLS_A_PROTOCOL_VERSION = 70
GNUTLS_A_RECORD_OVERFLOW = 22
GNUTLS_A_SSL3_NO_CERTIFICATE = 41
GNUTLS_A_UNEXPECTED_MESSAGE = 10
GNUTLS_A_UNKNOWN_CA = 48
GNUTLS_A_UNKNOWN_PSK_IDENTITY = 115
GNUTLS_A_UNRECOGNIZED_NAME = 112
GNUTLS_A_UNSUPPORTED_CERTIFICATE = 43
GNUTLS_A_UNSUPPORTED_EXTENSION = 110
GNUTLS_A_USER_CANCELED = 90
GNUTLS_CERT_IGNORE = 0
GNUTLS_CERT_INSECURE_ALGORITHM = 256
GNUTLS_CERT_INVALID = 2
GNUTLS_CERT_REQUEST = 1
GNUTLS_CERT_REQUIRE = 2
GNUTLS_CERT_REVOKED = 32
GNUTLS_CERT_SIGNER_NOT_CA = 128
GNUTLS_CERT_SIGNER_NOT_FOUND = 64
GNUTLS_CIPHER_3DES_CBC = 3
GNUTLS_CIPHER_AES_128_CBC = 4
GNUTLS_CIPHER_AES_256_CBC = 5
GNUTLS_CIPHER_ARCFOUR_128 = 2
GNUTLS_CIPHER_ARCFOUR_40 = 6
GNUTLS_CIPHER_CAMELLIA_128_CBC = 7
GNUTLS_CIPHER_CAMELLIA_256_CBC = 8
GNUTLS_CIPHER_DES_CBC = 91
GNUTLS_CIPHER_NULL = 1
GNUTLS_CIPHER_RC2_40_CBC = 90
GNUTLS_CIPHER_UNKNOWN = 0
GNUTLS_CLIENT = 2
GNUTLS_COMP_DEFLATE = 2
GNUTLS_COMP_LZO = 3
GNUTLS_COMP_NULL = 1
GNUTLS_COMP_UNKNOWN = 0
GNUTLS_CRD_ANON = 2
GNUTLS_CRD_CERTIFICATE = 1
GNUTLS_CRD_IA = 5
GNUTLS_CRD_PSK = 4
GNUTLS_CRD_SRP = 3
GNUTLS_CRL_REASON_AA_COMPROMISE = 32768 # Variable c_int
GNUTLS_CRL_REASON_AFFILIATION_CHANGED = 16 # Variable c_int
GNUTLS_CRL_REASON_CA_COMPROMISE = 32 # Variable c_int
GNUTLS_CRL_REASON_CERTIFICATE_HOLD = 2 # Variable c_int
GNUTLS_CRL_REASON_CESSATION_OF_OPERATION = 4 # Variable c_int
GNUTLS_CRL_REASON_KEY_COMPROMISE = 64 # Variable c_int
GNUTLS_CRL_REASON_PRIVILEGE_WITHDRAWN = 1 # Variable c_int
GNUTLS_CRL_REASON_SUPERSEEDED = 8 # Variable c_int
GNUTLS_CRL_REASON_UNUSED = 128 # Variable c_int
GNUTLS_CRT_OPENPGP = 2
GNUTLS_CRT_PRINT_FULL = 0
GNUTLS_CRT_PRINT_ONELINE = 1
GNUTLS_CRT_PRINT_UNSIGNED_FULL = 2
GNUTLS_CRT_UNKNOWN = 0
GNUTLS_CRT_X509 = 1
GNUTLS_DIG_MD2 = 5
GNUTLS_DIG_MD5 = 2
GNUTLS_DIG_NULL = 1
GNUTLS_DIG_RMD160 = 4
GNUTLS_DIG_SHA1 = 3
GNUTLS_DIG_SHA224 = 9
GNUTLS_DIG_SHA256 = 6
GNUTLS_DIG_SHA384 = 7
GNUTLS_DIG_SHA512 = 8
GNUTLS_E_AGAIN = -28 # Variable c_int
GNUTLS_E_APPLICATION_ERROR_MAX = -65000 # Variable c_int
GNUTLS_E_APPLICATION_ERROR_MIN = -65500 # Variable c_int
GNUTLS_E_ASN1_DER_ERROR = -69 # Variable c_int
GNUTLS_E_ASN1_DER_OVERFLOW = -77 # Variable c_int
GNUTLS_E_ASN1_ELEMENT_NOT_FOUND = -67 # Variable c_int
GNUTLS_E_ASN1_GENERIC_ERROR = -71 # Variable c_int
GNUTLS_E_ASN1_IDENTIFIER_NOT_FOUND = -68 # Variable c_int
GNUTLS_E_ASN1_SYNTAX_ERROR = -76 # Variable c_int
GNUTLS_E_ASN1_TAG_ERROR = -73 # Variable c_int
GNUTLS_E_ASN1_TAG_IMPLICIT = -74 # Variable c_int
GNUTLS_E_ASN1_TYPE_ANY_ERROR = -75 # Variable c_int
GNUTLS_E_ASN1_VALUE_NOT_FOUND = -70 # Variable c_int
GNUTLS_E_ASN1_VALUE_NOT_VALID = -72 # Variable c_int
GNUTLS_E_BASE64_DECODING_ERROR = -34 # Variable c_int
GNUTLS_E_BASE64_ENCODING_ERROR = -201 # Variable c_int
GNUTLS_E_BASE64_UNEXPECTED_HEADER_ERROR = -207 # Variable c_int
GNUTLS_E_CERTIFICATE_ERROR = -43 # Variable c_int
GNUTLS_E_CERTIFICATE_KEY_MISMATCH = -60 # Variable c_int
GNUTLS_E_COMPRESSION_FAILED = -27 # Variable c_int
GNUTLS_E_CONSTRAINT_ERROR = -101 # Variable c_int
GNUTLS_E_CRYPTO_ALREADY_REGISTERED = -209 # Variable c_int
GNUTLS_E_DB_ERROR = -30 # Variable c_int
GNUTLS_E_DECOMPRESSION_FAILED = -26 # Variable c_int
GNUTLS_E_DECRYPTION_FAILED = -24 # Variable c_int
GNUTLS_E_DH_PRIME_UNACCEPTABLE = -63 # Variable c_int
GNUTLS_E_ENCRYPTION_FAILED = -40 # Variable c_int
GNUTLS_E_ERROR_IN_FINISHED_PACKET = -18 # Variable c_int
GNUTLS_E_EXPIRED = -29 # Variable c_int
GNUTLS_E_FATAL_ALERT_RECEIVED = -12 # Variable c_int
GNUTLS_E_FILE_ERROR = -64 # Variable c_int
GNUTLS_E_GOT_APPLICATION_DATA = -38 # Variable c_int
GNUTLS_E_HANDSHAKE_TOO_LARGE = -210 # Variable c_int
GNUTLS_E_HASH_FAILED = -33 # Variable c_int
GNUTLS_E_IA_VERIFY_FAILED = -104 # Variable c_int
GNUTLS_E_ILLEGAL_SRP_USERNAME = -90 # Variable c_int
GNUTLS_E_INCOMPATIBLE_CRYPTO_LIBRARY = -202 # Variable c_int
GNUTLS_E_INCOMPATIBLE_GCRYPT_LIBRARY = -202 # Variable c_int
GNUTLS_E_INCOMPATIBLE_LIBTASN1_LIBRARY = -203 # Variable c_int
GNUTLS_E_INIT_LIBEXTRA = -82 # Variable c_int
GNUTLS_E_INSUFFICIENT_CREDENTIALS = -32 # Variable c_int
GNUTLS_E_INTERNAL_ERROR = -59 # Variable c_int
GNUTLS_E_INTERRUPTED = -52 # Variable c_int
GNUTLS_E_INVALID_PASSWORD = -99 # Variable c_int
GNUTLS_E_INVALID_REQUEST = -50 # Variable c_int
GNUTLS_E_INVALID_SESSION = -10 # Variable c_int
GNUTLS_E_KEY_USAGE_VIOLATION = -48 # Variable c_int
GNUTLS_E_LARGE_PACKET = -7 # Variable c_int
GNUTLS_E_LIBRARY_VERSION_MISMATCH = -83 # Variable c_int
GNUTLS_E_LZO_INIT_FAILED = -85 # Variable c_int
GNUTLS_E_MAC_VERIFY_FAILED = -100 # Variable c_int
GNUTLS_E_MEMORY_ERROR = -25 # Variable c_int
GNUTLS_E_MPI_PRINT_FAILED = -35 # Variable c_int
GNUTLS_E_MPI_SCAN_FAILED = -23 # Variable c_int
GNUTLS_E_NO_CERTIFICATE_FOUND = -49 # Variable c_int
GNUTLS_E_NO_CIPHER_SUITES = -87 # Variable c_int
GNUTLS_E_NO_COMPRESSION_ALGORITHMS = -86 # Variable c_int
GNUTLS_E_NO_TEMPORARY_DH_PARAMS = -93 # Variable c_int
GNUTLS_E_NO_TEMPORARY_RSA_PARAMS = -84 # Variable c_int
GNUTLS_E_OPENPGP_FINGERPRINT_UNSUPPORTED = -94 # Variable c_int
GNUTLS_E_OPENPGP_GETKEY_FAILED = -88 # Variable c_int
GNUTLS_E_OPENPGP_KEYRING_ERROR = -204 # Variable c_int
GNUTLS_E_OPENPGP_SUBKEY_ERROR = -208 # Variable c_int
GNUTLS_E_OPENPGP_UID_REVOKED = -79 # Variable c_int
GNUTLS_E_PKCS1_WRONG_PAD = -57 # Variable c_int
GNUTLS_E_PK_DECRYPTION_FAILED = -45 # Variable c_int
GNUTLS_E_PK_ENCRYPTION_FAILED = -44 # Variable c_int
GNUTLS_E_PK_SIGN_FAILED = -46 # Variable c_int
GNUTLS_E_PK_SIG_VERIFY_FAILED = -89 # Variable c_int
GNUTLS_E_PULL_ERROR = -54 # Variable c_int
GNUTLS_E_PUSH_ERROR = -53 # Variable c_int
GNUTLS_E_RANDOM_FAILED = -206 # Variable c_int
GNUTLS_E_RECEIVED_ILLEGAL_EXTENSION = -58 # Variable c_int
GNUTLS_E_RECEIVED_ILLEGAL_PARAMETER = -55 # Variable c_int
GNUTLS_E_RECORD_LIMIT_REACHED = -39 # Variable c_int
GNUTLS_E_REHANDSHAKE = -37 # Variable c_int
GNUTLS_E_REQUESTED_DATA_NOT_AVAILABLE = -56 # Variable c_int
GNUTLS_E_SHORT_MEMORY_BUFFER = -51 # Variable c_int
GNUTLS_E_SRP_PWD_ERROR = -31 # Variable c_int
GNUTLS_E_SRP_PWD_PARSING_ERROR = -91 # Variable c_int
GNUTLS_E_SUCCESS = 0 # Variable c_int
GNUTLS_E_TOO_MANY_EMPTY_PACKETS = -78 # Variable c_int
GNUTLS_E_UNEXPECTED_HANDSHAKE_PACKET = -19 # Variable c_int
GNUTLS_E_UNEXPECTED_PACKET = -15 # Variable c_int
GNUTLS_E_UNEXPECTED_PACKET_LENGTH = -9 # Variable c_int
GNUTLS_E_UNIMPLEMENTED_FEATURE = -1250 # Variable c_int
GNUTLS_E_UNKNOWN_ALGORITHM = -105 # Variable c_int
GNUTLS_E_UNKNOWN_CIPHER_SUITE = -21 # Variable c_int
GNUTLS_E_UNKNOWN_CIPHER_TYPE = -6 # Variable c_int
GNUTLS_E_UNKNOWN_COMPRESSION_ALGORITHM = -3 # Variable c_int
GNUTLS_E_UNKNOWN_HASH_ALGORITHM = -96 # Variable c_int
GNUTLS_E_UNKNOWN_PKCS_BAG_TYPE = -98 # Variable c_int
GNUTLS_E_UNKNOWN_PKCS_CONTENT_TYPE = -97 # Variable c_int
GNUTLS_E_UNKNOWN_PK_ALGORITHM = -80 # Variable c_int
GNUTLS_E_UNSUPPORTED_CERTIFICATE_TYPE = -61 # Variable c_int
GNUTLS_E_UNSUPPORTED_VERSION_PACKET = -8 # Variable c_int
GNUTLS_E_UNWANTED_ALGORITHM = -22 # Variable c_int
GNUTLS_E_WARNING_ALERT_RECEIVED = -16 # Variable c_int
GNUTLS_E_WARNING_IA_FPHF_RECEIVED = -103 # Variable c_int
GNUTLS_E_WARNING_IA_IPHF_RECEIVED = -102 # Variable c_int
GNUTLS_E_X509_UNKNOWN_SAN = -62 # Variable c_int
GNUTLS_E_X509_UNSUPPORTED_ATTRIBUTE = -95 # Variable c_int
GNUTLS_E_X509_UNSUPPORTED_CRITICAL_EXTENSION = -47 # Variable c_int
GNUTLS_E_X509_UNSUPPORTED_OID = -205 # Variable c_int
GNUTLS_HANDSHAKE_CERTIFICATE_PKT = 11
GNUTLS_HANDSHAKE_CERTIFICATE_REQUEST = 13
GNUTLS_HANDSHAKE_CERTIFICATE_VERIFY = 15
GNUTLS_HANDSHAKE_CLIENT_HELLO = 1
GNUTLS_HANDSHAKE_CLIENT_KEY_EXCHANGE = 16
GNUTLS_HANDSHAKE_FINISHED = 20
GNUTLS_HANDSHAKE_HELLO_REQUEST = 0
GNUTLS_HANDSHAKE_SERVER_HELLO = 2
GNUTLS_HANDSHAKE_SERVER_HELLO_DONE = 14
GNUTLS_HANDSHAKE_SERVER_KEY_EXCHANGE = 12
GNUTLS_HANDSHAKE_SUPPLEMENTAL = 23
GNUTLS_IA_APPLICATION_PAYLOAD = 0
GNUTLS_IA_FINAL_PHASE_FINISHED = 2
GNUTLS_IA_INTERMEDIATE_PHASE_FINISHED = 1
GNUTLS_KEY_CRL_SIGN = 2 # Variable c_int
GNUTLS_KEY_DATA_ENCIPHERMENT = 16 # Variable c_int
GNUTLS_KEY_DECIPHER_ONLY = 32768 # Variable c_int
GNUTLS_KEY_DIGITAL_SIGNATURE = 128 # Variable c_int
GNUTLS_KEY_ENCIPHER_ONLY = 1 # Variable c_int
GNUTLS_KEY_KEY_AGREEMENT = 8 # Variable c_int
GNUTLS_KEY_KEY_CERT_SIGN = 4 # Variable c_int
GNUTLS_KEY_KEY_ENCIPHERMENT = 32 # Variable c_int
GNUTLS_KEY_NON_REPUDIATION = 64 # Variable c_int
GNUTLS_KP_ANY = '2.5.29.37.0' # Variable STRING
GNUTLS_KP_CODE_SIGNING = '1.3.6.1.5.5.7.3.3' # Variable STRING
GNUTLS_KP_EMAIL_PROTECTION = '1.3.6.1.5.5.7.3.4' # Variable STRING
GNUTLS_KP_OCSP_SIGNING = '1.3.6.1.5.5.7.3.9' # Variable STRING
GNUTLS_KP_TIME_STAMPING = '1.3.6.1.5.5.7.3.8' # Variable STRING
GNUTLS_KP_TLS_WWW_CLIENT = '1.3.6.1.5.5.7.3.2' # Variable STRING
GNUTLS_KP_TLS_WWW_SERVER = '1.3.6.1.5.5.7.3.1' # Variable STRING
GNUTLS_KX_ANON_DH = 4
GNUTLS_KX_DHE_DSS = 2
GNUTLS_KX_DHE_PSK = 10
GNUTLS_KX_DHE_RSA = 3
GNUTLS_KX_PSK = 9
GNUTLS_KX_RSA = 1
GNUTLS_KX_RSA_EXPORT = 6
GNUTLS_KX_SRP = 5
GNUTLS_KX_SRP_DSS = 8
GNUTLS_KX_SRP_RSA = 7
GNUTLS_KX_UNKNOWN = 0
GNUTLS_MAC_MD2 = 5
GNUTLS_MAC_MD5 = 2
GNUTLS_MAC_NULL = 1
GNUTLS_MAC_RMD160 = 4
GNUTLS_MAC_SHA1 = 3
GNUTLS_MAC_SHA256 = 6
GNUTLS_MAC_SHA384 = 7
GNUTLS_MAC_SHA512 = 8
GNUTLS_MAC_UNKNOWN = 0
GNUTLS_MASTER_SIZE = 48 # Variable c_int
GNUTLS_MAX_ALGORITHM_NUM = 16 # Variable c_int
GNUTLS_MAX_SESSION_ID = 32 # Variable c_int
GNUTLS_NAME_DNS = 1
GNUTLS_OID_LDAP_DC = '0.9.2342.19200300.100.1.25' # Variable STRING
GNUTLS_OID_LDAP_UID = '0.9.2342.19200300.100.1.1' # Variable STRING
GNUTLS_OID_PKCS9_EMAIL = '1.2.840.113549.1.9.1' # Variable STRING
GNUTLS_OID_PKIX_COUNTRY_OF_CITIZENSHIP = '1.3.6.1.5.5.7.9.4' # Variable STRING
GNUTLS_OID_PKIX_COUNTRY_OF_RESIDENCE = '1.3.6.1.5.5.7.9.5' # Variable STRING
GNUTLS_OID_PKIX_DATE_OF_BIRTH = '1.3.6.1.5.5.7.9.1' # Variable STRING
GNUTLS_OID_PKIX_GENDER = '1.3.6.1.5.5.7.9.3' # Variable STRING
GNUTLS_OID_PKIX_PLACE_OF_BIRTH = '1.3.6.1.5.5.7.9.2' # Variable STRING
GNUTLS_OID_X520_COMMON_NAME = '2.5.4.3' # Variable STRING
GNUTLS_OID_X520_COUNTRY_NAME = '2.5.4.6' # Variable STRING
GNUTLS_OID_X520_DN_QUALIFIER = '2.5.4.46' # Variable STRING
GNUTLS_OID_X520_GENERATION_QUALIFIER = '2.5.4.44' # Variable STRING
GNUTLS_OID_X520_GIVEN_NAME = '2.5.4.42' # Variable STRING
GNUTLS_OID_X520_INITIALS = '2.5.4.43' # Variable STRING
GNUTLS_OID_X520_LOCALITY_NAME = '2.5.4.7' # Variable STRING
GNUTLS_OID_X520_ORGANIZATIONAL_UNIT_NAME = '2.5.4.11' # Variable STRING
GNUTLS_OID_X520_ORGANIZATION_NAME = '2.5.4.10' # Variable STRING
GNUTLS_OID_X520_PSEUDONYM = '2.5.4.65' # Variable STRING
GNUTLS_OID_X520_STATE_OR_PROVINCE_NAME = '2.5.4.8' # Variable STRING
GNUTLS_OID_X520_SURNAME = '2.5.4.4' # Variable STRING
GNUTLS_OID_X520_TITLE = '2.5.4.12' # Variable STRING
GNUTLS_OPENPGP_CERT = 0
GNUTLS_OPENPGP_CERT_FINGERPRINT = 1
GNUTLS_OPENPGP_FMT_BASE64 = 1
GNUTLS_OPENPGP_FMT_RAW = 0
GNUTLS_PARAMS_DH = 2
GNUTLS_PARAMS_RSA_EXPORT = 1
GNUTLS_PKCS_PLAIN = 1
GNUTLS_PKCS_USE_PBES2_3DES = 16
GNUTLS_PKCS_USE_PKCS12_3DES = 2
GNUTLS_PKCS_USE_PKCS12_ARCFOUR = 4
GNUTLS_PKCS_USE_PKCS12_RC2_40 = 8
GNUTLS_PK_DSA = 2
GNUTLS_PK_RSA = 1
GNUTLS_PK_UNKNOWN = 0
GNUTLS_PSK_KEY_HEX = 1
GNUTLS_PSK_KEY_RAW = 0
GNUTLS_RANDOM_SIZE = 32 # Variable c_int
GNUTLS_SAN_DN = 6
GNUTLS_SAN_DNSNAME = 1
GNUTLS_SAN_IPADDRESS = 4
GNUTLS_SAN_OTHERNAME = 5
GNUTLS_SAN_OTHERNAME_XMPP = 1000
GNUTLS_SAN_RFC822NAME = 2
GNUTLS_SAN_URI = 3
GNUTLS_SERVER = 1
GNUTLS_SHUT_RDWR = 0
GNUTLS_SHUT_WR = 1
GNUTLS_SIGN_DSA_SHA1 = 2
GNUTLS_SIGN_RSA_MD2 = 4
GNUTLS_SIGN_RSA_MD5 = 3
GNUTLS_SIGN_RSA_RMD160 = 5
GNUTLS_SIGN_RSA_SHA1 = 1
GNUTLS_SIGN_RSA_SHA224 = 9
GNUTLS_SIGN_RSA_SHA256 = 6
GNUTLS_SIGN_RSA_SHA384 = 7
GNUTLS_SIGN_RSA_SHA512 = 8
GNUTLS_SIGN_UNKNOWN = 0
GNUTLS_SUPPLEMENTAL_USER_MAPPING_DATA = 0
GNUTLS_SSL3 = 1
GNUTLS_TLS1_0 = 2
GNUTLS_TLS1_1 = 3
GNUTLS_TLS1_2 = 4
GNUTLS_VERIFY_ALLOW_ANY_X509_V1_CA_CRT = 8
GNUTLS_VERIFY_ALLOW_SIGN_RSA_MD2 = 16
GNUTLS_VERIFY_ALLOW_SIGN_RSA_MD5 = 32
GNUTLS_VERIFY_ALLOW_X509_V1_CA_CRT = 2
GNUTLS_VERIFY_DISABLE_CA_SIGN = 1
GNUTLS_VERIFY_DO_NOT_ALLOW_SAME = 4
GNUTLS_VERSION_UNKNOWN = 255
GNUTLS_X509_CRT_LIST_IMPORT_FAIL_IF_EXCEED = 1
GNUTLS_X509_FMT_DER = 0
GNUTLS_X509_FMT_PEM = 1

__all__ = sorted(name for name in dir() if name.startswith('GNUTLS_'))

