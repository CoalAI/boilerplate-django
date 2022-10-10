import pytest
from rest_framework.test import APIClient

client = APIClient()


@pytest.mark.django_db
def test_test_api():
    assert True
