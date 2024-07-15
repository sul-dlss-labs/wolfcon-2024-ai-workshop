# Transformers
Large Language Models (LLMs) are a specific type of neural net called a Transformer.
In a simplified transformer model, text is feed into a stack of encoders, where each 
encoder is made of two sub-layers that have different weights that feeds the text 
through the encoders stack and then text is sent to decoder stack that then 
assembles the output text.

## Encoders
A transformer with multiple, identical encoders with each encoder is made up of the 
following layers:

- **Self-Attention Layer** - helps the encoder consider the context of a word in the
  input sentence. As the model processes each word self attention allows it to look at
  others positions in the input sequence for clues for improving the encoding of the word.
- **Feed Forward Neural Network** - outputs from the self-attention layer are feed to 
  and independently applied to this layer.

The bottom encoder (#0) is the only encoder that directly creates a vector of the word
through an embedding algorithm. All downstream encoders from the first use the output
of vectors generated from the encoder's feed-forward layer.

## Decoders
After the text prompt have been feed through the encoders, the outputs from each of the
encoders are feed to the decoders. A decoder is made of three layers:

- **Self-Attention Layer** - same as the encoder, allows the word in context with the other
  words in the input sentence. 
- **Encoder-Decoder Attention** - a separate layer that assists the decoder in focusing on 
  the relevant parts in the input sentence.
- **Feed Forward Neural Network** 



