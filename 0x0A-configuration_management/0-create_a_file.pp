# Create a file school in /tmp directory
file { 'school':
  ensure  =>  'file',
  content =>  'I love Puppet',
  mode    =>  '0744',
  owner   =>  'www-data',
  group   =>  'www-data',
  path    =>  '/tmp/school',
}
