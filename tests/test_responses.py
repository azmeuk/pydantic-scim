import pytest
from pydanticscim.responses import ListResponse

from pydanticscim.user import User
from pydanticscim.group import Group
from pydanticscim.resource_type import ResourceType
from pydanticscim.service_provider import ServiceProviderConfiguration


def test_user_response(minimal_user_payload):
    payload = {
        "totalResults": 1,
        "itemsPerPage": 10,
        "startIndex": 1,
        "schemas": ["urn:ietf:params:scim:api:messages:2.0:ListResponse"],
        "Resources": [minimal_user_payload],
    }
    response = ListResponse.model_validate(payload)
    obj = response.Resources[0]
    assert isinstance(obj, User)


@pytest.mark.skip
def test_enterprise_user_response(enterprise_user_payload):
    from pydanticscim.enterprise_user import EnterpriseUser

    payload = {
        "totalResults": 1,
        "itemsPerPage": 10,
        "startIndex": 1,
        "schemas": ["urn:ietf:params:scim:api:messages:2.0:ListResponse"],
        "Resources": [enterprise_user_payload],
    }
    response = ListResponse.model_validate(payload)
    obj = response.Resources[0]
    assert isinstance(obj, User)
    assert isinstance(obj, EnterpriseUser)


def test_group_response(group_payload):
    payload = {
        "totalResults": 1,
        "itemsPerPage": 10,
        "startIndex": 1,
        "schemas": ["urn:ietf:params:scim:api:messages:2.0:ListResponse"],
        "Resources": [group_payload],
    }
    response = ListResponse.model_validate(payload)
    obj = response.Resources[0]
    assert isinstance(obj, Group)


def test_service_provider_configuration_response(
    service_provider_configuration_payload,
):
    payload = {
        "totalResults": 1,
        "itemsPerPage": 10,
        "startIndex": 1,
        "schemas": ["urn:ietf:params:scim:api:messages:2.0:ListResponse"],
        "Resources": [service_provider_configuration_payload],
    }
    response = ListResponse.model_validate(payload)
    obj = response.Resources[0]
    assert isinstance(obj, ServiceProviderConfiguration)


@pytest.mark.skip
def test_resource_type_response(resource_type_payload):
    payload = {
        "totalResults": 2,
        "itemsPerPage": 10,
        "startIndex": 1,
        "schemas": ["urn:ietf:params:scim:api:messages:2.0:ListResponse"],
        "Resources": resource_type_payload,
    }
    response = ListResponse.model_validate(payload)
    obj = response.Resources[0]
    assert isinstance(obj, ResourceType)
