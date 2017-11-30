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

"""GAM entity processing

"""

class GamEntity(object):

  ROLE_MANAGER = u'MANAGER'
  ROLE_MEMBER = u'MEMBER'
  ROLE_OWNER = u'OWNER'
  ROLE_USER = u'USER'
  ROLE_MANAGER_MEMBER = u','.join([ROLE_MANAGER, ROLE_MEMBER])
  ROLE_MANAGER_OWNER = u','.join([ROLE_MANAGER, ROLE_OWNER])
  ROLE_MEMBER_OWNER = u','.join([ROLE_MEMBER, ROLE_OWNER])
  ROLE_MANAGER_MEMBER_OWNER = u','.join([ROLE_MANAGER, ROLE_MEMBER, ROLE_OWNER])

# Keys into NAMES; arbitrary values but must be unique
  ACCESS_TOKEN = u'atok'
  ACCOUNT = u'acct'
  ACTION = u'actn'
  ACTIVITY = u'actv'
  ADMINISTRATOR = u'admi'
  ALIAS = u'alia'
  ALIAS_EMAIL = u'alie'
  ALIAS_TARGET = u'alit'
  API = u'api '
  APPLICATION_SPECIFIC_PASSWORD = u'aspa'
  ARROWS_ENABLED = u'arro'
  ATTENDEE = u'atnd'
  AUDIT_ACTIVITY_REQUEST = u'auda'
  AUDIT_EXPORT_REQUEST = u'audx'
  AUDIT_MONITOR_REQUEST = u'audm'
  BACKUP_VERIFICATION_CODES = u'buvc'
  CALENDAR = u'cale'
  CALENDAR_ACL = u'cacl'
  CALENDAR_SETTINGS = u'cset'
  CLIENT_SECRETS_JSON_FILE = u'clis'
  COLLABORATOR = u'cola'
  CONFIG_FILE = u'conf'
  CONTACT = u'cont'
  CONTACT_GROUP = u'cogr'
  CONTACT_GROUP_NAME = u'cogn'
  COURSE = u'cour'
  COURSE_ALIAS = u'coal'
  COURSE_ID = u'coid'
  CUSTOMER_ID = u'cust'
  CREDENTIALS = u'cred'
  CRITERIA = u'crit'
  CROS_DEVICE = u'cros'
  CUSTOMER_DOMAIN = u'cudo'
  CUSTOMER_ID = u'cuid'
  DEFAULT_LANGUAGE = u'dfla'
  DELEGATE = u'dele'
  DELEGATOR = u'delo'
  DELETED_USER = u'delu'
  DISCOVERY_JSON_FILE = u'disc'
  DOMAIN = u'doma'
  DOMAIN_ALIAS = u'doal'
  DRIVE_FILE = u'file'
  DRIVE_FILE_ID = u'fili'
  DRIVE_FILE_NAME = u'filn'
  DRIVE_FILE_REVISION = u'filr'
  DRIVE_FILE_OR_FOLDER = u'fifo'
  DRIVE_FILE_OR_FOLDER_ACL = u'fiac'
  DRIVE_FILE_OR_FOLDER_ID = u'fifi'
  DRIVE_FOLDER = u'fold'
  DRIVE_FOLDER_ID = u'foli'
  DRIVE_FOLDER_NAME = u'foln'
  DRIVE_ORPHAN_FILE_OR_FOLDER = u'orph'
  DRIVE_PATH = u'drvp'
  DRIVE_SETTINGS = u'drvs'
  DRIVE_TRASH = u'drvt'
  EMAIL = u'emai'
  EMAIL_ALIAS = u'emal'
  EMAIL_SETTINGS = u'emse'
  ENTITY = u'enti'
  EVENT = u'evnt'
  FIELD = u'fiel'
  FILTER = u'filt'
  FORWARD_ENABLED = u'fwde'
  FORWARDING_ADDRESS = u'fwda'
  GMAIL_PROFILE = u'gmpr'
  GPLUS_PROFILE = u'gppr'
  GROUP = u'grou'
  GROUP_ALIAS = u'gali'
  GROUP_EMAIL = u'gale'
  GROUP_MEMBERSHIP = u'gmem'
  GROUP_SETTINGS = u'gset'
  GUARDIAN = u'guar'
  GUARDIAN_INVITATION = u'gari'
  IMAP_ENABLED = u'imap'
  INSTANCE = u'inst'
  ITEM = u'item'
  ISSUER_CN = u'issu'
  KEYBOARD_SHORTCUTS_ENABLED = u'kbsc'
  LABEL = u'labe'
  LANGUAGE = u'lang'
  LICENSE = u'lice'
  LOGO = u'logo'
  MEMBER = u'memb'
  MESSAGE = u'mesg'
  MOBILE_DEVICE = u'mobi'
  NONEDITABLE_ALIAS = u'neal'
  NOTIFICATION = u'noti'
  OAUTH2_TXT_FILE = u'oaut'
  OAUTH2SERVICE_JSON_FILE = u'oau2'
  ORGANIZATIONAL_UNIT = u'orgu'
  PAGE_SIZE = u'page'
  PARENT_ORGANIZATIONAL_UNIT = u'porg'
  PARTICIPANT = u'part'
  PERMISSION = u'perm'
  PERMISSION_ID = u'peid'
  PERMITTEE = u'prmt'
  PHOTO = u'phot'
  POP_ENABLED = u'popa'
  PRINTER = u'prin'
  PRINTER_ACL = u'pacl'
  PRINTJOB = u'prjo'
  PRIVILEGE = u'priv'
  PRODUCT = u'prod'
  PROFILE_SHARING_ENABLED = u'prof'
  PROJECT = u'proj'
  PUBLIC_KEY = u'pubk'
  QUERY = u'quer'
  REPORT = u'rept'
  REQUEST_ID = u'reqi'
  RESOURCE_CALENDAR = u'resc'
  RESOURCE_ID = u'resi'
  ROLE = u'role'
  ROLE_ASSIGNMENT_ID = u'raid'
  SCOPE = u'scop'
  SECTION = u'sect'
  SENDAS_ADDRESS = u'sasa'
  SERVICE = u'serv'
  SIGNATURE = u'sign'
  SITE = u'site'
  SITE_ACL = u'sacl'
  SKU = u'sku '
  SMIME_ID = u'smid'
  SNIPPETS_ENABLED = u'snip'
  SSO_KEY = u'ssok'
  SSO_SETTINGS = u'ssos'
  SOURCE_USER = u'srcu'
  SPREADSHEET = u'sprd'
  SPREADSHEET_RANGE = u'ssrn'
  STUDENT = u'stud'
  SUBSCRIPTION = u'subs'
  TARGET_USER = u'tgtu'
  TEACHER = u'teac'
  TEAMDRIVE = u'tdrv'
  TEAMDRIVE_ID = u'tdid'
  TEAMDRIVE_NAME = u'tdna'
  TEAMDRIVE_THEME = u'tdth'
  THREAD = u'thre'
  TOKEN = u'tokn'
  TRANSFER_ID = u'trid'
  TRANSFER_REQUEST = u'trnr'
  UNICODE_ENCODING_ENABLED = u'unic'
  UNIQUE_ID = u'uniq'
  USER = u'user'
  USER_ALIAS = u'uali'
  USER_EMAIL = u'ual'
  USER_SCHEMA = u'usch'
  VACATION = u'vaca'
  VACATION_ENABLED = u'vace'
  VALUE = u'valu'
  VAULT_HOLD = u'vlth'
  VAULT_MATTER = u'vltm'
  VAULT_MATTER_ID = u'vlmi'
  WEBCLIPS_ENABLED = u'webc'
  # _NAMES[0] is plural, _NAMES[1] is singular unless the item name is explicitly plural (Calendar Settings)
  # For items with Boolean values, both entries are singular (Forward, POP)
  # These values can be translated into other languages
  _NAMES = {
    ACCESS_TOKEN: [u'Access Tokens', u'Access Token'],
    ACCOUNT: [u'G Suite Accounts', u'G Suite Account'],
    ACTION: [u'Actions', u'Action'],
    ACTIVITY: [u'Activities', u'Activity'],
    ADMINISTRATOR: [u'Administrators', u'Administrator'],
    ALIAS: [u'Aliases', u'Alias'],
    ALIAS_EMAIL: [u'Alias Emails', u'Alias Email'],
    ALIAS_TARGET: [u'Alias Targets', u'Alias Target'],
    API: [u'APIs', u'API'],
    APPLICATION_SPECIFIC_PASSWORD: [u'Application Specific Password IDs', u'Application Specific Password ID'],
    ARROWS_ENABLED: [u'Personal Indicator Arrows Enabled', u'Personal Indicator Arrows Enabled'],
    ATTENDEE: [u'Attendees', u'Attendee'],
    AUDIT_ACTIVITY_REQUEST: [u'Audit Activity Requests', u'Audit Activity Request'],
    AUDIT_EXPORT_REQUEST: [u'Audit Export Requests', u'Audit Export Request'],
    AUDIT_MONITOR_REQUEST: [u'Audit Monitor Requests', u'Audit Monitor Request'],
    BACKUP_VERIFICATION_CODES: [u'Backup Verification Codes', u'Backup Verification Codes'],
    CALENDAR: [u'Calendars', u'Calendar'],
    CALENDAR_ACL: [u'Calendar ACLs', u'Calendar ACL'],
    CALENDAR_SETTINGS: [u'Calendar Settings', u'Calendar Settings'],
    CLIENT_SECRETS_JSON_FILE: [u'Client Secrets File', u'Client Secrets File'],
    COLLABORATOR: [u'Collaborators', u'Collaborator'],    
    CONFIG_FILE: [u'Config File', u'Config File'],
    CONTACT: [u'Contacts', u'Contact'],
    CONTACT_GROUP: [u'Contact Groups', u'Contact Group'],
    CONTACT_GROUP_NAME: [u'Contact Group Names', u'Contact Group Name'],
    COURSE: [u'Courses', u'Course'],
    COURSE_ALIAS: [u'Course Aliases', u'Course Alias'],
    COURSE_ID: [u'Course IDs', u'Course ID'],
    CUSTOMER_DOMAIN: [u'Customer Domains', u'Customer Domain'],
    CUSTOMER_ID: [u'Customer IDs', u'Customer ID'],
    CREDENTIALS: [u'Credentials', u'Credentials'],
    CRITERIA: [u'Criteria', u'Criteria'],
    CROS_DEVICE: [u'CrOS Devices', u'CrOS Device'],
    CUSTOMER_ID: [u'Customer IDs', u'Customer ID'],
    DEFAULT_LANGUAGE: [u'Default Language', u'Default Language'],
    DELEGATE: [u'Delegates', u'Delegate'],
    DELEGATOR: [u'Delegators', u'Delegator'],
    DELETED_USER: [u'Deleted Users', u'Deleted User'],
    DISCOVERY_JSON_FILE: [u'Discovery File', u'Discovery File'],
    DOMAIN: [u'Domains', u'Domain'],
    DOMAIN_ALIAS: [u'Domain Aliases', u'Domain Alias'],
    DRIVE_FILE: [u'Drive Files', u'Drive File'],
    DRIVE_FILE_ID: [u'Drive File IDs', u'Drive File ID'],
    DRIVE_FILE_NAME: [u'Drive File Names', u'Drive File Name'],
    DRIVE_FILE_REVISION: [u'Drive File Revisions', u'Drive File Revision'],
    DRIVE_FILE_OR_FOLDER: [u'Drive Files/Folders', u'Drive File/Folder'],
    DRIVE_FILE_OR_FOLDER_ACL: [u'Drive File/Folder ACLs', u'Drive File/Folder ACL'],
    DRIVE_FILE_OR_FOLDER_ID: [u'Drive File/Folder IDs', u'Drive File/Folder ID'],
    DRIVE_FOLDER: [u'Drive Folders', u'Drive Folder'],
    DRIVE_FOLDER_ID: [u'Drive Folder IDs', u'Drive Folder ID'],
    DRIVE_FOLDER_NAME: [u'Drive Folder Names', u'Drive Folder Name'],
    DRIVE_ORPHAN_FILE_OR_FOLDER: [u'Drive Orphan Files/Folders', u'Drive Orphan File/Folder'],
    DRIVE_PATH: [u'Drive Paths', u'Drive Path'],
    DRIVE_SETTINGS: [u'Drive Settings', u'Drive Settings'],
    DRIVE_TRASH: [u'Drive Trash', u'Drive Trash'],
    EMAIL: [u'Email Addresses', u'Email Address'],
    EMAIL_ALIAS: [u'Email Aliases', u'Email Alias'],
    EMAIL_SETTINGS: [u'Email Settings', u'Email Settings'],
    ENTITY: [u'Entities', u'Entity'],
    EVENT: [u'Events', u'Event'],
    FIELD: [u'Fields', u'Field'],
    FILTER: [u'Filters', u'Filter'],
    FORWARD_ENABLED: [u'Forward Enabled', u'Forward Enabled'],
    FORWARDING_ADDRESS: [u'Forwarding Addresses', u'Forwarding Address'],
    GMAIL_PROFILE: [u'Gmail profile', u'Gmail profile'],
    GPLUS_PROFILE: [u'Gplus profile', u'Gplus profile'],
    GROUP: [u'Groups', u'Group'],
    GROUP_ALIAS: [u'Group Aliases', u'Group Alias'],
    GROUP_EMAIL: [u'Group Emails', u'Group Email'],
    GROUP_MEMBERSHIP: [u'Group Memberships', u'Group Membership'],
    GROUP_SETTINGS: [u'Group Settings', u'Group Settings'],
    GUARDIAN: [u'Guardians', u'Guardian'],
    GUARDIAN_INVITATION: [u'Guardian Invitations', u'Guardian Invitation'],
    IMAP_ENABLED: [u'IMAP Enabled', u'IMAP Enabled'],
    INSTANCE: [u'Instances', u'Instance'],
    ISSUER_CN: [u'Issuer CNs', u'Issuer CN'],
    ITEM: [u'Items', u'Item'],
    KEYBOARD_SHORTCUTS_ENABLED: [u'Keyboard Shortcuts Enabled', u'Keyboard Shortcuts Enabled'],
    LABEL: [u'Labels', u'Label'],
    LANGUAGE: [u'Languages', u'Language'],
    LICENSE: [u'Licenses', u'License'],
    LOGO: [u'Logos', u'Logo'],
    MEMBER: [u'Members', u'Member'],
    MESSAGE: [u'Messages', u'Message'],
    MOBILE_DEVICE: [u'Mobile Devices', u'Mobile Device'],
    NONEDITABLE_ALIAS: [u'Non-Editable Aliases', u'Non-Editable Alias'],
    NOTIFICATION: [u'Notifications', u'Notification'],
    OAUTH2_TXT_FILE: [u'Client OAuth2 File', u'Client OAuth2 File'],
    OAUTH2SERVICE_JSON_FILE: [u'Service Account OAuth2 File', u'Service Account OAuth2 File'],
    ORGANIZATIONAL_UNIT: [u'Organizational Units', u'Organizational Unit'],
    PAGE_SIZE: [u'Page Size', u'Page Size'],
    PARENT_ORGANIZATIONAL_UNIT: [u'Parent Organizational Units', u'Parent Organizational Unit'],
    PARTICIPANT: [u'Participants', u'Participant'],
    PERMISSION: [u'Permissions', u'Permission'],
    PERMISSION_ID: [u'Permission IDs', u'Permission ID'],
    PERMITTEE: [u'Permittees', u'Permittee'],
    PHOTO: [u'Photos', u'Photo'],
    POP_ENABLED: [u'POP Enabled', u'POP Enabled'],
    PRINTER: [u'Printers', u'Printer'],
    PRINTER_ACL: [u'Printer ACLs', u'Printer ACL'],
    PRINTJOB: [u'Print Jobs', u'Print Job'],
    PRIVILEGE: [u'Privileges', u'Privilege'],
    PRODUCT: [u'Products', u'Product'],
    PROFILE_SHARING_ENABLED: [u'Profile Sharing Enabled', u'Profile Sharing Enabled'],
    PROJECT: [u'Projects', u'Project'],
    PUBLIC_KEY: [u'Public Key', u'Public Key'],
    QUERY: [u'Queries', u'Query'],
    REPORT: [u'Reports', u'Report'],
    REQUEST_ID: [u'Request IDs', u'Request ID'],
    RESOURCE_CALENDAR: [u'Resource Calendars', u'Resource Calendar'],
    RESOURCE_ID: [u'Resource IDs', u'Resource ID'],
    ROLE: [u'Roles', u'Role'],
    ROLE_ASSIGNMENT_ID: [u'Role Assignment IDs', u'Role Assignment ID'],
    SCOPE: [u'Scopes', u'Scope'],
    SECTION: [u'Sections', u'Section'],
    SENDAS_ADDRESS: [u'SendAs Addresses', u'SendAs Address'],
    SERVICE: [u'Services', u'Service'],
    SIGNATURE: [u'Signatures', u'Signature'],
    SITE: [u'Sites', u'Site'],
    SITE_ACL: [u'Site ACLs', u'Site ACL'],
    SKU: [u'SKUs', u'SKU'],
    SMIME_ID: [u'S/MIME Certificate IDs', u'S/MIME Certificate ID'],
    SNIPPETS_ENABLED: [u'Preview Snippets Enabled', u'Preview Snippets Enabled'],
    SSO_KEY: [u'SSO Key', u'SSO Key'],
    SSO_SETTINGS: [u'SSO Settings', u'SSO Settings'],
    SOURCE_USER: [u'Source Users', u'Source User'],
    SPREADSHEET: [u'Spreadsheets', u'Spreadsheet'],
    SPREADSHEET_RANGE: [u'Spreadsheet Ranges', u'Spreadsheet Range'],
    SUBSCRIPTION: [u'Subscriptions', u'Subscription'],
    STUDENT: [u'Students', u'Student'],
    TARGET_USER: [u'Target Users', u'Target User'],
    TEACHER: [u'Teachers', u'Teacher'],
    TEAMDRIVE: [u'TeamDrives', u'TeamDrive'],
    TEAMDRIVE_ID: [u'TeamDrive IDs', u'TeamDrive ID'],
    TEAMDRIVE_NAME: [u'TeamDrive Names', u'TeamDrive Name'],
    TEAMDRIVE_THEME: [u'TeamDrive Themes', u'TeamDrive Theme'],
    THREAD: [u'Threads', u'Thread'],
    TOKEN: [u'Tokens', u'Token'],
    TRANSFER_ID: [u'Transfer IDs', u'Transfer ID'],
    TRANSFER_REQUEST: [u'Transfer Requests', u'Transfer Request'],
    UNICODE_ENCODING_ENABLED: [u'UTF-8 Encoding Enabled', u'UTF-8 Encoding Enabled'],
    UNIQUE_ID: [u'Unique IDs', u'Unique ID'],
    USER: [u'Users', u'User'],
    USER_ALIAS: [u'User Aliases', u'User Alias'],
    USER_EMAIL: [u'User Emails', u'User Email'],
    USER_SCHEMA: [u'Schemas', u'Schema'],
    VACATION: [u'Vacation', u'Vacation'],
    VACATION_ENABLED: [u'Vacation Enabled', u'Vacation Enabled'],
    VALUE: [u'Values', u'Value'],
    VAULT_HOLD: [u'Vault Holds', u'Vault Hold'],
    VAULT_MATTER: [u'Vault Matters', u'Vault Matter'],
    VAULT_MATTER_ID: [u'Vault Matter IDs', u'Vault Matter ID'],
    WEBCLIPS_ENABLED: [u'Web Clips Enabled', u'Web Clips Enabled'],
    ROLE_MANAGER: [u'Managers', u'Manager'],
    ROLE_MEMBER: [u'Members', u'Member'],
    ROLE_OWNER: [u'Owners', u'Owner'],
    ROLE_USER: [u'Users', u'User'],
    ROLE_MANAGER_MEMBER: [u'Members, Managers', u'Member, Manager'],
    ROLE_MANAGER_OWNER: [u'Managers, Owners', u'Manager, Owner'],
    ROLE_MEMBER_OWNER: [u'Members, Owners', u'Member, Owner'],
    ROLE_MANAGER_MEMBER_OWNER: [u'Members, Managers, Owners', u'Member, Manager, Owner'],
    }

  def __init__(self):
    self.entityType = None
    self.forWhom = None
    self.preQualifier = u''
    self.postQualifier = u''
    self.showTotal = False

  def SetGetting(self, entityType):
    self.entityType = entityType
    self.preQualifier = self.postQualifier = u''

  def SetGettingQuery(self, entityType, query):
    self.entityType = entityType
    self.preQualifier = u' that match query ({0})'.format(query)
    self.postQualifier = u' that matched query ({0})'.format(query)

  def SetGettingQualifier(self, entityType, qualifier):
    self.entityType = entityType
    self.preQualifier = self.postQualifier = qualifier

  def Getting(self):
    return self.entityType

  def GettingPreQualifier(self):
    return self.preQualifier

  def GettingPostQualifier(self):
    return self.postQualifier

  def SetGettingForWhom(self, forWhom):
    self.forWhom = forWhom

  def GettingForWhom(self):
    return self.forWhom

  def SetGettingShowTotal(self, showTotal):
    self.showTotal = showTotal

  def GettingShowTotal(self):
    return self.showTotal

  def Choose(self, entityType, count):
    return self._NAMES[entityType][[0, 1][count == 1]]

  def ChooseGetting(self, count):
    return self._NAMES[self.entityType][[0, 1][count == 1]]

  def Plural(self, entityType):
    return self._NAMES[entityType][0]

  def PluralGetting(self):
    return self._NAMES[self.entityType][0]

  def Singular(self, entityType):
    return self._NAMES[entityType][1]

  def SingularGetting(self):
    return self._NAMES[self.entityType][1]

  def MayTakeTime(self, entityType):
    if entityType:
      return u', may take some time on a large {0}...'.format(self.Singular(entityType))
    return u''

  def FormatEntityValueList(self, entityValueList):
    evList = []
    for j in range(0, len(entityValueList), 2):
      evList.append(self.Singular(entityValueList[j]))
      evList.append(entityValueList[j+1])
    return evList

  def TypeMessage(self, entityType, message):
    return u'{0}: {1}'.format(self.Singular(entityType), message)

  def TypeName(self, entityType, entityName):
    return u'{0}: {1}'.format(self.Singular(entityType), entityName)

  def TypeNameMessage(self, entityType, entityName, message):
    return u'{0}: {1} {2}'.format(self.Singular(entityType), entityName, message)
