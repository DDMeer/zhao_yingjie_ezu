
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
    CourseDetail,
    RegistrationDetail,
    InstructorCreate,
    SectionCreate,
    CourseCreate
)

urlpatterns = [


    path('instructor/',
         InstructorList.as_view(),
         name='courseinfo_instructor_list_urlpattern'),

    path('instructor/<int:pk>/',
         InstructorDetail.as_view(),
         name='courseinfo_instructor_detail_urlpattern'),

    path('instructor/create/',
         InstructorCreate.as_view(),
         name='courseinfo_instructor_create_urlpattern'),


    path('section/',
         SectionList.as_view(),
         name='courseinfo_section_list_urlpattern'),

    path('section/<int:pk>/',
         SectionDetail.as_view(),
         name='courseinfo_section_detail_urlpattern'),

    path('section/Create/',
         SectionCreate.as_view(),
         name='courseinfo_section_create_urlpattern'),

    path('course/',
         CourseList.as_view(),
         name='courseinfo_course_list_urlpattern'),
    path('course/<int:pk>/',
         CourseDetail.as_view(),
         name='courseinfo_course_detail_urlpattern'),
    path('course/Create/',
         CourseCreate.as_view(),
         name='courseinfo_course_create_urlpattern'),

    path('semester/',
         SemesterList.as_view(),
         name='courseinfo_semester_list_urlpattern'),

    path('semester/<int:pk>/',
         SemesterDetail.as_view(),
         name='courseinfo_semester_detail_urlpattern'),
    path('student/', StudentList.as_view(), name='courseinfo_student_list_urlpattern'),
    path('student/<int:pk>/',
         StudentDetail.as_view(),
         name='courseinfo_student_detail_urlpattern'),

    path('registration/', RegistrationList.as_view(), name='courseinfo_registration_list_urlpattern'),
    path('registration/<int:pk>/',
         RegistrationDetail.as_view(),
         name='courseinfo_registration_detail_urlpattern'),
]
