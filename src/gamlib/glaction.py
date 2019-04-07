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

"""GAM action processing

"""

class GamAction(object):

# Keys into NAMES; arbitrary values but must be unique
  ACCEPT = 'acpt'
  ADD = 'add '
  ADD_PREVIEW = 'addp'
  APPEND = 'apnd'
  ARCHIVE = 'arch'
  BACKUP = 'back'
  CANCEL = 'canc'
  CHECK = 'chek'
  CLAIM = 'clai'
  CLAIM_OWNERSHIP = 'clow'
  CLEAR = 'clea'
  CLOSE = 'clos'
  COLLECT = 'collect'
  COPY = 'copy'
  CREATE = 'crea'
  DELETE = 'dele'
  DELETE_EMPTY = 'delm'
  DEPROVISION = 'depr'
  DISABLE = 'disa'
  DOWNLOAD = 'down'
  EMPTY = 'empt'
  ENABLE = 'enbl'
  EXPORT = 'expo'
  EXTRACT = 'extr'
  FETCH = 'fetc'
  FORWARD = 'forw'
  IMPORT = 'impo'
  INFO = 'info'
  INITIALIZE = 'init'
  INSERT = 'insr'
  INVALIDATE = 'inva'
  LIST = 'list'
  MERGE = 'merg'
  MODIFY = 'modi'
  MOVE = 'move'
  PERFORM = 'perf'
  PRINT = 'prin'
  PROCESS = 'proc'
  PURGE = 'purg'
  REENABLE = 'reen'
  REGISTER = 'regi'
  RELABEL = 'rela'
  REMOVE = 'remo'
  REMOVE_PREVIEW = 'remp'
  RENAME = 'rena'
  REOPEN = 'reop'
  REPLACE = 'repl'
  REPORT = 'repo'
  RESTORE = 'rest'
  RESUBMIT = 'res'
  RETAIN = 'reta'
  RETRIEVE_DATA = 'retd'
  SAVE = 'save'
  SENDEMAIL = 'send'
  SET = 'set '
  SHOW = 'show'
  SPAM = 'spam'
  SUBMIT = 'subm'
  SUSPEND = 'susp'
  SYNC = 'sync'
  TRANSFER = 'tran'
  TRANSFER_OWNERSHIP = 'trow'
  TRASH = 'tras'
  UNDELETE = 'unde'
  UNSUSPEND = 'uns'
  UNTRASH = 'untr'
  UPDATE = 'upda'
  UPDATE_PREVIEW = 'updp'
  UPLOAD = 'uplo'
  UNZIP = 'unzi'
  USE = 'use '
  VERIFY = 'vrfy'
  WATCH = 'watc'
  WIPE = 'wipe'
  # Usage:
  # ACTION_NAMES[1] n Items - Delete 10 Users
  # Item xxx ACTION_NAMES[0] - User xxx Deleted
  # These values can be translated into other languages
  _NAMES = {
    ACCEPT: [u'Accepted', u'Accept'],
    ADD: [u'Added', u'Add'],
    ADD_PREVIEW: [u'Added (Preview)', u'Add (Preview)'],
    APPEND: [u'Appended', u'Append'],
    ARCHIVE: [u'Archived', u'Archive'],
    BACKUP: [u'Backed up', u'Backup'],
    CANCEL: [u'Cancelled', u'Cancel'],
    CHECK: [u'Checked', u'Check'],
    CLAIM: [u'Claimed', u'Claim'],
    CLAIM_OWNERSHIP: [u'Ownership Claimed', u'Claim Ownership'],
    CLEAR: [u'Cleared', u'Clear'],
    CLOSE: [u'Closed', u'Close'],
    COLLECT: [u'Collected', u'Collect'],
    COPY: [u'Copied', u'Copy'],
    CREATE: [u'Created', u'Create'],
    DELETE: [u'Deleted', u'Delete'],
    DELETE_EMPTY: [u'Deleted', u'Delete Empty'],
    DEPROVISION: [u'Deprovisioned', u'Deprovision'],
    DISABLE: [u'Disabled', u'Disable'],
    DOWNLOAD: [u'Downloaded', u'Download'],
    EMPTY: [u'Emptied', u'Empty'],
    ENABLE: [u'Enabled', u'Enable'],
    EXPORT: [u'Exported', u'Export'],
    EXTRACT: [u'Extracted', u'Extract'],
    FORWARD: [u'Forwarded', u'Forward'],
    IMPORT: [u'Imported', u'Import'],
    INFO: [u'Shown', u'Show Info'],
    INITIALIZE: [u'Initialized', u'Initialize'],
    INSERT: [u'Inserted', u'Insert'],
    INVALIDATE: [u'Invalidated', u'Invalidate'],
    LIST: [u'Listed', u'List'],
    MERGE: [u'Merged', u'Merge'],
    MODIFY: [u'Modified', u'Modify'],
    MOVE: [u'Moved', u'Move'],
    PERFORM: [u'Action Performed', u'Perform Action'],
    PRINT: [u'Printed', u'Print'],
    PROCESS: [u'Processed', u'Process'],
    PURGE: [u'Purged', u'Purge'],
    REENABLE: [u'Reenabled', u'Reenable'],
    REGISTER: [u'Registered', u'Register'],
    RELABEL: [u'Relabeled', u'Relabel'],
    REMOVE: [u'Removed', u'Remove'],
    REMOVE_PREVIEW: [u'Removed (Preview)', u'Remove (Preview)'],
    RENAME: [u'Renamed', u'Rename'],
    REOPEN: [u'Reopened', u'Reopen'],
    REPLACE: [u'Replaced', u'Replace'],
    REPORT: [u'Reported', u'Report'],
    RESTORE: [u'Restored', u'Restore'],
    RESUBMIT: [u'Resubmitted', u'Resubmit'],
    RETAIN: [u'Retained', u'Retain'],
    RETRIEVE_DATA: [u'Data Retrieved', u'Retrieve Data'],
    SAVE: [u'Saved', u'Save'],
    SENDEMAIL: [u'Email Sent', u'Send Email'],
    SET: [u'Set', u'Set'],
    SHOW: [u'Shown', u'Show'],
    SPAM: [u'Marked as Spam', u'Mark as Spam'],
    SUBMIT: [u'Submitted', u'Submit'],
    SUSPEND: [u'Suspended', u'Suspend'],
    SYNC: [u'Synced', u'Sync'],
    TRANSFER: [u'Transferred', u'Transfer'],
    TRANSFER_OWNERSHIP: [u'Ownership Transferred', u'Transfer Ownership'],
    TRASH: [u'Trashed', u'Trash'],
    UNDELETE: [u'Undeleted', u'Undelete'],
    UNSUSPEND: [u'Unsuspended', u'Unsuspend'],
    UNTRASH: [u'Untrashed', u'Untrash'],
    UNZIP: [u'Unzipped', u'Unzip'],
    UPDATE: [u'Updated', u'Update'],
    UPDATE_PREVIEW: [u'Updated (Preview)', u'Update (Preview)'],
    UPLOAD: [u'Uploaded', u'Upload'],
    USE: [u'Used', u'Use'],
    VERIFY: [u'Verified', u'Verify'],
    WATCH: [u'Watched', u'Watch'],
    WIPE: [u'Wiped', u'Wipe'],
    }
  #
  MODIFIER_CONTENTS_WITH = u'contents with'
  MODIFIER_FOR = u'for'
  MODIFIER_FROM = u'from'
  MODIFIER_IN = u'in'
  MODIFIER_INTO = u'into'
  MODIFIER_TO = u'to'
  MODIFIER_WITH = u'with'
  MODIFIER_WITH_CONTENT_FROM = u'with content from'
  PREFIX_NOT = u'Not'
  SUFFIX_FAILED = u'Failed'

  def __init__(self):
    self.action = None

  def Set(self, action):
    self.action = action

  def Get(self):
    return self.action

  def ToPerform(self):
    return self._NAMES[self.action][1]

  def Performed(self):
    return self._NAMES[self.action][0]

  def Failed(self):
    return u'{0} {1}'.format(self._NAMES[self.action][1], self.SUFFIX_FAILED)

  def NotPerformed(self):
    actionWords = self._NAMES[self.action][0].split(u' ')
    if len(actionWords) != 2:
      return u'{0} {1}'.format(self.PREFIX_NOT, self._NAMES[self.action][0])
    return u'{0} {1} {2}'.format(actionWords[0], self.PREFIX_NOT, actionWords[1])

  def PerformedName(self, action):
    return self._NAMES[action][0]

  def csvFormat(self):
    return self.action == self.PRINT
