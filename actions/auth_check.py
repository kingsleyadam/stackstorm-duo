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

from st2actions.runners.pythonrunner import Action
from lib.actions import AuthAction


class Check(AuthAction):
    def run(self):
        """
        Ping the Duo Platorm.

        Returns: An dict with info returned by Duo.

        Raises:
          RuntimeError: On Invalid keys.
        """

        try:
            data = self.duo_auth.check()
        except RuntimeError, e:
            print e
            raise RuntimeError("Check failed! '%s'" % e)
        else:
            return data
