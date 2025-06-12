from behave import given, when, then

@given("I open the ING homepage")
def step_open_ing_homepage(context):
    context.cookie_manager.verify_ing_homepage()

@given("Cookie consent modal is displayed")
def step_cookie_settings_displayed(context):
    context.cookie_manager.validate_cookie_settings_window()

@when("I customize cookie settings to enable analytical cookies")
def step_enable_analytical_cookies(context):
    context.cookie_manager.enable_analytical_cookies()

@when("I save my cookie preferences")
def step_confirm_cookie_selection(context):
    context.cookie_manager.confirm_cookie_selection()

@then("Cookie consent modal should disappear")
def step_modal_disappeared(context):
    context.cookie_manager.verify_cookie_dialog_closed()

@then("Analytical cookies should be stored in the browser")
def step_check_analytics_cookies(context):
    context.cookie_manager.verify_stored_cookies()