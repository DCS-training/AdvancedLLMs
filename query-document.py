from langchain.text_splitter import RecursiveCharacterTextSplitter
import ollama
import chromadb

# Define a simple document wrapper for retrieved texts.
# Each document contains the text content and optional metadata.
class SimpleDoc:
    def __init__(self, text: str):
        self.page_content = text
        self.metadata = {}  # You can add metadata about the document if needed

# Initialize a text splitter.
# This splitter uses a model-based tokenizer (via TikToken) to split text into chunks of a specified size.
text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=250,     # Maximum number of tokens per chunk
    chunk_overlap=0     # No overlapping text between chunks
)

# Read the markdown file that contains extracted text from a PDF.
with open("sarkar-paper.md", "r") as f:
    markdown_text = f.read()

# Wrap the entire markdown text into a single document object.
docs_list = [SimpleDoc(markdown_text)]

# Use the text splitter to divide the document into smaller chunks.
doc_splits = text_splitter.split_documents(docs_list)

# Create a ChromaDB client and instantiate a new collection to store vector embeddings.
client = chromadb.Client()
collection = client.create_collection(name="docs")

# Loop over each text chunk and generate its corresponding embedding,
# then add the chunk to the vector store for future similarity search.
for i, doc in enumerate(doc_splits):
    text = doc.page_content
    # Request an embedding from Ollama for the current text chunk.
    response = ollama.embed(model="mxbai-embed-large", input=text)
    embedding = response["embeddings"]
    # Add this chunk to the ChromaDB collection.
    collection.add(
        ids=[str(i)],
        embeddings=embedding,
        documents=[text]
    )

# Define an example input query.
input_query = "What are the five kinds of creativity Sarkar defines?"

# Generate an embedding for the query text.
response = ollama.embed(
    model="mxbai-embed-large",
    input=input_query
)
# Unpack the embedding vector for the query. Note: indexing ensures we pass the actual vector.
query_embedding = response["embeddings"][0]

# Query the collection for the top 10 chunks similar to the query embedding.
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=10
)

# Extract the documents (text chunks) from the query results.
data = results['documents']

# Generate an answer by passing the retrieved data along with the query to the language model.
output = ollama.generate(
    model="llama3.2:3B",
    prompt=f"Using this data: {data}. Respond to this prompt: {input_query}"
)

# Print the final response from the language model.
print(output['response'])