from django.urls import path
from .views import blog, detail

urlpatterns = [
    path('', blog, name='blog-home'),
    path('<int:blog_id>/', detail, name="blog-detail")
]
