# Meta's Llama
In February 2023, [Meta AI][METAAI] (the AI research division of the Meta that also includes Facebook) released 
an open-source Large Language Model (LLM) called Llama with a follow-up release in 
April 2024. Unlike other commercial LLMs, Meta AI released the weights along with supporting
code to allow for training and other uses not possible with similar models released by OpenAI,
Anthropic, and Google.

## Using Llama
The easiest way to use Llama is go to [https://www.meta.ai](https://www.meta.ai) and start entering chat prompts. This 
multi-modal web application allows users to generate images and text (although to use the image
generator function requires logging in with a Facebook account). 

## Using Llama Locally
Because of its release as open-source, you are able to download the Llama model to run and 
train locally without the service providing additional data to the corporate entity. While there 
are a number of ways for running Llama locally, a convenient method for running Llama
and other open-source models is using a project called [gpt4all][GPT4ALL]. While the computing
requirements can vary depending on your laptop's hardware and OS, there are desktop versions
for [Macintosh](https://gpt4all.io/installers/gpt4all-installer-darwin.dmg), 
[Windows](https://gpt4all.io/installers/gpt4all-installer-win64.exe), and 
[Ubuntu](https://gpt4all.io/installers/gpt4all-installer-linux.run).

## Using gpt4all 
For the purposes of this workshop, we will demonstrate a few crucial aspects of using and extending
LLM using [gpt4all][GPT4ALL], including [Retrieval Augmented Generation (RAG)](retrival-augment-generation.md) 
and [training LLMs](training-llms.md). If you haven't already prior to this workshop (and if you have
administrative rights on your local laptop), please download and install [gpt4all][GPT4ALL].

A nice feature of [gpt4all][GPT4ALL], is that you can use a locally running LLM without an internet connection. 
This also means that you can restrict access when using RAG on sensitive or private documentation.
 
[GPT4ALL]: https://gpt4all.io/
[METAAI]: https://ai.meta.com/ 
