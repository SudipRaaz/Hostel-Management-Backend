from django.contrib import admin
from .models import CategoryList, Expense, Income, Vendors

# Register the CategoryList model
@admin.register(CategoryList)
class CategoryListAdmin(admin.ModelAdmin):
    list_display = ('categoryID', 'category', 'active', 'type')
    search_fields = ('category', 'type')
    list_filter = ('active', 'type')

# Register the Expense model
@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('expenseID', 'expenseTitle', 'expenseAmount', 'date', 'category')
    search_fields = ('expenseTitle', 'category')
    list_filter = ('date', 'category')

# Register the Income model
@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('incomeID', 'incomeCategory', 'amount', 'discount', 'total')
    search_fields = ('incomeCategory',)
    list_filter = ('incomeCategory',)

# Register the Vendors model
@admin.register(Vendors)
class VendorsAdmin(admin.ModelAdmin):
    list_display = ('name', 'contactNumber', 'email', 'address', 'active', 'vendorType')
    search_fields = ('name', 'email', 'vendorType')
    list_filter = ('active', 'vendorType')
