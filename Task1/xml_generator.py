from user_interface import view_pressure, view_temperature, view_wind_speed

def create(device = 1):
    
    xml = '<xml>\n'
    
    xml += '    <temperature units = "c">{}</temperature>\n'.format(view_temperature(device))
    
    xml += '    <pressure units = "mmHg">{}</pressure>\n'.format(view_pressure(device))
    
    xml += '    <wind_speed units = "m/s">{}</wind_speed>\n'.format(view_wind_speed(device))
    
    xml += '</xml>'

    with open('data.xml', 'w') as page:
    
        page.write(xml)

    return xml

def new_create(data, device = 1):
    
    t, p, w = data
    
    t = t * 1.8 + 32
    
    xml = '<xml>\n'
    
    xml += '    <temperature units = "f">{}</temperature>\n'.format(t)
    
    xml += '    <pressure units = "mmHg">{}</pressure>\n'.format(p)
    
    xml += '    <wind_speed units = "m/s">{}</wind_speed>\n'.format(w)
    
    xml += '</xml>'

    with open('new_data.xml', 'w') as page:
    
        page.write(xml)

    return data