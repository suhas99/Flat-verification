from rest_framework import serializers
from django.contrib.auth.models import User as u
from rest_framework.serializers import ModelSerializer

from .models import User, Alerts, Projects, Floors, Blob


#
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'username', 'tel', 'type', 'status', 'profile_image']


class ChangeStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['status']


class AlertSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alerts
        fields = ['id', 'title', 'detail', 'status', 'app_redirect']


class AlertChangeStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alerts
        fields = ['status']


class UserInviteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'name']


class HouseFloornested(ModelSerializer):
    class Meta:
        model = Floors
        fields = ['id', 'name']


class ProjectSeralizer(serializers.HyperlinkedModelSerializer):
    floors = HouseFloornested(read_only=True)

    class Meta:
        model = Projects
        fields = ['id', 'name', 'location', 'type', 'status', 'name', 'nm_meta', 'floors']


class ProjectStatusChangeSeralizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Projects
        fields = ['status']
        lookup_field = 'id'


class nestedtry(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username']


#
# class HouseSeralizer(ModelSerializer):
#     assigned_to = nestedtry(read_only=True)
#     # user_id = serializers.PrimaryKeyRelatedField(
#     #     queryset=User.objects.all(), source='User', write_only=True)
#     # floors=HouseFloornested(read_only=True)
#     # floors_id = serializers.PrimaryKeyRelatedField(
#     #     queryset=Floors.objects.get(house_id=id), source='Floors', write_only=True)
#     floors = HouseFloornested(read_only=True)
#
#     class Meta:
#         model = House
#         # fields = ['id', 'name', 'nm_meta','assigned_to','user_id','floors','floors_id']
#         fields = ['id', 'name', 'nm_meta', 'assigned_to', 'floors']
#         read_only_fields = ["floors", "assigned_to"]
#         depth = 2

# def to_representation(self, instance):
#     response = super().to_representation(instance)
#     response['floors'] = HouseFloornested(instance.floors).data
#     return response


# class HouseretriveSerializer(serializers.HyperlinkedModelSerializer):

#
#
# class PasswordSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username', 'password']
#
#

# class createHouseSerializer(ModelSerializer):
#     class Meta:
#         model = House
#         fields = ['id', 'project_id', 'name']


# class blobNestedSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Blob
#         fields = ('id', 'data')


# class FloorSerializer(ModelSerializer):
#     # Blob_filed = blobNestedSerializer(many=True,write_only=True)
#     # _id = serializers.PrimaryKeyRelatedField(
#     #         queryset=Blob.objects.all(), source='Blob', write_only=True)
#     blobs = blobNestedSerializer(many=False)
#
#     class Meta:
#         model = Floors
#         fields = ('id', 'name', 'type', 'nm_meta', 'extra', 'blobs')

# def to_representation(self, instance):
#     response = super().to_representation(instance)
#     response['Blob'] = blobNested(instance.Blob).data
#     return response

# class FloorSerializer(serializers.ModelSerializer):
#     # blob=blobNestedSerializer()
#     # def to_internal_value(self, data):
#     #     self.fields['blob'] = serializers.PrimaryKeyRelatedField(
#     #         queryset=Blob.objects.all())
#     #     return super(FloorSerializer, self).to_internal_value(data)
#     blob_data = blobNestedSerializer(read_only=True, many=True)
#
#     class Meta:
#         model = Floors
#         fields = ('id', 'name', 'type', 'nm_meta', 'extra', 'blob_data')
#
#     def create(self, validated_data):
#         if validated_data.get('blobs'):
#             blob_data = validated_data.pop('blobs') | None
#         floor = Floors.objects.create(**validated_data)
#         if blob_data:
#             for blobs in blob_data:
#                 Blob.objects.create(floor_id=floor, **blobs)
#         return floor
#
#
# class FloorstatusupdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Floors
#         fields = ('type', 'name', 'extra')

# class BlobSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Blob
#         fields = ['floor_id', 'data']
#
#
#
# class FloorSerializer(serializers.ModelSerializer):
#     blobs = BlobSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Floors
#         fields = ['house_id', 'type', 'name', 'blobs']
#
#     def create(self, validated_data):
#         if validated_data.get('blobs'):
#             blob_data = validated_data.pop('blobs') | None
#         floor = Floors.objects.create(**validated_data)
#         if blob_data:
#             for blobs in blob_data:
#                 Blob.objects.create(floor_id=floor, **blobs)
#         return floor
#

class BlobSerializer(serializers.ModelSerializer):
    data = serializers.FileField()

    class Meta:
        model = Blob
        fields = ['floor_id', 'data']


class FloorSerializer(serializers.ModelSerializer):
    blobs = BlobSerializer(many=True, read_only=True ,required=False)

    class Meta:
        model = Floors
        fields = ['id', 'house_id', 'type', 'name', 'blobs']

    # def create(self, validated_data):
    #     blobs = validated_data.pop('blobs') if validated_data.get('blobs') else []
    #     floor = Floors.objects.create(**validated_data)
    #     for blob in blobs:
    #         Blob.objects.create(**blob, floor_id = floor)
    #     return floor
