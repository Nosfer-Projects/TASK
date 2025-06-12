from behave.runner import Context
from playwright.sync_api import Page, Browser, Playwright

class CustomContext(Context):
    """
    Custom context class extending Behave's Context to add
    Playwright-specific attributes with type hints for better IDE support:
    - page: current browser page
    - browser: browser instance
    - playwright: Playwright instance
    """
    page: Page
    browser: Browser
    playwright: Playwright