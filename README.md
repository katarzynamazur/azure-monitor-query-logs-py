# DEVELOPMENT 

#### Create virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

#### Install packages

```
python3 -m pip install azure-monitor-query
python3 -m pip install azure-identity
python3 -m pip install azure-storage-blob
python3 -m pip install pandas
```

#### Export environment variables

```
export AZURE_CLIENT_ID=XXXXXXXXX
export AZURE_TENANT_ID=XXXXXXXXX
export AZURE_CLIENT_SECRET=XXXXXXXXX
export AZURE_SUBSCRIBTION_ID=XXXXXXXXX
export LOGS_WORKSPACE_ID=XXXXXXXXX
export METRICS_RESOURCE_URI=XXXXXXXXX
export LOGS_RESOURCE_ID=XXXXXXXXX
```
