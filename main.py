meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD": "morirse de la risa",
            "KYS": "Significa suicidate",
            "F": "significa que no podemos hacer nada por el",
            }
while True():
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("ohh... esa no me la se")
