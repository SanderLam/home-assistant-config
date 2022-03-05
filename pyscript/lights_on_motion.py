import lights

toilet = lights.lights_on_motion(
    motion_id = "binary_sensor.toilet_motion_sensor_occupancy",
    light_id = "light.toilet_led_level_light_color_on_off"
)