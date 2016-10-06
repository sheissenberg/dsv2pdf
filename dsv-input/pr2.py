import csv

def read_csv(path = ''):
    file = csv.reader(open(path, 'r'))
    a = []
    for spam in file:
        a.append(spam)
    print a
    #retirn a
        
                    
p = 'test.csv'
read_csv(p)
