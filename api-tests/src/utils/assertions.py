"""
Generic assertion helpers for API response validation.
"""


def assert_status_code(response, expected_status):
    assert response.status_code == expected_status, (
        f"Expected status {expected_status}, got {response.status_code}. "
        f"Response: {response.text}"
    )


def assert_response_is_list(response):
    data = response.json()
    assert isinstance(data, list), "Response should be a list"
    assert len(data) > 0, "Response list should not be empty"


def assert_field_exists(data, field):
    assert field in data, f"Response should contain '{field}'"


def assert_fields_exist(data, fields: list):
    for field in fields:
        assert field in data, f"Response should contain '{field}'"


def assert_fields_match(response_data, expected_payload, fields: list):
    """
    Verify specific fields in response match expected payload.

    Usage:
        assert_fields_match(data, payload, ["name", "email", "status"])
    """
    for field in fields:
        assert response_data[field] == expected_payload[field], (
            f"Field '{field}' mismatch. "
            f"Expected: {expected_payload[field]}, Got: {response_data[field]}"
        )


def assert_fields_unchanged(response_data, original_data, exclude_fields=None):
    """
    Verify fields are unchanged after a PATCH.
    Compares all keys in original_data except excluded ones.

    Usage:
        assert_fields_unchanged(response.json(), original_user, exclude_fields=["name"])
    """
    exclude_fields = exclude_fields or []

    for field, value in original_data.items():
        if field not in exclude_fields:
            assert response_data[field] == value, (
                f"Field '{field}' should be unchanged. "
                f"Expected: {value}, Got: {response_data[field]}"
            )


def assert_response_time(response, max_seconds=2.0):
    """
    Verify response time is within acceptable threshold.
    """
    elapsed = response.elapsed.total_seconds()
    assert (
        elapsed < max_seconds
    ), f"Response too slow. Expected under {max_seconds}s, got {elapsed:.2f}s"
