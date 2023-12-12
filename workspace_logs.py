#!/usr/bin/env python3
import os
from datetime import datetime, timedelta, timezone

import pandas as pd
from azure.core.exceptions import HttpResponseError
from azure.identity import DefaultAzureCredential
from azure.monitor.query import LogsQueryClient, LogsQueryStatus


def create_azure_monitor_client():
    credential = DefaultAzureCredential()
    azure_client = LogsQueryClient(credential)
    return azure_client


def query_activity_workspace(client):
    query = "AzureActivity | summarize count()"
    try:
        response = client.query_workspace(
            os.environ["LOGS_WORKSPACE_ID"], query, timespan=timedelta(days=7)
        )
        if response.status == LogsQueryStatus.PARTIAL:
            error = response.partial_error
            data = response.partial_data
            print(error)
        elif response.status == LogsQueryStatus.SUCCESS:
            data = response.tables
        for table in data:
            df = pd.DataFrame(data=table.rows, columns=table.columns)
            key_value = df.to_dict(orient="records")
            print(key_value)
    except HttpResponseError as err:
        print("something fatal happened")
        print(err)


cli = create_azure_monitor_client()
query_activity_workspace(cli)
