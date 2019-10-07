# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 11:10:40 2019
@author: Sanjiv
@author: Manish
"""


f=open("words.txt", "r")

L = []
if f.mode == 'r':
    contents = f.read()
    L = contents.split(',')
    del[L[0]]
    L.insert(0,'i')
    L[len(L)-1] = 'kad'
    #print(len(L))

f.close()

f2 = open("doctest.txt", "r")


documents = {}

if f2.mode == 'r':
    contents = f2.read()
    documents_string = contents.strip().split()
#    print(documents_string[0])
    for s in documents_string:
        t = s.split(',')
        doc_id1 = t[0]
        doc_id2 = t[1]
        l = []
        l.append(t[0])
        l.append(t[1])
        words = {}
        del(t[0])
        del(t[0])
        for i in t:
            w_c = i.split(':')
            words[L[int(w_c[0])-1]] = int(w_c[1])
        l.append(words)
        documents[doc_id1] = l

#print(documents[0])
        
        
f2.close()  

word_hash = {}

for doc in documents:
    #print(documents[doc][2])
    for wd in documents[doc][2]:
        if wd not in word_hash:
            word_hash[wd] = []
            word_hash[wd].append((documents[doc][0],documents[doc][1],documents[doc][2][wd]))
        else:
            word_hash[wd].append((documents[doc][0],documents[doc][1],documents[doc][2][wd]))

def intersection2(List_of_lists): 
    temp = set(List_of_lists[0])
    for i in range(1,len(List_of_lists)):
        temp = (temp & set(List_of_lists[i]))
    return list(temp)

from lyricsToBow import input_to_bow
 
while(1):
    lyrics = input("Enter your Query (type QUIT to exit): ")
    if lyrics == "QUIT" :
        break
    print(lyrics)
    query = input_to_bow(lyrics)
    print(len(query))
    print(type(query))
    
    
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
    print(len(ans))
    
    doc_query_wdlist = []
    for doc_id in ans:
        query_wdlist =[]
        for wd in query:
            query_wdlist.append([wd, documents[doc_id][2][wd]])
        doc_query_wdlist.append([documents[doc_id][0], documents[doc_id][1], query_wdlist])
        
    print(len(doc_query_wdlist))
        