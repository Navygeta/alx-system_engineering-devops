#Client configuration file (w/ Puppet)
# Setting up my client config file
include sshkeys_core

sshkeys_core::client::config { 'my_ssh_config':
  options => {
    'PasswordAuthentication' => 'no',
    'IdentityFile'           => '~/.ssh/school',
  },
}
