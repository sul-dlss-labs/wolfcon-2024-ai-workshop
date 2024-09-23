# OpenAI's ChatGPT
The release of ChatGPT 3 by [OpenAI][OPENAI] in the fall of 2022 sparked 
the current boom in generative AI and Large Language Models (LLM). In March of 2023, 
OpenAI released ChatGPT 4 followed by various smaller upgrades with the latest release of ChatGPT 4.o.
Earlier this month, OpenAI released their reasoning models, o1[^O1], with 
improved reasoning and deductive skills in these models.

## Microsoft ChatGPT Variant 
Microsoft has invested in [OpenAI][OPENAI] and is using a version of ChatGPT 4 in their Bing
[Copilot][COPILOT] search service. Microsoft's Copilot is 
able to access recent material after ChatGPT model's training data cut-off through a 
combination of Retrieval Assisted Generation (RAG), fine-tuning the model, and other methods. 

Additionally, through Microsoft's [Copilot][COPILOT] service, you can use ChatGPT's image 
generation functionality without paying for a separate [OpenAI][OPENAI] account. You
still need a Microsoft account to log in and use these advanced features. 

## Using ChatGPT
To use ChatGPT, you can visit [https://chatgpt.com][CHATGPT] to access either the 
3.5 or 4.o models. If you want to use later models, including OpenAI's [DALL-E 3][DALLE3]
 or to use the ChatGPT 
[API](https://platform.openai.com/docs/api-reference), you will need to 
sign up for an account. 

### Workshop Exercise
Ask ChatGPT to create a three task Airflow DAG using the Taskflow API decorators in Python:

- **First task**: Query FOLIO using an HTTP FOLIO Connection
- **Second task**: Extract and update {property-related-to-a-use-case} using JSON Path
- **Third task**: POST the new JSON back to FOLIO using the HTTP Connection


## GPTs
OpenAI offers custom versions of ChatGPT that are available for use at [https://chatgpt.com/gpts](https://chatgpt.com/gpts).
These GPTs often use custom prompts along with text and image collections using 
Retrieval Augmented Generation (RAG), 

Other services are also available that use custom ChatGPT models for specific domains and 
problems and are good options if you need specific or custom functionality. For example:

- **[OSCAR](https://openai.com/index/oscar/)**: custom generative AI services for health insurance
  and compliance. 
- **[Harvey](https://openai.com/index/harvey/)**: ChatGPT for Legal professionals
- **[Arizona State University](https://news.asu.edu/20240118-university-news-new-collaboration-openai-charts-future-ai-higher-education)**:
  Proposed integration of OpenAI with ASU's content.

[^O1]: [Learning to Reason with LLMs](https://openai.com/index/learning-to-reason-with-llms/)
[CHATGPT]: https://chatgpt.com/
[COPILOT]: https://copilot.microsoft.com/
[DALLE3]: https://openai.com/index/dall-e-3/
[OPENAI]: https://openai.com/

