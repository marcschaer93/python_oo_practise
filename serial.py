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
    def __init__(self, start, serial_number=None):
        """makes a new generator and starts at the given startpoint. default serial_number is None"""
        self.start = start
        self.serial_number = serial_number

    def __repr__(self):
        return f"This is a Serialgenerator start={self.start} serial-Number={self.serial_number}"
        
    def generate(self):
        """generates a serial_number at a given starting point. If theres already a serial_number, than it increase the serial_number by 1"""
        if self.serial_number == None:
            self.serial_number = self.start 
        else:
            self.serial_number += 1
        return self.serial_number

    def reset(self):
        """resets the serial_number to default None"""
        self.serial_number = None




