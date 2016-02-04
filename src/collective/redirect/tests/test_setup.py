# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.redirectpage.testing import COLLECTIVE_REDIRECTPAGE_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.redirectpage is properly installed."""

    layer = COLLECTIVE_REDIRECTPAGE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.redirectpage is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.redirectpage'))

    def test_browserlayer(self):
        """Test that ICollectiveRedirectpageLayer is registered."""
        from collective.redirectpage.interfaces import (
            ICollectiveRedirectpageLayer)
        from plone.browserlayer import utils
        self.assertIn(ICollectiveRedirectpageLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_REDIRECTPAGE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['collective.redirectpage'])

    def test_product_uninstalled(self):
        """Test if collective.redirectpage is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.redirectpage'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveRedirectpageLayer is removed."""
        from collective.redirectpage.interfaces import ICollectiveRedirectpageLayer
        from plone.browserlayer import utils
        self.assertNotIn(ICollectiveRedirectpageLayer, utils.registered_layers())
