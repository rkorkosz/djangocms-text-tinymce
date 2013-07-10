from django.conf import settings
from tinymce.widgets import TinyMCE

class TextEditorWidget(TinyMCE):
    class Media:
        css = {
            'all': ('%scss/cms.tinymce.css' % settings.STATIC_URL,)
        }