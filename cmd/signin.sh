#!/bin/sh

curl -X POST -d 'username=user&password=pass&grant_type=password&client_id=user' http://localhost:8000/oauth2/access_token/
