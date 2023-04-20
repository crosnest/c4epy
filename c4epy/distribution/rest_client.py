# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2021 Fetch.AI Limited
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

"""Implementation of Distribution interface using REST."""


from c4epy.common.rest_client import RestClient
from c4epy.distribution.interface import Distribution
from c4epy.protos.cosmos.distribution.v1beta1 import (
    QueryCommunityPoolResponse,
    QueryDelegationRewardsRequest,
    QueryDelegationRewardsResponse,
    QueryDelegationTotalRewardsRequest,
    QueryDelegationTotalRewardsResponse,
    QueryDelegatorValidatorsRequest,
    QueryDelegatorValidatorsResponse,
    QueryDelegatorWithdrawAddressRequest,
    QueryDelegatorWithdrawAddressResponse,
    QueryParamsResponse,
    QueryValidatorCommissionRequest,
    QueryValidatorCommissionResponse,
    QueryValidatorOutstandingRewardsRequest,
    QueryValidatorOutstandingRewardsResponse,
    QueryValidatorSlashesRequest,
    QueryValidatorSlashesResponse,
)


class DistributionRestClient(Distribution):
    """Distribution REST client."""

    API_URL = "/cosmos/distribution/v1beta1"

    def __init__(self, rest_api: RestClient) -> None:
        """
        Initialize.

        :param rest_api: RestClient api
        """
        self._rest_api = rest_api

    def CommunityPool(self) -> QueryCommunityPoolResponse:
        """
        CommunityPool queries the community pool coins.

        :return: a QueryCommunityPoolResponse instance
        """
        json_response = self._rest_api.get(f"{self.API_URL}/community_pool")
        return QueryCommunityPoolResponse().from_json(json_response)

    def DelegationTotalRewards(
        self, request: QueryDelegationTotalRewardsRequest
    ) -> QueryDelegationTotalRewardsResponse:
        """
        DelegationTotalRewards queries the total rewards accrued by each validator.

        :param request: a QueryDelegationTotalRewardsRequest instance
        :return: a QueryDelegationTotalRewardsResponse instance
        """
        json_response = self._rest_api.get(
            f"{self.API_URL}/delegators/{request.delegator_address}/rewards"
        )
        return QueryDelegationTotalRewardsResponse().from_json(json_response)

    def DelegationRewards(
        self, request: QueryDelegationRewardsRequest
    ) -> QueryDelegationRewardsResponse:
        """
        DelegationRewards queries the total rewards accrued by a delegation.

        :param request: a QueryDelegationRewardsRequest instance
        :return: a QueryDelegationRewardsResponse instance
        """
        json_response = self._rest_api.get(
            f"{self.API_URL}/delegators/{request.delegator_address}/rewards/{request.validator_address}"
        )
        return QueryDelegationRewardsResponse().from_json(json_response)

    def DelegatorValidators(
        self, request: QueryDelegatorValidatorsRequest
    ) -> QueryDelegatorValidatorsResponse:
        """
        DelegatorValidators queries the validators of a delegator.

        :param request: a QueryDelegatorValidatorsRequest instance
        :return: a QueryDelegatorValidatorsResponse instance
        """
        json_response = self._rest_api.get(
            f"{self.API_URL}/delegators/{request.delegator_address}/validators"
        )
        return QueryDelegatorValidatorsResponse().from_json(json_response)

    def DelegatorWithdrawAddress(
        self, request: QueryDelegatorWithdrawAddressRequest
    ) -> QueryDelegatorWithdrawAddressResponse:
        """
        DelegatorWithdrawAddress queries withdraw address of a delegator.

        :param request: a QueryDelegatorWithdrawAddressRequest instance
        :return: a QueryDelegatorWithdrawAddressResponse instance
        """
        json_response = self._rest_api.get(
            f"{self.API_URL}/delegators/{request.delegator_address}/withdraw_address"
        )
        return QueryDelegatorWithdrawAddressResponse().from_json(json_response)

    def Params(self) -> QueryParamsResponse:
        """
        Params queries params of the distribution module.

        :return: a QueryParamsResponse instance
        """
        json_response = self._rest_api.get(f"{self.API_URL}/params")
        return QueryParamsResponse().from_json(json_response)

    def ValidatorCommission(
        self, request: QueryValidatorCommissionRequest
    ) -> QueryValidatorCommissionResponse:
        """
        ValidatorCommission queries accumulated commission for a validator.

        :param request: QueryValidatorCommissionRequest
        :return: QueryValidatorCommissionResponse
        """
        json_response = self._rest_api.get(
            f"{self.API_URL}/validators/{request.validator_address}/commission"
        )
        return QueryValidatorCommissionResponse().from_json(json_response)

    def ValidatorOutstandingRewards(
        self, request: QueryValidatorOutstandingRewardsRequest
    ) -> QueryValidatorOutstandingRewardsResponse:
        """
        ValidatorOutstandingRewards queries rewards of a validator address.

        :param request: QueryValidatorOutstandingRewardsRequest
        :return: QueryValidatorOutstandingRewardsResponse
        """
        json_response = self._rest_api.get(
            f"{self.API_URL}/validators/{request.validator_address}/outstanding_rewards"
        )
        return QueryValidatorOutstandingRewardsResponse().from_json(json_response)

    def ValidatorSlashes(
        self, request: QueryValidatorSlashesRequest
    ) -> QueryValidatorSlashesResponse:
        """
        ValidatorSlashes queries slash events of a validator.

        :param request: QueryValidatorSlashesRequest
        :return: QueryValidatorSlashesResponse
        """
        json_response = self._rest_api.get(
            f"{self.API_URL}/validators/{request.validator_address}/slashes",
            request,
            ["validatorAddress"],
        )
        return QueryValidatorSlashesResponse().from_json(json_response)
