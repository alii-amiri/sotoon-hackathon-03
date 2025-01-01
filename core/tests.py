from django.test import TestCase
from core.utils import replace_dynamic_data, send_email

class EmailFunctionalityTests(TestCase):
    def test_replace_dynamic_data(self):
        template = "Hello, ${candidate_name}. Your role is ${candidate_role}."
        context = {
            'candidate_name': 'John Doe',
            'candidate_role': 'Developer',
        }
        expected_output = "Hello, John Doe. Your role is Developer."
        result = replace_dynamic_data(template, context)
        self.assertEqual(result, expected_output)

    def test_send_email_valid(self):
        subject = "Welcome"
        body = "Hello, ${candidate_name}."
        recipients = ["aliamirii.am@gmail.com"]
        context = {"candidate_name": "John Doe"}
        
        try:
            send_email(subject, recipients, body, context)
        except Exception as e:
            self.fail(f"send_email() raised an exception: {e}")
