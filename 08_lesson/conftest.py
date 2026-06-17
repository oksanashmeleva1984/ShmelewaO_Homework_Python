import pytest
import uuid
from api_client import ProjectApiClient


@pytest.fixture(scope="session")
def api_client():
    return ProjectApiClient()


@pytest.fixture
def created_project_id(api_client):
    unique_name = f"Autotest_Project_{uuid.uuid4().hex[:6]}"
    payload = {"title": unique_name}
    response = api_client.create_project(payload)
    assert response.status_code == 201, (
        f"Не удалось подготовить тест-окружение:"
        f"{response.text}"
    )

    project_id = response.json().get("id")
    yield project_id
