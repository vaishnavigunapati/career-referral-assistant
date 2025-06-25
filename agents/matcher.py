from langchain_community.embeddings import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

def match(resume_embed, jd_text):
    jd_embed = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2").embed_query(jd_text)
    score = cosine_similarity([resume_embed], [jd_embed])[0][0]
    return score