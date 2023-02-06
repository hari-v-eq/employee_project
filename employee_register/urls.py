from django.urls import path
from. import views
from employee_project.settings import DEBUG, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',views.employee_form,name='employee_insert'),
    path('list/',views.employee_list,name='employee_list'),
    path('<int:id>/',views.employee_form,name='employee_update'),
    path('delete<int:id>/',views.employee_delete,name='employee_delete'),
]

# if DEBUG:
   
#     urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)