
from django.contrib import admin
from django.urls import path, include
from bookings.views import movie_list, book_seat, booking_history

urlpatterns = [
    # Django admin dashboard
    path('admin/', admin.site.urls),

    # REST API endpoints
    path('api/', include('bookings.urls')),

    # API authentication
    path('api-auth/', include('rest_framework.urls')),

    # User login and logout
    path('accounts/', include('django.contrib.auth.urls')),

    # Frontend pages
    path('', movie_list, name='movie_list'),
    path('movies/<int:movie_id>/book/', book_seat, name='book_seat'),
    path('history/', booking_history, name='booking_history'),
]


