# -*- coding: utf-8 -*-

# Copyright (C) 2019 Ross Scroggs All Rights Reserved.
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

  ROLE_MANAGER = 'MANAGER'
  ROLE_MEMBER = 'MEMBER'
  ROLE_OWNER = 'OWNER'
  ROLE_USER = 'USER'
  ROLE_MANAGER_MEMBER = ','.join([ROLE_MANAGER, ROLE_MEMBER])
  ROLE_MANAGER_OWNER = ','.join([ROLE_MANAGER, ROLE_OWNER])
  ROLE_MEMBER_OWNER = ','.join([ROLE_MEMBER, ROLE_OWNER])
  ROLE_MANAGER_MEMBER_OWNER = ','.join([ROLE_MANAGER, ROLE_MEMBER, ROLE_OWNER])

# Keys into NAMES; arbitrary values but must be unique
  ACCESS_TOKEN = 'atok'
  ACCOUNT = 'acct'
  ACTION = 'actn'
  ACTIVITY = 'actv'
  ADMINISTRATOR = 'admi'
  ALERT = 'alrt'
  ALERT_ID = 'alri'
  ALERT_FEEDBACK = 'alfb'
  ALERT_FEEDBACK_ID = 'alfi'
  ALIAS = 'alia'
  ALIAS_EMAIL = 'alie'
  ALIAS_TARGET = 'alit'
  API = 'api '
  APP_ACCESS_SETTINGS = 'apps'
  APPLICATION_SPECIFIC_PASSWORD = 'aspa'
  ARROWS_ENABLED = 'arro'
  ATTENDEE = 'atnd'
  AUDIT_ACTIVITY_REQUEST = 'auda'
  AUDIT_EXPORT_REQUEST = 'audx'
  AUDIT_MONITOR_REQUEST = 'audm'
  BACKUP_VERIFICATION_CODES = 'buvc'
  BUILDING = 'bldg'
  BUILDING_ID = 'bldi'
  CALENDAR = 'cale'
  CALENDAR_ACL = 'cacl'
  CALENDAR_SETTINGS = 'cset'
  CLASSROOM_INVITATION = 'clai'
  CLASSROOM_INVITATION_OWNER = 'clio'
  CLASSROOM_INVITATION_STUDENT = 'clis'
  CLASSROOM_INVITATION_TEACHER = 'clit'
  CLASSROOM_OAUTH2_TXT_FILE = 'coa'
  CLIENT_SECRETS_JSON_FILE = 'csjf'
  CLOUD_STORAGE_FILE = 'clsf'
  COLLABORATOR = 'cola'
  CONFIG_FILE = 'conf'
  CONTACT = 'cont'
  CONTACT_GROUP = 'cogr'
  CONTACT_GROUP_NAME = 'cogn'
  COPYFROM_COURSE = 'cfco'
  COURSE = 'cour'
  COURSE_ALIAS = 'coal'
  COURSE_ANNOUNCEMENT_ID = 'caid'
  COURSE_ANNOUNCEMENT_STATE = 'cast'
  COURSE_MATERIAL_FORM = 'comf'
  COURSE_NAME = 'cona'
  COURSE_STATE = 'cost'
  COURSE_SUBMISSION_ID = 'csid'
  COURSE_SUBMISSION_STATE = 'csst'
  COURSE_TOPIC = 'ctop'
  COURSE_TOPIC_ID = 'ctoi'
  COURSE_WORK_ID = 'cwid'
  COURSE_WORK_STATE = 'cwst'
  CREATOR_ID = 'crid'
  CREDENTIALS = 'cred'
  CRITERIA = 'crit'
  CROS_AUE_DATES_JSON_FILE = 'caue'
  CROS_DEVICE = 'cros'
  CUSTOMER_DOMAIN = 'cudo'
  CUSTOMER_ID = 'cuid'
  DEFAULT_LANGUAGE = 'dfla'
  DELEGATE = 'dele'
  DELETED_USER = 'del'
  DELIVERY = 'deli'
  DEVICE_FILE = 'devf'
  DIRECTORY = 'drct'
  DISCOVERY_JSON_FILE = 'disc'
  DOCUMENT = 'doc'
  DOMAIN = 'doma'
  DOMAIN_ALIAS = 'doal'
  DRIVE_FILE = 'dfil'
  DRIVE_FILE_ID = 'fili'
  DRIVE_FILE_NAME = 'filn'
  DRIVE_FILE_REVISION = 'filr'
  DRIVE_FILE_OR_FOLDER = 'fifo'
  DRIVE_FILE_OR_FOLDER_ACL = 'fiac'
  DRIVE_FILE_OR_FOLDER_ID = 'fifi'
  DRIVE_FOLDER = 'fold'
  DRIVE_FOLDER_ID = 'foli'
  DRIVE_FOLDER_NAME = 'foln'
  DRIVE_ORPHAN_FILE_OR_FOLDER = 'orph'
  DRIVE_PARENT_FOLDER = 'fipf'
  DRIVE_PATH = 'drvp'
  DRIVE_SETTINGS = 'drvs'
  DRIVE_TRASH = 'drvt'
  EMAIL = 'emai'
  EMAIL_ALIAS = 'emal'
  EMAIL_SETTINGS = 'emse'
  ENTITY = 'enti'
  EVENT = 'evnt'
  FEATURE = 'feat'
  FIELD = 'fiel'
  FILE = 'file'
  FILTER = 'filt'
  FORWARD_ENABLED = 'fwde'
  FORWARDING_ADDRESS = 'fwda'
  GMAIL_PROFILE = 'gmpr'
  GROUP = 'grou'
  GROUP_ALIAS = 'gali'
  GROUP_EMAIL = 'gale'
  GROUP_MEMBERSHIP = 'gmem'
  GROUP_SETTINGS = 'gset'
  GROUP_TREE = 'gtre'
  GUARDIAN = 'guar'
  GUARDIAN_INVITATION = 'gari'
  GUARDIAN_AND_INVITATION = 'gani'
  IMAP_ENABLED = 'imap'
  INSTANCE = 'inst'
  ITEM = 'item'
  ISSUER_CN = 'iss'
  KEYBOARD_SHORTCUTS_ENABLED = 'kbsc'
  LABEL = 'labe'
  LANGUAGE = 'lang'
  LICENSE = 'lice'
  MD5HASH = 'md5h'
  MEMBER = 'memb'
  MEMBER_NOT_SUSPENDED = 'mns'
  MEMBER_SUSPENDED = 'msup'
  MESSAGE = 'mesg'
  MOBILE_DEVICE = 'mobi'
  NAME = 'name'
  NONEDITABLE_ALIAS = 'neal'
  OAUTH2_TXT_FILE = 'oaut'
  OAUTH2SERVICE_JSON_FILE = 'oau2'
  ORGANIZATIONAL_UNIT = 'org'
  OWNER = 'ownr'
  OWNER_ID = 'owid'
  PAGE_SIZE = 'page'
  PARENT_ORGANIZATIONAL_UNIT = 'porg'
  PARTICIPANT = 'part'
  PERMISSION = 'perm'
  PERMISSION_ID = 'peid'
  PERMITTEE = 'prmt'
  PHOTO = 'phot'
  POP_ENABLED = 'popa'
  PRINTER = 'prin'
  PRINTER_ACL = 'pacl'
  PRINTJOB = 'prjo'
  PRIVILEGE = 'priv'
  PRODUCT = 'prod'
  PROFILE_SHARING_ENABLED = 'prof'
  PROJECT = 'proj'
  PROJECT_FOLDER = 'prjf'
  PUBLIC_KEY = 'pubk'
  QUERY = 'quer'
  RECIPIENT = 'recp'
  REPORT = 'rept'
  REQUEST_ID = 'reqi'
  RESOURCE_CALENDAR = 'resc'
  RESOURCE_ID = 'resi'
  ROLE = 'role'
  ROLE_ASSIGNMENT_ID = 'raid'
  ROW = 'row '
  SCOPE = 'scop'
  SECTION = 'sect'
  SENDAS_ADDRESS = 'sasa'
  SERVICE = 'serv'
  SHEET = 'shet'
  SIGNATURE = 'sign'
  SITE = 'site'
  SITE_ACL = 'sacl'
  SKU = 'sku '
  SMIME_ID = 'smid'
  SNIPPETS_ENABLED = 'snip'
  SSO_KEY = 'ssok'
  SSO_SETTINGS = 'ssos'
  SOURCE_USER = 'src'
  SPREADSHEET = 'sprd'
  SPREADSHEET_RANGE = 'ssrn'
  STUDENT = 'stud'
  SUBSCRIPTION = 'subs'
  TARGET_USER = 'tgt'
  TEACHER = 'teac'
  TEAMDRIVE = 'tdrv'
  TEAMDRIVE_ACL = 'tdac'
  TEAMDRIVE_FOLDER = 'tdfo'
  TEAMDRIVE_ID = 'tdid'
  TEAMDRIVE_NAME = 'tdna'
  TEAMDRIVE_THEME = 'tdth'
  THREAD = 'thre'
  TOKEN = 'tokn'
  TRANSFER_APPLICATION = 'trap'
  TRANSFER_ID = 'trid'
  TRANSFER_REQUEST = 'trnr'
  TRASHED_EVENT = 'trev'
  TRUSTED_APPLICATION = 'trus'
  UNICODE_ENCODING_ENABLED = 'unic'
  UNIQUE_ID = 'uniq'
  USER = 'user'
  USER_ALIAS = 'uali'
  USER_EMAIL = 'uema'
  USER_NOT_SUSPENDED = 'uns'
  USER_SCHEMA = 'usch'
  USER_SUSPENDED = 'usup'
  VACATION = 'vaca'
  VACATION_ENABLED = 'vace'
  VALUE = 'val'
  VAULT_EXPORT = 'vlte'
  VAULT_HOLD = 'vlth'
  VAULT_MATTER = 'vltm'
  VAULT_MATTER_ID = 'vlmi'
  WEBCLIPS_ENABLED = 'webc'
  # _NAMES[0] is plural, _NAMES[1] is singular unless the item name is explicitly plural (Calendar Settings)
  # For items with Boolean values, both entries are singular (Forward, POP)
  # These values can be translated into other languages
  _NAMES = {
    ACCESS_TOKEN: ['Access Tokens', 'Access Token'],
    ACCOUNT: ['G Suite Accounts', 'G Suite Account'],
    ACTION: ['Actions', 'Action'],
    ACTIVITY: ['Activities', 'Activity'],
    ADMINISTRATOR: ['Administrators', 'Administrator'],
    ALERT: ['Alerts', 'Alert'],
    ALERT_ID: ['Alert IDs', 'Alert ID'],
    ALERT_FEEDBACK: ['Alert Feedbacks', 'Alert Feedback'],
    ALERT_FEEDBACK_ID: ['Alert Feedback IDs', 'Alert Feedback ID'],
    ALIAS: ['Aliases', 'Alias'],
    ALIAS_EMAIL: ['Alias Emails', 'Alias Email'],
    ALIAS_TARGET: ['Alias Targets', 'Alias Target'],
    API: ['APIs', 'API'],
    APP_ACCESS_SETTINGS: ['Application Access Settings', 'Application Access Settings'],
    APPLICATION_SPECIFIC_PASSWORD: ['Application Specific Password IDs', 'Application Specific Password ID'],
    ARROWS_ENABLED: ['Personal Indicator Arrows Enabled', 'Personal Indicator Arrows Enabled'],
    ATTENDEE: ['Attendees', 'Attendee'],
    AUDIT_ACTIVITY_REQUEST: ['Audit Activity Requests', 'Audit Activity Request'],
    AUDIT_EXPORT_REQUEST: ['Audit Export Requests', 'Audit Export Request'],
    AUDIT_MONITOR_REQUEST: ['Audit Monitor Requests', 'Audit Monitor Request'],
    BACKUP_VERIFICATION_CODES: ['Backup Verification Codes', 'Backup Verification Codes'],
    BUILDING: ['Buildings', 'Building'],
    BUILDING_ID: ['Building IDs', 'Building ID'],
    CALENDAR: ['Calendars', 'Calendar'],
    CALENDAR_ACL: ['Calendar ACLs', 'Calendar ACL'],
    CALENDAR_SETTINGS: ['Calendar Settings', 'Calendar Settings'],
    CLASSROOM_INVITATION: ['Classroom Invitations', 'Classroom Invitation'],
    CLASSROOM_INVITATION_OWNER: ['Classroom Owner Invitations', 'Classroom Owner Invitation'],
    CLASSROOM_INVITATION_STUDENT: ['Classroom Student Invitations', 'Classroom Student Invitation'],
    CLASSROOM_INVITATION_TEACHER: ['Classroom Teacher Invitations', 'Classroom Teacher Invitation'],
    CLASSROOM_OAUTH2_TXT_FILE: ['Classroom OAuth2 File', 'Classroom OAuth2 File'],
    CLIENT_SECRETS_JSON_FILE: ['Client Secrets File', 'Client Secrets File'],
    CLOUD_STORAGE_FILE: ['Cloud Storage Files', 'Cloud Storage File'],
    COLLABORATOR: ['Collaborators', 'Collaborator'],
    CONFIG_FILE: ['Config File', 'Config File'],
    CONTACT: ['Contacts', 'Contact'],
    CONTACT_GROUP: ['Contact Groups', 'Contact Group'],
    CONTACT_GROUP_NAME: ['Contact Group Names', 'Contact Group Name'],
    COPYFROM_COURSE: ['Copy From Courses', 'CopyFrom Course'],
    COURSE: ['Courses', 'Course'],
    COURSE_ALIAS: ['Course Aliases', 'Course Alias'],
    COURSE_ANNOUNCEMENT_ID: ['Course Announcement IDs', 'Course Announcement ID'],
    COURSE_ANNOUNCEMENT_STATE: ['Course Announcement States', 'Course Announcement State'],
    COURSE_MATERIAL_FORM: ['Course Material Forms', 'Course Material Form'],
    COURSE_NAME: ['Course Names', 'Course Name'],
    COURSE_STATE: ['Course States', 'Course State'],
    COURSE_SUBMISSION_ID: ['Course Submission IDs', 'Course Submission ID'],
    COURSE_SUBMISSION_STATE: ['Course Submission States', 'Course Submission State'],
    COURSE_TOPIC: ['Course Topics', 'Course Topic'],
    COURSE_TOPIC_ID: ['Course Topic IDs', 'Course Topic ID'],
    COURSE_WORK_ID: ['Course Work IDs', 'Course Work ID'],
    COURSE_WORK_STATE: ['Course Work States', 'Course Work State'],
    CREATOR_ID: ['Creator IDs', 'Creator ID'],
    CREDENTIALS: ['Credentials', 'Credentials'],
    CRITERIA: ['Criteria', 'Criteria'],
    CROS_AUE_DATES_JSON_FILE: ['ChromeOS AUE Dates File', 'ChromeOS AUE Dates File'],
    CROS_DEVICE: ['CrOS Devices', 'CrOS Device'],
    CUSTOMER_DOMAIN: ['Customer Domains', 'Customer Domain'],
    CUSTOMER_ID: ['Customer IDs', 'Customer ID'],
    DEFAULT_LANGUAGE: ['Default Language', 'Default Language'],
    DELEGATE: ['Delegates', 'Delegate'],
    DELETED_USER: ['Deleted Users', 'Deleted User'],
    DELIVERY: ['Delivery', 'Delivery'],
    DEVICE_FILE: ['Device Files', 'Device File'],
    DIRECTORY: ['Directories', 'Directory'],
    DISCOVERY_JSON_FILE: ['Discovery File', 'Discovery File'],
    DOCUMENT: ['Documents', 'Document'],
    DOMAIN: ['Domains', 'Domain'],
    DOMAIN_ALIAS: ['Domain Aliases', 'Domain Alias'],
    DRIVE_FILE: ['Drive Files', 'Drive File'],
    DRIVE_FILE_ID: ['Drive File IDs', 'Drive File ID'],
    DRIVE_FILE_NAME: ['Drive File Names', 'Drive File Name'],
    DRIVE_FILE_REVISION: ['Drive File Revisions', 'Drive File Revision'],
    DRIVE_FILE_OR_FOLDER: ['Drive Files/Folders', 'Drive File/Folder'],
    DRIVE_FILE_OR_FOLDER_ACL: ['Drive File/Folder ACLs', 'Drive File/Folder ACL'],
    DRIVE_FILE_OR_FOLDER_ID: ['Drive File/Folder IDs', 'Drive File/Folder ID'],
    DRIVE_FOLDER: ['Drive Folders', 'Drive Folder'],
    DRIVE_FOLDER_ID: ['Drive Folder IDs', 'Drive Folder ID'],
    DRIVE_FOLDER_NAME: ['Drive Folder Names', 'Drive Folder Name'],
    DRIVE_ORPHAN_FILE_OR_FOLDER: ['Drive Orphan Files/Folders', 'Drive Orphan File/Folder'],
    DRIVE_PARENT_FOLDER: ['Drive Parent Folders', 'Drive Parent Folder'],
    DRIVE_PATH: ['Drive Paths', 'Drive Path'],
    DRIVE_SETTINGS: ['Drive Settings', 'Drive Settings'],
    DRIVE_TRASH: ['Drive Trash', 'Drive Trash'],
    EMAIL: ['Email Addresses', 'Email Address'],
    EMAIL_ALIAS: ['Email Aliases', 'Email Alias'],
    EMAIL_SETTINGS: ['Email Settings', 'Email Settings'],
    ENTITY: ['Entities', 'Entity'],
    EVENT: ['Events', 'Event'],
    FEATURE: ['Features', 'Feature'],
    FIELD: ['Fields', 'Field'],
    FILE: ['Files', 'File'],
    FILTER: ['Filters', 'Filter'],
    FORWARD_ENABLED: ['Forward Enabled', 'Forward Enabled'],
    FORWARDING_ADDRESS: ['Forwarding Addresses', 'Forwarding Address'],
    GMAIL_PROFILE: ['Gmail profile', 'Gmail profile'],
    GROUP: ['Groups', 'Group'],
    GROUP_ALIAS: ['Group Aliases', 'Group Alias'],
    GROUP_EMAIL: ['Group Emails', 'Group Email'],
    GROUP_MEMBERSHIP: ['Group Memberships', 'Group Membership'],
    GROUP_SETTINGS: ['Group Settings', 'Group Settings'],
    GROUP_TREE: ['Group Trees', 'Group Tree'],
    GUARDIAN: ['Guardians', 'Guardian'],
    GUARDIAN_INVITATION: ['Guardian Invitations', 'Guardian Invitation'],
    GUARDIAN_AND_INVITATION: ['Guardians and Invitations', 'Guardian and Invitation'],
    IMAP_ENABLED: ['IMAP Enabled', 'IMAP Enabled'],
    INSTANCE: ['Instances', 'Instance'],
    ISSUER_CN: ['Issuer CNs', 'Issuer CN'],
    ITEM: ['Items', 'Item'],
    KEYBOARD_SHORTCUTS_ENABLED: ['Keyboard Shortcuts Enabled', 'Keyboard Shortcuts Enabled'],
    LABEL: ['Labels', 'Label'],
    LANGUAGE: ['Languages', 'Language'],
    LICENSE: ['Licenses', 'License'],
    MD5HASH: ['MD5 hash', 'MD5 Hash'],
    MEMBER: ['Members', 'Member'],
    MEMBER_NOT_SUSPENDED: ['Members (Not suspended)', 'Member (Not suspended)'],
    MEMBER_SUSPENDED: ['Members (Suspended)', 'Member (Suspended)'],
    MESSAGE: ['Messages', 'Message'],
    MOBILE_DEVICE: ['Mobile Devices', 'Mobile Device'],
    NAME: ['Names', 'Name'],
    NONEDITABLE_ALIAS: ['Non-Editable Aliases', 'Non-Editable Alias'],
    OAUTH2_TXT_FILE: ['Client OAuth2 File', 'Client OAuth2 File'],
    OAUTH2SERVICE_JSON_FILE: ['Service Account OAuth2 File', 'Service Account OAuth2 File'],
    ORGANIZATIONAL_UNIT: ['Organizational Units', 'Organizational Unit'],
    OWNER: ['Owners', 'Owner'],
    OWNER_ID: ['Owner IDs', 'Owner ID'],
    PAGE_SIZE: ['Page Size', 'Page Size'],
    PARENT_ORGANIZATIONAL_UNIT: ['Parent Organizational Units', 'Parent Organizational Unit'],
    PARTICIPANT: ['Participants', 'Participant'],
    PERMISSION: ['Permissions', 'Permission'],
    PERMISSION_ID: ['Permission IDs', 'Permission ID'],
    PERMITTEE: ['Permittees', 'Permittee'],
    PHOTO: ['Photos', 'Photo'],
    POP_ENABLED: ['POP Enabled', 'POP Enabled'],
    PRINTER: ['Printers', 'Printer'],
    PRINTER_ACL: ['Printer ACLs', 'Printer ACL'],
    PRINTJOB: ['Print Jobs', 'Print Job'],
    PRIVILEGE: ['Privileges', 'Privilege'],
    PRODUCT: ['Products', 'Product'],
    PROFILE_SHARING_ENABLED: ['Profile Sharing Enabled', 'Profile Sharing Enabled'],
    PROJECT: ['Projects', 'Project'],
    PROJECT_FOLDER: ['Project Folders', 'Project Folder'],
    PUBLIC_KEY: ['Public Key', 'Public Key'],
    QUERY: ['Queries', 'Query'],
    RECIPIENT: ['Recipients', 'Recipient'],
    REPORT: ['Reports', 'Report'],
    REQUEST_ID: ['Request IDs', 'Request ID'],
    RESOURCE_CALENDAR: ['Resource Calendars', 'Resource Calendar'],
    RESOURCE_ID: ['Resource IDs', 'Resource ID'],
    ROLE: ['Roles', 'Role'],
    ROLE_ASSIGNMENT_ID: ['Role Assignment IDs', 'Role Assignment ID'],
    ROW: ['Rows', 'Row'],
    SCOPE: ['Scopes', 'Scope'],
    SECTION: ['Sections', 'Section'],
    SENDAS_ADDRESS: ['SendAs Addresses', 'SendAs Address'],
    SERVICE: ['Services', 'Service'],
    SHEET: ['Sheets', 'Sheet'],
    SIGNATURE: ['Signatures', 'Signature'],
    SITE: ['Sites', 'Site'],
    SITE_ACL: ['Site ACLs', 'Site ACL'],
    SKU: ['SKUs', 'SK'],
    SMIME_ID: ['S/MIME Certificate IDs', 'S/MIME Certificate ID'],
    SNIPPETS_ENABLED: ['Preview Snippets Enabled', 'Preview Snippets Enabled'],
    SSO_KEY: ['SSO Key', 'SSO Key'],
    SSO_SETTINGS: ['SSO Settings', 'SSO Settings'],
    SOURCE_USER: ['Source Users', 'Source User'],
    SPREADSHEET: ['Spreadsheets', 'Spreadsheet'],
    SPREADSHEET_RANGE: ['Spreadsheet Ranges', 'Spreadsheet Range'],
    SUBSCRIPTION: ['Subscriptions', 'Subscription'],
    STUDENT: ['Students', 'Student'],
    TARGET_USER: ['Target Users', 'Target User'],
    TEACHER: ['Teachers', 'Teacher'],
    TEAMDRIVE: ['Shared Drives', 'Shared Drive'],
    TEAMDRIVE_ACL: ['Shared Drive ACLs', 'Shared Drive ACL'],
    TEAMDRIVE_FOLDER: ['Shared Drive Folders', 'Shared Drive Folder'],
    TEAMDRIVE_ID: ['Shared Drive IDs', 'Shared Drive ID'],
    TEAMDRIVE_NAME: ['Shared Drive Names', 'Shared Drive Name'],
    TEAMDRIVE_THEME: ['Shared Drive Themes', 'Shared Drive Theme'],
    THREAD: ['Threads', 'Thread'],
    TOKEN: ['Tokens', 'Token'],
    TRANSFER_APPLICATION: ['Transfer Applications', 'Transfer Application'],
    TRANSFER_ID: ['Transfer IDs', 'Transfer ID'],
    TRANSFER_REQUEST: ['Transfer Requests', 'Transfer Request'],
    TRASHED_EVENT: ['Trashed Events', 'Trashed Event'],
    TRUSTED_APPLICATION: ['Trusted Applications', 'Trusted Application'],
    UNICODE_ENCODING_ENABLED: ['UTF-8 Encoding Enabled', 'UTF-8 Encoding Enabled'],
    UNIQUE_ID: ['Unique IDs', 'Unique ID'],
    USER: ['Users', 'User'],
    USER_ALIAS: ['User Aliases', 'User Alias'],
    USER_EMAIL: ['User Emails', 'User Email'],
    USER_NOT_SUSPENDED: ['Users (Not suspended)', 'User (Not suspended)'],
    USER_SCHEMA: ['Schemas', 'Schema'],
    USER_SUSPENDED: ['Users (Suspended)', 'User (Suspended)'],
    VACATION: ['Vacation', 'Vacation'],
    VACATION_ENABLED: ['Vacation Enabled', 'Vacation Enabled'],
    VALUE: ['Values', 'Value'],
    VAULT_EXPORT: ['Vault Exports', 'Vault Export'],
    VAULT_HOLD: ['Vault Holds', 'Vault Hold'],
    VAULT_MATTER: ['Vault Matters', 'Vault Matter'],
    VAULT_MATTER_ID: ['Vault Matter IDs', 'Vault Matter ID'],
    WEBCLIPS_ENABLED: ['Web Clips Enabled', 'Web Clips Enabled'],
    ROLE_MANAGER: ['Managers', 'Manager'],
    ROLE_MEMBER: ['Members', 'Member'],
    ROLE_OWNER: ['Owners', 'Owner'],
    ROLE_USER: ['Users', 'User'],
    ROLE_MANAGER_MEMBER: ['Members, Managers', 'Member, Manager'],
    ROLE_MANAGER_OWNER: ['Managers, Owners', 'Manager, Owner'],
    ROLE_MEMBER_OWNER: ['Members, Owners', 'Member, Owner'],
    ROLE_MANAGER_MEMBER_OWNER: ['Members, Managers, Owners', 'Member, Manager, Owner'],
    }

  def __init__(self):
    self.entityType = None
    self.forWhom = None
    self.preQualifier = ''
    self.postQualifier = ''
    self.showTotal = False

  def SetGetting(self, entityType):
    self.entityType = entityType
    self.preQualifier = self.postQualifier = ''

  def SetGettingQuery(self, entityType, query):
    self.entityType = entityType
    self.preQualifier = ' that match query ({0})'.format(query)
    self.postQualifier = ' that matched query ({0})'.format(query)

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
      return ', may take some time on a large {0}...'.format(self.Singular(entityType))
    return ''

  def FormatEntityValueList(self, entityValueList):
    evList = []
    for j in range(0, len(entityValueList), 2):
      evList.append(self.Singular(entityValueList[j]))
      evList.append(entityValueList[j+1])
    return evList

  def TypeMessage(self, entityType, message):
    return '{0}: {1}'.format(self.Singular(entityType), message)

  def TypeName(self, entityType, entityName):
    return '{0}: {1}'.format(self.Singular(entityType), entityName)

  def TypeNameMessage(self, entityType, entityName, message):
    return '{0}: {1} {2}'.format(self.Singular(entityType), entityName, message)
