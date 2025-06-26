l = ['mango','banana','apricot','strawberry','blueberry']
l1=l.copy()
l.append('rasberry')
l2=l.copy()
l.remove('apricot')
l3=l.copy()
print(f"Original list: {l1} \nAfter adding a fruit: {l2} \nAfter removing a fruit: {l3} \nReversed list: {l[::-1]}")