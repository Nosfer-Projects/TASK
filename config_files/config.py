import os

# Configuration file with basic test settings:
# - BASE_URL: Target URL for the tests (ING homepage).
# - BROWSER: Browser type used for testing; defaults to "chromium" if not set via environment variable.
# - URL_TITLE: Expected page title to verify successful page load.

BASE_URL =       "https://www.ing.pl/"
BROWSER =        os.getenv("BROWSER", "chromium")
URL_TITLE =      "ING Bank Śląski"