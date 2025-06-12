import allure
from config_files.config import *
from allure_commons.types import AttachmentType
from playwright.sync_api import sync_playwright
from type_class_files.types import CustomContext
from class_objects.cookie_manager import CookieManager

# Executed once before each feature file starts
def before_feature(context : CustomContext, feature):
    # Start Playwright and launch browser specified in config (default: Chromium)
    context.playwright = sync_playwright().start()
    browser_launcher = getattr(context.playwright, BROWSER)
    context.browser = browser_launcher.launch(headless=False)

    # Open a new page and navigate to ING homepage
    context.page = context.browser.new_page()
    context.page.goto(BASE_URL)

    # Initialize the CookieManager for cookie-related interactions
    context.cookie_manager = CookieManager(context.page)

    # Append browser name to scenario name (for reporting in pipeline run with Allure)
    feature.name += f" [{os.getenv('BROWSER', 'unknown')}]"

# Executed before each scenario starts
def before_scenario(context, scenario):
    # Append browser name to scenario name (for reporting in pipeline run with Allure)
    scenario.name += f" [{os.getenv('BROWSER', 'unknown')}]"

# Executed once after each feature ends
def after_feature(context: CustomContext, feature):
    # Clean up Playwright browser and context
    context.page.close()
    context.browser.close()
    context.playwright.stop()

# Executed after each step; captures screenshot on failure
def after_step(context: CustomContext, step):
    if step.status == "failed":
        # Attach screenshot to Allure report if step fails
        screenshot = context.page.screenshot()
        allure.attach(screenshot, name="screenshot", attachment_type=AttachmentType.PNG)