import pandas as pd
import time
import json
import requests
import datetime
#from message_helper2 import telegram_send_message
#from binance import Client
#from binance_helper2 import get_position, get_nickname, get_markprice
from loguru import logger as log
import sys
log.remove()
log.level("INFO",color="<blue>")
log.level("WARNING",color="<yellow>")
log.level("ERROR",color="<red>")
log.add(sys.stderr,format="<lvl>[{time:YYYY-MM-DD HH:mm:ss}][{level}]{message}</lvl>")

api = "a67V1yFZJaCMCMOnKZ8tIgDVQrUeAuoeDFRKeFYyUQykYKaCi29Yf9hTrnDDdu9D"
sec = "2D2SbHHp5wxxyG2KPrCgfUbCRcbL5xR33TIEsBk8ilRfPAOBgLbBeePVFFWSSYv5"


class Constants:
	def __init__(self,uid):
		self.headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
}
		self.uid = uid
	def post_data(self):
		return {
        'encryptedUid': self.uid,
        'tradeType': 'PERPETUAL'}

c=Constants("34553543fff").headers
print(c)
print(c.post_data())