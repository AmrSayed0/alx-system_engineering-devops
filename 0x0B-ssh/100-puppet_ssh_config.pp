#!/usr/bin/env bash
# using Puppet to make changes to my configuration file

file { '/etc/ssh/ssh_config':
  ensure => present,
  content => "
    #SSH client configuration
    host*
    IdentityFile ~/.ssh/school
    passwordAuthentication no
  ",
}
