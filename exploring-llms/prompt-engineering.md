# Prompt Engineering

<figure>
  <blockquote class="blockquote">
   The technique of prompt engineering, which entails the crafting of precise, 
   task-specific instructions in natural language, either manually or through 
   automated means, and the careful selection of representative examples for 
   inclusion in the prompt, has become a central area of investigation for LLMs.
  </blockquote>
  <figcaption class="blockquote-footer">
   Principled Instructions Are All You Need for Questioning LLaMA-1/2, GPT-3.5/4
   <sup id="fnref:PRINCIPLED"><a class="footnote-ref" href="#fn:PRINCIPLED">1</a></sup>
  </figcaption>
</figure>


To effectively use Large Language Models (LLMs) and generative AI, you will need to construct a short textual 
description, called a prompt, that the LLM will use to generate text, images, or 
other media. Usually, you will need to iterate and change your prompt to improve the LLMs
outputs a few times until you have a result that meets your needs. 

How you construct your prompt will also impact aspects of the model's output, like 
accuracy, verbosity, or style customization. Together,
a set of techniques and approaches for constructing prompts is collectively called 
prompt engineering. 

In Anthropic's Prompt Engineering Guide, they suggest that before you begin applying 
specific prompt engineering techniques, you have a clear definition of success criteria
for your use case, ways to empirically test those criteria, and a first draft of your 
prompt.[^ANTHROPIC]

## Popular Prompt Engineering Techniques
Let's explore some popular prompt engineering techniques in detail.

### Zero Shot
In a Zero-Shot prompt, ask the LLM perform a task that the LLM has not been explicitly 
trained on but is dependent on the LLM general knowledge and understanding of the language
based on its training data. 

**Example**: Please translate this sentence into Spanish, "The 2024 Summer Olympics are being
held in France".

The LLM likely hasn't been trained on translating this exact sentence but uses its general 
understanding and translation patterns to provide a response.  

### Including Examples or Multishot Prompting 
In this technique, you provide a few (1-5) examples of the LLMs output in your prompt and is 
particularly helpful when you require the output to include structured data like FOLIO JSON 
documents. 

**Example**: You are an expert cataloger, please return any records as FOLIO JSON, here is an
example:

```
Q: Parable of the Sower by Octiva Butler, published in 1993 by Four Walls Eight Windows in New York 

A: {"title": "Parable of the Sower", "source": "ChatGPT", 
    "contributors": [{"name": "Octiva Butler", "contributorTypeText": "Author"}], 
    "publication": [{"publisher": "Four Walls Eight Windows", "dateOfPublication": "1993", "place": "New York"}] }}
```

### Chain-of-Thought
Another useful prompt technique is called *chain-of-thought* where you explicitly ask 
the LLM to provide the reasoning or steps the model went through to construct the output.
This can be helpful if you're confused how or why a model returns the output to your prompt.

**Example** Create a circulation report template that includes all books that have been checked
out in the past month. Please show your thinking step-by-step as you construct the report.

## Remember you can combine multiple prompt techniques! 
For more examples, please check-out Prompt Engineering Guide[^PROMPT_GUIDE].


## Function calling or connecting Systems to External Tools
Related to prompt engineering is a powerful technique of function calling that allows you to 
provide a LLM with a function signature and expected parameters. LLMs response will then 
generate a function call and parameter values that can then be integrated into a Compound AI
system. Specific information on this technique with various LLMs:

- [Open AI's Function Calling Guide](https://platform.openai.com/docs/guides/function-calling)
- [Build with Claude Tool use (function calling)](https://docs.anthropic.com/en/docs/build-with-claude/tool-use)
- [Intro to Function Calling with Gemini API](https://ai.google.dev/gemini-api/docs/function-calling)
- [Function calling for Llama 3.1 models!](https://community.sambanova.ai/t/function-calling-for-llama-3-1-models/225)

[^PRINCPLED]: [Principled Instructions Are All You Need for Questioning LLaMA-1/2, GPT-3.5/4](https://arxiv.org/abs/2312.16171)
[^ANTHROPIC]: [Antropic Prompt Engineering Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/)
[^PROMPT_GUIDE]: [Prompt Engineering Guide](https://www.promptingguide.ai/)

