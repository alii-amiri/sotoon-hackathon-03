import re
from django.core.mail import EmailMessage
from core.constants import DynamicVariables
from django.conf import settings

def extract_placeholders(template_string):
    """
    Extracts placeholders (e.g., ${candidate_name}) from the template string.
    """
    return re.findall(r"\${(.*?)}", template_string)

def replace_dynamic_data(template_string, context):
    """
    Replace placeholders in the template string with values from the context.
    """
    placeholders = extract_placeholders(template_string)
    print(f"Extracted Placeholders: {placeholders}")  # Debug the output
    for placeholder in placeholders:
        key = placeholder.lower()
        value = context.get(key, '')
        template_string = template_string.replace(f"${{{placeholder}}}", value)
    return template_string

def send_email(subject, recipient_list, template_string, context):
    """
    Process the template, and send the email.
    """
    # if context is None:
    #     context = generate_default_context()

    print(f"Template String Before Replacement: {template_string}")  # Debug template string
    print(f"Context: {context}")  # Debug context

    processed_body = replace_dynamic_data(template_string, context)
    print(f"Processed Body: {processed_body}")  # Debug processed body
    email = EmailMessage(
        subject=subject,
        body=processed_body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=recipient_list,
    )
    email.content_subtype = 'html'
    email.send()
    
