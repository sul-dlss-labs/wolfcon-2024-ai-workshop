# Hallucinations and Generative AI
Since the initial release of ChatGPT 3.5 in 2022, a major criticism of Large 
Language Models (LLMs) has been the tendency of these models to fabricate factually
incorrect statements. LLMs generate text by predicting the most likely continuation token
based on the prompt's text, context, and model internal weights. Unlike a deductive process, LLMs
do not directly reference their training source material to generate responses. 

Hallucinations in LLMs can be categorized as follows[^TURING]:

- **Fact-conflicting**: The LLM's output contains statements that are known to be false
  (e.g. 2+2=5)
- **Input-conflicting**: The LLM's output diverges from the user prompt and context
  (e.g. the model summarize an article and adds information not present in the original text).
- **Context-conflicting**: The LLM's output contains inconsistent or self-contradictions, particularly 
  in larger, multi-part responses.

## Correcting Hallucinations
To address these hallucinations, companiess like OpenAI, Anthropic, and Google
suggest using a variety of techniques[^TURING], including:

- **Chain-of-thought (COT)**: A technique prompting the model to break down its reasoning process
  into sequential steps,explaining how it arrived to its final answer.
- **One-shot and Few-shot Prompts**: Techniques that provide context by offering sample responses in 
  a given format, enabling the model to infer patterns for consistency and accuracy in its
  answers.
- **Retrieval Augmented Generation (RAG)**: Combines contextual examples with the prompt, grounding the
  model in factual, current material from external sources, and reducing the model's dependence on 
  outdated or incomplete information training data.
- **Reinforcement Learning with Human Feedback (RLHF)**: A fine-tuning technique of adding direct human 
  feedback to a model's responses by rewarding factual responses and penalizing hallucinations.  

## Workshop Exercise
Choose an LLM service (ChatGPT, Claude, Gemini, Llama) and enter the following prompt.

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
