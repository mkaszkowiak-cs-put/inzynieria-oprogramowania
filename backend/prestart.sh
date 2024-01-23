#!/bin/bash

# This file is executed after each docker-compose up

# Install requirements in case they changed
pip install -r requirements-dev.txt
pip install -r requirements.txt