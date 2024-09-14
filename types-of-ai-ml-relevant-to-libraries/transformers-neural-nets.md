# Transformers
Large Language Models (LLMs) are based on a type of neural network called a Transformer.
First specified in a 2017[^ATTENTION] paper by then Google engineers, Transformers are the core
technology behind modern Generative AI models including LLMs. A transformer
neural net architecture improves on a basic task of predicting the next-word in a sentence or 
passage of text by adding a core mechanism called *self-attention* that allows the transformers a
greater ability to place incoming characters within a larger context of the entire text.  

In a simplified transformer model, text is fed into a stack of encoders, where each encoder 
consists of two sub-layers with different weights that process the text as it passes through 
the stack. From there, the text is then sent to a decoder stack, which assembles the predicated 
output text.

## Transformer Demonstration
An online explanation of the Transformer architecture is available at 
[https://poloclub.github.io/transformer-explainer/][EXPLANIER], which uses a live GPT-2 model 
to demonstrate how transformers work with an accompanying article[^EXPLAIN_PAPER].

## Text Embedding
Incoming text to the Transformer is parsed into smaller tokens, which can be a word or portions of
words. A numerical representation of these tokens, called embeddings, are generated that provide
a semantic relationship with other tokens.  

## Encoders
A transformer with multiple, identical encoders with each is made up of the 
following layers:

- **Self-Attention Layer** - helps the encoder consider the context of each word within the
  input sentence. As the model processes each word self attention allows it to look at
  others positions in the input sequence for clues for improving the encoding of the word.
- **Feed Forward Neural Network** - outputs from the self-attention layer are fed to 
  and independently applied to this layer.

The bottom encoder (#0) is the only encoder that directly creates a vector of the word
through an embedding algorithm. All downstream encoders from the first use the output
of vectors generated from the encoder's feed-forward layer.

## Decoders
After the text prompt has been fed through the encoders, the outputs from each of the
encoders are feed to the decoders. A decoder is made of three layers:

- **Self-Attention Layer** - same as the encoder, allows the word in context with the other
  words in the input sentence. 
- **Encoder-Decoder Attention** - a separate layer that assists the decoder in focusing on 
  the relevant parts in the input sentence.
- **Feed Forward Neural Network** 


transformer is like much more amazing it's not just like an it's not just another neural net it's like an amazing
neural nut extremely General uh so for example example when people talk about the scaling loss in neural networks the scaling loss are actually a um a to
[EXPLANIER]: https://poloclub.github.io/transformer-explainer/
[^ATTENTION]: [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
[^EXPLAIN_PAPER]: [Transformer Explainer: Interactive Learning of Text-Generative Models](https://arxiv.org/abs/2408.04619)
