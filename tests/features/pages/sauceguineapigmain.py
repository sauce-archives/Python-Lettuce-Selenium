from pages.page import Page

class SauceGuineaPig(Page):
  """
  SauceGuineaPig class that represents the guienea pig webpage
  """
  def __init__(self, selenium_driver):
    Page.__init__(self, selenium_driver, 'https://saucelabs.com/test/guinea-pig')

  def find_unchecked_checkbox(self):
    return self.driver.find_element_by_id('unchecked_checkbox')

  def find_email_input(self):
    return self.driver.find_element_by_id('fbemail') 

  def find_link(self):
    return self.driver.find_element_by_tag_name('a')



