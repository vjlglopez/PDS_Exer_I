def digit_sum(number):
    nums = str(number)
    num_list = []
    for el in nums:
        num_list.append(int(el))
    return sum(num_list)


def count_vowels(text):
    z = list(text)
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_list = []
    for el in z:
        if el in vowels:
            vowel_list.append(el)
        else:
            pass
    return len(vowel_list)


def is_interlock(word_list, word1, word2):
    '''
    Check if word1 and word2 interlocks based on word_list

    Two words "interlock" if taking alternating letters from each forms a new 
    word. For example, "shoe" and "cold" interlock to form "schooled".
    
    
    Parameters
    ----------
    word_list : list
        List of valid words
    word1 : string
        First word to check
    word2 : string
        Other word to check
        
        
    Returns
    -------
    interlockness : bool
        True if `word1` and `word2` interlock
    '''
    if len(word1) != len(word2):
        return False
    else:
        i =0
        interlock1 = ''
        interlock2 = ''
        for i in range(len(word1)):
            interlock1 += word1[i] + word2[i]
            
        for i in range(len(word2)):
            interlock2 += word2[i] + word1[i]
        
        if interlock1 in word_list or interlock2 in word_list:
            return True
        else:
            return False
        
        
def count_types(a_string):
    x = list(a_string.lower())
    y = list(a_string.upper())
    z = [' ', '\n']
    p = ('!', "," ,"\'" ,";" ,"\"", ".", "-" ,"?" )
    n = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    lower_list = []
    upper_list = []
    whitespace_list = []
    punctuation_list = []
    number_list = []
    for el in a_string:
        if el in p:
            punctuation_list.append(el)
        elif el in n:
            number_list.append(el)
        elif el in z:
            whitespace_list.append(el) 
        elif el in x:
            lower_list.append(el)
        elif el in y:
            upper_list.append(el)

    d = {'lowercase': len(lower_list),
         'uppercase': len(upper_list),
         'numeric': len(number_list),
         'punctuation': len(punctuation_list),
         'whitespace': len(whitespace_list)}
    
    return d


def matmul(mat1, mat2):
    
    def sum_of_product(A, B):
        result = 0
        for i in range(len(A)):
            result += (A[i] * B[i]) 
        return result

    output = []
    for mat1_row in mat1:
        sublist = []
        for i in range(len(mat2[0])):
            mat2_col = [j[i] for j in mat2]
            sublist.append(sum_of_product(mat1_row, mat2_col))
        output.append(sublist)
    
    return output


def encode(text):
    grid = int(len(text)**(1/2)) + 1

    rows = []
    for row in range(grid):
        pos = row * grid
        code = text[pos:pos + grid]
        rows.append(code)
    
    coded = ""
    for col in range(grid):
        for row in range(grid):
            if col < len(rows[row]):
                coded += rows[row][col]
        coded += " "

    return coded.rstrip()


def check_brackets(str_with_brackets):
    """Check whether str_with_bracks is bracketed correctly
    
    Parameters
    ----------
    str_with_brackets : str
        String with brackets that are possibly nested
    
    Returns
    -------
    is_correct : bool
        `True` if `str_with_brackets` is bracketed correctly, `False` 
        otherwise
    """
    brackets = [['(',')'], ['[',']'], ['{','}'], ['<','>']]
    b_open = [b[0] for b in brackets]
    b_close = [b[1] for b in brackets]
    
    b_sequence = []
    x = ([b_sequence.append(el) for el in str_with_brackets
          if el in b_close or el in b_open])
            
    fin_seq = ''.join(b_sequence)     
    
    for el in range(len(fin_seq)):
        if '()' in fin_seq:
            fin_seq = fin_seq.replace('()', '')
        elif '[]' in fin_seq:
            fin_seq = fin_seq.replace('[]', '')
        elif '{}' in fin_seq:
            fin_seq = fin_seq.replace('{}', '')
        elif '<>' in fin_seq:
            fin_seq = fin_seq.replace('<>', '')

    if len(fin_seq) == 0:
        return True
    else:
        return False
    
    
def nested_sum(list_of_lists):
    numlist = []
    for element in list_of_lists:
        for el in element:
            numlist.append(el)
    return sum(numlist)


def count_people(log):
    
    #clean the data first and extract list and count
    x_joined = list(log)
    w = ''.join(x_joined)
    y = w.replace('\t', '')
    z = y.split('\n') #list to be used
    nums1 = y.replace('IN', '')
    nums2 = nums1.replace('OUT', '')
    num_list = nums2.split('\n') #count to be used
    
    #remove empty string from list and create a list of numbers for range
    counts = num_list[:-1]
    total = []
    for el in counts:
        total.append(int(el))
    
    counter_in = []
    counter_out = []
    i = 1
    for i in range(0, max(total) + 1):
        inside = z.count('IN' + str(i))
        counter_in.append(inside)
    for i in range(0, max(total) + 1):
        outside = z.count('OUT' + str(i))
        counter_out.append(outside)
        
    g_in = 0
    g_out = 0
    for i in range(len(counter_in)):
         g_in += counter_in[i] * i
    for i in range(len(counter_out)):
         g_out += counter_out[i] * i
    
    return g_in - g_out


def next_word(text, word=None):
    """
    Return the most likely next word in text
    
    A word is defined as a sequence of all non-whitespace characters between
    whitespaces. Words are case-insensitive.
    
    Parameters
    ----------
    text : string
        Text to train at.
    word : string or `None`
        Find the most likely next word of `word` or likely next word of all
        words if `None`. 
        
    
    Returns
    -------
    next_word : tuple or list of tuple
        If `word` is a string then return the most likely next word of `word`
        as a tuple of `(word, most_likely_next_word)`. If `word` is not found
        in `text`, `most_likely_next_word` is an empty string. If `word` is
        `None` then return the list of `(word, most_likely_next_word)` for all
        words in `text`. If there is more than one most likely next word, pick
        the first word based on alphabetical (lexicographic) order.
    """ 
    from collections import Counter
    
    text_list = text.split()
    unique_texts = set(text_list)
    word_out = []
    
    for w in unique_texts:
        target = w
        words_after_target = []
        for i, t in enumerate(text_list[:-1]):
            if t == target:
                words_after_target.append(text_list[i+1])

        sorted_count = (sorted(Counter(words_after_target).items(),
                               key=lambda x: (-1 * x[1], x[0])))
        next_word = sorted_count[0][0]
        word_out.append((target, next_word))

    if word:
        for w_tuple in word_out:
            if w_tuple[0] == word:
                return w_tuple
    else:
        return word_out

