from django.urls import path
from apps.institute import views

from apps.institute.views import RegisterInstituteView

urlpatterns = [
    path(
        'register',
        views.RegisterInstituteView.as_view(),
        name='register-institute'
    ),
    path(
        'inistitutelist',
        views.ListInstituteView.as_view(),
        name = 'institute-list'
    ),
    path(
        '<institute_id>/scholorship/add',
        views.AddScholorshipView.as_view(),
        name = 'scholorship-add'
    ),
    path(
        '<institute_id>/scholorship/list',
        views.GetScholorshipListView.as_view(),
        name = 'scholorship-list'
    ),
    path(
        '<scholorship_id>/scholorship/update',
        views.UpdateScholorshipView.as_view(),
        name = 'scholorship-update'
    ),
    path(
        '<scholorship_id>/scholorship/delete',
        views.DeleteScholorshipView.as_view(),
        name= 'delete-scholorship-view'
    )
    # path()
]
