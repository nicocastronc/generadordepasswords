from django.urls import path
from generatorapp import views

#Despliegue
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.home),
    path('about/',views.about),
    path('pass_generada/',views.password,name='pass'),
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
