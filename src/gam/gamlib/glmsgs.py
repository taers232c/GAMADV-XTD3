# -*- coding: utf-8 -*-

# Copyright (C) 2022 Ross Scroggs All Rights Reserved.
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

"""GAM messages

"""

# These values can be translated into other languages
# Project creation messages in order of appearance
CREATING_PROJECT = 'Creating project "{0}"...\n'
CHECK_INTERRUPTED = 'Check interrupted'
CHECKING_PROJECT_CREATION_STATUS = 'Checking project creation status...\n'
NO_RIGHTS_GOOGLE_CLOUD_ORGANIZATION = 'Looks like you have no rights to your Google Cloud Organization.\nAttempting to fix that...\n'
YOUR_ORGANIZATION_NAME_IS = 'Your organization name is {0}\n'
YOU_HAVE_NO_RIGHTS_TO_CREATE_PROJECTS_AND_YOU_ARE_NOT_A_SUPER_ADMIN = 'You have no rights to create projects for your organization and you don\'t seem to be a super admin! Sorry, there\'s nothing more I can do.'
LOOKS_LIKE_NO_ONE_HAS_RIGHTS_TO_YOUR_GOOGLE_CLOUD_ORGANIZATION_ATTEMPTING_TO_GIVE_YOU_CREATE_RIGHTS = 'Looks like no one has rights to your Google Cloud Organization. Attempting to give you create rights...\n'
THE_FOLLOWING_RIGHTS_SEEM_TO_EXIST = 'The following rights seem to exist:\n'
GIVING_LOGIN_HINT_THE_CREATOR_ROLE = 'Giving {0} the role of {1}...\n'
ACCEPT_CLOUD_TOS = '''Please go to:

https://console.cloud.google.com/start&authuser={0}

and accept the Terms of Service (ToS). As soon as you've accepted the ToS popup, you can return here and press enter.\n'''

PROJECT_STILL_BEING_CREATED_SLEEPING = 'Project still being created. Sleeping {0} seconds\n'
FAILED_TO_CREATE_PROJECT = 'Failed to create project: {0}\n'
SETTING_GAM_PROJECT_CONSENT_SCREEN = 'Setting GAM project consent screen...\n'
PLEASE_RESOLVE_ERROR = '\nPlease resolve error as described above\n\n'
PRESS_ENTER_ONCE_ERROR_RESOLVED = 'Press enter once error is resolved and we will try enabling the API again.'
CREATE_PROJECT_INSTRUCTIONS = '''Please go to:

{0}

1. Choose "Desktop App" or "Other" for "Application type".
2. Enter "GAM" or another desired value for "Name".
3. Click the blue "Create" button.
4. Copy your "client ID" value that shows on the next page.
'''
ENTER_YOUR_CLIENT_ID = '\nEnter your Client ID: '
GO_BACK_TO_YOUR_BROWSER_AND_COPY_YOUR_CLIENT_SECRET_VALUE = '\n5. Go back to your browser and copy your "client secret" value.\n'
ENTER_YOUR_CLIENT_SECRET = '\nEnter your Client Secret: '
GO_BACK_TO_YOUR_BROWSER_AND_CLICK_OK_TO_CLOSE_THE_OAUTH_CLIENT_POPUP = '\n6. Go back to your browser and click OK to close the "OAuth client" popup if it\'s still open.\n'
IS_NOT_A_VALID_CLIENT_ID = '''

{0}

Is not a valid client ID.

Please make sure you are following the directions exactly and that there are no extra spaces in your client ID.
'''
IS_NOT_A_VALID_CLIENT_SECRET = '''

{0}

Is not a valid client secret.

Please make sure you are following the directions exactly and that there are no extra spaces in your client secret.
'''
YOUR_GAM_PROJECT_IS_CREATED_AND_READY_TO_USE = 'That\'s it! Your GAM Project is created and ready to use.\n'

# check|update service messages in order of appearance
SYSTEM_TIME_STATUS = 'System time status'
YOUR_SYSTEM_TIME_DIFFERS_FROM_GOOGLE = 'Your system time differs from {0} by {1}'
PRESS_ENTER_ONCE_AUTHORIZATION_IS_COMPLETE = 'Press enter once authorization is complete.'
SERVICE_ACCOUNT_PRIVATE_KEY_AUTHENTICATION = 'Service Account Private Key Authentication'
SERVICE_ACCOUNT_CHECK_PRIVATE_KEY_AGE = 'Service Account Private Key age; Google recommends rotating keys on a routine basis'
SERVICE_ACCOUNT_PRIVATE_KEY_AGE = 'Service Account Private Key age: {0} days'
UPDATE_PROJECT_TO_VIEW_MANAGE_SAKEYS = 'Please run "gam update project" to view/manage service account keys'
DOMAIN_WIDE_DELEGATION_AUTHENTICATION = 'Domain-Wide Delegation authentication'
SCOPE_AUTHORIZATION_PASSED = '''All scopes PASSED!

Service Account Client name: {0} is fully authorized.
'''
SCOPE_AUTHORIZATION_UPDATE_PASSED = '''All scopes PASSED!
To authorize them (in case some scopes were unselected), please go to the following link in your browser:
{0}
    {1}

You will be directed to the Google Workspace admin console Security/API Controls/Domain-wide Delegation page
The "Add a new Client ID" box will open
Make sure that "Overwrite existing client ID" is checked
Click AUTHORIZE
When the box closes you're done
After authorizing it may take some time for this test to pass so wait a few moments and then try this command again.
'''
SCOPE_AUTHORIZATION_FAILED = '''Some scopes FAILED!
To authorize them, please go to the following link in your browser:
{0}
    {1}

You will be directed to the Google Workspace admin console Security/API Controls/Domain-wide Delegation page
The "Add a new Client ID" box will open
Make sure that "Overwrite existing client ID" is checked
Click AUTHORIZE
When the box closes you're done
After authorizing it may take some time for this test to pass so wait a few moments and then try this command again.
'''
# General messages
ACCESS_FORBIDDEN = 'Access Forbidden'
ACTION_APPLIED = 'Action Applied'
ACTION_IN_PROGRESS = 'Action {0} in progress'
ACTION_MAY_BE_DELAYED = 'Action may be delayed'
ADMIN_STATUS_CHANGED_TO = 'Admin Status Changed to'
ALL = 'All'
ALREADY_WAS_OWNER = 'Already was owner'
ALREADY_EXISTS = 'Already exists'
ALREADY_EXISTS_IN_TARGET_FOLDER = 'Already exists in {0}: {1}'
ALREADY_EXISTS_USE_MERGE_ARGUMENT = 'Already exists; use the "merge" argument to merge the labels'
API_ACCESS_DENIED = 'API access Denied'
API_CALLS_RETRY_DATA = 'API calls retry data\n'
API_CHECK_CLIENT_AUTHORIZATION = 'Please make sure the Client ID: {0} is authorized for the appropriate API or scopes:\n{1}\n\nRun: gam oauth create\n'
API_CHECK_SVCACCT_AUTHORIZATION = 'Please make sure the Service Account Client name: {0} is authorized for the appropriate API or scopes:\n{1}\n\nRun: gam user {2} check serviceaccount\n'
API_ERROR_SETTINGS = 'API error, some settings not set'
ARE_MUTUALLY_EXCLUSIVE = 'Arguments {0} and {1} are mutually exclusive'
AS = 'as'
ATTENDEES_ADD = 'Add Attendees'
ATTENDEES_ADD_REMOVE = 'Add/Remove Attendees'
ATTENDEES_REMOVE = 'Remove Attendees'
AUTHORIZATION_FILE_ALREADY_EXISTS = '{0} already exists. Please delete or rename it before attempting to {1} project.'
AUTHENTICATION_FLOW_COMPLETE = 'The authentication flow has completed. You may close this browser window and return to GAM.'
AUTHENTICATION_FLOW_FAILED = 'The authentication flow failed (invalid verification code entered?): {0}'
BAD_ENTITIES_IN_SOURCE = '{0} {1} {2} in source marked >>> <<< above'
BAD_REQUEST = 'Bad Request'
BATCH = 'Batch'
BATCH_CSV_LOOP_DASH_DEBUG_INCOMPATIBLE = '"gam {0} - ..." is not compatible with debugging. Disable debugging by setting debug_level = 0 in gam.cfg'
BATCH_NOT_PROCESSED_ERRORS = '{0}batch file: {1}, not processed, {2} {3}\n'
CAN_NOT_DELETE_USER_WITH_VAULT_HOLD = '{0}: The user may be (or have recently been) on Google Vault Hold and thus not eligible for deletion. You can check holds with "gam user {1} show vaultholds".'
CAN_NOT_BE_DOWNLOADED = 'Can not be downloaded'
CAN_NOT_BE_SPECIFIED_MORE_THAN_ONCE = 'Argument {0} can not be specified more than once'
COLUMN_DOES_NOT_MATCH_ANY_INPUT_COLUMNS = '{0} column "{1}" does not match any input columns'
COLUMN_DOES_NOT_MATCH_ANY_OUTPUT_COLUMNS = '{0} column "{1}" does not match any output columns'
COMMAND_NOT_COMPATIBLE_WITH_ENABLE_DASA = 'gam {0} {1} is not compatible with enable_dasa = true in gam.cfg'
COMMIT_BATCH_COMPLETE = '{0},0/{1},commit-batch - running {2} finished, proceeding\n'
COMMIT_BATCH_WAIT_N_PROCESSES = '{0},0/{1},commit-batch - waiting for {2} running {3} to finish before proceeding\n'
CONTACT_ADMINISTRATOR_FOR_PASSWORD = 'Contact administrator for password'
CONTACT_PHOTO_NOT_FOUND = 'Contact photo not found'
CONTAINS_AT_LEAST_1_ITEM = 'Contains at least 1 item'
COUNT_N_EXCEEDS_MAX_TO_PROCESS_M = 'Count {0} exceeds maximum to {1} {2}'
CORRUPT_FILE = 'Corrupt file'
CREATE_USER_NOTIFY_MESSAGE = 'Hello #givenname# #familyname#,\n\nYou have a new account at #domain#\nAccount details:\nUsername: #user#\nPassword: #password#\nStart using your new account by signing in at\nhttps://www.google.com/accounts/AccountChooser?Email=#user#&continue=https://apps.google.com/user/hub\n'
CREATE_USER_NOTIFY_SUBJECT = 'Welcome to #domain#'
CSV_DATA_ALREADY_SAVED = 'CSV data already saved'
CSV_FILE_HEADERS = 'The CSV file ({0}) has the following headers:\n'
CSV_SAMPLE_COMMANDS = 'Here are the first {0} commands {1} will run\n'
DATA_FIELD_MISMATCH = 'datafield {0} does not match saved datafield {1}'
DATA_UPLOADED_TO_DRIVE_FILE = 'Data uploaded to Drive File'
DEFAULT_SMIME = 'Default S/MIME'
DELETED = 'Deleted'
DIRECTLY_IN_THE = ' directly in the {0}'
DISABLE_TLS_MIN_MAX = 'Execute: gam select default config tls_max_version "" tls_min_version "" save\n'
DISPLAYNAME_NOT_ALLOWED_WHEN_UPDATING_MULTIPLE_SCHEMAS = 'displayname not allowed when updating multiple schemas'
DOES_NOT_EXIST = 'Does not exist'
DOES_NOT_EXIST_OR_HAS_INVALID_FORMAT = '{0}: {1}, Does not exist or has invalid format, {2}'
DOES_NOT_MATCH = 'Does not match {0}'
DOMAIN_NOT_FOUND_IN_DNS = 'Domain not found in DNS!'
DOMAIN_NOT_VERIFIED_SECONDARY = 'Domain is not a verified secondary domain'
DONE_GENERATING_PRIVATE_KEY_AND_PUBLIC_CERTIFICATE = 'Done generating private key and public certificate'
DO_NOT_EXIST = 'Do not exist'
DOWNLOADING_AGAIN_AND_OVER_WRITING = 'Downloading again and over-writing...'
DUPLICATE = 'Duplicate'
DUPLICATE_ALREADY_A_ROLE = 'Duplicate, already a {0}'
DYNAMIC_GROUP_MEMBERSHIP_CANNOT_BE_MODIFIED = 'Dynamic group membership cannot be modified'
EITHER = 'Either'
EMAIL_ADDRESS_IS_UNMANAGED_ACCOUNT = 'The email address is an ummanaged account'
ENTER_GSUITE_ADMIN_EMAIL_ADDRESS = '\nEnter your Google Workspace admin email address? '
ENTER_MANAGE_GCP_PROJECT_EMAIL_ADDRESS = '\nEnter your Google Workspace admin or GCP project manager email address authorized to manage project(s): {0}? '
ENTER_VERIFICATION_CODE = 'Enter verification code: '
ENTITY_DOES_NOT_EXIST = '{0} does not exist'
ENTITY_NAME_NOT_VALID = 'Entity Name Not Valid'
ERROR = 'error'
ERRORS = 'errors'
EVENT_IS_CANCELED = 'Event is canceled'
EXECUTE_GAM_OAUTH_CREATE = '\nPlease run\n\ngam oauth delete\ngam oauth create\n\n'
EXISTS = 'Exists'
EXPECTED = 'Expected'
EXPORT_NOT_COMPLETE = 'Export needs to be complete before downloading, current status is: {0}'
EXTRACTING_PUBLIC_CERTIFICATE = 'Extracting public certificate'
FAILED_TO_PARSE_AS_JSON = 'Failed to parse as JSON'
FAILED_TO_PARSE_AS_LIST = 'Failed to parse as list'
FIELD_NOT_FOUND_IN_SCHEMA = 'Field {0} not found in schema {1}'
FINISHED = 'Finished'
FILTER_CAN_ONLY_CONTAIN_ONE_CATEGORY_LABEL = 'Filter can only contain one CATEGORY label'
FILTER_CAN_ONLY_CONTAIN_ONE_USER_LABEL = 'Filter can only contain one USER label'
FOR = 'for'
FORBIDDEN = 'Forbidden'
FORMAT_NOT_AVAILABLE = 'Format ({0}) not available'
FORMAT_NOT_DOWNLOADABLE = 'Format not downloadable'
FROM = 'From'
GAM_LATEST_VERSION_NOT_AVAILABLE = 'GAM Latest Version information not available'
GAM_OUT_OF_MEMORY = 'GAM has run out of memory. If this is a large Google Workspace instance, you should use a 64-bit version of GAM on Windows or a 64-bit version of Python on other systems.'
GENERATING_NEW_PRIVATE_KEY = 'Generating new private key'
GETTING = 'Getting'
GETTING_ALL = 'Getting all'
GOOGLE_DELEGATION_ERROR = 'Google delegation error, delegator and delegate both exist and are valid for delegation'
GOT = 'Got'
GROUP_MAPS_TO_MULTIPLE_OUS = 'File: {0}, Group: {1} references multiple OUs: {2}'
GROUP_MAPS_TO_OU_INVALID_ROW = 'File: {0}, Invalid row, must contain non-blank <EmailAddress> and <OrgUnitPath>: <{1}> <{2}>'
GUARDIAN_INVITATION_STATUS_NOT_PENDING = 'Guardian invitation status is not PENDING'
HAS_CHILD_ORGS = 'Has child {0}'
HAS_INVALID_FORMAT = '{0}: {1}, Has invalid format'
HAS_RIGHTS_TO_ROTATE_OWN_PRIVATE_KEY = 'Giving account {0} rights to rotate {1} private key'
HEADER_NOT_FOUND_IN_CSV_HEADERS = 'Header "{0}" not found in CSV headers of "{1}".'
HELP_SYNTAX = 'Help: Syntax in file {0}\n'
HELP_WIKI = 'Help: Documentation is at {0}\n'
IGNORED = 'Ignored'
INSTRUCTIONS_CLIENT_SECRETS_JSON = 'Please run\n\ngam create|use project\ngam oauth create\n\nto create and authorize a Client account.\n'
INSTRUCTIONS_OAUTH2SERVICE_JSON = 'Please run\n\ngam create|use project\ngam user <user> check serviceaccount\n\nto create and authorize a Service account.\n'
INSUFFICIENT_PERMISSIONS_TO_PERFORM_TASK = 'Insufficient permissions to perform this task'
INTER_BATCH_WAIT_INCREASED = 'inter_batch_wait increased to {0:.2f}'
INVALID = 'Invalid'
INVALID_ALIAS = 'Invalid Alias'
INVALID_ATTENDEE_CHANGE = 'Invalid attendee change "{0}"'
INVALID_CHARSET = 'Invalid charset "{0}"'
INVALID_DATE_TIME_RANGE = '{0} {1} must be greater than/equal to {2} {3}'
INVALID_ENTITY = 'Invalid {0}, {1}'
INVALID_GROUP = 'Invalid Group'
INVALID_JSON_INFORMATION = 'Google API reported Invalid JSON Information'
INVALID_JSON_SETTING = 'Invalid JSON setting'
INVALID_LIST = 'Invalid list'
INVALID_MEMBER = 'Invalid Member address'
INVALID_MESSAGE_ID = 'Invalid message id(s)'
INVALID_MIMETYPE = 'Invalid mimeType {0}, must be {1}'
INVALID_ORGUNIT = 'Invalid Organizational Unit'
INVALID_PATH = 'Invalid Path'
INVALID_PERMISSION_ATTRIBUTE_TYPE = 'permission attribute {0} not allowed with type {1}'
INVALID_QUERY = 'Invalid Query'
INVALID_RE = 'Invalid RE'
INVALID_REQUEST = 'Invalid Request'
INVALID_ROLE = 'Invalid subkeyfield Role, must be one of: {0}'
INVALID_SCHEMA_VALUE = 'Invalid Schema Value'
INVALID_SCOPE = 'Invalid Scope'
INVALID_SITE = 'Invalid Site ({0}), must match pattern ({1})'
INVALID_TAG_SPECIFICATION = 'Invalid tag, expected field.subfield or field.subfield.subfield.string'
IN_SKIPIDS = 'In skipids'
IN_THE = ' in the {0}'
IN_TRASH_AND_EXCLUDE_TRASHED = 'In Trash and excludeTrashed'
IS_EXPIRED_OR_REVOKED = '{0}: {1}, Is expired or has been revoked'
IS_NOT_DONE_CHECKING_IN_SECONDS = 'Is not done, checking again in {0} seconds'
IS_NOT_UNIQUE = 'Is not unique, {0}: {1}'
IS_REQD_TO_CHG_PWD_NO_DELEGATION = 'Is required to change password at next login. You must change password or clear changepassword flag for delegation.'
IS_SUSPENDED_NO_DELEGATION = 'Is suspended. You must unsuspend for delegation.'
KIOSK_MODE_REQUIRED = ' This command ({0}) requires that the ChromeOS device be in Kiosk mode.'
LESS_THAN_1_SECOND = 'less than 1 second'
LIST_CHROMEOS_INVALID_INPUT_PAGE_TOKEN_RETRY = 'List ChromeOSdevices Invalid Input: pageToken retry'
LOGGING_INITIALIZATION_ERROR = 'Logging inititalization error: {0}'
LOOKING_UP_GOOGLE_UNIQUE_ID = 'Looking up Google Unique ID'
MARKED_AS = 'Marked as'
MATCHED_THE_FOLLOWING = 'Matched the following'
MATTER_NOT_OPEN = 'Matter needs to be open, current state is: {0}'
MAXIMUM_OF = 'maximum of'
MEMBERSHIP_IS_PENDING_WILL_DELETE_ADD_TO_ACCEPT = 'Membership is pending, will delete and add to accept'
MIMETYPE_MISMATCH = 'Shortcut target mimeType {0} does not match actual target mimeType {1}'
MISMATCH_RE_SEARCH_REPLACE_SUBFIELDS = 'The subfield ({2}) in replace "{3}" exceeds the number of subfields ({0}) in search "{1}"'
MISMATCH_SEARCH_REPLACE_SUBFIELDS = 'The number of subfields ({0}) in search "{1}" does not match the number of subfields ({2}) in replace "{3}"'
MISSING_FIELDS = 'Missing fields: {0}\n'
MULTIPLE_BUILDINGS_SAME_NAME = '{0} {1} with the same (case-insensitive) name exist'
MULTIPLE_ENTITIES_FOUND = 'Multiple {0} ({1}) found, {2}'
MULTIPLE_ITEMS_SPECIFIED = 'Multiple {0} are specfied, only one is allowed'
MULTIPLE_ITEMS_MARKED_PRIMARY = 'Multiple {0} are marked primary, only one can be primary'
MULTIPLE_PARENTS_SPECIFIED = 'Multiple parents ({0}) specified, only one is allowed'
MULTIPLE_SEARCH_METHODS_SPECIFIED = 'Multiple search methods ({0}) specified, only one is allowed'
MUST_BE_NUMERIC = 'Must be numeric'
NEED_READ_ACCESS = 'Need Read access'
NEED_READ_WRITE_ACCESS = 'Need Read/Write access'
NEED_WRITE_ACCESS = 'Need Write access'
NESTED_LOOP_CMD_NOT_ALLOWED = 'Command can not be nested.'
NEWUSER_REQUIREMENTS = 'newuser option requires: at least 1 recipient and givenname, familyname and password options'
NEW_OWNER_MUST_DIFFER_FROM_OLD_OWNER = 'New owner must differ from old owner'
NO_DATA = 'No data'
NON_BLANK = 'Non-blank'
NON_EMPTY = 'Non-empty'
NOT_A = 'Not a'
NOT_A_PRIMARY_EMAIL_ADDRESS = 'Not a primary email address'
NOT_ACTIVE = 'Not Active'
NOT_ALLOWED = 'Not Allowed'
NOT_AN_ENTITY = 'Not a {0}'
NOT_COMPATIBLE = 'Not compatible'
NOT_COPYABLE = 'Not Copyable'
NOT_COPYABLE_SAME_NAME_CURRENT_FOLDER_MERGE = 'Not copyable with same name into current folder with duplicatefolders merge'
NOT_COPYABLE_SAME_NAME_CURRENT_FOLDER_OVERWRITE = 'Not copyable with same name into current folder with duplicatefiles overwriteall|overwriteolder'
NOT_DELETABLE = 'Not deletable'
NOT_FOUND = 'Not Found'
NOT_MOVABLE = 'Not Movable'
NOT_MOVABLE_IN_TRASH = 'Not Movable, in Trash'
NOT_MOVABLE_SAME_NAME_CURRENT_FOLDER_MERGE = 'Not movable with same name into current folder with duplicatefolders merge'
NOT_MOVABLE_SAME_NAME_CURRENT_FOLDER_OVERWRITE = 'Not movable with same name into current folder with duplicatefiles overwriteall|overwriteolder'
NOT_OWNED_BY = 'Not owned by {0}'
NOT_WRITABLE = 'Not Writable'
NOW_THE_PRIMARY_DOMAIN = 'Now the primary domain'
NO_ACTION_SPECIFIED = 'No action specified'
NO_CHANGES = 'No changes'
NO_CLIENT_ACCESS_ALLOWED = 'No Client Access allowed'
NO_CLIENT_ACCESS_CREATE_UPDATE_ALLOWED = 'No Client Access create/update allowed'
NO_COLUMNS_SELECTED_WITH_CSV_OUTPUT_HEADER_FILTER = 'No columns selected with {0} and {1}'
NO_CSV_DATA_TO_UPLOAD = 'No CSV data to upload'
NO_CSV_FILE_DATA_FOUND = 'No CSV file data found'
NO_CSV_FILE_DATA_SAVED = 'No CSV file data saved'
NO_CSV_FILE_SUBKEYS_SAVED = 'No CSV file subkeys saved'
NO_DATA_TRANSFER_APP_FOR_PARAMETER = 'No data transfer application for key {0}'
NO_ENTITIES_FOUND = 'No {0} found'
NO_ENTITIES_MATCHED = 'No {0} matched'
NO_FILTER_ACTIONS = 'No {0} actions specified'
NO_FILTER_CRITERIA = 'No {0} criteria specified'
NO_LABELS_MATCH = 'No Labels match'
NO_MESSAGES_WITH_LABEL = 'No Messages with Label'
NO_PARENTS_TO_CONVERT_TO_SHORTCUTS = 'No parents to convert to shortcuts'
NO_REPORT_AVAILABLE = 'No {0} report available.'
NO_SCOPES_FOR_API = 'There are no scopes authorized for the {0}'
NO_SVCACCT_ACCESS_ALLOWED = 'No Service Account Access allowed'
NO_TRANSFER_LACK_OF_DISK_SPACE = 'Transfer not performed due to lack of target drive space.'
NO_USAGE_PARAMETERS_DATA_AVAILABLE = 'No usage parameters data available.'
NO_USER_COUNTS_DATA_AVAILABLE = 'No User counts data available.'
OAUTH2_BROWSER_OPENED_MESSAGE = """
Your browser has been opened to visit:

    {url}

If your browser is on a different machine then press CTRL+C,
set no_browser = true in gam.cfg and re-run this command.
"""
OAUTH2_GO_TO_LINK_MESSAGE = """
Go to the following link in your browser:

    {url}
"""
ON_CURRENT_PRIVATE_KEY = ' on current key'
ON_VAULT_HOLD = 'On Google Vault Hold'
ONLY_ADMINISTRATORS_CAN_PERFORM_SHARED_DRIVE_QUERIES = 'Only administrators can perform Shared Drive queries'
ONLY_ONE_DEVICE_SELECTION_ALLOWED = 'Only one device selection allowed, filter = "{0}"'
ONLY_ONE_JSON_RANGE_ALLOWED = 'Only one range/json allowed'
ONLY_ONE_OWNER_ALLOWED = 'Only one owner allowed'
OR = 'or'
PERMISSION_DENIED = 'The caller does not have permission'
PLEASE_CORRECT_YOUR_SYSTEM_TIME = 'Please correct your system time.'
PLEASE_SELECT_ENTITY_TO_PROCESS = '{0} {1} found, please select the correct one to {2} and specify with {3}'
PLEASE_SPECIFY_BUILDING_EXACT_CASE_NAME_OR_ID = 'Please specify building by exact case name or ID.'
PREVIEW_ONLY = 'Preview Only'
PRIMARY_EMAIL_DID_NOT_MATCH_PATTERN = 'primaryEmail address did not match pattern: {0}'
PROCESS = 'process'
PROCESSES = 'processes'
PROCESSING_ITEM_N = '{0},0,Processing item {1}/{2}\n'
PROFILE_PHOTO_NOT_FOUND = 'Profile photo not found'
REASON_ONLY_VALID_WITH_CONTENTRESTRICTIONS_READONLY_TRUE = 'reason only valid with contentrestrictions readonly true'
REAUTHENTICATION_IS_NEEDED = 'Reauthentication is needed, please run\n\ngam oauth create'
RECOMMEND_RUNNING_GAM_ROTATE_SAKEY = 'Recommend running "gam rotate sakey" to get a new key\n'
REFUSING_TO_DEPROVISION_DEVICES = 'Refusing to deprovision {0} devices because acknowledge_device_touch_requirement not specified.\nDeprovisioning a device means the device will have to be physically wiped and re-enrolled to be managed by your domain again.\nThis requires physical access to the device and is very time consuming to perform for each device.\nPlease add "acknowledge_device_touch_requirement" to the GAM command if you understand this and wish to proceed with the deprovision.\nPlease also be aware that deprovisioning can have an effect on your device license count.\nSee https://support.google.com/chrome/a/answer/3523633 for full details.'
REPLY_TO_CUSTOM_REQUIRES_EMAIL_ADDRESS = 'replyto REPLY_TO_CUSTOM requires customReplyTo <EmailAddress>'
REQUEST_COMPLETED_NO_FILES = 'Request completed but no results/files were returned, try requesting again'
REQUEST_NOT_COMPLETE = 'Request needs to be completed before downloading, current status is: {0}'
RESOURCE_CAPACITY_FLOOR_REQUIRED = 'Options "capacity <Number>" (<Number> > 0) and "floor <String>" required'
RESOURCE_FLOOR_REQUIRED = 'Option "floor <String>" required'
RESULTS_TOO_LARGE_FOR_GOOGLE_SPREADSHEET = 'Results are too large for Google Spreadsheets. Uploading as a regular CSV file.'
RETRIES_EXHAUSTED = 'Retries {0} exhausted'
ROLE_MUST_BE_ORGANIZER = 'Role must be organizer'
SCHEMA_WOULD_HAVE_NO_FIELDS = '{0} would have no {1}'
SELECTED = 'Selected'
SERVICE_NOT_APPLICABLE = 'Service not applicable/Does not exist'
SERVICE_NOT_APPLICABLE_THIS_ADDRESS = 'Service not applicable for this address: {0}'
STARTING_THREAD = 'Starting thread'
STATISTICS_COPY_FILE = 'Total: {0}, Copied: {1}, Duplicate: {2}, Copy Failed: {3}, Not copyable: {4}, Permissions Failed: {5}, Protected Ranges Failed: {6}'
STATISTICS_COPY_FOLDER = 'Total: {0}, Copied: {1}, Duplicate: {2}, Merged: {3}, Copy Failed: {4}, Not writable: {5}, Permissions Failed: {6}'
STATISTICS_MOVE_FILE = 'Total: {0}, Moved: {1}, Duplicate: {2}, Move Failed: {3}, Not movable: {4}'
STATISTICS_MOVE_FOLDER = 'Total: {0}, Moved: {1}, Duplicate: {2}, Merged: {3}, Move Failed: {4}, Not writable: {5}'
STATISTICS_USER_NOT_ORGANIZER = 'User not organizer: {0}'
STRING_LENGTH = 'string length'
SUBKEY_FIELD_MISMATCH = 'subkeyfield {0} does not match saved subkeyfield {1}'
SUBSCRIPTION_NOT_FOUND = 'Could not find subscription'
SUFFIX_NOT_ALLOWED_WITH_CUSTOMLANGUAGE = 'Suffix {0} not allowed with customLanguage {1}'
THREAD = 'thread'
THREADS = 'threads'
TO = 'To'
TO_SET_UP_GOOGLE_CHAT = """
To set up Google Chat for your API project, please go to:

    {0}

and complete all fields.
"""
TOTAL_ITEMS_IN_ENTITY = 'Total {0} in {1}'
TRIMMED_MESSAGE_FROM_LENGTH_TO_MAXIMUM = 'Trimmed message of length {0} to maximum length {1}'
UNABLE_TO_GET_PERMISSION_ID = 'Unable to get Permission ID for <{0}>'
UNABLE_TO_CREATE_NOT_FOUND_USER = 'Unable to create not found user, some required field (givenName, familyName, password/notfoundpassword) not present'
UNAVAILABLE = 'Unavailable'
UNKNOWN = 'Unknown'
UNKNOWN_API_OR_VERSION = 'Unknown Google API or version: ({0}), contact {1}'
UNRECOVERABLE_ERROR = 'Unrecoverable error'
UPDATE_ATTENDEE_CHANGES = 'Update attendee changes'
UPDATE_GAM_TO_64BIT = "You're running a 32-bit version of GAM on a 64-bit version of Windows, upgrade to a windows-x86_64 version of GAM"
UPDATE_USER_PASSWORD_CHANGE_NOTIFY_MESSAGE = 'The account password for #givenname# #familyname#, #user# has been changed to: #password#\n'
UPDATE_USER_PASSWORD_CHANGE_NOTIFY_SUBJECT = 'Account #user# password has been changed'
UPLOADING_NEW_PUBLIC_CERTIFICATE_TO_GOOGLE = 'Uploading new public certificate to Google...\n'
USED = 'Used'
USER_BELONGS_TO_N_GROUPS_THAT_MAP_TO_ORGUNITS = 'User belongs to {0} groups ({1}) that map to OUs'
USER_CANCELLED = 'User cancelled'
USER_HAS_MULTIPLE_DIRECT_OR_INHERITED_MEMBERSHIPS_IN_GROUP = 'User has multiple direct or inherited memberships in group'
USER_IN_OTHER_DOMAIN = '{0}: {1} in other domain.'
USER_IS_NOT_ORGANIZER = 'User is not organizer, use anyorganizer option to override'
USER_NOT_IN_MATCHUSERS = 'User not in matchusers'
USER_SUBS_NOT_ALLOWED_TAG_REPLACEMENT = 'user substitutions not allowed in replace <Tag> <String>'
USE_DOIT_ARGUMENT_TO_PERFORM_ACTION = 'Use the "doit" argument to perform action'
USING_N_PROCESSES = '{0},0/{1},Using {2} {3}...\n'
VALUES_ARE_NOT_CONSISTENT = 'Values are not consistent'
VERSION_UPDATE_AVAILABLE = 'Version update available'
WAITING_FOR_SERVICE_ACCOUNT_CREATION_TO_COMPLETE_SLEEPING = 'Waiting for Service Account creation to complete. Sleeping {0} seconds\n'
WILL_RERUN_WITH_NO_BROWSER_TRUE = 'Will re-run command with no_browser true\n'
WITH = 'with'
WOULD_MAKE_MEMBERSHIP_CYCLE = 'Would make membership cycle'
YOU_CAN_ADD_DOMAIN_TO_ACCOUNT = 'You can now add: {0} or it\'s subdomains as secondary or domain aliases of the Google Workspace Account: {1}'
