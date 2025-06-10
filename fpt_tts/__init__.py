import requests, json, os, time
import logging

# Declare variables
DOMAIN = 'fpt_tts'
SERVICE_FPT_TTS = 'say'

# config
CONF_API_KEY = 'api_key'
CONF_SPEED = 'speed'

# data service setting
CONF_PLAYER_ID = 'entity_id'
CONF_MESSAGE = 'message'
CONF_VOICE_TYPE = 'voice_type'


_LOGGER = logging.getLogger(__name__)
def setup(hass, config):

    _LOGGER.info("The 'fpt_tts' component is ready!")

    def tts_handler(data_call):
        # Get config da setting tai file cofig.yaml
        openfpt_api = str(config[DOMAIN][CONF_API_KEY])
        speed_read = str(config[DOMAIN][CONF_SPEED])
        
        # Get data service setting khi goi service nay
        media_id = data_call.data.get(CONF_PLAYER_ID)
        voice_type = data_call.data.get(CONF_VOICE_TYPE)
        text_message = str(data_call.data.get(CONF_MESSAGE)[0:5000])

        # List voice of FPT Speech Synthesis
        voice_list = {'nam_mien_bac': 'leminh', 'nu_mien_bac': 'banmai', 'nu_mien_nam': 'lannhi', 'nu_mien_trung': 'myan'}
        voice_type = voice_list.get(voice_type)    

        url = 'https://api.fpt.ai/hmi/tts/v5'
        # Header Parameters
        header_parameters = {'api_key': openfpt_api, 'speed': speed_read, 'voice': voice_type}
        text_message = text_message.encode('utf-8')

        # Get url of audio file    
        url_mp3 = requests.post(url, data = text_message, headers = header_parameters).json()['async']
        time.sleep(2)

        # service data for 'CALL SERVICE' in Home Assistant
        service_data = {'entity_id': media_id, 'media_content_id': url_mp3, 'media_content_type': 'audio/mp4'}
        # Call service from Home Assistant
        hass.services.call('media_player', 'play_media', service_data)

    # Dang ki service vao HA
    hass.services.register(DOMAIN, SERVICE_FPT_TTS, tts_handler)
    _LOGGER.info("The 'fpt_tts' component is stop OK!")
    return True
