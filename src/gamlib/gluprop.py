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

"""GAM user properties

"""

# notes
# a|b|c
# getKeywordAttribute(CUSTOM_TYPE_NOCUSTOM, attrdict)

#CUSTOM_TYPE_NOCUSTOM = {
#    PTKW_CL_TYPE_KEYWORD: u'type',
#    PTKW_CL_CUSTOM_KEYWORD: None,
#    PTKW_ATTR_TYPE_KEYWORD: u'type',
#    PTKW_ATTR_TYPE_CUSTOM_VALUE: None,
#    PTKW_ATTR_CUSTOMTYPE_KEYWORD: None,
#    PTKW_KEYWORD_LIST: [u'a', u'b', u'c']
#    }

# addresses, ims
# type a|b|c|([custom] <String>)
# getChoice([CUSTOM_TYPE_CUSTOM[PTKW_CL_TYPE_KEYWORD]])
# getKeywordAttribute(CUSTOM_TYPE_CUSTOM, attrdict)

# emails, externalids, relations, websites
# [type] a|b|c|([custom] <String>)
# getChoice([CUSTOM_TYPE_CUSTOM[PTKW_CL_TYPE_KEYWORD]], defaultChoice=None)
# getKeywordAttribute(CUSTOM_TYPE_IMPLICIT, attrdict)

# locations, phones
# type a|b|c|([custom] <String>)
# if argument == CUSTOM_TYPE_CUSTOM[PTKW_CL_TYPE_KEYWORD]:
#   getKeywordAttribute(CUSTOM_TYPE_CUSTOM, attrdict)

#CUSTOM_TYPE_CUSTOM = {
#    PTKW_CL_TYPE_KEYWORD: u'type',
#    PTKW_CL_CUSTOM_KEYWORD: u'custom',
#    PTKW_ATTR_TYPE_KEYWORD: u'type',
#    PTKW_ATTR_TYPE_CUSTOM_VALUE: u'custom',
#    PTKW_ATTR_CUSTOMTYPE_KEYWORD: u'customType',
#    PTKW_KEYWORD_LIST: [u'custom', u'a', u'b', u'c']
#    }

# organizations
# (type a|b|c|([custom] <String>)) | (custom_type <String>)
# if argument == CUSTOM_TYPE_DIFFERENT_KEYWORD[PTKW_CL_TYPE_KEYWORD]:
#   getKeywordAttribute(CUSTOM_TYPE_DIFFERENT_KEYWORD, attrdict)
# elif argument == CUSTOM_TYPE_DIFFERENT_KEYWORD[PTKW_CL_CUSTOM_KEYWORD]:
#   attrdict[CUSTOM_TYPE_DIFFERENT_KEYWORD[PTKW_ATTR_CUSTOMTYPE_KEYWORD]] = getValue()

#CUSTOM_TYPE_DIFFERENT_KEYWORD = {
#    PTKW_CL_TYPE_KEYWORD: u'type',
#    PTKW_CL_CUSTOM_KEYWORD: u'custom',
#    PTKW_CL_CUSTOMTYPE_KEYWORD: u'custom_type',
#    PTKW_ATTR_TYPE_KEYWORD: u'type',
#    PTKW_ATTR_TYPE_CUSTOM_VALUE: u'custom',
#    PTKW_ATTR_CUSTOMTYPE_KEYWORD: u'customType',
#    PTKW_KEYWORD_LIST: [u'custom', u'a', u'b', u'c']
#    }

# Keys into USER_PROPERTIES
CLASS = u'clas'
TITLE = u'titl'
TYPE_KEYWORDS = u'tykw'
PTKW_CL_TYPE_KEYWORD = u'ctkw'
PTKW_CL_CUSTOM_KEYWORD = u'ccuk'
PTKW_CL_CUSTOMTYPE_KEYWORD = u'cctk'
PTKW_ATTR_TYPE_KEYWORD = u'atkw'
PTKW_ATTR_TYPE_CUSTOM_VALUE = u'atcv'
PTKW_ATTR_CUSTOMTYPE_KEYWORD = u'actk'
PTKW_KEYWORD_LIST = u'kwli'
#
PC_ADDRESSES = u'addr'
PC_ALIASES = u'alia'
PC_ARRAY = u'arry'
PC_BOOLEAN = u'bool'
PC_EMAILS = u'emai'
PC_GENDER = u'gndr'
PC_IMS = u'ims '
PC_LANGUAGES = u'lang'
PC_LOCATIONS = 'loca'
PC_NAME = u'name'
PC_NOTES = u'note'
PC_POSIX = u'posi'
PC_SCHEMAS = u'schm'
PC_SSH = u'ssh '
PC_STRING = u'stri'
PC_TIME = u'time'

PROPERTIES = {
  u'primaryEmail':
    {CLASS: PC_STRING, TITLE: u'User',},
  u'name':
    {CLASS: PC_NAME, TITLE: u'Name',},
  u'givenName':
    {CLASS: PC_STRING, TITLE: u'First Name',},
  u'familyName':
    {CLASS: PC_STRING, TITLE: u'Last Name',},
  u'fullName':
    {CLASS: PC_STRING, TITLE: u'Full Name',},
  u'languages':
    {CLASS: PC_LANGUAGES, TITLE: u'Languages',},
  u'languageCode':
    {CLASS: PC_LANGUAGES, TITLE: u'Languages',},
  u'customLanguage':
    {CLASS: PC_LANGUAGES, TITLE: u'Custom Languages',},
  u'password':
    {CLASS: PC_STRING, TITLE: u'Password',},
  u'hashFunction':
    {CLASS: PC_STRING, TITLE: u'Hash Function',},
  u'isAdmin':
    {CLASS: PC_BOOLEAN, TITLE: u'Is a Super Admin',},
  u'isDelegatedAdmin':
    {CLASS: PC_BOOLEAN, TITLE: u'Is Delegated Admin',},
  u'isEnrolledIn2Sv':
    {CLASS: PC_BOOLEAN, TITLE: u'2-step enrolled',},
  u'isEnforcedIn2Sv':
    {CLASS: PC_BOOLEAN, TITLE: u'2-step enforced',},
  u'agreedToTerms':
    {CLASS: PC_BOOLEAN, TITLE: u'Has Agreed to Terms',},
  u'ipWhitelisted':
    {CLASS: PC_BOOLEAN, TITLE: u'IP Whitelisted',},
  u'archived':
    {CLASS: PC_BOOLEAN, TITLE: u'Account Archived',},
  u'suspended':
    {CLASS: PC_BOOLEAN, TITLE: u'Account Suspended',},
  u'suspensionReason':
    {CLASS: PC_STRING, TITLE: u'Suspension Reason',},
  u'changePasswordAtNextLogin':
    {CLASS: PC_BOOLEAN, TITLE: u'Must Change Password',},
  u'id':
    {CLASS: PC_STRING, TITLE: u'Google Unique ID',},
  u'customerId':
    {CLASS: PC_STRING, TITLE: u'Customer ID',},
  u'isMailboxSetup':
    {CLASS: PC_BOOLEAN, TITLE: u'Mailbox is setup',},
  u'includeInGlobalAddressList':
    {CLASS: PC_BOOLEAN, TITLE: u'Included in GAL',},
  u'creationTime':
    {CLASS: PC_TIME, TITLE: u'Creation Time',},
  u'lastLoginTime':
    {CLASS: PC_TIME, TITLE: u'Last login time',},
  u'deletionTime':
    {CLASS: PC_TIME, TITLE: u'Deletion Time',},
  u'orgUnitPath':
    {CLASS: PC_STRING, TITLE: u'Google Org Unit Path',},
  u'thumbnailPhotoUrl':
    {CLASS: PC_STRING, TITLE: u'Photo URL',},
  u'addresses':
    {CLASS: PC_ADDRESSES, TITLE: u'Addresses',
     TYPE_KEYWORDS:
       {PTKW_CL_TYPE_KEYWORD: u'type', PTKW_CL_CUSTOM_KEYWORD: u'custom',
        PTKW_ATTR_TYPE_KEYWORD: u'type', PTKW_ATTR_TYPE_CUSTOM_VALUE: u'custom', PTKW_ATTR_CUSTOMTYPE_KEYWORD: u'customType',
        PTKW_KEYWORD_LIST: [u'custom', u'home', u'other', u'work'],},},
  u'emails':
    {CLASS: PC_EMAILS, TITLE: u'Other Emails',
     TYPE_KEYWORDS:
       {PTKW_CL_TYPE_KEYWORD: u'type', PTKW_CL_CUSTOM_KEYWORD: u'custom',
        PTKW_ATTR_TYPE_KEYWORD: u'type', PTKW_ATTR_TYPE_CUSTOM_VALUE: u'custom', PTKW_ATTR_CUSTOMTYPE_KEYWORD: u'customType',
        PTKW_KEYWORD_LIST: [u'custom', u'home', u'other', u'work'],},},
  u'externalIds':
    {CLASS: PC_ARRAY, TITLE: u'External IDs',
     TYPE_KEYWORDS:
       {PTKW_CL_TYPE_KEYWORD: u'type', PTKW_CL_CUSTOM_KEYWORD: u'custom',
        PTKW_ATTR_TYPE_KEYWORD: u'type', PTKW_ATTR_TYPE_CUSTOM_VALUE: u'custom', PTKW_ATTR_CUSTOMTYPE_KEYWORD: u'customType',
        PTKW_KEYWORD_LIST: [u'custom', u'account', u'customer', u'login_id', u'network', u'organization'],},},
  u'gender':
    {CLASS: PC_GENDER, TITLE: u'Gender',
     TYPE_KEYWORDS:
       {PTKW_CL_TYPE_KEYWORD: u'type', PTKW_CL_CUSTOM_KEYWORD: u'other',
        PTKW_ATTR_TYPE_KEYWORD: u'type', PTKW_ATTR_TYPE_CUSTOM_VALUE: u'other', PTKW_ATTR_CUSTOMTYPE_KEYWORD: u'customGender',
        PTKW_KEYWORD_LIST: [u'male', u'female', u'other', u'unknown'],},},
  u'ims':
    {CLASS: PC_IMS, TITLE: u'IMs',
     TYPE_KEYWORDS:
       {PTKW_CL_TYPE_KEYWORD: u'type', PTKW_CL_CUSTOM_KEYWORD: u'custom',
        PTKW_ATTR_TYPE_KEYWORD: u'type', PTKW_ATTR_TYPE_CUSTOM_VALUE: u'custom', PTKW_ATTR_CUSTOMTYPE_KEYWORD: u'customType',
        PTKW_KEYWORD_LIST: [u'custom', u'home', u'other', u'work'],},},
  u'keywords':
    {CLASS: PC_ARRAY, TITLE: u'Keywords',
     TYPE_KEYWORDS:
       {PTKW_CL_TYPE_KEYWORD: u'type', PTKW_CL_CUSTOM_KEYWORD: u'custom',
        PTKW_ATTR_TYPE_KEYWORD: u'type', PTKW_ATTR_TYPE_CUSTOM_VALUE: u'custom', PTKW_ATTR_CUSTOMTYPE_KEYWORD: u'customType',
        PTKW_KEYWORD_LIST: [u'custom', u'occupation', u'outlook'],},},
  u'locations':
    {CLASS: PC_LOCATIONS, TITLE: u'Locations',
     TYPE_KEYWORDS:
       {PTKW_CL_TYPE_KEYWORD: u'type', PTKW_CL_CUSTOM_KEYWORD: u'custom',
        PTKW_ATTR_TYPE_KEYWORD: u'type', PTKW_ATTR_TYPE_CUSTOM_VALUE: u'custom', PTKW_ATTR_CUSTOMTYPE_KEYWORD: u'customType',
        PTKW_KEYWORD_LIST: [u'custom', u'default', u'desk'],},},
  u'notes':
    {CLASS: PC_NOTES, TITLE: u'Notes',
     TYPE_KEYWORDS:
       {PTKW_CL_TYPE_KEYWORD: u'type', PTKW_CL_CUSTOM_KEYWORD: None,
        PTKW_ATTR_TYPE_KEYWORD: u'contentType', PTKW_ATTR_TYPE_CUSTOM_VALUE: None, PTKW_ATTR_CUSTOMTYPE_KEYWORD: None,
        PTKW_KEYWORD_LIST: [u'text_plain', u'text_html'],},},
  u'organizations':
    {CLASS: PC_ARRAY, TITLE: u'Organizations',
     TYPE_KEYWORDS:
       {PTKW_CL_TYPE_KEYWORD: u'type', PTKW_CL_CUSTOM_KEYWORD: u'custom', PTKW_CL_CUSTOMTYPE_KEYWORD: u'customtype',
        PTKW_ATTR_TYPE_KEYWORD: u'type', PTKW_ATTR_TYPE_CUSTOM_VALUE: None, PTKW_ATTR_CUSTOMTYPE_KEYWORD: u'customType',
        PTKW_KEYWORD_LIST: [u'custom', u'domain_only', u'school', u'unknown', u'work'],},},
  u'phones':
    {CLASS: PC_ARRAY, TITLE: u'Phones',
     TYPE_KEYWORDS:
       {PTKW_CL_TYPE_KEYWORD: u'type', PTKW_CL_CUSTOM_KEYWORD: u'custom',
        PTKW_ATTR_TYPE_KEYWORD: u'type', PTKW_ATTR_TYPE_CUSTOM_VALUE: u'custom', PTKW_ATTR_CUSTOMTYPE_KEYWORD: u'customType',
        PTKW_KEYWORD_LIST: [u'custom', u'home', u'work', u'other',
                            u'home_fax', u'work_fax', u'other_fax',
                            u'mobile', u'pager',
                            u'company_main', u'assistant',
                            u'car', u'radio', u'isdn', u'callback',
                            u'telex', u'tty_tdd', u'work_mobile',
                            u'work_pager', u'main', u'grand_central'],},},
  u'posixAccounts':
    {CLASS: PC_POSIX, TITLE: u'Posix Accounts',},
  u'relations':
    {CLASS: PC_ARRAY, TITLE: u'Relations',
     TYPE_KEYWORDS:
       {PTKW_CL_TYPE_KEYWORD: u'type', PTKW_CL_CUSTOM_KEYWORD: u'custom',
        PTKW_ATTR_TYPE_KEYWORD: u'type', PTKW_ATTR_TYPE_CUSTOM_VALUE: u'custom', PTKW_ATTR_CUSTOMTYPE_KEYWORD: u'customType',
        PTKW_KEYWORD_LIST: [u'custom', u'spouse', u'child', u'mother',
                            u'father', u'parent', u'brother',
                            u'sister', u'friend', u'relative',
                            u'domestic_partner', u'partner',
                            u'manager', u'dotted_line_manager',
                            u'assistant', u'admin_assistant', u'exec_assistant',
                            u'referred_by'],},},
  u'sshPublicKeys':
    {CLASS: PC_SSH, TITLE: u'SSH Public Keys',},
  u'websites':
    {CLASS: PC_ARRAY, TITLE: u'Websites',
     TYPE_KEYWORDS:
       {PTKW_CL_TYPE_KEYWORD: u'type', PTKW_CL_CUSTOM_KEYWORD: u'custom',
        PTKW_ATTR_TYPE_KEYWORD: u'type', PTKW_ATTR_TYPE_CUSTOM_VALUE: u'custom', PTKW_ATTR_CUSTOMTYPE_KEYWORD: u'customType',
        PTKW_KEYWORD_LIST: [u'custom', u'home', u'work',
                            u'home_page', u'ftp', u'blog',
                            u'profile', u'other', u'reservations',
                            u'app_install_page'],},},
  u'customSchemas':
    {CLASS: PC_SCHEMAS, TITLE: u'Custom Schemas',
     TYPE_KEYWORDS:
       {PTKW_CL_TYPE_KEYWORD: u'type', PTKW_CL_CUSTOM_KEYWORD: u'custom',
        PTKW_ATTR_TYPE_KEYWORD: u'type', PTKW_ATTR_TYPE_CUSTOM_VALUE: u'custom', PTKW_ATTR_CUSTOMTYPE_KEYWORD: u'customType',
        PTKW_KEYWORD_LIST: [u'custom', u'home', u'other', u'work'],},},
  u'aliases': {
    CLASS: PC_ALIASES, TITLE: u'Email Aliases',},
  u'nonEditableAliases': {
    CLASS: PC_ALIASES, TITLE: u'NonEditable Aliases',},
  }
#
IM_PROTOCOLS = {
  PTKW_CL_TYPE_KEYWORD: u'protocol', PTKW_CL_CUSTOM_KEYWORD: u'custom_protocol',
  PTKW_ATTR_TYPE_KEYWORD: u'protocol', PTKW_ATTR_TYPE_CUSTOM_VALUE: u'custom_protocol', PTKW_ATTR_CUSTOMTYPE_KEYWORD: u'customProtocol',
  PTKW_KEYWORD_LIST: [u'custom_protocol', u'aim', u'gtalk', u'icq', u'jabber', u'msn', u'net_meeting', u'qq', u'skype', u'xmpp', u'yahoo']
  }
