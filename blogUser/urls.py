from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from blogUser import views

urlpatterns = [
    path("crear/", views.SignUp.as_view(), name ="blogUser_signup"),
    path("profile/<pk>/", views.BlogUserProfile.as_view(), name ="blogUser_profile"),
    path("editar/<pk>/", views.BlogUserUpdate.as_view(), name ="blogUser_edit"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)