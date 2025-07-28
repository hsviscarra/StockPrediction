import pytest
from tests.fixtures.sample_data import generate_sample_sp500_data


@pytest.fixture
def sample_sp500_data():
    return generate_sample_sp500_data()
