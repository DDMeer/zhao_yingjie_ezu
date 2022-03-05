
from django.urls import path
from courseinfo.views import (
    # instructor_list_view,
    # section_list_view,
    # course_list_view,
    # semester_list_view,
    # student_list_view,
    # registration_list_view,
    InstructorList,
    SectionList,
    CourseList,
    SemesterList,
    StudentList,
    RegistrationList,
    InstructorDetail, SectionDetail,
)

urlpatterns = [
    # path('instructor/', instructor_list_view),

    path('instructor/', InstructorList.as_view(), name='courseinfo_instructor_list_urpattern'),
    path('instructor/<int:pk>/',
         InstructorDetail.as_view(),
         name='courseinfo_instructor_detail_urlpattern'),
    # path('section/', section_list_view),
    path('section/', SectionList.as_view(), name='courseinfo_section_list_urpattern'),
    path('section/<int:pk>/',
         SectionDetail.as_view(),
         name='courseinfo_section_detail_urlpattern'),
    # path('course/', course_list_view),
    path('course/', CourseList.as_view(), name='courseinfo_course_list_urpattern'),
    # path('semester/', semester_list_view),
    path('semester/', SemesterList.as_view(), name='courseinfo_semester_list_urpattern'),
    # path('student/', student_list_view),
    path('student/', StudentList.as_view(), name='courseinfo_student_list_urpattern'),
    # path('registration/', registration_list_view),
    path('registration/', RegistrationList.as_view(), name='courseinfo_registration_list_urpattern'),

]
