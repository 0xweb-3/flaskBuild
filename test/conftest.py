import pytest

from main import create_app


@pytest.fixture
def client():
    """获取flask应用并返回"""
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client
