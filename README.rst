.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide_addons.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
collective.redirector
==============================================================================

collective.redirector is used to redirect links on Plone websites to a specific
page on the same domain or another domain. This packages can redirect both
internal and external links on the Plone websites.
#### Note: collective.redirector is a contenttype (RedirectPage).

Features
--------

- Create a custom redirect/confirmation page.
- Allow redirection for external links on any page.
- Allow redirection for internal links on any page.


Examples
--------

This add-on can be seen in action at the following sites:
- adding a confirmation page for form submission.
- adding a confirmation page for external links on your plone site, which will allow users to choose if they want to leave your site or not.
- force the user to see a notification or warning page for any links or pages on your site before visiting it.


Installation
------------

Install collective.redirector by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.redirector


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/collective/collective.redirector/issues
- Source Code: https://github.com/collective/collective.redirector
- Documentation: https://github.com/b4oshany/collective.redirector/wiki


Support
-------

If you are having issues, please let us know.
We have a mailing list located at: project@example.com


License
-------

The project is licensed under the GPLv2.
