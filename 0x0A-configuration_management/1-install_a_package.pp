#!/usr/bin/pup
# Install flask (2.1.0)

package { 'python3-pip':
  ensure => installed,
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pipi',
}

package { 'werkzeug':
  ensure => '2.1.1',
  provider => 'pip',
  require => Package['python3-pip']
}
