from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from .forms import SignUpForm, EditProfileForm, ProjectForm, ProfileForm
from .models import Project, Profile
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic.edit import UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View
# Create your views here.
def home(request):
    profile = Profile.get_all()
    project=Project.objects.filter()
    current_user= request.user
    # commented = CommentForm()
    # rates = Review.get_all()
    context = {"project":project,"current_user":current_user,"profile":profile}
    return render(request, 'home.html', context )


@login_required(login_url='/login')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect('home')

    else:
        form = ProjectForm()
    return render(request, 'image.html', {"form": form})


@login_required(login_url='/login')
def comment(request,id):
    upload = Project.objects.get(id=id)
    if request.method == 'POST':
        comm=CommentForm(request.POST)
        if comm.is_valid():
            comment=comm.save(commit=False)
            comment.user = request.user
            comment.project=upload
            comment.save()
            return redirect('home')
    return redirect('home')



@login_required(login_url='/login')
def profile(request):
    profile =Profile.objects.filter(user=request.user.id)
    project =Project.objects.filter(user=request.user.id)
    # commented = CommentForm()
    return render(request, 'profile.html', {"profile": profile, "project": project})



def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = EditProfileForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ('You have editted your profile' ))
            return redirect('profile')

    else:
        form = EditProfileForm(instance=request.user)
    context = {'form': form }
    return render(request, 'edit_profile.html',context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You have been logged in' ))
            return redirect('home')
        else:
            messages.success(request, ('error logging in - please try again' ))
            return redirect('login')
    else:
        return render(request, 'login.html', {} )

def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out' ))
    return redirect('home')



# def rates(request,review_id):
#     current_user = request.user
#     rates = get_object_or_404(Project,pk=review_id)
#     if request.method == 'POST':
#         form = RateForm(request.POST, request.FILES)
#         if form.is_valid():
#             new_rates= form.save(commit=False)
#             new_rates.project = rates
#             new_rates.user = current_user
#             new_rates.save()
#         return redirect('home')
#     return render(request, 'home.html',{"rates":rates})


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ('You have been registered' ))
            return redirect('home')

    else:
        form = SignUpForm()
    context = {'form': form }
    return render(request, 'register.html',context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, ('You have password has been changed' ))
            return redirect('home')

    else:
        form = PasswordChangeForm(user=request.user)
    context = {'form': form }
    return render(request, 'change_password.html',context)

@login_required(login_url='/login')
def dump(request,pk):
    profile =Profile.objects.filter(user=request.user.id)
    project =Project.objects.filter(user=request.user.id)
    # commented = CommentForm()
    return render(request,'dump.html',{"profile": profile, "project": project})

@login_required( login_url='/login' )
def create(request):
    current_user=request.user
    if request.method == 'POST':
        form=ProfileForm( request.POST , request.FILES )
        if form.is_valid( ):
            update=form.save( commit=False )
            update.user=current_user
            update.save( )
            return redirect( 'profile' )
    else:
        form=ProfileForm( )
    return render( request , 'create.html' , {"form": form} )



@login_required( login_url='/login' )
def edit(request):
    current_user=request.user
    if request.method == 'POST':
        form=ProfileForm( request.POST , request.FILES )
        if form.is_valid( ):
            update=form.save( commit=False )
            update.user=current_user
            update.save( )
            return redirect( 'profile' )
    else:
        form=ProfileForm( )
    return render( request , 'edit.html' , {"form": form} )



class AlbumUpdate(UpdateView):
   model=Project
   template_name = 'edit-project.html'
   fields = ['title','landing_page','description', 'link']

class ProfileUpdate(UpdateView):
   model= Profile
   template_name = 'edit.html'
   fields = ['contact','bio','picture']


class AlbumDelete(DeleteView):
   model=Project
   success_url = reverse_lazy('profile')

class ProfileDelete(DeleteView):
   model=Profile
   success_url = reverse_lazy('profile')



def search(request):

    if 'title' in request.GET and request.GET["title"]:
        search_term = request.GET.get("title")
        searched_title = Project.objects.filter(title=search_term)
        # message = f"{search_title}"
        return render(request, 'search.html',{"title": searched_title})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
