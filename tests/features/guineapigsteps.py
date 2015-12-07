from selenium import webdriver
import os
from pages.sauceguineapigmain import SauceGuineaPig
from sauceclient import SauceClient
from lettuce import *

username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')

@before.each_scenario
def scenario_set_up(scenario):
  desired_cap = {
    "name": scenario.name,
    "platform": os.environ.get('platform'),
    "browser_name": os.environ.get('browser_name'),
    "version": os.environ.get('version')
  }

  browser =  webdriver.Remote(command_executor ='http://%s:%s@ondemand.saucelabs.com:80/wd/hub' % (username, access_key), desired_capabilities = desired_cap)

  for step in scenario.steps:
    step.browser = browser
    step.page = SauceGuineaPig(browser)

@step('we are looking at the guinea pig website')
def get_site(step):
  assert step.page.get_title() == "I am a page title - Sauce Labs", "Incorrect Page"

@step('we click on the uncheck box')
def click_box(step):
  step.page.find_unchecked_checkbox().click()

@step('it should be checked')
def assert_checked(step):
  assert step.page.find_unchecked_checkbox().is_selected(), "Checkbox is not selected"

@after.each_scenario
def teardown(scenario):
  step_results = []
  passed =True
  sauce_client = SauceClient(username, access_key)
  session_id = scenario.steps[0].browser.session_id

  for step in scenario.steps:
    step.browser.quit()
    step_results.append(step.passed)

  for result in step_results:
    if result != True:
      passed = False

  sauce_client.jobs.update_job(session_id, passed = passed)
  print "SauceOnDemandSessionID=" + session_id + " job-name=" + scenario.name
    






