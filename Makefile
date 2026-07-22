.PHONY: audit catalog validate test build clean

PYTHON ?= python3

audit:
	$(PYTHON) scripts/catalog_sources.py --check

catalog:
	$(PYTHON) scripts/catalog_sources.py --output build/catalog/sources.json

validate:
	$(PYTHON) scripts/validate_repository.py

test:
	$(PYTHON) -m unittest discover -s tests -v

build: validate
	$(PYTHON) scripts/build_knowledge_base.py

clean:
	$(PYTHON) scripts/clean_build.py
