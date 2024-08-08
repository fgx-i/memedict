meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "RIZZ": "Karizma kelimesinin kısaltılmış versiyonu",
            "/J": "'Tone indicator'lardan biri. Şaka anlamına gelir, cümlenin sonuna konur."
            }

while True:
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")


    if word in meme_dict.keys():
        print(word, ":", meme_dict[word], "\n")
    else:
        print("Aradığınız kelime bulunamadı. Lütfen tekrar deneyin ve tamamını büyük harfle yazdığınızdan emin olun. \n")


