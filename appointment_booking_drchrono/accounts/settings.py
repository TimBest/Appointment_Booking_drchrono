import os

LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/'
# URL_PATH = ''
# SOCIAL_AUTH_STRATEGY = 'social.strategies.django_strategy.DjangoStrategy'
# SOCIAL_AUTH_STORAGE = 'social.apps.django_app.default.models.DjangoStorage'
# SOCIAL_AUTH_EMAIL_FORM_URL = '/signup-email'
# SOCIAL_AUTH_EMAIL_FORM_HTML = 'email_signup.html'
# SOCIAL_AUTH_EMAIL_VALIDATION_FUNCTION = 'example.app.mail.send_validation'
# SOCIAL_AUTH_EMAIL_VALIDATION_URL = '/email-sent/'
# SOCIAL_AUTH_USERNAME_FORM_URL = '/signup-username'
# SOCIAL_AUTH_USERNAME_FORM_HTML = 'username_signup.html'

SOCIAL_AUTH_URL_NAMESPACE = 'social'

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'accounts.pipeline.create_practice',
)

SOCIAL_AUTH_DRCHRONO_KEY  = os.environ.get('DRCHRONO_CLIENT_ID', 'Riowa6L4VwMruzpWfL1DAs0jFuf7Gsd2xP9IfFsF')
SOCIAL_AUTH_DRCHRONO_SECRET = os.environ.get('DRCHRONO_API_SECRET', '')
SOCIAL_AUTH_DRCHRONO_SCOPE = ['patients', 'user', 'calendar']
