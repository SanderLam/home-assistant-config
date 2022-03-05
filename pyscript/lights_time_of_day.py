from homeassistant.const import EVENT_STATE_CHANGED

##### Downstairs #####

# Downstairs Lights On
@state_trigger("(light.zha_lights_downstairs == 'off') and (3 < (float(sensor.living_room_motion_sensor_illuminance) + float(sensor.kitchen_motion_sensor_illuminance))/2 < 6)")
@time_active("range(14:00, 20:00)")
def livingroom_lights_on():
    service.call(
        "light", "turn_on",
        entity_id="light.zha_lights_downstairs",
        brightness=128,
        color_temp=410
    )
    service.call("notify", "mobile_app_iphone_van_sander", message="Lights downstairs are turned on")

# Downstairs Lights Off - Weekdays
@state_trigger("sensor.time == '22:15' and binary_sensor.workday_sensor == 'on'")
def livingroom_lights_off():
    service.call("light", "turn_off", entity_id="light.zha_lights_downstairs")


##### Garden Lights #####
@state_trigger("sun.sun == 'below_horizon'")
def garden_light_on():
    service.call("light", "turn_on", entity_id="light.zha_garden")
    service.call("notify", "mobile_app_iphone_van_sander", message="Garden lights are turned on")

@state_trigger("sun.sun == 'above_horizon'")
def garden_light_off():
    service.call("light","turn_off",entity_id="light.zha_garden")
    service.call("notify", "mobile_app_iphone_van_sander", message="Garden lights are turned off")


##### Wake Up Light #####

# The actual logic
@state_trigger("(str(sensor.time) == str(input_datetime.wakeup_time)[:5]) and input_boolean.wakeup_enabled == 'on'")
def wake_up_light():
    service.call(
        "light", "turn_on",
        entity_id="light.bedroom_light_level_on_off",
        brightness=1
    )
    service.call("notify", "mobile_app_iphone_van_sander", message="Wake up light started")

    task.sleep(0.001)
    service.call(
        "light", "turn_on",
        entity_id="light.bedroom_light_level_on_off",
        brightness=100,
        transition=900
    )

# Turn it off in the weekend
@event_trigger(EVENT_STATE_CHANGED, "entity_id == 'sensor.date_dayoftheweek'")
def wake_up_light_toggle(entity_id=None, new_state=None, old_state=None):
    if new_state.state in ["Monday","Tuesday","Wednesday","Thursday","Friday"]:
        service.call(
            "input_boolean","turn_on",
            entity_id="input_boolean.wakeup_enabled"
        )
    elif new_state.state in ["Saturday","Sunday"]:
        service.call(
            "input_boolean","turn_off",
            entity_id="input_boolean.wakeup_enabled"
        )
