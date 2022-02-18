import pytest
from json import dumps

# parametr haei ke bara test niaze va halat ha va meqdarha

@pytest.mark.parametrize(
        ("data", "headers", "status"),
        [

            ({}, {}, 415),
            ({}, {"Content-Type": "application/json"}, 400),
            ({"": ""}, {"Content-Type": "application/json"}, 400),
            ({"user": "test", "pass": "test"}, {"Content-Type": "application/json"}, 400),
            ({"username": "test", "password": "test", "key": "test"}, {"Content-Type": "application/json"}, 400),
            ({"username": "", "password": ""}, {"Content-Type": "application/json"}, 400),
            ({"username": "test6", "password": "test6"}, {"Content-Type": "application/json"}, 201),
            ({"username": "test6", "password": "test6"}, {"Content-Type": "application/json"}, 409),
            
        ]
)

#barae test kardan be onvane user

def test_create_user(client, data, headers, status):
    result = client.post(
            "/users",
            data = dumps(data),
            headers = headers
    )
    assert result.status_code == status

