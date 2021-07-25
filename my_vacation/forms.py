from django import forms

from .models import MinnanoVacation


# バケーションの作成、編集用フォーム
class MinnanoVacationForm(forms.ModelForm):

    class Meta:
        model = MinnanoVacation
        fields = ('title', 'with_who', 'cost', 'time_required', 'published')

# 検索用フォーム
class SearchVacationForm(forms.ModelForm):
    # WITH_LIST = (
    #     ('0', 'ひとりで'),
    #     ('1', '恋人と'),
    #     ('2', '友達と'),
    #     ('3', '家族と'),
    #     ('4', '見知らぬ誰かと'),
    # )

    # TIME_REQUIRED_LIST = (
    #     ('0', '1時間以内'),
    #     ('1', '2~3時間'),
    #     ('2', '半日'),
    #     ('3', '1日'),
    #     ('4', '1泊以上'),
    # )

    # title = forms.CharField(initial="キーワード", label='やりたいこと', max_length=200)
    # with_who = forms.ChoiceField(label='誰と', choices=WITH_LIST)
    # cost = forms.IntegerField(label='およその金額')
    # time_required = forms.ChoiceField(initial="数字のみ入力", label='所要時間', choices=TIME_REQUIRED_LIST)

    class Meta:
        model = MinnanoVacation
        fields = ('title', 'with_who', 'cost', 'time_required')