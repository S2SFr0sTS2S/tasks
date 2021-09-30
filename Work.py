def get_sum_numb(numbers):
    sum_prev = 0
    for numb in numbers:
        sum_prev = sum_prev + numb
    return sum_prev
numbers = [1,5,5,4,10,6] #1 4 5 5 6 10
print(get_sum_numb(numbers))

def get_max_numb(numbers):
    max_numb = 0
    cur_numb = 0
    for numb in numbers:
        cur_numb = numb
        if cur_numb > max_numb:
            max_numb = cur_numb
    return max_numb
print(get_max_numb(numbers))

def get_average(numbers):
    amount = 0
    average = 0
    for numb in numbers:
        amount = amount + 1
    average = get_sum_numb(numbers) / amount
    return average
print(get_average(numbers))

def get_med_numb(numbers):
    cur_numb = 0
    max_numb = 0
    amount = 0
    med = 0
    med_odd = 0
    men_numb = 0
    numbers.sort()
    amount = len(numbers)
    if amount % 2 == 0:
        med = amount // 2
        med_numb = numbers[med-1] + numbers[med]
        return med_numb
    else:
        med_odd = amount // 2
        med_numb = numbers[med_odd]
        return med_numb
print(get_med_numb(numbers))

arr_2 = [0,1,4]
arr_1 = [2,6,8,9,15,624,72]
def get_unite_arr(f_arr,s_arr):
    position = 0
    overage=[]
    arr_unite = []
    if len(s_arr) > len(f_arr):
        for numb in range(len(f_arr)):
            arr_unite.append (f_arr[position])
            arr_unite.append (s_arr[position])
            position += 1
        for numb in range(len(s_arr) - len(f_arr)):
            arr_unite.append(s_arr[position])
            position += 1 
        arr_unite.sort()
        print(arr_unite)
        return arr_unite
    else:
        overage = f_arr
        f_arr = s_arr
        s_arr = overage
        get_unite_arr(f_arr,s_arr) 
get_unite_arr(arr_1,arr_2)

def get_longest(words):
    word_maxlen = ''
    maxlen = 0
    for word in words:
        curlen = len(word)
        if curlen > maxlen:
            maxlen = curlen
            word_maxlen = word
    return word_maxlen

words = ['Hi', 'Hello34werf', '123456', 'q','12345','123','1234']
word_ml = get_longest(words)
print(word_ml)

def get_5_letter_words(words):
    _5_letter_words = []
    for word in words:
        curlen = len(word)
        if curlen<5:
            _5_letter_words.append(word)
    return _5_letter_words
print(get_5_letter_words(words))

words = ['Hi', 'Hello34werf', 'Auf', 'Arg','Dest','Unholy','Holy']
def vow_and_cons(words):
    vowels = []
    consonants = []
    vowels_tez = ('A', 'E', 'I', 'O', 'U', 'Y','a', 'e', 'i', 'o', 'u', 'y')
    for word in words:
        if word.startswith(vowels_tez):
            vowels.append(word)
        else:
            consonants.append(word)
    return vowels , consonants

print("vow_and_cons" ,vow_and_cons(words))

string = 'Hello how do you do fellow kids'
def numb_words(string):
    numb = len(string.split())
    print(numb)
    return numb
numb_words(string)

string = 'The best'
def switсh_register(string):
   # string.title()
   # print(string.title())
   words = string.split()
    
    letters = list(string)
    for word in words:
        letters = word.split()
        letters[0]
        print (letters[0])
   
    return letters
print(switсh_register(string))
