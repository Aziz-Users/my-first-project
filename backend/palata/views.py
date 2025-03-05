from django.shortcuts import redirect
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth import get_user_model
from django.conf import settings
import requests
from django.core.files.base import ContentFile
from users.models import Profile

User = get_user_model()

@login_required
def social_login_callback(request):
    user = request.user

    social_account = SocialAccount.objects.filter(user=user).first()
    if not social_account:
        return redirect(f'{settings.DOMAIN}login/callback/?error=NoSocialAccount')

    provider = social_account.provider
    print(provider)

    token, created = Token.objects.get_or_create(user=user)
    print(social_account.extra_data)
    if social_account.extra_data:
        email = social_account.extra_data.get('email')
        avatar_url = social_account.extra_data.get('picture') if provider == 'google' else social_account.extra_data.get('avatar_url')
        if email:
            user.email = email
            user.save()

        if avatar_url:
            response = requests.get(avatar_url)
            if response.status_code == 200:
                profile, _ = Profile.objects.get_or_create(user=user)
                if profile.image.name == 'default.png' or not profile.image:
                    profile.image.save(
                        f"{user.username}_avatar.jpg",
                        ContentFile(response.content),
                        save=True
                    )

    return redirect(f'{settings.DOMAIN}login/callback/?token={token.key}')

@csrf_exempt
def validate_github_token(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            github_access_token = data.get('access_token')

            if not github_access_token:
                return JsonResponse({'detail': 'Access Token is missing.'}, status=400)
            
            return JsonResponse({'valid': True})
        except json.JSONDecodeError:
            return JsonResponse({'detail': 'Invalid JSON.'}, status=400)
    return JsonResponse({'detail': 'Method not allowed.'}, status=405)
