# features/types.py
from behave.runner import Context
from playwright.sync_api import Page, Browser, Playwright

class CustomContext(Context):
    page: Page
    browser: Browser
    playwright: Playwright