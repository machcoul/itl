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
