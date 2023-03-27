# CA2 (which is now CA3)
Back-End Web Development, Continuous Assessment 2.

Has now evolved into CA3, but remains in the same project, so bears the 'CA2' name.

## Updates made in CA3: Testing and Security updates !

### Testing
The testing is focused on the `buildings` app:
* Added tests on the views, in `tests_views.py`:
  * the `test_actual_views` tests whether the views that display a web page are working, by checking their return code. (positive testing)
  * the `test_redirect_views` tests whether the views that redirect the user to a web page are working, by checking their return code. (positive testing)
  * the `test_no_data` tests whether the various 'SortBy' views display an appropriate message when there is no data to display. (negative testing)
  * the `test_correct_pk_sort`, `test_correct_name_sort`, and `test_correct_address_sort` test whether the data is displayed in the correct order, by creating fake data and scanning the view's context. (positive testing)
* Added tests on the `Building` model, in `tests_buildings.py`:
  * the `test_number_floors_can_be_less_than_one` tests whether the number of floors of a building can be 0. Due to the use of a `PositiveSmallIntegerField`, it cannot be negative. Amends were made to the `Building` model based on failures to this test: the `__init__` function was modified, and a `MinValueValidator` was added. (negative testing)
  * the `test_address_function_works_correctly` tests whether the `get_address2` method returns the right string. (positive testing)

### Security
The `settings.py` file can now accept a 'development' or 'production' mode: by switching the `envVarMode` variable, some settings will be automatically updated/added. This facilitates deployment and secures information that could have been otherwise exploited.
This way, the following security measures have been implemented:
* switching of `DEBUG` from True (development) to False (production)
* setup of `ALLOWED_HOSTS` depending on production or development
* setup of several variables used to enforce HTTPS in production. I have not been able to test them, since the local hosting of Django only supports HTTP.

Should also be noted that the admin page of the website is no longer located at 'admin/', but at 'minda/tub/gnihtyna/', which is hard to find, but easy to remember: it simply spells "*anything but admin*", backwards.

A note on XSS and CSRF protection: Django has builtin protection, that I currently use: indeed, all my views are generic views, which make use of `RequestContext`, and my POST forms all include a `{% csrf_token %}`.

