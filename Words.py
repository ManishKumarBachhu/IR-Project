#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 22:34:27 2019

@author: sanjivshenoy
"""


f=open("words.txt", "r")

L = []
if f.mode == 'r':
    contents = f.read()
    L = contents.split(',')
    del[L[0]]
    L.insert(0,'i')
    L[len(L)-1] = 'kad'
#    print(L)

f.close()

f2 = open("doctest.txt", "r")


documents = []
 
if f2.mode == 'r':
    contents = f2.read()
    documents_string = contents.strip().split()
#    print(documents_string[0])
    for s in documents_string:
        t = s.split(',')
        l = []
        l.append(t[0])
        l.append(t[1])
        words = []
        cnt = []
        del(t[0])
        del(t[0])
        for i in t:
            w_c = i.split(':')
            words.append(L[int(w_c[0])-1])
            cnt.append(int(w_c[1]))
        l.append(words)
        l.append(cnt)
        documents.append(l)

#print(documents[0])
        
        
f2.close()  
        
    
'''
Thinking 

L = [ list of [id, id2, [words], [cnts]] ] to {word: [list of [id,id2,cnt] ]}

'''

word_hash = {}

for i in range(len(documents)):
    for j in range(len(documents[i][2])):
        if documents[i][2][j] not in word_hash:
            word_hash[documents[i][2][j]] = []
            word_hash[documents[i][2][j]].append((documents[i][0],documents[i][1],documents[i][3][j]))
        else:
            word_hash[documents[i][2][j]].append((documents[i][0],documents[i][1],documents[i][3][j]))

#print(word_hash['colleg'])
            
'''
Final dictionary is word_hash
'''

query = ['cri','i','and']

'''
Thinking
List of lists of sizes n, n-1, n-2, .... 1
L = [ [ [DocID,mxmID,[word_cnt],[missing_words]], similar docs], similar lists] is required

'''

#def intersection(List_of_lists,Missing):
#    ans = []
#    for docs in List_of_lists[0]:
#        ID = docs[0]
#        cnt = 1
#        word_cnts = []
#        for j in range(1,len(List_of_lists)):
#            for k in range(len(List_of_lists[j])):
#                if(ID == List_of_lists[j][k][0]):
#                    cnt+=1
#                    word_cnts.append(List_of_lists[j][k][2])
#        if(cnt == len(List_of_lists)):
#            temp = [docs[0],docs[1],word_cnts,Missing]
#            ans.append(temp)
#    return ans

'''
test code for intersection(works on test data)

L1 = [[(1,2,3),(4,5,6),(7,8,9)],[(1,2,4),(4,5,7)],[(3,4,5),(4,5,7),(1,2,10)]]
ans = intersection(L1,['hello'])
print(ans)

Not working for actual data due to load I think 
'''
            
                    

'''
Another way to intersect lists

reference link for this and more methods
https://www.geeksforgeeks.org/python-intersection-two-lists/
'''

def intersection2(List_of_lists): 
    temp = set(List_of_lists[0])
    for i in range(1,len(List_of_lists)):
        temp = (temp & set(List_of_lists[i]))
    return list(temp)


List_of_list_of_documents = []

for i in range(len(query)):
    List_of_list_of_documents.append(word_hash[query[i]])


#Code to just take out the Doc IDs. 
L = []
for i in range(len(List_of_list_of_documents)):
    t = []
    for j in range(len(List_of_list_of_documents[i])):
        t.append(List_of_list_of_documents[i][j][0])
    L.append(t)

#ans = intersection2(List_of_list_of_documents)
ans = intersection2(L)

print("Top documents which contain all words are :")
print(len(ans))

'''
for doc_id in ans:
    for doc in documents:
        if doc_id == doc[0] :
            doc_id_wdlist = []
            query_word_counts = []
            for wd in query:
                ls = []
                for i in range(0, len(doc[2])):
                    if wd == doc[2][i]:
                        ls.append([doc[2][i], doc[3][i]])
                query_word_counts.append(ls)
            doc_id_wdlist.append([doc_id, query_word_counts])
'''

'''
if len(ans) > 10 :
    for i in range(10):
        print(ans[i])
else:
    for i in range(len(ans)):
        print(ans[i])
'''


































    