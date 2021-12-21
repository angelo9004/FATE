#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#  Copyright 2019 The FATE Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

################################################################################
#
# AUTO GENERATED TRANSFER VARIABLE CLASS. DO NOT MODIFY
#
################################################################################

from federatedml.transfer_variable.base_transfer_variable import BaseTransferVariables


class SHAPTransferVariable(BaseTransferVariables):
    def __init__(self, flowid=0):
        super().__init__(flowid)
        self.host_node_anonymous = self._create_variable(name='host_node_anonymous', src=['host'], dst=['guest'])
        self.host_anonymous_list = self._create_variable(name='host_anonymous_list', src=['host'], dst=['guest'])
        self.host_node_route = self._create_variable(name='host_node_route', src=['host'], dst=['guest'])
        self.host_feat_num = self._create_variable(name='host_feat_num', src=['host'], dst=['guest'])
        self.selected_sample_index = self._create_variable(name='selected_sample_index', src=['guest'], dst=['host'])
        self.random_sample_id = self._create_variable(name='random_sample_id', src=['guest'], dst=['host'])