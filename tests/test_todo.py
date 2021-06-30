from fastapi.testclient import TestClient
from todo.database import Base, get_db
from main import app

client = TestClient(app)

def temp_db(f):
    def func(SessionLocal, *args, **kwargs):
        def override_get_db():
            try:
                db = SessionLocal()
                yield db
            finally:
                db.close()
        app.dependency_overrides[get_db] = override_get_db
        f(*args, **kwargs)
        app.dependency_overrides[get_db] = get_db
    return func


@temp_db
def test_create_todo():
    response = client.post(
        '/todos',
        json={'title': 'Foo Bar', 'text': 'The Foo Barters'},
    )
    assert response.status_code == 200
    assert response.json() == {
        'id': 1,
        'text': 'The Foo Barters',
        'title': 'Foo Bar'
    }

@temp_db
def test_read_todo():
    response = client.get('/todos/1')
    assert response.status_code == 200
    assert response.json() == {
        'id': 1,
        'text': 'The Foo Barters',
        'title': 'Foo Bar'
    }

@temp_db
def test_read_todo():
    response = client.get('/todos/11111111')
    assert response.status_code == 404
    assert response.json() == {'detail': 'Todo not found'}

@temp_db
def test_read_todos():
    response = client.post(
        '/todos',
        json={'title': 'Foo Bar', 'text': 'The Foo Barters'},
    )

    response = client.get('/todos')
    assert response.status_code == 200
    assert response.json() == [{
        'id': 1,
        'text': 'The Foo Barters',
        'title': 'Foo Bar'
    }]

@temp_db
def test_update_todo():
    response = client.post(
        '/todos',
        json={'title': 'Foo Bar', 'text': 'The Foo Barters'},
    )

    response = client.put(
        '/todos/1',
        json={'title': 'String', 'text': 'String'},
    )
    assert response.status_code == 200
    assert response.json() == {
        'id': 1,
        'text': 'String',
        'title': 'String'
    }

@temp_db
def test_delete_todo():
    response = client.post(
        '/todos',
        json={'title': 'Foo Bar', 'text': 'The Foo Barters'},
    )

    response = client.delete('/todos/1')
    assert response.status_code == 200
