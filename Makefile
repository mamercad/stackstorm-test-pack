.PHONY: install shell python list remove

install:
	st2 pack install https://github.com/mamercad/stackstorm-test-pack.git

shell:
	st2 run test.shell

python:
	st2 run test.python

list:
	st2 action list --pack test

remove:
	st2 pack remove test
