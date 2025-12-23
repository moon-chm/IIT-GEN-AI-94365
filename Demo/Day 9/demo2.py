from langchain_openai import OpenAIEmbeddings
import numpy as np

def relalg(a,b):
    return np.dot(a,b)/np.linalg.norm(a)*np.linalg.norm(b)

embed_model = OpenAIEmbeddings(
                model="text-embedding-nomic-embed-text-v1.5",
                base_url="http://localhost:1234/v1",
                api_key="dummy-token",
                check_embedding_ctx_length=False
            )
sentences=[
    'I am Rohit',
    'ich bin Rohit'
]
emb=embed_model.embed_documents(sentences)
for emb_vec in emb:
    print("len : ",len(emb_vec),"-->",emb_vec[:4])

print('1 & 2 :',relalg(emb[0],emb[1]))    