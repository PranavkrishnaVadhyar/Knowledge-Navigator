# Web Crawler and Semantic Search with MILVUS

This project involves developing a web crawler to scrape data from a given website, chunking the data based on semantic similarity, creating a vector database using MILVUS, and retrieving and re-ranking data to pass to a Language Model (LLM) for question answering.

## Table of Contents

- [Overview](#overview)
- [Setup](#setup)
- [Web Crawling](#web-crawling)
- [Data Chunking and Vector Database Creation](#data-chunking-and-vector-database-creation)
- [Retrieval and Re-ranking](#retrieval-and-re-ranking)
- [Question Answering](#question-answering)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

- **Web Crawling**: Scrapes data from [NVIDIA CUDA Documentation](https://docs.nvidia.com/cuda/), including sub-links up to a depth of 5.
- **Data Chunking**: Uses advanced techniques for chunking data based on sentence/topic similarity.
- **Vector Database**: Creates a vector database using MILVUS with HNSW indexing, storing embedding vectors and relevant metadata.
- **Retrieval and Re-ranking**: Implements query expansion and hybrid retrieval methods (BM25 and BERT/bi-encoder) to retrieve and re-rank data.
- **Question Answering**: Uses a Language Model (e.g., OpenAI's GPT) to generate answers based on retrieved data.

## Setup

### Prerequisites

- Python 3.8+
- [MILVUS](https://milvus.io/docs/v2.0.x/install_standalone-docker.md)
- Required Python packages (install via `requirements.txt`)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/web-crawler-semantic-search.git
    cd web-crawler-semantic-search
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up MILVUS by following the [installation guide](https://milvus.io/docs/v2.0.x/install_standalone-docker.md).

## Web Crawling

The web crawler scrapes data from the NVIDIA CUDA Documentation website, including sub-links up to 5 levels deep.

### Running the Web Crawler

1. Update the `start_url` variable in the script if necessary.
2. Run the web crawler:
    ```bash
    python web_crawler.py
    ```

## Data Chunking and Vector Database Creation

### Chunking Data

Chunk the scraped data based on sentence/topic similarity using advanced techniques like semantic similarity or topic modeling.

### Creating Vector Database

1. Generate embeddings for the chunked data using a model like `sentence-transformers/paraphrase-mpnet-base-v2`.
2. Create a vector database using MILVUS and store the embeddings with HNSW indexing.

## Retrieval and Re-ranking

1. Implement query expansion techniques to enhance retrieval.
2. Use a hybrid retrieval method combining BM25 and BERT/bi-encoder.
3. Re-rank the retrieved data based on relevance and similarity to the query.

## Question Answering

1. Pass the retrieved and re-ranked data to an LLM (e.g., OpenAI GPT).
2. Generate accurate and relevant answers based on the retrieved data.

### Code Example

Below is a simplified code example for integrating LLM for question answering:

```python
from langchain.chains import LLMChain
from langchain.llms import OpenAI

# Set your OpenAI API key
openai.api_key = 'your-openai-api-key'

# Initialize OpenAI LLM
llm = OpenAI(temperature=0.7)

# Example context from retrieved and re-ranked data
context = "Your retrieved context here"

# Example question
question = "What should be done in a first aid action plan?"

# Initialize LangChain LLMChain
llm_chain = LLMChain(llm)

# Generate answer
answer = llm_chain.answer(question, context)
print("Answer:", answer)
```

## Usage

1. Run the web crawler to scrape data.
2. Chunk the data based on semantic similarity.
3. Create embeddings and store them in the MILVUS vector database.
4. Implement retrieval and re-ranking for your queries.
5. Use an LLM to generate answers based on the retrieved data.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


### Additional Notes:
- Ensure you replace placeholders like `your-openai-api-key` with actual values.
- Include any additional setup or configuration steps specific to your environment or data sources.

This README provides a comprehensive guide for setting up and using your project, from web crawling to question answering using LangChain and MILVUS.
