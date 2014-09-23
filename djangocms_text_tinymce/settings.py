from django.conf import settings

from tinymce.profiles import DEFAULT

TINYMCE_ADMIN_CONFIG = getattr(settings, 'TINYMCE_ADMIN_CONFIG', DEFAULT.copy())

TEXT_SAVE_IMAGE_FUNCTION = getattr(settings, 'TEXT_SAVE_IMAGE_FUNCTION', 'djangocms_text_tinymce.picture_save.create_picture_plugin')
