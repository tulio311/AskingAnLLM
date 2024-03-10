import urllib3
import json

http = urllib3.PoolManager()


# Here I import my personal authentication key
key = open('MistralKey.txt','r').read()


pregunta = "Help me with the code for being able to choose to trade different coins in this project"


head = open("requestHeader.txt","r")
hh = head.read()
head.close()

pregunta = pregunta + ": " + """

 """ + hh


files = ['bucle.py','allModels.py','Crypto.js','ModelGNB.py','ModelRF.py','ModelSVC.py','ModelXGB.py','Prices.js','process.py','runModel.py']

for file in files:

    lectura = open(file,'r')
    datos = lectura.read()
    lectura.close()

    pregunta = pregunta +f"""

            {file}:

    """ + datos


print(pregunta)


headers = {"Authorization": "Bearer " + key,
           "Content-Type": "application/json",
           "Accept": "application/json"}


request = http.request("POST",
    'https://api.mistral.ai/v1/chat/completions',
    #'https://api.mistral.ai/v1/models',
    json={"model": "mistral-large-latest",
            "messages": [{"role": "user", "content": pregunta}]},
    headers = headers)

info = request.data
info = info.decode('utf-8')
objectInfo = json.loads(info)

respuesta = objectInfo['choices'][0]['message']['content']

print(respuesta)

f = open("MistralResponse.md", "w")
f.write(respuesta)
f.close()

