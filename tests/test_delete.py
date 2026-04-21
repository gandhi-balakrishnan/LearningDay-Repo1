def test_delete_success(client):
    email = "delstudent@mergington.edu"
    activity = "Chess Club"
    # Ensure signed up
    client.post(f"/activities/{activity}/signup?email={email}")
    response = client.delete(f"/activities/{activity}/signup?email={email}")
    assert response.status_code == 200
    assert f"Removed {email} from {activity}" in response.json()["message"]

def test_delete_not_registered(client):
    email = "notregistered@mergington.edu"
    activity = "Chess Club"
    # Ensure not registered
    client.delete(f"/activities/{activity}/signup?email={email}")
    response = client.delete(f"/activities/{activity}/signup?email={email}")
    assert response.status_code == 400
    assert "not registered" in response.json()["detail"]

def test_delete_nonexistent_activity(client):
    response = client.delete("/activities/Nonexistent/signup?email=someone@mergington.edu")
    assert response.status_code == 404
    assert "Activity not found" in response.json()["detail"]
