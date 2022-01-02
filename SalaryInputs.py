from TooLowerError import TooLowerError
from TooHigherError import TooHigherError


class SalaryInputs:

    @staticmethod
    def get_salary(amount):
        amount = float(amount)
        if amount > 100_000:
            raise TooHigherError
        elif amount < 10_000:
            raise TooLowerError
        else:
            return amount
