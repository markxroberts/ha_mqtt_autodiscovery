from dataclasses import dataclass
from html import entities
import yaml
import logging
import asyncio
import socket
from homeassistant.components import mqtt
from typing import Optional
from yaml.loader import SafeLoader
import aiohttp
import async_timeout
from .const import (
    DATA_FILE,
    HA_AUTODISCOVERY_PREFIX,
)
_LOGGER: logging.Logger = logging.getLogger(__package__)

class HAMQTTAutodiscovery:

    def __init__(self):

        self.data = DATA_FILE
        self.haprefix = HA_AUTODISCOVERY_PREFIX
        self.entitylist = []
        self.fileObj = []

    async def HAMQTTAutodiscoveryParse(self):
        try:
            self.fileObj = open(self.data, "r") #opens the file in read mode
            self.entitylist = self.fileObj.read().splitlines() #puts the file into an array
            self.fileObj.close()
        except:
            _LOGGER.info("File "+self.data+" cannot be read")
        return self.entitylist

    async def HAMQTTAutodiscoveryPublish(self):
        try:        
            HAMQTTAutodiscoveryParse(self.data)
            for id in self.entitylist.items():
                sensor_prefix = id
                for nested_value in id.items():
                    payload = {"device_class": nested_value.device_class, "state_topic": sensor_prefix+"/"+nested_value, }
                    topic = {"topic": self.haprefix+"/sensor/"+nested_value.mac_id+"/"+sensor_prefix+"/"+nested_value+"/config", "payload": payload, "qos": 1, "retain": "true" }
                    mqtt.publish(topic)
        except:
            _LOGGER.info("File "+self.data+" cannot be published to MQTT")
            
