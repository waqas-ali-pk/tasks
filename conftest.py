import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from fixtures_pytest.task import *
from fixtures_pytest.label import *


@pytest.fixture
def test_user_email1():
    return 'admin1@aak.com'

@pytest.fixture
def test_user_email2():
    return 'admin2@aak.com'

@pytest.fixture
def test_user_password1():
    return 'passAdmin1'

@pytest.fixture
def test_user_password2():
    return 'passAdmin2'

@pytest.fixture
def test_create_admin_user1(django_user_model, test_user_email1, test_user_password1):
    user = django_user_model.objects.create(email=test_user_email1, username=test_user_email1)
    user.set_password(test_user_password1)
    user.save()
    return user

@pytest.fixture
def test_create_admin_user2(django_user_model, test_user_email2, test_user_password2):
    user = django_user_model.objects.create(email=test_user_email2, username=test_user_email2)
    user.set_password(test_user_password2)
    user.save()
    return user

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def test_user_token_jwt1(api_client, test_create_admin_user1, test_user_email1, test_user_password1):
    response = api_client.post(
        reverse('token_obtain_pair'), {'username': test_user_email1, 'password':test_user_password1 }, format='json'
    )

    return response.data['access']

@pytest.fixture
def test_user_token_jwt2(api_client, test_create_admin_user2, test_user_email2, test_user_password2):
    response = api_client.post(
        reverse('token_obtain_pair'), { 'username': test_user_email2, 'password': test_user_password2 }, format='json'
    )

    return response.data['access']

@pytest.fixture
def api_client_with_credentials1(api_client, test_user_token_jwt1):
    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + test_user_token_jwt1)
    return api_client

@pytest.fixture
def api_client_with_credentials2(api_client, test_user_token_jwt2):
    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + test_user_token_jwt2)
    return api_client
