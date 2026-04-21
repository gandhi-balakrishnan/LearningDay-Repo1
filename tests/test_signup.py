def test_signup_success(client):
    email = "newstudent@mergington.edu"
    activity = "Chess Club"
    # Ensure not already signed up
    client.delete(f"/activities/{activity}/signup?email={email}")
    response = client.post(f"/activities/{activity}/signup?email={email}")
    assert response.status_code == 200
    data = response.json()
    assert f"Signed up {email} for {activity}" in data["message"]
    # Clean up
    client.delete(f"/activities/{activity}/signup?email={email}")

def test_signup_duplicate(client):
    email = "dupstudent@mergington.edu"
    activity = "Chess Club"
    client.delete(f"/activities/{activity}/signup?email={email}")
    client.post(f"/activities/{activity}/signup?email={email}")
    response = client.post(f"/activities/{activity}/signup?email={email}")
    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"]
    # Clean up
    client.delete(f"/activities/{activity}/signup?email={email}")

def test_signup_nonexistent_activity(client):
    response = client.post("/activities/Nonexistent/signup?email=someone@mergington.edu")
    assert response.status_code == 404
    assert "Activity not found" in response.json()["detail"]
