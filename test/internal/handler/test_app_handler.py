import pytest

from pkg.response.http_code import HttpCode


class TestAppHandler:
    """app控制器的测试类"""

    @pytest.mark.parametrize("email", ["", "a@xin.com"])
    def test_login(self, email, client):
        resp = client.post("/v1/login", json={"email": email, "password": "1234"})
        assert resp.status_code == 200
        if email is "":
            assert resp.json.get("code") == HttpCode.VALIDATE_ERROR
        else:
            assert resp.json.get("code") == HttpCode.SUCCESS
        print("响应内容：", resp.json)
