# 1.Գրել  ծրագիր  որ  կստուգի  թե արդյոք ճիշտ է  թե  սխալ  ձեր մուտքագրած  String-ը  pangram  է, pangram-ը  է կոչվում երբ լատինատառ տառերի ամբողք քանակն  առանց  կրկնվելու

def check_pangram(input_str: str = "The quick brown fox jumps over the lazy dog",) -> bool:

    frequency = set()
    input_str = input_str.replace(" ", "")
    for alpha in input_str:
        if "a" <= alpha.lower() <= "z":
            frequency.add(alpha.lower())
    if len(frequency) == 26:
        return True
    else:
        return False


print(check_pangram())

# Գրել  ծրագիր  որ կհամեմատի երկու
# տողերը  և կվերադարձնի 0 եթե երկուսն էլ
# նույն տողերն  են  ,եթե  չէ  կվերադարձնի
# երկու տողերի  տարբերությունը, եթե  տողերը
# իրար  հավասար չեն   կվերադարձնի -1


def hamming_distance(string1: str, string2: str) -> int:
    # >>> hamming_distance("python", "python")
    # 0
    # >>> hamming_distance("karolin", "kathrin")
    # 3
    # >>> hamming_distance("00000", "11111")
    # 5
    # >>> hamming_distance("karolin", "kath")
    # Traceback (most recent call last):
    #   ...
    # ValueError: String lengths must match!

    if len(string1) != len(string2):
        raise ValueError("String lengths must match!")
    count = 0
    #
    # for char1, char2 in (string1, string2):
    #     if char1 != char2:
    for i , j in zip(string1,string2):
        if i != j:
            count += 1

    return count

print(hamming_distance("python","kathri"))



# Գրել  ծրագիր  որը կստուգի տողը Պալինդրոմ է
# ,օրինակ ՝ "a man a plan a canal panama" այս
# տողը ինձ պիտի վերադարձնի True



def is_palindrome(s: str) -> bool:
    # """
    # Determine whether the string is palindrome
    # :param s:
    # :return: Boolean
    # >>> is_palindrome("a man a plan a canal panama".replace(" ", ""))
    # True
    # >>> is_palindrome("Hello")
    # False
    # >>> is_palindrome("Able was I ere I saw Elba")
    # True
    # >>> is_palindrome("racecar")
    # True
    # >>> is_palindrome("Mr. Owl ate my metal worm?")
    # True
    # """
    # Since Punctuation, capitalization, and spaces are usually ignored while checking
    # Palindrome,  we first remove them from our string.
    s = "".join([character for character in s.lower() if character.isalnum()])
    return s == s[::-1]

# print(is_palindrome("Able was I ere I saw Elba"))

s = input("Enter string to determine whether its palindrome or not: ").strip()
if is_palindrome(s):
        print("Given string is palindrome")
else:
        print("Given string is not palindrome")


# 5.Գրել ֆունկցիա  որ կստանա երկու տող ,առաջին
# արգումենտը կհամեմատի երկրորդի հետ  ,եթե
# երկրորդ արգումենտի արժեքները  պարնակվում են
# առաջինի մեջ ,վերադարձնի ,այդ դիրքում գտնվող
# առաջին ինդեքսները ,օրինակ ՝ ABAAABCDBBABCDDEBCABC",
# "ABC"  վերադարձնի  [4, 10, 18] ,եթե չի պարնակում ուրեմն
# թող վերադարձնի դատարկ list
#
def naive_pattern_search(s: str, pattern: str) -> list:
    # """
    # >>> naive_pattern_search("ABAAABCDBBABCDDEBCABC", "ABC")
    # [4, 10, 18]
    # >>> naive_pattern_search("ABC", "ABAAABCDBBABCDDEBCABC")
    # []
    # >>> naive_pattern_search("", "ABC")
    # []
    # >>> naive_pattern_search("TEST", "TEST")
    # [0]
    # >>> naive_pattern_search("ABCDEGFTEST", "TEST")
    # [7]
    # """
    pat_len = len(pattern)
    position = []
    for i in range(len(s) - pat_len + 1):
        match_found = True
        for j in range(pat_len):
            if s[i + j] != pattern[j]:
                match_found = False
                break
        if match_found:
            position.append(i)
    return position

print(naive_pattern_search("ABAAABCDBBABCDDEBCABC", "ABC"))




# 6.Գրել ծրագիր որ  կստանա տող ,և կշրջի բոլոր  բառերը տողի մեջ։

def reverse_letters(input_str: str) -> str:
        # """
        # Reverses letters in a given string without adjusting the position of the words
        # >>> reverse_letters('The cat in the hat')
        # 'ehT tac ni eht tah'
        # >>> reverse_letters('The quick brown fox jumped over the lazy dog.')
        # 'ehT kciuq nworb xof depmuj revo eht yzal .god'
        # >>> reverse_letters('Is this true?')
        # 'sI siht ?eurt'
        # >>> reverse_letters("I   love       Python")
        # 'I evol nohtyP'
        # """

        return " ".join([word[::-1] for word in input_str.split()])

print(reverse_letters("i love python"))



 # 7.  # Գրել ծրագիր, որ վերադարձնում
# է տրված  տողը՝ “cat” այսպես[“Cat”, ”cAt”, ”caT”], բոլոր
# հնարավոր տաբերակներով


def wave(txt: str) -> list:
        # """
        # Returns a so called 'wave' of a given string
        # >>> wave('cat')
        # ['Cat', 'cAt', 'caT']
        # >>> wave('one')
        # ['One', 'oNe', 'onE']
        # >>> wave('book')
        # ['Book', 'bOok', 'boOk', 'booK']
        # """

        return [
            txt[:a] + txt[a].upper() + txt[a + 1:]
            for a in range(len(txt))
            if txt[a].isalpha()
        ]

print(wave("cat"))



item = []
def Stack(func):
    def st(*args):
        print("Function that started running is " + func.__name__)
        func(*args)
    return st

@Stack
def push(*it):
    item.append(it)
    return item
@Stack
def pop():
    if len(item) == 0:
        return  print("Stack is empty")
    else:
        return item.pop()
@Stack
def peek():
    return item[-1]
@Stack
def size():
    print(len(item))
@Stack
def isEmpty():
    if len(item) == 0:
         print(True)
    print(False)
@Stack
def clear():
    global item
    item = []
@Stack
def top():
    print(item[0])

@Stack
def show():
    for x in item:
        print(x,end=" ||  \n" )
    if len(item) == 0:
        print(item)

push(1)
push(":qwasdSz")
pop()
push('asds')
top()
isEmpty()
clear()
size()
pop()
push("dsazdxas",44,14)
show()