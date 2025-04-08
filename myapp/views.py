from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import F
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = "myapp/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "myapp/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = "myapp/results.html"




def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "myapp/detail.html", {
            "question": question,
            "error_message": "You didn't select a choice.",
        })
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        selected_choice.refresh_from_db()

    return redirect("polls:results", pk=question.id)











# Create your views here.
# def home(request):
#     return HttpResponse("Hello world. you're at the polls index.")

# ####################################

# # def detail(request, question_id):
# #     try:
# #         question = Question.objects.get(pk=question_id)
# #     except Question.DoesNotExist:
# #         raise Http404("Question does not exist")
# #     return render(request, "myapp/detail.html", {"question": question} )



# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "myapp/detail.html", {"question": question} )



# # def results(request, question_id):
# #     response = "You're looking at the results of question %s."
# #     return HttpResponse(response % question_id)

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "myapp/results.html", {"question": question})



# # def vote(request, question_id):
# #     # return HttpResponse("You're voting on question %s." % question_id)
# #     return HttpResponse(f"You're voting on question {question_id}")

# # def index(request):
# #     latest_question_list = Question.objects.order_by("-pub_date")[:5]
# #     output = ", ".join([q.question_text for q in latest_question_list])
# #     return HttpResponse(output)


# # def index(request):
# #     latest_question_list = Question.objects.order_by("-pub_date")[:5]
# #     template = loader.get_template("myapp/index.html")
# #     context = {
# #         "latest_question_list": latest_question_list,
# #     }
# #     return HttpResponse(template.render(context, request))




# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     context = {
#         "latest_question_list": latest_question_list,
#     }
#     return render(request, "myapp/index.html", context)



# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST["choice"])
#     except (KeyError, Choice.DoesNotExist):
#         return render(request, "myapp/detail.html", {"question": question, "error_message": "You didn't select a choice."})
#     else:
#         selected_choice.votes = F("votes") + 1
#         selected_choice.save()
#     return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]


