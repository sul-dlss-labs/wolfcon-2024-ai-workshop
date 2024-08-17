# Bias and AI

> AI bias, also referred to as machine learning bias or algorithm bias, refers 
> to AI systems that produce biased results that reflect and perpetuate human 
> biases within a society, including historical and current social inequality. 
> Bias can be found in the initial training data, the algorithm, or the 
> predictions the algorithm produces.[^IBM_AI_BIAS]


## Sources of Bias

### Training data
- Training data can over or under sample underrepresented groups
  
    - **Example**:
      Exclusively using copyright-free material from the 1930s and earlier 
      may under-represent many groups.
 
- Training data can also be bias in labeling by excluding or over-representing
  certain categories or characteristics.

    - **Example**
      If using a controlled vocabulary that focuses on Western categories and concepts,
      might miss valid valid indigenous concepts and constructions that may be present in the
      training data.  

### Algorithms
- Algorithms based on biased data could perpetrate underlying flaws
    - **Example**
      If training data is taken to be relatively free of bias but bias exist, 
      algorithms at risk of Type II error of erroneous acceptance. 
  
- Programmers could introduce personal bias intentionally or unintentionally

- Unintended consequences of using proxies for characteristics in the 
  population

    - **Example**
      Using geographic location as a proxy for income may skew analysis 

### Cognitive
- People's experiences and preferences can introduce and favor bias or 
  weighting of outcomes or selection of data.


## Mitigation and Responses
How can we mitigate or respond to AI and Machine Learning bias? 

See how the LLM vendors respond and attempt to mitigate bias in their models:

- **OpenAI** Description of using Fine-tuning to addressing bias[^HOW_AI_BEHAVE]

- **Anthropic** Evaluating and Mitigating Discrimination in Language Model Decisions[^CLAUDE_LANG]

- **Google** Gemini for Google Cloud and responsible AI[^GEMINI]

## Workshop Use-cases

### Primary
- [Automated Metadata Generation Enrichment](https://github.com/folio-labs/ai-workflows/wiki/Automated-Metadata-Generation-Enrichment)
- [Collection Management and Optimization](https://github.com/folio-labs/ai-workflows/wiki/Collection-Management-and-Optimization)
- [Information Discovery](https://github.com/folio-labs/ai-workflows/wiki/Information-Discovery)
- [Improving User and Technical Documentation](https://github.com/folio-labs/ai-workflows/wiki/Improving-User-and-Technical-Documentation)

### Secondary
- [Create Course reserves from a csv](https://github.com/folio-labs/ai-workflows/wiki/Create-Course-reserves-from-a-csv)
- [Narrative Circulation Rules](https://github.com/folio-labs/ai-workflows/wiki/Narrative-Circulation-Rules)
- [Technical Support for Orphaned Modules](https://github.com/folio-labs/ai-workflows/wiki/Technical-Support-for-Orphaned-Modules)

### Tertiary
- [Analysis and Management Financial Orders and Invoices](https://github.com/folio-labs/ai-workflows/wiki/Analysis-and-Management-Financial-Orders-and-Invoices)
- [De‐duplicate and Cluster Existing FOLIO Inventory Records](https://github.com/folio-labs/ai-workflows/wiki/De%E2%80%90duplicate-and-Cluster-Existing-FOLIO-Inventory-Records)
- [From an Instance Title, find Circ Status and Researve Item](https://github.com/folio-labs/ai-workflows/wiki/From-an-Instance-Title,-find-Circ-Status-and-Researve-Item)


[^IBM_AI_BIAS]: [Shedding light on AI bias with real world examples](https://www.ibm.com/blog/shedding-light-on-ai-bias-with-real-world-examples/)
[^HOW_AI_BEHAVE]: [How should AI systems behave, and who should decide?](https://openai.com/index/how-should-ai-systems-behave/)
[^CLAUDE_LANG]: [Evaluating and Mitigating Discrimination in Language Model Decisions](https://www.anthropic.com/news/evaluating-and-mitigating-discrimination-in-language-model-decisions)
[^GEMINI]: [Gemini for Google Cloud and responsible AI](https://cloud.google.com/gemini/docs/discover/responsible-ai)
## Resources 
- https://www.nist.gov/news-events/news/2022/03/theres-more-ai-bias-biased-data-nist-report-highlights
- https://lin-web.clarkson.edu/~jmatthew/publications/ManagingBiasInAI_CAMERAREADY.pdf 
