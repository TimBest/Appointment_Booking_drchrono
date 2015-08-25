from accounts.models import Practice


def create_practice(request, strategy, backend, uid, response={}, details={}, user=None, social=None, *args, **kwargs):
    """
        if user has a practice skip else create new practice
    """
    practice, created = Practice.objects.update_or_create(user=user)
    return None
