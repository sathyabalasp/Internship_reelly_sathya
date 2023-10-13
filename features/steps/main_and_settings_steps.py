from behave import given, when, then
from time import sleep

@given('Open the login page')
def open_login_page(context):
    context.app.login_page.login_pages()


@when('Login to the page')
def login_to_webpage(context):
    context.app.login_page.click_on_signin_link()
    sleep(2)
    context.app.login_page.input_email("sathyabalasp@gmail.com")
    sleep(2)
    context.app.login_page.input_password("Sbala8435")
    sleep(2)
    context.app.login_page.click_continue_button()


@then('Click on settings option')
def click_settings(context):
    context.app.main_page.click_settings_option()
    sleep(1)


@then('Click on Subscription And payments option')
def click_subscription_payments(context):
    context.app.settings_page.click_subscription_and_payments()
    sleep(1)


@then('Verify the {text} page opens and visible')
def verify_sub_pay_page(context,text):
    context.app.sub_and_pay_page.verify_sub_and_pay_page(text)
    sleep(2)


@then('Verify title of Subscription & payments is visible')
def verify_Sub_and_pay_visible(context):
    context.app.sub_and_pay_page.verify_sub_and_pay_visible()
    sleep(1)


@then('Verify {button} button back are available')
def verify_back_button(context, button):
    context.app.sub_and_pay_page.verify_back_buttons_available(button)
    sleep(1)


@then('Verify {button} are available')
def verify_upgrade_plan_button(context, button):
    context.app.sub_and_pay_page.verify_upgrade_plan_buttons(button)
    sleep(1)