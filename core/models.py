from django.db import models
from django.template import Template, Context
from core.constants import DynamicVariables

class Category (models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class EmailTemplate(models.Model):
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()  # Stores HTML
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 null=True, related_name='templates')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def render(self, context):
        """
        Render the template content with the given context.
        :param context: A dictionary of key-value pairs for placeholders.
        """
        allowed_variables = [var.value for var in DynamicVariables]
        filtered_context = {key: value for key, value in context.items() if key in allowed_variables}
        template = Template(self.content)
        return template.render(Context(filtered_context))

    class Meta:
        app_label = 'core'
