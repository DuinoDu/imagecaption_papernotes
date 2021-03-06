## [Stack-Captioning: Coarse-to-Fine Learning for Image Captioning](https://arxiv.org/abs/1709.03376)

The authors extend LSTM decoder into multi stages, where the latter stage gives captions with more details. To cope with coarse-to-fine decoders, stacked attention model is proposed to provide different attentions on image.

### Contributes
- **multi stage** LSTM decoder.
- **stacked** attention model.

### Previous work
- CNN-LSTM arch. ([Show and Tell: A Neural Image Caption Generator](https://github.com/DuinoDu/imagecaption_papernotes/blob/master/README.md#2014): replace RNNs with LSTM)
- Attention. ([Show, Attend and Tell: Neural Image Caption Generation with Visual Attention](https://github.com/DuinoDu/imagecaption_papernotes/blob/master/README.md#2015): apply _attention_ on image caption)
- Reinforcement Learing. ([Self-critical Sequence Training for Image Captioning](https://github.com/DuinoDu/imagecaption_papernotes/blob/master/README.md#2016): apply RL on image caption)
- Coarse-to-Fine idea. ([Coarse-to-Fine Inference and Learning](http://turing.cs.washington.edu/papers/aaai11-kiddon.pdf))

CIDEr@coco(c5): 114.8  
