"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
from rest_framework.authtoken import views as authview
from .apiViews import UserViewSet,ChangeStatusViewset,UserInviteViewset,AlertsViewSet,AlertChangeStatusViewset,CustomAuthToken,ProjectViewSet,ProjectChangeStatus,Floorstatus# AlertsViewSet,

# schema_view = get_swagger_view(title='Nemmadi API')
schema_view = get_schema_view(title='Nemmadi API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer],
                              description="This project contains all the backend apis")

router = routers.DefaultRouter()
router.register(r'users/invite', UserInviteViewset, basename='Invite  operations')
router.register(r'users', UserViewSet, basename='user profile operations')
router.register(r'users/changestatus', ChangeStatusViewset, basename='change status operations')
router.register(r'users/alerts/', AlertsViewSet, basename='Alerts related operations')
router.register(r'users/alerts/change', AlertChangeStatusViewset, basename='Alerts status change related operations')
router.register(r'projects',ProjectViewSet,basename="project details operations")
router.register(r'projects/changestatus',ProjectChangeStatus,basename="project change status operations")
router.register(r'floors',Floorstatus,basename="House operations")
# router.register(r'house',HouseViewset,basename="House operations")











# router.register(r'users/alerts', AlertsViewSet, basename='Alert   operations')
# # router.register(r'users/reset', ResetViewSet, basename="Reset operations")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view),
    path('', include(router.urls)),
    # # path('auth/', include('djoser.urls.authtoken')),
    # # path('auth/', authview.obtain_auth_token, name='api-tokn-auth'),
    path('auth/', CustomAuthToken.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('House/', HouseAPIView.as_view()),
    # path('users',UserInviteViewset.as_view('post')),
    # path('floors/<int:id>', Floorcreate),
    # path('Floors/',Floorstatusupdate.as_view),
    # path('floors/', FloorsList.as_view()),
    # path('floors', BlobDetail.as_view()),





    # path('House/<int:id>/', HouseAPIView.as_view(), name='poll_edit'),
    # path('House/<int:id>/', HouseAPIView.as_view(), name='poll_delete'),
    # path('House/list/', index, name='polls_list'),
    # path('House/<int:id>/details/', details, name="poll_details"),
    # path('House/<int:id>/', vote_poll, name="poll_vote")

    # path('users/change/',ChangeReset.as_view())
    # ,

]
