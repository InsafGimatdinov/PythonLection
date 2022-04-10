from random import randint

def get_temperature(sensor):
    
    if sensor:
        
        return randint(-20, 0)
    
    else:
        
        return randint(0, 20)

def get_pressure(sensor):
    
    if sensor:
        
        return randint(720, 750)
    
    else:
        
        return randint(750, 770)

def get_wind_speed(sensor):
    
    if sensor:
        
        return randint(0, 20)
    
    else:
        
        return randint(20, 40)
    
def data_collection(sensor = 1):
    return (get_temperature(sensor), get_pressure(sensor), get_wind_speed(sensor))