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

"""GAM global variables

"""

import os

# The following GM_XXX constants are arbitrary but must be unique
# Most errors print a message and bail out with a return code
# Some commands want to set a non-zero return code but not bail
SYSEXITRC = u'sxrc'
# Process ID
PID = u'pid '
# Path to gam
GAM_PATH = u'gpth'
# Are we on Windows?
WINDOWS = u'wndo'
# Encodings
SYS_ENCODING = u'syen'
# Extra arguments to pass to GAPI functions
EXTRA_ARGS_LIST = u'exad'
# GAM admin user
ADMIN = u'admin'
# Current API user
CURRENT_API_USER = u'capu'
# Current API scope
CURRENT_API_SCOPES = u'scoc'
# Values retrieved from oauth2service.json
OAUTH2SERVICE_JSON_DATA = u'oajd'
OAUTH2_CLIENT_ID = u'oaci'
# gam.cfg parser
PARSER = u'pars'
# gam.cfg file
GAM_CFG_PATH = u'gcpa'
GAM_CFG_FILE = u'gcfi'
# redirected file: name, mode, encoding, delimiter, quotechar, write header, multiproces, queue
STDOUT = u'stdo'
STDERR = u'stde'
CSVFILE = u'csvf'
SAVED_STDOUT = u'svso'
REDIRECT_NAME = u'rdfn'
REDIRECT_MODE = u'rdmo'
REDIRECT_FD = u'rdfd'
REDIRECT_MULTI_FD = u'rdmf'
REDIRECT_ENCODING = u'rden'
REDIRECT_COLUMN_DELIMITER = u'rddl'
REDIRECT_QUOTE_CHAR = u'rdqc'
REDIRECT_WRITE_HEADER = u'rdwh'
REDIRECT_MULTIPROCESS = u'rdmp'
REDIRECT_QUEUE = u'rdqu'
REDIRECT_QUEUE_NAME = u'name'
REDIRECT_QUEUE_TODRIVE = u'todrive'
REDIRECT_QUEUE_TITLES = u'titles'
REDIRECT_QUEUE_DATA = u'rows'
REDIRECT_QUEUE_ARGS = u'args'
REDIRECT_QUEUE_GLOBALS = u'globals'
REDIRECT_QUEUE_VALUES = u'values'
REDIRECT_QUEUE_START = u'start'
REDIRECT_QUEUE_END = u'end'
REDIRECT_QUEUE_EOF = u'eof'
# File containing time of last GAM update check
LAST_UPDATE_CHECK_TXT = u'lupc'
# Index of start of <UserTypeEntity> in command line
ENTITY_CL_START = u'ecls'
ENTITY_CL_DELAY_START = u'eclD'
# csvfile keyfield <FieldName> [delimiter <Character>] (matchfield <FieldName> <MatchPattern>)* [datafield <FieldName>(:<FieldName>*) [delimiter <String>]]
# { key: [datafieldvalues]}
CSV_DATA_DICT = u'csdd'
CSV_KEY_FIELD = u'cskf'
CSV_SUBKEY_FIELD = u'cssk'
CSV_DATA_FIELD = u'csdf'
# Dictionary mapping OrgUnit ID to Name
MAP_ORGUNIT_ID_TO_NAME = u'oi2n'
# Dictionary mapping Role ID to Name
MAP_ROLE_ID_TO_NAME = u'ri2n'
# Dictionary mapping Role Name to ID
MAP_ROLE_NAME_TO_ID = u'rn2i'
# Dictionary mapping User ID to Name
MAP_USER_ID_TO_NAME = u'ui2n'
# oauth2.txt.lock lockfile
OAUTH2_TXT_LOCK = u'oalk'
# GAM cache directory. If no_cache is True, this variable will be set to None
CACHE_DIR = u'gacd'
# Reset GAM cache directory after discovery
CACHE_DISCOVERY_ONLY = u'gcdo'
# Shared by threadBatchWorker and threadBatchGAMCommands
TBATCH_QUEUE = u'batq'
# Location of cacerts.txt for GData calls
CACERTS_TXT = u'cert'
# datetime.datetime.now
DATETIME_NOW = u'dtno'
# Convert to local time
CONVERT_TO_LOCAL_TIME = u'ctlt'
#
Globals = {
  SYSEXITRC: 0,
  PID: 0,
  GAM_PATH: u'.',
  WINDOWS: os.name == u'nt',
  SYS_ENCODING: u'utf-8',
  EXTRA_ARGS_LIST: [],
  ADMIN: None,
  CURRENT_API_USER: None,
  CURRENT_API_SCOPES: [],
  OAUTH2SERVICE_JSON_DATA: None,
  OAUTH2_CLIENT_ID: None,
  PARSER: None,
  GAM_CFG_PATH: u'',
  GAM_CFG_FILE: u'',
  STDOUT: {},
  STDERR: {},
  CSVFILE: {},
  SAVED_STDOUT: None,
  LAST_UPDATE_CHECK_TXT: u'',
  ENTITY_CL_START: 1,
  ENTITY_CL_DELAY_START: 1,
  CSV_DATA_DICT: {},
  CSV_KEY_FIELD: None,
  CSV_SUBKEY_FIELD: None,
  CSV_DATA_FIELD: None,
  MAP_ORGUNIT_ID_TO_NAME: None,
  MAP_ROLE_ID_TO_NAME: None,
  MAP_ROLE_NAME_TO_ID: None,
  MAP_USER_ID_TO_NAME: None,
  OAUTH2_TXT_LOCK: None,
  CACHE_DIR: None,
  CACHE_DISCOVERY_ONLY: True,
  TBATCH_QUEUE: None,
  CACERTS_TXT: None,
  DATETIME_NOW: None,
  CONVERT_TO_LOCAL_TIME: False,
  }
