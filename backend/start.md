# allauth

```python
INSTALLED_APPS = [
    ...
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
    ...
]

SITE_ID = 1

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)
TEMPLATES = [
    {
        ...
        'OPTIONS': {
            'context_processors': [
                ...
                'django.template.context_processors.request',
                ...
            ],
        },
    },
]
MIDDLEWARE = [
    'allauth.account.middleware.AccountMiddleware',
]
path('accounts/', include('allauth.urls'))

LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'account_login'
LOGOUT_URL = 'account_logout'
SIGNUP_REDIRECT_URL = 'home'
SIGNUP_URL = 'account_signup'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ACCOUNT_EMAIL_VERIFICATION = "none"
```

# rest

```python
INSTALLED_APPS = [
    ...
    'rest_framework.authtoken', # Allows us create a token for each user
    ...
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # Allows us to use token authentication throughout the project
        'rest_framework.authentication.TokenAuthentication',
    ],
}
if DEBUG:
    REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] += [
        'rest_framework.authentication.SessionAuthentication',
    ]


    # urls.py
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    ...
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    ...
]
```


Admin
```python 
    from django.apps import apps
    from django.contrib import admin

    app = apps.get_app_config('users')

    for model_name, model in app.models.items():
        admin.site.register(model)
```