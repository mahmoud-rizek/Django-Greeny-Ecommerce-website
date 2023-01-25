from .models import Profile

def get_profile(request):
    if request.user.is_authenticated:
        quary_profile = Profile.objects.get(user=request.user)
        return {'user_profile':quary_profile}
    else:
        return {}