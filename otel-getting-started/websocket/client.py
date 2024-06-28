import websocket, json

url = 'wss://api.gemini.com/v1/marketdata/BTCUSD'



def open(ws):
    ws.send(json.dumps('test'))
    print('open')

def on_message(ws, message):
    message = json.loads(message)
    for msg in message['events']:
        print(msg)

    ws.close()

def on_close(ws):
    print('Close')


ws = websocket.WebSocketApp(url, on_open=open, on_message=on_message)

ws.run_forever()
