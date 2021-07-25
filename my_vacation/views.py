from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, TemplateView
from django.views.generic.edit import ModelFormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from .models import MinnanoVacation
from .forms import MinnanoVacationForm, SearchVacationForm

class VacationList(ListView):
    model = MinnanoVacation
    template_name = 'my_vacation/index.html'
    context_object_name = 'vacations'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = MinnanoVacation.objects.order_by('-created_at')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchVacationForm()
        return context

    def post(self, request, *args, **kwargs):
        yaritai_id = self.request.POST.get('yaritai')
        vacation = MinnanoVacation.objects.get(id=yaritai_id)
        vacation.yaritai += 1
        vacation.save()
        return redirect('/')


class SearchVacation(ListView):
    model = MinnanoVacation
    template_name = 'my_vacation/result_vacation.html'
    context_object_name = 'vacations'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchVacationForm()
        context['search_words'] = self.search_words
        return context

    def get_queryset(self):
        title = self.request.GET.get('title')
        with_who = self.request.GET.get('with_who')
        cost = self.request.GET.get('cost')
        time_required = self.request.GET.get('time_required')

        query = Q()
        self.search_words = []

        if title:
            query &= Q(title__icontains=title)
            self.search_words.append(title)

        if with_who:
            query &= Q(with_who__icontains=with_who)
            if with_who == '0':
                self.search_words.append('ひとりで')
            elif with_who == '1':
                self.search_words.append('恋人と')
            elif with_who == '2':
                self.search_words.append('友達と')
            elif with_who == '3':
                self.search_words.append('家族と')
            elif with_who == '4':
                self.search_words.append('見知らぬ誰かと')

        if cost:
            query &= Q(cost__lte=cost)
            self.search_words.append

        if time_required:
            query &= Q(time_required__icontains=time_required)
            if time_required == '0':
                self.search_words.append('1時間')
            elif time_required == '1':
                self.search_words.append('2~3時間')
            elif time_required == '2':
                self.search_words.append('半日')
            elif time_required == '3':
                self.search_words.append('1日')
            elif time_required == '4':
                self.search_words.append('1泊以上')

        queryset = MinnanoVacation.objects.filter(query).order_by('-created_at')
        
        return queryset


class MyVacation(LoginRequiredMixin, ListView):
    model = MinnanoVacation
    context_object_name = 'my_vacations'
    template_name = 'my_vacation/my-vacation.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchVacationForm()
        return context

    def get_queryset(self):
        user = MinnanoVacation.objects.filter(user__id=self.kwargs['pk']).order_by('-created_at')
        queryset = user
        return queryset


class SearchMyVacation(LoginRequiredMixin, ListView):
    model = MinnanoVacation
    template_name = 'my_vacation/result_my_vacation.html'
    context_object_name = 'vacations'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchVacationForm()
        context['search_words'] = self.search_words
        return context

    def get_queryset(self):
        title = self.request.GET.get('title')
        with_who = self.request.GET.get('with_who')
        cost = self.request.GET.get('cost')
        time_required = self.request.GET.get('time_required')

        query = Q()
        self.search_words = []

        if title:
            query &= Q(title__icontains=title)
            self.search_words.append(title)

        if with_who:
            query &= Q(with_who__icontains=with_who)
            if with_who == '0':
                self.search_words.append('ひとりで')
            elif with_who == '1':
                self.search_words.append('恋人と')
            elif with_who == '2':
                self.search_words.append('友達と')
            elif with_who == '3':
                self.search_words.append('家族と')
            elif with_who == '4':
                self.search_words.append('見知らぬ誰かと')

        if cost:
            query &= Q(cost__lte=cost)
            self.search_words.append

        if time_required:
            query &= Q(time_required__icontains=time_required)
            if time_required == '0':
                self.search_words.append('1時間')
            elif time_required == '1':
                self.search_words.append('2~3時間')
            elif time_required == '2':
                self.search_words.append('半日')
            elif time_required == '3':
                self.search_words.append('1日')
            elif time_required == '4':
                self.search_words.append('1泊以上')

        queryset = MinnanoVacation.objects.filter(query).order_by('-created_at')
        
        return queryset


class VacationDetail(DetailView):
    template_name = 'my_vacation/detail.html'
    model = MinnanoVacation
    context_object_name = 'vacation'

    def post(self, request, *args, **kwargs):
        yaritai_id = self.request.POST.get('yaritai')
        vacation = MinnanoVacation.objects.get(id=yaritai_id)
        vacation.yaritai += 1
        vacation.save()
        return reverse('my_vacation:detail')



class EditVacation(LoginRequiredMixin, UpdateView):
    template_name = 'my_vacation/edit.html'
    model = MinnanoVacation
    form_class = MinnanoVacationForm
    success_url = reverse_lazy('my_vacation:index')


class CreateVacation(CreateView):
    template_name = 'my_vacation/create.html'
    model = MinnanoVacation
    form_class = MinnanoVacationForm
    success_url = reverse_lazy('my_vacation:index')

    def form_valid(self, form):
        if not self.request.user.is_anonymous:
            form.instance.user = self.request.user
        return super().form_valid(form)


class DeleteVacation(LoginRequiredMixin, DeleteView):
    template_name = 'my_vacation/delete.html'
    model = MinnanoVacation
    success_url = reverse_lazy('my_vacation:index')
    context_object_name = 'vacation'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user != self.request.user:
            return redirect('my_vacation:nonauthority_delete')
        return super().post(request, *args, **kwargs)


class NonAuthorityDeleteVacation(TemplateView):
    template_name = 'my_vacation/nonauthority_delete.html'


class DuplicateVacation(LoginRequiredMixin, ListView):
    template_name = 'my_vacation/my-vacation.html'
    model = MinnanoVacation
    context_object_name = 'vacation'

    def post(self, request, *args, **kwargs):
        vacation_id = self.request.POST.get('copied')
        vacation = MinnanoVacation.objects.get(id=vacation_id)
        vacation.copied += 1
        vacation.save()
        vacation.pk = None
        vacation.original_id = vacation_id
        vacation.user = self.request.user
        vacation.yaritai = 0
        vacation.copied = 0
        vacation.save()
        return HttpResponseRedirect(reverse('my_vacation:my_vacation', kwargs={'pk':vacation.user.id}))

    
    def get_queryset(self):
        queryset = super(DuplicateVacation, self).get_queryset()
        return queryset