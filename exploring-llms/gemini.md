# Google Gemini
In December of 2023, [Google][GOOG] publicly released their own Large Language Model (LLM)
to compete with OpenAI's ChatGPT. Their service called Gemini, is available at 
[https://gemini.google.com/][GEMINI]. 

[Google][GOOG]'s release of Gemini has faced controversy, including an early version of their image 
generation that was widely criticized for being inaccurate when generating images of historical 
figures.[^GEMINI_PEOPLE]

Google Gemini has the following models available for use through the Gemini API:

- **Gemini 1.5 Flash**: A fast  multimodal model that accepts audio, images, video and text and
  outputs text. It has a text token limit of 1,048,576 with an output token limit of 8,192. It has 
  both a free and pay-as-you-go tiers based on usage.[^1.5FLASH]
- **Gemini 1.5 Pro**: A mid-size multimodal model for a wide-range of reasoning task that accepts
  audio, images, video, text and outputs text. It has a text token limit of 2,097,152 with an output 
  token limit of 8,192. It has both a free and pay-as-you-go tiers based on usage.[^1.5PRO]
- **Gemini 1.0 Pro**: A Natural Language Processing(NLP) model for text, code chat, and code
  generation that accepts text and outputs text.  It has both a free and pay-as-you-go tiers 
  based on usage.[^1.0PRO]

## Using Gemini
Gemini can be used through a [web interface][GEMINI] or programmatically through the Gemini 
[API](https://ai.google.dev/gemini-api). Google provides Python, Go, Node.js, Web, Dart, 
Swift, and Android libraries that wrap the API calls.[^LANG_LIBS]

## Workshop Exercise
Create a Github issue for a DSPy model signature of a FOLIO Circulation Record 

[^GEMINI_PEOPLE]: [Why Google’s AI tool was slammed for showing images of people of colour](https://www.aljazeera.com/news/2024/3/9/why-google-gemini-wont-show-you-white-people)
[^1.5FLASH]: [Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini#gemini-1.5-flash)
[^1.5PRO]: [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini#gemini-1.5-pro)
[^1.0PRO]: [Gemini 1.0 Pro](https://ai.google.dev/gemini-api/docs/models/gemini#gemini-1.5-pro)
[^LANG_LIBS]: [Download or install libraries to access Gemini](https://ai.google.dev/gemini-api/docs/downloads)

[GEMINI]: https://gemini.google.com/
[GOOG]: https://www.google.com/
