from collections import defaultdict
from heapq import *

def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))

    q, seen = [(0,f,())], set()
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (cost+c, v2, path))

    return float("inf")

def pathFind(start,end):
    out = dijkstra(edges, start, end)
    aux=[]
    while len(out)>1:
        aux.append(out[0])
        out = out[1]
    aux.reverse()
    print (aux)
    

edges = [
    ("One","Two",10),
    ("Two","Three",3),
    ("Two","Nine",10),
    ("Three","Four",10),
    ("Four","Five",3),
    ("Four","Twentyfive",10),
    ("Four","Nineteen",10),
    ("Five","Six",10),
    ("Six","Seven",3),
    ("Seven","Eight",10),
    ("Eight","One",3),
    
    
    ("Nine","Ten",10),
    ("Ten","Eleven",3),
    ("Eleven","Twelve",10),
    ("Twelve","Thirteen",3),
    ("Twelve","Twentyseven",10),
    ("Thirteen","Fourteen",10),
    ("Fourteen","Fifteen",3),
    ("Fourteen","Five",10),
    ("Fourteen","Nineteen",10),
    ("Fifteen","Sixteen",10),
    ("Sixteen","Nine",3),
    
    ("Seventeen","Eighteen",10),
    ("Eighteen","Nineteen",3),
    ("Eighteen","Twentyfive",10),
    ("Eighteen","Fifteen",10),
    ("Nineteen","Twenty",10),
    ("Twenty","Thirtythree",10),
    ("Twenty","Thirty",10),
    ("Twentythree","Twentyfour",10),
    ("Twentyfour","Seventeen",3),
    ("Twentyfour","Seven",10),
    
    ("Twentyfive","Twentysix",10),
    ("Twentysix","Twentyseven",3),
    ("Twentyseven","Twentyeight",10),
    ("Thirtyone","Thirtytwo",10),
    ("Thirtytwo","Twentyfive",3),
    ("Thirtytwo","Fifteen",10),
    ("Twentyeight","Thirtynine",10),
    
    ("Thirty","Twentynine",10),
    ("Twentynine","Thirtynine",3),
    ("Thirtynine","Fourty",10),
    ("Fourty","Fourtyone",3),
    ("Fourtyone","Fourtytwo",10),
    ("Fourtytwo","Fourtythree",3),
    ("Fourtytwo","Thirtyfive",10),
    ("Fourtythree","Fourtyfour",10),
    ("Fourtyfour","Thirty",3),
    ("Fourtyfour","Thirtyone",10),


    ("Twentytwo","Twentyone",10),
    ("Twentyone","Thirty",10),
    ("Twentyone","Thirtythree",3),
    ("Thirtythree","Thirtyfour",10),
    ("Thirtyfour","Thirtyfive",3),
    ("Thirtyfive","Thirtysix",3),
    ("Thirtysix","Thirtyseven",3),
    ("Thirtyseven","Thirtyeight",10),
    ("Thirtyeight","Twentytwo",3),
    ("Thrityeight","Twentythree",10)
]

print ("=== Dijkstra ===")
#print (edges)
#print ("A -> E:")
#print (dijkstra(edges, "A", "E"))
#print ("F -> G:")
#print (dijkstra(edges, "F", "G"))
pathFind('One', 'Fourtyone')
