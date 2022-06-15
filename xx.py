import streamlit as st
import string

def LexicalAnalysis(kalimat) :
  #initialization
  alphabet_list = list(string.ascii_lowercase)

  state_list = [
                "q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10", "q11", "q12", "q13", "q14", "q15", "q16",
                "q17", "q18", "q19", "q20", "q21", "q22", "q23", "q24", "q25", "q26", "q27", "q28", "q29", "q30", "q31", "q32", 
                "q33", "q34", "q35", "q36", "q37", "q38", "q39", "q40","q41", "q42", "q43", "q44", "q45", "q46", "q47", "q48"
                ]

  transition_table = {}

  for state in state_list :
    for alphabet in alphabet_list :
      transition_table[(state, alphabet)] = "error"
    transition_table[(state, "#")] = "error"
    transition_table[(state, " ")] = "error"

  #first state
  transition_table[("q0", " ")] = "q0"

  #finish state
  transition_table[("q47", "#")] = "accept"
  transition_table[("q47", " ")] = "q48"
  
  transition_table[("q48", "#")] = "accept"
  transition_table[("q48", " ")] = "q48"

  #string "ang"
  transition_table[("q48", "a")] = "q14"
  transition_table[("q0", "a")] = "q14"
  transition_table[("q14", "n")] = "q15"
  transition_table[("q15", "g")] = "q47"
  transition_table[("q47", " ")] = "q48"

  #string "inyo"
  transition_table[("q48", "i")] = "q1"
  transition_table[("q0", "i")] = "q1"
  transition_table[("q1", "n")] = "q2"
  transition_table[("q2", "y")] = "q7"
  transition_table[("q7", "o")] = "q47"
  transition_table[("q47", " ")] = "q48"

  #string "den"
  transition_table[("q48", "d")] = "q23"
  transition_table[("q0", "d")] = "q23"
  transition_table[("q23", "e")] = "q22"
  transition_table[("q22", "n")] = "q47"
  transition_table[("q47", " ")] = "q48"

  #string "lolok"
  transition_table[("q48", "l")] = "q31"
  transition_table[("q0", "l")] = "q31"
  transition_table[("q31", "o")] = "q32"
  transition_table[("q32", "l")] = "q33"
  transition_table[("q33", "o")] = "q34"
  transition_table[("q34", "k")] = "q47"
  transition_table[("q47", " ")] = "q48"

  #string "poi"
  transition_table[("q48", "p")] = "q16"
  transition_table[("q0", "p")] = "q16"
  transition_table[("q16", "o")] = "q17"
  transition_table[("q17", "i")] = "q47"
  transition_table[("q47", " ")] = "q48"

  #string "bakojo"
  transition_table[("q48", "b")] = "q3"
  transition_table[("q0", "b")] = "q3"
  transition_table[("q3", "a")] = "q4"
  transition_table[("q4", "k")] = "q5"
  transition_table[("q5", "o")] = "q6"
  transition_table[("q6", "j")] = "q7"
  transition_table[("q7", "o")] = "q47"
  transition_table[("q47", " ")] = "q48"

  #string "manunggu"
  transition_table[("q48", "m")] = "q40"
  transition_table[("q0", "m")] = "q40"
  transition_table[("q40", "a")] = "q41"
  transition_table[("q41", "n")] = "q42"
  transition_table[("q42", "u")] = "q43"
  transition_table[("q43", "n")] = "q44"
  transition_table[("q44", "g")] = "q45"
  transition_table[("q45", "g")] = "q46"
  transition_table[("q46", "u")] = "q47"
  transition_table[("q47", " ")] = "q48"

  #string "ngambiok"
  transition_table[("q48", "n")] = "q24"
  transition_table[("q0", "n")] = "q24"
  transition_table[("q24", "g")] = "q25"
  transition_table[("q25", "a")] = "q26"
  transition_table[("q26", "m")] = "q29"
  transition_table[("q29", "b")] = "q30"
  transition_table[("q30", "i")] = "q33"
  transition_table[("q33", "o")] = "q34"
  transition_table[("q34", "k")] = "q47"
  transition_table[("q47", " ")] = "q48"

  #string "ngajau"
  transition_table[("q48","n")] = "q24"
  transition_table[("q0","n")] = "q24"
  transition_table[("q24","g")] = "q25"
  transition_table[("q25","a")] = "q26"
  transition_table[("q26","j")] = "q27"
  transition_table[("q27","a")] = "q28"
  transition_table[("q28","u")] = "q47"
  transition_table[("q47"," ")] = "q48"

  #string "sonduok"
  transition_table[("q48","s")] = "q37"
  transition_table[("q0","s")] = "q37"
  transition_table[("q37","o")] = "q38"
  transition_table[("q38","n")] = "q39"
  transition_table[("q39","d")] = "q36"
  transition_table[("q36","u")] = "q33"
  transition_table[("q33","o")] = "q34"
  transition_table[("q34","k")] = "q47"
  transition_table[("q47"," ")] = "q48"

  #string "oto"
  transition_table[("q48","o")] = "q8"
  transition_table[("q0","o")] = "q8"
  transition_table[("q8","t")] = "q7"
  transition_table[("q7","o")] = "q47"
  transition_table[("q47"," ")] = "q48"

  #string "lawuok"
  transition_table[("q48","l")] = "q31"
  transition_table[("q0","l")] = "q31"
  transition_table[("q31","a")] = "q35"
  transition_table[("q35","w")] = "q36"
  transition_table[("q36","u")] = "q33"
  transition_table[("q33","o")] = "q34"
  transition_table[("q34","k")] = "q47"
  transition_table[("q47"," ")] = "q48"

  #string "guntiong"
  transition_table[("q48","g")] = "q9"
  transition_table[("q0","g")] = "q9"
  transition_table[("q9","u")] = "q10"
  transition_table[("q10","n")] = "q11"
  transition_table[("q11","t")] = "q12"
  transition_table[("q12","i")] = "q13"
  transition_table[("q13","o")] = "q14"
  transition_table[("q14","n")] = "q15"
  transition_table[("q15","g")] = "q47"
  transition_table[("q47"," ")] = "q48"

  #string "pinggan"
  transition_table[("q48","p")] = "q16"
  transition_table[("q0","p")] = "q16"
  transition_table[("q16","i")] = "q18"
  transition_table[("q18","n")] = "q19"
  transition_table[("q19","g")] = "q20"
  transition_table[("q20","g")] = "q21"
  transition_table[("q21","a")] = "q22"
  transition_table[("q22","n")] = "q47"
  transition_table[("q47"," ")] = "q48"
  
  #lexical analysis
  idx_char = 0
  state = "q0"
  current_token = ""

  st.write("current token: ")
  while state != "accept" :
    current_char = input_string[idx_char]
    current_token += current_char
    state = transition_table[(state, current_char)]

    if state == "q47" :
      st.write(current_token.strip(), "\t\t     -> valid")
      current_token = " "

    #if state == "error" :
    #  st.write("!!! ERROR !!!")
    #  break;

    idx_char = idx_char + 1
    
    #conclusion
    if state == "accept" :
      st.write()
      st.write("Semua token diinput: ", kalimat, "{valid}")

  return LexicalAnalysis

def Parser(kalimat) :
  tokens = kalimat.lower().split()
  tokens.append("EOS")

  #symbols definition
  non_terminals = ["S", "SB", "VB", "OB"]
  terminals = [
               "ang", "inyo", "den",
               "lolok", "poi", "bakojo", "manunggu", "ngambiok", "ngajau",
               "sonduok", "oto", "lawuok", "guntiong", "pinggan"
              ]

  parse_table = {}

  parse_table[("S", "ang")] = ["SB", "VB", "OB"]
  parse_table[("S", "inyo")] = ["SB", "VB", "OB"]
  parse_table[("S", "den")] = ["SB", "VB", "OB"]
  parse_table[("S", "lolok")] = ["error"]
  parse_table[("S", "poi")] = ["error"]
  parse_table[("S", "bakojo")] = ["error"]
  parse_table[("S", "manunggu")] = ["error"]
  parse_table[("S", "ngambiok")] = ["error"]
  parse_table[("S", "ngajau")] = ["error"]
  parse_table[("S", "sonduok")] = ["SB", "VB", "OB"]
  parse_table[("S", "oto")] = ["SB", "VB", "OB"]
  parse_table[("S", "lawuok")] = ["SB", "VB", "OB"]
  parse_table[("S", "guntiong")] = ["SB", "VB", "OB"]
  parse_table[("S", "pinggan")] = ["SB", "VB", "OB"]
  parse_table[("S", "EOS")] = ["error"]

  parse_table[("SB", "ang")] = ["ang"]
  parse_table[("SB", "inyo")] = ["inyo"]
  parse_table[("SB", "den")] = ["den"]
  parse_table[("SB", "lolok")] = ["error"]
  parse_table[("SB", "poi")] = ["error"]
  parse_table[("SB", "bakojo")] = ["error"]
  parse_table[("SB", "manunggu")] = ["error"]
  parse_table[("SB", "ngambiok")] = ["error"]
  parse_table[("SB", "ngajau")] = ["error"]
  parse_table[("SB", "sonduok")] = ["error"]
  parse_table[("SB", "oto")] = ["error"]
  parse_table[("SB", "lawuok")] = ["error"]
  parse_table[("SB", "guntiong")] = ["error"]
  parse_table[("SB", "pinggan")] = ["error"]
  parse_table[("SB", "EOS")] = ["error"]

  parse_table[("VB", "ang")] = ["error"]
  parse_table[("VB", "inyo")] = ["error"]
  parse_table[("VB", "den")] = ["error"]
  parse_table[("VB", "lolok")] = ["lolok"]
  parse_table[("VB", "poi")] = ["poi"]
  parse_table[("VB", "bakojo")] = ["bakojo"]
  parse_table[("VB", "manunggu")] = ["manunggu"]
  parse_table[("VB", "ngambiok")] = ["ngambiok"]
  parse_table[("VB", "ngajau")] = ["ngajau"]
  parse_table[("VB", "sonduok")] = ["error"]
  parse_table[("VB", "oto")] = ["error"]
  parse_table[("VB", "lawuok")] = ["error"]
  parse_table[("VB", "guntiong")] = ["error"]
  parse_table[("VB", "pinggan")] = ["error"]
  parse_table[("VB", "EOS")] = ["error"]

  parse_table[("OB", "ang")] = ["error"]
  parse_table[("OB", "inyo")] = ["error"]
  parse_table[("OB", "den")] = ["error"]
  parse_table[("OB", "lolok")] = ["error"]
  parse_table[("OB", "poi")] = ["error"]
  parse_table[("OB", "bakojo")] = ["error"]
  parse_table[("OB", "manunggu")] = ["error"]
  parse_table[("OB", "ngambiok")] = ["error"]
  parse_table[("OB", "ngajau")] = ["error"]
  parse_table[("OB", "sonduok")] = ["sonduok"]
  parse_table[("OB", "oto")] = ["oto"]
  parse_table[("OB", "lawuok")] = ["lawuok"]
  parse_table[("OB", "guntiong")] = ["guntiong"]
  parse_table[("OB", "pinggan")] = ["pinggan"]
  parse_table[("OB", "EOS")] = ["error"]

  #stack initialization
  stack = []
  stack.append("#")
  stack.append("S")

  #input reading initialization
  idx_token = 0
  symbol = tokens[idx_token]

  #parse table process
  while (len(stack) > 0) :
    top = stack[len(stack) - 1]
    st.write("top = ", top)
    st.write("symbol = ", symbol)

    if top in terminals :
      st.write("top adalah simbol terminal")

      if top == symbol :
        stack.pop()
        idx_token = idx_token + 1
        symbol = tokens[idx_token]

        if symbol == "EOS" :
          stack.pop()
          st.write("isi stack : ", stack)
      else :
        st.write("error")
        break;
    elif top in non_terminals :
      st.write("top adalah symbol non-terminal")

      if parse_table[(top,symbol)][0] != "error" :
        stack.pop()
        symbol_to_be_pushed = parse_table[(top, symbol)]

        for i in range(len(symbol_to_be_pushed)-1, -1, -1) :
          stack.append(symbol_to_be_pushed[i])
      else:
        st.write("error")
        break;
    else:
      st.write("error")
      break;

    st.write("isi stack: ",stack)
    st.write()

  #conclusion
  st.write()

  if symbol == "EOS" and len(stack) == 0 :
    st.write("Input string ", "\"", kalimat, "\"", "diterima, sesuai grammar.")
  else:
    st.write("Error, input string: ", "\"", kalimat, "\"", "tidak diterima, tidak sesuai grammar.")

  return Parser

def defLexicalAnalysis() :
  st.write("Analisis leksikal adalah sebuah proses yang mendahului parsing sebuat rangkaian karakter.\
            Ia menerima masukan dan menghasilkan deretan simbol yang dinamakan token. \
            Karakter tersebut akan diproses, bila mengikuti pola yang telah ditentukan dalam bahasa sumber dan disimpan dalam tabel simbol, \
            maka valid. Bila sebaliknya, token tak dapat dikenali (tidak valid).")
  st.write("-"*15)

def defParser() :
  st.write("Parser adalah suatu cara untuk memecah suatu rangkaian masukan dengan mengambil input dalam bentuk token. \
            Kemudian program akan menghasilkan struktur data dalam bentuk pohon uraian yang akan digunakan pada tahap kompilasi berikutnya, \
            yaitu analisis semantik.")
  st.write("-"*15)

def cek_kata(inputan) :
  kata = inputan.split()

  for i in kata :
    if i not in terminals :
      return False
      
  return True

def cek_kalimat(inputan) :
  S = ["ang", "inyo", "den"]
  V = ["lolok", "poi", "bakojo", "manunggu", "ngambiok", "ngajau"]
  O = ["sonduok", "oto", "lawuok", "guntiong", "pinggan"]

  kata = inputan.split()

  status = True
  
  i = 0
  cek = ((i + 1) - (3 * i))

  while i < len(kata) and status :
    if cek == 1 :
      if kata[i] not in S :
        status = False
    if cek == 2 :
      if kata[i] not in V :
        status = False
    if cek == 3 :
      if kata[i] not in O :
        status = False

    i += 1
    cek = ((i + 1) - (3 * i))

  return status

if __name__ == "__main__" :
  #symbols definition
  non_terminals = ["S", "SB", "VB", "OB"]
  terminals = [
               "ang", "inyo", "den",
               "lolok", "poi", "bakojo", "manunggu", "ngambiok", "ngajau",
               "sonduok", "oto", "lawuok", "guntiong", "pinggan"
              ]

  st.markdown("<h1 style='text-align: center; color: #a89932;'>Lexical Analysis and Parser</h1>", unsafe_allow_html=True)
  st.markdown("<h3 style='text-align: center; color: #ffffff;'>Bahasa Ocu</h3>", unsafe_allow_html=True)
  st.markdown("<h6 style='text-align: center; color: #ffffff;'>grammar = [subject] [verb] [object]</h6>", unsafe_allow_html=True)

  st.write("<subject> := ang | inyo | den")
  st.write("<verb> := lolok | poi | bakojo | manunggu | ngambiok | ngajau")
  st.write("<object> := sonduok | oto | lawuok | guntiong | pinggan")

  sentence = st.text_input("", placeholder="Input here!")
  input_string = sentence.lower() + "#"
  
  if st.button("Submit") :
    if sentence == "" :
      st.warning("Need input!")
    else :
      if cek_kalimat(sentence) :
        st.success("VALID")
      else :
        st.error("Invalid input.")

  if st.checkbox("Show Lexical Analysis") :
    if sentence == "" :
      st.warning("Need input!")
    else :
      if cek_kata(sentence) :
        defLexicalAnalysis()
        LexicalAnalysis(sentence)
      else :
        st.info("The input is not in the word list.")

  if st.checkbox("Show Parser") :
    if sentence == "" :
      st.warning("Need input!")
    else :
      if cek_kata(sentence) and cek_kalimat(sentence) :
        defParser()
        Parser(sentence)
      else :
        st.info("There is a grammatical error in the input.")

