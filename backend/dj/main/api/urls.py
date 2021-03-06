from django.urls import path

from .views import UserListView, UserDetailView, LearningCreditsUpdateView, WorkshopListView, WorkshopDetailView, WorkshopCreateView, WorkshopUpdateView, EnrollmentListView, EnrollmentDetailView, EnrollmentCreateView, EnrollmentUpdateView, EnrollmentDestroyView

urlpatterns = [
    path('user/', UserListView.as_view()),
    path('user/<pk>/', UserDetailView.as_view()),
    path('user/<pk>/updatelc', LearningCreditsUpdateView.as_view()),
    path('workshop/', WorkshopListView.as_view()),
    path('workshop/detail/<pk>/', WorkshopDetailView.as_view()),
    path('workshop/detail/<pk>/update/', WorkshopUpdateView.as_view()),
    path('workshop/create/', WorkshopCreateView.as_view()),
    path('enrollment/', EnrollmentListView.as_view()),
    path('enrollment/detail/<pk>/', EnrollmentDetailView.as_view()),
    path('enrollment/create/', EnrollmentCreateView.as_view()),
    path('enrollment/detail/<pk>/update/', EnrollmentUpdateView.as_view()),
    path('enrollment/detail/<pk>/delete/', EnrollmentDestroyView.as_view()),

]
