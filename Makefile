# If the first argument is "run"...
# ifeq (deploy-server,$(firstword $(MAKECMDGOALS)))
  # use the rest as arguments for "run"
RUN_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  # ...and turn them into do-nothing targets
$(eval $(RUN_ARGS):;@:)
# endif

deploy-all:
	cd deploy && ansible-playbook -i hosts --ask-vault-pass --extra-vars "comment='$(RUN_ARGS)'" deploy.yml -vv
edit-vars:
	ansible-vault edit deploy/vars.yml
edit-hosts:
	ansible-vault edit deploy/hosts
init:
	cd deploy && ansible-playbook -i hosts --ask-vault-pass deploy.yml -vv -t init
push:
	cd deploy && ansible-playbook -i hosts --ask-vault-pass --extra-vars "comment='$(RUN_ARGS)'" deploy.yml -vv -t push
pull:
	cd deploy && ansible-playbook -i hosts --ask-vault-pass deploy.yml -vv -t pull
