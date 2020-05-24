class CustomException(Exception):
    pass
    

class Basic_Calculator:
    def __init__(self, num1=None, num2=None):
        self._num1 = num1
        self._num2 = num2
    
    def __str__(self):
        return """
        This class behaves like a calculator in some manners.
        """
    def add(self):
        """
        returns: sum of two number
        """
        return self._num1 + self._num2

    @property
    def divide(self):
        """
        returns: divides a/b
        """
        if self._num2 == 0:
            raise ZeroDivisionError
        else:
            return self._num1 / self._num2