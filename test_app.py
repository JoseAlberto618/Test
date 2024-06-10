from app import app

def test_home():
    with app.test_client() as client:
        rv = client.get('/')
        assert rv.status_code == 200
        assert rv.data == b"Hello, World!"
