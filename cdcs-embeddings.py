import ollama
import chromadb

# List of documents to be stored in the vector embedding database.
documents = [
  "The Centre for Data, Culture & Society at the University of Edinburgh builds capacity for and supports data-led and digital research methods within the arts, humanities and social sciences. A platform for methodological innovation, we help our community to develop projects, learn new skills and techniques, and share experiences and practices.",
  "The Centre for Data, Culture & Society provides our community with space for methodological experimentation, innovation and skills development, and gives tailored advice and support to research groups and projects. We believe in the value of critical and creative exchange between technology and the arts, humanities and social sciences. We empower researchers in these disciplines to explore and engage with data and digital research methods.",
  "The Centre for Data Culture & Society's extensive training programme is designed to help our community develop new skills and enable them to conduct their research more effectively.  Courses range from introductory sessions on coding to deep dives into the affordances of particular tools and libraries. We also gather, develop and share resources, offering guidance on skills development though our Training Pathways, and work in partnership with other providers to support related training initiatives. ",
  "CDCS creates and hosts digital research tools and training resources, developing  research infrastructure to support applied digital methods as well as sharing information and signposting other services. We also host large datasets for research and can provide guidance on finding appropriate for your research, facilitate work with our text and data mining resources, and advise on how to share the data that you have produced with other researchers. ",
]

# Initialize the ChromaDB client and create a new collection called "docs"
client = chromadb.Client()
collection = client.create_collection(name="docs")

# Loop through each document, generate its embedding, and store it in the collection
for i, d in enumerate(documents):
  # Generate the embedding using the specified model
  response = ollama.embed(model="mxbai-embed-large", input=d)
  embeddings = response["embeddings"]
  # Add the document and its embedding into the collection with a unique id
  collection.add(
    ids=[str(i)],
    embeddings=embeddings,
    documents=[d]
  )

# Define an example user input query
input = "What is the Centre for Data Culture & Society?"

# Generate an embedding for the user input query
response = ollama.embed(
  model="mxbai-embed-large",
  input=input
)

# Query the collection with the generated embedding to retrieve the most relevant document
results = collection.query(
  query_embeddings=[response["embeddings"][0]],
  n_results=1
)
# Extract the retrieved document from the query results
data = results['documents'][0][0]

# Generate a response by combining the retrieved data and the original user input query
output = ollama.generate(
  model="llama3.2:3B",
  prompt=f"Using this data: {data}. Respond to this prompt: {input}"
)

# Print the final generated response
print(output['response'])