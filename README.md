[![Build Status](https://travis-ci.org/marteinn/django-log-trigger.svg?branch=master)](https://travis-ci.org/marteinn/django-log-trigger)
[![PyPI version](https://badge.fury.io/py/django-log-trigger.svg)](http://badge.fury.io/py/django-log-trigger)

# Django-Log-Trigger

A django app for simulating exceptions and logging calls of various levels through http. Its perfect when you want to try out your LOGGING settings.


## Requirements

- Python 2.7+/3.5+
- Django 1.8+


## Installing

### Stable

`pip install django-log-trigger`

### Develop

`pip install git+git://github.com/marteinn/django-log-trigger.git@develop`


## Getting started

1. Add `log_trigger` to installed apps

    ```python
    INSTALLED_APPS = [
        'pages',
        'pizza',
        ...
        'log_trigger',
    ]
    ```

2. Add `log_trigger.urls` to your `urls.py`

    ```python
    import log_trigger

    urlpatterns = [
        url(r'^api/', include('api.urls')),
        url(r'^log-trigger/', include(log_trigger.urls)),
        ...
    ```
3. Done!


## Usage

Open your browser and visit any of these urls.

### Exceptions
- `/log-trigger/system-exception/`: Trigger system exception
- `/log-trigger/unhandled-exception/`: Trigger unhandled exception
- `/log-trigger/disallowed-host-exception/`: Trigger disallowed exception

### Logging
- `/log-trigger/debug-logging/`: Debug logging
- `/log-trigger/info-logging/`: Info logging
- `/log-trigger/warn-logging/`: Warn logging
- `/log-trigger/error-logging/`: Error logging
- `/log-trigger/critical-logging/`: Critical logging


## Configuration

### `LOG_TRIGGER_LOGGER_NAME`
Default: `log_trigger.views`

The logger you want to use when testing the logging endpoints.

### `LOG_TRIGGER_SECRET`
Default: Empty

Use the param if you want to secure your testing endpoints, the secret are passed along as a get variable. Example: `/debug-logging/?secret=mysecret`


## Contributing

Want to contribute? Awesome. Just send a pull request.


## License

Django-Log-Trigger is released under the [MIT License](http://www.opensource.org/licenses/MIT).
