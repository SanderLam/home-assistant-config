@state_trigger("sensor.gad_morgen != 'Geen' and sensor.time == '20:00'")
def notify_gad_day_before():
    service.call("notify", "notify", message = f"Morgen wordt '{sensor.gad_morgen.title()}' opgehaald!")

@state_trigger("sensor.gad_vandaag != 'Geen' and sensor.time == '08:00'")
def notify_gad_today():
    service.call("notify", "notify", message = f"Vandaag wordt '{sensor.gad_vandaag.title()}' opgehaald!")
