from tires.tires import Tires

class CarriganTires(Tires):
    def __init__(self, sensorScore):
        self.sensorScore = sensorScore

    def needs_service(self):
        for score in self.sensorScore:
            if score >= 0.9:
                return True
            else:
                continue
        return False
        

      
