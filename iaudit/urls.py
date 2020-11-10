from django.urls import path
from iaudit.views import DetailedHardwareEntitlement, ListHardwareEntitlement


urlpatterns = [
path('<int:pk>/', DetailedHardwareEntitlement.as_view()),
path('', ListHardwareEntitlement.as_view()),
]