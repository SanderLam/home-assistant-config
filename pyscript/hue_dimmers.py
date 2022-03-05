import dimmer

livingroom = dimmer.hue_dimmer(
    device_id = pyscript.config.get("global").get("hue_dimmer_livingroom_device_id"),
    main_light = "light.corridor_light_level_on_off",
    hue_single_press = "light.zha_lights_downstairs",
    hue_double_press = ["pyscript.toggle_hue_dimmer_spotify","media_player.sonos_kitchen"]
)

office_sander = dimmer.hue_dimmer(
    device_id = pyscript.config.get("global").get("hue_dimmer_office_sander_device_id"),
    main_light = "light.zha_office_sander",
    hue_single_press = "light.zha_lights_downstairs"
)

office_amber = dimmer.hue_dimmer(
    device_id = pyscript.config.get("global").get("hue_dimmer_office_amber_device_id"),
    main_light = "light.zha_office_amber",
    hue_single_press = "light.corridor_light_level_on_off"
)

bedroom = dimmer.hue_dimmer(
    device_id = pyscript.config.get("global").get("hue_dimmer_bedroom_device_id"),
    main_light = "light.bedroom_light_level_on_off"
)