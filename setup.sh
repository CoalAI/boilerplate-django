#!/bin/bash
pip install -r requirements.txt
cp env-sample .env
pre-commit install
pre-commit install --hook-type commit-msg
