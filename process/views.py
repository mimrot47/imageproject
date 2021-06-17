from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import formUplod
from .models import Uplod

# Create your views here.
def home(Request):
    form=formUplod()
    if Request.method=='POST':
        form=formUplod(Request.POST,Request.FILES)
        if form.is_valid():
            form.save()
            form=formUplod()
            data=Uplod.objects.all().order_by('-id')[:1]
            MY_DICT={'form':form,'list':data}
            return render(Request,'uplods/index.html',MY_DICT)
      
    MY_DICT={'form':form}
    return render(Request,'uplods/index.html',MY_DICT)

