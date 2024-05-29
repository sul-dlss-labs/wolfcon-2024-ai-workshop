# Prompt Engineering
To effectively use LLMs and generative AI, you will need to construct a short textual 
description, called a prompt, that the LLM will use to generate text, images, or 
other media. Often, you will need to tweak and change your prompt to improve the LLMs
outputs and iterate a few times until you have a result that meets your need. How 
you construct your prompt will also impact aspects of the model's output, like 
accuracy and verbosity or if you want to customize the style of the output. Together,
a set of techniques and approaches for constructing prompts is collective called 
prompt engineering. 


## General Construction of Prompts

### Examples or Zero Shot
Often, you'll want to include an example of an expected output, particularly for code 
or data outputs, that can help the LLM construct an output that match a certain pattern.

Or, if you do what is called a zero shot prompt, or a prompt with any examples or other 
guidance for the LLM if you don't need or care about the specifics format or construction 
of the LLM's output.

### Chain-of-Thought
Another useful prompt technique is called *chain-of-thought* where you explicitly ask 
the LLM to provide the reasoning or steps the model went through to construct the output.
This can be helpful if you're confused how or why a model return the output to your prompt.

## Tips and Tricks for Prompts



## Resources
- https://github.com/microsoft/promptbase/tree/main
