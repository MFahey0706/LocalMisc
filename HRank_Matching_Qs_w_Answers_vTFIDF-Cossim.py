#Cosine similarity chain
#approach1: question similar to sentence; sentence similar to answer
#approach2: combine Q+A, choose combo with max possible cosine similarity to any sentence in passage
import re
import numpy as np
from math import log, sqrt

passage = [re.sub(r'([^\sA-Za-z0-9]|_)+', '',sentence.lower()).strip().split() for sentence in input().strip().split('.')]

Qs = []
for i in range(5):
    Qs += [re.sub(r'([^\sA-Za-z0-9]|_)+', '',input().strip().lower()).split()[1::]]

A_final = input().strip().split(';')
As = [re.sub(r'([^\sA-Za-z0-9]|_)+', '',a.strip().lower()).split() for a in A_final]

corpus = set([term for excerpt in Qs+As for term in excerpt])
termD = {term:0 for term in corpus}
idfD = termD.copy()

QAcomb = [q + a for q in Qs for a in As]

#TERM FREQUENCY
QA_TF = []
for excerpt in QAcomb:
    temp = termD.copy()
    t = len(excerpt)
    for term in excerpt:
        temp[term] += 1
        t+=1
    for term in set(excerpt):
        idfD[term] += 1/5 #combining Qs and As multiplies term freq in all docs by 5
    QA_TF += [list(map(lambda x:x/max(1,t), list(temp.values())))]

P_TF = []
for excerpt in passage:
    temp = termD.copy()
    t = len(excerpt)
    for term in excerpt:
        if term in corpus:
            temp[term] += 1
            t+=1
    for term in set(excerpt):
        if term in corpus:
            idfD[term] += 1
    P_TF += [list(map(lambda x:x/max(1,t), list(temp.values())))]

#INVERSE DOCUMENT FREQUENCY
n = len(As) + len(Qs) + len(passage)
for idfk in idfD.keys():
    idfD[idfk] = log(2*n/idfD[idfk])
idfL = list(idfD.values())

#TF-IDF
QA_TFIDF = []
for i in range(len(QA_TF)):
    QA_TFIDF += [[QA_TF[i][t]*idfL[t] for t in range(len(idfL))]]

P_TFIDF = []
for i in range(len(P_TF)):
    P_TFIDF += [[P_TF[i][t]*idfL[t] for t in range(len(idfL))]]

# MATRIX OPS - COSINE SIMILARITY
QAa = np.array(QA_TFIDF)
Pa = np.array(P_TFIDF)

asqrt = np.vectorize(sqrt)
asqr2 = np.vectorize(lambda x:x**2)

QAP = np.matmul(QAa,Pa.T)
Pd = np.reshape(asqrt(np.sum(asqr2(Pa),axis=1)),(1,Pa.shape[0]))
QAPd = np.add(np.reshape(asqrt(np.sum(asqr2(QAa),axis=1)),(QAa.shape[0],1)), Pd)
TFIDF_QAP = np.divide(QAP,QAPd)

#print(corpus)
#print(TFIDF_QP)
#print(TFIDF_PA)

QAPmax = np.max(TFIDF_QAP, axis = 1) 
QAd = {QAPmax[i]:(int((i - (i%5))/5), i%5) for i in range(5*5)}

order = sorted(QAPmax, reverse=True)
final = [-1]*5
i=0
while i < 5*5 and sum(final) < 15:
    t = QAd[order[i]]
    if final[t[0]] < 0 and t[1] not in final:
        final[t[0]] = t[1]
    i += 1
    
for i in final:
    print(A_final[i])

        


        
