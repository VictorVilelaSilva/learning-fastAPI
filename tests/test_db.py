from dataclasses import asdict

from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        new_user = User(
            username='alice', password='secret', email='teste@test'
        )
        session.add(new_user)
        session.commit()

        user = session.scalar(select(User).where(User.username == 'alice'))

    assert asdict(user) == {
        'id': 1,
        'username': 'alice',
        'password': 'secret',
        'email': 'teste@test',
        'created_at': time,
        'updated_at': None,
    }


def test_update_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        user = User(
            username='bob',
            email='bob@example.com',
            password='secret',
        )
        session.add(user)
        session.commit()

        user.email = 'bob_new@example.com'
        session.commit()

        user = session.scalar(select(User).where(User.username == 'bob'))

        assert asdict(user) == {
            'id': 1,
            'username': 'bob',
            'email': 'bob_new@example.com',
            'password': 'secret',
            'created_at': time,
            'updated_at': time,
        }
