#!/bin/sh


curl -X PUT -H 'Content-Type: application/json' -H 'Authorization: bearer f5d9379e2243d9f145c9b725fe43aea6c0177e4d' -d '{"description":"First ToDo Changed","done":"True"}' http://localhost:8000/todo/1 
