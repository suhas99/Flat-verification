from rest_framework import viewsets, serializers, routers, generics
from django.contrib.auth.models import User
from .serializer import UserSerializer, ChangeStatusSerializer, UserInviteSerializer, AlertSerializer, \
    AlertChangeStatusSerializer, ProjectSeralizer, ProjectStatusChangeSeralizer, FloorSerializer
    # FloorstatusupdateSerializer

# ,,PasswordSerializer
from django.contrib.auth.decorators import permission_required
from .models import User, Alerts, Projects, Floors
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.permissions import AllowAny
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from django.views.generic import ListView
from rest_framework import viewsets, mixins, status
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework import viewsets, mixins
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import viewsets
from django.views.generic.edit import UpdateView
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser, FormParser,MultiPartParser
from rest_framework import generics


class check_user:
    def check_admin_user(self, id):
        count, details = User.objects.filter(id=id, type="admin_user")
        if count is not None:
            return details.username


class UserInviteViewset(viewsets.ModelViewSet):
    """
           create:
                 Create a user.
    """
    http_method_names = ['post']
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = User.objects.filter(type="admin_user")
    serializer_class = UserInviteSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserInviteViewset(data=request.data)
        # serializer = self.serializer_class(data=request.data, context={'request': request})
        name = serializer.request.data['name']
        userEmail = serializer.request.data['email']
        if c := User(email=userEmail, name=name, username=name, type="admin_user"):
            return Response({
                'status': "ok",
                'id': c.pk,
                'type': c.type
            })
        else:
            return Response({
                'status': "Error"
            })


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
        retrieve:
              Return a particular from user profile.

        list:
             Get all users from user profile.
    """
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = User.objects.filter(type="admin_user")
    serializer_class = UserSerializer


class ChangeStatusViewset(viewsets.ModelViewSet):
    """
        update:
             Update status of a particular User.
    """
    http_method_names = ['put']
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = User.objects.filter(type="admin_user")
    serializer_class = ChangeStatusSerializer


class AlertsViewSet(viewsets.ReadOnlyModelViewSet):
    """
         retrieve:
               Return a particular alert.

         list:
              Get all alerts.
     """
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Alerts.objects.all()
    serializer_class = AlertSerializer


class AlertChangeStatusViewset(viewsets.ModelViewSet):
    """
           update:
                 Update status of a particular alert.
    """
    http_method_names = ['put']
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Alerts.objects.all()
    serializer_class = AlertChangeStatusSerializer

    # def post(self, request, *args, **kwargs):
    #     serializer_class = UserInviteSerializer
    #     userEmail = request.data['email']
    #     name = request.data['name']
    #     if c := User(email=userEmail, name=name, type="admin_user"):
    #         return Response({
    #             'status': "ok",
    #             'id': c.pk,
    #             'type': c.type
    #         })
    #     else:
    #         return Response({
    #             'status': "Error"
    #         })

    # def post(self, request, format=None):
    #     serializer = UserInviteSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomAuthToken(ObtainAuthToken):
    """
    create:
        Get auth credentials.
    """

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'id': user.pk,
            'type': user.type
        })


# #         serializer = PasswordSerializer(data=request.data)
# #         # serializer = self.serializer_class(data=request.data,
# #         #         :                           context={'request': request})
# #         user = serializer.validated_data['username']
# #         passwd = serializer.validated_data['password']

#     serializer = AnimalSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectViewSet(viewsets.ModelViewSet):
    """
        retrieve:
              Return a particular from Project .

        list:
             Get all projects.

        update:
            Update project status.

        create:
            create a project.

        destroy:
            Delete a project
    """
    http_method_names = ['get', 'post', 'delete']
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Projects.objects.all()
    serializer_class = ProjectSeralizer


class ProjectChangeStatus(viewsets.ModelViewSet):
    """
           update:
               Update role for a particular user.
    """
    http_method_names = ['put']
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Projects.objects.all()
    serializer_class = ProjectStatusChangeSeralizer


# class Floorcreate(viewsets.ModelViewSet):
#     permission_classes = [permissions.DjangoModelPermissions]
#     queryset = Floors.objects.all()
#     serializer_class = FloorstatusupdateSerializer
#
#     def post(self, request, *args, **kwargs):
#         id = self.request.query_params.get('id')
#         serializer = UserInviteViewset(data=request.data)
#         # serializer = self.serializer_class(data=request.data, context={'request': request})
#         type = serializer.request.data['type']
#         name = serializer.request.data['name']
#         extra = serializer.request.data['extra']
#         if c := Floors(house_id=id, type=type, name=name, extra=extra):
#             return Response({
#                 'status': "ok",
#             })
#         else:
#             return Response({
#                 'status': "Error"
#             })


# class Floorstatus(viewsets.ModelViewSet):
#     # http_method_names = ['put', 'get', 'delete']
#     permission_classes = [permissions.DjangoModelPermissions]
#     # queryset = Floors.objects.all()
#     serializer_class = FloorSerializer

# class Floorstatus(generics.ListCreateAPIView):
#     permission_classes = [permissions.DjangoModelPermissions]
#     queryset = Floors.objects.all()
#     serializer_class = FloorSerializer

# class Floorstatusupdate(generics.CreateAPIView):
#     permission_classes = [permissions.DjangoModelPermissions]
#     queryset = Floors.objects.all()
#     serializer_class = FloorstatusupdateSerializer


# class Floorstatus(mixins.ListModelMixin,
#                       mixins.CreateModelMixin,
#                       mixins.DestroyModelMixin,
#                       generics.GenericAPIView):
#
#     queryset = Floors.objects.all()
#     serializer_class = FloorSerializer
#     permission_classes = [permissions.DjangoModelPermissions]
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         name = request.GET.get('id')
#         return self.create(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# #
# class HouseViewset(viewsets.ModelViewSet):
#     """
#             retrieve:
#                   Return a particular from user profile.
#
#             list:
#                  Get all users from user profile.
#
#             update:
#                 Update role for a particular user.
#
#             create:
#                 create a project.
#
#             destroy:
#                 Delete a project
#         """
#     http_method_names = ['get', 'post', 'delete']
#     permission_classes = [permissions.DjangoModelPermissions]
#     queryset = House.objects.all()
#     serializer_class = HouseSeralizer
# #
#
# class Houseupdateview(UpdateView):
#     # http_method_names = ['put']
#     permission_classes = [permissions.DjangoModelPermissions]
#     model = House
#     fields = [status]

#
# class HouseViewset(viewsets.ModelViewSet):
#     http_method_names = ['get']
#     queryset = House.objects.all()
#     permission_classes = [permissions.DjangoModelPermissions]
#     serializer_class = HouseSeralizer
#
#     # @parser_classes([JSONParser])
#     def create(self, request, *args, **kwargs):
#         details = House.objects.all()
#         serializer = HouseSeralizer(House, many=True)
#         return Response(serializer.data)

# def retrieve(self, request, *args, **kwargs):
#     id=self.request.query_params.get('id')
#     detail=House.objects.filter(id=id)
#     serializer=

# # id = request.GET.get('id')
# if id:
#     detail=House.objects.get(id=id)
# else:
#     details=House.objects.all()
#     serializer = HouseSeralizer(House, many=True)
#     return Response(serializer.data)
# if detail:
#     serializer = HouseSeralizer(detail)
#     return Response(serializer.data)
# return Response(status=status.HTTP_404_NOT_FOUND)


# def get(self, request, format=None):
#     id = request.GET.get('id')
#     if id:
#         animal = House.objects.get(name=id)
#     else:
#         animals = House.objects.all()
#         serializer = HouseSeralizer(House, many=True)
#         return Response(serializer.data)
#
#     if animal:
#         serializer = HouseSeralizer(animal)
#         return Response(serializer.data)
#     return Response(status=status.HTTP_404_NOT_FOUND)

# def put(self, request, format=None):
#     name = request.GET.get('name')
#     animal = Animal.objects.get(name=name)
#     if animal:
#         serializer = AnimalSerializer(animal, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     return Response(status=status.HTTP_404_NOT_FOUND)
#
# def post(self, request, format=None):
#     serializer = AnimalSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# def delete(self, request, format=None):
#     name = request.GET.get('name')
#     animal = Animal.objects.get(name=name)
#     if animal:
#         animal.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     return Response(status=status.HTTP_400_BAD_REQUEST)
# #
# #
# # #
# # # class ResetViewSet(viewsets.ModelViewSet):
# # #     """
# # #     update:
# # #          Update a password for particular user.
# # #     """
# # #     http_method_names = ['post']
# # #     permission_classes = [permissions.DjangoModelPermissions]
# # #     queryset = Alerts.objects.all()
# # #     serializer_class = PasswordSerializer
# #
# # from django.contrib.auth import get_user_model
# # myuser=get_user_model()
# #
# # class ChangeReset(viewsets.ModelViewSet):
# #     """
# #     Change password
# #     """
# #     permission_classes = [permissions.DjangoModelPermissions]
# #     queryset = myuser.objects.all()
# #     serializer_class = PasswordSerializer
# #
# #     def post(self, request, *args, **kwargs):
# #         serializer = PasswordSerializer(data=request.data)
# #         # serializer = self.serializer_class(data=request.data,
# #         #         :                           context={'request': request})
# #         user = serializer.validated_data['username']
# #         passwd = serializer.validated_data['password']
# #         u = myuser.objects.get(username__exact=user)
# #         if u is not None:
# #             u.set_password(passwd)
# #             u.save()
# #             c = "password set"
# #             return Response(c, status=status.HTTP_201_CREATED)
# #         return Response("No user found", status=status.HTTP_400_BAD_REQUEST)
# #
# #
# #
# #
# #
# #     # def post(self, request):
# #     #     u = myuser.objects.get(username__exact=request.data['username'])
# #     #     if u is not None:
# #     #         u.set_password(request.data['password'])
# #     #         u.save()
# #     #         c="password set"
# #     #         return Response(c, status=status.HTTP_201_CREATED)
# #     #     return Response("No user", status=status.HTTP_400_BAD_REQUEST)
# #
# #
# #
# #
# #
# #

#
# class HouseAPIView(APIView):
#     permission_classes = [permissions.DjangoModelPermissions]
#     queryset = House.objects.all()
#
#     def get(self, request):
#         queryset = House.objects.all()
#         serailizer = HouseSeralizer(queryset, many=True)
#         return Response(serailizer.data, status=200)
#
#     def post(self, request):
#         data = request.data
#         project_id=request.query_params.get('id')
#         serializer = createHouseSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.erros, status=400)
#
# class PollDetailView(APIView):
#     def get_object(self, id):
#         try:
#             return House.objects.get(id=id)
#         except House.DoesNotExist as e:
#             return Response( {"error": "Given question object not found."}, status=404)
#
#     def get(self, request, id=None):
#         instance = self.get_object(id)
#         serailizer = HouseSeralizer(instance)
#         return Response(serailizer.data)
#
#     def put(self, request, id=None):
#         data = request.data
#         instance = self.get_object(id)
#         serializer = ProjectChangeStatus(instance, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=200)
#         return Response(serializer.erros, status=400)
#
#     def delete(self, request, id=None):
#         instance = self.get_object(id)
#         instance.delete()
#         return Response(status=204)

# class FloorsList(APIView):
#     parser_classes = (MultiPartParser, FormParser)
#     permission_classes = [permissions.DjangoModelPermissions]
#     queryset = Floors.objects.all()
#
#     def get(self, request):
#         items = Floors.objects.all()
#         serlaizer = FloorSerializer(items, many=True)
#         return Response(serlaizer.data, status=200)
#
#     def post(self, request):
#         data = request.data
#         serializer = FloorSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)


# class FloorsList(APIView):
#     # parser_classes = (MultiPartParser, FormParser)
#     queryset = Floors.objects.all()
#
#     # permission_classes = [permissions.DjangoModelPermissions]
#
#     def get(self, request):
#         items = Floors.objects.all()
#         serlaizer = FloorSerializer(items, many=True)
#         return Response(serlaizer.data, status=200)
#
#     # parser_classes = [JSONParser ]
#     def post(self, request, format=None):
#         data = request.data
#         serializer = FloorSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

class Floorstatus(viewsets.GenericViewSet):

    def get_queryset(self):
        queryset = Floors.objects.all()
        return queryset

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.get(pk=self.kwargs['pk'])
        return obj

    def list(self, request):
        queryset = self.get_queryset()
        serializer = FloorSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, **kwargs):
        obj = self.get_object()
        serializer = FloorSerializer(obj)
        return Response(serializer.data)

