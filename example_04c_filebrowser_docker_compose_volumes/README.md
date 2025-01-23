# Example 04c: Docker Compose file to run an application that uses an internal volume

This Dockerfile runs the filebrowser application uploaded to Barbara registry.

It exposes the port 8080. It also uses the an internal volume to store data in the Edge Node.

## Step 1: Run locally the docker compose file

Run it locally using:

``` docker compose up --build ```

## Step 2: Deploy to a node

1. Zip the contents of this folder.
2. Upload the zip file to the Panel's library.
3. Deploy the service in an Edge Node.