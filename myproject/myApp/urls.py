from . import views
from django.urls import path
from django.conf import settings  
from django.conf.urls.static import static  

urlpatterns = [
    path('',views.index_view,name='index'),
    path('gallery',views.gallery_view,name='gallery'),
    path('register/',views.register_view,name='register'),
    path('success',views.success_view,name='success'),
    path('gallery_details/<str:name>/',views.product,name='gallery_details'),
    path('about',views.aboutus,name='about')
]
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  