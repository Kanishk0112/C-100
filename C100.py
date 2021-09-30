class Car(object):
    def __init__(self,color,model,company,speed,features):
        self.color= color
        self.model=model
        self.company=company
        self.speed=speed
        self.features=features
    def Start(self):
        print("Car has started")
    def Stop(self):
        print("Car has stopped")
merc=Car("red","GLC 400d","Mercedes","300","4matic")
print(merc.Start())    
print(merc.Stop())    
