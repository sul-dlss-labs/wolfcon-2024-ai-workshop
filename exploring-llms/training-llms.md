# Training Large Language Models (LLMs)
One method for customizing and providing better context when using LLMs is to train the
LLM on your data. There are a number methods for fine-tuning LLMs including low-rank adaptation or LoRA[^LORA],
that allow you to fine-tune a small number of parameters of a LLM many parameters without a 
large number of GPUs used for the initial training of these large models. 
 

[OpenAI][OPENAI] allows you to train one of their models through their API
and custom GPTs. Google Gemni offers fine-tuning through the [Gemini API](https://ai.google.dev/gemini-api/docs/model-tuning)
as does Anthropic as explained in their [documentation](https://www.anthropic.com/news/fine-tune-claude-3-haiku).

Training [LLaMA][LLAMA] models locally on a personal computer is possible
depending on the capacities of your local computer. Unfortunately, the process isn't
easy or straight-forward and require running Python code. If you 
have an Apple computer, the [mlx-lm][MLX_LM] package,  
which uses Apple Silicon GPU, can be used for fine-tuning open-source models like LLaMA. Another
possibility is using HuggingFace's [peft][PEFT] package along 
with HuggingFace's transformers to fine-tune models.


## Steps for Fine-tuning 
OpenAI provides directions for [fine-tuning][^OPENAI_FINETUNE] a ChatGPT model that are 
general enough for most fine-tuning tasks:

1. Prepare and upload training data
1. Train a new fine-tuned model
1. Evaluate results and go back to step 1 if needed
1. Use your fine-tuned model


### Create Inventory Instance Training Set

We will create a training set 1,000 random records from the FOLIO community's [Quesnelia Bugfest](https://bugfest-quesnelia.int.aws.folio.org/) 
instance. The training set consists of the denormalize Instance along with a text prompt.

Depending on the model and service, you may need reformat the training set to match the expected inputs
to the model. 

For OpenAI, the expected format are JSON objects, typically saved one per line in the JSON-L
format, that would like the following for the training set:

```javascript
{"messages": [{"role": "system", "content": "As an expert cataloger, you will create the FOLIO inventory JSON record."}, 
              {"role": "user", "content": "For Vacancies in certain judgeships. Published in 1935 by [publisher not identified], Washington Subjects are Courts, Judges, United States--Officials and employees, Electronic books."},
              {"role": "assistant", "content": "{'title': 'Vacancies in certain judgeships.', 'contributors': [], 'subjects': [{'value': 'Courts'}, {'value': 'Judges'}, {'value': 'United States--Officials and employees'}, {'value': 'Electronic books'}], 'classifications': [], 'publication': [{'publisher': '[publisher not identified]', 'place': 'Washington', 'dateOfPublication': '1935', 'role': 'Publication'}], 'instanceTypeText': 'text', 'modeOfIssuanceText': 'single unit'}}"}]}
```

For training using [mlx-lm][MLX_LM], the data format is simpler than the OpenAI format but still uses JSON-L:

```javascript
{"text": "As an expert cataloger, you will create the FOLIO inventory JSON record. Q:For Statistical applications for chemistry, manufacturing and controls (CMC) in the pharmaceutical industry /Richard K. Burdick [and others]. Published in 2017 by Springer, Cham A:{'title': 'Statistical applications for chemistry, manufacturing and controls (CMC) in the pharmaceutical industry /Richard K. Burdick [and others].', 'contributors': [], 'publication': [{'publisher': 'Springer', 'place': 'Cham :', 'dateOfPublication': '2017', 'role': None}], 'instanceTypeText': 'text', 'modeOfIssuanceText': 'Monograph'}"}
```

### Training
To train a ChatGPT model after creating a training set, follow these steps:

1. Upload a training file to the [Files API](https://platform.openai.com/docs/api-reference/files/create)
1. Create a fine-tune job either through the OpenAI [User Interface](https://platform.openai.com/finetune) or through
   Python or Node.js SDK.

There are different methods for fine-tuning local LLaMA models. With Apple's Python [mlx-lm][MLX_LM], follow
these steps in [LoRA documentation](https://github.com/ml-explore/mlx-examples/blob/main/llms/mlx_lm/LORA.md).

On other platforms and assuming you have a supported GPU, [unsloth](https://unsloth.ai/) is a good option. 
You can use [unsloth](https://unsloth.ai/) on public cloud providers as well.  Huggingface's 
[peft][PEFT] is another good choice and includes the [loralib](https://github.com/microsoft/LoRA) package by 
the authors of the original LoRA paper[^LoRA_PAPER]. Both need to be used with [Pytorch](https://pytorch.org/) to 
fine-tune models as well. 

### Using a GPT4ALL Model 
Once you have a fine-tuned model and you have installed [GPT4ALL][GPT4ALL], you can use that model  
on a Mac by copying the fine-tuned models to this location:

 `/Users/{user-name}/Library/Application Support/nomic.ai/GPT4All/`


### Running the Model in Inference Mode

[^LORA]: [What is low-rank adaptation (LoRA)?](https://www.cloudflare.com/learning/ai/what-is-lora/)
[^OPENAI_FINETUNE]: [Guide for Fine-tuning](https://platform.openai.com/docs/guides/fine-tuning/)
[^LoRA_PAPER]: [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)

[GPT4ALL]: https://gpt4all.io/
[HUGFACE]: https://huggingface.co/
[LLAMA]: https://ai.meta.com/
[LLAMA.CCP]: https://github.com/ggerganov/llama.cpp
[MLX_LM]: https://github.com/ml-explore/mlx-examples
[OPENAI]: https://openai.com/
[PEFT]: https://github.com/huggingface/peft

[^DOCKER]: [LLaMA.cpp with Docker](https://github.com/ggerganov/llama.cpp/blob/master/docs/docker.md)

