from django.db import models

class Category (models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class EmailTemplate(models.Model):
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()  # Stores HTML
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='templates')

    def __str__(self):
        return self.title
    
    def render(self, context):
        """
        Render the template content with the given context.
        :param context: A dictionary of key-value pairs for placeholders.
        """
        from django.template import Template, Context
        template = Template(self.content)
        return template.render(Context(context))

    class Meta:
        app_label = 'core'
