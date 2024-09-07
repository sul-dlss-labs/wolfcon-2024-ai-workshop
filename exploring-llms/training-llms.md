# Training Large Language Models (LLMs)
One methods for customizing and providing better context when using LLMs is to train the
LLM on your data. [OpenAI][OPENAI] allows you to train one of their models through their API
and custom GPTs. 

Running a local version [Llama][LLAMA] allows to directly train the 
model (depending on the capacities of your local computer).

## OpenAI Training
To train or fine-tune a ChatGPT model, the OpenAI API provides the following endpoints:

- Create an Embedding
- Select a model

**NOTE:** Fine-tuning a ChatGPT model is significantly more cost than just using OpenAI's
API model inference. 


## Fine-tuning LLMs with Llama.cpp
The [LLaMA.cpp][LLAMA.CCP] project allows you to run and fine-tune
LLaMA models on your local computer.  [LLaMA.cpp][LLAMA.CCP] provides more 
lower-level access to these Open source LLMs. There is
also a [Python SDK](https://github.com/abetlen/llama-cpp-python) for integrating with 
[edge-ai](https://github.com/folio-labs/edge-ai). [LLaMA.cpp][LLAMA.CCP] provides an
OpenAI API compatible server that also allows us to integrate with [DSPy](dspy-docs.vercel.app/)

[LLaMA.cpp][LLAMA.CCP] can also be run with [Docker][^DOCKER] on your computer if you 
don't want or can't compile the C++ source code to run on your computer.

### Downloading a LLaMA-based Model
[LLaMA.cpp][LLAMA.CCP] uses the [GGUF](https://github.com/ggerganov/ggml/blob/master/docs/gguf.md) 
format for model inference and training. Look for GGUF models on [HuggingFace][HUGFACE]
and if you compiled [LLaMA.cpp][LLAMA.CCP] with `libcurl` support, you can use the `llama-cli` command-line
client to download:

 `./llama-cli --hf-repo lmstudio-community/Reflection-Llama-3.1-70B-GGUF --hf-file Reflection-Llama-3.1-70B-GGUF.gguf`

If `libcurl` hasn't been installed, you can usually directly download the models directly from [HuggingFace][HUGFACE] and
store in the `/models` directory under the main [LLaMA.cpp][LLAMA.CCP].

### Running the Model in Inference Mode

[HUGFACE]: https://huggingface.co/l
[LLAMA]: https://ai.meta.com/
[LLAMA.CCP]: https://github.com/ggerganov/llama.cpp
[OPENAI]: https://openai.com/

[^DOCKER]: [LLaMA.cpp with Docker](https://github.com/ggerganov/llama.cpp/blob/master/docs/docker.md)

