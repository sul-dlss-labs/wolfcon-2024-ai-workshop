# Privacy 
With the wide-spread release of Large Language Models (LLMs) by various corporate and 
other organizations, there have emerged a number of significant privacy issues[^PRIVACY_LLM], including:

- Personal details in Training data
- Personal details in logged prompts
- Re-identification of individuals


## Training Data 
The privacy of individuals may be compromised if their personal 
information is part of the massive amount of textual and other data used to train 
these models. Inclusion of personal information in the training data is problematic 
because the individuals in question have not consented to have their data included and
even if the corporations have included counter-measures to keep personal data private,
there exist prompt engineering attacks that can reveal the raw training data from such 
models as ChatGPT.[^SCALEABLE]   

## Inference Data privacy i.e. Revealing Too Much in your prompts
As people use LLMs for such personal issues and topics like relationship advice, medical
information on current or potential conditions, and psychological counseling, the privacy 
risks of disclosing this information through prompts continues to grow.[^GEN_AI_PRIVACY].

These prompts are often collected and logged by organizations like OpenAI or Google and the
inclusion of sensitive details that are potentially damaging to the reputation and mental
health of the users that

## Re-identification
Even if the training data has been anonymized for personal details, by combining and collecting
responses from LLMs, individuals could potential be identified thereby comprising their privacy
when using the LLM. 

[^PRIVACY_LLM]: [Privacy in Large Language Models: Attacks, Defenses and Future Directions](https://arxiv.org/abs/2310.10383)
[^SCALEABLE]: [Scalable Extraction of Training Data from (Production) Language Models](https://arxiv.org/abs/2311.17035)
[^GEN_AI_PRIVACY]: [Generative AI's privacy problem](https://www.axios.com/2024/03/14/generative-ai-privacy-problem-chatgpt-openai)
