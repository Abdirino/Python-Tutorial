class Car: 
    def __init__(self, color: str, horsepower: int) -> None:
        self.color = color
        self.horsepower = horsepower

bmw: Car = Car("BMW", 540)
