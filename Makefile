.PHONY: gen update_deps run

gen:
	@./proto/install_betterproto.sh
	@./proto/gen.sh

update_deps:
	@./proto/update_deps.sh

run:
	@./run.sh

freeze:
	@pip freeze > requirements.txt