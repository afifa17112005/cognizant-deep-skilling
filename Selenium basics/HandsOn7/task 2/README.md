# POM Benefit

In a flat Selenium script, if the Submit button ID changes from `submit` to `btn-submit`, every test containing that locator must be updated.

With the Page Object Model, the locator exists in one page class. Updating the locator in that class automatically fixes all tests that use it, reducing maintenance and duplication.
