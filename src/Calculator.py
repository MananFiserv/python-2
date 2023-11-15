class Calculator:

    def __init__(self, num_1, num_2):
        self.__num_1 = num_1
        self.__num_2 = num_2
        self.__result = 0

    def add(self):
        self.__result = self.__num_1 + self.__num_2

    def sub(self):
        self.__result = self.__num_1 - self.__num_2

    def mul(self):
        self.__result = self.__num_1 * self.__num_2
    
    def div(self):
        self.__result = self.__num_1 / self.__num_2

    def get_result(self):
        return self.__result