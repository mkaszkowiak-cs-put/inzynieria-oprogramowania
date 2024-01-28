def test_tests_are_running():
    assert True


def test_docs(client, db_session):
    response = client.get("/api/v1/docs")
    assert response.status_code == 200, response.text
