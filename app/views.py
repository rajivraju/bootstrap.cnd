from django.shortcuts import render


def bootstrap(request):
    return render(request,'bootstrap_cnd.html')