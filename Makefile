PYTHON ?= python
REPO_ROOT := $(CURDIR)

.PHONY: test demo

test:
	$(PYTHON) -m unittest discover -s tests -v

demo:
	$(PYTHON) -m computational_geology.cli demo --output-dir $(REPO_ROOT)/examples/demo-output
