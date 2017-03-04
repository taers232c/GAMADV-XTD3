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

"""GAM action processing

"""

class GamAction(object):

# Keys into NAMES; arbitrary values but must be unique
  ADD = 'add '
  ADD_OWNERSHIP = 'adow'
  ARCHIVE = 'arch'
  BACKUP = 'back'
  CANCEL = 'canc'
  CHECK = 'chek'
  CLAIM = 'clai'
  CLAIM_OWNERSHIP = 'clow'
  COPY = 'copy'
  CREATE = 'crea'
  DELETE = 'dele'
  DELETE_EMPTY = 'delm'
  DEPROVISION = 'depr'
  DISABLE = 'disa'
  DOWNLOAD = 'down'
  EMPTY = 'empt'
  ENABLE = 'enbl'
  FETCH = 'fetc'
  FORWARD = 'forw'
  INFO = 'info'
  INITIALIZE = 'init'
  INVALIDATE = 'inva'
  LIST = 'list'
  MERGE = 'merg'
  MODIFY = 'modi'
  MOVE = 'move'
  PERFORM = 'perf'
  PRINT = 'prin'
  PURGE = 'purg'
  REENABLE = 'reen'
  REGISTER = 'regi'
  RELABEL = 'rela'
  REMOVE = 'remo'
  RENAME = 'rena'
  REPLACE = 'repl'
  REPORT = 'repo'
  RESTORE = 'rest'
  RESUBMIT = 'resu'
  RETAIN = 'reta'
  SAVE = 'save'
  SET = 'set '
  SHOW = 'show'
  SPAM = 'spam'
  SUBMIT = 'subm'
  SYNC = 'sync'
  TRANSFER = 'tran'
  TRANSFER_OWNERSHIP = 'trow'
  TRASH = 'tras'
  UNDELETE = 'unde'
  UNTRASH = 'untr'
  UPDATE = 'upda'
  UPLOAD = 'uplo'
  WATCH = 'watc'
  WIPE = 'wipe'
  # Usage:
  # ACTION_NAMES[1] n Items - Delete 10 Users
  # Item xxx ACTION_NAMES[0] - User xxx Deleted
  # These values can be translated into other languages
  _NAMES = {
    ADD: ['Added', 'Add'],
    ADD_OWNERSHIP: ['Ownership Added', 'Add Ownership'],
    ARCHIVE: ['Archived', 'Archive'],
    BACKUP: ['Backed up', 'Backup'],
    CANCEL: ['Cancelled', 'Cancel'],
    CHECK: ['Checked', 'Check'],
    CLAIM: ['Claimed', 'Claim'],
    CLAIM_OWNERSHIP: ['Ownership Claimed', 'Claim Ownership'],
    COPY: ['Copied', 'Copy'],
    CREATE: ['Created', 'Create'],
    DELETE: ['Deleted', 'Delete'],
    DELETE_EMPTY: ['Deleted', 'Delete Empty'],
    DEPROVISION: ['Deprovisioned', 'Deprovision'],
    DISABLE: ['Disabled', 'Disable'],
    DOWNLOAD: ['Downloaded', 'Download'],
    EMPTY: ['Emptied', 'Empty'],
    ENABLE: ['Enabled', 'Enable'],
    FORWARD: ['Forwarded', 'Forward'],
    INFO: ['Shown', 'Show Info'],
    INITIALIZE: ['Initialized', 'Initialize'],
    INVALIDATE: ['Invalidated', 'Invalidate'],
    LIST: ['Listed', 'List'],
    MERGE: ['Merged', 'Merge'],
    MODIFY: ['Modified', 'Modify'],
    MOVE: ['Moved', 'Move'],
    PERFORM: ['Action Performed', 'Perfrom Action'],
    PRINT: ['Printed', 'Print'],
    PURGE: ['Purged', 'Purge'],
    REENABLE: ['Reenabled', 'Reenable'],
    REGISTER: ['Registered', 'Register'],
    RELABEL: ['Relabeled', 'Relabel'],
    REMOVE: ['Removed', 'Remove'],
    RENAME: ['Renamed', 'Rename'],
    REPLACE: ['Replaced', 'Replace'],
    REPORT: ['Reported', 'Report'],
    RESTORE: ['Restored', 'Restore'],
    RESUBMIT: ['Resubmitted', 'Resubmit'],
    RETAIN: ['Retained', 'Retain'],
    SAVE: ['Saved', 'Save'],
    SET: ['Set', 'Set'],
    SHOW: ['Shown', 'Show'],
    SPAM: ['Marked as Spam', 'Mark as Spam'],
    SUBMIT: ['Submitted', 'Submit'],
    SYNC: ['Synced', 'Sync'],
    TRANSFER: ['Transferred', 'Transfer'],
    TRANSFER_OWNERSHIP: ['Ownership Transferred', 'Transfer Ownership'],
    TRASH: ['Trashed', 'Trash'],
    UNDELETE: ['Undeleted', 'Undelete'],
    UNTRASH: ['Untrashed', 'Untrash'],
    UPDATE: ['Updated', 'Update'],
    UPLOAD: ['Uploaded', 'Upload'],
    WATCH: ['Watched', 'Watch'],
    WIPE: ['Wiped', 'Wipe'],
    }
  #
  MODIFIER_FOR = 'for'
  MODIFIER_FROM = 'from'
  MODIFIER_IN = 'in'
  MODIFIER_TO = 'to'
  MODIFIER_WITH = 'with'
  MODIFIER_WITH_CONTENT_FROM = 'with content from'
  PREFIX_NOT = 'Not'
  SUFFIX_FAILED = 'Failed'

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
    return '{0} {1}'.format(self._NAMES[self.action][1], self.SUFFIX_FAILED)

  def NotPerformed(self):
    actionWords = self._NAMES[self.action][0].split(' ')
    if len(actionWords) != 2:
      return '{0} {1}'.format(self.PREFIX_NOT, self._NAMES[self.action][0])
    return '{0} {1} {2}'.format(actionWords[0], self.PREFIX_NOT, actionWords[1])

  def PerformedName(self, action):
    return self._NAMES[action][0]
