from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from views import Index

urlpatterns = [    
    #Front
    url(r'^$', Index.as_view(), name="Index"),
   ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
