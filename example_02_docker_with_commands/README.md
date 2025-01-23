# Example 02: Dockerfile to build the filebrowser application

Dockerfile to build the Filebrowser application in several steps.

Build it with:

``` docker build . -t filebrowser ```

Then, run it using:

``` docker run -p 8080:8080 filebrowser ```

To check that the service is running, just open a new tab in your browser and navigate to the URL: [localhost:8080](http://localhost:8080)
