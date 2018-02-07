from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Album
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm


class IndexView(generic.ListView):
    template_name = 'music/index.html'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/details.html'


# responsible for form creation
class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'albumTitle', 'genre', 'albumLogo']


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'albumTitle', 'genre', 'albumLogo']


class AlbumDelete(DeleteView):
    model = Album
    context_object_name = 'album'
    success_url = reverse_lazy('music:index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registeration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        # request passed sucessfully
        if form.is_valid():
            # filterData
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            # saveData
            user.save()
            # authenticate Data
            user = authenticate(username=username, password=password)
            # check if user is authenticated
            if user is not None:
                # check if user is not frozen or banned
                if user.is_active:
                    # login and redirect to a defined Page
                    login(request, user)
                    return redirect('music:index')
        # request Failed        
        return render(request, self.template_name, {'form': form})
