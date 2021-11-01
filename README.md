# django-accounts-starter
A more up-to-date authentication/account system in Django3 which uses as many built in views, models, and forms.

Emails by default use a development environment so they go to `testing/emails`.

## Features
- Uses (Argon2id)[https://github.com/hynek/argon2-cffi] for password hashing
- Uses (django-mailer)[https://github.com/pinax/django-mailer] for async mailing of password reset emails so the system is less vulnerable to timing attacks.
- Uses a show/hide instead of typing a password twice for improved UX.
