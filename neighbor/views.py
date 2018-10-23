from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from .forms import SignUpForm, EditProfileForm, NeighbourhoodForm, BusinessForm, ProfileForm
from .models import Neighbourhood, Business, Profile
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic.edit import UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View
# Create your views here.
def home(request):
    profile = Profile.get_all()
    neighbour=Neighbourhood.objects.filter()
    current_user= request.user
    business =Business.objects.filter(user=request.user.id)

    context = {"neighbour":neighbour,"current_user":current_user,"profile":profile,"business":business}
    return render(request, 'home.html', context )

# Create your views here.
def all(request, neighbourhoud_id):
    neighbour=Neighbourhood.objects.get(pk = neighbourhoud_id)
    current_user= request.user
    business=BusinessForm()
    biz =Business.objects.filter(neighbourhood=neighbourhoud_id)
    context = {"neighbour":neighbour,"current_user":current_user,"profile":profile,"business":business,"biz":biz}
    return render(request, 'all.html', context )



@login_required(login_url='/login')
def new_neighbour(request):
    current_user = request.user
    if request.method == 'POST':
        form = NeighbourhoodForm(request.POST, request.FILES)
        if form.is_valid():
            neighbour = form.save(commit=False)
            neighbour.user = current_user
            neighbour.save()
        return redirect('home')

    else:
        form = NeighbourhoodForm()
    return render(request, 'image.html', {"form": form})


@login_required(login_url='/login')
def new_business(request, pk):
    neighbourhood = get_object_or_404(Neighbourhood,id=pk)
    current_user = request.user
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.user = current_user
            print('x')
            business.neighbourhood = neighbourhood
            business.save()
        return redirect('all', neighbourhoud_id=neighbourhood.id)

    else:
        form = BusinessForm()
    return render(request, 'business.html', {"form": form, "neighbourhood":neighbourhood })



@login_required(login_url='/login')
def profile(request):
    profile =Profile.objects.filter(user=request.user.id)
    neighbour =Neighbourhood.objects.filter(user=request.user.id)
    # commented = CommentForm()
    return render(request, 'profile.html', {"profile": profile, "neighbour": neighbour})



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
#     rates = get_object_or_404(Neighbourhood,pk=review_id)
#     if request.method == 'POST':
#         form = RateForm(request.POST, request.FILES)
#         if form.is_valid():
#             new_rates= form.save(commit=False)
#             new_rates.neighbour = rates
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
    neighbour =Neighbourhood.objects.filter(user=request.user.id)
    # commented = CommentForm()
    return render(request,'dump.html',{"profile": profile, "neighbour": neighbour})

@login_required( login_url='/login' )
def create(request):
    current_user=request.user
    if request.method == 'POST':
        form=ProfileForm( request.POST , request.FILES )
        if form.is_valid( ):
            update=form.save( commit=False )
            update.user=current_user
            update.neighbourhood=current_user
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
   model=Neighbourhood
   template_name = 'edit-neighbour.html'
   fields = ['neighbourhood_name','neighbourhood_location','area']

class ProfileUpdate(UpdateView):
   model= Profile
   template_name = 'edit.html'
   fields = ['contact','bio','picture']


class AlbumDelete(DeleteView):
   model=Neighbourhood
   success_url = reverse_lazy('profile')

class ProfileDelete(DeleteView):
   model=Profile
   success_url = reverse_lazy('profile')



def search(request):

    if 'neighbourhood' in request.GET and request.GET["neighbourhood"]:
        search_term = request.GET.get("neighbourhood")
        searched_neighbor = Neighbourhood.search_by_name(search_term)
        # message=f'{search_term}'
        return render(request, 'search.html',{"neighbour": searched_neighbor})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
