from rest_framework import viewsets
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from core.utils import send_email
from core.constants import DynamicVariables
from .models import Category, EmailTemplate
from .serializers import CategorySerializer, EmailTemplateSerializer
from users.models import User
from django.utils import timezone

class DynamicVariablesView(APIView):
    """
    Exposes the list of dynamic variables as an API endpoint
    """
    def get(self, request):
        variables = [var.value for var in DynamicVariables]
        return Response({"variables": variables})

#   ViewSets for CRUD operations 
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class EmailTemplateViewSet(viewsets.ModelViewSet):
    queryset = EmailTemplate.objects.all()
    serializer_class = EmailTemplateSerializer

GROUPS = {
    'team_leaders': ['team_leader1@example.com', 'team_leader2@example.com'],
    'all_employees': ['employee1@example.com', 'employee2@example.com', 'employee3@example.com'],
}

@csrf_exempt
def send_email_view(request):
    """
    Handles the email-sending process. Replaces placeholders and sends the email.
    """
    if request.method == 'POST':
        data = eval(request.body.decode())
        email_type = data.get('type', 'direct')  # direct, group, or all
        subject = data.get('subject', 'No Subject')
        body = data.get('body', '')  # Body provided as plain text
        print(f"Raw Body from Request: {body}")  # Log the body received from the request
        if not body:
            return JsonResponse({'error': 'Email body is required'}, status=400)

        # Determine recipients
        if email_type == 'direct':
            recipients = data.get('recipients')
        elif email_type == 'group':
            group_name = data.get('group')
            recipients = GROUPS.get(group_name, [])
        elif email_type == 'all':
            recipients = GROUPS['all_employees']
        else:
            return JsonResponse({'error': 'Invalid email type'}, status=400)

        user = User.objects.get(username="admin")
        context = {
            "candidate_name": user.first_name,
            "date": timezone.now(),
            "candidate_role": user.role,
            "candidate_team": user.team,
        }
        try:
        # Send email using backend logic
            send_email(data["subject"], data["recipients"], data["body"], context=context)
            return JsonResponse({'message': 'Email sent successfully!'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)
