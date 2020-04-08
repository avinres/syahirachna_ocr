CHARS_UNICODE = ["‘",   "’",   "“",   "”",   "(",    ")",   "{",    "}",   "=", "।",  "?",  "-",  "µ", "॰", ",", ".", "् ", 
                "०",  "१",  "२",  "३",     "४",   "५",  "६",   "७",   "८",   "९", "x", 

                "फ़्",  "क़",  "ख़",  "ग़", "ज़्", "ज़",  "ड़",  "ढ़",   "फ़",  "य़",  "ऱ",  "ऩ",    #// one-byte nukta varNas
                "त्त्",   "त्त",     "क्त",  "दृ",  "कृ",

                "ह्न",  "ह्य",  "हृ",  "ह्म",  "ह्र",  "ह्",   "द्द",  "क्ष्", "क्ष", "त्र्", "त्र","ज्ञ",
                "छ्य",  "ट्य",  "ठ्य",  "ड्य",  "ढ्य", "द्य","द्व",
                "श्र",  "ट्र",    "ड्र",    "ढ्र",    "छ्र",   "क्र",  "फ्र",  "द्र",   "प्र",   "ग्र", "रु",  "रू",
                "्र",

                "ओ",  "औ",  "आ",   "अ",   "ई",   "इ",  "उ",   "ऊ",  "ऐ",  "ए", "ऋ",

                "क्",  "क",  "क्क",  "ख्",   "ख",    "ग्",   "ग",  "घ्",  "घ",    "ङ",
                "चै",   "च्",   "च",   "छ",  "ज्", "ज",   "झ्",  "झ",   "ञ",

                "ट्ट",   "ट्ठ",   "ट",   "ठ",   "ड्ड",   "ड्ढ",  "ड",   "ढ",  "ण्", "ण",  
                "त्",  "त",  "थ्", "थ",  "द्ध",  "द", "ध्", "ध",  "न्",  "न",  

                "प्",  "प",  "फ्", "फ",  "ब्",  "ब", "भ्",  "भ",  "म्",  "म",
                "य्",  "य",  "र",  "ल्", "ल",  "ळ",  "व्",  "व", 
                "श्", "श",  "ष्", "ष",  "स्",   "स",   "ह",     

                "ऑ",   "ॉ",  "ो",   "ौ",   "ा",   "ी",   "ु",   "ू",   "ृ",   "े",   "ै",
                "ं",   "ँ",   "ः",   "ॅ",    "ऽ",  "् ", "्" ]

CHARS_KD = ["^", "*",  "Þ", "ß", "¼", "½", "¿", "À", "¾", "A", "\\", "&", "&", "Œ", "]","-","~ ", 
            "å",  "ƒ",  "„",   "…",   "†",   "‡",   "ˆ",   "‰",   "Š",   "‹","Û",

            "¶",   "d",    "[k",  "x",  "T",  "t",   "M+", "<+", "Q",  ";",    "j",   "u",
            "Ù",   "Ùk",   "ä",    "–",   "—",       

            "à",   "á",    "â",   "ã",   "ºz",  "º",   "í", "{", "{k",  "«", "=","K", 
            "Nî",   "Vî",    "Bî",   "Mî",   "<î", "|","}",
            "J",   "Vª",   "Mª",  "<ªª",  "Nª",   "Ø",  "Ý",   "æ", "ç", "xz", "#", ":",
            "z",

            "vks",  "vkS",  "vk",    "v",   "bZ",  "b",  "m",  "Å",  ",s",  ",",   "_",

            "D",  "d",    "ô",     "[",     "[k",    "X",   "x",  "?",    "?k",   "³", 
            "pkS",  "P",    "p",  "N",   "T",    "t",   "÷",  ">",   "¥",

            "ê",      "ë",      "V",  "B",   "ì",       "ï",     "M",  "<",  ".", ".k",   
            "R",  "r",   "F", "Fk",  ")",    "n", "/",  "/k",  "U", "u",   

            "I",  "i",   "¶", "Q",   "C",  "c",  "H",  "Hk", "E",   "e",
            "¸",   ";",    "j",  "Y",   "y",  "G",  "O",  "o",
            "'", "'k",  "\"", "\"k", "L",   "l",   "g",      

            "v‚",    "‚",    "ks",   "kS",   "k",     "h",    "q",   "w",   "`",    "s",    "S",
            "a",    "¡",    "%",     "W",   "·",   "~ ", "~"]

def uni_to_kruti(uni_text):
    uni_text = uni_text
    if uni_text != "":
        #print("In uni_text if")
        uni_text = uni_text.replace ( "क़" , "क़" )
        uni_text = uni_text.replace ( "ख़‌" , "ख़" )
        uni_text = uni_text.replace ( "ग़" , "ग़" )
        uni_text = uni_text.replace ( "ज़" , "ज़" )
        uni_text = uni_text.replace ( "ड़" , "ड़" )
        uni_text = uni_text.replace ( "ढ़" , "ढ़" )
        uni_text = uni_text.replace ( "ऩ" , "ऩ" )
        uni_text = uni_text.replace ( "फ़" , "फ़" )
        uni_text = uni_text.replace ( "य़" , "य़" )
        uni_text = uni_text.replace ( "ऱ" , "ऱ" )
        ###############################################################
        #replacing #  ? + ि  ->  f + ?
        position_of_f = uni_text.find("ि")
        #print(position_of_f)
        while(position_of_f != -1):
            #print("First While")
            character_left_to_f = uni_text[position_of_f-1]
            uni_text = uni_text.replace(character_left_to_f + "ि", "f" + character_left_to_f, 1)
            position_of_f = position_of_f-1
            while((uni_text[position_of_f-1]=="्")&(position_of_f!=0)):
                #print("second_while")
                string_to_be_replaced = uni_text[position_of_f-2] + "्"
                uni_text = uni_text.replace(string_to_be_replaced + "f", "f" + string_to_be_replaced, 1)
                position_of_f = position_of_f-2
            position_of_f = uni_text.find("ि",position_of_f)
        ###############################################################
        #eliminating "र्" and putting  Z  at proper position for this.
        set_of_matras = str(["ा","ि","ी","ु","ू","ृ","े","ै","ो","ौ","ं",":","ँ","ॅ"])
        uni_text += '  ' #putting a pad of 2 string to avoid undefined character error
        position_of_half_R = uni_text.find("र्")
        #print(position_of_half_R)
        while(position_of_half_R > 0):
            #print("third while")
            probable_position_of_Z = position_of_half_R + 2
            #print(probable_position_of_Z)
            character_right_to_probable_position_of_Z = uni_text[probable_position_of_Z+1]
            #print(character_right_to_probable_position_of_Z)
            while(set_of_matras.find(character_right_to_probable_position_of_Z) != -1):
                #print("FOURTH while")
                probable_position_of_Z = probable_position_of_Z + 1
                character_right_to_probable_position_of_Z = uni_text[probable_position_of_Z+1]
            string_to_be_replaced = uni_text[(position_of_half_R + 2):(probable_position_of_Z - position_of_half_R - 1)]
            uni_text = uni_text.replace("र्" + string_to_be_replaced , string_to_be_replaced + "Z", 1)
            position_of_half_R = uni_text.find("र्")
        ###############################################################
        uni_text = uni_text[(0):(len(uni_text)-2)] #removing the padding
        len_uni = int(len(CHARS_UNICODE))
        #print(len_uni)
        len_kd = int(len(CHARS_KD))
        #print(len_kd)

        for input_symbol_idx in range (len_uni):
            #print("IN FINAL FOR LOOP")
            idx = 0
            while(idx != -1):
                ##print("FIFTH while")
                a = CHARS_UNICODE[input_symbol_idx]
                b = CHARS_KD[input_symbol_idx]
                ##print(a, b)
                uni_text = uni_text.replace(a, b, 1)
                idx = uni_text.find(CHARS_UNICODE[input_symbol_idx])
                ##print(idx)
    return uni_text

def convert_to_kruti(uni_string):
    kruti_string = ''
    
    text_size = len(uni_string)
    sthiti1 = 0
    sthiti2 = 0
    chale_chalo = 1
    max_text_size = 6000
    
    while chale_chalo == 1:
        sthiti1 = sthiti2
        
        if sthiti2 < (text_size - max_text_size):
            sthiti2 += max_text_size
            while uni_string[sthiti2] != ' ':
                sthiti2 -= 1
        else:
            sthiti2 = text_size
            chale_chalo = 0
        
        uni_text = uni_string[sthiti1:sthiti2]
        kruti_string += uni_to_kruti(uni_text)
    return kruti_string

# file1 = open("uni_text_1.txt","r", encoding="utf8")
# a = file1.read()
# print(len(a))
# # a = "रही थीं। 26 सितम्बर 1977 की सुबह छह बजकर 10 मिनट पर आखिर मृत्यु \
# #      जब आई तो उन्होंने उसे गले लगा लिया, क्योंकि वही अब उन्हें कष्ट से, अकेलेपन की यातना \
# #      से मुक्ति दिला सकती थी। उन्होंने अपने बेटे-बेटी और पत्नी को आशीर्वाद दिया \
# #      और चले गए अंजाने पथ की ओर। नृत्य परम्परा को आगे बढाने के लिए ----गए। \
# #      पश्चिम बंगाल सरकार ने राजकीय सम्मान के साथ उनकी अत्येंष्टिकी | बंगाल के \
# #      सरकारी दफ्तर बंद कर दिए गए। मृत्यु ने उन्हें गुमनामी के अंधेरे से निकाला, फिर \
# #      प्रसिद्धि के शिखर पर पहुंचा दिया था। रवीन्द्र भवन में उनको श्रद्धांजलि अर्पित करने \
# #      हजारों लोग पहुंचे। आकाशवाणी और दूरदर्शन पर उन्हें श्रद्धांजलि देने वालों की भीड \
# #      लग गई । डाक विभाग ने उदयशंकर और उनकी नृत्यमंडली पर टिकट निकाले। \
# #      उनका `तांडव नृत्य` का टिकट बहुत प्रसिद्ध हुआ। सत्यजीत राय ने उदयशंकर पर \
# #      वृत्त चित्र बनाने की कोशिशें की, लेकिन वह काम नहीं हो पाया। \
# #      अमला शंकर और नमता शंकर कोलकाता में उदयशंकर नृत्यविद्यालय चलाते \
# #      हैं। वे उदयशंकर की नृत्य परम्परा को आगे बढा रहे हैं। नटराज अब नहीं हैं, लेकिन \
# #      उनके घुघरुओं की आवाज अब भी सुनी जा सकती है। संगीत नाटक अकादमी ने \
# #      उनकी जन्म शताब्दी 2001 में दिल्ली में एक सप्ताह का नृत्य नाटक सभाएं आयोजित \
# #      किया था। जिसमें इस जीनियस के काम की फिर पहचान की गई थी ।"
# a = str(a)
# uni_a = convert_to_kruti(a)
# file2 = open("kruti_text_from_code_im.txt", "w", encoding="utf8")
# file2.write(uni_a)