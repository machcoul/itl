deploy-server:
	( cd deploy && ansible-playbook -i hosts --ask-vault-pass deploy.yml -vv )
