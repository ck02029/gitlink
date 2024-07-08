from django.urls import path , re_path


from django.urls import path, include


from rest_framework import routers

from organization import views 

from django.conf import settings

from django.conf.urls.static import static


# router = routers.DefaultRouter()
# router.register(r'work/', views.WorkExperienceViewset)
# router.register(r'education/', views.EducationViewset)


urlpatterns = [
     #path('route/', view_name, name='route-name'),
    # path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)