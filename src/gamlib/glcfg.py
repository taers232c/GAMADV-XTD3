# -*- coding: utf-8 -*-

# Copyright (C) 2016 Ross Scroggs All Rights Reserved.
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

TRUE = u'true'
FALSE = u'false'
DEFAULT_CHARSET = u'utf-8'
MY_CUSTOMER = u'my_customer'
NEVER = u'Never'

FN_CACERTS_PEM = u'cacerts.pem'
FN_CLIENT_SECRETS_JSON = u'client_secrets.json'
FN_EXTRA_ARGS_TXT = u'extra-args.txt'
FN_OAUTH2SERVICE_JSON = u'oauth2service.json'
FN_OAUTH2_TXT = u'oauth2.txt'

# Global variables defined in gam.cfg

# The following XXX constants are the names of the items in gam.cfg
# When retrieving lists of Google Drive activities from API, how many should be retrieved in each chunk
ACTIVITY_MAX_RESULTS = u'activity_max_results'
# Automatically generate gam batch command if number of users specified in gam users xxx command exceeds this number
# Default: 0, don't automatically generate gam batch commands
AUTO_BATCH_MIN = u'auto_batch_min'
# When processing items in batches, how many should be processed in each batch
BATCH_SIZE = u'batch_size'
# Location of cacerts.pem for API calls
CACERTS_PEM = u'cacerts_pem'
# GAM cache directory
CACHE_DIR = u'cache_dir'
# GAM cache discovery only. If no_cache is False, only API discovery calls will be cached
CACHE_DISCOVERY_ONLY = u'cache_discovery_only'
# Character set of batch, csv, data files
CHARSET = u'charset'
# When retrieving lists of Google Classroom items from API, how many should be retrieved in each chunk
CLASSROOM_MAX_RESULTS = u'classroom_max_results'
# Path to client_secrets.json
CLIENT_SECRETS_JSON = u'client_secrets_json'
# GAM config directory containing client_secrets.json, oauth2.txt, oauth2service.json, extra_args.txt
CONFIG_DIR = u'config_dir'
# When retrieving lists of Google Contacts from API, how many should be retrieved in each chunk
CONTACT_MAX_RESULTS = u'contact_max_results'
# Column delimiter in CSV input file
CSV_INPUT_COLUMN_DELIMITER = u'csv_input_column_delimiter'
# Quote character in CSV input file
CSV_INPUT_QUOTE_CHAR = u'csv_input_quote_char'
# Convert newlines in text fields to "\n" in CSV output file
CSV_OUTPUT_CONVERT_CR_NL = u'csv_output_convert_cr_nl'
# Column delimiter in CSV output file
CSV_OUTPUT_COLUMN_DELIMITER = u'csv_output_column_delimiter'
# Field list delimiter in CSV output file
CSV_OUTPUT_FIELD_DELIMITER = u'csv_output_field_delimiter'
# Quote character in CSV output file
CSV_OUTPUT_QUOTE_CHAR = u'csv_output_quote_char'
# Line terminator in CSV output file
CSV_OUTPUT_LINE_TERMINATOR = u'csv_output_line_terminator'
# Output rows for users even if they do not have the print object (delegate, filters, ...)
CSV_OUTPUT_USERS_AUDIT = u'csv_output_users_audit'
# custmerId from gam.cfg or retrieved from Google
CUSTOMER_ID = u'customer_id'
# If debug_level > 0: extra_args[u'prettyPrint'] = True, httplib2.debuglevel = gam_debug_level, appsObj.debug = True
DEBUG_LEVEL = u'debug_level'
# When retrieving lists of ChromeOS/Mobile devices from API, how many should be retrieved in each chunk
DEVICE_MAX_RESULTS = u'device_max_results'
# Domain obtained from gam.cfg or oauth2.txt
DOMAIN = u'domain'
# Google Drive download directory
DRIVE_DIR = u'drive_dir'
# When retrieving lists of Drive files/folders from API, how many should be retrieved in each chunk
DRIVE_MAX_RESULTS = u'drive_max_results'
# Use Drive V3 ntive names
DRIVE_V3_NATIVE_NAMES = u'drive_v3_native_names'
# When processing email messages in batches, how many should be processed in each batch
EMAIL_BATCH_SIZE = u'email_batch_size'
# When retrieving lists of calendar events from API, how many should be retrieved in each chunk
EVENT_MAX_RESULTS = u'event_max_results'
# Path to extra_args.txt
EXTRA_ARGS = u'extra_args'
# When processing items in batches, how many seconds should GAM wait between batches
INTER_BATCH_WAIT = u'inter_batch_wait'
# When retrieving lists of Google Group members from API, how many should be retrieved in each chunk
MEMBER_MAX_RESULTS = u'member_max_results'
# When deleting or modifying Gmail messages, how many should be processed in each batch
MESSAGE_BATCH_SIZE = u'message_batch_size'
# When retrieving lists of Gmail messages from API, how many should be retrieved in each chunk
MESSAGE_MAX_RESULTS = u'message_max_results'
# Value to substitute for NEVER_TIME
NEVER_TIME = u'never_time'
# If no_browser is False, writeCSVfile won't open a browser when todrive is set
# and doOAuthRequest prints a link and waits for the verification code when oauth2.txt is being created
NO_BROWSER = u'no_browser'
# Disable GAM API caching
NO_CACHE = u'no_cache'
# Disable GAM update check
NO_UPDATE_CHECK = u'no_update_check'
# Disable SSL certificate validation
NO_VERIFY_SSL = u'no_verify_ssl'
# Number of threads for gam tbatch
NUM_TBATCH_THREADS = u'num_tbatch_threads'
# Number of threads for gam batch/csv
NUM_THREADS = u'num_threads'
# Path to oauth2.txt
OAUTH2_TXT = u'oauth2_txt'
# Path to oauth2service.json
OAUTH2SERVICE_JSON = u'oauth2service_json'
# Use native field names in gam print groups/orgs
PRINT_NATIVE_NAMES = u'print_native_names'
# Default section to use for processing
SECTION = u'section'
# Convert newlines in text fields to "\n" in show commands
SHOW_CONVERT_CR_NL = u'show_convert_cr_nl'
# Add (n/m) to end of messages if number of items to be processed exceeds this number
SHOW_COUNTS_MIN = u'show_counts_min'
# Enable/disable "Getting ... " messages
SHOW_GETTINGS = u'show_gettings'
# Enable/disable NL at end of "Got ..." messages
SHOW_GETTINGS_GOT_NL = u'show_gettings_got_nl'
# Enable/disable showing multiprocess info in redirected stdout/stderr
SHOW_MULTIPROCESS_INFO = u'show_multiprocess_info'
# Time Zone
TIMEZONE = u'timezone'
# Enable conversion to Google Sheets when uploading todrive files
TODRIVE_CONVERSION = u'todrive_conversion'
# User for todrive files
TODRIVE_USER = u'todrive_user'
# ID/Name of parent folder for todrive files
TODRIVE_PARENT = u'todrive_parent'
# Append timestamp to todrive file name
TODRIVE_TIMESTAMP = u'todrive_timestamp'
# Save local copy of CSV file
TODRIVE_LOCALCOPY = u'todrive_localcopy'
# When retrieving lists of Users from API, how many should be retrieved in each chunk
USER_MAX_RESULTS = u'user_max_results'

Defaults = {
  ACTIVITY_MAX_RESULTS: u'100',
  AUTO_BATCH_MIN: u'0',
  BATCH_SIZE: u'50',
  CACERTS_PEM: u'',
  CACHE_DIR: u'',
  CACHE_DISCOVERY_ONLY: TRUE,
  CHARSET: DEFAULT_CHARSET,
  CLASSROOM_MAX_RESULTS: u'0',
  CLIENT_SECRETS_JSON: FN_CLIENT_SECRETS_JSON,
  CONFIG_DIR: u'',
  CONTACT_MAX_RESULTS: u'100',
  CSV_INPUT_COLUMN_DELIMITER: u',',
  CSV_INPUT_QUOTE_CHAR: u'\'"\'',
  CSV_OUTPUT_CONVERT_CR_NL: FALSE,
  CSV_OUTPUT_COLUMN_DELIMITER: u',',
  CSV_OUTPUT_FIELD_DELIMITER: u"' '",
  CSV_OUTPUT_LINE_TERMINATOR: u'lf',
  CSV_OUTPUT_QUOTE_CHAR: u'\'"\'',
  CSV_OUTPUT_USERS_AUDIT: FALSE,
  CUSTOMER_ID: MY_CUSTOMER,
  DEBUG_LEVEL: u'0',
  DEVICE_MAX_RESULTS: u'500',
  DOMAIN: u'',
  DRIVE_DIR: u'',
  DRIVE_MAX_RESULTS: u'1000',
  DRIVE_V3_NATIVE_NAMES: TRUE,
  EMAIL_BATCH_SIZE: u'100',
  EVENT_MAX_RESULTS: u'250',
  EXTRA_ARGS: u'',
  INTER_BATCH_WAIT: u'0',
  MEMBER_MAX_RESULTS: u'200',
  MESSAGE_BATCH_SIZE: u'1000',
  MESSAGE_MAX_RESULTS: u'1000',
  NEVER_TIME: NEVER,
  NO_BROWSER: FALSE,
  NO_CACHE: FALSE,
  NO_UPDATE_CHECK: TRUE,
  NO_VERIFY_SSL: FALSE,
  NUM_TBATCH_THREADS: u'2',
  NUM_THREADS: u'5',
  OAUTH2_TXT: FN_OAUTH2_TXT,
  OAUTH2SERVICE_JSON: FN_OAUTH2SERVICE_JSON,
  PRINT_NATIVE_NAMES: TRUE,
  SECTION: u'',
  SHOW_CONVERT_CR_NL: FALSE,
  SHOW_COUNTS_MIN: u'1',
  SHOW_GETTINGS: TRUE,
  SHOW_GETTINGS_GOT_NL: FALSE,
  SHOW_MULTIPROCESS_INFO: FALSE,
  TIMEZONE: u'utc',
  TODRIVE_CONVERSION: TRUE,
  TODRIVE_USER: u'',
  TODRIVE_PARENT: u'root',
  TODRIVE_TIMESTAMP: FALSE,
  TODRIVE_LOCALCOPY: FALSE,
  USER_MAX_RESULTS: u'500',
  }

Values = {DEBUG_LEVEL: 0}

TYPE_BOOLEAN = u'bool'
TYPE_CHARACTER = u'char'
TYPE_CHOICE = u'choi'
TYPE_DATETIME = u'datm'
TYPE_DIRECTORY = u'dire'
TYPE_EMAIL = u'emai'
TYPE_EMAIL_OPTIONAL = u'emao'
TYPE_FILE = u'file'
TYPE_FLOAT = u'floa'
TYPE_INTEGER = u'inte'
TYPE_LANGUAGE = u'lang'
TYPE_STRING = u'stri'
TYPE_TIMEZONE = u'tmzn'

VAR_TYPE = u'type'
VAR_ENVVAR = u'enva'
VAR_CHOICES = u'chod'
VAR_LIMITS = u'lmit'
VAR_SFFT = u'sfft'
VAR_SIGFILE = u'sigf'
VAR_ACCESS = u'aces'

VAR_INFO = {
  ACTIVITY_MAX_RESULTS: {VAR_TYPE: TYPE_INTEGER, VAR_ENVVAR: u'GAM_ACTIVITY_MAX_RESULTS', VAR_LIMITS: (1, 500)},
  AUTO_BATCH_MIN: {VAR_TYPE: TYPE_INTEGER, VAR_ENVVAR: u'GAM_AUTOBATCH', VAR_LIMITS: (0, 100)},
  BATCH_SIZE: {VAR_TYPE: TYPE_INTEGER, VAR_ENVVAR: u'GAM_BATCH_SIZE', VAR_LIMITS: (1, 1000)},
  CACERTS_PEM: {VAR_TYPE: TYPE_FILE, VAR_ACCESS: os.R_OK},
  CACHE_DIR: {VAR_TYPE: TYPE_DIRECTORY, VAR_ENVVAR: u'GAMCACHEDIR'},
  CACHE_DISCOVERY_ONLY: {VAR_TYPE: TYPE_BOOLEAN, VAR_SIGFILE: u'allcache.txt', VAR_SFFT: (TRUE, FALSE)},
  CHARSET: {VAR_TYPE: TYPE_STRING, VAR_ENVVAR: u'GAM_CHARSET', VAR_LIMITS: (1, None)},
  CLASSROOM_MAX_RESULTS: {VAR_TYPE: TYPE_INTEGER, VAR_LIMITS: (0, 1000)},
  CLIENT_SECRETS_JSON: {VAR_TYPE: TYPE_FILE, VAR_ENVVAR: u'CLIENTSECRETS', VAR_ACCESS: os.R_OK},
  CONFIG_DIR: {VAR_TYPE: TYPE_DIRECTORY, VAR_ENVVAR: u'GAMUSERCONFIGDIR'},
  CONTACT_MAX_RESULTS: {VAR_TYPE: TYPE_INTEGER, VAR_LIMITS: (1, 10000)},
  CSV_INPUT_COLUMN_DELIMITER: {VAR_TYPE: TYPE_CHARACTER},
  CSV_INPUT_QUOTE_CHAR: {VAR_TYPE: TYPE_CHARACTER},
  CSV_OUTPUT_CONVERT_CR_NL: {VAR_TYPE: TYPE_BOOLEAN},
  CSV_OUTPUT_COLUMN_DELIMITER: {VAR_TYPE: TYPE_CHARACTER},
  CSV_OUTPUT_FIELD_DELIMITER: {VAR_TYPE: TYPE_CHARACTER},
  CSV_OUTPUT_LINE_TERMINATOR: {VAR_TYPE: TYPE_CHOICE, VAR_CHOICES: {u'cr': u'\r', u'lf': u'\n', u'crlf': u'\r\n'}},
  CSV_OUTPUT_QUOTE_CHAR: {VAR_TYPE: TYPE_CHARACTER},
  CSV_OUTPUT_USERS_AUDIT: {VAR_TYPE: TYPE_BOOLEAN},
  CUSTOMER_ID: {VAR_TYPE: TYPE_STRING, VAR_ENVVAR: u'CUSTOMER_ID', VAR_LIMITS: (0, None)},
  DEBUG_LEVEL: {VAR_TYPE: TYPE_INTEGER, VAR_SIGFILE: u'debug.gam', VAR_LIMITS: (0, None), VAR_SFFT: (u'0', u'4')},
  DEVICE_MAX_RESULTS: {VAR_TYPE: TYPE_INTEGER, VAR_ENVVAR: u'GAM_DEVICE_MAX_RESULTS', VAR_LIMITS: (1, 1000)},
  DOMAIN: {VAR_TYPE: TYPE_STRING, VAR_ENVVAR: u'GA_DOMAIN', VAR_LIMITS: (0, None)},
  DRIVE_DIR: {VAR_TYPE: TYPE_DIRECTORY, VAR_ENVVAR: u'GAMDRIVEDIR'},
  DRIVE_MAX_RESULTS: {VAR_TYPE: TYPE_INTEGER, VAR_ENVVAR: u'GAM_DRIVE_MAX_RESULTS', VAR_LIMITS: (1, 1000)},
  DRIVE_V3_NATIVE_NAMES: {VAR_TYPE: TYPE_BOOLEAN},
  EMAIL_BATCH_SIZE: {VAR_TYPE: TYPE_INTEGER, VAR_LIMITS: (1, 100)},
  EVENT_MAX_RESULTS: {VAR_TYPE: TYPE_INTEGER, VAR_LIMITS: (1, 2500)},
  EXTRA_ARGS: {VAR_TYPE: TYPE_FILE, VAR_SIGFILE: FN_EXTRA_ARGS_TXT, VAR_SFFT: (u'', FN_EXTRA_ARGS_TXT), VAR_ACCESS: os.R_OK},
  INTER_BATCH_WAIT: {VAR_TYPE: TYPE_FLOAT, VAR_LIMITS: (0.0, 60.0)},
  MEMBER_MAX_RESULTS: {VAR_TYPE: TYPE_INTEGER, VAR_LIMITS: (1, 10000)},
  MESSAGE_BATCH_SIZE: {VAR_TYPE: TYPE_INTEGER, VAR_LIMITS: (1, 1000)},
  MESSAGE_MAX_RESULTS: {VAR_TYPE: TYPE_INTEGER, VAR_LIMITS: (1, 10000)},
  NEVER_TIME: {VAR_TYPE: TYPE_STRING, VAR_LIMITS: (0, None)},
  NO_BROWSER: {VAR_TYPE: TYPE_BOOLEAN, VAR_SIGFILE: u'nobrowser.txt', VAR_SFFT: (FALSE, TRUE)},
  NO_CACHE: {VAR_TYPE: TYPE_BOOLEAN, VAR_SIGFILE: u'nocache.txt', VAR_SFFT: (FALSE, TRUE)},
  NO_UPDATE_CHECK: {VAR_TYPE: TYPE_BOOLEAN, VAR_SIGFILE: u'noupdatecheck.txt', VAR_SFFT: (FALSE, TRUE)},
  NO_VERIFY_SSL: {VAR_TYPE: TYPE_BOOLEAN, VAR_SIGFILE: u'noverifyssl.txt', VAR_SFFT: (FALSE, TRUE)},
  NUM_TBATCH_THREADS: {VAR_TYPE: TYPE_INTEGER, VAR_LIMITS: (1, 100)},
  NUM_THREADS: {VAR_TYPE: TYPE_INTEGER, VAR_ENVVAR: u'GAM_THREADS', VAR_LIMITS: (1, 100)},
  OAUTH2_TXT: {VAR_TYPE: TYPE_FILE, VAR_ENVVAR: u'OAUTHFILE', VAR_ACCESS: os.R_OK | os.W_OK},
  OAUTH2SERVICE_JSON: {VAR_TYPE: TYPE_FILE, VAR_ENVVAR: u'OAUTHSERVICEFILE', VAR_ACCESS: os.R_OK},
  PRINT_NATIVE_NAMES: {VAR_TYPE: TYPE_BOOLEAN},
  SECTION: {VAR_TYPE: TYPE_STRING, VAR_LIMITS: (0, None)},
  SHOW_CONVERT_CR_NL: {VAR_TYPE: TYPE_BOOLEAN},
  SHOW_COUNTS_MIN: {VAR_TYPE: TYPE_INTEGER, VAR_LIMITS: (0, 100)},
  SHOW_GETTINGS: {VAR_TYPE: TYPE_BOOLEAN},
  SHOW_GETTINGS_GOT_NL: {VAR_TYPE: TYPE_BOOLEAN},
  SHOW_MULTIPROCESS_INFO: {VAR_TYPE: TYPE_BOOLEAN},
  TIMEZONE: {VAR_TYPE: TYPE_TIMEZONE},
  TODRIVE_CONVERSION: {VAR_TYPE: TYPE_BOOLEAN},
  TODRIVE_USER: {VAR_TYPE: TYPE_STRING, VAR_LIMITS: (0, None)},
  TODRIVE_PARENT: {VAR_TYPE: TYPE_STRING, VAR_LIMITS: (0, None)},
  TODRIVE_TIMESTAMP: {VAR_TYPE: TYPE_BOOLEAN},
  TODRIVE_LOCALCOPY: {VAR_TYPE: TYPE_BOOLEAN},
  USER_MAX_RESULTS: {VAR_TYPE: TYPE_INTEGER, VAR_ENVVAR: u'GAM_USER_MAX_RESULTS', VAR_LIMITS: (1, 500)},
  }
