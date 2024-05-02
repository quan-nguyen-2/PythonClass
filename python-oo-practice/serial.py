"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """
        Initialize the SerialGenerator with a starting value.

        Parameters:
        start (int): The starting value for the serial numbers.
        """
        self.start = start
        self.next_serial = start

    def generate(self):
        """
        Generate the next serial number.

        Returns:
        int: The generated serial number.
        """
        serial = self.next_serial
        self.next_serial += 1
        return serial

    def reset(self):
        """Reset the serial number back to its initial value."""
        self.next_serial = self.start