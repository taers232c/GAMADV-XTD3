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

# Keys into USER_PROPERTIES
CLASS = 'clas'
TITLE = 'titl'
TYPE_KEYWORDS = 'tykw'
PTKW_CL_TYPE_KEYWORD = 'ctkw'
PTKW_CL_CUSTOMTYPE_KEYWORD = 'cctk'
PTKW_ATTR_TYPE_KEYWORD = 'atkw'
PTKW_ATTR_TYPE_CUSTOM_VALUE = 'atcv'
PTKW_ATTR_CUSTOMTYPE_KEYWORD = 'actk'
PTKW_KEYWORD_LIST = 'kwli'
#
PC_ADDRESSES = 'addr'
PC_ALIASES = 'alia'
PC_ARRAY = 'arry'
PC_BOOLEAN = 'bool'
PC_EMAILS = 'emai'
PC_IMS = 'ims '
PC_NAME = 'name'
PC_NOTES = 'note'
PC_SCHEMAS = 'schm'
PC_STRING = 'stri'
PC_TIME = 'time'

PROPERTIES = {
  'primaryEmail':
    {CLASS: PC_STRING, TITLE: 'User',},
  'name':
    {CLASS: PC_NAME, TITLE: 'Name',},
  'givenName':
    {CLASS: PC_STRING, TITLE: 'First Name',},
  'familyName':
    {CLASS: PC_STRING, TITLE: 'Last Name',},
  'fullName':
    {CLASS: PC_STRING, TITLE: 'Full Name',},
  'password':
    {CLASS: PC_STRING, TITLE: 'Password',},
  'isAdmin':
    {CLASS: PC_BOOLEAN, TITLE: 'Is a Super Admin',},
  'isDelegatedAdmin':
    {CLASS: PC_BOOLEAN, TITLE: 'Is Delegated Admin',},
  'isEnrolledIn2Sv':
    {CLASS: PC_BOOLEAN, TITLE: '2-step enrolled',},
  'isEnforcedIn2Sv':
    {CLASS: PC_BOOLEAN, TITLE: '2-step enforced',},
  'agreedToTerms':
    {CLASS: PC_BOOLEAN, TITLE: 'Has Agreed to Terms',},
  'ipWhitelisted':
    {CLASS: PC_BOOLEAN, TITLE: 'IP Whitelisted',},
  'suspended':
    {CLASS: PC_BOOLEAN, TITLE: 'Account Suspended',},
  'suspensionReason':
    {CLASS: PC_STRING, TITLE: 'Suspension Reason',},
  'changePasswordAtNextLogin':
    {CLASS: PC_BOOLEAN, TITLE: 'Must Change Password',},
  'id':
    {CLASS: PC_STRING, TITLE: 'Google Unique ID',},
  'customerId':
    {CLASS: PC_STRING, TITLE: 'Customer ID',},
  'isMailboxSetup':
    {CLASS: PC_BOOLEAN, TITLE: 'Mailbox is setup',},
  'includeInGlobalAddressList':
    {CLASS: PC_BOOLEAN, TITLE: 'Included in GAL',},
  'creationTime':
    {CLASS: PC_TIME, TITLE: 'Creation Time',},
  'lastLoginTime':
    {CLASS: PC_TIME, TITLE: 'Last login time',},
  'deletionTime':
    {CLASS: PC_TIME, TITLE: 'Deletion Time',},
  'orgUnitPath':
    {CLASS: PC_STRING, TITLE: 'Google Org Unit Path',},
  'thumbnailPhotoUrl':
    {CLASS: PC_STRING, TITLE: 'Photo URL',},
  'addresses':
    {CLASS: PC_ADDRESSES, TITLE: 'Addresses',
     TYPE_KEYWORDS:
       {PTKW_CL_TYPE_KEYWORD: 'type', PTKW_CL_CUSTOMTYPE_KEYWORD: 'custom',
        PTKW_ATTR_TYPE_KEYWORD: 'type', PTKW_ATTR_TYPE_CUSTOM_VALUE: 'custom', PTKW_ATTR_CUSTOMTYPE_KEYWORD: 'customType',
        PTKW_KEYWORD_LIST: ['custom', 'home', 'other', 'work'],},},
  'emails':
    {CLASS: PC_EMAILS, TITLE: 'Other Emails',
     TYPE_KEYWORDS:
       {PTKW_CL_TYPE_KEYWORD: 'type', PTKW_CL_CUSTOMTYPE_KEYWORD: None,
        PTKW_ATTR_TYPE_KEYWORD: 'type', PTKW_ATTR_TYPE_CUSTOM_VALUE: 'custom', PTKW_ATTR_CUSTOMTYPE_KEYWORD: 'customType',
        PTKW_KEYWORD_LIST: ['custom', 'home', 'other', 'work'],},},
  'externalIds':
    {CLASS: PC_ARRAY, TITLE: 'External IDs',
     TYPE_KEYWORDS:
       {PTKW_CL_TYPE_KEYWORD: 'type', PTKW_CL_CUSTOMTYPE_KEYWORD: None,
        PTKW_ATTR_TYPE_KEYWORD: 'type', PTKW_ATTR_TYPE_CUSTOM_VALUE: 'custom', PTKW_ATTR_CUSTOMTYPE_KEYWORD: 'customType',
        PTKW_KEYWORD_LIST: ['account', 'customer', 'network', 'organization'],},},
  'ims':
    {CLASS: PC_IMS, TITLE: 'IMs',
     TYPE_KEYWORDS:
       {PTKW_CL_TYPE_KEYWORD: 'type', PTKW_CL_CUSTOMTYPE_KEYWORD: 'custom',
        PTKW_ATTR_TYPE_KEYWORD: 'type', PTKW_ATTR_TYPE_CUSTOM_VALUE: 'custom', PTKW_ATTR_CUSTOMTYPE_KEYWORD: 'customType',
        PTKW_KEYWORD_LIST: ['custom', 'home', 'other', 'work'],},},
  'notes':
    {CLASS: PC_NOTES, TITLE: 'Notes',
     TYPE_KEYWORDS:
       {PTKW_CL_TYPE_KEYWORD: 'type', PTKW_CL_CUSTOMTYPE_KEYWORD: 'type',
        PTKW_ATTR_TYPE_KEYWORD: 'contentType', PTKW_ATTR_TYPE_CUSTOM_VALUE: None, PTKW_ATTR_CUSTOMTYPE_KEYWORD: None,
        PTKW_KEYWORD_LIST: ['text_plain', 'text_html'],},},
  'organizations':
    {CLASS: PC_ARRAY, TITLE: 'Organizations',
     TYPE_KEYWORDS:
       {PTKW_CL_TYPE_KEYWORD: 'type', PTKW_CL_CUSTOMTYPE_KEYWORD: 'customtype',
        PTKW_ATTR_TYPE_KEYWORD: 'type', PTKW_ATTR_TYPE_CUSTOM_VALUE: 'custom', PTKW_ATTR_CUSTOMTYPE_KEYWORD: 'customType',
        PTKW_KEYWORD_LIST: ['domain_only', 'school', 'unknown', 'work'],},},
  'phones':
    {CLASS: PC_ARRAY, TITLE: 'Phones',
     TYPE_KEYWORDS:
       {PTKW_CL_TYPE_KEYWORD: 'type', PTKW_CL_CUSTOMTYPE_KEYWORD: 'custom',
        PTKW_ATTR_TYPE_KEYWORD: 'type', PTKW_ATTR_TYPE_CUSTOM_VALUE: 'custom', PTKW_ATTR_CUSTOMTYPE_KEYWORD: 'customType',
        PTKW_KEYWORD_LIST: ['custom', 'home', 'work', 'other',
                            'home_fax', 'work_fax', 'other_fax',
                            'mobile', 'pager',
                            'company_main', 'assistant',
                            'car', 'radio', 'isdn', 'callback',
                            'telex', 'tty_tdd', 'work_mobile',
                            'work_pager', 'main', 'grand_central'],},},
  'relations':
    {CLASS: PC_ARRAY, TITLE: 'Relations',
     TYPE_KEYWORDS:
       {PTKW_CL_TYPE_KEYWORD: 'type', PTKW_CL_CUSTOMTYPE_KEYWORD: None,
        PTKW_ATTR_TYPE_KEYWORD: 'type', PTKW_ATTR_TYPE_CUSTOM_VALUE: 'custom', PTKW_ATTR_CUSTOMTYPE_KEYWORD: 'customType',
        PTKW_KEYWORD_LIST: ['spouse', 'child', 'mother',
                            'father', 'parent', 'brother',
                            'sister', 'friend', 'relative',
                            'domestic_partner', 'manager', 'assistant',
                            'referred_by', 'partner'],},},
  'websites':
    {CLASS: PC_ARRAY, TITLE: 'Websites',
     TYPE_KEYWORDS:
       {PTKW_CL_TYPE_KEYWORD: 'type', PTKW_CL_CUSTOMTYPE_KEYWORD: None,
        PTKW_ATTR_TYPE_KEYWORD: 'type', PTKW_ATTR_TYPE_CUSTOM_VALUE: 'custom', PTKW_ATTR_CUSTOMTYPE_KEYWORD: 'customType',
        PTKW_KEYWORD_LIST: ['custom', 'home', 'work',
                            'home_page', 'ftp', 'blog',
                            'profile', 'other', 'reservations',
                            'app_install_page'],},},
  'customSchemas':
    {CLASS: PC_SCHEMAS, TITLE: 'Custom Schemas',
     TYPE_KEYWORDS:
       {PTKW_CL_TYPE_KEYWORD: 'type', PTKW_CL_CUSTOMTYPE_KEYWORD: 'custom',
        PTKW_ATTR_TYPE_KEYWORD: 'type', PTKW_ATTR_TYPE_CUSTOM_VALUE: 'custom', PTKW_ATTR_CUSTOMTYPE_KEYWORD: 'customType',
        PTKW_KEYWORD_LIST: ['custom', 'home', 'other', 'work'],},},
  'aliases': {
    CLASS: PC_ALIASES, TITLE: 'Email Aliases',},
  'nonEditableAliases': {
    CLASS: PC_ALIASES, TITLE: 'Non-Editable Aliases',},
  }
#
IM_PROTOCOLS = {
  PTKW_CL_TYPE_KEYWORD: 'protocol', PTKW_CL_CUSTOMTYPE_KEYWORD: 'custom_protocol',
  PTKW_ATTR_TYPE_KEYWORD: 'protocol', PTKW_ATTR_TYPE_CUSTOM_VALUE: 'custom_protocol', PTKW_ATTR_CUSTOMTYPE_KEYWORD: 'customProtocol',
  PTKW_KEYWORD_LIST: ['custom_protocol', 'aim', 'gtalk', 'icq', 'jabber', 'msn', 'net_meeting', 'qq', 'skype', 'xmpp', 'yahoo']
  }
