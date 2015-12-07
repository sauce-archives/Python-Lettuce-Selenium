class Page(object):
  """
  Base class that all page models can inherit from
  """
  def __init__(self, selenium_driver, url):
    self.driver = selenium_driver
    if self.driver.current_url != url:
      self.driver.get(url)

  def get_title(self):
    return self.driver.title

