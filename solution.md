# SSL-certificate-expiration-API

Repo is an automated pipeline to personal AWS account where any active website can be entered in HTTP params. Returns SSL certificate expiration date of given site in body.

## Features
- Serverless function that checks SSL certificate expiration
- Infrastructure as Code representing deployment to AWS Lambda with an AWS API gateway

## Example
[google.com SSL expiration](https://4odn1tb6ef.execute-api.us-east-1.amazonaws.com/Prod/site?siteId=www.google.com)

[example.com SSL expiration](https://4odn1tb6ef.execute-api.us-east-1.amazonaws.com/Prod/site?siteId=www.example.com)

### Custom Site
To enter in custom site, go to links above and change the `siteId` in the HTTP address.

For example, if I wanted to check youtube.com 

#### original:

[https://4odn1tb6ef.execute-api.us-east-1.amazonaws.com/Prod/site?siteId=ENTER_SITE_NAME](https://4odn1tb6ef.execute-api.us-east-1.amazonaws.com/Prod/site?siteId=ENTER_SITE_NAME)

#### custom:

[https://4odn1tb6ef.execute-api.us-east-1.amazonaws.com/Prod/site?siteId=www.youtube.com](https://4odn1tb6ef.execute-api.us-east-1.amazonaws.com/Prod/site?siteId=www.youtube.com)

## Pipeline
- Pipeline was created using Github Actions and can be viewed in the github actions tab
- There, you can see the pipeline breakdown and its steps
- Every time there is a push/merge to the main branch, a new pipeline is created that deploys the app to personal AWS account

 

## Local Testing
Local testing can speed up any future changes



### Installation

First clone repo and download [Docker](https://www.docker.com/products/docker-desktop/) and keep launched

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install aws, sam, pyopenssl

```bash
pip install aws
```
```bash
pip install sam
```
```bash
pip install pyopenssl
```
next, build local and launch
```bash
sam build
```
```bash
sam local start-api
```
This will deploy the app in a local address that can be viewed on any browser


## Contributing
For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

In the future, it would be nice to slim down app.py
