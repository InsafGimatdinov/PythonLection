import data_provider as dp

import logger as log

def view_temperature(sensor):

    data = dp.get_temperature(sensor)

    log.temperature_logger(data)

    return data

def view_pressure(sensor):

    data = dp.get_pressure(sensor)

    log.pressure_logger(data)

    return data

def view_wind_speed(sensor):
  
    data = dp.get_wind_speed(sensor)
  
    log.wind_speed_logger(data)
  
    return data