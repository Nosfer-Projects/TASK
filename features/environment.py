import allure
from config_files.config import *
from allure_commons.types import AttachmentType
from playwright.sync_api import sync_playwright
from type_class_files.types import CustomContext
from class_objects.cookie_manager import CookieManager


def before_feature(context : CustomContext, feature):
    context.playwright = sync_playwright().start()
    browser_launcher = getattr(context.playwright, BROWSER)
    context.browser = browser_launcher.launch(headless=True, slow_mo=500) 
    # I used browser slow_mo here so we could see what was happening on the UI. 
    # In normal tests I would remove this to increase test performance
    context.page = context.browser.new_page()
    context.page.goto(BASE_URL)
    context.cookie_manager = CookieManager(context.page)
    feature.name += f" [{os.getenv('BROWSER', 'unknown')}]"

def before_scenario(context, scenario):
    scenario.name += f" [{os.getenv('BROWSER', 'unknown')}]"

def after_feature(context: CustomContext, feature):
    context.page.close()
    context.browser.close()
    context.playwright.stop()

def after_step(context: CustomContext, step):
    if step.status == "failed":
        screenshot = context.page.screenshot()
        allure.attach(screenshot, name = "screenshot", attachment_type = AttachmentType.PNG)