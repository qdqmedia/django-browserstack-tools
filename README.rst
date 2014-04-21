=============================
django-browserstack-tools
=============================

.. image:: https://badge.fury.io/py/django-browserstack-tools.png
    :target: https://badge.fury.io/py/django-browserstack-tools

.. image:: https://travis-ci.org/dnmellen/django-browserstack-tools.png?branch=master
    :target: https://travis-ci.org/dnmellen/django-browserstack-tools

.. image:: https://coveralls.io/repos/dnmellen/django-browserstack-tools/badge.png?branch=master
    :target: https://coveralls.io/r/dnmellen/django-browserstack-tools?branch=master

Unofficial Browserstack integration for Django

Documentation
-------------

The full documentation is at https://django-browserstack-tools.readthedocs.org.

Quickstart
----------

Install django-browserstack-tools::

    pip install django-browserstack-tools  (Package not ready yet)

Then use it in a project::


.. code-block :: python

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

* TODO