class SalesInputRequest():
    def __init__(self) -> None:
        pass


class SalesAnalysisRequest:
    def __init__(self,queryset):
        self.queryset=queryset

    def getAnalysis(self):
        total_sales=self.queryset.aggregate(sales=Sum(F('items__quantity')*F('items__item__price')))
        no_of_transactions=self.queryset.count()
        total_quantity_items_sold=self.queryset.aggregate(Sum('items__quantity'))
        total_quantity_items_sold_for_each_item=self.queryset.values('items__item__title').annotate(Sum('items__quantity'))
        total_quantity_items_sold_for_each_item=self.queryset.values('items__item__title').annotate(Sum('items__quantity'))
        total_quantity_sold_in_each_item_category=self.queryset.values('items__item__category__name').annotate(Sum('items__quantity'))
        total_sales_amount_in_each_item_category=self.queryset.values('items__item__category__name').annotate(sales=Sum(F('items__quantity')*F('items__item__price')))
        response=SalesAnalysisResponse(total_sales,total_quantity_items_sold)



class SalesAnalysisResponse:
    def __init__(self,total_sales,no_of_transactions,total_quantity_items_sold,total_quantity_items_sold_for_each_item,total_quantity_sold_in_each_item_category,total_sales_amount_in_each_item_category) -> None:
         self.total_sales=total_sales,
         self.no_of_transactions=no_of_transactions, 
         self.total_quantity_items_sold=total_quantity_items_sold,
         self.total_quantity_items_sold_for_each_item=total_quantity_items_sold_for_each_item, 
         self.total_quantity_sold_in_each_item_category=total_quantity_sold_in_each_item_category, 
         self.total_sales_amount_in_each_item_category=total_sales_amount_in_each_item_category

    # total_sales,no_of_transactions
    # total_quantity_items_sold
    # total_quantity_items_sold_for_each_item
    # total_quantity_sold_in_each_item_category
    # total_sales_amount_in_each_item_category



class SalesAnalysis():
    def __init__(self,total_sales,no_of_transactions,total_quantity_items_sold,total_quantity_items_sold_for_each_item,total_quantity_sold_in_each_item_category,total_sales_amount_in_each_item_category) -> None:
         self.total_sales=total_sales,
         self.no_of_transactions=no_of_transactions, 
         self.total_quantity_items_sold=total_quantity_items_sold,
         self.total_quantity_items_sold_for_each_item=total_quantity_items_sold_for_each_item, 
         self.total_quantity_sold_in_each_item_category=total_quantity_sold_in_each_item_category, 
         self.total_sales_amount_in_each_item_category=total_sales_amount_in_each_item_category

    