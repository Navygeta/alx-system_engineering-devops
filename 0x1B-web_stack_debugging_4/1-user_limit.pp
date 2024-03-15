# Puppet manifest for adjusting the limits.conf file to address high file descriptor usage by modifying nofile settings.

exec { 'replace_nofile_1':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',
  before   => Exec['replace_nofile_2'],
}

exec { 'replace_nofile_2':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf',
}
