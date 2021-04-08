# Fast-API Sagemaker Endpoint

This example will create a sagemaker endpoint using a custom docker container with Fast-API

## Running Locally

Execute these commands:
```
$ chmod +x serve_local.sh
$ ./serve_local.sh
```

After running serve, this should show within the console:
```
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
```

## Testing Locally

After serving the endpoint locally, you can run a couple tests.

For viewing the swagger api, enter `http://0.0.0.0:8080/docs` into your search bar.

For testing the `/ping` endpoint, enter `curl http://0.0.0.0:8080/ping` into the console.

For testing the `/invocations` endpoint, enter `curl http://0.0.0.0:8080/invocations` into the console.