from dataclasses import dataclass
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

async def HAMQTTAutodiscoveryParse(DATA_FILE):
    with open(DATA_FILE) as f:
        data = yaml.load(f, Loader=SafeLoader)
    return data

async def HAMQTTAutodiscoveryPublish(DATA_FILE):
    data = DATA_FILE
    sensor = 0
    HAMQTTAutodiscoveryParse(data)
    for sensor_id in data:
        type = 0
        for sensor_type in data.sensor_id:
            payload = {"device_class": data.sensor_type, "state_topic": data.sensor_id+"/"+data.sensor_type, }
            topic = {"topic": HA_AUTODISCOVERY_PREFIX+"/sensor/"+data.mac_id+"/"+data.sensor_id+"/"+data.sensor_type+"/config", "payload": payload, "qos": 1, "retain": "true" }
            mqtt.publish(topic)
            type +=1
        sensor +=1
