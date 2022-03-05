@service
def toggle_hue_dimmer_spotify(media_player_id, playlist="2vtP6DyFlbyKD4sMMqI7hy?si=9e2f36ed73214a0c", volume=0.2):
    if media_player_id == "playing":
        log.warning("Hue Dimmer turned the music in the kitchen off")
        service.call("media_player", "media_pause", entity_id=media_player_id)
    else:
        log.warning("Hue Dimmer turned the music in the kitchen on")
        
        service.call(
            "media_player","play_media", 
            entity_id=media_player_id,
            media_content_id="https://open.spotify.com/playlist/"+playlist,
            media_content_type="playlist"
        )
        service.call("media_player", "volume_set", entity_id=media_player_id, volume_level=volume)
        service.call("media_player", "shuffle_set", entity_id=media_player_id, shuffle=True)
