# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2022 Fetch.AI Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""Implementation of Evidence interface using REST."""


from c4epy.common.rest_client import RestClient
from c4epy.evidence.interface import Evidence
from c4epy.protos.cosmos.evidence.v1beta1 import (
    QueryAllEvidenceRequest,
    QueryAllEvidenceResponse,
    QueryEvidenceRequest,
    QueryEvidenceResponse,
)


class EvidenceRestClient(Evidence):
    """Evidence REST client."""

    API_URL = "/cosmos/evidence/v1beta1"

    def __init__(self, rest_api: RestClient) -> None:
        """
        Initialize.

        :param rest_api: RestClient api
        """
        self._rest_api = rest_api

    def Evidence(self, request: QueryEvidenceRequest) -> QueryEvidenceResponse:
        """
        Evidence queries evidence based on evidence hash.

        :param request: QueryEvidenceRequest

        :return: QueryEvidenceResponse
        """
        json_response = self._rest_api.get(
            "{}/evidence/{!r}".format(self.API_URL, request.evidence_hash),
        )
        return QueryEvidenceResponse().from_json(json_response)

    def AllEvidence(self, request: QueryAllEvidenceRequest) -> QueryAllEvidenceResponse:
        """
        AllEvidence queries all evidence.

        :param request: QueryAllEvidenceRequest

        :return: QueryAllEvidenceResponse
        """
        json_response = self._rest_api.get(f"{self.API_URL}/evidence", request)
        return QueryAllEvidenceResponse().from_json(json_response)
