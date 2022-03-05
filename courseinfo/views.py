from django.shortcuts import render
from django.views import View

from courseinfo.models import (
    Instructor,
    Section,
    Course,
    Semester,
    Student,
    Registration,

)


# def instructor_list_view(request):
#     # instructor_list = Instructor.objects.all()
#     instructor_list = Instructor.objects.none()
#     return render(request, 'courseinfo/instructor_list.html', {'instructor_list': instructor_list})

class InstructorList(View):

    def get(self, request):
        return render(
            request,
            'courseinfo/instructor_list.html',
            {'instructor_list': Instructor.objects.all()}
        )

# def section_list_view(request):
#     # section_list = Section.objects.all()
#     section_list = Section.objects.none()
#     return render(request, 'courseinfo/section_list.html', {'section_list': section_list})


class SectionList(View):

    def get(self, request):
        return render(
            request,
            'courseinfo/section_list.html',
            {'section_list': Section.objects.all()}
        )


#
# def course_list_view(request):
#     # course_list = Course.objects.all()
#     course_list = Course.objects.none()
#     return render(request, 'courseinfo/course_list.html', {'course_list': course_list})


class CourseList(View):

    def get(self, request):
        return render(
            request,
            'courseinfo/course_list.html',
            {'course_list': Course.objects.all()}
        )

# def semester_list_view(request):
#     semester_list = Semester.objects.all()
#     # semester_list = Semester.objects.none()
#     return render(request, 'courseinfo/semester_list.html', {'semester_list': semester_list})
class SemesterList(View):

    def get(self, request):
        return render(
            request,
            'courseinfo/semester_list.html',
            {'course_list': Semester.objects.all()}
        )



# def student_list_view(request):
#     student_list = Student.objects.all()
#     # student_list = Student.objects.none()
#     return render(request, 'courseinfo/student_list.html', {'student_list': student_list})


class StudentList(View):

    def get(self, request):
        return render(
            request,
            'courseinfo/student_list.html',
            {'course_list': Student.objects.all()}
        )

# def registration_list_view(request):
#     registration_list = Registration.objects.all()
#     # registration_list = Registration.objects.none()
#     return render(request, 'courseinfo/registration_list.html', {'registration_list': registration_list})


class RegistrationList(View):

    def get(self, request):
        return render(
            request,
            'courseinfo/registration_list.html',
            {'course_list': Registration.objects.all()}
        )