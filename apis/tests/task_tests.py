import pytest
from django.urls import reverse
from rest_framework import status

from mock_data.task import mock_task_data


@pytest.mark.django_db
def test_get_tasks_admin1(
    test_create_admin_user1,
    test_create_admin_user2,
    test_create_task,
    api_client_with_credentials1,
):
    response = api_client_with_credentials1.get(reverse("task-list"))

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0].get("owner") == test_create_admin_user1.pk


@pytest.mark.django_db
def test_get_tasks_admin2(
    test_create_admin_user1,
    test_create_admin_user2,
    test_create_task,
    api_client_with_credentials2,
):
    response = api_client_with_credentials2.get(reverse("task-list"))

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 0


@pytest.mark.django_db
def test_create_task_by_api_admin1(
    test_create_admin_user1, test_create_admin_user2, api_client_with_credentials1
):
    response = api_client_with_credentials1.post(
        reverse("task-list"), {**mock_task_data, "owner": 1}, format="json"
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data.get("title") == mock_task_data.get("title")
    assert response.data.get("owner") == test_create_admin_user1.pk


@pytest.mark.django_db
def test_get_task_by_api_admin1(
    test_create_admin_user1,
    test_create_admin_user2,
    test_create_task,
    api_client_with_credentials1,
):
    response = api_client_with_credentials1.get(
        reverse("task-detail", kwargs={"pk": test_create_task.pk})
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.data.get("title") == test_create_task.title
    assert response.data.get("owner") == test_create_admin_user1.pk


@pytest.mark.django_db
def test_update_task_by_api_admin1(
    test_create_admin_user1,
    test_create_admin_user2,
    test_create_task,
    api_client_with_credentials1,
):
    updated_task = {**mock_task_data, "owner": 1}
    updated_task["title"] = updated_task["title"] + " Updated"
    response = api_client_with_credentials1.put(
        reverse("task-detail", kwargs={"pk": test_create_task.pk}),
        updated_task,
        format="json",
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.data.get("title") == updated_task["title"]
    assert response.data.get("owner") == test_create_admin_user1.pk


@pytest.mark.django_db
def test_partial_update_task_by_api_admin1(
    test_create_admin_user1,
    test_create_admin_user2,
    test_create_task,
    api_client_with_credentials1,
):
    updated_task = {"title": "Task 1 Updated"}
    response = api_client_with_credentials1.patch(
        reverse("task-detail", kwargs={"pk": test_create_task.pk}),
        updated_task,
        format="json",
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.data.get("title") == updated_task["title"]
    assert response.data.get("owner") == test_create_admin_user1.pk


@pytest.mark.django_db
def test_delete_task_by_api_admin1(
    test_create_admin_user1,
    test_create_admin_user2,
    test_create_task,
    api_client_with_credentials1,
):
    response = api_client_with_credentials1.delete(
        reverse("task-detail", kwargs={"pk": test_create_task.pk})
    )

    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_delete_task_by_api_when_no_task_exist_admin1(
    test_create_admin_user1, test_create_admin_user2, api_client_with_credentials1
):
    response = api_client_with_credentials1.delete(
        reverse("task-detail", kwargs={"pk": 1})
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND
