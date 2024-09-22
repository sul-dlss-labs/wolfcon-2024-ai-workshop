# Retrieval Augmented Generation (RAG)
Retrieval Augmented Generation (RAG) is a Natural Language Processing (NLP) 
technique to enhance and localize the use of generative based Large Language 
Models (LLMs) by including specific external content in the LLM's context window. 

RAG is often employed to improve the accuracy and reliability of LLMs by 
better contextualizing the generative abilities of these models.

### Key features of RAG:
- First proposed in a 2020 paper[^RAG_NLP]
- Provides a means to ground LLM output
- Allows LLMs to act as a narrative interface for document corpora or data repositories
- Enables LLMs to cite specific documents or data, reducing the chance of incorrect answers

## Embeddings and Vector Databases
While the RAG technique doesn't require the use of embeddings or vector databases,
adding an information retrieval component to your RAG system can improve overall
performance of compound AI systems. To create a vector database, first the documents
or data is converted into a mathematical representation as a text embedding,
or set of numeric vectors, that are used for matching and creating relationships.

These text embeddings are then stored in a database or datastore and then can be queried
by first converting a query into a text embedding and then finding the stored embeddings
that most closely match the query. The resulting embeddings are then converted back to
textual documents and then sent as a part of the context window to the LLM.

## Application to FOLIO
Creating a vector database of FOLIO JSON documents offers a number of advantages to 
AI workflows; both in the generative aspects of creating new documents
like invoices or inventory records from text or automatic prompts, and
minimize errors in the LLMs output. 

## Workshop Exercise
1. Download the following [zip file](folio-docs.zip) and extract to a local directory named *folio-docs*
1. Open [gpt4all][GPT4ALL]
1. Click on the **LocalDocs** button on left-hand side
1. In the upper-right corner select the green button, **+ Add Collection**
1. Name the new collection and browse to the *folio-docs* folder you created in step 1
1. Create collection
1. Create a new Chat and select the collection to query the model using RAG

[GPT4ALL]: https://gpt4all.io/
[^RAG_NLP]: [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)
[^GUIDE_RAG]: [A Simple Guide To Retrieval Augmented Generation Language Models](https://www.smashingmagazine.com/2024/01/guide-retrieval-augmented-generation-language-models/)
