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
    def __init__(self, start=0):
        self.num = start
        self.num_of_times_gen = 0

    def generate(self):
        """ a funtion that will return the number generated and adds one to the next"""
        number = self.num + self.num_of_times_gen
        self.num_of_times_gen += 1
        return number
        
    def reset(self):
        """resets the number so its back to original"""
        self.num_of_times_gen = 0
    
    def __repr__(self):
        return f'<SerialGenerator Start={self.num} Current={self.num + self.num_of_times_gen - 1} next={self.num + self.num_of_times_gen}>'
