
from django.urls import path
from courseinfo.views import (
    # instructor_list_view,
    # section_list_view,
    # course_list_view,
    semester_list_view,
    student_list_view,
    registration_list_view,
    InstructorList,
    SectionList,
    CourseList,
)

urlpatterns = [
    # path('instructor/', instructor_list_view),

    path('instructor/', InstructorList.as_view(), name='courseinfo_instructor_list_urpattern'),
    # path('section/', section_list_view),
    path('section/', SectionList.as_view(), name='courseinfo_section_list_urpattern'),
    # path('course/', course_list_view),
    path('course/', CourseList.as_view(), name='courseinfo_course_list_urpattern'),
    path('semester/', semester_list_view),
    path('student/', student_list_view),
    path('registration/', registration_list_view),

]
