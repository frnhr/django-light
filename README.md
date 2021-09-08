# django-light

Disable dark mode in Django admin UI.


## Installation

1. `pip install django-light`
2. Add `'django_light',` to `INSTALLED_APPS` **before** `django.contrib.admin`


## Implementation

This is a pure CSS tweak. The CSS file is injected via `base.html` in the `extrastyle` block. If you are using Jinja2 
or override `base.html` in a way that doesn't call `{{ block.super }}` on that block, YMMV. But in the end all that is
needed is for the browser to load `<STATIC_URL>/django_light/django_light.css` stylesheet.

Please report any problems via GitHub issues. PRs welcome.
