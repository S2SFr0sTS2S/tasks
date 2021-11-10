#реализовать встроенные функции bin
def get_bin(numb):
    bin_str = ''
    while numb > 0:
        bin_str = str(numb % 2) + bin_str
        numb = numb // 2
    return('bin',bin_str)



#реализовать встроенные функции hex
def get_hex(numb):
    hex_str = ''
    hex_digits ={
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }

    while numb > 0:
        digit = numb % 16
        if digit >= 10:
            digit = hex_digits[digit]
        hex_str = str(digit) + hex_str    
        numb = numb // 16
    return('hex',hex_str)



#написать функцию, которая возвращает его представление в n-ичной
def get_anoth(numb,notat):
    an_str = ''
    abc = ''
    while numb > 0:
        digit = numb % notat
        if digit >= 10:
            abc = chr(digit-10 + ord('A'))
            digit = abc
        an_str = str(digit) + an_str    
        numb = numb // notat
    return('число в',notat,'системе счисления',an_str)




#сумму всех элементов (реализовать встроенную функцию sum)
def get_sum_numb(numbers):
    sum_prev = 0
    for numb in numbers:
        sum_prev = sum_prev + numb
    return sum_prev
numbers = [1,5,5,4,10,6] #1 4 5 5 6 10
print('Сумма',get_sum_numb(numbers))



#максимальный элемент (реализовать встроенную функцию max)
def get_max_numb(numbers):
    max_numb = 0
    cur_numb = 0
    for numb in numbers:
        cur_numb = numb
        if cur_numb > max_numb:
            max_numb = cur_numb
    return max_numb
print('Максимальный элемент',get_max_numb(numbers))



#среднее арифметическое
def get_average(numbers):
    amount = 0
    average = 0
    for numb in numbers:
        amount = amount + 1
    average = get_sum_numb(numbers) / amount
    return average
print('Среднее арифмитическое',get_average(numbers))



#медианное значение (указание: предварительно упорядочить c помощью mylist.sort())
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
print('медианое значение',get_med_numb(numbers))



#Дано 2 упорядоченных списка. Объединить их в один упорядоченный список.
#Указание: встроенная функция sort ухудшает алгоритмическую сложность и ее использовать в данной задаче нельзя.
arr_2 = [0,1,4]
arr_1 = [2,6,8,9,15,624,72]
def get_unite_arr(f_arr, s_arr):
    new_arr = []
    arr = f_arr + s_arr
    while arr:
        new_arr.append(arr.pop(arr.index(min(arr))))
    return new_arr

print('объединнеый список',get_unite_arr(arr_1,arr_2))



#самое длинное слово
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
print('самое длинное слово',word_ml)



#список слов короче N букв
def get_n_letter_words(words,n):
    _n_letter_words = []
    for word in words:
        curlen = len(word)
        if curlen < n:
            _n_letter_words.append(word)
    return _n_letter_words
print(get_n_letter_words(words,5))



#2 списка: слова на гласную и согласную буквы
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
print("гласные и согласные" ,vow_and_cons(words))



#количество уникальных слов в строке 
string = 'Hello how do you do fellow! man are you okay you you you dude'
def numb_words(string):
    jour = {}
    spl = string.split()
    test = []
    for word in spl:
        jour[word] = spl.count(word)
    return len(jour)
print('уникальных слов',numb_words(string))            
    


#превратить в заголовок ('the best' -> 'The Best') (реализовать встроенный метод title)
string = 'thE best PRO mlG 322 2D3c'
def switсh_register(string):
    shft = ord('A')-ord('a')
    arr_sent = string.split()
    size = len(arr_sent) 
    for word in range(size):
        f_let = arr_sent[word][0]
        w_size = len(arr_sent[word])
        arr_let = list(arr_sent[word])
        for let in range(w_size):
            
            if let == 0: 
                if ord(arr_let[let]) >= ord('a') and ord(arr_let[let]) <= ord('z'):
                    arr_let[let] = chr(ord(f_let) + shft)
                else:
                    let += let
                
            else:
                if ord(arr_let[let]) >= ord('A') and ord(arr_let[let]) <= ord('Z'):
                    arr_let[let] = chr(ord(arr_let[let]) - shft)
                else:
                    let += let
        
        arr_sent[word]=''.join(arr_let)           
    string = ' '.join(arr_sent)
    return string
        
print('Заголовок',switсh_register(string))



#заменить все гласные на звездочки (hello -> h*ll*)
string = 'hello fritnd add'
def star(string):
    vowels_tez = ('A', 'E', 'I', 'O', 'U', 'Y','a', 'e', 'i', 'o', 'u', 'y')
    for lett in string:
        if lett in vowels_tez:
            string = string.replace(lett,'*')
        else:
            pass
    return(string)
print("замена гласных на *",star(string))



#выбросить из нее все слова короче 4 букв
string = 'as hello fritnd add 1234 12 12 12345'
def long(string,n=4):
    stp = string.split()
    trash = get_n_letter_words(stp,n)
    for word in trash:
        stp.pop(stp.index(word))
    result = ' '.join(stp)
    return result
print(long(string))
    
    
    
#Реализовать функцию zip: из пары списков сделать список пар:
f_arr=[1,2,3]
s_arr=['a','b','c']
def get_zip(f_arr,s_arr):
    un_ar = []
    big_ar = []
    if len(f_arr)-len(s_arr) <= 0:
        size = len(f_arr)
    else:
        size = len(s_arr)
    for el in range(size):
        un_ar.append(f_arr[el])
        un_ar.append(s_arr[el])
        big_ar.append(un_ar)
        un_ar = []
    return big_ar 
        
print('zip',get_zip(f_arr,s_arr))




#дано натуральное число, вычислить простое ли оно или составное
numb = 997
def cas(numb):
    max_numb = int(numb ** 0.5)
    if numb == 2:
        return('Простое', numb)
    i = 2 
    while i <= max_numb:
        if numb % i == 0:
            return('Cоставное', numb)
        i += 1    
    return('Простое', numb)
print(cas(numb))



#вывести все простые числа от 2 до n
numb = 47
def cas_arr(numb):
    arr = []
    start = 2
    for start in range(numb + 1):
        if start < 2:
            pass
        elif cas(start) == ('Простое', start):
            arr.append(start)
        else:
            pass
    return(arr)
print(cas_arr(numb))

        

#Дано 2 списка: ключи и значения. Создать из них словарь.
arr1=[1,2,3]
arr2=['a','b','c']
def creat_tez(arr1,arr2):
    tez = {}
    if len(arr1) > len(arr2):
        steps = len(arr2)
    else:
        steps = len(arr1)
    for step in range(steps):
        tez[arr1[step]] = arr2[step]
    return(tez)
print('Словарь ',creat_tez(arr1,arr2))





        


