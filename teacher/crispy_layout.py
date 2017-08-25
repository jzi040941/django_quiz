from __future__ import unicode_literals

from random import randint

from django.template import Template
from django.template.defaultfilters import slugify
from django.template.loader import render_to_string

from crispy_forms.compatibility import text_type
from crispy_forms.layout import Div, Field, LayoutObject, TemplateNameMixin
from crispy_forms.utils import TEMPLATE_PACK, flatatt, render_field
from crispy_forms.bootstrap import *

class PrependedField(PrependedAppendedText):
    def __init__(self, field, text, **kwargs):
        kwargs.pop('appended_text', None)
        kwargs.pop('prepended_text', None)
        self.text = text
        super(PrependedField, self).__init__(field, prepended_text=text, **kwargs)

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK, extra_context=None, **kwargs):
        extra_context = extra_context.copy() if extra_context is not None else {}
        template = self.get_template_name(template_pack)
        extra_context.update({
            'crispy_appended_text': self.appended_text,
            'crispy_prepended_text': render_field(
                self.prepended_text, form, form_style, context,
                template, attrs=None,
                template_pack=template_pack, extra_context=None
            ),
            'input_size': self.input_size,
            'active': getattr(self, "active", False)
        })
        if hasattr(self, 'wrapper_class'):
            extra_context['wrapper_class'] = self.wrapper_class
        template = self.get_template_name(template_pack)
        return render_field(
            self.field, form, form_style, context,
            template=template, attrs=self.attrs,
            template_pack=template_pack, extra_context=extra_context, **kwargs
        )
