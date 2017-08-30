from django.conf.urls import url, include
from .views import IndexView, CategoryView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^category/([0-9]+)/', CategoryView.as_view(), name="category"),
    url(r'^company-index/', CategoryView.as_view(), name="company_index"),
]
