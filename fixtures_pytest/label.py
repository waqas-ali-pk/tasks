import pytest

from mock_data.label import mock_label_data
from apis.models import Label


@pytest.fixture
def get_label_data():
    return {**mock_label_data}


@pytest.fixture
def test_create_label(get_label_data):
    label = Label.objects.create(**get_label_data)
    return label
