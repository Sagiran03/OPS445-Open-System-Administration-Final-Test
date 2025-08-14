class Distance:
    '''
    Author: David Mayer
    Distance in imperial format
    1 yard == 3 feet
    1 foot == 12 inches
    to convert to metric:
    1 inch == 2.54 centimetres 
    '''

    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def print_height(self):
        print(f'{self.feet} ft {self.inches} in')

    def add_cm(self, cm):
        # Convert cm to inches, round to nearest whole number
        add_inches = round(cm / 2.54)
        self.inches += add_inches
        # Convert excess inches to feet
        if self.inches >= 12:
            self.feet += self.inches // 12
            self.inches = self.inches % 12

    def __str__(self):
        return f"{self.feet} ft {self.inches} in"

# Example usage:
if __name__ == "__main__":
    d2 = Distance(1, 10)
    print(d2)
    d2.add_cm(10)  # adds 4 inches
    print(d2)
