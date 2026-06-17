import uuid


def test_create_project_positive(api_client):
    unique_title = f"Project_{uuid.uuid4().hex[:6]}"
    payload = {
        "title": unique_title
    }
    response = api_client.create_project(payload)

    assert response.status_code == 201
    assert response.json()["title"] == unique_title
    assert "id" in response.json()


def test_create_project_negative_empty_body(api_client):
    payload = {}
    response = api_client.create_project(payload)

    assert response.status_code == 400


def test_get_project_positive(api_client, created_project_id):
    response = api_client.get_project(created_project_id)

    assert response.status_code == 200
    assert response.json()["id"] == created_project_id


def test_get_project_negative_not_found(api_client):
    invalid_id = "non-existent-uuid-12345"
    response = api_client.get_project(invalid_id)

    assert response.status_code == 404


def test_update_project_positive(api_client, created_project_id):
    updated_title = f"Updated_{uuid.uuid4().hex[:6]}"
    payload = {
        "title": updated_title
    }
    response = api_client.update_project(created_project_id, payload)

    assert response.status_code == 200
    assert response.json()["title"] == updated_title


def test_update_project_negative_invalid_id(api_client):
    invalid_id = "00000000-0000-0000-0000-000000000000"
    payload = {"title": "New Title"}
    response = api_client.update_project(invalid_id, payload)

    assert response.status_code in [404, 400]
