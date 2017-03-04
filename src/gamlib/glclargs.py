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

"""GAM command line argument processing

"""

# Concatenate list members, any item containing spaces is enclosed in ""
def QuotedArgumentList(items):
  qstr = ''
  for item in items:
    if item and (item.find(' ') == -1) and (item.find(',') == -1):
      qstr += item
    else:
      qstr += '"'+item+'"'
    qstr += ' '
  return qstr[:-1] if len(qstr) > 0 else ''

class GamCLArgs(object):

# GAM entity types as specified on the command line
  ENTITY_COURSEPARTICIPANTS = 'courseparticipants'
  ENTITY_CROS = 'cros'
  ENTITY_CROS_QUERY = 'crosquery'
  ENTITY_CROS_OU = 'cros_ou'
  ENTITY_CROS_OU_AND_CHILDREN = 'cros_ou_and_children'
  ENTITY_CROS_OUS = 'cros_ous'
  ENTITY_CROS_OUS_AND_CHILDREN = 'cros_ous_and_children'
  ENTITY_GROUP = 'group'
  ENTITY_GROUPS = 'groups'
  ENTITY_GROUP_USERS = 'group_users'
  ENTITY_LICENSES = 'licenses'
  ENTITY_OU = 'ou'
  ENTITY_OU_AND_CHILDREN = 'ou_and_children'
  ENTITY_OUS = 'ous'
  ENTITY_OUS_AND_CHILDREN = 'ous_and_children'
  ENTITY_QUERY = 'query'
  ENTITY_STUDENTS = 'students'
  ENTITY_TEACHERS = 'teachers'
  ENTITY_USER = 'user'
  ENTITY_USERS = 'users'
#
  CROS_ENTITIES = [
    ENTITY_CROS,
    ENTITY_CROS_QUERY,
    ENTITY_CROS_OU,
    ENTITY_CROS_OU_AND_CHILDREN,
    ENTITY_CROS_OUS,
    ENTITY_CROS_OUS_AND_CHILDREN,
    ]
  USER_ENTITIES = [
    ENTITY_COURSEPARTICIPANTS,
    ENTITY_GROUP,
    ENTITY_GROUPS,
    ENTITY_GROUP_USERS,
    ENTITY_LICENSES,
    ENTITY_OU,
    ENTITY_OU_AND_CHILDREN,
    ENTITY_OUS,
    ENTITY_OUS_AND_CHILDREN,
    ENTITY_QUERY,
    ENTITY_STUDENTS,
    ENTITY_TEACHERS,
    ENTITY_USER,
    ENTITY_USERS,
    ]
# Aliases for CL entity types
  ENTITY_ALIAS_MAP = {
    'crosorg': ENTITY_CROS_OU,
    'crosorg_and_child': ENTITY_CROS_OU_AND_CHILDREN,
    'crosorg_and_children': ENTITY_CROS_OU_AND_CHILDREN,
    'crosorgs': ENTITY_CROS_OUS,
    'crosorgs_and_child': ENTITY_CROS_OUS_AND_CHILDREN,
    'crosorgs_and_children': ENTITY_CROS_OUS_AND_CHILDREN,
    'crosou_and_child': ENTITY_CROS_OU_AND_CHILDREN,
    'crosou_and_childen': ENTITY_CROS_OU_AND_CHILDREN,
    'crosous_and_child': ENTITY_CROS_OUS_AND_CHILDREN,
    'cros_org': ENTITY_CROS_OU,
    'cros_org_and_child': ENTITY_CROS_OU_AND_CHILDREN,
    'cros_org_and_children': ENTITY_CROS_OU_AND_CHILDREN,
    'cros_orgs': ENTITY_CROS_OUS,
    'cros_orgs_and_child': ENTITY_CROS_OUS_AND_CHILDREN,
    'cros_orgs_and_children': ENTITY_CROS_OUS_AND_CHILDREN,
    'cros_ou_and_child': ENTITY_CROS_OU_AND_CHILDREN,
    'cros_ou_and_childen': ENTITY_CROS_OU_AND_CHILDREN,
    'cros_ous_and_child': ENTITY_CROS_OUS_AND_CHILDREN,
    'license': ENTITY_LICENSES,
    'licence': ENTITY_LICENSES,
    'licences': ENTITY_LICENSES,
    'org': ENTITY_OU,
    'org_and_child': ENTITY_OU_AND_CHILDREN,
    'org_and_children': ENTITY_OU_AND_CHILDREN,
    'orgs': ENTITY_OUS,
    'orgs_and_child': ENTITY_OUS_AND_CHILDREN,
    'orgs_and_children': ENTITY_OUS_AND_CHILDREN,
    'ou_and_child': ENTITY_OU_AND_CHILDREN,
    'ous_and_child': ENTITY_OUS_AND_CHILDREN,
    }
# CL entity source selectors
  ENTITY_SELECTOR_ALL = 'all'
  ENTITY_SELECTOR_CSV = 'csv'
  ENTITY_SELECTOR_CSVFILE = 'csvfile'
  ENTITY_SELECTOR_FILE = 'file'
  ENTITY_SELECTOR_DATAFILE = 'datafile'
  ENTITY_SELECTOR_CROSCSV = 'croscsv'
  ENTITY_SELECTOR_CROSCSVFILE = 'croscsvfile'
  ENTITY_SELECTOR_CROSFILE = 'crosfile'
  ENTITY_SELECTOR_CSVKMD = 'csvkmd'
  ENTITY_SELECTOR_CSVSUBKEY = 'csvsubkey'
  ENTITY_SELECTOR_CSVDATA = 'csvdata'
  ENTITY_SELECTOR_CSVCROS = 'csvcros'
#
  CROS_ENTITY_SELECTORS = [
    ENTITY_SELECTOR_CROSCSV,
    ENTITY_SELECTOR_CROSCSVFILE,
    ENTITY_SELECTOR_CROSFILE,
    ]
  ENTITY_SELECTORS = [
    ENTITY_SELECTOR_ALL,
    ENTITY_SELECTOR_CSV,
    ENTITY_SELECTOR_CSVFILE,
    ENTITY_SELECTOR_FILE,
    ENTITY_SELECTOR_DATAFILE,
    ENTITY_SELECTOR_CSVKMD,
    ENTITY_SELECTOR_CSVSUBKEY,
    ]
  CSVCROS_ENTITY_SELECTORS = [
    ENTITY_SELECTOR_CSVCROS,
    ]
  CSVDATA_ENTITY_SELECTORS = [
    ENTITY_SELECTOR_CSVDATA,
    ]
# Allowed values for CL source selector all
  CROS_ENTITY_SELECTOR_ALL_SUBTYPES = [
    ENTITY_CROS,
    ]
  USER_ENTITY_SELECTOR_ALL_SUBTYPES = [
    ENTITY_USERS,
    ]
#
  ENTITY_ALL_CROS = ENTITY_SELECTOR_ALL+' '+ENTITY_CROS
  ENTITY_ALL_USERS = ENTITY_SELECTOR_ALL+' '+ENTITY_USERS
#
  ENTITY_SELECTOR_ALL_SUBTYPES_MAP = {
    ENTITY_CROS: ENTITY_ALL_CROS,
    ENTITY_USERS: ENTITY_ALL_USERS,
    }
# Allowed values for CL source selector args, datafile, csvkmd
  CROS_ENTITY_SELECTOR_DATAFILE_CSVKMD_SUBTYPES = [
    ENTITY_CROS,
    ENTITY_CROS_OUS,
    ENTITY_CROS_OUS_AND_CHILDREN,
    ]
  USER_ENTITY_SELECTOR_DATAFILE_CSVKMD_SUBTYPES = [
    ENTITY_USERS,
    ENTITY_GROUPS,
    ENTITY_GROUP_USERS,
    ENTITY_OUS,
    ENTITY_OUS_AND_CHILDREN,
    ENTITY_COURSEPARTICIPANTS,
    ENTITY_STUDENTS,
    ENTITY_TEACHERS,
    ]
# Command line batch/csv/loop keywords
  GAM_CMD = 'gam'
  COMMIT_BATCH_CMD = 'commit-batch'
  LOOP_CMD = 'loop'
# Command line select/config/redirect arguments
  SELECT_CMD = 'select'
  CONFIG_CMD = 'config'
  REDIRECT_CMD = 'redirect'
  GAM_META_COMMANDS = [SELECT_CMD, CONFIG_CMD, REDIRECT_CMD,]
# Command line arguments
  ARG_ACL = 'acl'
  ARG_ACLS = 'acls'
  ARG_ADMIN = 'admin'
  ARG_ADMINS = 'admins'
  ARG_ADMINROLES = 'adminroles'
  ARG_ALIAS = 'alias'
  ARG_ALIASES = 'aliases'
  ARG_ASP = 'asp'
  ARG_ASPS = 'asps'
  ARG_BACKUPCODES = 'backupcodes'
  ARG_CALATTENDEES = 'calattendees'
  ARG_CALENDAR = 'calendar'
  ARG_CALENDARS = 'calendars'
  ARG_CALENDARACL = 'calendaracl'
  ARG_CALENDARACLS = 'calendaracls'
  ARG_CALSETTINGS = 'calsettings'
  ARG_CONTACT = 'contact'
  ARG_CONTACTS = 'contacts'
  ARG_CONTACT_GROUP = 'contactgroup'
  ARG_CONTACT_GROUPS = 'contactgroups'
  ARG_COURSE = 'course'
  ARG_COURSES = 'courses'
  ARG_COURSE_PARTICIPANTS = 'course-participants'
  ARG_CROS = 'cros'
  ARG_CROSES = 'croses'
  ARG_CUSTOMER = 'customer'
  ARG_DATA_TRANSFER = 'datatransfer'
  ARG_DATA_TRANSFERS = 'datatransfers'
  ARG_DELEGATE = 'delegate'
  ARG_DELEGATES = 'delegates'
  ARG_DOMAIN = 'domain'
  ARG_DOMAINS = 'domains'
  ARG_DOMAIN_ALIAS = 'domainalias'
  ARG_DOMAIN_ALIASES = 'domainaliases'
  ARG_DRIVE = 'drive'
  ARG_DRIVEACTIVITY = 'driveactivity'
  ARG_DRIVEFILE = 'drivefile'
  ARG_DRIVEFILEACL = 'drivefileacl'
  ARG_DRIVEFILEACLS = 'drivefileacls'
  ARG_DRIVESETTINGS = 'drivesettings'
  ARG_DRIVETRASH = 'drivetrash'
  ARG_EMPTYDRIVEFOLDERS = 'emptydrivefolders'
  ARG_EVENT = 'event'
  ARG_EVENTS = 'events'
  ARG_FILEINFO = 'fileinfo'
  ARG_FILELIST = 'filelist'
  ARG_FILEPATH = 'filepath'
  ARG_FILEREVISIONS = 'filerevisions'
  ARG_FILETREE = 'filetree'
  ARG_FILTER = 'filter'
  ARG_FILTERS = 'filters'
  ARG_FORWARD = 'forward'
  ARG_FORWARDINGADDRESS = 'forwardingaddress'
  ARG_FORWARDINGADDRESSES = 'forwardingaddresses'
  ARG_GAL = 'gal'
  ARG_GMAILPROFILE = 'gmailprofile'
  ARG_GPLUSPROFILE = 'gplusprofile'
  ARG_GROUP = 'group'
  ARG_GROUPS = 'groups'
  ARG_GROUP_MEMBERS = 'group-members'
  ARG_GUARDIAN = 'guardian'
  ARG_GUARDIANS = 'guardians'
  ARG_GUARDIAN_INVITATION = 'guardianinvitation'
  ARG_GUARDIAN_INVITATIONS = 'guardianinvitations'
  ARG_IMAP = 'imap'
  ARG_INSTANCE = 'instance'
  ARG_LABEL = 'label'
  ARG_LABELS = 'labels'
  ARG_LABELSETTINGS = 'labelsettings'
  ARG_LICENSE = 'license'
  ARG_LICENSES = 'licenses'
  ARG_LOGO = 'logo'
  ARG_MESSAGE = 'message'
  ARG_MESSAGES = 'messages'
  ARG_MOBILE = 'mobile'
  ARG_MOBILES = 'mobiles'
  ARG_NOTE = 'note'
  ARG_NOTIFICATION = 'notification'
  ARG_ORG = 'org'
  ARG_ORGS = 'orgs'
  ARG_ORGTREE = 'orgtree'
  ARG_OWNERSHIP = 'ownership'
  ARG_PERMISSIONS = 'permissions'
  ARG_PHOTO = 'photo'
  ARG_POP = 'pop'
  ARG_PRINTER = 'printer'
  ARG_PRINTERS = 'printers'
  ARG_PRINTJOBS = 'printjobs'
  ARG_PROFILE = 'profile'
  ARG_PROJECT = 'project'
  ARG_PROJECTS = 'projects'
  ARG_RESELLERCUSTOMER = 'resellercustomer'
  ARG_RESELLERCUSTOMERS = 'resellercustomers'
  ARG_RESELLERSUBSCRIPTION = 'resellersubscription'
  ARG_RESELLERSUBSCRIPTIONS = 'resellersubscriptions'
  ARG_RESOLDCUSTOMER = 'resoldcustomer'
  ARG_RESOLDCUSTOMERS = 'resoldcustomers'
  ARG_RESOLDSUBSCRIPTION = 'resoldsubscription'
  ARG_RESOLDSUBSCRIPTIONS = 'resoldsubscriptions'
  ARG_RESOURCE = 'resource'
  ARG_RESOURCES = 'resources'
  ARG_SCHEMA = 'schema'
  ARG_SCHEMAS = 'schemas'
  ARG_SENDAS = 'sendas'
  ARG_SERVICEACCOUNT = 'serviceaccount'
  ARG_SIGNATURE = 'signature'
  ARG_SITE = 'site'
  ARG_SITES = 'sites'
  ARG_SITEACL = 'siteacl'
  ARG_SITEACLS = 'siteacls'
  ARG_SITEACTIVITY = 'siteactivity'
  ARG_SMIME = 'smime'
  ARG_SMIMES = 'smimes'
  ARG_THREAD = 'thread'
  ARG_THREADS = 'threads'
  ARG_TOKEN = 'token'
  ARG_TOKENS = 'tokens'
  ARG_TRANSFERAPPS = 'transferapps'
  ARG_USER = 'user'
  ARG_USERS = 'users'
  ARG_VACATION = 'vacation'
  ARG_VERIFY = 'verify'
# Lists of arguments for use in checkArgumentPresent
  CLEAR_NONE_ARGUMENT = ['clear', 'none',]
  CLIENTID_ARGUMENT = ['clientid',]
  COLUMN_DELIMITER_ARGUMENT = ['columndelimiter',]
  DATA_ARGUMENT = ['data',]
  FILE_ARGUMENT = ['file',]
  FROM_ARGUMENT = ['from',]
  LOGO_ARGUMENT = ['logo',]
  MOVE_ADD_ARGUMENT = ['move', 'add',]
  MULTIVALUE_ARGUMENT = ['multivalued', 'multivalue', 'value', 'multinonempty']
  NOINFO_ARGUMENT = ['noinfo',]
  NOTSUSPENDED_ARGUMENT = ['notsuspended',]
  ORG_OU_ARGUMENT = ['org', 'ou',]
  PRIMARY_NOTPRIMARY_CHOICE_MAP = {'primary': True, 'notprimary': False}
  QUERY_ARGUMENT = ['query',]
  SHOWTITLES_ARGUMENT = ['showtitles',]
  TODRIVE_ARGUMENT = ['todrive',]
  TO_ARGUMENT = ['to',]
  UNSTRUCTURED_FORMATTED_ARGUMENT = ['unstructured', 'formatted',]

# Object BNF names
  OB_ACCESS_TOKEN = 'AccessToken'
  OB_ACL_SCOPE = 'ACLScope'
  OB_ACL_SCOPE_ENTITY = 'ACLScopeEntity'
  OB_ARGUMENT = 'argument'
  OB_ASP_ID = 'AspID'
  OB_CALENDAR_ENTITY = 'CalendarEntity'
  OB_CALENDAR_ITEM = 'CalendarItem'
  OB_CHAR_SET = 'CharacterSet'
  OB_CIDR_NETMASK = 'CIDRnetmask'
  OB_CLIENT_ID = 'ClientID'
  OB_CONTACT_EMAIL_TYPE = 'ContactEmailType'
  OB_CONTACT_ENTITY = 'ContactEntity'
  OB_CONTACT_GROUP_ENTITY = 'ContactGroupEntity'
  OB_CONTACT_GROUP_ITEM = 'ContactGroupItem'
  OB_COURSE_ALIAS = 'CourseAlias'
  OB_COURSE_ALIAS_ENTITY = 'CourseAliasEntity'
  OB_COURSE_ENTITY = 'CourseEntity'
  OB_COURSE_ID = 'CourseID'
  OB_CROS_DEVICE_ENTITY = 'CrOSDeviceEntity'
  OB_CROS_ENTITY = 'CrOSEntity'
  OB_CUSTOMER_ID = 'CustomerID'
  OB_CUSTOMER_AUTH_TOKEN = 'CustomerAuthToken'
  OB_DELIMITER = 'Delimiter'
  OB_DOMAIN_ALIAS = 'DomainAlias'
  OB_DOMAIN_NAME = 'DomainName'
  OB_DOMAIN_NAME_ENTITY = 'DomainNameEntity'
  OB_DRIVE_FILE_ENTITY = 'DriveFileEntity'
  OB_DRIVE_FILE_ID = 'DriveFileID'
  OB_DRIVE_FILE_NAME = 'DriveFileName'
  OB_DRIVE_FILE_PERMISSION_ENTITY = 'DriveFilePermissionEntity'
  OB_DRIVE_FILE_PERMISSION_ID = 'DriveFilePermissionID'
  OB_DRIVE_FILE_PERMISSION_ID_ENTITY = 'DriveFilePermissionIDEntity'
  OB_DRIVE_FOLDER_ID = 'DriveFolderID'
  OB_DRIVE_FOLDER_ID_LIST = 'DriveFolderIDList'
  OB_DRIVE_FOLDER_NAME = 'DriveFolderName'
  OB_EMAIL_ADDRESS = 'EmailAddress'
  OB_EMAIL_ADDRESS_ENTITY = 'EmailAddressEntity'
  OB_EMAIL_ADDRESS_OR_UID = 'EmailAaddress|UniqueID'
  OB_ENTITY = 'Entity'
  OB_ENTITY_TYPE = 'EntityType'
  OB_EVENT_ID = 'EventID'
  OB_EVENT_ID_ENTITY = 'EventIDEntity'
  OB_FIELD_NAME = 'FieldName'
  OB_FIELD_NAME_LIST = "FieldNameList"
  OB_FILE_NAME = 'FileName'
  OB_FILE_NAME_FIELD_NAME = OB_FILE_NAME+'(:'+OB_FIELD_NAME+')+'
  OB_FILE_NAME_OR_URL = 'FileName|URL'
  OB_FILE_PATH = 'FilePath'
  OB_FILTER_ID_ENTITY = 'FilterIDEntity'
  OB_FORMAT_LIST = 'FormatList'
  OB_GAM_ARGUMENT_LIST = 'GAM argument list'
  OB_GROUP_ENTITY = 'GroupEntity'
  OB_GROUP_ITEM = 'GroupItem'
  OB_GUARDIAN_INVITATION_ID = 'GuardianInvitationID'
  OB_GUARDIAN_ITEM = 'GuardianItem'
  OB_GUARDIAN_STATE_LIST = 'GuardianStateList'
  OB_HOST_NAME = 'HostName'
  OB_JOB_ID = 'JobID'
  OB_JOB_OR_PRINTER_ID = 'JobID|PrinterID'
  OB_LABEL_NAME = 'LabelName'
  OB_LABEL_REPLACEMENT = 'LabelReplacement'
  OB_MESSAGE_ID = 'MessageID'
  OB_MOBILE_DEVICE_ENTITY = 'MobileDeviceEntity'
  OB_MOBILE_ENTITY = 'MobileEntity'
  OB_NAME = 'Name'
  OB_NOTIFICATION_ID = 'NotificationID'
  OB_ORGUNIT_ENTITY = 'OrgUnitEntity'
  OB_ORGUNIT_ITEM = 'OrgUnitItem'
  OB_ORGUNIT_PATH = 'OrgUnitPath'
  OB_PARAMETER_KEY = 'ParameterKey'
  OB_PARAMETER_VALUE = 'ParameterValue'
  OB_PASSWORD = 'Password'
  OB_PHOTO_FILENAME_PATTERN = 'FilenameNamePattern'
  OB_PRINTER_ID = 'PrinterID'
  OB_PRINTER_ID_ENTITY = 'PrinterIDEntity'
  OB_PRINTJOB_AGE = 'PrintJobAge'
  OB_PRINTJOB_ID = 'PrintJobID'
  OB_PRODUCT_ID = 'ProductID'
  OB_PRODUCT_ID_LIST = 'ProductIDList'
  OB_PROPERTY_KEY = 'PropertyKey'
  OB_PROPERTY_VALUE = 'PropertyValue'
  OB_QUERY = 'Query'
  OB_RECURRENCE = 'RRULE EXRULE RDATE and EXDATE lines'
  OB_REQUEST_ID = 'RequestID'
  OB_RESOURCE_ENTITY = 'ResourceEntity'
  OB_RESOURCE_ID = 'ResourceID'
  OB_RE_PATTERN = 'REPattern'
  OB_ROLE_ASSIGNMENT_ID = 'RoleAssignmentId'
  OB_ROLE_ID = 'RoleId'
  OB_ROLE_LIST = 'RoleList'
  OB_SCHEMA_ENTITY = 'SchemaEntity'
  OB_SCHEMA_NAME = 'SchemaName'
  OB_SCHEMA_NAME_FIELD_NAME = 'SchemaName.FieldName'
  OB_SCHEMA_NAME_LIST = 'SchemaNameList'
  OB_SECTION_NAME = 'SectionName'
  OB_SERVICE_NAME = 'ServiceName'
  OB_SITE_ENTITY = 'SiteEntity'
  OB_SKU_ID = 'SKUID'
  OB_SKU_ID_LIST = 'SKUIDList'
  OB_SMIME_ID = 'S/MIMEID'
  OB_STRING = 'String'
  OB_STUDENT_ITEM = 'StudentItem'
  OB_TAG = 'Tag'
  OB_THREAD_ID = 'ThreadID'
  OB_TRANSFER_ID = 'TransferID'
  OB_URI = 'URI'
  OB_URL = 'URL'
  OB_USER_ENTITY = 'UserEntity'
  OB_USER_ITEM = 'UserItem'

#
# Error message types; keys into ARGUMENT_ERROR_NAMES; arbitrary values but must be unique
  ARGUMENT_BLANK = 'blnk'
  ARGUMENT_EMPTY = 'empt'
  ARGUMENT_EXTRANEOUS = 'extr'
  ARGUMENT_INVALID = 'inva'
  ARGUMENT_MISSING = 'miss'
# ARGUMENT_ERROR_NAMES[0] is plural,ARGUMENT_ERROR_NAMES[1] is singular
# These values can be translated into other languages
  ARGUMENT_ERROR_NAMES = {
    ARGUMENT_BLANK: ['Blank arguments', 'Blank argument'],
    ARGUMENT_EMPTY: ['Empty arguments', 'Empty argument'],
    ARGUMENT_EXTRANEOUS: ['Extra arguments', 'Extra argument'],
    ARGUMENT_INVALID: ['Invalid arguments', 'Invalid argument'],
    ARGUMENT_MISSING: ['Missing arguments', 'Missing argument'],
    }

  def __init__(self):
    self.argv = []
    self.argvI = 0
    self.argvLen = 0
    self.argvIsave = 0

# Initialize arguments
  def InitializeArguments(self, args):
    self.argv = args[:]
    self.argvI = 1
    self.argvLen = len(self.argv)

# Any arguments remaining
  def ArgumentsRemaining(self):
    return self.argvI < self.argvLen

# Multiple arguments remaining
  def MultipleArgumentsRemaining(self):
    return not self.argvI+1 == self.argvLen

# All arguments
  def AllArguments(self):
    return self.argv

# Specific argument
  def Argument(self, index):
    return self.argv[index]

# Current argument
  def Current(self):
    return self.argv[self.argvI]

# Previous argument
  def Previous(self):
    return self.argv[self.argvI-1]

# Remaining arguments
  def Remaining(self):
    return self.argv[self.argvI:]

# Argument location
  def Location(self):
    return self.argvI

# Advance to next argument
  def Advance(self):
    self.argvI += 1

# Backup to previous argument
  def Backup(self):
    self.argvI -= 1

# Save argument location
  def SaveLocation(self):
    self.argvIsave = self.argvI

# Reset argument location
  def ResetLocation(self, offset):
    self.argvI = self.argvIsave+offset

# Set argument location
  def SetLocation(self, location):
    self.argvI = location

# Mark bad argument in command line
  def CommandLineWithBadArgumentMarked(self, extraneous):
    if extraneous:
      return 'Command: {0} >>>{1}<<<\n'.format(QuotedArgumentList(self.argv[:self.argvI]),
                                                QuotedArgumentList(self.argv[self.argvI:]))
    if self.ArgumentsRemaining():
      return 'Command: {0} >>>{1}<<< {2}\n'.format(QuotedArgumentList(self.argv[:self.argvI]),
                                                    QuotedArgumentList([self.argv[self.argvI]]),
                                                    QuotedArgumentList(self.argv[self.argvI+1:]))
    return 'Command: {0} >>><<<\n'.format(QuotedArgumentList(self.argv))
