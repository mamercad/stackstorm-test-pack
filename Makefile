.PHONY: install
install:
	st2 pack install git@github.com:mamercad/stackstorm-test-pack.git

.PHONY: test
test:
	st2 run test.jira \
		endpoint="https://cloudmason.atlassian.net" \
		username="mamercad@gmail.com" \
		api_token="$(JIRA_API_TOKEN)" \
		create='{"project":"HOME","summary":"Testing from StackStorm","description":"Testing one two three","issuetype":"Bug"}'
