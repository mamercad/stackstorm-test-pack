.PHONY: install
install:
	st2 pack install git@github.com:mamercad/stackstorm-test-pack.git

.PHONY: run
run:
	st2 run test.awx \
		tower_host="$(TOWER_HOST)" \
		tower_oauth_token="$(TOWER_OAUTH_TOKEN)" \
		job_template_id=17 \
		inventory_id=4 \
		limit="localhost,localhost0,localhost1" \
		extra_vars='{"foo":"bar","fiz":42}'
