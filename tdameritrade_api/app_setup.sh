#!/bin/sh

[ ! -f config.json ] && cp config.json.dist config.json

[ ! -d certs ] && mkdir certs

[ ! -f certs/key.pem -a ! -f certificate.pem ] && openssl req -newkey rsa:2048 \
  -nodes -keyout certs/key.pem -x509 -days 365 -out certs/certificate.pem || \
  echo "Certificates exist; use existing or delete and run this script again."
