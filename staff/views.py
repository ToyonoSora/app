from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from .forms import EmployeeForm as EmployeeForm


# 一覧ページ用
def staff_list(request):
    # データベースから全ての社員を取ってくる
    staff_members = Employee.objects.all().order_by("-joined_date")
    # テンプレートで使うための「辞書」を作る（contextと呼びます）
    context = {"staff_members": staff_members, "message": "社員一覧です"}
    # render関数：(リクエスト, 使うテンプレート, 渡すデータ)
    return render(request, "staff/list.html", context)


# 詳細ページ用
def staff_detail(request, user_id):
    user = get_object_or_404(Employee, id=user_id)
    return render(request, "staff/detail.html", {"user": user})


# 追加機能
def employee_create(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("staff_list")  # urls.pyで決めた名前を指定
    else:
        form = EmployeeForm()

    return render(request, "staff/employee_form.html", {"form": form})
