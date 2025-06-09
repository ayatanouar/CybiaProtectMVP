from django.conf import settings
from social_core.exceptions import AuthForbidden

def block_unauthorized_emails(strategy, backend, details, *args, **kwargs):
    email = details.get('email')
    print(f"[OAuth DEBUG] Email reçu : {email}")  # <- vérifie si l’email est bien reçu

    if not email:
        print("[OAuth DEBUG] Pas d'e-mail reçu, refusé.")
        raise AuthForbidden(backend)

    allowed_emails = set(settings.ALLOWED_OAUTH_EMAILS)
    print(f"[OAuth DEBUG] Emails autorisés : {allowed_emails}")

    if email not in allowed_emails:
        print(f"[OAuth DEBUG] Email {email} NON autorisé, refusé.")
        raise AuthForbidden(backend)

    print(f"[OAuth DEBUG] Email {email} autorisé, continuation.")
