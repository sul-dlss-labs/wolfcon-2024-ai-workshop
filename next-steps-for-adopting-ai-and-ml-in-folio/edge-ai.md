# Edge AI Module and AI Workflows
This workshop introduces two key components of FOLIO's AI integration: the 
[Edge AI Module][EDGE_AI] and [AI Workflows][AI_WRKFLW].

The FOLIO [Edge AI Module][EDGE_AI] provides a set of 
API endpoints for different FOLIO modules. The backend module supports the following 
Generative AI services:

- OpenAI's ChatGPT (requires an API token)
- Anthropic Claude (requires an API token)
- Google Gemini (requires an API token)
- Locally hosted Llama model (through a hosted [GPT4ALL](https://www.nomic.ai/gpt4all) or [LLaMA.cpp](https://github.com/ggerganov/llama.cpp) instance)

## Existing API endpoints

### Inventory Instance Record
Most of the development so far on [Edge AI Module][EDGE_AI] so far has focused on the requirements of the 
[Automated Metadata Generation Enrichment](https://github.com/folio-labs/ai-workflows/wiki/Automated-Metadata-Generation-Enrichment)
use-case around the FOLIO Inventory Instance records.  


## AI Workflows
The [AI Workflows][AI_WRKFLW] is a proof-of-concept open-source repository that operates within the
[Apache Airflow](https://airflow.apache.org/) workflow technology stack.

### What about mod-workflow?
The [Edge AI Module][EDGE_AI] is compatible with the new [mod-workflows][MOD_WRKFLW]
module in FOLIO, which will be available in the upcoming months. The current Directed Acyclic Graphs (DAGs) in
[AI Workflows][AI_WRKFLW] are simple enough to be migrated to [mod-workflows][MOD_WRKFLW].

The purpose of [AI Workflows][AI_WRKFLW] is to support more complex DAGs and additional features beyond
the planned functionality of [mod-workflows][MOD_WRKFLW]. The [Edge AI Module][EDGE_AI] should be able to 
complement" and support both workflow technologies. 

## Connection to FOLIO AI Use-cases
From the use cases hosted in [Edge AI Module][EDGE_AI]'s repository wiki, a set of requirements are
being formulated (thank-you for the help during this workshop!) to prioritize the development of [Edge AI Module][EDGE_AI].


## TODO
- Automate the deployment of the [Edge AI Module][EDGE_AI] to a FOLIO environment API service, 
  using either [Okapi][OKAPI] or [Kong][KONG]
- Increase Unit test coverage
- Add Integration Tests

[AIRFLOW]: https://airflow.apache.org/
[AI_WRKFLW]: https://github.com/folio-labs/ai-workflows
[EDGE_AI]: https://github.com/folio-labs/edge-ai
[KONG]: https://konghq.com/
[MOD_WRKFLW]: https://github.com/folio-org/mod-workflow
[OKAPI]: https://github.com/folio-org/okapi
