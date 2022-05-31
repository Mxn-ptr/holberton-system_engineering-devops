# Fix the web stack debugging 3
exec { 'fix' :
  command  => 'sed -i s/phpp/php/g /var/www/hrml/wp-settings.php',
  provider => shell,
}
