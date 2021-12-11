from selenium import webdriver


def set_options():
    """
    Set options for WebDriver.
    Enable option.headless, if you need.
    """
    option = webdriver.FirefoxOptions()
    option.set_preference('dom.webdriver.enabled', False)
    option.set_preference('dom.webnotifications.enabled', False)
    option.set_preference('media.volume_scale', '0.0')
    #option.headless = True
    return option
