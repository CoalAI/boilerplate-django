python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pre-commit install
cp env-sample .env
