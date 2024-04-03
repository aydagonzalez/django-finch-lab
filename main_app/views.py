from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Cat
from .forms import FeedingForm
# Add UpdateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# cats = [
#   {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
#   {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
#   {'name': 'Olivia', 'breed': 'Tortie', 'description': 'Runs the house', 'age': 4},
#   {'name': 'Clive', 'breed': 'tabby', 'description': 'Likes petting a bag of bones', 'age': 10},
# ]
# Create your views here.
class CatCreate(CreateView):
  model = Cat
  fields = '__all__'
  # success_url = '/cats/{cat_id}'

class CatUpdate(UpdateView):
  model = Cat
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['breed', 'description', 'age']

class CatDelete(DeleteView):
  model = Cat
  success_url = '/cats'

def add_feeding(request, cat_id):
    # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.cat_id = cat_id
    new_feeding.save()
  return redirect('detail', cat_id=cat_id)

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cats_index(request):
    cats = Cat.objects.all() # Retrieve all cats
    return render(request, 'cats/index.html', 
    { 
        'cats': cats 
    }
)

def cats_detail(request, cat_id):
  cat = Cat.objects.get(id=cat_id)
  feeding_form = FeedingForm()
  return render(request, 'cats/detail.html', { 'cat': cat, 'feeding_form' : feeding_form })