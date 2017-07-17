from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from api import views

router = routers.DefaultRouter ()
# router.register (r'user', views.UserViewSet)
# router.register (r'apar', views.AparViewSet)
# router.register (r'inspection', views.InspectionReportViewSet)
# router.register (r'pressure-report', views.PressureReportViewSet)
# router.register (r'apar/detail/(?P<id>[\d]+)', views.AparDetail)

urlpatterns = [
    # url (r'^', include (router.urls)),
    url (r'^token', obtain_auth_token),
    url (r'^user/(?P<username>[\w]+)$', views.UserRetrieve.as_view ()),
    url (r'^apar/all$', views.AparViewSet.as_view ()),
    url (r'^apar/detail/(?P<id>[\d]+)$', views.AparRetrieve.as_view ()),
    url (r'^inspection/all$', views.InspectionReportList.as_view ()),
    url (r'^verification/all$', views.VerificationReportList.as_view ()),
    url (r'^inspect$', views.inspect),
    url (r'^verify$', views.verify),
    url (r'^report$', views.ReportCreate.as_view ())
]