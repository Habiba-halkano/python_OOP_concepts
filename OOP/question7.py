#composition
class Engine:
    def __init__(self):
        self.running = False

    def start(self):
        if not self.running:
            self.running = True
            print("Engine started")
        else:
            print("Engine already running")

    def stop(self):
        if self.running:
            self.running = False
            print("Engine stopped")
        else:
            print("Engine is already stopped")

class Car:
    def __init__(self):
        #composition :car has an instance of engine
        self.engine = Engine()

    def start_engine(self):
            self.engine.start()

    def stop_engine(self):
            self.engine.stop()


my_car = Car()
my_car.start_engine()
my_car.start_engine()
my_car.stop_engine()
my_car.stop_engine()
