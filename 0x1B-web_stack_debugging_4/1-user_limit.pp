# Puppet manifest to adjust OS configuration
#Resolves "Too many open files" issue for the holberton user

# Increase Holberton user hard file limit.

exec { 'increase-hard-file-limit-for-holberton-user':

  command => "sed -i '/^holberton hard/s/4/50000/' /etc/security/limits.conf",

  path    => '/usr/local/bin/:/bin/'

}


# Increase Holberton user soft file limit.

exec { 'increase-soft-file-limit-for-holberton-user':

  command => 'sed -i "/^holberton soft/s/5/50000/" /etc/security/limits.conf',

  path    => '/usr/local/bin/:/bin/'

}
