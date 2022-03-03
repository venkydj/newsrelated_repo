from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'testapp/index.html')

def moviesinfo(request):
    head_msg='To Get Latest Information.....'
    msg1="PawanKalyan's Bheemlanayak Crossed 100 crores"
    msg2="Radhe Syam released on 11th march"
    msg3="yesterday Radhe syam pre release event cheif guest SS Rajamouli"
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'testapp/movies.html',context=my_dict)
def politicsinfo(request):
    return render(request,'testapp/polytics.html')
def allinfo(request):
    return render(request,'testapp/allinfo.html')
def sportsinforamation(request):
    return render(request,'testapp/sports.html')
