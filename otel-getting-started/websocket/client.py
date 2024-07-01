import websocket, json

url = 'wss://api.gemini.com/v1/marketdata/BTCUSD'



# def open(ws):
#     ws.send(json.dumps('test'))
#     print('open')

# def on_message(ws, message):
#     message = json.loads(message)
#     for msg in message['events']:
#         print(msg)

#     ws.close()

# def on_close(ws):
#     print('Close')


# ws = websocket.WebSocketApp(url, on_open=open, on_message=on_message)

# ws.run_forever()

import time
import threading

def one(x):
    c = 0
    print('[sub-thread] Thread processing 4 task')
    while c < 4:
        time.sleep(2)
        print(f'[sub-thread] running {x} - Task of {c}')
        c += 1

time.sleep(1)

# t = threading.Thread(target=one, args=(1,))
# t.start()

#print('thread running')
time.sleep(1)
print('main')
for i in range(100):
    time.sleep(1)
    if i %2 == 0 and i %8==0:
        t = threading.Thread(target=one, args=(i,))
        t.start()
    print(f'[main thread] {i}')

