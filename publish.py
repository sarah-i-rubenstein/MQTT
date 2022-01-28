#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
Publish some messages to queue
"""
import paho.mqtt.publish as publish


msgs = [{'topic': "indicators/red1", 'payload': "1"},
        {'topic': "indicators/red2", 'payload': "0"},
        {'topic': "indicators/red3", 'payload': "1"},
        {'topic': "indicators/yellow1", 'payload': "0"},
        {'topic': "indicators/yellow1", 'payload': "1"},
        {'topic': "indicators/yellow1", 'payload': "0"},
        {'topic': "indicators/green1", 'payload': "1"},
        {'topic': "indicators/green2", 'payload': "0"},
        {'topic': "indicators/green3", 'payload': "1"}]

host = "localhost"

numLights = 6 #number of lights to turn on

if __name__ == '__main__':
    # publish a single message
    for x in range(numLights):
        color = "red"
        if x < 2:
            x = x+1
            color = "green"
        elif x < 4:
            x = x-1
            color = "yellow"
        else:
            x = x-3
        publish.single(topic="indicators/"+color+str(x), payload="1", hostname=host)

    # publish multiple messages
    publish.multiple(msgs, hostname=host)


# vi: set fileencoding=utf-8 :