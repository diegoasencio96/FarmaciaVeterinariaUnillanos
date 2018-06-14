from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from views import test

urlpatterns = [    
    #Front
    url(r'^$', test, name="Index"),
   ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
