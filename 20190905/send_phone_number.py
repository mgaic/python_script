import requests
import urllib
import json

data = {
	"uri": "60027",
	"version": "2.4",
	"context": "WB-73ea5c6e375d4dc48ef6ce8e2580a94b-C896845C0D600001645F507010001FF5-0e74abbc8d88705d82bef2c1f3c1772f",
	"appId": "5002",
	"smid": "",
	"lcid": "2052",
	"byPass": "3",
	"sdid": "62816238",
	"requestId": "64023647",
	"data": {
		"phone": "08615872998154",
		"behavior": "%5B%7B%22page.login%22%3A%220.251%22%7D%2C%7B%22page.phoneLogin%22%3A%220.261%22%7D%2C%7B%22input.l.phone%22%3A%2223.839%22%7D%2C%7B%22input.l.phone%22%3A%2226.183%22%7D%2C%7B%22input.l.phone%22%3A%2231.388%22%7D%2C%7B%22input.l.phone%22%3A%221202.239%22%7D%2C%7B%22input.l.phone%22%3A%221206.188%22%7D%5D",
		"page": "https://www.huya.com/19496828"
	}
}

headers = {
"Host":"udblgn.huya.com",
"Connection":"keep-alive",
"Content-Length":"581",
"reqid":"60361790",
"Origin":"https://udblgn.huya.com",
"uri":"60027",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
"content-type":"application/json;charset=UTF-8",
"context":"WB-73ea5c6e375d4dc48ef6ce8e2580a94b-C896845C0D600001645F507010001FF5-0e74abbc8d88705d82bef2c1f3c1772f",
"lcid":"2052",
"Accept":"*/*",
"Referer":"https://udblgn.huya.com/web/middle/2.4/60326152/https/73ea5c6e375d4dc48ef6ce8e2580a94b",
"Accept-Encoding":"gzip, deflate, br",
"Accept-Language":"zh-CN,zh;q=0.9",
"Cookie":"SoundValue=0.50; __yamid_tt1=0.7077163618277236; __yamid_new=C896845C0D600001645F507010001FF5; udb_guiddata=73ea5c6e375d4dc48ef6ce8e2580a94b; alphaValue=0.80; isInLiveRoom=true; guid=0e74abbc8d88705d82bef2c1f3c1772f; udb_accdata=08613438334763; __yasmid=0.7077163618277236; udb_passdata=3; h_unt=1567671938; __yaoldyyuid=; _yasids=__rootsid%3DC89693AC19E000019D841BC21EE07800",
}

url = 'https://udblgn.huya.com/web/v2/smsCode'
res = requests.post(url, headers = headers, data = json.dumps(data), verify=False)
print(res)
print(res.text)

