from playwright.sync_api import Page, expect
from config_files.config import *

class CookieManager:
    def __init__(self, page: Page):
        self.page = page
        self.title_text =                          "ING Bank Śląski (my) korzysta z cookies i innych podobnych technologii"
        self.accept_all_button_text =              "Zaakceptuj wszystkie"
        self.decline_all_button_text =             "Odrzuć wszystkie"
        self.customize_button_text =               "Dostosuj"
        self.privacy_policy_text=                  "Polityką prywatności"
        self.cookie_policy_text=                   "Polityką cookies"
        self.cookie_policy_description_text=       "Jeśli zaakceptujesz wszystkie cookies"
        self.customize_title_window_text=          "Ustawienia plików cookies i innych technologii"
        self.customize_tech_cookie_text=           "Cookies techniczne"
        self.customize_analytical_cookie_text=     "Cookies analityczne"
        self.customize_marketing_cookie_text=      "Cookies marketingowe"
        self.customize_reject_all_button_text=     "Odrzuć wszystkie"
        self.customize_accept_selected_button_text= "Zaakceptuj zaznaczone"
        self.cookie_window =                       self.page.locator("div.js-cookie-policy-main div[role='dialog']")
        self.title_window_locator =                self.cookie_window.locator("h2.cookie-policy-title", has_text=self.title_text)
        self.accept_all_button_locator =           self.cookie_window.locator("button.js-cookie-policy-main-accept-button", has_text=self.accept_all_button_text)
        self.decline_all_button_locator =          self.cookie_window.locator("button.js-cookie-policy-main-decline-button", has_text=self.decline_all_button_text)
        self.customize_button_locator =            self.cookie_window.locator("button.js-cookie-policy-main-settings-button", has_text=self.customize_button_text)
        self.privacy_policy_link =                 self.cookie_window.locator("a[href='https://www.ing.pl/indywidualni/tabele-i-regulaminy/regulacje/ochrona-danych-osobowych']")
        self.cookie_policy_link =                  self.cookie_window.locator("a[href='https://www.ing.pl/cookie']")
        self.cookie_policy_description_locator=    self.cookie_window.locator("div.cookie-policy-description", has_text=self.cookie_policy_description_text)
        self.customize_cookie_window_locator=      self.page.locator("div.js-cookie-policy-settings div[role='dialog']")
        self.customize_title_window_locator=       self.customize_cookie_window_locator.locator("h2.cookie-policy-title", has_text=self.customize_title_window_text)
        self.customize_tech_cookie_header=         self.customize_cookie_window_locator.locator("#header-1-technical", has_text=self.customize_tech_cookie_text)
        self.customize_analytical_cookie_header=   self.customize_cookie_window_locator.locator("#header-2-analytical", has_text=self.customize_analytical_cookie_text)
        self.customize_marketing_cookie_header=    self.customize_cookie_window_locator.locator("#header-3-marketing", has_text=self.customize_marketing_cookie_text)
        self.customize_analytical_switch_button=   self.customize_cookie_window_locator.locator("div.cookie-policy-toggle-button[name='CpmAnalyticalOption']")
        self.customize_tech_switch_button=         self.customize_cookie_window_locator.locator("div.cookie-policy-toggle-button[name='CpmTechnicalOption']")
        self.customize_marketing_switch_button=    self.customize_cookie_window_locator.locator("div.cookie-policy-toggle-button[name='CpmMarketingOption']")
        self.customize_reject_all_button=          self.customize_cookie_window_locator.get_by_role("button", name=self.customize_reject_all_button_text)
        self.customize_accept_selected_button=     self.customize_cookie_window_locator.get_by_role("button", name=self.customize_accept_selected_button_text)
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
        expect(self.page).to_have_title(URL_TITLE)
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
        pass
    def get_cookies(self):
        pass
