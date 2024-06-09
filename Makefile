.PHONY: gen update_deps run freeze test

gen:
	@./proto/install_betterproto.sh
	@./proto/gen.sh

update_deps:
	@./proto/update_deps.sh

run:
	@./run.sh

freeze:
	@pip freeze > requirements.txt

test:
	@python -m unittest discover -p "*_test.py" memos_webhook

.PHONY: package_build package_clean package_publish

package_build:
	@python -m build

package_clean:
	@rm -rf dist
	@rm -rf *.egg-info

package_publish:
	@python -m twine upload dist/*
