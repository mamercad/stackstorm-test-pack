.PHONY: install
install:
	st2 pack install git@github.com:mamercad/stackstorm-test-pack.git

.PHONY: test
test: install
	st2 run test.jira \
		create='{"project":"HOME","summary":"Testing from StackStorm",description:"Testing one two three","issuetype"={"name":"Bug"}}'
