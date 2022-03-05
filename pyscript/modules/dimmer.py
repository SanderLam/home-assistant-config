def hue_dimmer(device_id, main_light, hue_single_press=None, hue_double_press=None):
    @event_trigger("zha_event",  "device_id == '"+device_id+"'")
    def make_hue_dimmer_great_again(**kwargs):
        command = kwargs.get("command")
        args = kwargs.get("args")

        if command == "on_press":
            service.call(
                "light","toggle",transition=0.001,
                entity_id=main_light,
                brightness=128,
                color_temp=410
            )
            
        elif command == "on_double_press":
            service.call(
                "light","turn_on",transition=0.001,
                entity_id=main_light,
                effect="colorloop"
            )

        elif (command == "step" and args == [0,63,9]) or (command == "step" and args == [0,30,9]):
            service.call(
                "light","turn_on",
                entity_id=main_light,
                brightness_step_pct=25,
                transition=0.2
            )

        elif (command == "step" and args == [1,63,9]) or (command == "step" and args == [1,30,9]):
            service.call(
                "light", "turn_on",
                entity_id=main_light,
                brightness_step_pct=-25,
                transition=0.2
            )

        elif command == "off_press":
            service.call(
                "light", "toggle",
                entity_id=hue_single_press
            )

        elif command == "off_double_press":
            service.call(
                hue_double_press[0].split(".")[0], hue_double_press[0].split(".")[1],
                media_player_id=hue_double_press[1]
            )

    return make_hue_dimmer_great_again
