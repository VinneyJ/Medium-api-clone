from authors_api.settings.local import DEFAULT_FROM_EMAIL
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView


from .exceptions import CantFollowYourself, NotyourProfile
from .models import Profile
from .pagination import ProfilePagination
from .renderer import ProfileJSONRenderer, ProfilesJSONRenderer
from .serializers import ProfileSerializer,  UpdateProfileSerializer, FollowingSerializer


User = get_user_model()

# @api_view(["GET"])
# @permission_classes([permissions.AllowAny])
# def get_all_profiles(request):
#     profiles = Profile.objects.all()
#     serializer = ProfileSerializer(profiles, many=True)
#     namespaced_response = {"profiles": serializer.data}
#     return Response(namespaced_response, status=status.HTTP_200_OK)


# @api_view(["GET"])
# @permission_classes([permissions.AllowAny])
# def get_profile_details(request, username):
#     try:
#         user_profile = Profile.objects.filter(user__username=username)
#     except Profile.DoesNotExist:
#         raise NotFound('A profile with this username does not exist...')
    
#     serializer = ProfileSerializer(user_profile, many=False)
#     formatted_response = {"profile": serializer.data}
#     return Response(formatted_response, status=status.HTTP_200_OK)



class ProfileListAPIView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()
    renderer_classes = (ProfilesJSONRenderer,)
    pagination_class = ProfilePagination


class ProfileDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.select_related("user")
    serializer_class = ProfileSerializer
    renderer_classes = (ProfileJSONRenderer,)

    def retrieve(self, request, username, *args, **kwargs):

        try:
            user_profile = self.queryset.get(user__username=username)
        except Profile.DoesNotExist:
            raise NotFound('A profile with this username does not exist...')
        
        serializer = self.serializer_class(user_profile, context={"request": request})

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class UpdateProfileAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.select_related("user")
    renderer_classes = [ProfilesJSONRenderer]
    serializer_class = UpdateProfileSerializer

    def patch(self, request, username):
        try:
            self.queryset.get(user__username=username)
        except Profile.DoesNotExist:
            raise NotFound('A profile with this username does not exist...')

        current_user = request.user.username

        if current_user != username:
            raise NotyourProfile
        
        data = request.data

        serializer = UpdateProfileSerializer(instance=request.user.profile, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def get_my_followers(request, username):
    try:
        specific_user = User.objects.get(username=username)
    except:
        raise NotFound('A user with this username does not exist...')
    
    user_profile_instance = Profile.objects.get(user__pkid=specific_user.pkid)

    user_followers = user_profile_instance.followed_by.all()
    serialializer = FollowingSerializer(user_followers, many=True)
    formatted_response = {
        "status_code": status.HTTP_200_OK,
        "followers": serialializer.data,
        "number_of_followers": len(serialializer.data)
    }
    return Response(formatted_response, status=status.HTTP_200_OK)


class FollowUnfollowAPIView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FollowingSerializer

    def get(self, request, username):
        try:
            specific_user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise NotFound("User with that username does not exist")
        
        user_profile_instance = Profile.objects.get(user__pkid=specific_user.pkid)

        my_following_list = user_profile_instance.following_list()
        serializer = ProfileSerializer(my_following_list, many=True)
        formatted_response = {
            "status_code": status.HTTP_200_OK,
            "users_i_follow": serializer.data,
            "num_of_users_i_follow": len(serializer.data)
        }

        return Response(formatted_response, status=status.HTTP_200_OK)
    
    def post(self, request, username):
        try:
            specific_user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise NotFound("User with that username does not exist")
        
        if specific_user.pkid == request.user.pkid:
            raise CantFollowYourself
        
        user_profile_instance = Profile.objects.get(user__pkid=specific_user.pkid)

        current_user_profile = request.user.profile

        if current_user_profile.check_following(user_profile_instance):
            formatted_response = {
                "status_code": status.HTTP_400_BAD_REQUEST,
                "errors": f"You already follow {specific_user}"
            }
            return Response(formatted_response, status=status.HTTP_400_BAD_REQUEST)
        
        current_user_profile.follow(user_profile_instance)

        subject = "A new user follows you"
        message = f"Hi there {specific_user.username}!!, the user {current_user_profile.user.username} now follows you."
        from_email = DEFAULT_FROM_EMAIL
        recipient_list = [specific_user.email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=True)

        return Response(
            {
            "status_code": status.HTTP_200_OK,
            "detail": f"You now follow {specific_user.username}"
            }
        )
    
    def delete(self, request, username):
        try:
            specific_user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise NotFound("User with that username does not exist")
        
        user_profile_instance = Profile.objects.get(user__pkid=specific_user.pkid)

        current_user_profile = request.user.profile

        if not current_user_profile.check_following(user_profile_instance):
            # check if not following a specific user
            formatted_response = {
                "status_code": status.HTTP_400_BAD_REQUEST,
                "errors": f"You do not follow {specific_user.username}"
            }
            return Response(formatted_response, status=status.HTTP_400_BAD_REQUEST)
        
        current_user_profile.unfollow(user_profile_instance)
        formatted_response = {
                "status_code": status.HTTP_200_OK,
                "errors": f"You have unfollowed {specific_user.username}"
            }
        return Response(formatted_response, status=status.HTTP_200_OK)