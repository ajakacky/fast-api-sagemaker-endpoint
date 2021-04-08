#!/bin/bash
docker build -t test .
docker run --it -rm -p 8080:8080 test serve