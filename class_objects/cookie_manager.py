from playwright.sync_api import Page, expect
from config_files.cookie_constants import *
from config_files.config import *

class CookieManager:
    def __init__(self, page: Page):
        self.page = page
        self.cookie_window =                       self.page.locator("div.js-cookie-policy-main div[role='dialog']")
        self.title_window_locator =                self.cookie_window.locator("h2.cookie-policy-title", has_text=TITLE_TEXT)
        self.accept_all_button_locator =           self.cookie_window.locator("button.js-cookie-policy-main-accept-button", has_text=ACCEPT_ALL_BUTTON_TEXT)
        self.decline_all_button_locator =          self.cookie_window.locator("button.js-cookie-policy-main-decline-button", has_text=DECLINE_ALL_BUTTON_TEXT)
        self.customize_button_locator =            self.cookie_window.locator("button.js-cookie-policy-main-settings-button", has_text=CUSTOMIZE_BUTTON_TEXT)
        self.privacy_policy_link =                 self.cookie_window.locator("a[href='https://www.ing.pl/indywidualni/tabele-i-regulaminy/regulacje/ochrona-danych-osobowych']")
        self.cookie_policy_link =                  self.cookie_window.locator("a[href='https://www.ing.pl/cookie']")
        self.cookie_policy_description_locator=    self.cookie_window.locator("div.cookie-policy-description", has_text=COOKIE_POLICY_DESCRIPTION_TEXT)
        self.customize_cookie_window_locator=      self.page.locator("div.js-cookie-policy-settings div[role='dialog']")
        self.customize_title_window_locator=       self.customize_cookie_window_locator.locator("h2.cookie-policy-title", has_text=CUSTOMIZE_TITLE_WINDOW_TEXT)
        self.customize_tech_cookie_header=         self.customize_cookie_window_locator.locator("#header-1-technical", has_text=CUSTOMIZE_TECH_COOKIE_TEXT)
        self.customize_analytical_cookie_header=   self.customize_cookie_window_locator.locator("#header-2-analytical", has_text=CUSTOMIZE_ANALYTICAL_COOKIE_TEXT)
        self.customize_marketing_cookie_header=    self.customize_cookie_window_locator.locator("#header-3-marketing", has_text=CUSTOMIZE_MARKETING_COOKIE_TEXT)
        self.customize_analytical_switch_button=   self.customize_cookie_window_locator.locator("div.cookie-policy-toggle-button[name='CpmAnalyticalOption']")
        self.customize_tech_switch_button=         self.customize_cookie_window_locator.locator("div.cookie-policy-toggle-button[name='CpmTechnicalOption']")
        self.customize_marketing_switch_button=    self.customize_cookie_window_locator.locator("div.cookie-policy-toggle-button[name='CpmMarketingOption']")
        self.customize_reject_all_button=          self.customize_cookie_window_locator.get_by_role("button", name=CUSTOMIZE_REJECT_ALL_BUTTON_TEXT)
        self.customize_accept_selected_button=     self.customize_cookie_window_locator.get_by_role("button", name=CUSTOMIZE_ACCEPT_SELECTED_BUTTON_TEXT)
        self.cookie_window_selectors_list=[
            self.title_window_locator,
            self.accept_all_button_locator,
            self.decline_all_button_locator,
            self.customize_button_locator,
            self.privacy_policy_link,
            self.cookie_policy_link,
            self.cookie_policy_description_locator
        ]
        self.cookie_customize_window_selectors_list=[
            self.customize_tech_cookie_header,
            self.customize_analytical_cookie_header,
            self.customize_marketing_cookie_header,
            self.customize_analytical_switch_button,
            self.customize_tech_switch_button,
            self.customize_marketing_switch_button,
            self.customize_reject_all_button,
            self.customize_accept_selected_button
        ]

    def expect_visible_with_text(self, selectors_list : list):
        for selector in selectors_list:
            expect(selector).to_be_visible()

    def verify_ing_homepage(self):
        self.page.wait_for_load_state("domcontentloaded")
        # expect(self.page).to_have_title(URL_TITLE)
        expect(self.page).to_have_url(BASE_URL)

    def validate_cookie_settings_window(self):
        expect(self.cookie_window).to_be_visible()
        expect(self.cookie_window).to_be_enabled()
        self.expect_visible_with_text(self.cookie_window_selectors_list)

    def enable_analytical_cookies(self):
        self.customize_button_locator.click()
        self.expect_visible_with_text(self.cookie_customize_window_selectors_list)
        self.customize_analytical_switch_button.click()
        expect(self.customize_tech_switch_button).to_be_checked()
        expect(self.customize_analytical_switch_button).to_be_checked()
        expect(self.customize_marketing_switch_button).not_to_be_checked()

    def confirm_cookie_selection(self):
        self.customize_accept_selected_button.click()

    def verify_cookie_dialog_closed(self):
        expect(self.cookie_window).not_to_be_visible()
        expect(self.customize_cookie_window_locator).not_to_be_visible()
    
    def verify_stored_cookies(self):
        cookies = self.page.context.cookies(BASE_URL)
        cookies_dict = {cookie['name']: cookie['value'] for cookie in cookies}
        assert 'cookiePolicyGDPR' in cookies_dict, "Missing cookiePolicyGDPR"
        assert cookies_dict['cookiePolicyGDPR'] == '3', "cookiePolicyGDPR value incorrect"
        assert 'cookiePolicyINCPS' in cookies_dict, "Missing cookiePolicyINCPS"
        assert cookies_dict['cookiePolicyINCPS'] == 'true', "cookiePolicyINCPS value incorrect"
        assert 'cookiePolicyGDPR__details' in cookies_dict, "Missing cookiePolicyGDPR__details"
        assert '_fbp' not in cookies_dict, "_fbp cookie should not be present"