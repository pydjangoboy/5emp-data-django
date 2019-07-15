from django.shortcuts import render


# Create your views here.
def ShowEmp(request):
    emp_details = {
        "101": {'name': 'jai',  'salary': 10000, 'designations': 'python developers', 'address': 'sonebhadra3',},
        "102": {'name': 'jai',  'salary': 10000, 'designations': 'data scientists', 'address': 'sonebhadra1',},
        "103": {'name': 'jai',  'salary': 10000, 'designations': 'wep desiginers', 'address': 'sonebhadra2',},
        "104": {'name': 'jai',  'salary': 10000, 'designations': 'data mining engg', 'address': 'sonebhadra4',},
        "105": {'name': 'jai',  'salary': 10000, 'designations': 'soft engg', 'address': 'sonebhadra5',},
        "106": {'name': 'jai',  'salary': 10000, 'designations': 'chemical  scientists', 'address': 'sonebhadra6',}
    }
    return render(request, 'index.html',{'dict':emp_details})
