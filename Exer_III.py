def value_counts(a_list, out_path):
    import csv
    unique_el = [] 
    el_count = [] 
    a_list.sort()
    
    for element in a_list:
        
        if element not in unique_el:
            unique_el.append(element)
            el_count.append(1)
        else:
            el_count[unique_el.index(element)] += 1        
    
    with open(out_path, 'w') as out_file:
        csv_writer = csv.writer(out_file, delimiter = ',')
        
        for element in range(len(unique_el)):
            csv_writer.writerow([unique_el[element],el_count[element]])
            
            
def is_subset(sublist, superlist, strict=True):
    if strict:
        if sublist[0] not in superlist:
            return False
        else:
            indexes = [superlist.index(element) for element in sublist]
            return (sorted(indexes) == list(range(min(indexes),
                                                  max(indexes)+1)))
    else:
        return set(sublist).issubset(set(superlist))
    

def has_duplicates(a_list):
    unique_list = []
    for i in a_list:
        if i not in unique_list:
            unique_list.append(i)
    if len(a_list) > len(unique_list):
        return True
    else:
        return False

    
def count_words(input_file, output_file):
    
    import pickle
    
    in_file = open(input_file, "r")
    read_in = in_file.read()
    read_lower = read_in.lower()
    clean_in = read_lower.split()
    count = {i : clean_in.count(i) for i in clean_in}
    in_file.close()

    out_file = open(output_file, 'wb')
    pickle.dump(count, out_file)
    out_file.close()
    
    
class Person:
    def __init__(self, pos=(0,0), infected=False):
        self.x = pos[0]
        self.y = pos[1]
        self.infected = infected
    
    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
        
    def get_position(self):
        return (self.x,self.y)
    
    def is_infected(self):
        return self.infected
    
    def set_infected(self):
        self.infected = True
        
    def get_infected(self, person, thresh):
        euc_distance = ((person.x - self.x)**2 + (person.y - self.y)**2)**1/2
        if (person.infected) and (euc_distance < thresh):
            self.infected = True
      
    
class QuarantinedPerson(Person):
    def move(self, dx=0, dy=0):
        pass
    
    
def file_lines(**kwargs):
    
    val_dict = {}
    
    for i in kwargs:
        try:        
            file_path = open(kwargs.get(i), 'r')
            val_dict[i] = len(file_path.readlines())
        except:
            pass
                
    return val_dict


class TenDivError(Exception):
    def __init__(self, msg):
        super().__init__(msg)

def ten_div(num,den):
    try:
        if(num > 0) and  (num <= 10):
            return num / den
        else:
            raise TenDivError('Error encountered')
    except Exception as e:
        raise TenDivError(f'Error encountered: {e}')
        
        
import imp
imp.reload(wordfreq)
           
with open('wordfreq.py', 'w') as f:

    function = """
def most_frequent(file_path):
    
    file = open(file_path, 'r')
    word_list = "".join(file.read())
    word_lower = word_list.lower()
    word_split = word_lower.split()           
    tup_list = [(x,word_split.count(x)) for x in set(word_split)]       
    tup_list.sort(key = lambda x: (-x[1],x[0]))                            
    return [x[0] for x in tup_list[:9]]   
"""        

    f.write(function)

