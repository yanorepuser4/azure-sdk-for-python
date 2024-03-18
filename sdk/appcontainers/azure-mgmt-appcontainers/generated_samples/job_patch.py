# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, IO, Union

from azure.identity import DefaultAzureCredential

from azure.mgmt.appcontainers import ContainerAppsAPIClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-appcontainers
# USAGE
    python job_patch.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ContainerAppsAPIClient(
        credential=DefaultAzureCredential(),
        subscription_id="34adfa4f-cedf-4dc0-ba29-b6d1a69ab345",
    )

    response = client.jobs.begin_update(
        resource_group_name="rg",
        job_name="testcontainerAppsJob0",
        job_envelope={
            "properties": {
                "configuration": {
                    "manualTriggerConfig": {"parallelism": 4, "replicaCompletionCount": 1},
                    "replicaRetryLimit": 10,
                    "replicaTimeout": 10,
                    "triggerType": "Manual",
                },
                "template": {
                    "containers": [
                        {
                            "image": "repo/testcontainerAppsJob0:v1",
                            "name": "testcontainerAppsJob0",
                            "probes": [
                                {
                                    "httpGet": {
                                        "httpHeaders": [{"name": "Custom-Header", "value": "Awesome"}],
                                        "path": "/health",
                                        "port": 8080,
                                    },
                                    "initialDelaySeconds": 3,
                                    "periodSeconds": 3,
                                    "type": "Liveness",
                                }
                            ],
                        }
                    ],
                    "initContainers": [
                        {
                            "args": ["-c", "while true; do echo hello; sleep 10;done"],
                            "command": ["/bin/sh"],
                            "image": "repo/testcontainerAppsJob0:v4",
                            "name": "testinitcontainerAppsJob0",
                            "resources": {"cpu": 0.2, "memory": "100Mi"},
                        }
                    ],
                },
            }
        },
    ).result()
    print(response)


# x-ms-original-file: specification/app/resource-manager/Microsoft.App/preview/2023-11-02-preview/examples/Job_Patch.json
if __name__ == "__main__":
    main()
