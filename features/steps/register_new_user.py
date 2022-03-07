from behave import*
from locator import*
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support.ui import Select
from time import sleep
from database import*
from hamcrest import*
from datetime import datetime
import logging

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

print("Automated testing started on:", dt_string)


@given(u'I go to homepage')
def step_impl(context):
    logging.info("Opening homepage URL: {0}".format(database.userdata["base_url"]))
    context.browser.get(database.userdata["base_url"])
    sleep(3)

@when(u'Clicking on the sign in button')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.signin).is_displayed()
    context.browser.find_element(By.XPATH,locator.signin).click()
    sleep(3)

@then(u'I enter my email to register')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.email_create).click()
    context.browser.find_element(By.XPATH,locator.email_create).send_keys(database.userdata["my_email"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.SubmitCreate).click()
    sleep(3)

@then(u'I populate the registration form')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.gender_mr).click()
    sleep(1)
    context.browser.find_element(By.XPATH,locator.customer_firstname).click()
    context.browser.find_element(By.XPATH,locator.customer_firstname).send_keys(database.userdata["firstname"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.customer_lastname).click()
    context.browser.find_element(By.XPATH,locator.customer_lastname).send_keys(database.userdata["lastname"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.password).click()
    context.browser.find_element(By.XPATH,locator.password).send_keys(database.userdata["password"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.days_dob).send_keys(Keys.TAB)
    sleep(1)
    context.browser.find_element(By.XPATH,locator.days_dob).send_keys(Keys.DOWN)
    context.browser.find_element(By.XPATH,locator.days_dob).send_keys(database.userdata["days"])
    context.browser.find_element(By.XPATH,locator.days_dob).send_keys(Keys.TAB)
    sleep(1)
    context.browser.find_element(By.XPATH,locator.months_dob).click()
    context.browser.find_element(By.XPATH,locator.days_dob).send_keys(Keys.DOWN)
    context.browser.find_element(By.XPATH,locator.months_dob).send_keys(database.userdata["months"])
    context.browser.find_element(By.XPATH,locator.months_dob).send_keys(Keys.TAB)
    sleep(1)
    context.browser.find_element(By.XPATH,locator.years_dob).click()
    context.browser.find_element(By.XPATH,locator.days_dob).send_keys(Keys.DOWN)
    context.browser.find_element(By.XPATH,locator.years_dob).send_keys(database.userdata["years"])
    context.browser.find_element(By.XPATH,locator.years_dob).send_keys(Keys.RETURN)
    sleep(1)
#    context.browser.find_element(By.XPATH,locator.firstname).click()
#    context.browser.find_element(By.XPATH,locator.firstname).send_keys(database.userdata["firstname"])
#    sleep(1)
#    context.browser.find_element(By.XPATH,locator.lastname).click()
#    context.browser.find_element(By.XPATH,locator.lastname).send_keys(database.userdata["lastname"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.company).click()
    context.browser.find_element(By.XPATH,locator.company).send_keys(database.userdata["company"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.address).click()
    context.browser.find_element(By.XPATH,locator.address).send_keys(database.userdata["address"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.city).click()
    context.browser.find_element(By.XPATH,locator.city).send_keys(database.userdata["city"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.state).click()
    context.browser.find_element(By.XPATH,locator.state).send_keys(database.userdata["state"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.postcode).click()
    context.browser.find_element(By.XPATH,locator.postcode).send_keys(database.userdata["postcode"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.other_info).click()
    context.browser.find_element(By.XPATH,locator.other_info).send_keys(database.userdata["other_info"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.phone).click()
    context.browser.find_element(By.XPATH,locator.phone).send_keys(database.userdata["phone"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.mobile).click()
    context.browser.find_element(By.XPATH,locator.mobile).send_keys(database.userdata["mobile"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.alias).click()
    context.browser.find_element(By.XPATH,locator.alias).send_keys(database.userdata["alias"])
    sleep(1)

@then(u'I click Submit')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.register_button).click()
    sleep(3)

@then(u'Verify registration completed')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.page_heading).is_displayed()
    text_element = context.browser.find_elements(By.XPATH,locator.page_heading)
    edit_text = text_element[0].text
    assert_that(edit_text, contains_string(database.userdata["page_heading"]))
    sleep(1)
    context.browser.find_element(By.XPATH,locator.info_account).is_displayed()
    text_element = context.browser.find_elements(By.XPATH,locator.info_account)
    edit_text = text_element[0].text
    assert_that(edit_text, contains_string(database.userdata["info_account"]))
    sleep(3)
    context.browser.find_element(By.XPATH,locator.signout_button).is_displayed()
    context.browser.find_element(By.XPATH,locator.signout_button).click()
    sleep(3)

@then(u'I enter my email to login')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.email_signin).click()
    context.browser.find_element(By.XPATH,locator.email_signin).send_keys(database.userdata["my_email"])
    context.browser.find_element(By.XPATH,locator.password_signin).click()
    context.browser.find_element(By.XPATH,locator.password_signin).send_keys(database.userdata["password"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.signin_button).click()
    sleep(3)
