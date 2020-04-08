CHARS_UNICODE = [" ।", " ?"," !",
                    "ॐ",
                    # ignore all nuktas except in ड़ and ढ़
                    "‘", "’", "“", "”", "(", ")", "=", "।", "?", "-", "µ", "॰", ",", ".", "् ","%", "॥",
                    "०","१","२","३","४","५","६","७","८","९","x","+",";","_",

                    "फ़्","क़","ख़","ग़","ज़्","ज़","ड़","ढ़","फ़","य़","ऱ","ऩ",    #// one-byte nukta varNas
                    "त्त्","त्त","क्त","कृ","ङ्क्ष","द्घ","ञ्च","ङ्क","ङ्ख","ङ्ग","ङ्घ","ल्ल","श्च","श्व",

                    "श्व","ह्व","ह्य","हृ","ह्म","ह्र","ह्","द्द","क्ष्","क्ष","त्र्","त्र्","त्र","ज्ञ", #//"त्र",
                    "छ्य","ञ्ज","ट्य","ठ्य","ड्य","ढ्य","द्म","द्य","द्व","द्भ","द्ग",
                    "श्र","स्र","स्त्र","ट्र","ड्र","ढ्र","छ्र","क्र","फ्र","ङ्क्त","ग्र","रु","रू","ह्ण","ह्ल","ह्न","ह्र",
                    "्र",

                    "ओ","औ","आ","अ","ई","इ","उ","ऊ","ऐ","ए","ऋ","ॠ","ॡ",

                    "क्क","क्","क","ख्","ख","ग्","ग","घ्","घ","ङ",
                    "चै","च्","च","छ","ज्","ज","झ","ञ्","ञ",

                    "ट्ट","ट्ठ","ट","ठ","ड्ड","ड्ढ","ड","ढ","ण्","ण",  
                    "त्","त","थ्","थ","द्ध","द","ध्","ध","न्","न",  

                    "प्","प","फ्","फ","ब्","ब","भ्","भ","म्","म",
                    "य्","य","र","ल्","ल","ळ","व्","व", 
                    "श्", "श",  "ष्", "ष",  "स्",   "स",   "ह",

                    "र्‍",

                    "ऑ","ॉ","ो","ौ","ा","ीं","ी","ु","ू","ृ","ॄ","ॢ","ें","े","ैं","ै",
                    "ं","ँ","ः","ॅ","ऽ","् ","्","़","/"]


CHARS_SHIVA = ["।", "?","!",
                 "¬",

                "^", "*", "ß", "Þ", "¼", "½", "¾", "A", "\\", "&", "&", "ñ", "]", "-", "~ ", "»","Ï",
                "‚","ƒ","„","…","†","‡","ˆ","‰","Š","‹","Û","$","(","&", #//"å",

                #// "¶","d","[k","x","T","t","M+","<+","Q",";","j","u",
                "¶+","d+","[k+","x+","T+","t+","M+","<+","Q+",";+","j+","u+",
                "Ù","Ùk","ä","Ñ","Ó","ð","÷", "ø","ù","ú","û","ü","ý","þ",    

                "Üo","à","á","â","ã","ºz","º","í","{","{k","«","=","=k","K", 
                "Nî","À","Vî","Bî","Mî","<î","É","|","}","Ò","å",
                "J","ò","ó","Vª","Mª","<ªª","Nª","Ø","Ý","ç","xz","#",":","Ê","Ë","Ì","Ð",
                "z",

                "vks","vkS","vk","v","bZ","b","m","Å",",s",",","_","Ç","È",

                "ô","D","d","[","[k","X","x","?","?k","³", 
                "pkS","P","p","N","T","t",">","×","×k",

                "ê","ë","V","B","ì","ï","M","<",".",".k",   
                "R","r","F","Fk",")","n","è","èk","U","u",   

                "I","i","¶","Q","C","c","H","Hk","E","e",
                "¸",";","j","Y","y","G","O","o",
                "'","'k","\"","\"k","L","l","g",      

                "Ú",

                "vkW","kW","ks","kS","k","°","h","q","w","`","¤","¦","­","s","®","S",
                "a","¡","¢","W","·","~ ","~","+","@"]

# CHARS_UNICODE = [" ।", " ?"," !",
#                 "ॐ",
#                 # ignore all nuktas except in ड़ and ढ़
#                 "‘", "’", "“", "”", "(", ")", "=", "।", "?", "-", "µ", "॰", ",", ".", "् ","%", "॥",
#                 "०","१","२","३","४","५","६","७","८","९","x","+",";","_",

#                 "फ़्","क़","ख़","ग़","ज़्","ज़","ड़","ढ़","फ़","य़","ऱ","ऩ",#    // one-byte nukta varNas
#                 "त्त्","त्त","क्त","कृ","ङ्क्ष","द्घ","ञ्च","ङ्क","ङ्ख","ङ्ग","ङ्घ","ल्ल","श्च","श्व",

#                 "श्व","ह्व","ह्य","हृ","ह्म","ह्र","ह्","द्द","क्ष्","क्ष","त्र्","त्र्","त्र","ज्ञ", #//"त्र",
#                 "छ्य","ञ्ज","ट्य","ठ्य","ड्य","ढ्य","द्म","द्य","द्व","द्भ","द्ग",
#                 "श्र","स्र","स्त्र","ट्र","ड्र","ढ्र","छ्र","क्र","फ्र","ङ्क्त","ग्र","रु","रू","ह्ण","ह्ल","ह्न","ह्र",
#                 "्र",

#                 "ओ","औ","आ","अ","ई","इ","उ","ऊ","ऐ","ए","ऋ","ॠ","ॡ",

#                 "क्क","क्","क","ख्","ख","ग्","ग","घ्","घ","ङ",
#                 "चै","च्","च","छ","ज्","ज","झ","ञ्","ञ",

#                 "ट्ट","ट्ठ","ट","ठ","ड्ड","ड्ढ","ड","ढ","ण्","ण",  
#                 "त्","त","थ्","थ","द्ध","द","ध्","ध","न्","न",  

#                 "प्","प","फ्","फ","ब्","ब","भ्","भ","म्","म",
#                 "य्","य","र","ल्","ल","ळ","व्","व", 
#                 "श्", "श",  "ष्", "ष",  "स्",   "स",   "ह",

#                 "र्‍",

#                 "ऑ","ॉ","ो","ौ","ा","ीं","ी","ु","ू","ृ","ॄ","ॢ","ें","े","ैं","ै",
#                 "ं","ँ","ः","ॅ","ऽ","् ","्","़","/"]

# CHARS_SHIVA = ["।", "?","!",
#                  "¬",

#                 "^", "*", "ß", "Þ", "¼", "½", "¾", "A", "\\", "&", "&", "ñ", "]", "-", "~ ", "»","Ï",
#                 "‚","ƒ","„","…","†","‡","ˆ","‰","Š","‹","Û","$","(","&", #//"å",

#                 #// "¶","d","[k","x","T","t","M+","<+","Q",";","j","u",
#                 "¶+","d+","[k+","x+","T+","t+","M+","<+","Q+",";+","j+","u+",
#                 "Ù","Ùk","ä","Ñ","Ó","ð","÷", "ø","ù","ú","û","ü","ý","þ",    

#                 "Üo","à","á","â","ã","ºz","º","í","{","{k","«","=","=k","K", 
#                 "Nî","À","Vî","Bî","Mî","<î","É","|","}","Ò","å",
#                 "J","ò","ó","Vª","Mª","<ªª","Nª","Ø","Ý","ç","xz","#",":","Ê","Ë","Ì","Ð",
#                 "z",

#                 "vks","vkS","vk","v","bZ","b","m","Å",",s",",","_","Ç","È",

#                 "ô","D","d","[","[k","X","x","?","?k","³", 
#                 "pkS","P","p","N","T","t",">","×","×k",

#                 "ê","ë","V","B","ì","ï","M","<",".",".k",   
#                 "R","r","F","Fk",")","n","è","èk","U","u",   

#                 "I","i","¶","Q","C","c","H","Hk","E","e",
#                 "¸",";","j","Y","y","G","O","o",
#                 "'","'k","\"","\"k","L","l","g",      

#                 "Ú",

#                 "vkW","kW","ks","kS","k","°","h","q","w","`","¤","¦","­","s","®","S",
#                 "a","¡","¢","W","·","~ ","~","+","@"]

def uni_to_shiva(uni_text):
    uni_text = uni_text
    if uni_text != "":
        uni_text = uni_text.replace ("त्र्य", "«य" )
        uni_text = uni_text.replace ("श्र्य", "Ü‍‍zय" )
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
        while(position_of_f != -1):
            character_left_to_f = uni_text[position_of_f-1]
            uni_text = uni_text.replace(character_left_to_f + "ि", "f" + character_left_to_f, 1)
            position_of_f = position_of_f-1
            while((uni_text[position_of_f-1]=="्")&(position_of_f!=0)):
                string_to_be_replaced = uni_text[position_of_f-2] + "्"
                uni_text = uni_text.replace(string_to_be_replaced + "f", "f" + string_to_be_replaced, 1)
                position_of_f = position_of_f-2
            position_of_f = uni_text.find("ि",position_of_f+1)
        ###############################################################
        #eliminating "र्" and putting  Z  at proper position for this.
        #set_of_matras = "ािीुूृेैोौं:ँॅ" 
        set_of_matras = str(["ा","ि","ी","ु","ू","ृ","े","ै","ो","ौ","ं",":","ँ","ॅ"])
        uni_text += '  ' #putting a pad of 2 string to avoid undefined character error
        position_of_half_R = uni_text.find("र्")
        while(position_of_half_R > 0):
            probable_position_of_Z = position_of_half_R + 2
            character_at_probable_position_of_Z = uni_text[probable_position_of_Z]
            while(set_of_matras.find(character_at_probable_position_of_Z) != -1):
                probable_position_of_Z = probable_position_of_Z + 1
                character_at_probable_position_of_Z = uni_text[probable_position_of_Z]
            right_to_position_of_Z = probable_position_of_Z+1
            if (right_to_position_of_Z>0):
                character_right_to_position_of_Z = uni_text[right_to_position_of_Z]
                while(character_right_to_position_of_Z == "्"):
                    probable_position_of_Z = right_to_position_of_Z + 1
                    character_at_probable_position_of_Z = uni_text[probable_position_of_Z]
                    right_to_position_of_Z = probable_position_of_Z + 1
                    character_right_to_position_of_Z = uni_text[right_to_position_of_Z]
            string_to_be_replaced = uni_text[(position_of_half_R + 2):(probable_position_of_Z + 1)]
            uni_text = uni_text.replace("र्" + string_to_be_replaced , string_to_be_replaced + "Z", 1)
            position_of_half_R = uni_text.find("र्")
        ###############################################################
        uni_text = uni_text[(0):(len(uni_text)-2)] #removing the padding
        len_uni = int(len(CHARS_UNICODE))
        len_kd = int(len(CHARS_SHIVA))
        
        for input_symbol_idx in range (len_uni):
            idx = 0
            while(idx != -1):
                a = CHARS_UNICODE[input_symbol_idx]
                b = CHARS_SHIVA[input_symbol_idx]
                uni_text = uni_text.replace(a, b, 1)
                idx = uni_text.find(CHARS_UNICODE[input_symbol_idx])
    uni_text = uni_text.replace("Zksa" , "ksZa" ) ; 
    uni_text = uni_text.replace("~ Z" , "Z~" ) ; 
    uni_text = uni_text.replace("Zk" , "kZ" ) ; 
    return uni_text

def convert_to_shiva(uni_string):
    shiva_string = ''
    
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
        shiva_string += uni_to_shiva(uni_text)
    return shiva_string

# file1 = open("uni_text_1.txt","r", encoding="utf8")
# a = file1.read()
# print(len(a))
# # # a = "रही थीं। 26 सितम्बर 1977 की सुबह छह बजकर 10 मिनट पर आखिर मृत्यु \
# # #      जब आई तो उन्होंने उसे गले लगा लिया, क्योंकि वही अब उन्हें कष्ट से, अकेलेपन की यातना \
# # #      से मुक्ति दिला सकती थी। उन्होंने अपने बेटे-बेटी और पत्नी को आशीर्वाद दिया \
# # #      और चले गए अंजाने पथ की ओर। नृत्य परम्परा को आगे बढाने के लिए ----गए। \
# # #      पश्चिम बंगाल सरकार ने राजकीय सम्मान के साथ उनकी अत्येंष्टिकी | बंगाल के \
# # #      सरकारी दफ्तर बंद कर दिए गए। मृत्यु ने उन्हें गुमनामी के अंधेरे से निकाला, फिर \
# # #      प्रसिद्धि के शिखर पर पहुंचा दिया था। रवीन्द्र भवन में उनको श्रद्धांजलि अर्पित करने \
# # #      हजारों लोग पहुंचे। आकाशवाणी और दूरदर्शन पर उन्हें श्रद्धांजलि देने वालों की भीड \
# # #      लग गई । डाक विभाग ने उदयशंकर और उनकी नृत्यमंडली पर टिकट निकाले। \
# # #      उनका `तांडव नृत्य` का टिकट बहुत प्रसिद्ध हुआ। सत्यजीत राय ने उदयशंकर पर \
# # #      वृत्त चित्र बनाने की कोशिशें की, लेकिन वह काम नहीं हो पाया। \
# # #      अमला शंकर और नमता शंकर कोलकाता में उदयशंकर नृत्यविद्यालय चलाते \
# # #      हैं। वे उदयशंकर की नृत्य परम्परा को आगे बढा रहे हैं। नटराज अब नहीं हैं, लेकिन \
# # #      उनके घुघरुओं की आवाज अब भी सुनी जा सकती है। संगीत नाटक अकादमी ने \
# # #      उनकी जन्म शताब्दी 2001 में दिल्ली में एक सप्ताह का नृत्य नाटक सभाएं आयोजित \
# # #      किया था। जिसमें इस जीनियस के काम की फिर पहचान की गई थी ।"
# #a = str(a)
# uni_a = convert_to_shiva(a)
# file2 = open("shiva_text_from_code_im.txt", "w", encoding="utf8")
# file2.write(uni_a)