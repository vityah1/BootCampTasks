# lib for work with authors notes

import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()


def DoMenu():
    def Menu():
        print (f'''Input:\n1 - list authors\n2 - create note\n3 - print notes\n4- Get author with the highest rating\n5 - Get author with the lowest rating\n6 - Get average rating among all authors\n0 - Exit''')

    loop=True
    while loop:
        Menu()
        v=input()
        print (f'''you input: {v}\n''')

        try:
            v=int(v)
        except:
            print ('wrong input!\n')
            exit()    

        if v==1:
            c.execute("select * from authors")
            print(c.fetchall())
            print ('\n')
        elif v==2:
            author=input('input author: ')
            note=input('input note: ')
            rate=input('input rate [0,1]: ')

            try:
                rate=int(rate)
            except:
                print ('wrong input!\n')
                exit()     
            if rate not in [1,0]:
                print ('wrong input! rate must be only 1 or 0\n')
                exit()     

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
            print ('wrong input!\n')
    return v

DoMenu()
conn.close()