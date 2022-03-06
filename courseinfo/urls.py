
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
    InstructorDetail,
    SectionDetail,
    SemesterDetail,
    StudentDetail,
    CourseDetail, RegistrationDetail,

)

urlpatterns = [


    path('instructor/', InstructorList.as_view(), name='courseinfo_instructor_list_urpattern'),
    path('instructor/<int:pk>/',
         InstructorDetail.as_view(),
         name='courseinfo_instructor_detail_urlpattern'),

    path('section/', SectionList.as_view(), name='courseinfo_section_list_urpattern'),
    path('section/<int:pk>/',
         SectionDetail.as_view(),
         name='courseinfo_section_detail_urlpattern'),

    path('course/', CourseList.as_view(), name='courseinfo_course_list_urpattern'),
    path('course/<int:pk>/',
         CourseDetail.as_view(),
         name='courseinfo_course_detail_urlpattern'),

    path('semester/', SemesterList.as_view(), name='courseinfo_semester_list_urpattern'),

    path('semester/<int:pk>/',
         SemesterDetail.as_view(),
         name='courseinfo_semester_detail_urpattern'),
    path('student/', StudentList.as_view(), name='courseinfo_student_list_urpattern'),
    path('student/<int:pk>/',
         StudentDetail.as_view(),
         name='courseinfo_student_detail_urlpattern'),

    path('registration/', RegistrationList.as_view(), name='courseinfo_registration_list_urpattern'),
    path('registration/<int:pk>/',
         RegistrationDetail.as_view(),
         name='courseinfo_registration_detail_urpattern'),
]
