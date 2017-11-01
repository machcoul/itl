# itl

This is my project :-)

## Getting Started

### Prerequisites

You need to install on the control machine :
  - git
  - ansible > 2.3 [Installing ansible with pip](http://docs.ansible.com/ansible/latest/intro_installation.html#latest-releases-via-pip)
  - sshpass

### Installing

Clone the repository

    git clone https://github.com/machcoul/itl.git

Go to the directory

    cd itl

Edit vars.yml and/or edit hosts with your parameters (required password)

    make edit-vars
    make edit-hosts

### Usage

How to push on github and deploy on server (required password)

    make deploy-server 'your comments'

### Notes

#### Remove sensitive data in GitHub repository [link](https://help.github.com/articles/removing-sensitive-data-from-a-repository/)

  - delete files
  - Overwrite your existing tags

        git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch <file>' --prune-empty --tag-name-filter cat -- --all

  - Add your file with sensitive data to .gitignore
  - Force-push your local changes to overwrite your GitHub repository

        git push origin --force --all
        git push origin --force --tags
