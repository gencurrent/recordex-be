"""
Configuration utilities
"""

import os
import ast


def get_var(name, default=None):
    """Get the value from the environment key or return defaul if not present"""
    os_env_value = os.environ.get(name)
    if os_env_value is None:
        return default
    try:
        value = ast.literal_eval(os_env_value)
    except ValueError:
        value = os_env_value
    finally:
        return value
