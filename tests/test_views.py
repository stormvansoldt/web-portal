import pytest
from quart import Quart


class TestLogin:
    @staticmethod
    def create_login_form(username: str, password: str):
        return {
            "username": username,
            "password": password,
        }

    @pytest.mark.asyncio
    async def test_get_login(self, app: Quart):
        client = app.test_client()
        response = await client.get("/auth/login")
        assert response.status_code == 200
        assert "Login" in await response.get_data(as_text=True)

    @pytest.mark.asyncio
    async def test_login_valid(self, app: Quart):
        client = app.test_client()
        response = await client.post(
            "/auth/login",
            form=self.create_login_form("admin", "admin"),
            follow_redirects=True,
        )
        assert "Log Out" in await response.get_data(as_text=True)

    @pytest.mark.asyncio
    async def test_login_invalid(self, app: Quart):
        client = app.test_client()
        response = await client.post(
            "/auth/login",
            form=self.create_login_form("admin", "wrong password 1234"),
            follow_redirects=True,
        )
        assert "username or password incorrect" in await response.get_data(as_text=True)

    @pytest.mark.asyncio
    async def test_logout(self, app: Quart):
        client = app.test_client()
        response = await client.post(
            "/auth/login",
            form=self.create_login_form("admin", "admin"),
            follow_redirects=True,
        )

        response = await client.get("/auth/logout", follow_redirects=True)
        assert "You have been logged out" in await response.get_data(as_text=True)

        response = await client.get("/auth/logout", follow_redirects=True)
        assert "You need to be logged in to view this page" in await response.get_data(as_text=True)


class TestPortal:
    @pytest.mark.asyncio
    async def test_portal(self, app: Quart):
        client = app.test_client()
        response = await client.get("/")
        assert response.status_code == 200
        assert "Portal" in await response.get_data(as_text=True)
