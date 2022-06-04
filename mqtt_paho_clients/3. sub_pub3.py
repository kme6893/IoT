import paho.mqtt.client as mqtt

person = 0
temp = 0

def on_connect(client, userdata, flags, rc):
    # 브로커에 연결이 이루어지면 실행됨
    
    print("connected with result code " + str(rc))
    # 브로커에 구독 요청
    client.subscribe("building/person")
    client.subscribe("building/temperature")
    
def on_message(client, userdata, msg):
    global temp
    global person
    # 브로커로부터 구독 메시지를 받으면 실행됨
    
    print("Topic: " + msg.topic + " Message: " + msg.payload.decode("utf-8"))
    
    # 메시지에 담긴 페이로드 데이터를 정수형으로 변환하여 변수에 저장
    if msg.topic == "building/person":
        person = int(msg.payload.decode("utf-8"))
    else :
        temp = int(msg.payload.decode("utf-8"))
    
    # 데이터 값에 따라 on/off 메시지 발행
    if person != 1:
        infot = pubClient.publish("building/light", "off")
        infot.wait_for_publish()
        print("*** light OFF ***")
    else :
        infot = pubClient.publish("building/light", "on")
        infot.wait_for_publish()
        print("*** light ON ***")
        if (temp >= 25):
            infot = pubClient.publish("building/airconditioner", "on")
            infot.wait_for_publish()
            print("temp:", temp, "*** Air conditioning ON ***")
        elif (temp < 25):
            infot = pubClient.publish("building/airconditioner", "off")
            infot.wait_for_publish()
            print("temp:", temp, "*** Air conditioning OFF ***")

# subscribe 용 클라이언트 객체 생성 후 브로커에 연결
subClient = mqtt.Client()
subClient.on_connect = on_connect
subClient.on_message = on_message
subClient.connect("localhost", 1883)

# publish 용 클라이언트 객체 생성 후 브로커에 연결
pubClient = mqtt.Client()
pubClient.connect("localhost", 1883)
pubClient.loop_start()

try:
    subClient.loop_forever()
except KeyboardInterrupt:
    print("Finished!")
    subClient.unsubscribe("building/person")
    subClient.unsubscribe("building/temperature")
    subClient.disconnect()
    pubClient.disconnect()