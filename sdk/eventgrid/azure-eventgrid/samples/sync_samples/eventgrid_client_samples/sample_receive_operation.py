# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import os
from azure.core.credentials import AzureKeyCredential
from azure.eventgrid import EventGridClient
from azure.eventgrid.models import *
from azure.core.exceptions import HttpResponseError

EVENTGRID_KEY = os.environ.get("EVENTGRID_KEY")
EVENTGRID_ENDPOINT = os.environ.get("EVENTGRID_ENDPOINT")
TOPIC_NAME = os.environ.get("TOPIC_NAME")
EVENT_SUBSCRIPTION_NAME = os.environ.get("EVENT_SUBSCRIPTION_NAME")

# Create a client
client = EventGridClient(EVENTGRID_ENDPOINT, AzureKeyCredential(EVENTGRID_KEY))


# Receive CloudEvents
try:
    receive_result = client.receive_cloud_events(
        topic_name=TOPIC_NAME,
        event_subscription_name=EVENT_SUBSCRIPTION_NAME,
        max_events=10,
        max_wait_time=10,
    )
    print(receive_result)
except HttpResponseError:
    raise
