from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('locations/', views.location_handler, name='locations'),
    path('locations/create/', views.location_handler, name='location_create'),
    path('locations/<int:pk>/', views.location_handler, name='location_detail'),
    path('locations/<int:pk>/update/', views.location_handler, name='location_update'),
    path('locations/<int:pk>/delete/', views.location_handler, name='location_delete'),

    path('roads/', views.road_handler, name='roads'),
    path('roads/create/', views.road_handler, name='road_create'),
    path('roads/<int:pk>/', views.road_handler, name='road_detail'),
    path('roads/<int:pk>/update/', views.road_handler, name='road_update'),
    path('roads/<int:pk>/delete/', views.road_handler, name='road_delete'),

    path('contypes/', views.contype_handler, name='contypes'),
    path('contypes/create/', views.contype_handler, name='contype_create'),
    path('contypes/<int:pk>/', views.contype_handler, name='contype_detail'),
    path('contypes/<int:pk>/update/', views.contype_handler, name='contype_update'),
    path('contypes/<int:pk>/delete/', views.contype_handler, name='contype_delete'),

    path('traffic/', views.traffic_handler, name='traffic'),
    path('traffic/create/', views.traffic_handler, name='traffic_create'),
    path('traffic/<int:pk>/', views.traffic_handler, name='traffic_detail'),
    path('traffic/<int:pk>/update/', views.traffic_handler, name='traffic_update'),
    path('traffic/<int:pk>/delete/', views.traffic_handler, name='traffic_delete'),







    # path('locations', views.list_locations, name='locations'),
    # path('roads', views.list_roads, name='roads'),
    # path('contypes', views.list_contypes, name='contypes'),
    # path('traffic', views.list_traffic, name='traffic'),
    #
    # path('get_locations', views.get_locations, name='get_locations'),
    # path('get_roads', views.get_roads, name='get_roads'),
    # path('get_con_types', views.get_congestion_types, name='get_con_types'),
    # path('get_traffic', views.get_traffic, name='get_traffic'),
    #
    # path('create_location', views.create_location, name='create_location'),
    # path('create_road', views.create_road, name='create_road'),
    # path('create_contype', views.create_contype, name='create_contype'),
    #
    # path('locations/<int:pk>', views.LocationDetailView.as_view(), name='detail_location'),
    # path('roads/<int:pk>', views.RoadDetailView.as_view(), name='detail_road'),
    # path('contypes/<int:pk>', views.ContypeDetailView.as_view(), name='detail_contype'),
    # path('traffic/<int:pk>', views.TrafficDetailView.as_view(), name='detail_traffic'),
    #
    # path('locations/<int:pk>/update', views.LocationUpdateView.as_view(), name='update_location'),
    # path('roads/<int:pk>/update', views.RoadUpdateView.as_view(), name='update_road'),
    # path('contypes/<int:pk>/update', views.ContypeUpdateView.as_view(), name='update_contype'),
    # path('traffic/<int:pk>/update', views.TrafficUpdateView.as_view(), name='update_traffic'),
    #
    # path('locations/<int:pk>/delete', views.LocationDeleteView.as_view(), name='delete_location'),
    # path('roads/<int:pk>/delete', views.RoadDeleteView.as_view(), name='delete_road'),
    # path('contypes/<int:pk>/delete', views.ContypeDeleteView.as_view(), name='delete_contype'),
]