from django.conf.urls import url
from . import views

app_name = "images" # Django 2.0 need it.
urlpatterns = [
    url(
        regex=r'^$',
        view=views.Images.as_view(),
        name='feed'
    ),
    url(
    	regex=r'^(?P<image_id>[0-9]+)/$',
    	view=views.ImageDetail.as_view(),
    	name='detail_image'
    ),
    url(
    	regex=r'^(?P<image_id>\w+)/like/',
    	view=views.LikeImage.as_view(),
    	name='like_image'
    ),
    url(
    	regex=r'^(?P<image_id>\w+)/unlike/',
    	view=views.UnLikeImage.as_view(),
    	name='unlike_image'
    ),
    url(
    	regex=r'^(?P<image_id>[0-9]+)/comments/(?P<comment_id>[0-9]+)/$',
    	view=views.ModerateComments.as_view(),
    	name='comment_delete'
    ),
    url(
    	regex=r'^(?P<image_id>\w+)/comments/',
    	view=views.CommentOnImage.as_view(),
    	name='comment_image'
    ),
    url(
    	regex=r'^comments/(?P<comment_id>[0-9]+)/$',
    	view=views.Comment.as_view(),
    	name='comment'
    ),
    url(
    	regex=r'^search/$',
    	view=views.Search.as_view(),
    	name='search'
    )
]

#0 create the url and the view
#1 take the id from the url
#2 we wnat to find an image with this id
#3 we want to create a like for that image