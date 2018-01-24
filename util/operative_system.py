import sys

CHROME_DRIVER = "resources/drivers/{sys_platform}/chromedriver"


def select_driver():
    if sys.platform in ['win32', 'cygwin']:
        raise ValueError("Windows is not supported.")
    return CHROME_DRIVER.format(sys_platform=sys.platform)
