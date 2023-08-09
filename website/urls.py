from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('login/',views.login_user, name='login'),
    path('logout/',views.logout_user, name='logout'),
    path('register/',views.register, name='register'),
    path('record/<int:pk>',views.customer_record, name='record'),
    path('delete_record/<int:pk>',views.delete_record, name='delete_record'),
    path('create_record/',views.create_record, name='create_record'),
    path('update/<int:pk>/',views.update_record, name='update_record'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)