#!/usr/bin/pup
# Install flask (2.1.0)

package { 'python3-pip3':
  ensure => installed,
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pipi3',
}

package { 'werkzeug':
  ensure => '2.0.2',
  provider => 'pip3',
  require => Package['python3-pip3']
}

