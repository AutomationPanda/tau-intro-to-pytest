"""
This module contains basic UI tests using Playwright.
Their purpose is to show how to use the pytest framework by example.
"""

# --------------------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------------------

import pytest
import re

from playwright.sync_api import Page, expect


# --------------------------------------------------------------------------------
# Tests
# --------------------------------------------------------------------------------

@pytest.mark.ui
@pytest.mark.acme_bank
def test_acme_bank_login(page: Page):

  # Arrange
  page.goto('https://demo.applitools.com/')

  # Act
  page.locator('id=username').fill('andy')
  page.locator('id=password').fill('i<3pandas')
  page.locator('id=log-in').click()

  # Assert
  expect(page.locator('div.logo-w')).to_be_visible()
  expect(page.locator('ul.main-menu')).to_be_visible()
  expect(page.get_by_text('Add Account')).to_be_visible()
  expect(page.get_by_text('Make Payment')).to_be_visible()
  expect(page.get_by_text('View Statement')).to_be_visible()
  expect(page.get_by_text('Request Increase')).to_be_visible()
  expect(page.get_by_text('Pay Now')).to_be_visible()

  warning_msg = re.compile(r'Your nearest branch closes in:( \d+[hms])+')
  expect(page.locator('id=time')).to_have_text(warning_msg)

  acceptable_statuses = ['Complete', 'Pending', 'Declined']
  actual_statuses = page.locator('span.status-pill + span').all_text_contents()
  for status in actual_statuses:
    assert status in acceptable_statuses
