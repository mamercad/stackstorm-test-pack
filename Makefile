.PHONY: install
install:
	st2 pack install git@github.com:mamercad/stackstorm-test-pack.git

.PHONY: test
test:
	st2 run test.jira
