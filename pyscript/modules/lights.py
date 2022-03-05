def lights_on_motion(motion_id, light_id, no_motion_wait=120):
    @state_trigger(motion_id+" == 'on'")
    @task_unique("restart_lights_motion")
    def on_motion_logic():
        service.call(
            "light","turn_on",transition=0.001,
            entity_id=light_id
        )

        task.wait_until(state_trigger=motion_id+" == 'off'")

        task.sleep(no_motion_wait)

        service.call(
            "light","turn_off",transition=0.001,
            entity_id=light_id
        )

        return on_motion_logic
