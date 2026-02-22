from django.urls import path
from website import views

app_name = 'website'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('blog-home/', views.blog_home, name='blog-home'),
    path('blog-single/', views.blog_single, name='blog-single'),
    path('elements/', views.elements, name='elements'),
    path('test',views.test_view, name='test'),
    path('newsletter',views.newsletter_view,name='newsletter')

]
