from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login  # Renamed to avoid conflict
from .forms import CustomUserCreationForm, BlogPostForm, UnitForm, LessonForm
from django.contrib import messages
from .models import BlogPost,Lesson, Unit

# Create your views here.
def homeView(request):
    return render(request, 'home.html')

def getBlog(request):
    return render(request, 'table.html')

def addUnit(request):
    return render(request, 'unitForm.html')



def editLesson(request, id):
    # Logic to fetch the lesson by id could be added here
    return render(request, 'blogForm.html')

def addContent(request):
    if request.method == 'POST':
        # Handle form submission logic here
        pass
    return render(request, 'blogForm.html')

def loginView(request):  # Renamed to avoid conflict
    if request.method == 'POST':
        # Handle login logic here
        pass
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Log the user in immediately after registration
            messages.success(request, "You are logged in!!!")
            return redirect('home')  # Redirect to a success page or home page
        messages.error(request, "There is an error. Try with correct information.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def submitContentView(request):
    if request.method =='POST':
        print(request.POST.get('content'))
        return redirect('home')
    return render(request, 'blogForm.html')

def forgotPassword(request):
    return render(request, 'forgotPassword.html')

def getAutomation(request):
    return render(request, 'automation.html')

def create_lesson(request, unit_id):
    unit = get_object_or_404(Unit, id=unit_id)
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.unit = unit
            lesson.save()
            messages.success(request, "Lesson created successfully!")

            return redirect('unit_detail', unit_id=unit.id)
        messages.error(request, "All fields are required.")

    else:
        form = LessonForm()
    return render(request, 'create_lesson.html', {'form': form, 'unit': unit})

def lesson_detail(request, unit_id, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id, unit_id=unit_id)
    return render(request, 'lesson_detail.html', {'lesson': lesson})


def edit_lesson(request, unit_id, lesson_id):
    unit = get_object_or_404(Unit, id=unit_id)
    lesson = get_object_or_404(Lesson, id=lesson_id, unit=unit)

    if request.method == 'POST':
        form = LessonForm(request.POST, instance=lesson)
        if form.is_valid():
            form.save()
            return redirect('unit_detail', unit_id=unit.id)
    else:
        form = LessonForm(instance=lesson)

    return render(request, 'edit_lesson.html', {
        'form': form,
        'unit': unit,
        'lesson': lesson
    })

def delete_lesson(request, unit_id, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id, unit_id=unit_id)
    if request.method == 'POST':
        lesson.delete()
        messages.success(request, "Lesson deleted successfully!")
    return redirect('unit_detail', unit_id=unit_id)

def lesson_list(request):
    lessons = Lesson.objects.all()
    return render(request, 'lesson_list.html', {'lessons': lessons})


def create_unit(request):
    if request.method == 'POST':
        form = UnitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('unit_list')  # replace with your success URL/view name
    else:
        form = UnitForm()
    return render(request, 'create_unit.html', {'form': form})

def edit_unit(request,unit_id):
    return render(request, 'unitForm.html')

# List all units
def unit_list(request):
    units = Unit.objects.all().order_by('-id')  # latest units first (optional)
    return render(request, 'unit_list.html', {'units': units})

# View a single unit detail (optional)
def unit_detail(request, unit_id):
    unit = get_object_or_404(Unit, id=unit_id)
    return render(request, 'unit_detail.html', {'unit': unit})

def cerete_blog_lesson(request):
    return render(request, 'create_blog_post.html', {'form':BlogPostForm()})

def blog_list(request):
    posts = BlogPost.objects.order_by('-publish_date')
    return render(request, 'blog_list.html', {'posts': posts})
