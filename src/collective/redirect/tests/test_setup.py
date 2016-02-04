# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.redirect.testing import COLLECTIVE_REDIRECTPAGE_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.redirect is properly installed."""

    layer = COLLECTIVE_REDIRECTPAGE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.redirect is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.redirect'))

    def test_browserlayer(self):
        """Test that ICollectiveRedirectLayer is registered."""
        from collective.redirect.interfaces import (
            ICollectiveRedirectLayer)
        from plone.browserlayer import utils
        self.assertIn(ICollectiveRedirectLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_REDIRECTPAGE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['collective.redirect'])

    def test_product_uninstalled(self):
        """Test if collective.redirect is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.redirect'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveRedirectLayer is removed."""
        from collective.redirect.interfaces import ICollectiveRedirectLayer
        from plone.browserlayer import utils
        self.assertNotIn(ICollectiveRedirectLayer, utils.registered_layers())
