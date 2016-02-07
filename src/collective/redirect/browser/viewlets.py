from datetime import datetime

from plone.app.layout.viewlets import ViewletBase
from plone import api
from zope.component import ComponentLookupError
from Products.CMFCore.interfaces import ISiteRoot
from zope.component import getMultiAdapter
from plone.app.layout.navigation.interfaces import INavigationRoot
from plone.api.exc import InvalidParameterError
from collective.redirect.interfaces import (IRedirect, schema_prefix,
                                                TESTDATA)

from time import time
from plone.memoize import ram


class JSFunctionsViewlet(ViewletBase):
	pass


class RedirectViewlet(ViewletBase):
    """ viewlet that displays announcements """

    def script(self, obj):
        return "<script>$(document).ready(function(){url_redirector('%s', '%s', '%s');});</script>" % (
                obj.redirectURL.replace('\n', ' ').replace('\r', ''),
                obj.absolute_url(),
                "^" if obj.enableRegexURL else "")

    @property
    def prefix(self):
        return schema_prefix

    def is_front_page(self):
        """
        Check if the viewlet is on a front page.
        Handle canonical paths correctly.
        based on docs:
        http://docs.plone.org/develop/plone/serving/traversing.html#checking-if-an-item-is-the-site-front-page
        """
        # Get path with "Default content item" wrapping applied
        context_helper = getMultiAdapter((self.context, self.request),
                                                 name="plone_context_state")
        canonical = context_helper.canonical_object()
        path = canonical.absolute_url_path()
        return INavigationRoot.providedBy(canonical)

    @ram.cache(lambda *args: time() // (60 * 60))
    def redirects(self):
        """Get the list of RedirectPage objects from portal_catalog."""
        catalog = api.portal.get_tool('portal_catalog')
        redirects = catalog(portal_type='RedirectPage', review_state="published")
        results = []
        for redirect in redirects:
            r = redirect.getObject()
            obj = dict(
                script=self.script(r),
                enableRedirect=r.enableRedirect,
            )
            results.append(obj)
        return results
