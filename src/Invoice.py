class Invoice:
    def __init__(self, invoice_id, user_id, amount, paid):
        self.__invoice_id = invoice_id
        self.__user_id = user_id
        self.amount = amount
        self.paid = paid

    def __repr__(self):
          return f'invoice_id: {self.__invoice_id} user_id: {self.__user_id} amount:{self.amount} paid:{self.paid}'

    