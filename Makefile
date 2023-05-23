VENV = .venv
PYTHON = $(VENV)/Scripts/python
PIP = $(VENV)/Scripts/pip3
UVICORN = $(VENV)/Scripts/uvicorn
PYTEST = $(VENV)/Scripts/pytest

include .env
export

# Need to use python 3.9 for aws lambda
$(VENV)/Scripts/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

emb: $(VENV)/Scripts/activate
	$(PYTHON) emb.py
	
crawl: $(VENV)/Scripts/activate
	$(PYTHON) crawl_index.py

esgpt: $(VENV)/Scripts/activate
	$(PYTHON) es_gpt.py

test: $(VENV)/Scripts/activate
	$(PYTEST) --verbose es_gpt_test.py -s -vv

app: $(VENV)/Scripts/activate
	$(UVICORN) app:app --reload --port 7002

clean:
	rm -rf __pycache__
	rm -rf $(VENV)
