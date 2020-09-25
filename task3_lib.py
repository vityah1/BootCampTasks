# lib for work with authors notes

import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()

def myexit():
    print('Do Exit...')
    conn.close()
    exit()

def setup_database():
# Create table
    print ('Init...')
    try:
        c.execute('''CREATE TABLE authors
     (name text, note text, rating real)''')
    except:
        print ('Table exist!')
    print  ('Table check ok')

def DoMenu():
    def Menu():
        print (f'''MENU:\n1 - List authors\n2 - Create note\n3 - Print notes\n4 - Get author with the highest rating\n5 - Get author with the lowest rating\n6 - Get average rating among all authors\n0 - Exit''')

    loop=True
    while loop:
        Menu()
        v=input()
        print (f'''you input: {v}\n''')

        try:
            v=int(v)
        except:
            print ('wrong input!\n')
            myexit()    

        if v==1:
            c.execute("select * from authors")
            print(c.fetchall())
            print ('\n')
        elif v==2:
            author=input('Input author: ')
            note=input('Input note: ')
            rate=input('Input rate [0,1]: ')

            try:
                rate=int(rate)
            except:
                print ('Wrong input!\n')
                exit()     
            if rate not in [1,0]:
                print ('Wrong input! rate must be only 1 or 0\n')
                myexit()     

            c.execute(f'''INSERT INTO authors VALUES ('{author}','{note}',{rate}) ''')
            conn.commit()
            print (f'''{author}','{note}',{rate} added\n''')
        elif v==4:
            c.execute("select name,max(rating) from authors group by name limit 1")
            print(c.fetchall())
        elif v==5:
            c.execute("select name,min(rating) from authors group by name limit 1")
            print(c.fetchall())
        elif v==6:
            c.execute("select avg(rating) from authors")
            print(c.fetchall())

        elif v==0:
            print('Exit')
            loop=False
        else:
            print ('Wrong input!\n')
    return v

setup_database()
DoMenu()
myexit()
