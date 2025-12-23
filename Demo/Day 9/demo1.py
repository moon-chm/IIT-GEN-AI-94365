from sentence_transformers import SentenceTransformer
import numpy as np

def relalg(a,b):
    return np.dot(a,b)/np.linalg.norm(a)*np.linalg.norm(b)

embmodel=SentenceTransformer('all-MiniLM-L6-v2')
sentence=[
    'I am rohit',
    'I am rohit'
]
emb=embmodel.encode(sentence)

for emb_vec in emb:
    print("len : ",len(emb_vec),'-->',emb_vec[:4])

print("1 & 3 :",relalg(emb[0],emb[1]))    