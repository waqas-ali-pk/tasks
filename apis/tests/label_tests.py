import pytest
from django.urls import reverse
from rest_framework import status

from mock_data.label import mock_label_data


@pytest.mark.django_db
def test_get_labels_admin1(
    test_create_admin_user1,
    test_create_admin_user2,
    test_create_label,
    api_client_with_credentials1,
):
    response = api_client_with_credentials1.get(reverse("label-list"))

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0].get("owner") == test_create_admin_user1.pk


@pytest.mark.django_db
def test_get_labels_admin2(
    test_create_admin_user1,
    test_create_admin_user2,
    test_create_label,
    api_client_with_credentials2,
):
    response = api_client_with_credentials2.get(reverse("label-list"))

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 0


@pytest.mark.django_db
def test_create_label_by_api_admin1(
    test_create_admin_user1, test_create_admin_user2, api_client_with_credentials1
):
    response = api_client_with_credentials1.post(
        reverse("label-list"), {**mock_label_data, "owner": 1}, format="json"
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data.get("name") == mock_label_data.get("name")
    assert response.data.get("owner") == test_create_admin_user1.pk


@pytest.mark.django_db
def test_get_label_by_api_admin1(
    test_create_admin_user1,
    test_create_admin_user2,
    test_create_label,
    api_client_with_credentials1,
):
    response = api_client_with_credentials1.get(
        reverse("label-detail", kwargs={"pk": test_create_label.pk})
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.data.get("name") == test_create_label.name
    assert response.data.get("owner") == test_create_admin_user1.pk


@pytest.mark.django_db
def test_update_label_by_api_admin1(
    test_create_admin_user1,
    test_create_admin_user2,
    test_create_label,
    api_client_with_credentials1,
):
    updated_label = {**mock_label_data, "owner": 1}
    updated_label["name"] = updated_label["name"] + " Updated"
    response = api_client_with_credentials1.put(
        reverse("label-detail", kwargs={"pk": test_create_label.pk}),
        updated_label,
        format="json",
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.data.get("name") == updated_label["name"]
    assert response.data.get("owner") == test_create_admin_user1.pk


@pytest.mark.django_db
def test_partial_update_label_by_api_admin1(
    test_create_admin_user1,
    test_create_admin_user2,
    test_create_label,
    api_client_with_credentials1,
):
    updated_label = {"name": "Label 1 Updated"}
    response = api_client_with_credentials1.patch(
        reverse("label-detail", kwargs={"pk": test_create_label.pk}),
        updated_label,
        format="json",
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.data.get("name") == updated_label["name"]
    assert response.data.get("owner") == test_create_admin_user1.pk


@pytest.mark.django_db
def test_delete_label_by_api_admin1(
    test_create_admin_user1,
    test_create_admin_user2,
    test_create_label,
    api_client_with_credentials1,
):
    response = api_client_with_credentials1.delete(
        reverse("label-detail", kwargs={"pk": test_create_label.pk})
    )

    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_delete_label_by_api_when_no_task_exist_admin1(
    test_create_admin_user1, test_create_admin_user2, api_client_with_credentials1
):
    response = api_client_with_credentials1.delete(
        reverse("label-detail", kwargs={"pk": 1})
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND
