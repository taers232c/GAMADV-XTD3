# -*- coding: utf-8 -*-

# Copyright (C) 2020 Ross Scroggs All Rights Reserved.
#
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""GAM gam.cfg variables

"""

import os
import ssl

TRUE = 'true'
FALSE = 'false'
DEFAULT_CHARSET = 'utf-8'
MY_CUSTOMER = 'my_customer'
NEVER = 'Never'
TLS_CHOICE_MAP = {
  '': '',
  'tlsv1': 'TLSv1',
  'tlsv1_0': 'TLSv1', 'tlsv1.0': 'TLSv1',
  'tlsv1_1': 'TLSv1_1', 'tlsv1.1': 'TLSv1_1',
  'tlsv1_2': 'TLSv1_2', 'tlsv1.2': 'TLSv1_2',
  'tlsv1_3': 'TLSv1_3', 'tlsv1.3': 'TLSv1_3',
  }

FN_CACERTS_PEM = 'cacerts.pem'
FN_CLIENT_SECRETS_JSON = 'client_secrets.json'
FN_EXTRA_ARGS_TXT = 'extra-args.txt'
FN_OAUTH2_TXT = 'oauth2.txt'
FN_OAUTH2SERVICE_JSON = 'oauth2service.json'

# Global variables defined in gam.cfg

# The following XXX constants are the names of the items in gam.cfg
# When retrieving lists of Google Drive activities from API, how many should be retrieved in each chunk
ACTIVITY_MAX_RESULTS = 'activity_max_results'
# Check if API calls rate exceeds limit
API_CALLS_RATE_CHECK = 'api_calls_rate_check'
# API calls per 100 seconds limit
API_CALLS_RATE_LIMIT = 'api_calls_rate_limit'
# Automatically generate gam batch command if number of users specified in gam users xxx command exceeds this number
# Default: 0, don't automatically generate gam batch commands
AUTO_BATCH_MIN = 'auto_batch_min'
# When processing items in batches, how many should be processed in each batch
BATCH_SIZE = 'batch_size'
# Location of cacerts.pem for API calls
CACERTS_PEM = 'cacerts_pem'
# GAM cache directory
CACHE_DIR = 'cache_dir'
# GAM cache discovery only. If no_cache is False, only API discovery calls will be cached
CACHE_DISCOVERY_ONLY = 'cache_discovery_only'
# Character set of batch, csv, data files
CHARSET = 'charset'
# When retrieving lists of Google Classroom items from API, how many should be retrieved in each chunk
CLASSROOM_MAX_RESULTS = 'classroom_max_results'
# Path to client_secrets.json
CLIENT_SECRETS_JSON = 'client_secrets_json'
# GAM config directory containing client_secrets.json, oauth2.txt, oauth2service.json, extra_args.txt
CONFIG_DIR = 'config_dir'
# When retrieving lists of Google Contacts from API, how many should be retrieved in each chunk
CONTACT_MAX_RESULTS = 'contact_max_results'
# Column delimiter in CSV input file
CSV_INPUT_COLUMN_DELIMITER = 'csv_input_column_delimiter'
# Quote character in CSV input file
CSV_INPUT_QUOTE_CHAR = 'csv_input_quote_char'
# Convert newlines in text fields to "\n" in CSV output file
CSV_OUTPUT_CONVERT_CR_NL = 'csv_output_convert_cr_nl'
# Column delimiter in CSV output file
CSV_OUTPUT_COLUMN_DELIMITER = 'csv_output_column_delimiter'
# Field list delimiter in CSV output file
CSV_OUTPUT_FIELD_DELIMITER = 'csv_output_field_delimiter'
# Filter for column headers
CSV_OUTPUT_HEADER_FILTER = 'csv_output_header_filter'
# Line terminator in CSV output file
CSV_OUTPUT_LINE_TERMINATOR = 'csv_output_line_terminator'
# Quote character in CSV output file
CSV_OUTPUT_QUOTE_CHAR = 'csv_output_quote_char'
# Filter for column values
CSV_OUTPUT_ROW_FILTER = 'csv_output_row_filter'
# Output rows for users even if they do not have the print object (delegate, filters, ...)
CSV_OUTPUT_USERS_AUDIT = 'csv_output_users_audit'
# custmerId from gam.cfg or retrieved from Google
CUSTOMER_ID = 'customer_id'
# If debug_level > 0: extra_args['prettyPrint'] = True, httplib2.debuglevel = gam_debug_level, appsObj.debug = True
DEBUG_LEVEL = 'debug_level'
# When retrieving lists of ChromeOS devices from API, how many should be retrieved in each chunk
DEVICE_MAX_RESULTS = 'device_max_results'
# Domain obtained from gam.cfg or oauth2.txt
DOMAIN = 'domain'
# Google Drive download directory
DRIVE_DIR = 'drive_dir'
# When retrieving lists of Drive files/folders from API, how many should be retrieved in each chunk
DRIVE_MAX_RESULTS = 'drive_max_results'
# Use Drive V3 ntive names
DRIVE_V3_NATIVE_NAMES = 'drive_v3_native_names'
# When processing email messages in batches, how many should be processed in each batch
EMAIL_BATCH_SIZE = 'email_batch_size'
# When retrieving lists of calendar events from API, how many should be retrieved in each chunk
EVENT_MAX_RESULTS = 'event_max_results'
# Path to extra_args.txt
EXTRA_ARGS = 'extra_args'
# When processing items in batches, how many seconds should GAM wait between batches
INTER_BATCH_WAIT = 'inter_batch_wait'
# When retrieving lists of Google Group members from API, how many should be retrieved in each chunk
MEMBER_MAX_RESULTS = 'member_max_results'
# When deleting or modifying Gmail messages, how many should be processed in each batch
MESSAGE_BATCH_SIZE = 'message_batch_size'
# When retrieving lists of Gmail messages from API, how many should be retrieved in each chunk
MESSAGE_MAX_RESULTS = 'message_max_results'
# When retrieving lists of Mobile devices from API, how many should be retrieved in each chunk
MOBILE_MAX_RESULTS = 'mobile_max_results'
# Value to substitute for NEVER_TIME
NEVER_TIME = 'never_time'
# If no_browser is False, writeCSVfile won't open a browser when todrive is set
# and doOAuthRequest prints a link and waits for the verification code when oauth2.txt is being created
NO_BROWSER = 'no_browser'
# Disable GAM API caching
NO_CACHE = 'no_cache'
# Disable GAM update check
NO_UPDATE_CHECK = 'no_update_check'
# Disable SSL certificate validation
NO_VERIFY_SSL = 'no_verify_ssl'
# Number of threads for gam tbatch
NUM_TBATCH_THREADS = 'num_tbatch_threads'
# Number of threads for gam batch/csv
NUM_THREADS = 'num_threads'
# Path to oauth2.txt
OAUTH2_TXT = 'oauth2_txt'
# Path to oauth2service.json
OAUTH2SERVICE_JSON = 'oauth2service_json'
# Default section to use for processing
SECTION = 'section'
# Show API calls retry data
SHOW_API_CALLS_RETRY_DATA = 'show_api_calls_retry_data'
# Convert newlines in text fields to "\n" in show commands
SHOW_CONVERT_CR_NL = 'show_convert_cr_nl'
# Add (n/m) to end of messages if number of items to be processed exceeds this number
SHOW_COUNTS_MIN = 'show_counts_min'
# Enable/disable "Getting ... " messages
SHOW_GETTINGS = 'show_gettings'
# Enable/disable NL at end of "Got ..." messages
SHOW_GETTINGS_GOT_NL = 'show_gettings_got_nl'
# Enable/disable showing multiprocess info in redirected stdout/stderr
SHOW_MULTIPROCESS_INFO = 'show_multiprocess_info'
# SMTP fqdn
SMTP_FQDN = 'smtp_fqdn'
# SMTP host
SMTP_HOST = 'smtp_host'
# SMTP username
SMTP_USERNAME = 'smtp_username'
# SMTP password
SMTP_PASSWORD = 'smtp_password'
## Minimum TLS Version required for HTTPS connections
TLS_MIN_VERSION = 'tls_min_version'
## Maximum TLS Version used for HTTPS connections
TLS_MAX_VERSION = 'tls_max_version'
# Time Zone
TIMEZONE = 'timezone'
# Use client access for todrive
TODRIVE_CLIENTACCESS = 'todrive_clientaccess'
# Enable conversion to Google Sheets when uploading todrive files
TODRIVE_CONVERSION = 'todrive_conversion'
# Save local copy of CSV file
TODRIVE_LOCALCOPY = 'todrive_localcopy'
# Specify locale for Google Sheets
TODRIVE_LOCALE = 'todrive_locale'
# Suppress opening browser on todrive upload
TODRIVE_NOBROWSER = 'todrive_nobrowser'
# Suppress sending email on todrive upload
TODRIVE_NOEMAIL = 'todrive_noemail'
# ID/Name of parent folder for todrive files
TODRIVE_PARENT = 'todrive_parent'
# Append timestamp to todrive file name
TODRIVE_TIMESTAMP = 'todrive_timestamp'
# Specify timezone for Google Sheets
TODRIVE_TIMEZONE = 'todrive_timezone'
# User for todrive files
TODRIVE_USER = 'todrive_user'
# When retrieving lists of Users from API, how many should be retrieved in each chunk
USER_MAX_RESULTS = 'user_max_results'
# User service account access only, no client access
USER_SERVICE_ACCOUNT_ACCESS_ONLY = 'user_service_account_access_only'

Defaults = {
  ACTIVITY_MAX_RESULTS: '100',
  API_CALLS_RATE_CHECK: FALSE,
  API_CALLS_RATE_LIMIT: '100',
  AUTO_BATCH_MIN: '0',
  BATCH_SIZE: '50',
  CACERTS_PEM: '',
  CACHE_DIR: '',
  CACHE_DISCOVERY_ONLY: TRUE,
  CHARSET: DEFAULT_CHARSET,
  CLASSROOM_MAX_RESULTS: '0',
  CLIENT_SECRETS_JSON: FN_CLIENT_SECRETS_JSON,
  CONFIG_DIR: '',
  CONTACT_MAX_RESULTS: '100',
  CSV_INPUT_COLUMN_DELIMITER: ',',
  CSV_INPUT_QUOTE_CHAR: '\'"\'',
  CSV_OUTPUT_COLUMN_DELIMITER: ',',
  CSV_OUTPUT_CONVERT_CR_NL: FALSE,
  CSV_OUTPUT_FIELD_DELIMITER: u"' '",
  CSV_OUTPUT_HEADER_FILTER: '',
  CSV_OUTPUT_LINE_TERMINATOR: 'lf',
  CSV_OUTPUT_QUOTE_CHAR: '\'"\'',
  CSV_OUTPUT_ROW_FILTER: '',
  CSV_OUTPUT_USERS_AUDIT: FALSE,
  CUSTOMER_ID: MY_CUSTOMER,
  DEBUG_LEVEL: '0',
  DEVICE_MAX_RESULTS: '200',
  DOMAIN: '',
  DRIVE_DIR: '',
  DRIVE_MAX_RESULTS: '1000',
  DRIVE_V3_NATIVE_NAMES: TRUE,
  EMAIL_BATCH_SIZE: '50',
  EVENT_MAX_RESULTS: '250',
  EXTRA_ARGS: '',
  INTER_BATCH_WAIT: '0',
  MEMBER_MAX_RESULTS: '200',
  MESSAGE_BATCH_SIZE: '50',
  MESSAGE_MAX_RESULTS: '500',
  MOBILE_MAX_RESULTS: '100',
  NEVER_TIME: NEVER,
  NO_BROWSER: FALSE,
  NO_CACHE: FALSE,
  NO_UPDATE_CHECK: TRUE,
  NO_VERIFY_SSL: FALSE,
  NUM_TBATCH_THREADS: '2',
  NUM_THREADS: '5',
  OAUTH2_TXT: FN_OAUTH2_TXT,
  OAUTH2SERVICE_JSON: FN_OAUTH2SERVICE_JSON,
  SECTION: '',
  SHOW_API_CALLS_RETRY_DATA: FALSE,
  SHOW_CONVERT_CR_NL: FALSE,
  SHOW_COUNTS_MIN: '1',
  SHOW_GETTINGS: TRUE,
  SHOW_GETTINGS_GOT_NL: FALSE,
  SHOW_MULTIPROCESS_INFO: FALSE,
  SMTP_FQDN: '',
  SMTP_HOST: '',
  SMTP_USERNAME: '',
  SMTP_PASSWORD: '',
  TLS_MIN_VERSION: 'TLSv1_2' if hasattr(ssl.SSLContext(), "minimum_version") else '',
  TLS_MAX_VERSION: '',
  TIMEZONE: 'utc',
  TODRIVE_CLIENTACCESS: FALSE,
  TODRIVE_CONVERSION: TRUE,
  TODRIVE_LOCALCOPY: FALSE,
  TODRIVE_LOCALE: '',
  TODRIVE_NOBROWSER: '',
  TODRIVE_NOEMAIL: '',
  TODRIVE_PARENT: 'root',
  TODRIVE_TIMESTAMP: FALSE,
  TODRIVE_TIMEZONE: '',
  TODRIVE_USER: '',
  USER_MAX_RESULTS: '500',
  USER_SERVICE_ACCOUNT_ACCESS_ONLY: FALSE,
  }

Values = {DEBUG_LEVEL: 0}

TYPE_BOOLEAN = 'bool'
TYPE_CHARACTER = 'char'
TYPE_CHOICE = 'choi'
TYPE_DATETIME = 'datm'
TYPE_DIRECTORY = 'dire'
TYPE_EMAIL = 'emai'
TYPE_EMAIL_OPTIONAL = 'emao'
TYPE_FILE = 'file'
TYPE_FLOAT = 'floa'
TYPE_HEADERFILTER = 'heaf'
TYPE_INTEGER = 'inte'
TYPE_LANGUAGE = 'lang'
TYPE_LOCALE = 'locl'
TYPE_PASSWORD = 'pass'
TYPE_ROWFILTER = 'rowf'
TYPE_STRING = 'stri'
TYPE_TIMEZONE = 'tmzn'

VAR_TYPE = 'type'
VAR_ENVVAR = 'enva'
VAR_CHOICES = 'chod'
VAR_LIMITS = 'lmit'
VAR_SFFT = 'sfft'
VAR_SIGFILE = 'sigf'
VAR_ACCESS = 'aces'

VAR_INFO = {
  ACTIVITY_MAX_RESULTS: {VAR_TYPE: TYPE_INTEGER, VAR_LIMITS: (1, 500)},
  API_CALLS_RATE_CHECK: {VAR_TYPE: TYPE_BOOLEAN},
  API_CALLS_RATE_LIMIT: {VAR_TYPE: TYPE_INTEGER, VAR_LIMITS: (50, None)},
  AUTO_BATCH_MIN: {VAR_TYPE: TYPE_INTEGER, VAR_ENVVAR: 'GAM_AUTOBATCH', VAR_LIMITS: (0, 100)},
  BATCH_SIZE: {VAR_TYPE: TYPE_INTEGER, VAR_ENVVAR: 'GAM_BATCH_SIZE', VAR_LIMITS: (1, 1000)},
  CACERTS_PEM: {VAR_TYPE: TYPE_FILE, VAR_ENVVAR: 'GAM_CA_FILE', VAR_ACCESS: os.R_OK},
  CACHE_DIR: {VAR_TYPE: TYPE_DIRECTORY, VAR_ENVVAR: 'GAMCACHEDIR'},
  CACHE_DISCOVERY_ONLY: {VAR_TYPE: TYPE_BOOLEAN, VAR_SIGFILE: 'allcache.txt', VAR_SFFT: (TRUE, FALSE)},
  CHARSET: {VAR_TYPE: TYPE_STRING, VAR_ENVVAR: 'GAM_CHARSET', VAR_LIMITS: (1, None)},
  CLASSROOM_MAX_RESULTS: {VAR_TYPE: TYPE_INTEGER, VAR_LIMITS: (0, 1000)},
  CLIENT_SECRETS_JSON: {VAR_TYPE: TYPE_FILE, VAR_ENVVAR: 'CLIENTSECRETS', VAR_ACCESS: os.R_OK},
  CONFIG_DIR: {VAR_TYPE: TYPE_DIRECTORY, VAR_ENVVAR: 'GAMUSERCONFIGDIR'},
  CONTACT_MAX_RESULTS: {VAR_TYPE: TYPE_INTEGER, VAR_LIMITS: (1, 10000)},
  CSV_INPUT_COLUMN_DELIMITER: {VAR_TYPE: TYPE_CHARACTER},
  CSV_INPUT_QUOTE_CHAR: {VAR_TYPE: TYPE_CHARACTER},
  CSV_OUTPUT_COLUMN_DELIMITER: {VAR_TYPE: TYPE_CHARACTER},
  CSV_OUTPUT_CONVERT_CR_NL: {VAR_TYPE: TYPE_BOOLEAN},
  CSV_OUTPUT_FIELD_DELIMITER: {VAR_TYPE: TYPE_CHARACTER},
  CSV_OUTPUT_HEADER_FILTER: {VAR_TYPE: TYPE_HEADERFILTER, VAR_ENVVAR: 'GAM_CSV_HEADER_FILTER'},
  CSV_OUTPUT_LINE_TERMINATOR: {VAR_TYPE: TYPE_CHOICE, VAR_CHOICES: {'cr': '\r', 'lf': '\n', 'crlf': '\r\n'}},
  CSV_OUTPUT_QUOTE_CHAR: {VAR_TYPE: TYPE_CHARACTER},
  CSV_OUTPUT_ROW_FILTER: {VAR_TYPE: TYPE_ROWFILTER, VAR_ENVVAR: 'GAM_CSV_ROW_FILTER'},
  CSV_OUTPUT_USERS_AUDIT: {VAR_TYPE: TYPE_BOOLEAN},
  CUSTOMER_ID: {VAR_TYPE: TYPE_STRING, VAR_ENVVAR: 'CUSTOMER_ID', VAR_LIMITS: (0, None)},
  DEBUG_LEVEL: {VAR_TYPE: TYPE_INTEGER, VAR_SIGFILE: 'debug.gam', VAR_LIMITS: (0, None), VAR_SFFT: ('0', '4')},
  DEVICE_MAX_RESULTS: {VAR_TYPE: TYPE_INTEGER, VAR_LIMITS: (1, 200)},
  DOMAIN: {VAR_TYPE: TYPE_STRING, VAR_ENVVAR: 'GA_DOMAIN', VAR_LIMITS: (0, None)},
  DRIVE_DIR: {VAR_TYPE: TYPE_DIRECTORY, VAR_ENVVAR: 'GAMDRIVEDIR'},
  DRIVE_MAX_RESULTS: {VAR_TYPE: TYPE_INTEGER, VAR_LIMITS: (1, 1000)},
  DRIVE_V3_NATIVE_NAMES: {VAR_TYPE: TYPE_BOOLEAN},
  EMAIL_BATCH_SIZE: {VAR_TYPE: TYPE_INTEGER, VAR_LIMITS: (1, 100)},
  EVENT_MAX_RESULTS: {VAR_TYPE: TYPE_INTEGER, VAR_LIMITS: (1, 2500)},
  EXTRA_ARGS: {VAR_TYPE: TYPE_FILE, VAR_SIGFILE: FN_EXTRA_ARGS_TXT, VAR_SFFT: ('', FN_EXTRA_ARGS_TXT), VAR_ACCESS: os.R_OK},
  INTER_BATCH_WAIT: {VAR_TYPE: TYPE_FLOAT, VAR_LIMITS: (0.0, 60.0)},
  MEMBER_MAX_RESULTS: {VAR_TYPE: TYPE_INTEGER, VAR_LIMITS: (1, 200)},
  MESSAGE_BATCH_SIZE: {VAR_TYPE: TYPE_INTEGER, VAR_LIMITS: (1, 1000)},
  MESSAGE_MAX_RESULTS: {VAR_TYPE: TYPE_INTEGER, VAR_LIMITS: (1, 10000)},
  MOBILE_MAX_RESULTS: {VAR_TYPE: TYPE_INTEGER, VAR_LIMITS: (1, 100)},
  NEVER_TIME: {VAR_TYPE: TYPE_STRING, VAR_LIMITS: (0, None)},
  NO_BROWSER: {VAR_TYPE: TYPE_BOOLEAN, VAR_SIGFILE: 'nobrowser.txt', VAR_SFFT: (FALSE, TRUE)},
  NO_CACHE: {VAR_TYPE: TYPE_BOOLEAN, VAR_SIGFILE: 'nocache.txt', VAR_SFFT: (FALSE, TRUE)},
  NO_UPDATE_CHECK: {VAR_TYPE: TYPE_BOOLEAN, VAR_SIGFILE: 'noupdatecheck.txt', VAR_SFFT: (FALSE, TRUE)},
  NO_VERIFY_SSL: {VAR_TYPE: TYPE_BOOLEAN},
  NUM_TBATCH_THREADS: {VAR_TYPE: TYPE_INTEGER, VAR_LIMITS: (1, 100)},
  NUM_THREADS: {VAR_TYPE: TYPE_INTEGER, VAR_ENVVAR: 'GAM_THREADS', VAR_LIMITS: (1, 100)},
  OAUTH2_TXT: {VAR_TYPE: TYPE_FILE, VAR_ENVVAR: 'OAUTHFILE', VAR_ACCESS: os.R_OK | os.W_OK},
  OAUTH2SERVICE_JSON: {VAR_TYPE: TYPE_FILE, VAR_ENVVAR: 'OAUTHSERVICEFILE', VAR_ACCESS: os.R_OK | os.W_OK},
  SECTION: {VAR_TYPE: TYPE_STRING, VAR_LIMITS: (0, None)},
  SHOW_API_CALLS_RETRY_DATA: {VAR_TYPE: TYPE_BOOLEAN},
  SHOW_CONVERT_CR_NL: {VAR_TYPE: TYPE_BOOLEAN},
  SHOW_COUNTS_MIN: {VAR_TYPE: TYPE_INTEGER, VAR_LIMITS: (0, 100)},
  SHOW_GETTINGS: {VAR_TYPE: TYPE_BOOLEAN},
  SHOW_GETTINGS_GOT_NL: {VAR_TYPE: TYPE_BOOLEAN},
  SHOW_MULTIPROCESS_INFO: {VAR_TYPE: TYPE_BOOLEAN},
  SMTP_FQDN: {VAR_TYPE: TYPE_STRING, VAR_LIMITS: (0, None)},
  SMTP_HOST: {VAR_TYPE: TYPE_STRING, VAR_LIMITS: (0, None)},
  SMTP_USERNAME: {VAR_TYPE: TYPE_STRING, VAR_LIMITS: (0, None)},
  SMTP_PASSWORD: {VAR_TYPE: TYPE_PASSWORD, VAR_LIMITS: (0, None)},
  TLS_MIN_VERSION: {VAR_TYPE: TYPE_CHOICE, VAR_ENVVAR: 'GAM_TLS_MIN_VERSION', VAR_CHOICES: TLS_CHOICE_MAP},
  TLS_MAX_VERSION: {VAR_TYPE: TYPE_CHOICE, VAR_ENVVAR: 'GAM_TLS_MAX_VERSION', VAR_CHOICES: TLS_CHOICE_MAP},
  TIMEZONE: {VAR_TYPE: TYPE_TIMEZONE},
  TODRIVE_CLIENTACCESS: {VAR_TYPE: TYPE_BOOLEAN},
  TODRIVE_CONVERSION: {VAR_TYPE: TYPE_BOOLEAN},
  TODRIVE_LOCALCOPY: {VAR_TYPE: TYPE_BOOLEAN},
  TODRIVE_LOCALE: {VAR_TYPE: TYPE_LOCALE},
  TODRIVE_NOBROWSER: {VAR_TYPE: TYPE_BOOLEAN, VAR_SIGFILE: 'nobrowser.txt', VAR_SFFT: (FALSE, TRUE)},
  TODRIVE_NOEMAIL: {VAR_TYPE: TYPE_BOOLEAN},
  TODRIVE_PARENT: {VAR_TYPE: TYPE_STRING, VAR_LIMITS: (0, None)},
  TODRIVE_TIMESTAMP: {VAR_TYPE: TYPE_BOOLEAN},
  TODRIVE_TIMEZONE: {VAR_TYPE: TYPE_STRING, VAR_LIMITS: (0, None)},
  TODRIVE_USER: {VAR_TYPE: TYPE_STRING, VAR_LIMITS: (0, None)},
  USER_MAX_RESULTS: {VAR_TYPE: TYPE_INTEGER, VAR_ENVVAR: 'GAM_USER_MAX_RESULTS', VAR_LIMITS: (1, 500)},
  USER_SERVICE_ACCOUNT_ACCESS_ONLY: {VAR_TYPE: TYPE_BOOLEAN},
  }
