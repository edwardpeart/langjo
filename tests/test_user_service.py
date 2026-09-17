import uuid

from backend.app.services.user_service import UserService


class TestUserService:
    def test_create_user_persists_username_and_hash(self):
        service = UserService()
        user = service.create_user(
            username="alice",
            email="alice@example.com",
            password="supersecret",
        )

        assert user.username == "alice"
        assert user.email == "alice@example.com"
        assert user.password_hash
        assert user.id is not None

    def test_get_or_create_default_user_returns_stable_user(self):
        service = UserService()
        user1 = service.get_or_create_default_user()
        user2 = service.get_or_create_default_user()

        assert user1.id == user2.id
        assert user1.username == "system"
