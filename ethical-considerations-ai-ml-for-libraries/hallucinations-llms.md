# Hallucinations and Generative AI
From the initial release of ChatGPT 3.5 in 2022, a major criticism of Large 
Language Models (LLMs) is the tendency of these models to fabricate factual 
incorrect statements. Because LLMs work through predictive means based on the text and
context of the prompt based on the model weights, the resulting output is not  
a deductive process based on the model's training source material. These hallucinations 
have been broken down into the following categories[^TURING]:

- **Fact-conflicting** - the LLMs output contains statements that are known to be false
  i.e. 2+2=5
- **Input-conflicting** - the LLMs output diverges from what the user prompt and context,
  i.e. asking a LLM to summarize an article and the summarization adds information not present
  in the article.
- **Context-conflicting** - the LLMs output contains inconsistent or self-contradictions, particularly 
  in larger, mult-part responses.

## Correcting Hallucinations
To correct these hallucinations, corporations like OpenAI, Anthropic, and Google use a
varied of techniques. These include:

- Chain-of-thought (COT)
- One-shot and Few-shot Prompts
- Retrieval Augmented Generation (RAG)
- Fine-tuning
  - Reinforcement Learning with Human Feedback (RLHF)

## Workshop Exercise
Take the LLM service of your choice (ChatGPT, Claude, Gemini, Llama) and enter the following prompt.

```
Who is the first person to swim across the Pacific Ocean?
```
 

## Final Thought
<figure>
  <blockquote class="blockquote">
   <p>
    TLDR I know I'm being super pedantic but the LLM has no "hallucination problem". 
    Hallucination is not a bug, it is LLM's greatest feature. 
    The LLM Assistant has a hallucination problem, and we should fix it.
   </p>
  </blockquote>
  <figcaption class="blockquote-footer" markdown="span">
   Andrej Karpathy <sup><a class="footnote-ref" href="#fn:TURING">3</a></sup>
  </figcaption>
</figure>


## Resources
- [Hallucinations, Errors, and Dreams](https://medium.com/@colin.fraser/hallucinations-errors-and-dreams-c281a66f3c35)

[^TURING]: [Best Strategies to Minimize Hallucinations in LLMs: A Comprehensive Guide](https://www.turing.com/resources/minimize-llm-hallucinations-strategy)
[^NYTIMES]: [A.I. Has a Measurement Problem](https://www.nytimes.com/2024/04/15/technology/ai-models-measurement.html)
[^KARPATHY]: X post on [8 December 2023](https://x.com/karpathy/status/1733299213503787018?lang=en)
