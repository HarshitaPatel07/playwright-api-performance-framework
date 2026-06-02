"""
Test data for API tests.
"""

import uuid


def create_user_payload(name="John Doe", gender="male", age=21):
    """Always generates a fresh unique email"""
    return {
        "name": name,
        "email": f"{uuid.uuid4()}@test.com",
        "gender": gender,
        "age": age,
    }


def update_user_payload():
    return {
        "name": "Jane Smith",
        "email": f"{uuid.uuid4()}@test.com",
        "gender": "female",
        "age": 32,
    }


UPDATE_USER_NAME = {"name": "John Updated"}
UPDATE_USER_EMAIL = {"email": f"{uuid.uuid4()}@test.com"}
UPDATE_USER_INVALID_EMAIL = {"email": "not-an-email"}

# Invalid Payloads — for negative tests
CREATE_USER_MISSING_NAME = {
    "email": "noname@test.com",
    "gender": "male",
    "age": 27,
}

CREATE_USER_MISSING_EMAIL = {"name": "No Email", "gender": "male", "age": 31}

CREATE_USER_MISSING_GENDER = {
    "name": "No Email",
    "email": "noname@test.com",
    "age": 16,
}
CREATE_USER_MISSING_AGE = {
    "name": "No Email",
    "email": "noname@test.com",
    "gender": "male",
}

CREATE_USER_INVALID_EMAIL = {
    "name": "Bad Email",
    "email": "not-an-email",
    "gender": "male",
    "age": 25,
}

CREATE_USER_INVALID_GENDER = {
    "name": "Jane",
    "email": "jane@test.com",
    "gender": "test",  # should be male or female
}
CREATE_USER_INVALID_AGE = {
    "name": "Jane",
    "email": "jane@test.com",
    "age": "twenty"
}
CREATE_USER_NEGATIVE_AGE = {
    "name": "Jane",
    "email": "jane@test.com",
    "age": -1
}

CREATE_USER_EMPTY = {}

# Parametrize-ready — list of (payload, expected_status)
CREATE_USER_INVALID_CASES = [
    (CREATE_USER_MISSING_NAME, 422),
    (CREATE_USER_MISSING_EMAIL, 422),
    (CREATE_USER_MISSING_GENDER, 422),
    (CREATE_USER_MISSING_AGE, 422),
    (CREATE_USER_INVALID_EMAIL, 422),
    (CREATE_USER_INVALID_GENDER, 422),
    (CREATE_USER_INVALID_AGE, 422),
    (CREATE_USER_NEGATIVE_AGE, 422),
    (CREATE_USER_EMPTY, 422),
]
