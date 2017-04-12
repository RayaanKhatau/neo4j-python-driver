#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Copyright (c) 2002-2017 "Neo Technology,"
# Network Engine for Objects in Lund AB [http://neotechnology.com]
#
# This file is part of Neo4j.
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

# tag::config-trust-import[]
from neo4j.v1 import GraphDatabase
# end::config-trust-import[]

class ConfigTrustExample:
    # tag::config-trust[]
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password),
                Config.build().withTrustStrategy( Config.TrustStrategy.trustSystemCertificates() ).toConfig() )
    # end::config-trust[]

    def close(self):
        self._driver.close();
