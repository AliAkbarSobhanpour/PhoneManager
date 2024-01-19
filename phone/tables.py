from django_tables2 import tables, Column
from django.utils.safestring import mark_safe
from .models import PhoneModel


class PhoneTable(tables.Table):
    text = Column(empty_values=())

    class Meta:
        model = PhoneModel
        template_name = "django_tables2/bootstrap.html"
        per_page_choices = [5, 10, 25, 50, 100]

    def render_text(self, value, **kwargs):
        record = kwargs.get('record')
        text_area = '''
            <textarea name="{}" id="{}" cols="5" class="textinput" rows="5"></textarea><br/>
            <small id='s-{}' class="small-danger"></small>
        '''.format(record.id, record.id, record.id)

        return mark_safe(text_area)

