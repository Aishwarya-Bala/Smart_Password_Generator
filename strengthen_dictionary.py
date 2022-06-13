import GeneratePassword
from GeneratePassword import *
import random, string
from entropy import PasswordStrength
from tqdm import tqdm

rules = ['Shit', Rule1, Rule2, Rule3, Rule4, Rule5, Rule6, Rule7, Rule8, Rule9, Rule10, Rule11, Rule12, Rule13, Rule14, Rule15, Rule16, Rule17, Rule18, Rule19, Rule20, Rule21, Rule22, Rule23, Rule24, Rule25, Rule26, Rule27, Rule28, Rule29, Rule30, Rule31, Rule32, Rule33, Rule34, Rule35]

def strengthen(pw):
    user_pass = pw

    # We give a random number sequence to the user indicating the positions at which
    # tweaking should be done to the base password incase that rule is applied to the password

    # The length the sequence is limited to be 3 - 7
    user_sequence_length = (random.randint(3, random.randint(3, 7)))

    GenPass.times = (user_sequence_length % 3) + 1

    GenPass.symbol = gimme_special_symbol()
    #print("symbol : ", Genpass.symbol)
    # We now generate the sequence of random numbers
    GenPass.seq = [random.randint(1, len(user_pass)-1) for i in range(user_sequence_length)]
    #print("seq =", seq)

    num_rules = (random.randint(5, random.randint(5, 8)))

    l = [random.randint(1, 35) for i in range(num_rules)]


    def map_func(x):
        if(len(str(x)) == 1):
            return '0' + str(x)
        else:
            return str(x)

    l1 = list(map(map_func, l))

    num = ''.join(l1)

    to_remember = int2base32(int(num))


    # Cascade apply the rules
    ends = user_pass

    #l = [6,11,5,1,2,3,12]
    times = 2
    prev_length = len(user_pass)
    for i in l:
        ends = rules[i](ends)

        if(len(GenPass.seq) != user_sequence_length):
            #print("SEQUENCE HAS BEEN MODIFIED!!!")
            #exit(0)
            pass
        if(len(ends) < prev_length):
            #print("PASSWORD LENGTH HAS BEEN REDUCED!!!")
            #print("RULE", i, sep = "")
            #exit(0)
            pass

    ends = Rule18(ends)
    #print(ends)
    return (ends, to_remember)

def function():
    #print("FUNCTION2")
    with open("realhuman_phill.txt", 'r', encoding = "latin-1") as f:
        dicti = f.readlines()

    base_ent = 0
    ent = 0
    total = 0
    total2 = 0
    for i in tqdm(range(len(dicti))):
        (p, h) = strengthen(str(dicti[i].strip().encode("utf-8")))
        print("Base_Pass : " + str(dicti[i].strip().encode("utf-8")) + "\nSecret_Code : " + h + "\nModified Pass : " + p, end = "")
        passy = PasswordStrength()
        try:
            entr = passy.calculate_entropy(password = p)
            ent += entr
        except:
            entr = "nan"
            total += 1
        try:
            base_entr = passy.calculate_entropy(password = str(dicti[i].strip().encode("utf-8")))
            base_ent += base_entr
        except:
            base_entr = "nan"
            total2 += 1
        print("\nBase Password Entropy : " + str(base_entr) + "\nSyphered Password entropy : " + str(entr))
        print("_" * 90)

    print("\n\n")
    print("Average Entropy of Dictionary passwords = ", base_ent / (len(dicti) - total2))
    print("Average Entropy of syphered Dictionary passwords = ", ent / (len(dicti) - total))


function()