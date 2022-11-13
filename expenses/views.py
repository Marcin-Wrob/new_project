from django.views.generic.list import ListView
# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
# from django.urls import reverse
# from django.views import View
# from django.db.models import Q

from .forms import ExpenseSearchForm
from .models import Expense, Category
from .reports import summary_per_category, total_amount_spent
from .reports import total_expense_per_month

from .filters import ExpenseFilter


class ExpenseListView(ListView):
    model = Expense
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = object_list if object_list is not None else self.object_list

        form = ExpenseSearchForm(self.request.GET)
        if form.is_valid():
            name = form.cleaned_data.get('name', '').strip()
            if name:
                queryset = queryset.filter(name__icontains=name)

        # search by category
            category = form.cleaned_data['category']
            if category:
                queryset = queryset.filter(category=category)

        # search by amount
            amount = form.cleaned_data['amount']
            if amount:
                queryset = queryset.filter(amount=amount)

        # filtering by date
            date = form.cleaned_data['date']
            if date:
                queryset = queryset.filter(date=date)

        # filtering by date
            date = form.cleaned_data['date']
            if date:
                queryset = queryset.filter(date__range=(date, date))

        # grouping by values
            grouping = form.cleaned_data.get('name', '').strip()
            if grouping:
                queryset = queryset.order_by('category', '-date').values()

        return super().get_context_data(
            form=form,
            object_list=queryset,
            summary_per_category=summary_per_category(queryset),
            total_amount_spent=total_amount_spent(queryset),
            total_expense_per_month=total_expense_per_month(queryset),
            **kwargs)


class CategoryListView(ListView):
    model = Category
    paginate_by = 5