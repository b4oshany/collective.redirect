# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s collective.redirector -t test_redirectpage.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src collective.redirector.testing.COLLECTIVE_REDIRECTPAGE_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_redirectpage.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a RedirectPage
  Given a logged-in site administrator
    and an add redirectpage form
   When I type 'My RedirectPage' into the title field
    and I submit the form
   Then a redirectpage with the title 'My RedirectPage' has been created

Scenario: As a site administrator I can view a RedirectPage
  Given a logged-in site administrator
    and a redirectpage 'My RedirectPage'
   When I go to the redirectpage view
   Then I can see the redirectpage title 'My RedirectPage'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add redirectpage form
  Go To  ${PLONE_URL}/++add++RedirectPage

a redirectpage 'My RedirectPage'
  Create content  type=RedirectPage  id=my-redirectpage  title=My RedirectPage


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the redirectpage view
  Go To  ${PLONE_URL}/my-redirectpage
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a redirectpage with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the redirectpage title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
