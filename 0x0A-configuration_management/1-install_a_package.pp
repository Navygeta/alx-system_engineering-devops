#!/usr/bin/pup
# Install flask (2.1.0)
package { 'python3-pip':
  ensure => installed,
}
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pipi3',
}

