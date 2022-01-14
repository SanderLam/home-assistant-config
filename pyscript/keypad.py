# Disarming

@state_trigger("alarm_control_panel.front_door_keypad == 'disarmed'")
def align_alarm_on_disarm():
    service.call(
        "alarm_control_panel", "alarm_disarm", 
        entity_id="alarm_control_panel.home_alarm", 
        code=pyscript.config.get("global").get("alarm_control_panel_code")
    )

@state_trigger("alarm_control_panel.home_alarm == 'disarmed'")
def align_keypad_on_disarm():
    service.call(
        "alarm_control_panel", "alarm_disarm", 
        entity_id="alarm_control_panel.front_door_keypad", 
        code=pyscript.config.get("global").get("alarm_control_panel_code")
    )

# Armed Home

@state_trigger("alarm_control_panel.front_door_keypad == 'armed_home' or alarm_control_panel.front_door_keypad == 'armed_night'")
def align_alarm_on_armed_home():
    service.call(
        "alarm_control_panel", "alarm_arm_home", 
        entity_id="alarm_control_panel.home_alarm", 
        code=pyscript.config.get("global").get("alarm_control_panel_code")
    )

@state_trigger("alarm_control_panel.home_alarm == 'armed_home'")
def align_keypad_on_armed_home():
    service.call(
        "alarm_control_panel", "alarm_arm_home", 
        entity_id="alarm_control_panel.front_door_keypad", 
        code=pyscript.config.get("global").get("alarm_control_panel_code")
    )

# Armed Away

@state_trigger("alarm_control_panel.front_door_keypad == 'armed_away'")
def align_alarm_on_armed_away():
    service.call(
        "alarm_control_panel", "alarm_arm_away", 
        entity_id="alarm_control_panel.home_alarm", 
        code=pyscript.config.get("global").get("alarm_control_panel_code")
    )

@state_trigger("alarm_control_panel.home_alarm == 'armed_away'")
def align_keypad_on_armed_away():
    service.call(
        "alarm_control_panel", "alarm_arm_away", 
        entity_id="alarm_control_panel.front_door_keypad", 
        code=pyscript.config.get("global").get("alarm_control_panel_code")
    )
