from django.shortcuts import render

# Create your views here.
def main(request):
    absences = models.Absences.objects.all()
    return render(request, "appabs/main.html",{"absences": absences})