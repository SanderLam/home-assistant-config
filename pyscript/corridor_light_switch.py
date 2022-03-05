@event_trigger("zha_event", "device_id == '"+pyscript.config.get("global").get("corridor_light_switch_device_id")+"'")
def toggle_corridor_light(**kwargs):
    command = kwargs.get("command")

    if command == "left_press":
        service.call(
            "light","toggle",transition=0.001,
            entity_id="light.corridor_light_level_on_off"
        )