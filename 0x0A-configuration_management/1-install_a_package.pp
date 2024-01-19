#!/usr/bin/pup
# Install a specific version of flask (2.1.0)

package { 'python3-pip':
  ensure => installed,
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pipi3',
}
