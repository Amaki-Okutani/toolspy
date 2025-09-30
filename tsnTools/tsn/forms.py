from django import forms

class ProductGroupSearchForm(forms.Form):
    productGroupCode = forms.CharField(max_length=3, required=False)
    productGroupName = forms.CharField(max_length=128, required=False)
    productGroupAbbreviation = forms.CharField(max_length=15, required=False)
    domesticAbroadClass = forms.MultipleChoiceField(
        choices=[('0', '海外'), ('1', '国内')],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    sort = forms.ChoiceField(
        choices=[
            ('product_group_code,asc', '商品グループコード 昇順'),
            ('product_group_code,desc', '商品グループコード 降順'),
            ('product_group_name,asc', '商品グループ名称 昇順'),
            ('product_group_name,desc', '商品グループ名称 降順'),
        ],
        required=False
    )
