# Example 01b: Hello World Dockerfile using parameters

Simple Dockerfile to build a basic "Hello World" application using parameters.

## Step 1: Parameters defined in buildtime 

Build it with:

``` docker build . -t holamundo ```

Then, run it using:

``` docker run holamundo ```

and you will see the message:

``` holamundo ```

## Step2: Defining parameters in runtime

Now, run it using:

``` docker run -e testvariable=adiosmundo holamundo ```

and you will see the message:

```adiosmundo```