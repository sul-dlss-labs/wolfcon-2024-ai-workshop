# Edge AI Module and AI Workflows

The FOLIO [Edge AI Module][EDGE_AI] provides a set of 
API endpoints for different FOLIO modules. This backend model supports the following 
Generative AI services:

- OpenAI's ChatGPT (requires an API token)
- Anthropic Claude (requires an API token)
- Google Gemini (requires an API token)
- Locally hosted Llama model (through a hosted [GPT4ALL]() or [LLaMA.cpp](https://github.com/ggerganov/llama.cpp) instance)

## Existing API endpoints

### Inventory
Most of the development so far on [edge-ai][EDGE_AI] has been supporting the requirements from the 
[Automated Metadata Generation Enrichment](https://github.com/folio-labs/ai-workflows/wiki/Automated-Metadata-Generation-Enrichment)
use-case. 

### Circulation

### Finance

## AI Workflows
The [ai-workflows][AI_WRKFLW] is a proof-of-concept open-source repository that 

### What about mod-workflow?
There is nothing that would prevent [edge-ai][EDGE_AI] to use the new [mod-workflows][MOD_WRKFLW]
module in FOLIO once it is available for use and release. The current Directed Acyclic Graphs (DAGs) in
[ai-workflows][AI_WRKFLW] are simple enough that could be ported to [mod-workflows][MOD_WRKFLW] directly.

Where the [ai-workflows][AI_WRKFLW] is positioned to support more complex DAGs and other features beyond
[edge-ai][EDGE_AI] and the planned functionality of [mod-workflows][MOD_WRKFLW] and should be able to 
compliment and support both. 

## Connection to FOLIO AI Use-cases
From the edge-ai's use-cases hosted in the repository's wiki, a set of requirements are
being formulated (thank-you for help!) and will help prioritize the development of [edge-ai][EDGE_AI].



## TODO
- Automate the deployment of the [edge-ai][EDGE_AI] to a FOLIO environment API service, 
  either [Okapi][OKAPI] or [Kong][KONG]
- Increase Unit test coverage
- Add Integration Tests

[AI_WRKFLW]: https://github.com/folio-labs/ai-workflows
[EDGE_AI]: https://github.com/folio-labs/edge-ai
[KONG]: https://konghq.com/
[MOD_WRKFLW]: 
[OKAPI]: https://github.com/folio-org/okapi
