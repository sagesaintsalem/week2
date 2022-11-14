class Car:
    def __init__(self, colour, model, engine, gearBox):
        self.colour = colour
        self.model = model
        self.engine = engine
        self.gearBox = gearBox

    def breakdown(self):
        return 'Danger! Car breaking down!'