import logging
import random
import time

logging.basicConfig(filename='../logs/access.log', level=logging.INFO)

logs = [
    '127.0.0.1 - - [01/Jan/2022:00:00:01 +0000] "GET / HTTP/1.1" 200 758 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"',
    '127.0.0.1 - - [01/Jan/2022:00:00:02 +0000] "GET / HTTP/1.1" 200 758 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15"',
    '127.0.0.1 - - [01/Jan/2022:00:00:03 +0000] "GET / HTTP/1.1" 200 758 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"',
    '127.0.0.1 - - [01/Jan/2022:00:00:04 +0000] "GET / HTTP/1.1" 200 758 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0"',
    '127.0.0.1 - - [01/Jan/2022:00:00:05 +0000] "GET / HTTP/1.1" 200 758 "-" "Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"',
]

while True:
    log = random.choice(logs)
    logging.info(log)
    time.sleep(60)  # wait one minute before logging again
