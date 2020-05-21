from rest_framework_swagger.views import get_swagger_view
from rest_framework_simplejwt import views as jwt_views
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from .views import *

schema_view = get_swagger_view(title='BOOKSTORE API')


urlpatterns = [
    
    path('api-docs/', schema_view),

    path('', ApiRoot.as_view(), name=ApiRoot.name),

    path('users/', UserListView.as_view(), name=UserListView.name),
    path('users/<int:pk>/', UserDetail.as_view(), name=UserDetail.name),

    path('address/', AddressListView.as_view(), name=AddressListView.name),
    path('address/<int:pk>/', AddressDetail.as_view(), name=AddressDetail.name),

    path('clients/', ClientListView.as_view(), name=ClientListView.name),
    path('clients/<int:pk>/', ClientDetail.as_view(), name=ClientDetail.name),

    path('managers/', ManagerListView.as_view(), name=ManagerListView.name),
    path('managers/<int:pk>/', ManagerDetail.as_view(), name=ManagerDetail.name),

    path('status/', StatusListView.as_view(), name=StatusListView.name),
    path('status/<int:pk>/', StatusDetail.as_view(), name=StatusDetail.name),

    path('genres/', GenreListView.as_view(), name=GenreListView.name),
    path('genres/<int:pk>/', GenreDetail.as_view(), name=GenreDetail.name),
    
    path('authors/', AuthorListView.as_view(), name=AuthorListView.name),
    path('authors/<int:pk>/', AuthorDetail.as_view(), name=AuthorDetail.name),

    path('writes/', WriteListView.as_view(), name=WriteListView.name),
    path('writes/<int:pk>/', WriteDetail.as_view(), name=WriteDetail.name),

    path('books/', BookListView.as_view(), name=BookListView.name),
    path('books/<int:pk>/', BookDetail.as_view(), name=BookDetail.name),

    path('orders/', OrderListView.as_view(), name=OrderListView.name),
    path('orders/<int:pk>/', OrderDetail.as_view(), name=OrderDetail.name),

    path('itemsorders/', ItemOrderListView.as_view(), name=ItemOrderListView.name),
    path('itemsorders/<int:pk>/', ItemOrderDetail.as_view(), name=ItemOrderDetail.name),

    path('creditscards/', CreditCardListView.as_view(), name=CreditCardListView.name),
    path('creditscards/<int:pk>/', CreditCardDetail.as_view(), name=CreditCardDetail.name),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api-token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

