import googlesearch
import time
def init():    
    print("Finder")

    try: 
        from googlesearch import search 
    except ImportError:
        print("No module named 'google' found") 
    query = str(input(" "))
    
    for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
        print(j)
    a = input("- digite 's' para sair")
    if a == 's':
        exit()
    init()
init()