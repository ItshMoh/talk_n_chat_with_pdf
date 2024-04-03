# talk_n_chat_with_pdf
It is a fun project where a user can talk with a pdf. Here he can ask some questions related to the pdf and our model will answer the questions. 
Here I have used langchain, FAISS-cpu, Gemini and Google Generative AI embeddings, whisper and gradio. 
FAISS-cpu has been used as a vector store. Then we have performed similarity search on the embeddings.
I have used whisper for audio transcription. I have used the base model.As it is fast.
PyPDF has been used for reading the pdf and extracting the text inside it.
Gemini has been used as model which will generate answer from the docs found after the similarity search from the vector store.
