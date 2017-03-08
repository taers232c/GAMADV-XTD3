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

TRUE = 'true'
FALSE = 'false'
DEFAULT_CHARSET = 'utf-8'
MY_CUSTOMER = 'my_customer'

FN_CLIENT_SECRETS_JSON = 'client_secrets.json'
FN_EXTRA_ARGS_TXT = 'extra-args.txt'
FN_OAUTH2SERVICE_JSON = 'oauth2service.json'
FN_OAUTH2_TXT = 'oauth2.txt'

# Global variables defined in gam.cfg

# The following XXX constants are the names of the items in gam.cfg
# When retrieving lists of Google Drive activities from API, how many should be retrieved in each chunk
ACTIVITY_MAX_RESULTS = 'activity_max_results'
# Automatically generate gam batch command if number of users specified in gam users xxx command exceeds this number
# Default: 0, don't automatically generate gam batch commands
AUTO_BATCH_MIN = 'auto_batch_min'
# When processing items in batches, how many should be processed in each batch
BATCH_SIZE = 'batch_size'
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
# Convert newlines in text fields to "\n" in CSV output file
CSV_OUTPUT_CONVERT_CR_NL = 'csv_output_convert_cr_nl'
# Column delimiter in CSV output file
CSV_OUTPUT_COLUMN_DELIMITER = 'csv_output_column_delimiter'
# Field list delimiter in CSV output file
CSV_OUTPUT_FIELD_DELIMITER = 'csv_output_field_delimiter'
# custmerId from gam.cfg or retrieved from Google
CUSTOMER_ID = 'customer_id'
# If debug_level > 0: extra_args[u'prettyPrint'] = True, httplib2.debuglevel = gam_debug_level, appsObj.debug = True
DEBUG_LEVEL = 'debug_level'
# When retrieving lists of ChromeOS/Mobile devices from API, how many should be retrieved in each chunk
DEVICE_MAX_RESULTS = 'device_max_results'
# Domain obtained from gam.cfg or oauth2.txt
DOMAIN = 'domain'
# Google Drive download directory
DRIVE_DIR = 'drive_dir'
# When retrieving lists of Drive files/folders from API, how many should be retrieved in each chunk
DRIVE_MAX_RESULTS = 'drive_max_results'
# When processing email messages in batches, how many should be processed in each batch
EMAIL_BATCH_SIZE = 'email_batch_size'
# Path to extra_args.txt
EXTRA_ARGS = 'extra_args'
# When retrieving lists of Google Group members from API, how many should be retrieved in each chunk
MEMBER_MAX_RESULTS = 'member_max_results'
# When deleting or modifying Gmail messages, how many should be processed in each batch
MESSAGE_BATCH_SIZE = 'message_batch_size'
# When retrieving lists of Gmail messages from API, how many should be retrieved in each chunk
MESSAGE_MAX_RESULTS = 'message_max_results'
# If no_browser is False, writeCSVfile won't open a browser when todrive is set
# and doOAuthRequest prints a link and waits for the verification code when oauth2.txt is being created
NO_BROWSER = 'no_browser'
# Disable GAM API caching
NO_CACHE = 'no_cache'
# Disable GAM update check
NO_UPDATE_CHECK = 'no_update_check'
# Disable SSL certificate validation
NO_VERIFY_SSL = 'no_verify_ssl'
# Number of threads for gam batch
NUM_THREADS = 'num_threads'
# Path to oauth2.txt
OAUTH2_TXT = 'oauth2_txt'
# Path to oauth2service.json
OAUTH2SERVICE_JSON = 'oauth2service_json'
# Default section to use for processing
SECTION = 'section'
# Convert newlines in text fields to "\n" in show commands
SHOW_CONVERT_CR_NL = 'show_convert_cr_nl'
# Add (n/m) to end of messages if number of items to be processed exceeds this number
SHOW_COUNTS_MIN = 'show_counts_min'
# Enable/disable "Getting ... " messages
SHOW_GETTINGS = 'show_gettings'
# Enable/disable showing multiprocess info in redirected stdout/stderr
SHOW_MULTIPROCESS_INFO = 'show_multiprocess_info'
# Time Zone
TIMEZONE = 'timezone'
# Enable conversion to Google Sheets when uploading todrive files
TODRIVE_CONVERSION = 'todrive_conversion'
# User for todrive files
TODRIVE_USER = 'todrive_user'
# ID/Name of parent folder for todrive files
TODRIVE_PARENT = 'todrive_parent'
# Append timestamp to todrive file name
TODRIVE_TIMESTAMP = 'todrive_timestamp'
# When retrieving lists of Users from API, how many should be retrieved in each chunk
USER_MAX_RESULTS = 'user_max_results'

Defaults = {
  ACTIVITY_MAX_RESULTS: 100,
  AUTO_BATCH_MIN: 0,
  BATCH_SIZE: 50,
  CACHE_DIR: '',
  CACHE_DISCOVERY_ONLY: TRUE,
  CHARSET: DEFAULT_CHARSET,
  CLASSROOM_MAX_RESULTS: 0,
  CLIENT_SECRETS_JSON: FN_CLIENT_SECRETS_JSON,
  CONFIG_DIR: '',
  CONTACT_MAX_RESULTS: 100,
  CSV_INPUT_COLUMN_DELIMITER: ',',
  CSV_OUTPUT_CONVERT_CR_NL: FALSE,
  CSV_OUTPUT_COLUMN_DELIMITER: ',',
  CSV_OUTPUT_FIELD_DELIMITER: "' '",
  CUSTOMER_ID: MY_CUSTOMER,
  DEBUG_LEVEL: 0,
  DEVICE_MAX_RESULTS: 500,
  DOMAIN: '',
  DRIVE_DIR: '',
  DRIVE_MAX_RESULTS: 1000,
  EMAIL_BATCH_SIZE: 100,
  EXTRA_ARGS: '',
  MEMBER_MAX_RESULTS: 200,
  MESSAGE_BATCH_SIZE: 1000,
  MESSAGE_MAX_RESULTS: 1000,
  NO_BROWSER: FALSE,
  NO_CACHE: FALSE,
  NO_UPDATE_CHECK: FALSE,
  NO_VERIFY_SSL: FALSE,
  NUM_THREADS: 25,
  OAUTH2_TXT: FN_OAUTH2_TXT,
  OAUTH2SERVICE_JSON: FN_OAUTH2SERVICE_JSON,
  SECTION: '',
  SHOW_CONVERT_CR_NL: FALSE,
  SHOW_COUNTS_MIN: 1,
  SHOW_GETTINGS: TRUE,
  SHOW_MULTIPROCESS_INFO: FALSE,
  TIMEZONE: 'utc',
  TODRIVE_CONVERSION: TRUE,
  TODRIVE_USER: '',
  TODRIVE_PARENT: 'root',
  TODRIVE_TIMESTAMP: FALSE,
  USER_MAX_RESULTS: 500,
  }

Values = {DEBUG_LEVEL: 0}

TYPE_BOOLEAN = 'bool'
TYPE_CHOICE = 'choi'
TYPE_DATETIME = 'datm'
TYPE_DIRECTORY = 'dire'
TYPE_EMAIL = 'emai'
TYPE_FILE = 'file'
TYPE_INTEGER = 'inte'
TYPE_LANGUAGE = 'lang'
TYPE_STRING = 'stri'
TYPE_TIMEZONE = 'tmzn'

VAR_TYPE = 'type'
VAR_ENVVAR = 'enva'
VAR_LIMITS = 'lmit'
VAR_SFFT = 'sfft'
VAR_SIGFILE = 'sigf'

VAR_INFO = {
  ACTIVITY_MAX_RESULTS: {VAR_TYPE: TYPE_INTEGER, VAR_ENVVAR: 'GAM_ACTIVITY_MAX_RESULTS', VAR_LIMITS: (1, 500)},
  AUTO_BATCH_MIN: {VAR_TYPE: TYPE_INTEGER, VAR_ENVVAR: 'GAM_AUTOBATCH', VAR_LIMITS: (0, None)},
  BATCH_SIZE: {VAR_TYPE: TYPE_INTEGER, VAR_ENVVAR: 'GAM_BATCH_SIZE', VAR_LIMITS: (1, 1000)},
  CACHE_DIR: {VAR_TYPE: TYPE_DIRECTORY, VAR_ENVVAR: 'GAMCACHEDIR'},
  CACHE_DISCOVERY_ONLY: {VAR_TYPE: TYPE_BOOLEAN, VAR_SIGFILE: 'allcache.txt', VAR_SFFT: (TRUE, FALSE)},
  CHARSET: {VAR_TYPE: TYPE_STRING, VAR_ENVVAR: 'GAM_CHARSET', VAR_LIMITS: (1, None)},
  CLASSROOM_MAX_RESULTS: {VAR_TYPE: TYPE_INTEGER, VAR_ENVVAR: 'GAM_CLASSROOM_MAX_RESULTS', VAR_LIMITS: (0, 1000)},
  CLIENT_SECRETS_JSON: {VAR_TYPE: TYPE_FILE, VAR_ENVVAR: 'CLIENTSECRETS'},
  CONFIG_DIR: {VAR_TYPE: TYPE_DIRECTORY, VAR_ENVVAR: 'GAMUSERCONFIGDIR'},
  CONTACT_MAX_RESULTS: {VAR_TYPE: TYPE_INTEGER, VAR_ENVVAR: 'GAM_CONTACT_MAX_RESULTS', VAR_LIMITS: (1, 10000)},
  CSV_INPUT_COLUMN_DELIMITER: {VAR_TYPE: TYPE_STRING, VAR_ENVVAR: 'GAM_CSV_INPUT_COLUMN_DELIMITER', VAR_LIMITS: (1, 1)},
  CSV_OUTPUT_CONVERT_CR_NL: {VAR_TYPE: TYPE_BOOLEAN, VAR_ENVVAR: 'GAM_CSV_OUTPUT_CONVERT_CR_NL', VAR_SFFT: (FALSE, TRUE)},
  CSV_OUTPUT_COLUMN_DELIMITER: {VAR_TYPE: TYPE_STRING, VAR_ENVVAR: 'GAM_CSV_OUTPUT_COLUMN_DELIMITER', VAR_LIMITS: (1, 1)},
  CSV_OUTPUT_FIELD_DELIMITER: {VAR_TYPE: TYPE_STRING, VAR_ENVVAR: 'GAM_CSV_OUTPUT_FIELD_DELIMITER', VAR_LIMITS: (1, 1)},
  CUSTOMER_ID: {VAR_TYPE: TYPE_STRING, VAR_ENVVAR: 'CUSTOMER_ID', VAR_LIMITS: (0, None)},
  DEBUG_LEVEL: {VAR_TYPE: TYPE_INTEGER, VAR_SIGFILE: 'debug.gam', VAR_LIMITS: (0, None), VAR_SFFT: ('0', '4')},
  DEVICE_MAX_RESULTS: {VAR_TYPE: TYPE_INTEGER, VAR_ENVVAR: 'GAM_DEVICE_MAX_RESULTS', VAR_LIMITS: (1, 1000)},
  DOMAIN: {VAR_TYPE: TYPE_STRING, VAR_ENVVAR: 'GA_DOMAIN', VAR_LIMITS: (0, None)},
  DRIVE_DIR: {VAR_TYPE: TYPE_DIRECTORY, VAR_ENVVAR: 'GAMDRIVEDIR'},
  DRIVE_MAX_RESULTS: {VAR_TYPE: TYPE_INTEGER, VAR_ENVVAR: 'GAM_DRIVE_MAX_RESULTS', VAR_LIMITS: (1, 1000)},
  EMAIL_BATCH_SIZE: {VAR_TYPE: TYPE_INTEGER, VAR_ENVVAR: 'GAM_EMAIL_BATCH_SIZE', VAR_LIMITS: (1, 100)},
  EXTRA_ARGS: {VAR_TYPE: TYPE_FILE, VAR_SIGFILE: FN_EXTRA_ARGS_TXT, VAR_SFFT: ('', FN_EXTRA_ARGS_TXT)},
  MEMBER_MAX_RESULTS: {VAR_TYPE: TYPE_INTEGER, VAR_ENVVAR: 'GAM_MEMBER_MAX_RESULTS', VAR_LIMITS: (1, 10000)},
  MESSAGE_BATCH_SIZE: {VAR_TYPE: TYPE_INTEGER, VAR_ENVVAR: 'GAM_MESSAGE_BATCH_SIZE', VAR_LIMITS: (1, 1000)},
  MESSAGE_MAX_RESULTS: {VAR_TYPE: TYPE_INTEGER, VAR_ENVVAR: 'GAM_MESSAGE_MAX_RESULTS', VAR_LIMITS: (1, 10000)},
  NO_BROWSER: {VAR_TYPE: TYPE_BOOLEAN, VAR_SIGFILE: 'nobrowser.txt', VAR_SFFT: (FALSE, TRUE)},
  NO_CACHE: {VAR_TYPE: TYPE_BOOLEAN, VAR_SIGFILE: 'nocache.txt', VAR_SFFT: (FALSE, TRUE)},
  NO_UPDATE_CHECK: {VAR_TYPE: TYPE_BOOLEAN, VAR_SIGFILE: 'noupdatecheck.txt', VAR_SFFT: (FALSE, TRUE)},
  NO_VERIFY_SSL: {VAR_TYPE: TYPE_BOOLEAN, VAR_SIGFILE: 'noverifyssl.txt', VAR_SFFT: (FALSE, TRUE)},
  NUM_THREADS: {VAR_TYPE: TYPE_INTEGER, VAR_ENVVAR: 'GAM_THREADS', VAR_LIMITS: (1, None)},
  OAUTH2_TXT: {VAR_TYPE: TYPE_FILE, VAR_ENVVAR: 'OAUTHFILE'},
  OAUTH2SERVICE_JSON: {VAR_TYPE: TYPE_FILE, VAR_ENVVAR: 'OAUTHSERVICEFILE'},
  SECTION: {VAR_TYPE: TYPE_STRING, VAR_ENVVAR: 'GAM_SECTION'}, VAR_LIMITS: (0, None),
  SHOW_CONVERT_CR_NL: {VAR_TYPE: TYPE_BOOLEAN, VAR_ENVVAR: 'GAM_SHOW_CONVERT_CR_NL', VAR_SFFT: (FALSE, TRUE)},
  SHOW_COUNTS_MIN: {VAR_TYPE: TYPE_INTEGER, VAR_ENVVAR: 'GAM_SHOW_COUNTS_MIN', VAR_LIMITS: (0, None)},
  SHOW_GETTINGS: {VAR_TYPE: TYPE_BOOLEAN, VAR_ENVVAR: 'GAM_SHOW_GETTINGS'},
  SHOW_MULTIPROCESS_INFO: {VAR_TYPE: TYPE_BOOLEAN, VAR_ENVVAR: 'GAM_SHOW_MULTI_INFO'},
  TIMEZONE: {VAR_TYPE: TYPE_TIMEZONE, VAR_ENVVAR: 'GAM_TIMEZONE'},
  TODRIVE_CONVERSION: {VAR_TYPE: TYPE_BOOLEAN, VAR_ENVVAR: 'GAM_TODRIVE_CONVERSION'},
  TODRIVE_USER: {VAR_TYPE: TYPE_STRING, VAR_ENVVAR: 'GAM_TODRIVE_USER', VAR_LIMITS: (0, None)},
  TODRIVE_PARENT: {VAR_TYPE: TYPE_STRING, VAR_ENVVAR: 'GAM_TODRIVE_PARENT', VAR_LIMITS: (0, None)},
  TODRIVE_TIMESTAMP: {VAR_TYPE: TYPE_BOOLEAN, VAR_ENVVAR: 'GAM_TODRIVE_TIMESTAMP'},
  USER_MAX_RESULTS: {VAR_TYPE: TYPE_INTEGER, VAR_ENVVAR: 'GAM_USER_MAX_RESULTS', VAR_LIMITS: (1, 500)},
  }
