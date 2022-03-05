@state_trigger("float(sensor.ble_moisture_plant_elephant) < 15 and sensor.time == '12:00'")
def align_alarm_on_disarm():
    service.call(
        "notify", "notify", 
        message="Dumbo heeft dorst! Waterniveau is op: "+sensor.ble_moisture_plant_elephant
    )


@state_trigger("float(sensor.ble_moisture_plant_palm) < 15 and sensor.time == '12:00'")
def align_alarm_on_disarm():
    service.call(
        "notify", "notify", 
        message="Coconut heeft dorst! Waterniveau is op: "+sensor.ble_moisture_plant_palm
    )