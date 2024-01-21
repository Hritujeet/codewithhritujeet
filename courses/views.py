from django.shortcuts import render, HttpResponse
from .models import Course, Tutorial

# Create your views here.
def main(request):
    allCourses = Course.objects.order_by('-id')
    print(allCourses)

    allSlugs = []

    for i in allCourses:
        tut = Tutorial.objects.filter(course=i.name).first()
        print(tut.slug)
        allSlugs.append(tut.slug)

    params = {"courses":zip(allCourses, allSlugs)}

    return render(request, 'courses/courseHome.html', params)

def course(request, slug):
    tutorial = Tutorial.objects.filter(slug=slug).first()
    course = Course.objects.filter(name=tutorial.course).first()

    allTuts = Tutorial.objects.filter(course=course.name)
    print(allTuts)

    params = {"tut":tutorial, "course":course, "allTuts":allTuts}

    return render(request, 'courses/course.html', params)