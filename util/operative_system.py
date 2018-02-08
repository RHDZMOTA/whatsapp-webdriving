import sys

from settings import FileConf


def select_driver():
    if sys.platform in ['win32', 'cygwin']:
        raise ValueError("Windows is not supported.")
    return FileConf.FileNames.chrome_driver.format(sys_platform=sys.platform)
