import pytest
from rest_framework.test import APIClient

client = APIClient()


@pytest.mark.django_db
def test_register_user_success():
    res = client.post(
        "/api/auth/register/",
        data={
            "first_name": "Afshar",
            "last_name": "Sharifi",
            "requested_phone": "09012095461",
            "password": "12345678",
        },
    )
    assert res.status_code == 201
    assert res.data["first_name"] == "Afshar"
    assert res.data["last_name"] == "Sharifi"
    assert "password" not in res.data
