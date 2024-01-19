#!/usr/bin/pup
# Install flask (2.1.0)

package { 'python3-pip':
  ensure => installed,
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip',
}

package { 'werkzeug':
  ensure   => '2.0.2',
  provider => 'pip',
  require  => Package['python3-pip'],
}
