=============================
django-browserstack-tools
=============================

.. image:: https://badge.fury.io/py/django-browserstack-tools.png
    :target: https://badge.fury.io/py/django-browserstack-tools

.. image:: https://pypip.in/d/django-browserstack-tools/badge.png
    :target: https://crate.io/packages/django-browserstack-tools?version=latest


Unofficial Browserstack integration for Django

Documentation
-------------

The full documentation is at https://django-browserstack-tools.readthedocs.org.

Quickstart
----------

Install django-browserstack-tools::

    pip install django-browserstack-tools

Then use it in a project:


.. code-block:: python

    from browserstack_tools.testcases import BrowserStackLiveServerTestCase

    class SeleniumTest(BrowserStackLiveServerTestCase):

        desired_capabilities = {'browser': 'Chrome',
                                'browser_version': '33.0',
                                'os': 'Windows',
                                'os_version': '8.1',
                                'resolution': '1680x1050'}

        def test_login(self):
            self.selenium.get('%s%s' % (self.live_server_url, reverse('home')))
            self.assertIn("Hello", self.selenium.title)

Features
--------

* Create Selenium Test using BrowserStack in Django
