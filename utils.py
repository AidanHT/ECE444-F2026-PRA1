class utils:
    """Utility functions for integer formatting and reversal."""

    @staticmethod
    def _require_int(number):
        if isinstance(number, bool) or not isinstance(number, int):
            raise TypeError("number must be an integer")

    @staticmethod
    def reversed(number):
        """Return the digits of an integer in reverse order."""
        utils._require_int(number)

        sign = -1 if number < 0 else 1
        reversed_number = int(str(abs(number))[::-1])
        return sign * reversed_number

    @staticmethod
    def formatter(number):
        """Return an integer's binary and octal representations."""
        utils._require_int(number)
        return bin(number), oct(number)
