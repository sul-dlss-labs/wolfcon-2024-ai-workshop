# FOLIOAIthon
In our user case exercises today, we will adopting some technique 
and ideas from hackathons[^WHATIS]. Original held as a start-up activity, 
hackathons are made up of teams in a competition that attempt to solve or
at least speed up software development of specific problems in a particular
industry.

## Team Use-Cases
After each topic area or section, we will break up into small teams, with
each team working on one of the these use-cases. 

Each break-out session will have a theme based on the topics covered 
to brainstorm, write, and experiment
as we improve the wiki pages for the [use-cases](https://github.com/folio-labs/ai-workflows/wiki).
Each team will write Github issues in either 
[edge-ai](https://github.com/folio-labs/edge-ai/issues) or the 
[ai-workflows](https://github.com/folio-labs/ai-workflows/issues) based on the wiki. 
Please be verbose in your Github ticket descriptions and
include example prompts, expected outputs, and even screen-shots from FOLIO.

For those interested in actual hacking code, I suggest coding stub
edge-ai functions and/or Airflow DAGS and create pull-requests referencing the 
issues your group creates.

I encourage each to group to use generative AI in these tasks!

Although we won't be declaring a winner of the hackathon today, informal kudos will go to the
group with the most Github activity in either repository. 


## My Use Case: Automated Metadata Generation Enrichment
I'll go first and illustrate some of the possibilities of what can be done today.

I've been working on the [Automated Metadata Generation Enrichment](https://github.com/folio-labs/ai-workflows/wiki/Automated-Metadata-Generation-Enrichment)
over the past year and have created both [edge-ai](https://github.com/folio-labs/edge-ai/) API calls
and Airflow [DAGs](https://github.com/folio-labs/ai-workflows/tree/main/src/folio_ai_workflows/dags/inventory)
to implement the requirements in this use-case.

[^WHATIS]: [What exactly is a Hackathon?](https://eventornado.com/blog/hackathon-meaning-definition)
