#!/usr/bin/env python

# Licensed to the StackStorm, Inc ('StackStorm') under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from lib.actions import AdminBaseAction


class AdminUserList(AdminBaseAction):
    def run(self, emails, username_alias=None):
        """
        Get list of user from admin endpoint

        Returns: An list with dict of users

        Raises:
          ValueError: 'Duo admin config not found in config' or 'Invalid factor'
        """

        _response = self.duo_admin.get_users()

        _user_list = _response
        if emails:
            _user_list = [
                user for user in _response if user.get('email') in emails
            ]
        if username_alias:
            _user_list = [
                user for user in _response
                if username_alias.lower() in user.get('aliases').values() or
                   user.get('username') == username_alias
            ]

        return _user_list


if __name__ == '__main__':
    pass