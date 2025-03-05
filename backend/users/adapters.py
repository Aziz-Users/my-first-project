from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.models import SocialAccount
from rest_framework.authtoken.models import Token


class CustomAccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        user = request.user
        print(f"User authenticated: {user.is_authenticated}") 
        
        if user.is_authenticated:
            social_account = SocialAccount.objects.filter(user=user).first()
            if social_account:
                token, created = Token.objects.get_or_create(user=user)
                print(f"Redirecting to: http://localhost:5173/login/callback/?token={token.key}") 
                return f'http://localhost:5173/login/callback/?token={token.key}'
        return 'http://localhost:5173/login/callback/?error=UserNotAuthenticated'
