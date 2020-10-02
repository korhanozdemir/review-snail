from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
import random
list=["a","b","c","d","e","f","g","h","j"]
def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        data=request.POST.copy()
        name=data.get('ad')
        comp=data.get('comp')
        email=data.get('emails')
        amazon=data.get('amazon')
        print(name)
        Path_of_main = os.path.realpath(__file__)
        Path_of_database = Path_of_main.replace(r"beta/views.py", r"media/" +  comp)
        try:
            os.makedirs(Path_of_database)
        except FileExistsError:
            Path_of_database= Path_of_database+str(random.random())
            os.makedirs(Path_of_database)
        fs = FileSystemStorage(location=Path_of_database)
        print("Path: "+Path_of_database)
        data = open(Path_of_database + r"/" + "data.txt","w+")
        data.write("name: "+ name + "\n" + "company name: " + comp +"\n" + "emails: " + email+"\n" + "amazon: "+ amazon )
        data.close()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'index.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'beta.html')

def index(request):
    return render(request, 'index.html')
