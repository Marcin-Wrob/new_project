from collections import OrderedDict

from django.db.models import Sum, Value, Count
from django.db.models.functions import Coalesce, TruncMonth


def summary_per_category(queryset):
    return OrderedDict(sorted(
        queryset
        .annotate(category_name=Coalesce('category__name', Value('-')))
        .order_by()
        .values('category_name')        .annotate(s=Sum('amount'))
        .values_list('category_name', 's')
    ))


# pt 4
def total_amount_spent(queryset):
    total_spent = queryset.aggregate(Sum("amount"))['amount__sum']
    return total_spent


# pt 5
def total_expense_per_month(queryset):
    total_per_month = queryset.values(month=TruncMonth('date')).annotate(Sum('amount')).order_by()
    return total_per_month

"""

pt. 5 for tests
total_per_month = queryset.values(month=TruncMonth('date')).annotate(Sum('amount')).order_by()
for list_expenses in total_per_month:
    for month_expense in list_expenses.values():
        return month_expense # months & amounts of total expenses
"""

# pt 7
def num_expense_per_month(queryset):
    num_expense_category = queryset.values('category').annotate(Count('name'))
    for num_expense_month in num_expense_category.items():
        return num_expense_month

"""
pt. 7 for tests
num_expense_category = queryset.values('category').annotate(Count('name'))
for num_expense_month in num_expense_category:
    for month_expense in num_expense_month.values():
        return month_expense # no of category & number of expenses per category
"""
