import lights
from datetime import datetime, timedelta

morning_routine_duration_hours = 2
morning_routine_light_duration = 5

active_until = (
    datetime.strptime(input_datetime.wakeup_time, "%H:%M:%S") + 
    timedelta(hours=morning_routine_duration_hours)
).strftime("%H:%M:%S")

# One-time behavior during morning routine
@state_trigger("binary_sensor.bathroom_motion_sensor_occupancy == 'on' and input_boolean.morning_routine == 'on'")
@time_active("range("+input_datetime.wakeup_time+", "+active_until+")")
def morning_routine_active():
    service.call("notify", "mobile_app_iphone_van_sander", message="Morning routine activated")

    service.call(
        "pyscript", "toggle_hue_dimmer_spotify",
        media_player_id="media_player.sonos_bathroom",
        playlist="37i9dQZF1DX2fMaj5GfMh3?si=ecb65b3cb1734e54",
        volume=0.12
    )

    bathroom = lights.lights_on_motion(
        motion_id = "binary_sensor.bathroom_motion_sensor_occupancy",
        light_id = "light.zha_bathroom_leds",
        no_motion_wait = morning_routine_light_duration
    )

    service.call(
        "input_boolean","turn_off",
        entity_id="input_boolean.morning_routine"
    )


x = (
    input_boolean.morning_routine.last_changed + 
    timedelta(seconds=3600) # UTC to Dutch time
).strftime("%H:%M:%S")
y = (
    input_boolean.morning_routine.last_changed + 
    timedelta(seconds=3600+morning_routine_light_duration)
).strftime("%H:%M:%S")

# Behavior when morning routine not active
@state_trigger("binary_sensor.bathroom_motion_sensor_occupancy == 'on' and input_boolean.morning_routine == 'off'")
@time_active("not range("+x+", "+y+")")
def morning_routine_not_active():
    # service.call("notify", "mobile_app_iphone_van_sander", message="Light on motion outside morning routine activated")
    bathroom = lights.lights_on_motion(
        motion_id = "binary_sensor.bathroom_motion_sensor_occupancy",
        light_id = "light.zha_bathroom_leds",
        no_motion_wait = 120
    )


# Reset input_boolean.morning_routine
@time_trigger("cron(0 0 * * *)")
def reset_morning_routine():
    # service.call("notify", "mobile_app_iphone_van_sander", message="Morning routine boolean reset")
    service.call(
        "input_boolean","turn_on",
        entity_id="input_boolean.morning_routine"
    )