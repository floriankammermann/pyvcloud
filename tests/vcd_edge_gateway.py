# VMware vCloud Director Python SDK
# Copyright (c) 2017 VMware, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

from pyvcloud.vcd.org import Org
from pyvcloud.vcd.test import TestCase
from pyvcloud.vcd.vdc import VDC


class TestEdgeGateway(TestCase):

    def test_001_list_edge_gateways(self):
        logged_in_org = self.client.get_org()
        org = Org(self.client, resource=logged_in_org)
        v = org.get_vdc(self.config['vcd']['vdc'])
        vdc = VDC(self.client, resource=v)
        edge_gateways = vdc.list_edge_gateways()
        assert len(edge_gateways) > 0

    def test_002_get_edge_gateway(self):
        logged_in_org = self.client.get_org()
        org = Org(self.client, resource=logged_in_org)
        v = org.get_vdc(self.config['vcd']['vdc'])
        vdc = VDC(self.client, resource=v)
        edge_gateway = vdc.get_edge_gateway(self.config['vcd']['edge_gateway'])
        assert edge_gateway.get('name') == self.config['vcd']['edge_gateway']

    def test_003_get_edge_gateway_not_existent(self):
        logged_in_org = self.client.get_org()
        org = Org(self.client, resource=logged_in_org)
        v = org.get_vdc(self.config['vcd']['vdc'])
        vdc = VDC(self.client, resource=v)
        with self.assertRaisesRegex(Exception, 'Edge Gateway not found \'' +
                                    self.config['vcd']['edge_gateway'] +
                                    '_not_existent\'') as exception:
            assert exception
            vdc.get_edge_gateway(self.config['vcd']['edge_gateway'] +
                                 '_not_existent')

    def test_004_get_nat_rules(self):
        logged_in_org = self.client.get_org()
        org = Org(self.client, resource=logged_in_org)
        v = org.get_vdc(self.config['vcd']['vdc'])
        vdc = VDC(self.client, resource=v)
        nat_rules = vdc.get_nat_rules(self.config['vcd']['edge_gateway'])
        assert len(nat_rules) > 0


if __name__ == '__main__':
    unittest.main()
