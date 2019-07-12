from profissional.views import Is_prof

def is_prof1(request):
    is_prof1 = Is_prof(request)
    print(is_prof1)
    return{"is_prof1": is_prof1}
