DIR := deploy
HOSTS := hosts
VARS := vars.yml
PLAYBOOK := playbook.yml

RUN_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
$(eval $(RUN_ARGS):;@:)
EDIT := cd $(DIR) && ansible-vault edit
PLAY := cd $(DIR) && ansible-playbook -i $(HOSTS) -e "comment='$(RUN_ARGS)'" $(PLAYBOOK) --ask-vault-pass

refresh:
	$(PLAY) -t refresh
edit-vars:
	$(EDIT) $(VARS)
edit-hosts:
	$(EDIT) $(HOSTS)
init:
	$(PLAY) -t init
push:
	$(PLAY) -t push
pull:
	$(PLAY) -t pull
test:
	$(PLAY) -t test
