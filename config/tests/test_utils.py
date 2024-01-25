"""
Test config.utils functions
"""

from unittest.mock import patch
from config.utils import get_var


def test__get_var():
    """
    Test config.utils.get_var to read values from the OS environment
    """

    cases = (
        ("1", 1),
        ("string", "string"),
        ('[1, "string"]', [1, "string"]),
        ("{1, 2}", {1, 2}),
    )

    for value, expected in cases:
        with patch.dict("os.environ", {"key": value}):
            value = get_var("key")
            assert value == expected

    value = get_var("non_existing_key")
    assert value is None
