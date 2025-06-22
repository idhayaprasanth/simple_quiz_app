from django.shortcuts import render , redirect ,get_object_or_404
from .forms import questionform
from .models import questions , category

# Create your views here.
def index(request):
    obj = category.objects.all()
    return render(request, 'index.html' ,{'obj': obj})

def create(request):
    if request.method == "POST":
        form =questionform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = questionform()
    return render(request,'create.html',{'form': form})

def quiz(request , id):
    obj = get_object_or_404(category, id=id)
    question = questions.objects.filter(category=obj)

    if request.method == "POST":
        score = 0
        for q in question:
            user_ans = request.POST.get(str(q.id))  
            correct_ans = getattr(q, f"option{ord(q.answer) - 96}") 
            if user_ans and user_ans.strip().lower() == correct_ans.strip().lower():
                score += 1
        return render(request, 'result.html', {'score': score, 'total': question.count()})

    return render(request, 'quiz.html', {'questions': question})

