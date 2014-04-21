"""
Django test cases with BrowserStack support
"""

import time
import subprocess
from django.test import LiveServerTestCase
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings
from selenium import webdriver


def get_settings(name):
    """
    Gets Django settings and raises an Exception if the setting name
    is not found
    """
    try:
        return getattr(settings, name)
    except AttributeError:
        raise ImproperlyConfigured("You have to set %s your settings.py" % name)


class BrowserStackLiveServerTestCase(LiveServerTestCase):
    """
    LiveServerTestCase adapted to run BrowserStackLocal script
    when Django live test server is up.

    'selenium' class attribute is provided to interact with the webdriver.

    * `desired_capabilities` attribute is used to build the webdriver.
    * `webdriver_remote_args` overrides the default parameters used to
    build the webdriver.
    """

    desired_capabilities = {}
    webdriver_remote_args = {}

    @classmethod
    def setUpClass(cls):
        # Django launchs live server
        super(BrowserStackLiveServerTestCase, cls).setUpClass()

        # Run BrowserStackLocal
        cls.browserstacklocal = subprocess.Popen(['BrowserStackLocal',
                                                  get_settings('BROWSERSTACK_ACCESS_KEY'),
                                                 '%s,%d,0' % (cls.server_thread.host,
                                                              cls.server_thread.port)],
                                                 stdout=subprocess.PIPE,
                                                 stderr=subprocess.PIPE)
        time.sleep(2)  # BrowserStackLocal must be initialized, I don't know a better
                       # way to know if it is ready.
        # Check webdriver parameters
        desired_capabilities = cls.desired_capabilities.copy()
        desired_capabilities.update({'browserstack.local': True})
        default_webdriver_parameters = {
            'command_executor': 'http://{username}:{access_key}@hub.browserstack.com:80/wd/hub'.format(username=get_settings('BROWSERSTACK_USERNAME'),
                                                                                                       access_key=get_settings('BROWSERSTACK_ACCESS_KEY')),
            'desired_capabilities': desired_capabilities,
        }

        webdriver_parameters = default_webdriver_parameters.copy()
        webdriver_parameters.update(cls.webdriver_remote_args)

        # Create selenium remote webdriver
        cls.selenium = webdriver.Remote(**webdriver_parameters)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        cls.browserstacklocal.send_signal(subprocess.signal.SIGINT)
        super(BrowserStackLiveServerTestCase, cls).tearDownClass()
