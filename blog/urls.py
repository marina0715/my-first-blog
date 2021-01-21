from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.start, name='start'),
    path('post_list/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('category/<str:category>/', views.category, name='category'),
    path('post_calorie_low/', views.post_calorie_low, name='post_calorie_low'),
    path('post_calorie_high/', views.post_calorie_high, name='post_calorie_high'),
    path('post_protein_low/', views.post_protein_low, name='post_protein_low'),
    path('post_protein_high/', views.post_protein_high, name='post_protein_high'),
    path('post_carbohydrate_low/', views.post_carbohydrate_low, name='post_carbohydrate_low'),
    path('post_carbohydrate_high/', views.post_carbohydrate_high, name='post_carbohydrate_high'),
    path('post_lipid_low/', views.post_lipid_low, name='post_lipid_low'),
    path('post_lipid_high/', views.post_lipid_high, name='post_lipid_high'),
]
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.IMAGE_URL, document_root=settings.IMAGE_ROOT)
