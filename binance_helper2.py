import requests
import time
from message_helper2 import telegram_send_message
from loguru import logger as log

class Constants:
	def __init__(self,uid):
		self.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',}
		self.uid = uid
	def post_data(self):
		return {
        'encryptedUid': self.uid,
        'tradeType': 'PERPETUAL'}
def get_position(uid,data,max_retries=5):
	c = Constants(uid)
	retry = 0
	while retry <= max_retries:
		try:
			return requests.post("https://www.binance.com/bapi/futures/v1/public/future/leaderboard/getOtherPosition",
				c.headers, json=c.post_data())
		except requests.exceptions.ConnectionError as e:
			log.exception(e)
			log.error("Connection error")
			telegram_send_message(f"Connection error: {e}")
			if retry >= max_retries:
				telegram_send_message(f"Max retries reached. Waiting for 10 minutes before next try.")
				time.sleep(600)
				retry = 0
			else:
				log.info("Retrying.")
				time.sleep(5)
				retry+=1

def get_nickname(uid,data,max_retries=5):
	c = Constants(uid)
	retry = 0
	while retry <= max_retries:
		try:
			return requests.post("https://www.binance.com/bapi/futures/v2/public/future/leaderboard/getOtherLeaderboardBaseInfo",
				c.headers, json=c.post_data())
		except requests.exceptions.ConnectionError as e:
			log.exception(e)
			log.error("Connection error get_nickname")
			telegram_send_message(f"Connection error: {e}")
			if retry >= max_retries:
				telegram_send_message(f"Max retries reached. Waiting for 10 minutes before next try.")
				time.sleep(600)
				retry = 0
			else:
				log.info("Retrying.")
				time.sleep(5)
				retry+=1

def get_markprice(symbol):
	api_url = "https://fapi.binance.com/fapi/v1/premiumIndex"
	response = requests.get(api_url,params={"symbol":symbol})
	try:
		r = response.json()
		return r["markPrice"]
	except Exception as e:
		log.exception(e)
		return "Mark price retrieved failed."
