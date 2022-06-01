# Fix the web stack debugging 3
exec { 'fix' :
  command => 'sed -i s/phpp/php/g /var/www/hrml/wp-settings.php',
  path    => [ '/bin/', '/sbin/', '/usr/bin', '/usr/sbin']
}
