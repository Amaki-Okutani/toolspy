from django.shortcuts import render
from .models import TsnTools
from .forms import ProductGroupSearchForm
from .forms import ProductregistForm

from django.db.models import Q

def product_group_list(request):
    # フォームの初期化
    form = ProductGroupSearchForm(request.POST or None)
    qs = TsnTools.objects.all()

    # 関数呼び出しと POST 到達確認用
    print("=== product_group_list called ===")
    print("Request method:", request.method)
    print("Raw POST data:", request.POST)

    if request.method == "POST":
        print("POST received")

        if form.is_valid():
            print("Form is valid!")
            cd = form.cleaned_data
            print("Cleaned data:", cd)

            # フィルタ処理
            if cd.get('productGroupCode'):
                qs = qs.filter(
                    Q(product_group_code__icontains=cd['productGroupCode']) |
                    Q(product_group_code__exact='') |
                    Q(product_group_code__isnull=True)
                )

            if cd.get('productGroupName'):
                qs = qs.filter(product_group_name__icontains=cd['productGroupName'])

            if cd.get('productGroupAbbreviation'):
                qs = qs.filter(
                    Q(product_group_abbreviation__icontains=cd['productGroupAbbreviation']) |
                    Q(product_group_abbreviation__exact='') |
                    Q(product_group_abbreviation__isnull=True)
                )

            if cd.get('domesticAbroadClass'):
                qs = qs.filter(domestic_abroad_class__in=cd['domesticAbroadClass'])

            # ソート
            if cd.get('sort'):
                field, order = cd['sort'].split(',')
                if order == 'desc':
                    field = '-' + field
                qs = qs.order_by(field)

            print("Filtered queryset count:", qs.count())

        else:
            print("Form is invalid!")
            print("Form errors:", form.errors)

    else:
        print("GET request")

    # コンテキスト渡し
    context = {
        'form': form,
        'rows': qs,
    }

    return render(request, 'tsn/ProductGroup/group_list.html', context)

def regist_page(request):
    form = ProductregistForm(request.POST or None)
    context = {
        'form': form,
    }
    return render(request,'tsn/ProductGroup/group_regist.html',context)

def check_page(request):
    form = ProductregistForm(request.POST or None)
    context = {
        'form': form,
    }
    return render(request,'tsn/ProductGroup/group_confirm.html',context)