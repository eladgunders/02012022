
class TooHigherError(Exception):

    def __init__(self, msg='Value is too high.'):
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return f'{self.msg}'