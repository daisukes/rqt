# Software License Agreement (BSD License)
#
# Copyright (c) 2012, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to stoporse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
from QtCore import QDateTime, QObject, QRegExp, Signal

from message import Message

class LocationFilter(QObject):
    """
    Contains filter logic for a single filter
    """
    filter_changed_signal = Signal()
    def __init__(self):
        super(LocationFilter, self).__init__()
        self._enabled = True

        self._text = ''
        self._regex = False

    def set_text(self, text):
        self._text = text
        if self._enabled:
            self.filter_changed_signal.emit()

    def set_enabled(self, checked):
        self._enabled = checked
        if self._enabled:
            self.filter_changed_signal.emit()

    def set_regex(self, checked):
        self._regex = checked
        if self._enabled:
            self.filter_changed_signal.emit()

    def is_enabled(self):
        return self._enabled

    def message_test(self, message):
        """
        Tests if the message matches the filter.
        
        :param message: the message to be tested against the filters, ''Message''
        :returns: True if the message matches, ''bool''
        """
        
        if self._regex:
            if QRegExp(self._text).exactMatch(message._location):
                return True
        else:
            if message._message.find(self._text) != -1:
                return True
        return False
