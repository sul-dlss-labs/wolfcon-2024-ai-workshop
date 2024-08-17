# Carbon Footprint of LLMs
A real concern of Large Language Models (LLMs) is the amount of energy and water 
required for training and deploying these models. For example, in their 2024 report[^GOOG_2024],
Google admitted that their carbon output increased over 13% year-over-year primarily due to the 
increased energy usage of their customer-facing AI efforts, including the training and inference
of their flagship [Gemini LLM](https://gemini.google.com/). In the report they admit:

> As our business and industry continue to evolve, we expect our total GHG emissions
> to rise before dropping toward our absolute emissions reduction target.
> - page 31, Google 2024 Environmental Report[^GOOG_2024].

Similarly, Microsoft in its 2024 Sustainability report[^MS_2024], admitted that it's Greenhouse Gas (GHG)
Scope 3 emissions increased over 30% from its 2020 base year (page 11[^MS_2024]). 

As model parameters continue to increase to the billions of parameters, the associated energy to train these
models as well as the energy requirements for actual model inference use by customers has increased quickly. 
The training of the ChatGPT 3.5 model is estimated to have used 1,287 MWh of electricity and produced 552 
tons of CO2. ChatGPT 4.0 models are estimated to require 7,200 MWh of energy[^AI_CHATBOTS_2023], 
significantly more than OpenAI's previous 3.5 model.

In a 2024 report[^PIKTO_2024], Wong estimates that each query to ChatGPT 3.5 generates 4.32 grams of CO2 with over 10 million
queries running on 30,000 GPUs, the total daily CO2 generation of 43,200 kg.

## How can we reduce the LLMs' Carbon Footprint?
In a 2024 report [^MS_REDUCE_GENAI] released by Microsoft, four suggestions are presented to help Generative AI developers 
and users of these LLMs that can help reduce the environmental impact of these models. These suggestions are:

- **Model Selection**: Pre-trained models use significantly less power than training new models
- **Model Improvement**: Prompt engineering, RAG, and Fine-tuning can all be used to improve functionality of existing models
  without needed to train the models
- **Model Deployment**: Using Model-as-a-Service (MaaS), the costs and energy requirements are less because the MaaS infrastructure
  is typically optimized by the vendor. Model-as-a-Platform (MaaP) requires more customization and may be inefficient to 
  use. Model Parameters can also be used to optimize the model performance while minimizing the energy requirements to use. 
- **Model Evaluation**: When using these models, users should evaluate the costs and performance in order to assess the applicability 
  of their models as well as evaluate the output of the models for safety and risk concerns.


## Workshop Use-cases

### Primary

### Secondary

### Tertiary


## Resources
- [Assessing the environmental impact of large language models](https://www.techtarget.com/searchenterpriseai/tip/Assessing-the-environmental-impact-of-large-language-models)
- [LLMCarbon: Modeling the end-to-end Carbon Footprint of Large Language Models](https://arxiv.org/abs/2309.14393)


[^AI_CHATBOTS_2023]: [AI Chatbots: Energy usage of 2023’s most popular chatbots (so far)](https://www.trgdatacenters.com/resource/ai-chatbots-energy-usage-of-2023s-most-popular-chatbots-so-far/)
[^GOOG_2024]: [Google Environmental Report 2024](https://www.gstatic.com/gumdrop/sustainability/google-2024-environmental-report.pdf)
[^MS_2024]: [Microsoft How can we advance sustainability? 2024 Environmental Sustainability Report](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RW1lMjE)
[^MS_REDUCE_GENAI]: [Reducing the Environmental Impact of Generative AI: a Guide for Practitioners](https://techcommunity.microsoft.com/t5/azure-architecture-blog/reducing-the-environmental-impact-of-generative-ai-a-guide-for/)
[^PIKTO_2024]: [Gen AI’s Environmental Ledger: A Closer Look at the Carbon Footprint of ChatGPT](https://piktochart.com/blog/carbon-footprint-of-chatgpt/)


