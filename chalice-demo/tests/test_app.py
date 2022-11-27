import json

from app import app
from chalice.test import Client


def test_user_signup():
    json_payload = {
        "first_name": "ivica",
        "city": "Amsterdam",
        "type": "A+",
        "email": "ivica@server.com"
    }

    with Client(app) as client:
        response = client.http.post(
            "/signup",
            headers={"Content-Type": "application/json"},
            body=json.dumps(json_payload)
        )

        assert response.status_code == 200
        assert response.json_body == json_payload