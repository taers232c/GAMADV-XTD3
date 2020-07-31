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

"""Google API resources

"""
# APIs
ALERTCENTER = 'alertcenter'
CALENDAR = 'calendar'
CHAT = 'chat'
CLASSROOM = 'classroom'
CLOUDIDENTITY_DEVICES = 'cloudidentitydevices'
CLOUDIDENTITY_GROUPS = 'cloudidentitygroups'
CLOUDPRINT = 'cloudprint'
CLOUDRESOURCEMANAGER_V1 = 'cloudresourcemanager1'
CLOUDRESOURCEMANAGER_V2 = 'cloudresourcemanager2'
CONTACTS = 'contacts'
DATATRANSFER = 'datatransfer'
DIRECTORY = 'directory'
DRIVE2 = 'drive2'
DRIVE3 = 'drive3'
DRIVETD = 'drivetd'
DRIVEACTIVITY_V1 = 'appsactivity'
DRIVEACTIVITY_V2 = 'driveactivity'
EMAIL_AUDIT = 'email-audit'
GMAIL = 'gmail'
GROUPSMIGRATION = 'groupsmigration'
GROUPSSETTINGS = 'groupssettings'
IAM = 'iam'
IAP = 'iap'
LICENSING = 'licensing'
OAUTH2 = 'oauth2'
PEOPLE = 'people'
PUBSUB = 'pubsub'
REPORTS = 'reports'
RESELLER = 'reseller'
SERVICEMANAGEMENT = 'servicemanagement'
SERVICEUSAGE = 'serviceusage'
SHEETS = 'sheets'
SHEETSTD = 'sheetstd'
SITES = 'sites'
SITEVERIFICATION = 'siteVerification'
STORAGE = 'storage'
VAULT = 'vault'
#
GAM_SCOPES = 'gam'
FAM1_SCOPES = 'fam1'
FAM2_SCOPES = 'fam2'
FAM_LIST = [FAM1_SCOPES, FAM2_SCOPES]
#
DRIVE_SCOPE = 'https://www.googleapis.com/auth/drive'
GMAIL_SEND_SCOPE = 'https://www.googleapis.com/auth/gmail.send'
USERINFO_EMAIL_SCOPE = 'https://www.googleapis.com/auth/userinfo.email' # email
USERINFO_PROFILE_SCOPE = 'https://www.googleapis.com/auth/userinfo.profile' # profile
VAULT_SCOPES = ['https://www.googleapis.com/auth/ediscovery', 'https://www.googleapis.com/auth/ediscovery.readonly']
REQUIRED_SCOPES = ['email', 'profile']
REQUIRED_SCOPES_SET = set(REQUIRED_SCOPES)
#
REFRESH_PERM_ERRORS = [
  'invalid_grant: reauth related error (rapt_required)', # no way to reauth today
  'invalid_grant: Token has been expired or revoked.',
  ]

OAUTH2_TOKEN_ERRORS = [
  'access_denied',
  'access_denied: Requested client not authorized',
  'internal_failure: Backend Error',
  'internal_failure: None',
  'invalid_grant',
  'invalid_grant: Bad Request',
  'invalid_grant: Invalid email or User ID',
  'invalid_grant: Not a valid email',
  'invalid_grant: Invalid JWT: No valid verifier found for issuer',
  'invalid_grant: reauth related error (invalid_rapt)',
  'invalid_grant: The account has been deleted',
  'invalid_request: Invalid impersonation prn email address',
  'invalid_request: Invalid impersonation &quot;sub&quot; field',
  'unauthorized_client: Client is unauthorized to retrieve access tokens using this method',
  'unauthorized_client: Client is unauthorized to retrieve access tokens using this method, or client not authorized for any of the scopes requested',
  'unauthorized_client: Unauthorized client or scope in request',
  ]

PROJECT_APIS = [
  'admin.googleapis.com',
  'alertcenter.googleapis.com',
  'appsactivity.googleapis.com',
  'audit.googleapis.com',
  'calendar-json.googleapis.com',
  'chat.googleapis.com',
  'classroom.googleapis.com',
  'cloudidentity.googleapis.com',
  'cloudresourcemanager.googleapis.com',
  'contacts.googleapis.com',
  'drive.googleapis.com',
  'driveactivity.googleapis.com',
  'gmail.googleapis.com',
  'groupsmigration.googleapis.com',
  'groupssettings.googleapis.com',
  'iam.googleapis.com',
  'iap.googleapis.com',
  'licensing.googleapis.com',
  'people.googleapis.com',
  'pubsub.googleapis.com',
  'reseller.googleapis.com',
  'sheets.googleapis.com',
  'siteverification.googleapis.com',
  'storage-api.googleapis.com',
  'vault.googleapis.com',
  ]

_INFO = {
  ALERTCENTER: {'name': 'AlertCenter API', 'version': 'v1beta1', 'v2discovery': True},
  CALENDAR: {'name': 'Calendar API', 'version': 'v3', 'v2discovery': False},
  CLASSROOM: {'name': 'Classroom API', 'version': 'v1', 'v2discovery': True},
  CLOUDIDENTITY_DEVICES: {'name': 'Cloud Identity Devices API', 'version': 'v1beta1', 'v2discovery': True, 'mappedAPI': 'cloudidentity'},
  CLOUDIDENTITY_GROUPS: {'name': 'Cloud Identity Groups API', 'version': 'v1beta1', 'v2discovery': True, 'mappedAPI': 'cloudidentity'},
  CLOUDPRINT: {'name': 'Cloudprint API', 'version': 'v2', 'v2discovery': True, 'localjson': True},
  CLOUDRESOURCEMANAGER_V1: {'name': 'Cloud Resource Manager API v1', 'version': 'v1', 'v2discovery': True, 'mappedAPI': 'cloudresourcemanager'},
  CLOUDRESOURCEMANAGER_V2: {'name': 'Cloud Resource Manager API v2', 'version': 'v2', 'v2discovery': True, 'mappedAPI': 'cloudresourcemanager'},
  CONTACTS: {'name': 'Contacts API', 'version': 'v3', 'v2discovery': False},
  DATATRANSFER: {'name': 'Data Transfer API', 'version': 'datatransfer_v1', 'v2discovery': False, 'mappedAPI': 'admin'},
  DIRECTORY: {'name': 'Directory API', 'version': 'directory_v1', 'v2discovery': False, 'mappedAPI': 'admin'},
  DRIVE2: {'name': 'Drive API v2', 'version': 'v2', 'v2discovery': False, 'mappedAPI': 'drive'},
  DRIVE3: {'name': 'Drive API v3', 'version': 'v3', 'v2discovery': False, 'mappedAPI': 'drive'},
  DRIVETD: {'name': 'Drive API v3 - todrive', 'version': 'v3', 'v2discovery': False, 'mappedAPI': 'drive'},
  DRIVEACTIVITY_V1: {'name': 'Drive Activity API v1', 'version': 'v1', 'v2discovery': False},
  DRIVEACTIVITY_V2: {'name': 'Drive Activity API v2', 'version': 'v2', 'v2discovery': True},
  EMAIL_AUDIT: {'name': 'Email Audit API', 'version': 'v1', 'v2discovery': False},
  GMAIL: {'name': 'Gmail API', 'version': 'v1', 'v2discovery': False},
  GROUPSMIGRATION: {'name': 'Groups Migration API', 'version': 'v1', 'v2discovery': False},
  GROUPSSETTINGS: {'name': 'Groups Settings API', 'version': 'v1', 'v2discovery': False},
  IAM: {'name': 'Identity and Access Management API', 'version': 'v1', 'v2discovery': True},
  IAP: {'name': 'Cloud Identity-Aware Proxy API', 'version': 'v1', 'v2discovery': True},
  LICENSING: {'name': 'License Manager API', 'version': 'v1', 'v2discovery': False},
  OAUTH2: {'name': 'OAuth2 API', 'version': 'v2', 'v2discovery': False},
  PEOPLE: {'name': 'People API', 'version': 'v1', 'v2discovery': True},
  PUBSUB: {'name': 'Pub / Sub API', 'version': 'v1', 'v2discovery': True},
  REPORTS: {'name': 'Reports API', 'version': 'reports_v1', 'v2discovery': False, 'mappedAPI': 'admin'},
  RESELLER: {'name': 'Reseller API', 'version': 'v1', 'v2discovery': False},
  SERVICEMANAGEMENT: {'name': 'Service Management API', 'version': 'v1', 'v2discovery': True},
  SERVICEUSAGE: {'name': 'Service Usage API', 'version': 'v1', 'v2discovery': True},
  SHEETS: {'name': 'Sheets API', 'version': 'v4', 'v2discovery': True},
  SHEETSTD: {'name': 'Sheets API - todrive', 'version': 'v4', 'v2discovery': True, 'mappedAPI': 'sheets'},
  SITES: {'name': 'Sites API', 'version': 'v1', 'v2discovery': False},
  SITEVERIFICATION: {'name': 'Site Verification API', 'version': 'v1', 'v2discovery': False},
  STORAGE: {'name': 'Cloud Storage API', 'version': 'v1', 'v2discovery': False},
  VAULT: {'name': 'Vault API', 'version': 'v1', 'v2discovery': True},
  }

READONLY = ['readonly',]

_CLIENT_SCOPES = [
  {'name': 'Calendar API',
   'api': CALENDAR,
   'subscopes': READONLY,
   'scope': 'https://www.googleapis.com/auth/calendar'},
  {'name': 'Classroom API - Courses',
   'api': CLASSROOM,
   'subscopes': READONLY,
   'scope': 'https://www.googleapis.com/auth/classroom.courses'},
  {'name': 'Classroom API - Course Announcements',
   'api': CLASSROOM,
   'subscopes': READONLY,
   'scope': 'https://www.googleapis.com/auth/classroom.announcements'},
  {'name': 'Classroom API - Course Topics',
   'api': CLASSROOM,
   'subscopes': READONLY,
   'scope': 'https://www.googleapis.com/auth/classroom.topics'},
  {'name': 'Classroom API - Course Work/Submissions',
   'api': CLASSROOM,
   'subscopes': READONLY,
   'scope': 'https://www.googleapis.com/auth/classroom.coursework.students'},
  {'name': 'Classroom API - Student Guardians',
   'api': CLASSROOM,
   'subscopes': READONLY,
   'scope': 'https://www.googleapis.com/auth/classroom.guardianlinks.students'},
  {'name': 'Classroom API - Profile Emails',
   'api': CLASSROOM,
   'subscopes': [],
   'scope': 'https://www.googleapis.com/auth/classroom.profile.emails'},
  {'name': 'Classroom API - Profile Photos',
   'api': CLASSROOM,
   'subscopes': [],
   'scope': 'https://www.googleapis.com/auth/classroom.profile.photos'},
  {'name': 'Classroom API - Rosters',
   'api': CLASSROOM,
   'subscopes': READONLY,
   'scope': 'https://www.googleapis.com/auth/classroom.rosters'},
#  {'name': 'Cloud Identity Devices API',
#   'api': CLOUDIDENTITY_DEVICES,
#   'subscopes': READONLY,
#   'scope': 'https://www.googleapis.com/auth/cloud-identity.devices'},
#  {'name': 'Cloud Identity Groups API',
#   'api': CLOUDIDENTITY_GROUPS,
#   'subscopes': READONLY,
#   'scope': 'https://www.googleapis.com/auth/cloud-identity.groups'},
  {'name': 'Cloudprint API',
   'api': CLOUDPRINT,
   'subscopes': [],
   'scope': 'https://www.googleapis.com/auth/cloudprint'},
  {'name': 'Cloud Storage (Vault Export - read only)',
   'api': STORAGE,
   'subscopes': [],
   'scope': 'https://www.googleapis.com/auth/devstorage.read_only'},
  {'name': 'Contacts API - Domain Shared and Users and GAL',
   'api': CONTACTS,
   'subscopes': [],
   'scope': 'https://www.google.com/m8/feeds'},
  {'name': 'Data Transfer API',
   'api': DATATRANSFER,
   'subscopes': READONLY,
   'scope': 'https://www.googleapis.com/auth/admin.datatransfer'},
  {'name': 'Directory API - Chrome OS Devices',
   'api': DIRECTORY,
   'subscopes': READONLY,
   'scope': 'https://www.googleapis.com/auth/admin.directory.device.chromeos'},
  {'name': 'Directory API - Customers',
   'api': DIRECTORY,
   'subscopes': READONLY,
   'scope': 'https://www.googleapis.com/auth/admin.directory.customer'},
  {'name': 'Directory API - Domains',
   'api': DIRECTORY,
   'subscopes': READONLY,
   'scope': 'https://www.googleapis.com/auth/admin.directory.domain'},
  {'name': 'Directory API - Groups',
   'api': DIRECTORY,
   'subscopes': READONLY,
   'scope': 'https://www.googleapis.com/auth/admin.directory.group'},
  {'name': 'Directory API - Mobile Devices Directory',
   'api': DIRECTORY,
   'subscopes': ['readonly', 'action'],
   'scope': 'https://www.googleapis.com/auth/admin.directory.device.mobile'},
  {'name': 'Directory API - Organizational Units',
   'api': DIRECTORY,
   'subscopes': READONLY,
   'scope': 'https://www.googleapis.com/auth/admin.directory.orgunit'},
  {'name': 'Directory API - Resource Calendars',
   'api': DIRECTORY,
   'subscopes': READONLY,
   'scope': 'https://www.googleapis.com/auth/admin.directory.resource.calendar'},
  {'name': 'Directory API - Roles',
   'api': DIRECTORY,
   'subscopes': READONLY,
   'scope': 'https://www.googleapis.com/auth/admin.directory.rolemanagement'},
  {'name': 'Directory API - User Schemas',
   'api': DIRECTORY,
   'subscopes': READONLY,
   'scope': 'https://www.googleapis.com/auth/admin.directory.userschema'},
  {'name': 'Directory API - User Security',
   'api': DIRECTORY,
   'subscopes': [],
   'scope': 'https://www.googleapis.com/auth/admin.directory.user.security'},
  {'name': 'Directory API - Users',
   'api': DIRECTORY,
   'subscopes': READONLY,
   'scope': 'https://www.googleapis.com/auth/admin.directory.user'},
  {'name': 'Email Audit API',
   'api': EMAIL_AUDIT,
   'subscopes': [],
   'scope': 'https://apps-apis.google.com/a/feeds/compliance/audit/'},
  {'name': 'Groups Migration API',
   'api': GROUPSMIGRATION,
   'subscopes': [],
   'scope': 'https://www.googleapis.com/auth/apps.groups.migration'},
  {'name': 'Groups Settings API',
   'api': GROUPSSETTINGS,
   'subscopes': [],
   'scope': 'https://www.googleapis.com/auth/apps.groups.settings'},
  {'name': 'License Manager API',
   'api': LICENSING,
   'subscopes': [],
   'scope': 'https://www.googleapis.com/auth/apps.licensing'},
  {'name': 'People API',
   'api': PEOPLE,
   'subscopes': READONLY,
   'scope': 'https://www.googleapis.com/auth/contacts'},
  {'name': 'Pub / Sub API',
   'api': PUBSUB,
   'subscopes': [],
   'offByDefault': True,
   'scope': 'https://www.googleapis.com/auth/pubsub'},
  {'name': 'Reports API - Audit Reports',
   'api': REPORTS,
   'subscopes': [],
   'scope': 'https://www.googleapis.com/auth/admin.reports.audit.readonly'},
  {'name': 'Reports API - Usage Reports',
   'api': REPORTS,
   'subscopes': [],
   'scope': 'https://www.googleapis.com/auth/admin.reports.usage.readonly'},
  {'name': 'Reseller API',
   'api': RESELLER,
   'subscopes': [],
   'offByDefault': True,
   'scope': 'https://www.googleapis.com/auth/apps.order'},
  {'name': 'Site Verification API',
   'api': SITEVERIFICATION,
   'subscopes': [],
   'scope': 'https://www.googleapis.com/auth/siteverification'},
  {'name': 'Sites API',
   'api': SITES,
   'subscopes': [],
   'scope': 'https://sites.google.com/feeds'},
  {'name': 'Vault API',
   'api': VAULT,
   'subscopes': READONLY,
   'scope': 'https://www.googleapis.com/auth/ediscovery'},
  ]

_TODRIVE_CLIENT_SCOPES = [
  {'name': 'Drive API - todrive_clientaccess',
   'api': DRIVE3,
   'subscopes': [],
   'scope': DRIVE_SCOPE},
  {'name': 'Gmail API - todrive_clientaccess',
   'api': GMAIL,
   'subscopes': [],
   'scope': GMAIL_SEND_SCOPE},
  {'name': 'Sheets API - todrive_clientaccess',
   'api': SHEETS,
   'subscopes': [],
   'scope': 'https://www.googleapis.com/auth/spreadsheets'},
  ]

OAUTH2SA_SCOPES = 'us_scopes'

_SVCACCT_SCOPES = [
  {'name': 'AlertCenter API',
   'api': ALERTCENTER,
   'subscopes': [],
   'scope': 'https://www.googleapis.com/auth/apps.alerts'},
  {'name': 'Calendar API',
   'api': CALENDAR,
   'subscopes': READONLY,
   'scope': 'https://www.googleapis.com/auth/calendar'},
  {'name': 'Classroom API - Course Announcements',
   'api': CLASSROOM,
   'subscopes': READONLY,
   'scope': 'https://www.googleapis.com/auth/classroom.announcements'},
  {'name': 'Classroom API - Course Topics',
   'api': CLASSROOM,
   'subscopes': READONLY,
   'scope': 'https://www.googleapis.com/auth/classroom.topics'},
  {'name': 'Classroom API - Course Work/Submissions',
   'api': CLASSROOM,
   'subscopes': READONLY,
   'scope': 'https://www.googleapis.com/auth/classroom.coursework.students'},
  {'name': 'Classroom API - Profile Emails',
   'api': CLASSROOM,
   'subscopes': [],
   'scope': 'https://www.googleapis.com/auth/classroom.profile.emails'},
  {'name': 'Classroom API - Rosters',
   'api': CLASSROOM,
   'subscopes': READONLY,
   'scope': 'https://www.googleapis.com/auth/classroom.rosters'},
  {'name': 'Cloud Print API',
   'api': CLOUDPRINT,
   'subscopes': [],
   'scope': 'https://www.googleapis.com/auth/cloudprint'},
  {'name': 'Contacts API - Users',
   'api': CONTACTS,
   'subscopes': [],
   'scope': 'https://www.google.com/m8/feeds'},
  {'name': 'Drive API',
   'api': DRIVE3,
   'subscopes': READONLY,
   'scope': DRIVE_SCOPE},
  {'name': 'Drive Activity API v1 - must pair with Drive API',
   'api': DRIVEACTIVITY_V1,
   'subscopes': [],
   'scope': 'https://www.googleapis.com/auth/activity'},
  {'name': 'Drive Activity API v2 - must pair with Drive API',
   'api': DRIVEACTIVITY_V2,
   'subscopes': [],
   'scope': 'https://www.googleapis.com/auth/drive.activity'},
  {'name': 'Gmail API - Full Access',
   'api': GMAIL,
   'subscopes': [],
   'scope': 'https://mail.google.com/'},
  {'name': 'Gmail API - Full Access except immediate delete',
   'api': GMAIL,
   'subscopes': [],
   'scope': 'https://www.googleapis.com/auth/gmail.modify'},
  {'name': 'Gmail API - Basic Settings',
   'api': GMAIL,
   'subscopes': [],
   'scope': 'https://www.googleapis.com/auth/gmail.settings.basic'},
  {'name': 'Gmail API - Settings Sharing (Forwarding, Aliases)',
   'api': GMAIL,
   'subscopes': [],
   'scope': 'https://www.googleapis.com/auth/gmail.settings.sharing'},
  {'name': 'Identity and Access Management API',
   'api': IAM,
   'subscopes': [],
   'scope': 'https://www.googleapis.com/auth/cloud-platform'},
  {'name': 'People API',
   'api': PEOPLE,
   'subscopes': READONLY,
   'scope': 'https://www.googleapis.com/auth/contacts'},
  {'name': 'Sheets API',
   'api': SHEETS,
   'subscopes': READONLY,
   'scope': 'https://www.googleapis.com/auth/spreadsheets'},
  {'name': 'Sites API',
   'api': SITES,
   'subscopes': [],
   'scope': 'https://sites.google.com/feeds'},
  ]

_SVCACCT_SPECIAL_SCOPES = [
  {'name': 'Cloud Resource Manager API v1',
   'api': CLOUDRESOURCEMANAGER_V1,
   'subscopes': [],
   'scope': 'https://www.googleapis.com/auth/cloud-platform'},
  {'name': 'Drive API - todrive',
   'api': DRIVETD,
   'subscopes': [],
   'scope': DRIVE_SCOPE},
  {'name': 'Gmail API - Full Access - read only',
   'api': GMAIL,
   'subscopes': [],
   'scope': 'https://www.googleapis.com/auth/gmail.readonly'},
  {'name': 'Gmail API - Send Messages - including todrive',
   'api': GMAIL,
   'subscopes': [],
   'scope': GMAIL_SEND_SCOPE},
  {'name': 'Sheets API - todrive',
   'api': SHEETSTD,
   'subscopes': [],
   'scope': 'https://www.googleapis.com/auth/spreadsheets'},
  ]

_USER_SVCACCT_ONLY_SCOPES = [
  {'name': 'Groups Migration API',
   'api': GROUPSMIGRATION,
   'subscopes': [],
   'scope': 'https://www.googleapis.com/auth/apps.groups.migration'},
  ]

DRIVE3_TO_DRIVE2_ABOUT_FIELDS_MAP = {
  'displayName': 'name',
  'limit': 'quotaBytesTotal',
  'usage': 'quotaBytesUsedAggregate',
  'usageInDrive': 'quotaBytesUsed',
  'usageInDriveTrash': 'quotaBytesUsedInTrash',
  }

DRIVE3_TO_DRIVE2_CAPABILITIES_FIELDS_MAP = {
  'canComment': 'canComment',
  'canReadRevisions': 'canReadRevisions',
  'canCopy': 'copyable',
  'canEdit': 'editable',
  'canShare': 'shareable',
  }

DRIVE3_TO_DRIVE2_CAPABILITIES_NAMES_MAP = {
  'canChangeViewersCanCopyContent': 'canChangeRestrictedDownload',
  }

DRIVE3_TO_DRIVE2_CAPABILITIES_TITLES_MAP = {
  'capabilities.canComment': 'canComment',
  'capabilities.canReadRevisions': 'canReadRevisions',
  'capabilities.canCopy': 'copyable',
  'capabilities.canEdit': 'editable',
  'capabilities.canShare': 'shareable',
  }

DRIVE3_TO_DRIVE2_FILES_FIELDS_MAP = {
  'allowFileDiscovery': 'withLink',
  'createdTime': 'createdDate',
  'expirationTime': 'expirationDate',
  'modifiedByMe': 'modified',
  'modifiedByMeTime': 'modifiedByMeDate',
  'modifiedTime': 'modifiedDate',
  'name': 'title',
  'sharedWithMeTime': 'sharedWithMeDate',
  'size': 'fileSize',
  'trashedTime': 'trashedDate',
  'viewedByMe': 'viewed',
  'viewedByMeTime': 'lastViewedByMeDate',
  'webViewLink': 'alternateLink',
  }

DRIVE3_TO_DRIVE2_LABELS_MAP = {
  'modifiedByMe': 'modified',
  'starred': 'starred',
  'trashed': 'trashed',
  'viewedByMe': 'viewed',
  }

DRIVE3_TO_DRIVE2_REVISIONS_FIELDS_MAP = {
  'modifiedTime': 'modifiedDate',
  'keepForever': 'pinned',
  'size': 'fileSize',
  }

def getAPIName(api):
  return _INFO[api]['name']

def getVersion(api):
  version = _INFO[api]['version']
  v2discovery = _INFO[api]['v2discovery']
  api = _INFO[api].get('mappedAPI', api)
  return (api, version, v2discovery)

def getClientScopesSet(api):
  return {scope['scope'] for scope in _CLIENT_SCOPES if scope['api'] == api}

def getClientScopesList(todriveClientAccess):
  caScopes = _CLIENT_SCOPES[:]
  if todriveClientAccess:
    caScopes.extend(_TODRIVE_CLIENT_SCOPES)
  return sorted(caScopes, key=lambda k: k['name'])

def getClientScopesURLs(todriveClientAccess):
  caScopes = _CLIENT_SCOPES[:]
  if todriveClientAccess:
    caScopes.extend(_TODRIVE_CLIENT_SCOPES)
  return sorted({scope['scope'] for scope in _CLIENT_SCOPES})

def getSvcAcctScopeAPI(uscope):
  for scope in _SVCACCT_SCOPES:
    if uscope == scope['scope'] or (uscope.endswith('.readonly') and 'readonly' in scope['subscopes']):
      return scope['api']
  return None

def getSvcAcctScopes(userServiceAccountAccessOnly, svcAcctSpecialScopes):
  saScopes = [scope['scope'] for scope in _SVCACCT_SCOPES]
  if userServiceAccountAccessOnly:
    saScopes.extend([scope['scope'] for scope in _USER_SVCACCT_ONLY_SCOPES])
  if svcAcctSpecialScopes:
    saScopes.extend([scope['scope'] for scope in _SVCACCT_SPECIAL_SCOPES])
  return saScopes

def getSvcAcctScopesList(userServiceAccountAccessOnly, svcAcctSpecialScopes):
  saScopes = _SVCACCT_SCOPES[:]
  if userServiceAccountAccessOnly:
    saScopes.extend(_USER_SVCACCT_ONLY_SCOPES)
  if svcAcctSpecialScopes:
    saScopes.extend(_SVCACCT_SPECIAL_SCOPES)
  return sorted(saScopes, key=lambda k: k['name'])

def hasLocalJSON(api):
  return _INFO[api].get('localjson', False)
