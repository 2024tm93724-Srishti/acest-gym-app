from app import create_app

def test_home():
    app = create_app()
    client = app.test_client()
    res = client.get('/')
    assert res.status_code == 200

def test_members():
    app = create_app()
    client = app.test_client()
    res = client.get('/members')
    assert b"Aman" in res.data

def test_plans():
    app = create_app()
    client = app.test_client()
    res = client.get('/plans')
    assert b"Basic" in res.data