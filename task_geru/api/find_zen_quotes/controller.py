from zen_quotes.quotes import Quotes
from random import randint


class Task():

    def get_quotes(self):
        resp = Quotes().get_quotes()

        return resp

    def get_only_quote(self, quote_number):
        resp = Quotes().get_quotes(quote_number)

        return resp

    def get_random_quote(self):
        list_quotes = Quotes().get_quotes()
        resp = Quotes().get_quotes(randint(0, len(list_quotes['quotes']) - 1))

        return resp