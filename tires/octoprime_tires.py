from tires.tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, sensorScore):
        self.sensorScore = sensorScore

    def needs_service(self):
        scoreSum=0
        for score in self.sensorScore:
            scoreSum += score
        if scoreSum >= 3:
            return True

      
