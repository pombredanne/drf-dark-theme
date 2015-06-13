drf-dark-theme
==============

.. image:: https://img.shields.io/pypi/v/drf-dark-theme.svg

Dark them for `Django REST Framework`_

.. _Django REST Framework: https://github.com/tomchristie/django-rest-framework

Color Palette
-------------
.. image:: https://raw.githubusercontent.com/aledista/drf-dark-theme/master/drf_dark_theme/static/drf_dark_theme/img/color-palette.png

Screenshot
----------
.. image:: https://raw.githubusercontent.com/aledista/drf-dark-theme/master/drf_dark_theme/static/drf_dark_theme/img/screenshot.png


Installation
============

Install using ``pip``\

::

    pip install drf-dark-theme

Add 'drf_chaos' to your INSTALLED_APPS setting

::

    INSTALLED_APPS = (
        ...
        'drf_dark_theme',
    )

Add 'DarkBrowsableAPIRenderer' to DEFAULT_RENDERER_CLASSES

::

    REST_FRAMEWORK = {
        'DEFAULT_RENDERER_CLASSES': (
            ...
            'drf_dark_theme.renderers.DarkBrowsableAPIRenderer',
        )
    }
