from . models import Category
from assignment.models import SocialLinks

def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)

def get_social_Links(request):
    social_links = SocialLinks.objects.all()
    return dict(social_links=social_links)