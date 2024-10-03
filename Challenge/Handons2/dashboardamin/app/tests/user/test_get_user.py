def test_get_all_users(db_session):
    # Insert test data into the database
    db_session.execute("INSERT INTO users (id, name) VALUES (1, 'John Doe')")
    db_session.execute("INSERT INTO users (id, name) VALUES (2, 'Jane Doe')")
    db_session.commit()

    response = client.get("/users")
    assert response.status_code == 200
    assert len(response.json()) == 2  # Adjust this based on expected output