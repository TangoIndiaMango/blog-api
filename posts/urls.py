from django.urls import path
from rest_framework.routers import SimpleRouter
from .models import Post
from .views import UserViewSet, PostViewSet


router = SimpleRouter()

router.register("users", UserViewSet, basename="users")
router.register("", PostViewSet, basename="posts")

urlpatterns = router.urls

# urlpatterns = [
#     path("users/", UserList.as_view(), name=""),
#     path("users/<int:pk>/", UserDetail.as_view(), name=""),
#     path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
#     path("", PostList.as_view(), name="post_list"),
# ]


# PostList, PostDetail, UserList, UserDetail
