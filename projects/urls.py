from django.urls import path
from projects.views import projectsindex , projectDetail,CreateprojectView,EditprojectView,deletprojectView
urlpatterns = [
    path('index', projectsindex ),
    path('<int:pk>', projectDetail.as_view(), name='projects.show'),
    path('create', CreateprojectView.as_view()), 
    path('edit/<int:pk>', EditprojectView.as_view(), name='projects.edit'),
    path('delete/<int:pk>', deletprojectView.as_view(), name='projects.delete'),
]
 