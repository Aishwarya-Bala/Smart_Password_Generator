import GeneratePassword
from GeneratePassword import *
import random, string
from entropy import PasswordStrength

myrg = random.SystemRandom()

DEBUG2 = False

def debug2(msg):
    if(DEBUG2):
        print(msg)

alphabets = string.ascii_letters
alphanumeric  = string.ascii_letters + string.digits
alphanumeric_character  = string.ascii_letters + string.digits +  string.punctuation


rules = ['Shit', Rule1, Rule2, Rule3, Rule4, Rule5, Rule6, Rule7, Rule8, Rule9, Rule10, Rule11, Rule12, Rule13, Rule14, Rule15, Rule16, Rule17, Rule18, Rule19, Rule20, Rule21, Rule22, Rule23, Rule24, Rule25, Rule26, Rule27, Rule28, Rule29, Rule30, Rule31, Rule32, Rule33, Rule34, Rule35]
charset = [alphabets, alphanumeric, alphanumeric_character]

names = ['alphabets', 'alphanumeric', 'alphanumchar']

values = {}

for length in [5,7,10,12]:
    #print('\t\tPassword generation of length - '+str(length))
    for k in [0, 1, 2]:
        if(k == 0):
            debug2('\n' + ('*' * 75))
            debug2("\nPassword containing only alphabets -- length = " + str(length))
            debug2('\n' + ('*' * 75))
        elif(k == 1):
            debug2('\n' + ('*' * 75))
            debug2("\nPassword containing alphanumeric characters -- length = " + str(length))
            debug2('\n' + ('*' * 75))
        else:
            debug2('\n' + ('*' * 75))
            debug2("\nPassword containing alphanumeric + punctuation characters -- length = " + str(length))
            debug2('\n' + ('*' * 75))

        debug2('\n\n\tPassword\t\t\tENTROPY\n')
        ent_sum = 0
        for j in range(10):
            # generating a random password of lenngth = length of
            # a particular class -- alphabets/alphanumeric/alphanumeric_character
            pw = str().join(myrg.choice(charset[k]) for _ in range(length))

            if(j % 100 == 0):
                #print(j, '/', 1000)
                pass
            passy = PasswordStrength()
            ent = passy.calculate_entropy(password = pw)

            ent_sum += ent

            debug2("\t" + pw + '\t\t\t' + str(ent))
            string = '\t' + names[k] + ' \t\t' + str(length) + '\t\t\t'
            values[string] = ent_sum / 10

print("\n")
print("$" * 75)
print("\n")
print('\t' + "CLASS" + ' \t\t\t' + "LENGTH" + '\t\t\tENTROPY\n')
for k, v in values.items():
    print(k + str(v))
print("\n")
print("$" * 75)
print('\n')

values2={}

def strengthen(pw):
    user_pass = pw

    # We give a random number sequence to the user indicating the positions at which
    # tweaking should be done to the base password incase that rule is applied to the password

    # The length the sequence is limited to be 3 - 7
    user_sequence_length = (random.randint(3, random.randint(3, 7)))

    GeneratePassword.times = (user_sequence_length % 3) + 1

    GeneratePassword.symbol = gimme_special_symbol()
    #print("symbol : ", GeneratePassword.symbol)
    # We now generate the sequence of random numbers
    GeneratePassword.seq = [random.randint(1, len(user_pass)-1) for i in range(user_sequence_length)]
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

    # l = [6,11,5,1,2,3,12]
    times = 2
    prev_length = len(user_pass)
    for i in l:
        ends = rules[i](ends)

        if (len(GeneratePassword.seq) != user_sequence_length):
            # print("SEQUENCE HAS BEEN MODIFIED!!!")
            # exit(0)
            pass
        if (len(ends) < prev_length):
            # print("PASSWORD LENGTH HAS BEEN REDUCED!!!")
            # print("RULE", i, sep = "")
            # exit(0)
            pass

    ends = Rule18(ends)
    # print(ends)
    return (ends, to_remember)

for length in [5, 7, 10, 12]:
    #print('\t\tPassword generation of length - '+str(length))
    for k in [0, 1, 2]:
        #print('\t\tPasswords of '+(names[k])+' set')
        if(k == 0):
            debug2('\n' + ('*' * 75))
            debug2("\nBASE Password containing only alphabets -- length = " + str(length))
            debug2('\n' + ('*' * 75))
        elif(k == 1):
            debug2('\n' + ('*' * 75))
            debug2("\nBASE Password containing alphanumeric characters -- length = " + str(length))
            debug2('\n' + ('*' * 75))
        else:
            debug2('\n' + ('*' * 75))
            debug2("\nBASE Password containing alphanumeric + punctuation characters -- length = " + str(length))
            debug2('\n' + ('*' * 75))

        ent_sum = 0
        total = 10
        for j in range(10):
            pw = str().join(myrg.choice(charset[k]) for _ in range(length))
            newpass, hexseq = strengthen(pw)
            # if(j%100==0):
            # print(newpass)
            passy = PasswordStrength()
            try:
                ent = passy.calculate_entropy(password=newpass)
                ent_sum += ent
            except:
                ent = "nan"
                total -= 1
            base_ent = passy.calculate_entropy(password=pw)
            debug2("\tBase password -> " + pw + "\n\tBase Entropy -> " + str(
                base_ent) + '\n\tModified password -> ' + newpass + '\n\tHexCode -> ' + str(
                hexseq) + '\n\tEntropy -> ' + str(ent))
            debug2("-" * 75)
        string = '\t' + names[k] + ' \t\t' + str(length) + '\t\t\t'
        values2[string] = ent_sum / total

print("\n")
print("$" * 95)
print("\n")
print('\t' + "CLASS" + ' \t\t\t' + "LENGTH" + '\t\t\tENTROPY-Random'+'\t\tENTROPY-Smartpassword\n')
for k, v in values.items():
    for x,z in values2.items():
        if(k==x):
            print(k + str(v) +'\t'+ str(z))
print("\n")
print("$" * 95)
print('\n')