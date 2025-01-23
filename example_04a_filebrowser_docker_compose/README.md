# Example 04a: Docker Compose file to run an application

This Dockerfile runs the filebrowser application uploaded to Barbara registry.

It exposes the port 8080.

## Step 1: Upload the local image created in example 02 to a registry

Tag the local image:

```docker tag filebrowser reg.barbaralabs.com/bbr_test/filebrowser:<yourname>```

Push it to the registry:

```docker push reg.barbaralabs.com/bbr_test/filebrowser:<yourname>```

## Step 2: Run locally the docker compose file

Run it locally using:

``` docker compose up --build ```

## Step 3: Deploy to a node

1. Zip the contents of this folder.
2. Upload the zip file to the Panel's library.
3. Deploy the service in an Edge Node.