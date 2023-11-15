class TaxMan:

    def __init__(self, items, sales_Tax):
        self.__items = items
        self.__sales_Tax = sales_Tax
        self.__total = 0

    def calc_total(self):
        for  p in self.__items:
            self.__total += p['price'] 
        
        tax = (int(self.__sales_Tax[0:2]))/100
        self.__total*=(1+tax)

    def get_total(self):
        return self.__total