djangocms-text-tinymce
=======================

Text Plugin for django-cms with TinyMCE, forked from djangocms-text-ckeditor. 

.. WARNING::
   ``cms.plugins.text`` and ``djangocms-text-tinymce`` can't be used at the same time.


Installation
------------

This plugin requires `django CMS` 2.3 or higher to be properly installed as well as django-tinymce.

* In your projects `virtualenv`_, run ``pip install djangocms-text-tinymce django-tinymce``.
* Add ``'djangocms_text_tinymce'`` to your ``INSTALLED_APPS`` setting **BEFORE** the ``cms`` entry.
* Run ``manage.py migrate djangocms_text_tinymce``.


Upgrading from ``cms.plugins.text``
-----------------------------------

* Remove ``cms.plugins.text`` from ``INSTALLED_APPS``
* Add ``tinymce`` and ``djangocms_text_tinymce`` to ``INSTALLED_APPS``
* Run ``python manage.py migrate djangocms_text_tinymce 0001 --fake``


Usage
-----

Add a new setting to your settings.py called `TINYMCE_DEFAULT_CONFIG` with these base settings::

    TINYMCE_DEFAULT_CONFIG = {
        'height': 335,
        'theme': 'advanced',
        'width': 752,
    }

It is a dict that holds all TinyMCE settings. For an overview of all the available settings have a look here:

http:#wiki.moxiecode.com/index.php/TinyMCE:Configuration for all settings


Drag & Drop Images
------------------

In IE and Firefox based browsers it is possible to drag and drop a picture into the text editor.
This image is base64 encoded and lives in the 'src' attribute as a 'data' tag.

We detect this images, encode them and convert them to picture plugins.
If you want to overwrite this behavior for your own picture plugin:

There is a setting called:

`TEXT_SAVE_IMAGE_FUNCTION = 'djangocms_text_tinymce.picture_save.create_picture_plugin'` 

you can overwrite this setting in your settings.py and point it to a function that handles image saves.
Have a look at the function `create_picture_plugin` for details.




Usage as a model field
----------------------

If you want to use the widget on your own model fields, you can! Just import the ``HTMLField`` from the django-tinymce package:

::

    from tinymce.fields import HTMLField

And use it in your models, just like a TextField:

::

    class MyModel(models.Model):
        myfield = HTMLField(blank=True)