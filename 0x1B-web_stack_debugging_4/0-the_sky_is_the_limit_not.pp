# Double the worker processes to fix the requests failed

exec { 'fix-nginx':
  command => "sed -i '/s/worker_processes 4;/worker_processes 8;/g' etc/nginx/nginx.conf; sudo service nginx restart",
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}
