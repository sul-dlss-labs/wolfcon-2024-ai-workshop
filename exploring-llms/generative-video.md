# Generative AI Images and Videos
The flexibility and power of transformer-based models allow for uses of 
Large Language Models (LLMs) beyond just text. LLMs can be extended to generate audio,
images, and videos with surprising creativity but with some limitations. 

## DALL-E 3
OpenAI text-to-image model [DALL-E 3](https://openai.com/index/dall-e-3/) generates images 
from text prompts. Here is an example of DALL-E image based on the following prompt:
 *Set in a library on a Saturn moon, a robotic librarian looks for a book on a shelf, 
reaches up and opens a book with a title, "AI in FOLIO"*,

![DALL-E Robot in Saturn Moon Library](dalli-robot-in-saturn-library.png)

## Google Gemini
Google's [Gemini][GEMINI] allows you to generate images based on your text descriptions. 
It currently avoids generating images of people due to earlier issues[^GEMINI_PEOPLE] with historical 
figures appearing with incorrect racial or gender characteristics.
 

## Midjourney
Midjourney is a research lab offering a paid Generative AI service for image creation.
It operates through a [Discord](https://discord.com/) server. To use this service, users 
must subscribe to a paid plan and create a Discord account.

Once set up, interact with the Midjourney bot using text prompts to generate images.

## Sora
[OpenAI][OPENAI] recently unveiled [Sora](https://openai.com/index/sora/), a new 
text-to-video model (released February 15, 2024). While not yet available to the public,
 Sora's video demos have generated excitement, with some concerns raised about consistency. 
OpenAI is currently conducting rigorous testing before releasing Sora for wider use. 
Interestingly, Sora attempts to simulate real-world physics for enhanced realism, 
addressing a common criticism of LLMs.

## Luma Labs Dream Machine
[Luma Labs](https://lumalabs.ai/) is a San Francisco Bay area software company that offers 
a text-to-video LLM-based service, [Dream Machine](https://lumalabs.ai/dream-machine). 
Currently you can sign up for and use the service with a Google Account.

### Example:
From this prompt, *Set in a library on a Saturn moon, a robotic librarian looks for a book on a shelf, 
reaches up and opens a book with a title, "AI in FOLIO"*, Dream Machine generated the following video:

<video width="800" height="600" controls>
 <source src="dream-machine-video.mp4" type="video/mp4">
 Your browser does not support the video tag
</video>

## Footnotes
[^GEMINI_PEOPLE]: [Why Google’s AI tool was slammed for showing images of people of colour](https://www.aljazeera.com/news/2024/3/9/why-google-gemini-wont-show-you-white-people)
[GEMINI]: https://gemini.google.com/
[OPENAI]: https://openai.com/
