from langchain_text_splitters import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
      separators=[
        "\n\n",
        "\n\n\n",
        "\n",
        " ",
        ".",
        ",",
        "\u200B",  # Zero-width space
        "\uff0c",  # Fullwidth comma
        "\u3001",  # Ideographic comma
        "\uff0e",  # Fullwidth full stop
        "\u3002",  # Ideographic full stop
        "",
    ],
    chunk_size=100,
    chunk_overlap=20,
    length_function=len,
    is_separator_regex=True,
)

texts = text_splitter.create_documents([pdf_text])

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
model = "models/embedding-001"

# Create the embeddings object with the model argument
embeddings = GoogleGenerativeAIEmbeddings(
    google_api_key="google_api_key",
    model=model
)

db = Chroma.from_documents(texts, embeddings)

query = "who killed caesar"
docs = db.similarity_search(query)
print(docs[0].page_content)