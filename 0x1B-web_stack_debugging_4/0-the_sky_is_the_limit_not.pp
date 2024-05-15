# Puppet manifest to optimize Nginx configuration for handling high load

# Increase default file ULIMIT

exec { 'fix--for-nginx':

  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',

  path    => '/usr/local/bin/:/bin/',

}

#->

# Restart Nginx

exec { 'nginx-restart':

  command => '/etc/init.d/nginx restart',

  path    => '/etc/init.d/',

}
