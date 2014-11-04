from django.conf import settings

TINYMCE_ADMIN_CONFIG = getattr(settings, 'TINYMCE_DEFAULT_CONFIG')

TEXT_SAVE_IMAGE_FUNCTION = getattr(settings, 'TEXT_SAVE_IMAGE_FUNCTION', 'djangocms_text_tinymce.picture_save.create_picture_plugin')
