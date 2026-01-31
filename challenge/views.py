
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.http import HttpResponse

from .models import Performance

from .forms import PerformanceForm

# ログイン必須です
# @login_required
@never_cache
def challengeTopView(request):
    next_url_s = reverse("challenge:challengePerformance")
    next_url_f = reverse("challenge:challengeFailed")
    data = {"timelimit_seconds":3,"next_success":next_url_s,"next_failed":next_url_f}
    return render(request,"challenge/challenge-top.html",{"data":data})

@login_required
@never_cache
def challengePerformance(request):
    data = {"種目":"RADIO","強度":"中"}
    if request.method == "POST" :
        if request.POST.get("action") == "start":
            form = PerformanceForm()
            return render(request,"challenge/challenge-performance.html",{"form":form,"data":data})
        else:
            form = PerformanceForm(request.POST)
            if form.is_valid():
                Performance.objects.create(
                    user=request.user,
                    menu=form.cleaned_data["menu"],
                    level=form.cleaned_data["level"],
                    time=form.cleaned_data["time"],
                    result=form.cleaned_data["result"],
                )
                return redirect("challenge:challengeSuccess")
            else:
                return redirect("challenge:test")
    else:
        return redirect("challenge:test")

def challengeFailedView(request):
    return HttpResponse("間に合わなかった。")

def challengeSuccessView(request):
    return HttpResponse("おめでとう、クリアや。")

def testView(request):
    return HttpResponse("運動スタートや。")

