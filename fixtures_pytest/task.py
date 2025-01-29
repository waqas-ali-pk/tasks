import pytest

from mock_data.task import mock_task_data
from apis.models import Task

@pytest.fixture
def get_task_data():
    return {**mock_task_data}

@pytest.fixture
def test_create_task(get_task_data):
    task = Task.objects.create(**get_task_data)
    return task
