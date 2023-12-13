import os
from typing import Final


class LCBOConfig(object):
    LCBO_API_HOST: Final = os.environ.get("LCBO_API_HOST")
    MAX_RESULTS_RETURNED: Final = 5000
    AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
