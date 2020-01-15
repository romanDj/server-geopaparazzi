from django.urls import path
from django.conf.urls import url
from .views import SubdivisionListView, SubdivisionDetailView, SubdivisionCreate, SubdivisionUpdate, SubdivisionDelete

urlpatterns = [
	path("", SubdivisionListView.as_view(), name="subdivision_list"),
	path('<int:pk>/', SubdivisionDetailView.as_view(), name="subdivision_detail"),
	path('create/', SubdivisionCreate.as_view(), name="subdivision_create"),
	path('update/<int:pk>/', SubdivisionUpdate.as_view(), name="subdivision_update"),
	path('delete/<int:pk>/', SubdivisionDelete.as_view(), name="subdivision_update"),
]
