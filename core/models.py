from django.db import models
from django.template import Template, Context
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from core.constants import DynamicVariables

# To auto-populate category field with 'Other' when left empty
def get_default_category():
    #  Defer model access using apps.get_model - a workaround

    from django.apps import apps
    Category = apps.get_model('core', 'Category') 
    category, created = Category.objects.get_or_create(title="Other")
    return category.id    

class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class EmailTemplate(models.Model):
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()  # Stores HTML
    category = models.ForeignKey(Category,
                                 on_delete=models.SET(get_default_category),
                                 default=get_default_category, 
                                 related_name='templates')
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

class Media(models.Model):
    file_url = models.URLField(max_length=2048)  # Link to S3 file
    description = models.TextField(blank=True, null=True)

    # Generic relation
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Media for {self.content_object}: {self.file_url}"

