#!/bin/bash
pip install -r requirements.txt
cp env-sample .env
echo "ENTER PASSWORD:" && read -s PASSWORD
echo $PASSWORD | sudo pre-commit install
