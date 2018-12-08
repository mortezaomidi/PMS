from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView
from django.views.generic.edit import FormView
from . models import Property
from .forms import PropertyForm

try:
    from django.core.urlresolvers import reverse_lazy
except ImportError:
    from django.core.urlresolvers import reverse
    from django.utils.functional import lazy
    reverse_lazy = lambda *args, **kwargs: lazy(reverse, str)(*args, **kwargs)



class PropertyListView(ListView):

    template_name = 'property/property-list.html'
    context_object_name = 'properties'
    model = Property
    paginate_by = 13


class PropertyDetailView(DetailView):

    template_name = 'property/property-detail.html'
    model = Property


class NewPropertyView(CreateView):
    model = Property
    form_class = PropertyForm
    success_url = reverse_lazy('property-list')
    template_name = 'new-property.html'


class PropertyFormView(FormView):
    template_name = 'property-edit-form.html'
    form_class = PropertyForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        print('form valid ast')
        return super(PropertyFormView, self).form_valid(form)

def home(request):
    return render(request, 'property/home.html')
