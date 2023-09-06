django-otp
PyPI Documentation Source

https://django-otp-official.readthedocs.io/en/stable/


This project makes it easy to add support for one-time passwords (OTPs) to Django. It can be integrated at various levels, depending on how much customization is required. It integrates with django.contrib.auth, although it is not a Django authentication backend. The primary target is developers wishing to incorporate OTPs into their Django projects as a form of two-factor authentication.

Several simple OTP plugins are included and more are available separately. This package also includes an implementation of OATH HOTP and TOTP for convenience, as these are standard OTP algorithms used by multiple plugins.

If you’re looking for a higher-level or more opinionated solution, you might be interested in django-two-factor-auth.

Status
This project is stable and maintained, but is no longer actively used by the author and is not seeing much ongoing investment.

Well-formed issues and pull requests are welcome, but please see CONTRIBUTING.rst first. General questions and ideas should be directed to the Discussions section; issues should be reserved for confirmed bugs.

Contents
Overview and Key Concepts
Installation
Upgrading
Upgrading from 0.2.3 or Earlier
Upgrading to Django 1.7+
Upgrading to 0.3.x with South
Authentication and Verification
Plugins and Devices
Built-in Plugins
Other Plugins
Settings
Glossary
Authentication and Authorization
Authenticating Users
The Easy Way
The Authentication Form
The Admin Site
The Token Form
Custom Forms
The Low-Level API
Authorizing Users
Managing Devices
Extending Django-OTP
Writing a Device
Helpers
Utilities
django_otp.oath
django_otp.util
Contributing
Change Log
v1.2.2 - June 16, 2023 - otp_email html support
v1.2.1 - May 26, 2023 - pt-BR translations
v1.2.0 - May 11, 2023 - Tooling, TOTP images
v1.1.6 - March 07, 2023 - German translation
v1.1.5 - March 06, 2023 - Bugfix release
v1.1.4 - November 10, 2022 - Spanish translation
v1.1.3 - November 30, 2021 - Admin template fix
v1.1.2 - November 29, 2021 - Forward compatibility
v1.1.1 - September 14, 2021 - Throttling message fix
v1.1.0 - September 13, 2021 - Concurrent verification
v1.0.6 - May 28, 2021 - Email customization
v1.0.5 - May 08, 2021 - config_url fix
v1.0.4 - April 28, 2021 - Dark mode fix
v1.0.3 - April 03, 2021 - Email body template path setting
v1.0.2 - October 23, 2020 - Email body template path setting
v1.0.1 - October 06, 2020 - Add French translations
v1.0.0 - August 13, 2020 - Update supported Django verisons.
v0.9.4 - August 05, 2020 - Django 3.1 support
v0.9.3 - June 23, 2020 - June 18, 2020 - Admin fix
v0.9.1 - May 08, 2020 - Admin fix
v0.9.0 - April 17, 2020 - Improved email device
v0.8.1 - February 08, 2020 - Admin fix
v0.8.0 - February 06, 2020 - Drop Python 2 support
v0.7.5 - December 27, 2019 - Django 3.0 support
v0.7.4 - November 21, 2019 - Cleanup
v0.7.3 - October 22, 2019 - Minor improvements
v0.7.2 - September 17, 2019 - LoginView fix
v0.7.1 - September 12, 2019 - Preliminary Django 3.0 support
v0.7.0 - August 26, 2019 - Housekeeping
v0.6.0 - April 22, 2019 - Failure throttling
v0.5.2 - February 11 - 2019 - Fix URL encoding
v0.5.1 - October 24, 2018 - Customizable error messages
v0.5.0 - August 14, 2018 - Django 2.1 support
v0.4.3 - March 8, 2018 - Minor static token fix
v0.4.2 - December 15, 2017 - addstatictoken fix
v0.4.1 - August 29, 2017 - Misc fixes
v0.4.0 - July 19, 2017 - Update support matrix
v0.3.14 - May 30, 2017 - addstatictoken fix
v0.3.13 - April 11, 2017 - Pickle compatibility
v0.3.12 - April 2, 2017 - Forward compatibility
v0.3.11 - March 8, 2017 - Built-in QR Code support
v0.3.8 - November 27, 2016 - Forward compatbility for Django 2.0
v0.3.7 - September 24, 2016 - Convenience API
v0.3.6 - September 4, 2016 - Django 1.10
v0.3.5 - April 13, 2016 - Fix default TOTP key
v0.3.4 - January 10, 2016 - Python 3 cleanup
v0.3.3 - October 15, 2015 - Django 1.9
v0.3.2 - October 11, 2015 - Django 1.8
v0.3.1 - April 3, 2015 - Django 1.8
v0.3.0 - February 7, 2015 - Support Django migrations
v0.2.7 - April 26, 2014 - Fix for Custom user models with South
v0.2.6 - April 18, 2014 - Fix for Python 3.2 with South
v0.2.4 - April 15, 2014 - TOTP plugin fix (migration warning)
v0.2.3 - March 3, 2014 - Fix pickling
v0.2.2 - December 31, 2013 - Require Django 1.4.2
v0.2.1 - November 19, 2013 - Bug fix
v0.2.0 - November 10, 2013 - Django 1.6
v0.1.8 - August 20, 2013 - user_has_device API
v0.1.7 - July 3, 2013 - Decorator improvement
v0.1.6 - May 9, 2013 - Unit test improvements
v0.1.5 - May 8, 2013 - OTPAdminSite improvement
v0.1.3 - March 10, 2013 - Django 1.5 compatibility
v0.1.2 - October 8, 2012 - Bug fix
v0.1.0 - August 20, 2012 - Initial Release
License
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or distribute this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means.

In jurisdictions that recognize copyright laws, the author or authors of this software dedicate any and all copyright interest in the software to the public domain. We make this dedication for the benefit of the public at large and to the detriment of our heirs and successors. We intend this dedication to be an overt act of relinquishment in perpetuity of all present and future rights to this software under copyright law.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.