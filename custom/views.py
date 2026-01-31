from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from .models import SetMenu
from .forms import SetMenuForm

def custom_home_view(request):
    SetMenuFormSet = modelformset_factory(SetMenu, form=SetMenuForm, extra=0)
    
    weekdays = [(i, day) for i, day in enumerate(['月', '火', '水', '木', '金', '土', '日'])]

    setmenus = SetMenu.objects.all().order_by('weekday', 'starttime')

    if request.method == "POST":
        formset = SetMenuFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect("custom:custom_home")
    else:
        setmenus = SetMenu.objects.all().order_by('weekday', 'starttime')

        # 保存済みの曜日番号だけ取得（重複除去）
        existing_weekdays = set(SetMenu.objects.values_list('weekday', flat=True).distinct())

        # まだ保存されていない曜日用の空フォーム initial データ作成
        initial_data = []
        for i, day_name in weekdays:
            if i not in existing_weekdays:
                initial_data.append({'weekday': i})

        # フォームセットを初期化
        formset = SetMenuFormSet(queryset=setmenus, initial=initial_data)

    # 表示用にフォームと曜日を組み合わせ
    rows = list(zip(weekdays, formset))

    return render(request, "custom/custom_home.html", {
        "formset": formset,
        "rows": rows,
        "setmenus": setmenus
    })
