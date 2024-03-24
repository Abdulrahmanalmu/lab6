from django.shortcuts import render, redirect
from .models import Student, Course
from .forms import StudentForm, CourseForm

def students_view(request):
    students = Student.objects.all()
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
    return render(request, 'students.html', {'students': students, 'form': form})

def courses_view(request):
    courses = Course.objects.all()
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses')
    return render(request, 'courses.html', {'courses': courses, 'form': form})

def details_view(request, student_id):
    student = Student.objects.get(id=student_id)
    available_courses = Course.objects.exclude(students=student)
    if request.method == 'POST':
        selected_course_id = request.POST.get('course_id')
        if selected_course_id:
            selected_course = Course.objects.get(id=selected_course_id)
            student.courses.add(selected_course)
            student.save()
            return redirect('details', student_id=student_id)
    return render(request, 'details.html', {'student': student, 'available_courses': available_courses})
