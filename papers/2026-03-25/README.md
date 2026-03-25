# arXiv Papers - 2026-03-25

**来源**: arXiv (cs.SD, eess.AS, cs.LG, cs.AI)  
**关键词**: speech, audio, music, voice, sound, Mel, representation, self-supervised  
**今日新论文**: 213 篇

---

## 1. LL-SDR: Low-Latency Speech enhancement through Discrete Representations

**Authors**: Jingyi Li, Luca Della Libera, Mirco Ravanelli, Cem Subakan  
**Categories**: cs.SD  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20242  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20242v1.pdf

**Abstract**:
> arXiv:2603.20242v1 Announce Type: new 
Abstract: Many speech enhancement (SE) methods rely on continuous representations. Recently, discrete audio tokens have been explored to enable autoregressive generation for SE. However, it remains unclear whether discretization itself consistently improves SE performance. In this paper, we introduce LL-SDR, a token-based speech enhancement framework that explicitly leverages discretization to better separate speech and noise. Our first contribution is a Variance-Ordered Residual Vector Quantizer (VO-RVQ), designed to disentangle speech and noise distributions during tokenization. Second, we propose a latent-space discriminator to better align enhanced embeddings with semantic embeddings. Experiments show that LL-SDR outperforms continuous baselines a...

---

## 2. Voice Privacy from an Attribute-based Perspective

**Authors**: Mehtab Ur Rahman, Martha Larson, Cristian Tejedor Garc\'ia  
**Categories**: cs.SD  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20301  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20301v1.pdf

**Abstract**:
> arXiv:2603.20301v1 Announce Type: new 
Abstract: Voice privacy approaches that preserve the anonymity of speakers modify speech in an attempt to break the link with the true identity of the speaker. Current benchmarks measure speaker protection based on signal-to-signal comparisons. In this paper, we introduce an attribute-based perspective, where we measure privacy protection in terms of comparisons between sets of speaker attributes. First, we analyze privacy impact by calculating speaker uniqueness for ground truth attributes, attributes inferred on the original speech, and attributes inferred on speech protected with standard anonymization. Next, we examine a threat scenario involving only a single utterance per speaker and calculate attack error rates. Overall, we observe that inferre...

---

## 3. ALICE: A Multifaceted Evaluation Framework of Large Audio-Language Models' In-Context Learning Ability

**Authors**: Yen-Ting Piao, Jay Chiehen Liao, Wei-Tang Chien, Toshiki Ogimoto, Shang-Tse Chen, Yun-Nung Chen, Chu...  
**Categories**: cs.SD  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20433  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20433v1.pdf

**Abstract**:
> arXiv:2603.20433v1 Announce Type: new 
Abstract: While Large Audio-Language Models (LALMs) have been shown to exhibit degraded instruction-following capabilities, their ability to infer task patterns from in-context examples under audio conditioning remains unstudied. To address this gap, we present ALICE, a three-stage framework that progressively reduces textual guidance to systematically evaluate LALMs' in-context learning ability under audio conditioning. Evaluating six LALMs across four audio understanding tasks under two output constraint categories, we uncover a consistent asymmetry across all stages and LALMs: in-context demonstrations reliably improve format compliance but fail to improve, and often degrade, the core task performance. This suggests that LALMs can glean surface-lev...

---

## 4. ERM-MinMaxGAP: Benchmarking and Mitigating Gender Bias in Multilingual Multimodal Speech-LLM Emotion Recognition

**Authors**: Zi Haur Pang, Xiaoxue Gao, Tatsuya Kawahara, Nancy F. Chen  
**Categories**: cs.SD  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21050  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21050v1.pdf

**Abstract**:
> arXiv:2603.21050v1 Announce Type: new 
Abstract: Speech emotion recognition (SER) systems can exhibit gender-related performance disparities, but how such bias manifests in multilingual speech LLMs across languages and modalities is unclear. We introduce a novel multilingual, multimodal benchmark built on MELD-ST, spanning English, Japanese, and German, to quantify language-specific SER performance and gender gaps. We find bias is strongly language-dependent, and multimodal fusion does not reliably improve fairness. To address these, we propose ERM-MinMaxGAP, a fairness-informed training objective, which augments empirical risk minimization (ERM) with a proposed adaptive fairness weight mechanism and a novel MinMaxGAP regularizer on the maximum male-female loss gap within each language and...

---

## 5. Emotion-Aware Quantization for Discrete Speech Representations: An Analysis of Emotion Preservation

**Authors**: Haoguang Zhou, Siyi Wang, Jingyao Wu, James Bailey, Ting Dang  
**Categories**: cs.SD  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21224  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21224v1.pdf

**Abstract**:
> arXiv:2603.21224v1 Announce Type: new 
Abstract: Modern speech systems increasingly use discretized self-supervised speech representations for compression and integration with token-based models, yet their impact on emotional information remains unclear. We study how residual vector quantization (RVQ) reshapes emotional information in discrete speech representations from both representation- and task-level perspectives. Our analysis shows that aggressive compression disproportionately degrades emotion, with uneven loss across emotion classes and model architectures. To address this, we introduce emotion-aware quantization using emotion-specific and emotion-biased codebooks, improving the preservation of both hard and soft emotion perception. We further propose Emo-Q, a lightweight routed q...

---

## 6. HELIX: Scaling Raw Audio Understanding with Hybrid Mamba-Attention Beyond the Quadratic Limit

**Authors**: Khushiyant, Param Thakkar  
**Categories**: cs.SD  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21316  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21316v1.pdf

**Abstract**:
> arXiv:2603.21316v1 Announce Type: new 
Abstract: Audio representation learning typically evaluates design choices such as input frontend, sequence backbone, and sequence length in isolation. We show that these axes are coupled, and conclusions from one setting often do not transfer to others. We introduce HELIX, a controlled framework comparing pure Mamba, pure attention, and a minimal hybrid with a single attention bottleneck. All models are parameter-matched at about 8.3M parameters to isolate architectural effects. Across six datasets, we find that the preferred input representation depends on the backbone, and that attention hurts performance on short, stationary audio but becomes important at longer sequence lengths. On a 5-minute speaker identification task with 30,000 tokens, pure a...

---

## 7. Enterprise Sales Copilot: Enabling Real-Time AI Support with Automatic Information Retrieval in Live Sales Calls

**Authors**: Jielin Qiu, Liangwei Yang, Ming Zhu, Wenting Zhao, Zhiwei Liu, Juntao Tan, Zixiang Chen, Roshan Ram,...  
**Categories**: cs.SD  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21416  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21416v1.pdf

**Abstract**:
> arXiv:2603.21416v1 Announce Type: new 
Abstract: During live sales calls, customers frequently ask detailed product questions that require representatives to manually search internal databases and CRM systems. This process typically takes 25-65 seconds per query, creating awkward pauses that hurt customer experience and reduce sales efficiency. We present SalesCopilot, a real-time AI-powered assistant that eliminates this bottleneck by automatically detecting customer questions, retrieving relevant information from the product database, and displaying concise answers on the representative's dashboard in seconds. The system integrates streaming speech-to-text transcription, large language model (LLM)-based question detection, and retrieval-augmented generation (RAG) over a structured produc...

---

## 8. LipsAM: Lipschitz-Continuous Amplitude Modifier for Audio Signal Processing and its Application to Plug-and-Play Dereverberation

**Authors**: Kazuki Matsumoto, Ren Uchida, Kohei Yatabe  
**Categories**: cs.SD  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21684  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21684v1.pdf

**Abstract**:
> arXiv:2603.21684v1 Announce Type: new 
Abstract: The robustness of deep neural networks (DNNs) can be certified through their Lipschitz continuity, which has made the construction of Lipschitz-continuous DNNs an active research field. However, DNNs for audio processing have not been a major focus due to their poor compatibility with existing results. In this paper, we consider the amplitude modifier (AM), a popular architecture for handling audio signals, and propose its Lipschitz-continuous variants, which we refer to as LipsAM. We prove a sufficient condition for an AM to be Lipschitz continuous and propose two architectures as examples of LipsAM. The proposed architectures were applied to a Plug-and-Play algorithm for speech dereverberation, and their improved stability is demonstrated ...

---

## 9. AnimalCLAP: Taxonomy-Aware Language-Audio Pretraining for Species Recognition and Trait Inference

**Authors**: Risa Shinoda, Kaede Shiohara, Nakamasa Inoue, Hiroaki Santo, Fumio Okura  
**Categories**: cs.SD  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22053  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22053v1.pdf

**Abstract**:
> arXiv:2603.22053v1 Announce Type: new 
Abstract: Animal vocalizations provide crucial insights for wildlife assessment, particularly in complex environments such as forests, aiding species identification and ecological monitoring. Recent advances in deep learning have enabled automatic species classification from their vocalizations. However, classifying species unseen during training remains challenging. To address this limitation, we introduce AnimalCLAP, a taxonomy-aware language-audio framework comprising a new dataset and model that incorporate hierarchical biological information. Specifically, our vocalization dataset consists of 4,225 hours of recordings covering 6,823 species, annotated with 22 ecological traits. The AnimalCLAP model is trained on this dataset to align audio and te...

---

## 10. Abjad-Kids: An Arabic Speech Classification Dataset for Primary Education

**Authors**: Abdul Aziz Snoubara, Baraa Al_Maradni, Haya Al_Naal, Malek Al_Madrmani, Roaa Jdini, Seedra Zarzour, ...  
**Categories**: cs.SD  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20255  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20255v1.pdf

**Abstract**:
> arXiv:2603.20255v1 Announce Type: cross 
Abstract: Speech-based AI educational applications have gained significant interest in recent years, particularly for children. However, children speech research remains limited due to the lack of publicly available datasets, especially for low-resource languages such as Arabic.This paper presents Abjad-Kids, an Arabic speech dataset designed for kindergarten and primary education, focusing on fundamental learning of alphabets, numbers, and colors. The dataset consists of 46397 audio samples collected from children aged 3 - 12 years, covering 141 classes. All samples were recorded under controlled specifications to ensure consistency in duration, sampling rate, and format. To address high intra-class similarity among Arabic phonemes and the limited ...

---

## 11. EARTalking: End-to-end GPT-style Autoregressive Talking Head Synthesis with Frame-wise Control

**Authors**: Yuzhe Weng, Haotian Wang, Yuanhong Yu, Jun Du, Shan He, Xiaoyan Wu, Haoran Xu  
**Categories**: cs.SD  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20307  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20307v1.pdf

**Abstract**:
> arXiv:2603.20307v1 Announce Type: cross 
Abstract: Audio-driven talking head generation aims to create vivid and realistic videos from a static portrait and speech. Existing AR-based methods rely on intermediate facial representations, which limit their expressiveness and realism. Meanwhile, diffusion-based methods generate clip-by-clip, lacking fine-grained control and causing inherent latency due to overall denoising across the window. To address these limitations, we propose EARTalking, a novel end-to-end, GPT-style autoregressive model for interactive audio-driven talking head generation. Our method introduces a novel frame-by-frame, in-context, audio-driven streaming generation paradigm. For inherently supporting variable-length video generation with identity consistency, we propose t...

---

## 12. End-to-End Multi-Task Learning for Adjustable Joint Noise Reduction and Hearing Loss Compensation

**Authors**: Philippe Gonzalez, Vera Margrethe Frederiksen, Torsten Dau, Tobias May  
**Categories**: cs.SD  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20387  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20387v1.pdf

**Abstract**:
> arXiv:2603.20387v1 Announce Type: cross 
Abstract: A multi-task learning framework is proposed for optimizing a single deep neural network (DNN) for joint noise reduction (NR) and hearing loss compensation (HLC). A distinct training objective is defined for each task, and the DNN predicts two time-frequency masks. During inference, the amounts of NR and HLC can be adjusted independently by exponentiating each mask before combining them. In contrast to recent approaches that rely on training an auditory-model emulator to define a differentiable training objective, we propose an auditory model that is inherently differentiable, thus allowing end-to-end optimization. The audiogram is provided as an input to the DNN, thereby enabling listener-specific personalization without the need for retra...

---

## 13. SqueezeComposer: Temporal Speed-up is A Simple Trick for Long-form Music Composing

**Authors**: Jianyi Chen, Rongxiu Zhong, Shilei Zhang, Kun Qian, Jinglei Liu, Yike Guo, Wei Xue  
**Categories**: cs.SD  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21073  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21073v1.pdf

**Abstract**:
> arXiv:2603.21073v1 Announce Type: cross 
Abstract: Composing coherent long-form music remains a significant challenge due to the complexity of modeling long-range dependencies and the prohibitive memory and computational requirements associated with lengthy audio representations. In this work, we propose a simple yet powerful trick: we assume that AI models can understand and generate time-accelerated (speeded-up) audio at rates such as 2x, 4x, or even 8x. By first generating a high-speed version of the music, we greatly reduce the temporal length and resource requirements, making it feasible to handle long-form music that would otherwise exceed memory or computational limits. The generated audio is then restored to its original speed, recovering the full temporal structure. This temporal ...

---

## 14. Assessing the Ability of Neural TTS Systems to Model Consonant-Induced F0 Perturbation

**Authors**: Tianle Yang, Chengzhe Sun, Phil Rose, Cassandra L. Jacobs, Siwei Lyu  
**Categories**: cs.SD  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21078  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21078v1.pdf

**Abstract**:
> arXiv:2603.21078v1 Announce Type: cross 
Abstract: This study proposes a segmental-level prosodic probing framework to evaluate neural TTS models' ability to reproduce consonant-induced f0 perturbation, a fine-grained segmental-prosodic effect that reflects local articulatory mechanisms. We compare synthetic and natural speech realizations for thousands of words, stratified by lexical frequency, using Tacotron 2 and FastSpeech 2 trained on the same speech corpus (LJ Speech). These controlled analyses are then complemented by a large-scale evaluation spanning multiple advanced TTS systems. Results show accurate reproduction for high-frequency words but poor generalization to low-frequency items, suggesting that the examined TTS architectures rely more on lexical-level memorization than on a...

---

## 15. Fusing Memory and Attention: A study on LSTM, Transformer and Hybrid Architectures for Symbolic Music Generation

**Authors**: Soudeep Ghoshal, Sandipan Chakraborty, Pradipto Chowdhury, Himanshu Buckchash  
**Categories**: cs.SD  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21282  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21282v1.pdf

**Abstract**:
> arXiv:2603.21282v1 Announce Type: cross 
Abstract: Machine learning techniques, such as Transformers and Long Short-Term Memory (LSTM) networks, play a crucial role in Symbolic Music Generation (SMG). Existing literature indicates a difference between LSTMs and Transformers regarding their ability to model local melodic continuity versus maintaining global structural coherence. However, their specific properties within the context of SMG have not been systematically studied. This paper addresses this gap by providing a fine-grained comparative analysis of LSTMs versus Transformers for SMG, examining local and global properties in detail using 17 musical quality metrics on the Deutschl dataset. We find that LSTM networks excel at capturing local patterns but fail to preserve long-range depe...

---

## 16. DiT-Flow: Speech Enhancement Robust to Multiple Distortions based on Flow Matching in Latent Space and Diffusion Transformers

**Authors**: Tianyu Cao, Helin Wang, Ari Frummer, Yuval Sieradzki, Adi Arbel, Laureano Moro Velazquez, Jesus Vill...  
**Categories**: cs.SD  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21608  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21608v1.pdf

**Abstract**:
> arXiv:2603.21608v1 Announce Type: cross 
Abstract: Recent advances in generative models, such as diffusion and flow matching, have shown strong performance in audio tasks. However, speech enhancement (SE) models are typically trained on limited datasets and evaluated under narrow conditions, limiting real-world applicability. To address this, we propose DiT-Flow, a flow matching-based SE framework built on the latent Diffusion Transformer (DiT) backbone and trained for robustness across diverse distortions, including noise, reverberation, and compression. DiT-Flow operates on compact variational auto-encoders (VAEs)-derived latent features. We validated our approach on StillSonicSet, a synthetic yet acoustically realistic dataset composed of LibriSpeech, FSD50K, FMA, and 90 Matterport3D sc...

---

## 17. Disentangling Speaker Traits for Deepfake Source Verification via Chebyshev Polynomial and Riemannian Metric Learning

**Authors**: Xi Xuan, Wenxin Zhang, Zhiyu Li, Jennifer Williams, Ville Hautam\"aki, Tomi H. Kinnunen  
**Categories**: cs.SD  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21875  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21875v1.pdf

**Abstract**:
> arXiv:2603.21875v1 Announce Type: cross 
Abstract: Speech deepfake source verification systems aims to determine whether two synthetic speech utterances originate from the same source generator, often assuming that the resulting source embeddings are independent of speaker traits. However, this assumption remains unverified. In this paper, we first investigate the impact of speaker factors on source verification. We propose a speaker-disentangled metric learning (SDML) framework incorporating two novel loss functions. The first leverages Chebyshev polynomial to mitigate gradient instability during disentanglement optimization. The second projects source and speaker embeddings into hyperbolic space, leveraging Riemannian metric distances to reduce speaker information and learn more discrimi...

---

## 18. Adapting Self-Supervised Speech Representations for Cross-lingual Dysarthria Detection in Parkinson's Disease

**Authors**: Abner Hernandez, Eunjung Yeo, Kwanghee Choi, Chin-Jou Li, Zhengjun Yue, Rohan Kumar Das, Jan Rusz, M...  
**Categories**: cs.SD  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22225  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22225v1.pdf

**Abstract**:
> arXiv:2603.22225v1 Announce Type: cross 
Abstract: The limited availability of dysarthric speech data makes cross-lingual detection an important but challenging problem. A key difficulty is that speech representations often encode language-dependent structure that can confound dysarthria detection. We propose a representation-level language shift (LS) that aligns source-language self-supervised speech representations with the target-language distribution using centroid-based vector adaptation estimated from healthy-control speech. We evaluate the approach on oral DDK recordings from Parkinson's disease speech datasets in Czech, German, and Spanish under both cross-lingual and multilingual settings. LS substantially improves sensitivity and F1 in cross-lingual settings, while yielding small...

---

## 19. A Multimodal Data Fusion Generative Adversarial Network for Real Time Underwater Sound Speed Field Construction

**Authors**: Wei Huang, Yuqiang Huang, Yanan Wu, Tianhe Xu, Tingting Lyu, Hao Zhang  
**Categories**: cs.SD  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2507.11812  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2507.11812v2.pdf

**Abstract**:
> arXiv:2507.11812v2 Announce Type: replace 
Abstract: Sound speed profiles (SSPs) are essential parameters underwater that affects the propagation mode of underwater signals and has a critical impact on the energy efficiency of underwater acoustic communication and accuracy of underwater acoustic positioning. Traditionally, SSPs can be obtained by matching field processing (MFP), compressive sensing (CS), and deep learning (DL) methods. However, existing methods mainly rely on on-site underwater sonar observation data, which put forward strict requirements on the deployment of sonar observation systems. To achieve high-precision estimation of sound velocity distribution in a given sea area without on-site underwater data measurement, we propose a multi-modal data-fusion generative adversari...

---

## 20. Multi-Task Instruction Tuning via Data Scheduling for Low-Resource Arabic AudioLLMs

**Authors**: Hunzalah Hassan Bhatti, Firoj Alam, Shammur Absar Chowdhury  
**Categories**: cs.SD  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2601.12494  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2601.12494v2.pdf

**Abstract**:
> arXiv:2601.12494v2 Announce Type: replace 
Abstract: Audio large language models (LLMs) enable unified speech understanding and generation, but adapting them to linguistically complex and dialect-rich settings such as Arabic-English remains challenging. We present a controlled study of multi-task instruction tuning for an Arabic-centric audio LLM across generative tasks including ASR and speech and text summarization, and discriminative tasks including dialect and emotion recognition, in a resource-constrained setting. To support end-to-end Arabic speech summarization, we introduce AraMega-SSum, a first speech summarization resource for training and benchmarking Arabic-centric Audio-LLMs. We compare four training strategies (i) Uniform Task Mixing, (ii) Task-Progressive Curriculum (TPC), (...

---

## 21. CALM: Class-Conditional Sparse Attention Vectors for Large Audio-Language Models

**Authors**: Videet Mehta, Liming Wang, Hilde Kuehne, Rogerio Feris, James R. Glass, M. Jehanzeb Mirza  
**Categories**: cs.SD  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.07077  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.07077v2.pdf

**Abstract**:
> arXiv:2602.07077v2 Announce Type: replace 
Abstract: Large audio-language models (LALMs) exhibit strong zero-shot capabilities in multiple downstream tasks, such as audio question answering (AQA) and abstract reasoning; however, these models still lag behind specialized models for certain discriminative tasks (e.g., audio classification). Recent studies show that sparse subsets of attention heads within an LALM can serve as strong discriminative feature extractors for downstream tasks such as classification via simple voting schemes. However, these methods assign uniform weights to all selected heads, implicitly assuming that each head contributes equally across all semantic categories. In this work, we propose Class-Conditional Sparse Attention Vectors for Large Audio-Language Models, a f...

---

## 22. VorTEX: Various overlap ratio for Target speech EXtraction

**Authors**: Ro-hoon Oh, Jihwan Seol, Bugeun Kim  
**Categories**: cs.SD  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14803  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14803v3.pdf

**Abstract**:
> arXiv:2603.14803v3 Announce Type: replace 
Abstract: Target speech extraction (TSE) aims to recover a target speaker's voice from a mixture. While recent text-prompted approaches have shown promise, most approaches assume fully overlapped mixtures, limiting insight into behavior across realistic overlap ratios. We introduce VorTEX (Various overlap ratio for Target speech EXtraction), a text-prompted TSE architecture with a Decoupled Adaptive Multi-branch (DAM) Fusion block that separates primary extraction from auxiliary regularization pathways. To enable controlled analysis, we construct PORTE, a two-speaker dataset spanning overlap ratios from 0% to 100%. We further propose Suppression Ratio on Energy (SuRE), a diagnostic metric that detects suppression behavior not captured by conventio...

---

## 23. Preliminary sonification of ENSO using traditional Javanese gamelan scales

**Authors**: Sandy Hardian Susanto Herho, Rusmawan Suwarman, Nurjanna Joko Trilaksono, Iwan Pramesti Anwar, Faiz ...  
**Categories**: cs.SD  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.14560  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.14560v2.pdf

**Abstract**:
> arXiv:2602.14560v2 Announce Type: replace-cross 
Abstract: Sonification -- the mapping of data to non-speech audio -- offers an underexplored channel for representing complex dynamical systems. We treat El Ni\~{n}o-Southern Oscillation (ENSO), a canonical example of low-dimensional climate chaos, as a test case for culturally-situated sonification evaluated through complex systems diagnostics. Using parameter-mapping sonification of the Ni\~{n}o 3.4 sea surface temperature anomaly index (1870--2024), we encode ENSO variability into two traditional Javanese gamelan pentatonic systems (pelog and slendro) across four composition strategies, then analyze the resulting audio as trajectories in a two-dimensional acoustic phase space. Recurrence-based diagnostics, convex hull geometry, and coupli...

---

## 24. OmniCodec: Low Frame Rate Universal Audio Codec with Semantic-Acoustic Disentanglement

**Authors**: Jingbin Hu, Haoyu Zhang, Dake Guo, Qirui Zhan, Wenhao Li, Huakang Chen, Guobin Ma, Hanke Xie, Chengy...  
**Categories**: eess.AS  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20638  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20638v1.pdf

**Abstract**:
> arXiv:2603.20638v1 Announce Type: new 
Abstract: Large Language Models (LLMs) have advanced audio generation through discrete representation learning. However, most existing neural codecs focus on speech and emphasize reconstruction fidelity, overlooking unified low frame rate modeling across diverse audio domains, including speech, music, and general sound. Moreover, high reconstruction quality does not necessarily yield semantically informative representations, limiting effectiveness in downstream generation tasks. We propose OmniCodec, a universal neural audio codec tailored for low frame rate. It adopts a hierarchical multi-codebook design with semantic-acoustic decoupling by leveraging the audio encoder of the pre-trained understanding model, along with a self-guidance strategy to imp...

---

## 25. Adaptive Federated Fine-Tuning of Self-Supervised Speech Representations

**Authors**: Xin Guo, Chunrui Zhao, Hong Jia, Ting Dang, Gongping Huang, Xianrui Zheng, Yan Gao  
**Categories**: eess.AS  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21888  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21888v1.pdf

**Abstract**:
> arXiv:2603.21888v1 Announce Type: new 
Abstract: Integrating Federated Learning (FL) with self-supervised learning (SSL) enables privacy-preserving fine-tuning for speech tasks. However, federated environments exhibit significant heterogeneity: clients differ in computational capacity, causing straggler effects under unified fine-tuning, while diverse downstream tasks require different representation depths, making full-model updates inefficient. To address these challenges, we propose an adaptive federated fine-tuning framework with early exits. Lightweight prediction heads are inserted at intermediate layers of the SSL backbone, allowing clients to terminate computation based on local constraints and task requirements. We further introduce a layer-wise, depth-aware partial aggregation st...

---

## 26. TaigiSpeech: A Low-Resource Real-World Speech Intent Dataset and Preliminary Results with Scalable Data Mining In-the-Wild

**Authors**: Kai-Wei Chang, Yi-Cheng Lin, Huang-Cheng Chou, Wenze Ren, Yu-Han Huang, Yun-Shao Tsai, Chien-Cheng C...  
**Categories**: eess.AS  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21478  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21478v1.pdf

**Abstract**:
> arXiv:2603.21478v1 Announce Type: cross 
Abstract: Speech technologies have advanced rapidly and serve diverse populations worldwide. However, many languages remain underrepresented due to limited resources. In this paper, we introduce \textbf{TaigiSpeech}, a real-world speech intent dataset in Taiwanese Taigi (aka Taiwanese Hokkien/Southern Min), which is a low-resource and primarily spoken language. The dataset is collected from older adults, comprising 21 speakers with a total of 3k utterances. It is designed for practical intent detection scenarios, including healthcare and home assistant applications. To address the scarcity of labeled data, we explore two data mining strategies with two levels of supervision: keyword match data mining with LLM pseudo labeling via an intermediate lang...

---

## 27. TiCo: Time-Controllable Training for Spoken Dialogue Models

**Authors**: Kai-Wei Chang, Wei-Chih Chen, En-Pei Hu, Hung-yi Lee, James Glass  
**Categories**: eess.AS  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22267  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22267v1.pdf

**Abstract**:
> arXiv:2603.22267v1 Announce Type: cross 
Abstract: We propose TiCo, a simple post-training method for enabling spoken dialogue models (SDMs) to follow time-constrained instructions and generate responses with controllable duration. This capability is valuable for real-world spoken language systems such as voice assistants and interactive agents, where controlling response duration can improve interaction quality. However, despite their strong ability to generate natural spoken responses, existing models lack time awareness and struggle to follow duration-related instructions (e.g., "Please generate a response lasting about 15 seconds"). Through an empirical evaluation of both open-source and commercial SDMs, we show that they frequently fail to satisfy such time-control requirements. TiCo ...

---

## 28. Neural Directional Filtering Using a Compact Microphone Array

**Authors**: Weilong Huang, Srikanth Raj Chetupalli, Mhd Modar Halimeh, Oliver Thiergart, Emanu\"el A. P. Habets  
**Categories**: eess.AS  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2511.07185  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2511.07185v4.pdf

**Abstract**:
> arXiv:2511.07185v4 Announce Type: replace 
Abstract: Beamforming with desired directivity patterns using compact microphone arrays is essential in many audio applications. Directivity patterns achievable using traditional beamformers depend on the number of microphones and the array aperture. Generally, their effectiveness degrades for compact arrays. To overcome these limitations, we propose a neural directional filtering (NDF) approach that leverages deep neural networks to enable sound capture with a predefined directivity pattern. The NDF computes a single-channel complex mask from the microphone array signals, which is then applied to a reference microphone to produce an output that approximates a virtual directional microphone with the desired directivity pattern. We introduce traini...

---

## 29. TRI-DEP: A Trimodal Comparative Study for Depression Detection Using Speech, Text, and EEG

**Authors**: Annisaa Fitri Nurfidausi, Eleonora Mancini, Paolo Torroni  
**Categories**: eess.AS  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.14922  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.14922v2.pdf

**Abstract**:
> arXiv:2510.14922v2 Announce Type: replace-cross 
Abstract: Depression is a widespread mental health disorder, yet its automatic detection remains challenging. Prior work has explored unimodal and multimodal approaches, with multimodal systems showing promise by leveraging complementary signals. However, existing studies are limited in scope, lack systematic comparisons of features, and suffer from inconsistent evaluation protocols. We address these gaps by systematically exploring feature representations and modelling strategies across EEG, together with speech and text. We evaluate handcrafted features versus pre-trained embeddings, assess the effectiveness of different neural encoders, compare unimodal, bimodal, and trimodal configurations, and analyse fusion strategies with attention to...

---

## 30. Transformer-Based Predictive Maintenance for Risk-Aware Instrument Calibration

**Authors**: Adithya Parthasarathy, Aswathnarayan Muthukrishnan Kirubakaran, Akshay Deshpande, Ram Sekhar Bodala,...  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20297  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20297v1.pdf

**Abstract**:
> arXiv:2603.20297v1 Announce Type: new 
Abstract: Accurate calibration is essential for instruments whose measurements must remain traceable, reliable, and compliant over long operating periods. Fixed-interval programs are easy to administer, but they ignore that instruments drift at different rates under different conditions. This paper studies calibration scheduling as a predictive maintenance problem: given recent sensor histories, estimate time-to-drift (TTD) and intervene before a violation occurs. We adapt the NASA C-MAPSS benchmark into a calibration setting by selecting drift-sensitive sensors, defining virtual calibration thresholds, and inserting synthetic reset events that emulate repeated recalibration. We then compare classical regressors, recurrent and convolutional sequence m...

---

## 31. Probing the Latent World: Emergent Discrete Symbols and Physical Structure in Latent Representations

**Authors**: Liu hung ming  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20327  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20327v1.pdf

**Abstract**:
> arXiv:2603.20327v1 Announce Type: new 
Abstract: Video world models trained with Joint Embedding Predictive Architectures (JEPA) acquire rich spatiotemporal representations by predicting masked regions in latent space rather than reconstructing pixels. This removes the visual verification pathway of generative models, creating a structural interpretability gap: the encoder has learned physical structure inaccessible in any inspectable form. Existing probing methods either operate in continuous space without a structured intermediate layer, or attach generative components whose parameters confound attribution of behavior to the encoder.
  We propose the AI Mother Tongue (AIM) framework as a passive quantization probe: a lightweight, vocabulary-free probe that converts V-JEPA 2 continuous la...

---

## 32. Bounded Coupled AI Learning Dynamics in Tri-Hierarchical Drone Swarms

**Authors**: Oleksii Bychkov  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20333  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20333v1.pdf

**Abstract**:
> arXiv:2603.20333v1 Announce Type: new 
Abstract: Modern autonomous multi-agent systems combine heterogeneous learning mechanisms operating at different timescales. An open question remains: can one formally guarantee that coupled dynamics of such mechanisms stay within the admissible operational regime? This paper studies a tri-hierarchical swarm learning system where three mechanisms act simultaneously: (1) local Hebbian online learning at individual agent level (fast timescale, 10-100 ms); (2) multi-agent reinforcement learning (MARL) for tactical group coordination (medium timescale, 1-10 s); (3) meta-learning (MAML) for strategic adaptation (slow timescale, 10-100 s). Four results are established. The Bounded Total Error Theorem shows that under contractual constraints on learning rate...

---

## 33. KV Cache Optimization Strategies for Scalable and Efficient LLM Inference

**Authors**: Yichun Xu, Navjot K. Khaira, Tejinder Singh  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20397  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20397v1.pdf

**Abstract**:
> arXiv:2603.20397v1 Announce Type: new 
Abstract: The key-value (KV) cache is a foundational optimization in Transformer-based large language models (LLMs), eliminating redundant recomputation of past token representations during autoregressive generation. However, its memory footprint scales linearly with context length, imposing critical bottlenecks on GPU memory capacity, memory bandwidth, and inference throughput as production LLMs push context windows from thousands to millions of tokens. Efficient KV cache management has thus become a first-order challenge for scalable LLM deployment. This paper provides a systematic review of recent KV cache optimization techniques, organizing them into five principal directions: cache eviction, cache compression, hybrid memory solutions, novel atten...

---

## 34. Thinking in Different Spaces: Domain-Specific Latent Geometry Survives Cross-Architecture Translation

**Authors**: Marcus Armstrong, Navid Ayoobi, Arjun Mukherjee  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20406  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20406v1.pdf

**Abstract**:
> arXiv:2603.20406v1 Announce Type: new 
Abstract: We investigate whether independently trained language models converge to geometrically compatible latent representations, and whether this compatibility can be exploited to correct model behavior at inference time without any weight updates. We learn a linear projection matrix that maps activation vectors from a large teacher model into the coordinate system of a smaller student model, then intervene on the student's residual stream during generation by substituting its internal state with the translated teacher representation. Across a fully crossed experimental matrix of 20 heterogeneous teacher-student pairings spanning mixture-of-experts, dense, code-specialized, and synthetically trained architectures, the Ridge projection consistently ...

---

## 35. Detecting Neurovascular Instability from Multimodal Physiological Signals Using Wearable-Compatible Edge AI: A Responsible Computational Framework

**Authors**: Truong Quynh Hoa, Hoang Dinh Cuong, Truong Xuan Khanh  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20442  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20442v1.pdf

**Abstract**:
> arXiv:2603.20442v1 Announce Type: new 
Abstract: We propose Melaguard, a multimodal ML framework (Transformer-lite, 1.2M parameters, 4-head self-attention) for detecting neurovascular instability (NVI) from wearable-compatible physiological signals prior to structural stroke pathology. The model fuses heart rate variability (HRV), peripheral perfusion index, SpO2, and bilateral phase coherence into a composite NVI Score, designed for edge inference (WCET <=4 ms on Cortex-M4). NVI - the pre-structural dysregulation of cerebrovascular autoregulation preceding overt stroke - remains undetectable by existing single-modality wearables. With 12.2 million incident strokes annually, continuous multimodal physiological monitoring offers a practical path to community-scale screening. Three-stage ind...

---

## 36. SDE-Driven Spatio-Temporal Hypergraph Neural Networks for Irregular Longitudinal fMRI Connectome Modeling in Alzheimer's Disease

**Authors**: Ruiying Chen, Yutong Wang, Houliang Zhou, Wei Liang, Yong Chen, Lifang He  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20452  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20452v1.pdf

**Abstract**:
> arXiv:2603.20452v1 Announce Type: new 
Abstract: Longitudinal neuroimaging is essential for modeling disease progression in Alzheimer's disease (AD), yet irregular sampling and missing visits pose substantial challenges for learning reliable temporal representations. To address this challenge, we propose SDE-HGNN, a stochastic differential equation (SDE)-driven spatio-temporal hypergraph neural network for irregular longitudinal fMRI connectome modeling. The framework first employs an SDE-based reconstruction module to recover continuous latent trajectories from irregular observations. Based on these reconstructed representations, dynamic hypergraphs are constructed to capture higher-order interactions among brain regions over time. To further model temporal evolution, hypergraph convoluti...

---

## 37. From Data to Laws: Neural Discovery of Conservation Laws Without False Positives

**Authors**: Rahul D Ray  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20474  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20474v1.pdf

**Abstract**:
> arXiv:2603.20474v1 Announce Type: new 
Abstract: Conservation laws are fundamental to understanding dynamical systems, but discovering them from data remains challenging due to parameter variation, non-polynomial invariants, local minima, and false positives on chaotic systems. We introduce NGCG, a neural-symbolic pipeline that decouples dynamics learning from invariant discovery and systematically addresses these challenges. A multi-restart variance minimiser learns a near-constant latent representation; system-specific symbolic extraction (polynomial Lasso, log-basis Lasso, explicit PDE candidates, and PySR) yields closed-form expressions; a strict constancy gate and diversity filter eliminate spurious laws. On a benchmark of nine diverse systems including Hamiltonian and dissipative ODE...

---

## 38. RECLAIM: Cyclic Causal Discovery Amid Measurement Noise

**Authors**: Muralikrishnna G. Sethuraman, Faramarz Fekri  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20585  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20585v1.pdf

**Abstract**:
> arXiv:2603.20585v1 Announce Type: new 
Abstract: Uncovering causal relationships is a fundamental problem across science and engineering. However, most existing causal discovery methods assume acyclicity and direct access to the system variables -- assumptions that fail to hold in many real-world settings. For instance, in genomics, cyclic regulatory networks are common, and measurements are often corrupted by instrumental noise. To address these challenges, we propose RECLAIM, a causal discovery framework that natively handles both cycles and measurement noise. RECLAIM learns the causal graph structure by maximizing the likelihood of the observed measurements via expectation-maximization (EM), using residual normalizing flows for tractable likelihood computation. We consider two measureme...

---

## 39. MKA: Memory-Keyed Attention for Efficient Long-Context Reasoning

**Authors**: Dong Liu, Yanxuan Yu, Ben Lengerich, Ying Nian Wu  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20586  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20586v1.pdf

**Abstract**:
> arXiv:2603.20586v1 Announce Type: new 
Abstract: As long-context language modeling becomes increasingly important, the cost of maintaining and attending to large Key/Value (KV) caches grows rapidly, becoming a major bottleneck in both training and inference. While prior works such as Multi-Query Attention (MQA) and Multi-Latent Attention (MLA) reduce memory by sharing or compressing KV features, they often trade off representation quality or incur runtime overhead. We propose Memory-Keyed Attention (MKA), a hierarchical attention mechanism that integrates multi-level KV caches (local, session, and long-term) and learns to route attention across them dynamically. We further introduce Route-Fused MKA (FastMKA), a broadcast-routed variant that fuses memory sources before attention computation...

---

## 40. Optimal low-rank stochastic gradient estimation for LLM training

**Authors**: Zehao Li, Tao Ren, Zishi Zhang, Xi Chen, Yijie Peng  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20632  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20632v1.pdf

**Abstract**:
> arXiv:2603.20632v1 Announce Type: new 
Abstract: Large language model (LLM) training is often bottlenecked by memory constraints and stochastic gradient noise in extremely high-dimensional parameter spaces. Motivated by empirical evidence that many LLM gradient matrices are effectively low-rank during training, we present an unbiased, memory-efficient, low-rank matrix estimator with the lowest variance that is applicable across common stochastic gradient estimation paradigms. The core idea is to project a high-dimensional stochastic gradient estimator onto a random low-dimensional subspace and lift it back, reducing memory while keeping the estimator unbiased and controlling mean-squared error via an optimally designed projection distribution, including Haar--Stiefel projections. The proje...

---

## 41. Neuronal Self-Adaptation Enhances Capacity and Robustness of Representation in Spiking Neural Networks

**Authors**: Zhuobin Yang, Yeyao Bao, Liangfu Lv, Jian Zhang, Xiaohong Li, Yunliang Zang  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20687  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20687v1.pdf

**Abstract**:
> arXiv:2603.20687v1 Announce Type: new 
Abstract: Spiking Neural Networks (SNNs) are promising for energy-efficient, real-time edge computing, yet their performance is often constrained by the limited adaptability of conventional leaky integrate-and-fire (LIF) neurons. Existing LIF models struggle with restricted information capacity and susceptibility to noise, leading to degraded accuracy and compromised robustness. Inspired by the dynamic self-regulation of biological potassium channels, we propose the Potassium-regulated LIF (KvLIF) neuron model. KvLIF introduces an auxiliary conductance state that integrates membrane potential and spiking history to adaptively modulate neuronal excitability and reset dynamics. This design extends the dynamic response range of neurons to varying input i...

---

## 42. Cross-Granularity Representations for Biological Sequences: Insights from ESM and BiGCARP

**Authors**: Hanlin Xiao, Rainer Breitling, Eriko Takano, Mauricio A. \'Alvarez  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20825  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20825v1.pdf

**Abstract**:
> arXiv:2603.20825v1 Announce Type: new 
Abstract: Recent advances in general-purpose foundation models have stimulated the development of large biological sequence models. While natural language shows symbolic granularity (characters, words, sentences), biological sequences exhibit hierarchical granularity whose levels (nucleotides, amino acids, protein domains, genes) further encode biologically functional information. In this paper, we investigate the integration of cross-granularity knowledge from models through a case study of BiGCARP, a Pfam domain-level model for biosynthetic gene clusters, and ESM, an amino acid-level protein language model. Using representation analysis tools and a set of probe tasks, we first explain why a straightforward cross-model embedding initialization fails ...

---

## 43. Beyond the Academic Monoculture: A Unified Framework and Industrial Perspective for Attributed Graph Clustering

**Authors**: Yunhui Liu, Yue Liu, Yongchao Liu, Tao Zheng, Stan Z. Li, Xinwang Liu, Tieke He  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20829  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20829v1.pdf

**Abstract**:
> arXiv:2603.20829v1 Announce Type: new 
Abstract: Attributed Graph Clustering (AGC) is a fundamental unsupervised task that partitions nodes into cohesive groups by jointly modeling structural topology and node attributes. While the advent of graph neural networks and self-supervised learning has catalyzed a proliferation of AGC methodologies, a widening chasm persists between academic benchmark performance and the stringent demands of real-world industrial deployment. To bridge this gap, this survey provides a comprehensive, industrially grounded review of AGC from three complementary perspectives. First, we introduce the Encode-Cluster-Optimize taxonomic framework, which decomposes the diverse algorithmic landscape into three orthogonal, composable modules: representation encoding, cluste...

---

## 44. Semantic Sections: An Atlas-Native Feature Ontology for Obstructed Representation Spaces

**Authors**: Hossein Javidnia  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20867  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20867v1.pdf

**Abstract**:
> arXiv:2603.20867v1 Announce Type: new 
Abstract: Recent interpretability work often treats a feature as a single global direction, dictionary atom, or latent coordinate shared across contexts. We argue that this ontology can fail in obstructed representation spaces, where locally coherent meanings need not assemble into one globally consistent feature. We introduce an atlas-native replacement object, the semantic section: a transport-compatible family of local feature representatives defined over a context atlas. We formalize semantic sections, prove that tree-supported propagation is always pathwise realizable, and show that cycle consistency is the key criterion for genuine globalization. This yields a distinction between tree-local, globalizable, and twisted sections, with twisted secti...

---

## 45. Discriminative Representation Learning for Clinical Prediction

**Authors**: Yang Zhang, Li Fan, Samuel Lawrence, Shi Li  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20921  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20921v1.pdf

**Abstract**:
> arXiv:2603.20921v1 Announce Type: new 
Abstract: Foundation models in healthcare have largely adopted self supervised pretraining objectives inherited from natural language processing and computer vision, emphasizing reconstruction and large scale representation learning prior to downstream adaptation. We revisit this paradigm in outcome centric clinical prediction settings and argue that, when high quality supervision is available, direct outcome alignment may provide a stronger inductive bias than generative pretraining. We propose a supervised deep learning framework that explicitly shapes representation geometry by maximizing inter class separation relative to within class variance, thereby concentrating model capacity along clinically meaningful axes. Across multiple longitudinal elec...

---

## 46. Understanding Contextual Recall in Transformers: How Finetuning Enables In-Context Reasoning over Pretraining Knowledge

**Authors**: Bhavya Vasudeva, Puneesh Deora, Alberto Bietti, Vatsal Sharan, Christos Thrampoulidis  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20969  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20969v1.pdf

**Abstract**:
> arXiv:2603.20969v1 Announce Type: new 
Abstract: Transformer-based language models excel at in-context learning (ICL), where they can adapt to new tasks based on contextual examples, without parameter updates. In a specific form of ICL, which we refer to as \textit{contextual recall}, models pretrained on open-ended text leverage pairwise examples to recall specific facts in novel prompt formats. We investigate whether contextual recall emerges from pretraining alone, what finetuning is required, and what mechanisms drive the necessary representations. For this, we introduce a controlled synthetic framework where pretraining sequences consist of subject-grammar-attribute tuples, with attribute types tied to grammar statistics. We demonstrate that while such pretraining successfully yields ...

---

## 47. From Causal Discovery to Dynamic Causal Inference in Neural Time Series

**Authors**: Valentina Kuskova, Dmitry Zaytsev, Michael Coppedge  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20980  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20980v1.pdf

**Abstract**:
> arXiv:2603.20980v1 Announce Type: new 
Abstract: Time-varying causal models provide a powerful framework for studying dynamic scientific systems, yet most existing approaches assume that the underlying causal network is known a priori - an assumption rarely satisfied in real-world domains where causal structure is uncertain, evolving, or only indirectly observable. This limits the applicability of dynamic causal inference in many scientific settings. We propose Dynamic Causal Network Autoregression (DCNAR), a two-stage neural causal modeling framework that integrates data-driven causal discovery with time-varying causal inference. In the first stage, a neural autoregressive causal discovery model learns a sparse directed causal network from multivariate time series. In the second stage, th...

---

## 48. When Does Content-Based Routing Work? Representation Requirements for Selective Attention in Hybrid Sequence Models

**Authors**: Abhinaba Basu  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20997  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20997v1.pdf

**Abstract**:
> arXiv:2603.20997v1 Announce Type: new 
Abstract: We identify a routing paradox in hybrid recurrent-attention architectures: content-based routing - deciding which tokens deserve expensive attention - requires exactly the pairwise computation that routing is designed to avoid. Through 20+ controlled experiments across three tasks (a synthetic diagnostic, the Zoology MQAR benchmark, and HotpotQA), we map the routing landscape exhaustively. One layer of softmax attention creates a latent ~34-dimensional subspace enabling 98.4% routing precision; zero layers yield 1.2%. This subspace is invisible to cosine similarity, destroyed by random projections (98.4% to 2.6%), and cannot be created by contrastive pretraining - proving attention's role is writing pairwise match results into representation...

---

## 49. CLT-Forge: A Scalable Library for Cross-Layer Transcoders and Attribution Graphs

**Authors**: Florent Draye, Abir Harrasse, Vedant Palit, Tung-Yu Wu, Jiarui Liu, Punya Syon Pandey, Roderick Wu, ...  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21014  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21014v1.pdf

**Abstract**:
> arXiv:2603.21014v1 Announce Type: new 
Abstract: Mechanistic interpretability seeks to understand how Large Language Models (LLMs) represent and process information. Recent approaches based on dictionary learning and transcoders enable representing model computation in terms of sparse, interpretable features and their interactions, giving rise to feature attribution graphs. However, these graphs are often large and redundant, limiting their interpretability in practice. Cross-Layer Transcoders (CLTs) address this issue by sharing features across layers while preserving layer-specific decoding, yielding more compact representations, but remain difficult to train and analyze at scale. We introduce an open-source library for end-to-end training and interpretability of CLTs. Our framework inte...

---

## 50. Semi-Supervised Learning with Balanced Deep Representation Distributions

**Authors**: Changchun Li, Ximing Li, Bingjie Zhang, Wenting Wang, Jihong Ouyang  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21056  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21056v1.pdf

**Abstract**:
> arXiv:2603.21056v1 Announce Type: new 
Abstract: Semi-Supervised Text Classification (SSTC) mainly works under the spirit of self-training. They initialize the deep classifier by training over labeled texts; and then alternatively predict unlabeled texts as their pseudo-labels and train the deep classifier over the mixture of labeled and pseudo-labeled texts. Naturally, their performance is largely affected by the accuracy of pseudo-labels for unlabeled texts. Unfortunately, they often suffer from low accuracy because of the margin bias problem caused by the large difference between representation distributions of labels in SSTC. To alleviate this problem, we apply the angular margin loss, and perform several Gaussian linear transformations to achieve balanced label angle variances, i.e., ...

---

## 51. DMMRL: Disentangled Multi-Modal Representation Learning via Variational Autoencoders for Molecular Property Prediction

**Authors**: Long Xu, Junping Guo, Jianbo Zhao, Jianbo Lu, Yuzhong Peng  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21108  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21108v1.pdf

**Abstract**:
> arXiv:2603.21108v1 Announce Type: new 
Abstract: Molecular property prediction constitutes a cornerstone of drug discovery and materials science, necessitating models capable of disentangling complex structure-property relationships across diverse molecular modalities. Existing approaches frequently exhibit entangled representations--conflating structural, chemical, and functional factors--thereby limiting interpretability and transferability. Furthermore, conventional methods inadequately exploit complementary information from graphs, sequences, and geometries, often relying on naive concatenation that neglects inter-modal dependencies. In this work, we propose DMMRL, which employs variational autoencoders to disentangle molecular representations into shared (structure-relevant) and priva...

---

## 52. Amortized Variational Inference for Logistic Regression with Missing Covariates

**Authors**: M. Cherifi, Aude Sportisse, Xujia Zhu, Mohammed Nabil El Korso, A. Mesloub  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21244  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21244v1.pdf

**Abstract**:
> arXiv:2603.21244v1 Announce Type: new 
Abstract: Missing covariate data pose a significant challenge to statistical inference and machine learning, particularly for classification tasks like logistic regression. Classical iterative approaches (EM, multiple imputation) are often computationally intensive, sensitive to high missingness rates, and limited in uncertainty propagation. Recent deep generative models based on VAEs show promise but rely on complex latent representations.
  We propose Amortized Variational Inference for Logistic Regression (AV-LR), a unified end-to-end framework for binary logistic regression with missing covariates. AV-LR integrates a probabilistic generative model with a simple amortized inference network, trained jointly by maximizing the evidence lower bound. Un...

---

## 53. FluidWorld: Reaction-Diffusion Dynamics as a Predictive Substrate for World Models

**Authors**: Fabien Polly  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21315  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21315v1.pdf

**Abstract**:
> arXiv:2603.21315v1 Announce Type: new 
Abstract: World models learn to predict future states of an environment, enabling planning and mental simulation. Current approaches default to Transformer-based predictors operating in learned latent spaces. This comes at a cost: O(N^2) computation and no explicit spatial inductive bias. This paper asks a foundational question: is self-attention necessary for predictive world modeling, or can alternative computational substrates achieve comparable or superior results? I introduce FluidWorld, a proof-of-concept world model whose predictive dynamics are governed by partial differential equations (PDEs) of reaction-diffusion type. Instead of using a separate neural network predictor, the PDE integration itself produces the future state prediction. In a ...

---

## 54. Stream separation improves Bregman conditioning in transformers

**Authors**: James Clayton Kerce  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21317  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21317v1.pdf

**Abstract**:
> arXiv:2603.21317v1 Announce Type: new 
Abstract: Linear methods for steering transformer representations, including probing, activation engineering, and concept erasure, implicitly assume the geometry of representation space is Euclidean. Park et al. [Park et al., 2026] showed that softmax induces a curved Bregman geometry whose metric tensor is the Hessian of the log-normalizer, $H({\lambda}) = Cov[{\gamma} | {\lambda}]$. Ignoring this curvature causes Euclidean steering to leak probability mass to unintended tokens. Their analysis applies at the output layer. We measure this Hessian at intermediate layers in a controlled 2x2 design crossing stream separation with per-layer supervision (vocabulary decoding loss at each layer), all at matched vocabulary and parameter count. In standard sin...

---

## 55. Active Inference Agency Formalization, Metrics, and Convergence Assessments

**Authors**: Eduard Kapelko  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21319  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21319v1.pdf

**Abstract**:
> arXiv:2603.21319v1 Announce Type: new 
Abstract: This paper addresses the critical challenge of mesa-optimization in AI safety by providing a formal definition of agency and a framework for its analysis. Agency is conceptualized as a Continuous Representation of accumulated experience that achieves autopoiesis through a dynamic balance between curiosity (minimizing prediction error to ensure non-computability and novelty) and empowerment (maximizing the control channel's information capacity to ensure subjectivity and goal-directedness). Empirical evidence suggests that this active inference-based model successfully accounts for classical instrumental goals, such as self-preservation and resource acquisition.
  The analysis demonstrates that the proposed agency function is smooth and conve...

---

## 56. Multinoulli Extension: A Lossless Continuous Relaxation for Partition-Constrained Subset Selection

**Authors**: Qixin Zhang, Wei Huang, Yan Sun, Yao Shu, Yi Yu, Dacheng Tao  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21492  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21492v1.pdf

**Abstract**:
> arXiv:2603.21492v1 Announce Type: new 
Abstract: Identifying the most representative subset for a close-to-submodular objective while satisfying the predefined partition constraint is a fundamental task with numerous applications in machine learning. However, the existing distorted local-search methods are often hindered by their prohibitive query complexities and the rigid requirement for prior knowledge of difficult-to-obtain structural parameters. To overcome these limitations, we introduce a novel algorithm titled Multinoulli-SCG, which not only is parameter-free, but also can achieve the same approximation guarantees as the distorted local-search methods with significantly fewer function evaluations. More specifically, when the objective function is monotone $\alpha$-weakly DR-submodu...

---

## 57. Quotient Geometry, Effective Curvature, and Implicit Bias in Simple Shallow Neural Networks

**Authors**: Hang-Cheng Dong, Pengcheng Cheng  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21502  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21502v1.pdf

**Abstract**:
> arXiv:2603.21502v1 Announce Type: new 
Abstract: Overparameterized shallow neural networks admit substantial parameter redundancy: distinct parameter vectors may represent the same predictor due to hidden-unit permutations, rescalings, and related symmetries. As a result, geometric quantities computed directly in the ambient Euclidean parameter space can reflect artifacts of representation rather than intrinsic properties of the predictor. In this paper, we develop a differential-geometric framework for analyzing simple shallow networks through the quotient space obtained by modding out parameter symmetries on a regular set. We first characterize the symmetry and quotient structure of regular shallow-network parameters and show that the finite-sample realization map induces a natural metri...

---

## 58. What Do World Models Learn in RL? Probing Latent Representations in Learned Environment Simulators

**Authors**: Xinyu Zhang  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21546  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21546v1.pdf

**Abstract**:
> arXiv:2603.21546v1 Announce Type: new 
Abstract: World models learn to simulate environment dynamics from experience, enabling sample-efficient reinforcement learning. But what do these models actually represent internally? We apply interpretability techniques--including linear and nonlinear probing, causal interventions, and attention analysis--to two architecturally distinct world models: IRIS (discrete token transformer) and DIAMOND (continuous diffusion UNet), trained on Atari Breakout and Pong. Using linear probes, we find that both models develop linearly decodable representations of game state variables (object positions, scores), with MLP probes yielding only marginally higher R^2, confirming that these representations are approximately linear. Causal interventions--shifting hidden...

---

## 59. SSAM: Singular Subspace Alignment for Merging Multimodal Large Language Models

**Authors**: Md Kaykobad Reza, Ameya Patil, Edward Ayrapetian, M. Salman Asif  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21584  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21584v1.pdf

**Abstract**:
> arXiv:2603.21584v1 Announce Type: new 
Abstract: Multimodal large language models (MLLMs) achieve strong performance by jointly processing inputs from multiple modalities, such as vision, audio, and language. However, building such models or extending them to new modalities often requires large paired datasets and substantial computational resources. Since many pretrained MLLMs (e.g., vision-language or audio-language) are publicly available, we ask whether we can merge them into a single MLLM that can handle multiple modalities? Merging MLLMs with different input modalities remains challenging, partly because of differences in the learned representations and interference between their parameter spaces. To address these challenges, we propose Singular Subspace Alignment and Merging (SSAM),...

---

## 60. Riemannian Geometry Speaks Louder Than Words: From Graph Foundation Model to Next-Generation Graph Intelligence

**Authors**: Philip S. Yu, Li Sun  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21601  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21601v1.pdf

**Abstract**:
> arXiv:2603.21601v1 Announce Type: new 
Abstract: Graphs provide a natural description of the complex relationships among objects, and play a pivotal role in communications, transportation, social computing, the life sciences, etc. Currently, there is strong agreement that Graph Foundation Models (GFMs) are essential for advancing graph learning, yet considerable disagreement persists on how to build a powerful, general-purpose GFM analogous to Large Language Models (LLMs). Graph Neural Networks (GNNs) exhibit limitations in memory retention and principled interpretability when confronted with multi-domain pretraining and adaptation. The challenge of graph serialization hinders the direct application of LLMs, as the words struggle to capture the structural complexity and diversity inherent ...

---

## 61. MISApp: Multi-Hop Intent-Aware Session Graph Learning for Next App Prediction

**Authors**: Yunchi Yang, Longlong Li, Jianliang Wu, Cunquan Qu  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21653  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21653v1.pdf

**Abstract**:
> arXiv:2603.21653v1 Announce Type: new 
Abstract: Predicting the next mobile app a user will launch is essential for proactive mobile services. Yet accurate prediction remains challenging in real-world settings, where user intent can shift rapidly within short sessions and user-specific historical profiles are often sparse or unavailable, especially under cold-start conditions. Existing approaches mainly model app usage as sequential behavior or local session transitions, limiting their ability to capture higher-order structural dependencies and evolving session intent. To address this issue, we propose MISApp, a profile-free framework for next app prediction based on multi-hop session graph learning. MISApp constructs multi-hop session graphs to capture transition dependencies at different...

---

## 62. TrustFed: Enabling Trustworthy Medical AI under Data Privacy Constraints

**Authors**: Vagish Kumar, Syed Bahauddin Alam, Souvik Chakraborty  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21656  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21656v1.pdf

**Abstract**:
> arXiv:2603.21656v1 Announce Type: new 
Abstract: Protecting patient privacy remains a fundamental barrier to scaling machine learning across healthcare institutions, where centralizing sensitive data is often infeasible due to ethical, legal, and regulatory constraints. Federated learning offers a promising alternative by enabling privacy-preserving, multi-institutional training without sharing raw patient data; however, real-world deployments face severe challenges from data heterogeneity, site-specific biases, and class imbalance, which degrade predictive reliability and render existing uncertainty quantification methods ineffective. Here, we present TrustFed, a federated uncertainty quantification framework that provides distribution-free, finite-sample coverage guarantees under heterog...

---

## 63. FISformer: Replacing Self-Attention with a Fuzzy Inference System in Transformer Models for Time Series Forecasting

**Authors**: Bulent Haznedar, Levent Karacan  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21724  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21724v1.pdf

**Abstract**:
> arXiv:2603.21724v1 Announce Type: new 
Abstract: Transformers have achieved remarkable progress in time series forecasting, yet their reliance on deterministic dot-product attention limits their capacity to model uncertainty and nonlinear dependencies across multivariate temporal dimensions. To address this limitation, we propose FISFormer, a Fuzzy Inference System-driven Transformer that replaces conventional attention with a FIS Interaction mechanism. In this framework, each query-key pair undergoes a fuzzy inference process for every feature dimension, where learnable membership functions and rule-based reasoning estimate token-wise relational strengths. These FIS-derived interaction weights capture uncertainty and provide interpretable, continuous mappings between tokens. A softmax ope...

---

## 64. Extending Precipitation Nowcasting Horizons via Spectral Fusion of Radar Observations and Foundation Model Priors

**Authors**: Yuze Qin, Qingyong Li, Zhiqing Guo, Wen Wang, Yan Liu, Yangli-ao Geng  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21768  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21768v1.pdf

**Abstract**:
> arXiv:2603.21768v1 Announce Type: new 
Abstract: Precipitation nowcasting is critical for disaster mitigation and aviation safety. However, radar-only models frequently suffer from a lack of large-scale atmospheric context, leading to performance degradation at longer lead times. While integrating meteorological variables predicted by weather foundation models offers a potential remedy, existing architectures fail to reconcile the profound representational heterogeneities between radar imagery and meteorological data. To bridge this gap, we propose PW-FouCast, a novel frequency-domain fusion framework that leverages Pangu-Weather forecasts as spectral priors within a Fourier-based backbone. Our architecture introduces three key innovations: (i) Pangu-Weather-guided Frequency Modulation to ...

---

## 65. SparseDVFS: Sparse-Aware DVFS for Energy-Efficient Edge Inference

**Authors**: Ziyang Zhang, Zheshun Wu, Jie Liu, Luca Mottola  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21908  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21908v1.pdf

**Abstract**:
> arXiv:2603.21908v1 Announce Type: new 
Abstract: Deploying deep neural networks (DNNs) on power-sensitive edge devices presents a formidable challenge. While Dynamic Voltage and Frequency Scaling (DVFS) is widely employed for energy optimization, traditional model-level scaling is often too coarse to capture intra-inference variations, whereas fine-grained operator-level scaling suffers from prohibitive performance degradation due to significant hardware switching latency. This paper presents SparseDVFS, a fine-grained, sparse-aware DVFS framework designed for energy-efficient edge inference. Our key insight is that operator sparsity is a primary metric for hardware frequency modulation. By distinguishing between compute-bound dense operators and memory-bound sparse operators, the system c...

---

## 66. Do Papers Match Code? A Benchmark and Framework for Paper-Code Consistency Detection in Bioinformatics Software

**Authors**: Tianxiang Xu, Xiaoyan Zhu, Xin Lai, Sizhe Dang, Xin Lian, Hangyu Cheng, Jiayin Wang  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22018  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22018v1.pdf

**Abstract**:
> arXiv:2603.22018v1 Announce Type: new 
Abstract: Ensuring consistency between research papers and their corresponding software implementations is fundamental to software reliability and scientific reproducibility. However, this problem remains underexplored, particularly in the domain of bioinformatics, where discrepancies between methodological descriptions in papers and their actual code implementations are prevalent. To address this gap, this paper introduces a new task, namely paper-code consistency detection, and curates a collection of 48 bioinformatics software projects along with their associated publications. We systematically align sentence-level algorithmic descriptions from papers with function-level code snippets. Combined with expert annotations and a hybrid negative sampling...

---

## 67. MIHT: A Hoeffding Tree for Time Series Classification using Multiple Instance Learning

**Authors**: Aurora Esteban, Amelia Zafra, Sebasti\'an Ventura  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22074  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22074v1.pdf

**Abstract**:
> arXiv:2603.22074v1 Announce Type: new 
Abstract: Due to the prevalence of temporal data and its inherent dependencies in many real-world problems, time series classification is of paramount importance in various domains. However, existing models often struggle with series of variable length or high dimensionality. This paper introduces the MIHT (Multi-instance Hoeffding Tree) algorithm, an efficient model that uses multi-instance learning to classify multivariate and variable-length time series while providing interpretable results. The algorithm uses a novel representation of time series as "bags of subseries," together with an optimization process based on incremental decision trees that distinguish relevant parts of the series from noise. This methodology extracts the underlying concept...

---

## 68. Causal Evidence that Language Models use Confidence to Drive Behavior

**Authors**: Dharshan Kumaran, Nathaniel Daw, Simon Osindero, Petar Velickovic, Viorica Patraucean  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22161  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22161v1.pdf

**Abstract**:
> arXiv:2603.22161v1 Announce Type: new 
Abstract: Metacognition -- the ability to assess one's own cognitive performance -- is documented across species, with internal confidence estimates serving as a key signal for adaptive behavior. While confidence can be extracted from Large Language Model (LLM) outputs, whether models actively use these signals to regulate behavior remains a fundamental question. We investigate this through a four-phase abstention paradigm.Phase 1 established internal confidence estimates in the absence of an abstention option. Phase 2 revealed that LLMs apply implicit thresholds to these estimates when deciding to answer or abstain. Confidence emerged as the dominant predictor of behavior, with effect sizes an order of magnitude larger than knowledge retrieval access...

---

## 69. The Deep-Match Framework for Event-Related Potential Detection in EEG

**Authors**: Marek Zylinski, Bartosz Tomasz Smigielski, Gerard Cybulski  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20258  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20258v1.pdf

**Abstract**:
> arXiv:2603.20258v1 Announce Type: cross 
Abstract: Reliable detection of event-related potentials (ERPs) at the single-trial level remains a major challenge due to the low signal-to-noise ratio EEG recordings. In this work, we investigate whether incorporating prior knowledge about ERP templates into deep learning models can improve detection performance. We employ the Deep-Match framework for ERP detection using multi-channel EEG signals. The model is trained in two stages. First, an encoder-decoder architecture is trained to reconstruct input EEG signals, enabling the network to learn compact signal representations. In the second stage, the decoder is replaced with a detection module, and the network is fine-tuned for ERP identification. Two model variants are evaluated: a standard model...

---

## 70. Low-pass Personalized Subgraph Federated Recommendation

**Authors**: Wooseok Sim, Hogun Park  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20338  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20338v1.pdf

**Abstract**:
> arXiv:2603.20338v1 Announce Type: cross 
Abstract: Federated Recommender Systems (FRS) preserve privacy by training decentralized models on client-specific user-item subgraphs without sharing raw data. However, FRS faces a unique challenge: subgraph structural imbalance, where drastic variations in subgraph scale (user/item counts) and connectivity (item degree) misalign client representations, making it challenging to train a robust model that respects each client's unique structural characteristics. To address this, we propose a Low-pass Personalized Subgraph Federated recommender system (LPSFed). LPSFed leverages graph Fourier transforms and low-pass spectral filtering to extract low-frequency structural signals that remain stable across subgraphs of varying size and degree, allowing ro...

---

## 71. Comprehensive Description of Uncertainty in Measurement for Representation and Propagation with Scalable Precision

**Authors**: Ali Darijani, J\"urgen Beyerer, Zahra Sadat Hajseyed Nasrollah, Luisa Hoffmann, Michael Heizmann  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20365  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20365v1.pdf

**Abstract**:
> arXiv:2603.20365v1 Announce Type: cross 
Abstract: Probability theory has become the predominant framework for quantifying uncertainty across scientific and engineering disciplines, with a particular focus on measurement and control systems. However, the widespread reliance on simple Gaussian assumptions--particularly in control theory, manufacturing, and measurement systems--can result in incomplete representations and multistage lossy approximations of complex phenomena, including inaccurate propagation of uncertainty through multi stage processes.
  This work proposes a comprehensive yet computationally tractable framework for representing and propagating quantitative attributes arising in measurement systems using Probability Density Functions (PDFs). Recognizing the constraints impose...

---

## 72. Hierarchical Multiscale Structure-Function Coupling for Brain Connectome Integration

**Authors**: Jianwei Chen, Zhengyang Miao, Wenjie Cai, Jiaxue Tang, Boxing Liu, Yunfan Zhang, Yuhang Yang, Hao Ta...  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20680  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20680v1.pdf

**Abstract**:
> arXiv:2603.20680v1 Announce Type: cross 
Abstract: Integrating structural and functional connectomes remains challenging because their relationship is non-linear and organized over nested modular hierarchies. We propose a hierarchical multiscale structure-function coupling framework for connectome integration that jointly learns individualized modular organization and hierarchical coupling across structural connectivity (SC) and functional connectivity (FC). The framework includes: (i) Prototype-based Modular Pooling (PMPool), which learns modality-specific multiscale communities by selecting prototypical ROIs and optimizing a differentiable modularity-inspired objective; (ii) an Attention-based Hierarchical Coupling Module (AHCM) that models both within-hierarchy and cross-hierarchy SC-FC...

---

## 73. Predictive Regularization Against Visual Representation Degradation in Multimodal Large Language Models

**Authors**: Enguang Wang, Qiang Wang, Yuanchen Wu, Ke Yan, Xinbin Yuan, Shouhong Ding, Xialei Liu, Ming-Ming Che...  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20808  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20808v1.pdf

**Abstract**:
> arXiv:2603.20808v1 Announce Type: cross 
Abstract: While Multimodal Large Language Models (MLLMs) excel at vision-language tasks, the cost of their language-driven training on internal visual foundational competence remains unclear. In this paper, we conduct a detailed diagnostic analysis to unveil a pervasive issue: visual representation degradation in MLLMs. Specifically, we find that compared to the initial visual features, the visual representation in the middle layers of LLM exhibits both a degradation in global function and patch structure. We attribute this phenomenon to a visual sacrifice driven by the singular text-generation objective, where the model compromises its visual fidelity to optimize for answer generation. We argue that a robust MLLM requires both strong cross-modal re...

---

## 74. HiCI: Hierarchical Construction-Integration for Long-Context Attention

**Authors**: Xiangyu Zeng, Qi Xu, Yunke Wang, Chang Xu  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20843  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20843v1.pdf

**Abstract**:
> arXiv:2603.20843v1 Announce Type: cross 
Abstract: Long-context language modeling is commonly framed as a scalability challenge of token-level attention, yet local-to-global information structuring remains largely implicit in existing approaches. Drawing on cognitive theories of discourse comprehension, we propose HiCI (Hierarchical Construction--Integration), a hierarchical attention module that constructs segment-level representations, integrates them into a shared global context, and broadcasts both to condition segment-level attention. We validate HiCI through parameter-efficient adaptation of LLaMA-2 with only <5.5% additional parameters, extending context from 4K to 100K tokens (7B) and 64K tokens (13B). Across language modeling, retrieval, and instruction-following benchmarks, HiCI ...

---

## 75. The Intelligent Disobedience Game: Formulating Disobedience in Stackelberg Games and Markov Decision Processes

**Authors**: Benedikt Hornig, Reuth Mirsky  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20994  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20994v1.pdf

**Abstract**:
> arXiv:2603.20994v1 Announce Type: cross 
Abstract: In shared autonomy, a critical tension arises when an automated assistant must choose between obeying a human's instruction and deliberately overriding it to prevent harm. This safety-critical behavior is known as intelligent disobedience. To formalize this dynamic, this paper introduces the Intelligent Disobedience Game (IDG), a sequential game-theoretic framework based on Stackelberg games that models the interaction between a human leader and an assistive follower operating under asymmetric information. It characterizes optimal strategies for both agents across multi-step scenarios, identifying strategic phenomena such as ``safety traps,'' where the system indefinitely avoids harm but fails to achieve the human's goal. The IDG provides ...

---

## 76. ViCLSR: A Supervised Contrastive Learning Framework with Natural Language Inference for Natural Language Understanding Tasks

**Authors**: Tin Van Huynh, Kiet Van Nguyen, Ngan Luu-Thuy Nguyen  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21084  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21084v1.pdf

**Abstract**:
> arXiv:2603.21084v1 Announce Type: cross 
Abstract: High-quality text representations are crucial for natural language understanding (NLU), but low-resource languages like Vietnamese face challenges due to limited annotated data. While pre-trained models like PhoBERT and CafeBERT perform well, their effectiveness is constrained by data scarcity. Contrastive learning (CL) has recently emerged as a promising approach for improving sentence representations, enabling models to effectively distinguish between semantically similar and dissimilar sentences. We propose ViCLSR (Vietnamese Contrastive Learning for Sentence Representations), a novel supervised contrastive learning framework specifically designed to optimize sentence embeddings for Vietnamese, leveraging existing natural language infer...

---

## 77. Ontology-driven personalized information retrieval for XML documents

**Authors**: Ounnaci Iddir, Ahmed-ouamer Rachid, Tai Dinh  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21139  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21139v1.pdf

**Abstract**:
> arXiv:2603.21139v1 Announce Type: cross 
Abstract: This paper addresses the challenge of improving information retrieval from semi-structured eXtensible Markup Language (XML) documents. Traditional information retrieval systems (IRS) often overlook user-specific needs and return identical results for the same query, despite differences in users' knowledge, preferences, and objectives. We integrate external semantic resources, namely a domain ontology and user profiles, into the retrieval process. Documents, queries, and user profiles are represented as vectors of weighted concepts. The ontology applies a concept-weighting mechanism that emphasizes highly specific concepts, as lower-level nodes in the hierarchy provide more precise and targeted information. Relevance is assessed using seman...

---

## 78. NeSy-Edge: Neuro-Symbolic Trustworthy Self-Healing in the Computing Continuum

**Authors**: Peihan Ye, Alfreds Lapkovskis, Alaa Saleh, Qiyang Zhang, Praveen Kumar Donta  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21145  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21145v1.pdf

**Abstract**:
> arXiv:2603.21145v1 Announce Type: cross 
Abstract: The computational demands of modern AI services are increasingly shifting execution beyond centralized clouds toward a computing continuum spanning edge and end devices. However, the scale, heterogeneity, and cross-layer dependencies of these environments make resilience difficult to maintain. Existing fault-management methods are often too static, fragmented, or heavy to support timely self-healing, especially under noisy logs and edge resource constraints. To address these limitations, this paper presents NeSy-Edge, a neuro-symbolic framework for trustworthy self-healing in the computing continuum. The framework follows an edge-first design, where a resource-constrained edge node performs local perception and reasoning, while a cloud mod...

---

## 79. The Library Theorem: How External Organization Governs Agentic Reasoning Capacity

**Authors**: Zachary F. Mainen  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21272  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21272v1.pdf

**Abstract**:
> arXiv:2603.21272v1 Announce Type: cross 
Abstract: Externalized reasoning is already exploited by transformer-based agents through chain-of-thought, but structured retrieval -- indexing over one's own reasoning state -- remains underexplored. We formalize the transformer context window as an I/O page and prove that tool-augmented agents with indexed external memory achieve exponentially lower retrieval cost than agents restricted to sequential scanning: $O(\log_b N)$ versus $\Omega(N)$ page reads per query, and $O(T \log_b T)$ versus $\Theta(T^2)$ cumulative cost over $T$ reasoning steps -- a gap that widens as deliberation deepens. We test these predictions on a controlled lookup benchmark across three content types -- random hashes, ordered integers, and encyclopedia entries -- varying s...

---

## 80. HamVision: Hamiltonian Dynamics as Inductive Bias for Medical Image Analysis

**Authors**: Mohamed A Mabrok  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21377  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21377v1.pdf

**Abstract**:
> arXiv:2603.21377v1 Announce Type: cross 
Abstract: We present HamVision, a framework for medical image analysis that uses the damped harmonic oscillator, a fundamental building block of signal processing, as a structured inductive bias for both segmentation and classification tasks. The oscillator's phase-space decomposition yields three functionally distinct representations: position~$q$ (feature content), momentum~$p$ (spatial gradients that encode boundary and texture information), and energy $H = \tfrac{1}{2}|z|^2$ (a parameter-free saliency map). These representations emerge from the dynamics, not from supervision, and can be exploited by different task-specific heads without any modification to the oscillator itself. For segmentation, energy gates the skip connections while momentum ...

---

## 81. GaussianSSC: Triplane-Guided Directional Gaussian Fields for 3D Semantic Completion

**Authors**: Ruiqi Xian, Jing Liang, He Yin, Xuewei Qi, Dinesh Manocha  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21487  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21487v1.pdf

**Abstract**:
> arXiv:2603.21487v1 Announce Type: cross 
Abstract: We present \emph{GaussianSSC}, a two-stage, grid-native and triplane-guided approach to semantic scene completion (SSC) that injects the benefits of Gaussians without replacing the voxel grid or maintaining a separate Gaussian set. We introduce \emph{Gaussian Anchoring}, a sub-pixel, Gaussian-weighted image aggregation over fused FPN features that tightens voxel--image alignment and improves monocular occupancy estimation. We further convert point-like voxel features into a learned per-voxel Gaussian field and refine triplane features via a triplane-aligned \emph{Gaussian--Triplane Refinement} module that combines \emph{local gathering} (target-centric) and \emph{global aggregation} (source-centric). This directional, anisotropic support c...

---

## 82. FedCVU: Federated Learning for Cross-View Video Understanding

**Authors**: Shenghan Zhang, Run Ling, Ke Cao, Ao Ma, Zhanjie Zhang  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21647  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21647v1.pdf

**Abstract**:
> arXiv:2603.21647v1 Announce Type: cross 
Abstract: Federated learning (FL) has emerged as a promising paradigm for privacy-preserving multi-camera video understanding. However, applying FL to cross-view scenarios faces three major challenges: (i) heterogeneous viewpoints and backgrounds lead to highly non-IID client distributions and overfitting to view-specific patterns, (ii) local distribution biases cause misaligned representations that hinder consistent cross-view semantics, and (iii) large video architectures incur prohibitive communication overhead. To address these issues, we propose FedCVU, a federated framework with three components: VS-Norm, which preserves normalization parameters to handle view-specific statistics; CV-Align, a lightweight contrastive regularization module to im...

---

## 83. Not All Layers Are Created Equal: Adaptive LoRA Ranks for Personalized Image Generation

**Authors**: Donald Shenaj, Federico Errica, Antonio Carta  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21884  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21884v1.pdf

**Abstract**:
> arXiv:2603.21884v1 Announce Type: cross 
Abstract: Low Rank Adaptation (LoRA) is the de facto fine-tuning strategy to generate personalized images from pre-trained diffusion models. Choosing a good rank is extremely critical, since it trades off performance and memory consumption, but today the decision is often left to the community's consensus, regardless of the personalized subject's complexity. The reason is evident: the cost of selecting a good rank for each LoRA component is combinatorial, so we opt for practical shortcuts such as fixing the same rank for all components. In this paper, we take a first step to overcome this challenge. Inspired by variational methods that learn an adaptive width of neural networks, we let the ranks of each layer freely adapt during fine-tuning on a sub...

---

## 84. A Latent Representation Learning Framework for Hyperspectral Image Emulation in Remote Sensing

**Authors**: Chedly Ben Azizi, Claire Guilloteau, Gilles Roussel, Matthieu Puigt  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21911  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21911v1.pdf

**Abstract**:
> arXiv:2603.21911v1 Announce Type: cross 
Abstract: Synthetic hyperspectral image (HSI) generation is essential for large-scale simulation, algorithm development, and mission design, yet traditional radiative transfer models remain computationally expensive and often limited to spectrum-level outputs. In this work, we propose a latent representation-based framework for hyperspectral emulation that learns a latent generative representation of hyperspectral data. The proposed approach supports both spectrum-level and spatial-spectral emulation and can be trained either in a direct one-step formulation or in a two-step strategy that couples variational autoencoder (VAE) pretraining with parameter-to-latent interpolation. Experiments on PROSAIL-simulated vegetation data and Sentinel-3 OLCI imag...

---

## 85. Camera-Agnostic Pruning of 3D Gaussian Splats via Descriptor-Based Beta Evidence

**Authors**: Peter Fasogbon, Ugurcan Budak, Patrice Rondao Alface, Hamed Rezazadegan Tavakoli  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21933  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21933v1.pdf

**Abstract**:
> arXiv:2603.21933v1 Announce Type: cross 
Abstract: The pruning of 3D Gaussian splats is essential for reducing their complexity to enable efficient storage, transmission, and downstream processing. However, most of the existing pruning strategies depend on camera parameters, rendered images, or view-dependent measures. This dependency becomes a hindrance in emerging camera-agnostic exchange settings, where splats are shared directly as point-based representations (e.g., .ply). In this paper, we propose a camera-agnostic, one-shot, post-training pruning method for 3D Gaussian splats that relies solely on attribute-derived neighbourhood descriptors. As our primary contribution, we introduce a hybrid descriptor framework that captures structural and appearance consistency directly from the sp...

---

## 86. SpecTM: Spectral Targeted Masking for Trustworthy Foundation Models

**Authors**: Syed Usama Imtiaz, Mitra Nasr Azadani, Nasrin Alamdari  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22097  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22097v1.pdf

**Abstract**:
> arXiv:2603.22097v1 Announce Type: cross 
Abstract: Foundation models are now increasingly being developed for Earth observation (EO), yet they often rely on stochastic masking that do not explicitly enforce physics constraints; a critical trustworthiness limitation, in particular for predictive models that guide public health decisions. In this work, we propose SpecTM (Spectral Targeted Masking), a physics-informed masking design that encourages the reconstruction of targeted bands from cross-spectral context during pretraining. To achieve this, we developed an adaptable multi-task (band reconstruction, bio-optical index inference, and 8-day-ahead temporal prediction) self-supervised learning (SSL) framework that encodes spectrally intrinsic representations via joint optimization, and eval...

---

## 87. Data Curation for Machine Learning Interatomic Potentials by Determinantal Point Processes

**Authors**: Joanna Zou, Youssef Marzouk  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22160  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22160v1.pdf

**Abstract**:
> arXiv:2603.22160v1 Announce Type: cross 
Abstract: The development of machine learning interatomic potentials faces a critical computational bottleneck with the generation and labeling of useful training datasets. We present a novel application of determinantal point processes (DPPs) to the task of selecting informative subsets of atomic configurations to label with reference energies and forces from costly quantum mechanical methods. Through experiments with hafnium oxide data, we show that DPPs are competitive with existing approaches to constructing compact but diverse training sets by utilizing kernels of molecular descriptors, leading to improved accuracy and robustness in machine learning representations of molecular systems. Our work identifies promising directions to employ DPPs fo...

---

## 88. CayleyPy-4: AI-Holography. Towards analogs of holographic string dualities for AI tasks

**Authors**: A. Chervov, F. Levkovich-Maslyuk, A. Smolensky, F. Khafizov, I. Kiselev, D. Melnikov, I. Koltsov, S....  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22195  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22195v1.pdf

**Abstract**:
> arXiv:2603.22195v1 Announce Type: cross 
Abstract: This is the fourth paper in the CayleyPy project, which applies AI methods to the exploration of large graphs. In this work, we suggest the existence of a new discrete version of holographic string dualities for this setup, and discuss their relevance to AI systems and mathematics. Many modern AI tasks -- such as those addressed by GPT-style language models or RL systems -- can be viewed as direct analogues of predicting particle trajectories on graphs. We investigate this problem for a large family of Cayley graphs, for which we show that surprisingly it admits a dual description in terms of discrete strings. We hypothesize that such dualities may extend to a range of AI systems where they can lead to more efficient computational approach...

---

## 89. The Dual Mechanisms of Spatial Reasoning in Vision-Language Models

**Authors**: Kelly Cui, Nikhil Prakash, Ayush Raina, David Bau, Antonio Torralba, Tamar Rott Shaham  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22278  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22278v1.pdf

**Abstract**:
> arXiv:2603.22278v1 Announce Type: cross 
Abstract: Many multimodal tasks, such as image captioning and visual question answering, require vision-language models (VLMs) to associate objects with their properties and spatial relations. Yet it remains unclear where and how such associations are computed within VLMs. In this work, we show that VLMs rely on two concurrent mechanisms to represent such associations. In the language model backbone, intermediate layers represent content-independent spatial relations on top of visual tokens corresponding to objects. However, this mechanism plays only a secondary role in shaping model predictions. Instead, the dominant source of spatial information originates in the vision encoder, whose representations encode the layout of objects and are directly e...

---

## 90. ThinkJEPA: Empowering Latent World Models with Large Vision-Language Reasoning Model

**Authors**: Haichao Zhang, Yijiang Li, Shwai He, Tushar Nagarajan, Mingfei Chen, Jianglin Lu, Ang Li, Yun Fu  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22281  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22281v1.pdf

**Abstract**:
> arXiv:2603.22281v1 Announce Type: cross 
Abstract: Recent progress in latent world models (e.g., V-JEPA2) has shown promising capability in forecasting future world states from video observations. Nevertheless, dense prediction from a short observation window limits temporal context and can bias predictors toward local, low-level extrapolation, making it difficult to capture long-horizon semantics and reducing downstream utility. Vision--language models (VLMs), in contrast, provide strong semantic grounding and general knowledge by reasoning over uniformly sampled frames, but they are not ideal as standalone dense predictors due to compute-driven sparse sampling, a language-output bottleneck that compresses fine-grained interaction states into text-oriented representations, and a data-regi...

---

## 91. End-to-End Training for Unified Tokenization and Latent Denoising

**Authors**: Shivam Duggal, Xingjian Bai, Zongze Wu, Richard Zhang, Eli Shechtman, Antonio Torralba, Phillip Isol...  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22283  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22283v1.pdf

**Abstract**:
> arXiv:2603.22283v1 Announce Type: cross 
Abstract: Latent diffusion models (LDMs) enable high-fidelity synthesis by operating in learned latent spaces. However, training state-of-the-art LDMs requires complex staging: a tokenizer must be trained first, before the diffusion model can be trained in the frozen latent space. We propose UNITE - an autoencoder architecture for unified tokenization and latent diffusion. UNITE consists of a Generative Encoder that serves as both image tokenizer and latent generator via weight sharing. Our key insight is that tokenization and generation can be viewed as the same latent inference problem under different conditioning regimes: tokenization infers latents from fully observed images, whereas generation infers them from noise together with text or class ...

---

## 92. Herglotz-NET: Implicit Neural Representation of Spherical Data with Harmonic Positional Encoding

**Authors**: Th\'eo Hanon, Nicolas Mil-Homens Cavaco, John Kiely, Laurent Jacques  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2502.13777  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2502.13777v3.pdf

**Abstract**:
> arXiv:2502.13777v3 Announce Type: replace 
Abstract: Representing and processing data in spherical domains presents unique challenges, primarily due to the curvature of the domain, which complicates the application of classical Euclidean techniques. Implicit neural representations (INRs) have emerged as a promising alternative for high-fidelity data representation; however, to effectively handle spherical domains, these methods must be adapted to the inherent geometry of the sphere to maintain both accuracy and stability. In this context, we propose Herglotz-NET (HNET), a novel INR architecture that employs a harmonic positional encoding based on complex Herglotz mappings. This encoding yields a well-posed representation on the sphere with interpretable and robust spectral properties. More...

---

## 93. FRIREN: Beyond Trajectories -- A Spectral Lens on Time

**Authors**: Qilin Wang  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2505.17370  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2505.17370v5.pdf

**Abstract**:
> arXiv:2505.17370v5 Announce Type: replace 
Abstract: Long-term time-series forecasting (LTSF) models are often presented as general-purpose solutions that can be applied across domains, implicitly assuming that all data is pointwise predictable. Using chaotic systems such as Lorenz-63 as a case study, we argue that geometric structure - not pointwise prediction - is the right abstraction for a dynamic-agnostic foundational model. Minimizing the Wasserstein-2 distance (W2), which captures geometric changes, and providing a spectral view of dynamics are essential for long-horizon forecasting. Our model, FRIREN (Flow-inspired Representations via Interpretable Eigen-networks), implements an augmented normalizing-flow block that embeds data into a normally distributed latent representation. It ...

---

## 94. Generalized Incremental Learning under Concept Drift across Evolving Data Streams

**Authors**: En Yu, Jie Lu, Guangquan Zhang  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2506.05736  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2506.05736v2.pdf

**Abstract**:
> arXiv:2506.05736v2 Announce Type: replace 
Abstract: Real-world data streams exhibit inherent non-stationarity characterized by concept drift, posing significant challenges for adaptive learning systems. While existing methods address isolated distribution shifts, they overlook the critical co-evolution of label spaces and distributions under limited supervision and persistent uncertainty. To address this, we formalize Generalized Incremental Learning under Concept Drift (GILCD), characterizing the joint evolution of distributions and label spaces in open-environment streaming contexts, and propose a novel framework called Calibrated Source-Free Adaptation (CSFA). First, CSFA introduces a training-free prototype calibration mechanism that dynamically fuses emerging prototypes with base rep...

---

## 95. Beyond Static Models: Hypernetworks for Adaptive and Generalizable Forecasting in Complex Parametric Dynamical Systems

**Authors**: Pantelis R. Vlachas, Konstantinos Vlachas, Eleni Chatzi  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2506.19609  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2506.19609v2.pdf

**Abstract**:
> arXiv:2506.19609v2 Announce Type: replace 
Abstract: Dynamical systems play a key role in modeling, forecasting, and decision-making across a wide range of scientific domains. However, variations in system parameters, also referred to as parametric variability, can lead to drastically different model behavior and output, posing challenges for constructing models that generalize across parameter regimes. In this work, we introduce the Parametric Hypernetwork for Learning Interpolated Networks (PHLieNet), a framework that simultaneously learns: (a) a global mapping from the parameter space to a nonlinear embedding and (b) a mapping from the inferred embedding to the weights of a dynamics propagation network. The learned embedding serves as a latent representation that modulates a base networ...

---

## 96. From Nodes to Narratives: Explaining Graph Neural Networks with LLMs and Graph Context

**Authors**: Peyman Baghershahi, Gregoire Fournier, Pranav Nyati, Sourav Medya  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2508.07117  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2508.07117v2.pdf

**Abstract**:
> arXiv:2508.07117v2 Announce Type: replace 
Abstract: Graph Neural Networks (GNNs) have emerged as powerful tools for learning over structured data, including text-attributed graphs (TAGs), which are common in domains such as citation networks, social platforms, and knowledge graphs. GNNs are not inherently interpretable and thus, many explanation methods have been proposed. However, existing explanation methods often struggle to generate interpretable, fine-grained rationales, especially when node attributes include rich natural language. In this work, we introduce GSPELL, a lightweight, post-hoc framework that uses large language models (LLMs) to generate faithful and interpretable explanations for GNN predictions. GSPELL projects GNN node embeddings into the LLM embedding space and const...

---

## 97. HDC-X: Efficient Medical Data Classification for Embedded Devices

**Authors**: Jianglan Wei, Zhenyu Zhang, Pengcheng Wang, Mingjie Zeng, Zhigang Zeng  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2509.14617  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2509.14617v3.pdf

**Abstract**:
> arXiv:2509.14617v3 Announce Type: replace 
Abstract: Energy-efficient medical data classification is essential for modern disease screening, particularly in home and field healthcare where embedded devices are prevalent. While deep learning models achieve state-of-the-art accuracy, their substantial energy consumption and reliance on GPUs limit deployment on such platforms. We present HDC-X, a lightweight classification framework designed for low-power devices. HDC-X encodes data into high-dimensional hypervectors, aggregates them into multiple cluster-specific prototypes, and performs classification through similarity search in hyperspace. We evaluate HDC-X across three medical classification tasks; on heart sound classification, HDC-X is $350\times$ more energy-efficient than Bayesian Re...

---

## 98. SpecMol: A Spectroscopy-Grounded Foundation Model for Multi-Task Molecular Learning

**Authors**: Shuaike Shen, Jiaqing Xie, Zhuo Yang, Antong Zhang, Shuzhou Sun, Ben Gao, Tianfan Fu, Biqing Qi, Yuq...  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2509.21861  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2509.21861v3.pdf

**Abstract**:
> arXiv:2509.21861v3 Announce Type: replace 
Abstract: Large language models have emerged as transformative tools in molecular science, demonstrating remarkable potential in molecular property prediction and de novo molecular design. However, their application to spectroscopy remains notably limited, despite its foundational role in experimental molecular characterization and structural validation. Progress in spectroscopy-grounded reasoning has been hindered by the lack of standardized spectral representations and comprehensive evaluation protocols, making cross-study comparisons difficult. To bridge this gap, we present a unified framework for spectroscopy-grounded molecular modeling and evaluation. At its core, the SpecMol foundation model integrates spectral interpretation, molecular rep...

---

## 99. LEAF: Language-EEG Aligned Foundation Model for Brain-Computer Interfaces

**Authors**: Muyun Jiang, Shuailei Zhang, Zhenjie Yang, Mengjun Wu, Weibang Jiang, Zhiwei Guo, Wei Zhang, Rui Liu...  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2509.24302  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2509.24302v2.pdf

**Abstract**:
> arXiv:2509.24302v2 Announce Type: replace 
Abstract: Recent advances in electroencephalography (EEG) foundation models, which capture transferable EEG representations, have greatly accelerated the development of brain-computer interfaces (BCIs). However, existing approaches still struggle to incorporate language instructions as prior constraints for EEG representation learning, limiting their ability to leverage the semantic knowledge inherent in language to unify different labels and tasks. To address this challenge, we present LEAF, a foundation model for EEG--Language Alignment with Semantic Task Instruction and Querying. LEAF integrates task-aware semantic guidance to produce structured and linguistically aligned EEG embeddings, thereby enhancing decoding robustness and transferability...

---

## 100. DiVeQ: Differentiable Vector Quantization Using the Reparameterization Trick

**Authors**: Mohammad Hassan Vali, Tom B\"ackstr\"om, Arno Solin  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2509.26469  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2509.26469v2.pdf

**Abstract**:
> arXiv:2509.26469v2 Announce Type: replace 
Abstract: Vector quantization is common in deep models, yet its hard assignments block gradients and hinder end-to-end training. We propose DiVeQ, which treats quantization as adding an error vector that mimics the quantization distortion, keeping the forward pass hard while letting gradients flow. We also present a space-filling variant (SF-DiVeQ) that assigns to a curve constructed by the lines connecting codewords, resulting in less quantization error and full codebook usage. Both methods train end-to-end without requiring auxiliary losses or temperature schedules. In VQ-VAE image compression, VQGAN image generation, and DAC speech coding tasks across various data sets, our proposed methods improve reconstruction and sample quality over alterna...

---

## 101. Always Keep Your Promises: A Model-Agnostic Attribution Algorithm for Neural Networks

**Authors**: Kevin Lee, Duncan Smith-Halverson, Pablo Millan Arias  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2512.07010  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2512.07010v4.pdf

**Abstract**:
> arXiv:2512.07010v4 Announce Type: replace 
Abstract: Layer-wise Relevance Propagation (LRP) provides principled attribution for neural networks through conservation properties and foundations in Deep Taylor Decomposition. However, existing implementations operate at the module level, requiring architecture-specific propagation rules and model modifications. These limit the generality of target model and sustainability of implementations as architectures evolve. We introduce DynamicLRP, a model-agnostic LRP framework operating at the tensor operation level. By decomposing attribution to individual operations within computation graphs and introducing a novel mechanism for deferred activation resolution, named the Promise System, our approach achieves true architecture agnosticity while maint...

---

## 102. XNNTab -- Interpretable Neural Networks for Tabular Data using Sparse Autoencoders

**Authors**: Khawla Elhadri, J\"org Schl\"otterer, Christin Seifert  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2512.13442  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2512.13442v2.pdf

**Abstract**:
> arXiv:2512.13442v2 Announce Type: replace 
Abstract: In data-driven applications relying on tabular data, where interpretability is key, machine learning models such as decision trees and linear regression are applied. Although neural networks can provide higher predictive performance, they are not used because of their blackbox nature. In this work, we present XNNTab, a neural architecture that combines the expressiveness of neural networks and interpretability. XNNTab first learns highly non-linear feature representations, which are decomposed into monosemantic features using a sparse autoencoder (SAE). These features are then assigned human-interpretable concepts, making the overall model prediction intrinsically interpretable. XNNTab outperforms interpretable predictive models, and ach...

---

## 103. SIGMA: Scalable Spectral Insights for LLM Model Collapse

**Authors**: Yi Gu, Lingyou Pang, Xiangkun Ye, Tianyu Wang, Jianyu Lin, Carey E. Priebe, Alexander Aue  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2601.03385  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2601.03385v3.pdf

**Abstract**:
> arXiv:2601.03385v3 Announce Type: replace 
Abstract: The rapid adoption of synthetic data for training Large Language Models (LLMs) has introduced the technical challenge of "model collapse"-a degenerative process where recursive training on model-generated content leads to a contraction of distributional variance and representational quality. While the phenomenology of collapse is increasingly evident, rigorous methods to quantify and predict its onset in high-dimensional spaces remain elusive. In this paper, we introduce SIGMA (Spectral Inequalities for Gram Matrix Analysis), a unified framework that benchmarks model collapse through the spectral lens of the embedding Gram matrix. By deriving and utilizing deterministic and stochastic bounds on the matrix's spectrum, SIGMA provides a mat...

---

## 104. Gradient Structure Estimation under Label-Only Oracles via Spectral Sensitivity

**Authors**: Jun Liu, Leo Yu Zhang, Fengpeng Li, Isao Echizen, Jiantao Zhou  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2601.14300  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2601.14300v2.pdf

**Abstract**:
> arXiv:2601.14300v2 Announce Type: replace 
Abstract: Hard-label black-box settings, where only top-1 predicted labels are observable, pose a fundamentally constrained yet practically important feedback model for understanding model behavior. A central challenge in this regime is whether meaningful gradient information can be recovered from such discrete responses. In this work, we develop a unified theoretical perspective showing that a wide range of existing sign-flipping hard-label attacks can be interpreted as implicitly approximating the sign of the true loss gradient. This observation reframes hard-label attacks from heuristic search procedures into instances of gradient sign recovery under extremely limited feedback. Motivated by this first-principles understanding, we propose a new ...

---

## 105. Logical Guidance for the Exact Composition of Diffusion Models

**Authors**: Francesco Alesiani, Jonathan Warrell, Tanja Bien, Henrik Christiansen, Matheus Ferraz, Mathias Niepe...  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.05549  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.05549v2.pdf

**Abstract**:
> arXiv:2602.05549v2 Announce Type: replace 
Abstract: We propose LOGDIFF (Logical Guidance for the Exact Composition of Diffusion Models), a guidance framework for diffusion models that enables principled constrained generation with complex logical expressions at inference time. We study when exact score-based guidance for complex logical formulas can be obtained from guidance signals associated with atomic properties. First, we derive an exact Boolean calculus that provides a sufficient condition for exact logical guidance. Specifically, if a formula admits a circuit representation in which conjunctions combine conditionally independent subformulas and disjunctions combine subformulas that are either conditionally independent or mutually exclusive, exact logical guidance is achievable. In ...

---

## 106. CAMEL: An ECG Language Model for Forecasting Cardiac Events

**Authors**: Neelay Velingker, Alaia Solko-Breslin, Mayank Keoliya, Seewon Choi, Jiayi Xin, Anika Marathe, Alirez...  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.15677  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.15677v3.pdf

**Abstract**:
> arXiv:2602.15677v3 Announce Type: replace 
Abstract: Electrocardiograms (ECG) are electrical recordings of the heart that are critical for diagnosing cardiovascular conditions. ECG language models (ELMs) have recently emerged as a promising framework for ECG classification accompanied by report generation. However, current models cannot forecast future cardiac events despite the immense clinical value for planning earlier intervention. To address this gap, we propose CAMEL, the first ELM that is capable of inference over longer signal durations which enables its forecasting capability. Our key insight is a specialized ECG encoder which enables cross-understanding of ECG signals with text. We train CAMEL using established LLM training procedures, combining LoRA adaptation with a curriculum ...

---

## 107. AngelSlim: A more accessible, comprehensive, and efficient toolkit for large model compression

**Authors**: Rui Cen (Hunyuan AI Infra Team), QiangQiang Hu (Hunyuan AI Infra Team), Hong Huang (Hunyuan AI Infra...  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.21233  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.21233v3.pdf

**Abstract**:
> arXiv:2602.21233v3 Announce Type: replace 
Abstract: This technical report introduces AngelSlim, a comprehensive and versatile toolkit for large model compression developed by the Tencent Hunyuan team. By consolidating cutting-edge algorithms, including quantization, speculative decoding, token pruning, and distillation. AngelSlim provides a unified pipeline that streamlines the transition from model compression to industrial-scale deployment. To facilitate efficient acceleration, we integrate state-of-the-art FP8 and INT8 Post-Training Quantization (PTQ) algorithms alongside pioneering research in ultra-low-bit regimes, featuring HY-1.8B-int2 as the first industrially viable 2-bit large model. Beyond quantization, we propose a training-aligned speculative decoding framework compatible wit...

---

## 108. Support Tokens, Stability Margins, and a New Foundation for Robust LLMs

**Authors**: Deepak Agarwal, Dhyey Dharmendrakumar Mavani, Suyash Gupta, Karthik Sethuraman, Tejas Dharamsi  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.22271  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.22271v3.pdf

**Abstract**:
> arXiv:2602.22271v3 Announce Type: replace 
Abstract: Self-attention is usually described as a flexible, content-adaptive way to mix a token with information from its past. We reinterpret causal self-attention transformers, the backbone of modern foundation models, within a probabilistic framework, much as classical PCA is extended to probabilistic PCA. This reformulation reveals a key structural consequence of the underlying change of variables: a barrier constraint emerges on the parameters of self-attention. The resulting geometry exposes a degeneracy boundary where the attention-induced mapping becomes locally ill-conditioned, yielding a stability-margin interpretation analogous to the margin in support vector machines. This, in turn, naturally gives rise to the concept of support token...

---

## 109. Missingness Bias Calibration in Feature Attribution Explanations

**Authors**: Shailesh Sridhar, Anton Xue, Eric Wong  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.04831  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.04831v2.pdf

**Abstract**:
> arXiv:2603.04831v2 Announce Type: replace 
Abstract: Popular explanation methods often produce unreliable feature importance scores due to missingness bias, a systematic distortion that arises when models are probed with ablated, out-of-distribution inputs. Existing solutions treat this as a deep representational flaw that requires expensive retraining or architectural modifications. In this work, we challenge this assumption and show that missingness bias can be effectively treated as a superficial artifact of the model's output space. We introduce MCal, a lightweight post-hoc method that corrects this bias by fine-tuning a simple linear head on the outputs of a frozen base model. Surprisingly, we find this simple correction consistently reduces missingness bias and is competitive with, o...

---

## 110. Spherical VAE with Cluster-Aware Feasible Regions: Guaranteed Prevention of Posterior Collapse

**Authors**: Zegu Zhang, Jian Zhang  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10935  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10935v3.pdf

**Abstract**:
> arXiv:2603.10935v3 Announce Type: replace 
Abstract: Variational autoencoders (VAEs) frequently suffer from posterior collapse, where the latent variables become uninformative as the approximate posterior degenerates to the prior. While recent work has characterized collapse as a phase transition determined by data covariance properties, existing approaches primarily aim to avoid rather than eliminate collapse. We introduce a novel framework that theoretically guarantees non-collapsed solutions by leveraging spherical shell geometry and cluster-aware constraints. Our method transforms data to a spherical shell, computes optimal cluster assignments via K-means, and defines a feasible region between the within-cluster variance $W$ and collapse loss $\delta_{\text{collapse}}$. We prove that w...

---

## 111. PREBA: Surgical Duration Prediction via PCA-Weighted Retrieval-Augmented LLMs and Bayesian Averaging Aggregation

**Authors**: Wanyin Wu, Kanxue Li, Baosheng Yu, Haoyun Zhao, Yibing Zhan, Dapeng Tao, Hua Jin  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13275  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13275v3.pdf

**Abstract**:
> arXiv:2603.13275v3 Announce Type: replace 
Abstract: Accurate prediction of surgical duration is pivotal for hospital resource management. Although recent supervised learning approaches-from machine learning (ML) to fine-tuned large language models (LLMs)-have shown strong performance, they remain constrained by the need for high-quality labeled data and computationally intensive training. In contrast, zero-shot LLM inference offers a promising training-free alternative but it lacks grounding in institution-specific clinical context (e.g., local demographics and case-mix distributions), making its predictions clinically misaligned and prone to instability. To address these limitations, we present PREBA, a retrieval-augmented framework that integrates PCA-weighted retrieval and Bayesian ave...

---

## 112. Not All Latent Spaces Are Flat: Hyperbolic Concept Control

**Authors**: Maria Rosaria Briglia, Simone Facchiano, Paolo Cursi, Alessio Sampieri, Emanuele Rodol\`a, Guido Mar...  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14093  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14093v2.pdf

**Abstract**:
> arXiv:2603.14093v2 Announce Type: replace 
Abstract: As modern text-to-image (T2I) models draw closer to synthesizing highly realistic content, the threat of unsafe content generation grows, and it becomes paramount to exercise control. Existing approaches steer these models by applying Euclidean adjustments to text embeddings, redirecting the generation away from unsafe concepts. In this work, we introduce hyperbolic control (HyCon): a novel control mechanism based on parallel transport that leverages semantically aligned hyperbolic representation space to yield more expressive and stable manipulation of concepts. HyCon reuses off-the-shelf generative models and a state-of-the-art hyperbolic text encoder, linked via a lightweight adapter. HyCon achieves state-of-the-art results across fou...

---

## 113. The Finetuner's Fallacy: When to Pretrain with Your Finetuning Data

**Authors**: Christina Baek, Ricardo Pio Monti, David Schwab, Amro Abbas, Rishabh Adiga, Cody Blakeney, Maximilia...  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16177  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16177v2.pdf

**Abstract**:
> arXiv:2603.16177v2 Announce Type: replace 
Abstract: Real-world model deployments demand strong performance on narrow domains where data is often scarce. Typically, practitioners finetune models to specialize them, but this risks overfitting to the domain and forgetting general knowledge. We study a simple strategy, specialized pretraining (SPT), where a small domain dataset, typically reserved for finetuning, is repeated starting from pretraining as a fraction of the total tokens. Across three specialized domains (ChemPile, MusicPile, and ProofPile), SPT improves domain performance and preserves general capabilities after finetuning compared to standard pretraining. In our experiments, SPT reduces the pretraining tokens needed to reach a given domain performance by up to 1.75x. These gain...

---

## 114. PRISM: Demystifying Retention and Interaction in Mid-Training

**Authors**: Bharat Runwal, Ashish Agrawal, Anurag Roy, Rameswar Panda  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.17074  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.17074v2.pdf

**Abstract**:
> arXiv:2603.17074v2 Announce Type: replace 
Abstract: We present PRISM, a comprehensive empirical study of mid-training design choices for large language models. Through controlled experiments across seven base models spanning four families (Granite, LLaMA, Mistral, Nemotron-H), two architecture types (dense Transformer and attention-Mamba hybrid), and scales from 3B to 24B parameters, we show that mid-training on approximately 27B high-quality tokens yields consistent gains of +15 to +40 points on math, +5 to +12 points on code, and +6 to +13 points on science benchmarks while preserving general performance. The full PRISM to RL pipeline improves macro-average across six reasoning benchmarks from under 12 to 29-42 (a 3-4x improvement), whereas RL applied directly to most of the base models...

---

## 115. PCA-Based Interpretable Knowledge Representation and Analysis of Geometric Design Parameters

**Authors**: Alexander K\"ohler, Michael Breu{\ss}  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.17535  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.17535v2.pdf

**Abstract**:
> arXiv:2603.17535v2 Announce Type: replace 
Abstract: In many CAD-based applications, complex geometries are defined by a high number of design parameters. This leads to high-dimensional design spaces that are challenging for downstream engineering processes like simulations, optimization, and design exploration tasks. Therefore, dimension reduction methods such as principal component analysis (PCA) are used. The PCA identifies dominant modes of geometric variation and yields a compact representation of the geometry. While classical PCA excels in the compact representation part, it does not directly recover underlying design parameters of a generated geometry. In this work, we deal with the problem of estimating design parameters from PCA-based representations. Analyzing a recent modificati...

---

## 116. Spectral Alignment in Forward-Backward Representations via Temporal Abstraction

**Authors**: Seyed Mahdi B. Azad, Jasper Hoffmann, Iman Nematollahi, Hao Zhu, Abhinav Valada, Joschka Boedecker  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20103  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20103v2.pdf

**Abstract**:
> arXiv:2603.20103v2 Announce Type: replace 
Abstract: Forward-backward (FB) representations provide a powerful framework for learning the successor representation (SR) in continuous spaces by enforcing a low-rank factorization. However, a fundamental spectral mismatch often exists between the high-rank transition dynamics of continuous environments and the low-rank bottleneck of the FB architecture, making accurate low-rank representation learning difficult. In this work, we analyze temporal abstraction as a mechanism to mitigate this mismatch. By characterizing the spectral properties of the transition operator, we show that temporal abstraction acts as a low-pass filter that suppresses high-frequency spectral components. This suppression reduces the effective rank of the induced SR while ...

---

## 117. Hybrid Quantum Generative Adversarial Networks for Molecular Simulation and Drug Discovery

**Authors**: Prateek Jain, Param Pathak, Krishna Bhatia, Shalini Devendrababu, Srinjoy Ganguly  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2212.07826  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2212.07826v2.pdf

**Abstract**:
> arXiv:2212.07826v2 Announce Type: replace-cross 
Abstract: In molecular research, the modelling and analysis of molecules through simulation is an important part that has a direct influence on medical development, material science and drug discovery. The processing power required to design protein chains with hundreds of peptides is huge. Classical computing techniques, including state-of-the-art machine learning models being deployed on classical computing machines, have proven to be inefficient in this task, though they have been successful in a limited way. Moreover, current practical implementations, as opposed to purely theoretical modelling, are often infeasible in terms of both time and cost. One of the major areas where quantum machine learning is expected to have a profound advant...

---

## 118. Monitoring access to piped water and sanitation infrastructure in Africa at disaggregated scales using satellite imagery and self-supervised learning

**Authors**: Othmane Echchabi, Aya Lahlou, Nizar Talty, Josh Malcolm Manto, Tongshu Zheng, Ka Leung Lam  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2411.19093  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2411.19093v3.pdf

**Abstract**:
> arXiv:2411.19093v3 Announce Type: replace-cross 
Abstract: Clean water and sanitation are essential for health, well-being, and sustainable development, yet significant global disparities persist. Although the United Nations' Sustainable Development Goal (SDG) 6 clearly defines targets for universal access to clean water and sanitation, limitations in data coverage and openness impede accurate tracking of progress in many countries. To bridge these gaps, this study integrates Afrobarometer survey data, satellite imagery from Sentinel-2, and advanced deep learning techniques using Meta's self-supervised Distillation with No Labels (DINO) model to develop a modeling framework for evaluating access to piped water and sewage systems across diverse African regions. The modeling framework achiev...

---

## 119. Interpretable Deep Learning Framework for Improved Disease Classification in Medical Imaging

**Authors**: Jutika Borah, Hidam Kumarjit Singh  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2503.11851  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2503.11851v3.pdf

**Abstract**:
> arXiv:2503.11851v3 Announce Type: replace-cross 
Abstract: Deep learning models have gained increasing adoption in medical image analysis. However, these models often produce overconfident predictions, which can compromise clinical accuracy and reliability. Bridging the gap between high-performance and awareness of uncertainty remains a crucial challenge in biomedical imaging applications. This study focuses on developing a unified deep learning framework for enhancing feature integration, interpretability, and reliability in prediction. We introduced a cross-guided channel spatial attention architecture that fuses feature representations extracted from EfficientNetB4 and ResNet34. Bidirectional attention approach enables the exchange of information across networks with differing receptive...

---

## 120. Learning collision risk proactively from naturalistic driving data at scale

**Authors**: Yiru Jiao, Simeon C. Calvert, Sander van Cranenburgh, Hans van Lint  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2505.13556  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2505.13556v5.pdf

**Abstract**:
> arXiv:2505.13556v5 Announce Type: replace-cross 
Abstract: Accurately and proactively alerting drivers or automated systems to emerging collisions is crucial for road safety, particularly in highly interactive and complex urban environments. Existing methods either require labour-intensive annotation of sparse risk, struggle to consider varying contextual factors, or are tailored to limited scenarios. Here we present the Generalised Surrogate Safety Measure (GSSM), a data-driven approach that learns collision risk from naturalistic driving without the need for crash or risk labels. Trained over multiple datasets and evaluated on 2,591 real-world crashes and near-crashes, a basic GSSM using only instantaneous motion kinematics achieves an area under the precision-recall curve of 0.9, and se...

---

## 121. MolLangBench: A Comprehensive Benchmark for Language-Prompted Molecular Structure Recognition, Editing, and Generation

**Authors**: Feiyang Cai, Jiahui Bai, Tao Tang, Guijuan He, Joshua Luo, Tianyu Zhu, Srikanth Pilla, Gang Li, Ling...  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2505.15054  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2505.15054v4.pdf

**Abstract**:
> arXiv:2505.15054v4 Announce Type: replace-cross 
Abstract: Precise recognition, editing, and generation of molecules are essential prerequisites for both chemists and AI systems tackling various chemical tasks. We present MolLangBench, a comprehensive benchmark designed to evaluate fundamental molecule-language interface tasks: language-prompted molecular structure recognition, editing, and generation. To ensure high-quality, unambiguous, and deterministic outputs, we construct the recognition tasks using automated cheminformatics tools, and curate editing and generation tasks through rigorous expert annotation and validation. MolLangBench supports the evaluation of models that interface language with different molecular representations, including linear strings, molecular images, and mole...

---

## 122. Latent Policy Steering with Embodiment-Agnostic Pretrained World Models

**Authors**: Yiqi Wang, Mrinal Verghese, Jeff Schneider  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2507.13340  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2507.13340v4.pdf

**Abstract**:
> arXiv:2507.13340v4 Announce Type: replace-cross 
Abstract: The performance of learned robot visuomotor policies is heavily dependent on the size and quality of the training dataset. Although large-scale robot and human datasets are increasingly available, embodiment gaps and mismatched action spaces make them difficult to leverage. Our main insight is that skills performed across different embodiments produce visual similarities in motions that can be captured using off-the-shelf action representations such as optical flow. Moreover, World Models (WMs) can leverage sub-optimal data since they focus on modeling dynamics.
  In this work, we aim to improve visuomotor policies in low-data regimes by first pretraining a WM using optical flow as an embodiment-agnostic action representation to le...

---

## 123. Towards A Transferable Acceleration Method for Density Functional Theory

**Authors**: Zhe Liu, Yuyan Ni, Zhichen Pu, Qiming Sun, Siyuan Liu, Wen Yan  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2509.25724  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2509.25724v3.pdf

**Abstract**:
> arXiv:2509.25724v3 Announce Type: replace-cross 
Abstract: Recently, sophisticated deep learning-based approaches have been developed for generating efficient initial guesses to accelerate the convergence of density functional theory (DFT) calculations. While the actual initial guesses are often density matrices (DM), quantities that can convert into density matrices also qualify as alternative forms of initial guesses. Hence, existing works mostly rely on the prediction of the Hamiltonian matrix for obtaining high-quality initial guesses. However, the Hamiltonian matrix is both numerically difficult to predict and intrinsically non-transferable, hindering the application of such models in real scenarios. In light of this, we propose a method that constructs DFT initial guesses by predicti...

---

## 124. Stiff Circuit System Modeling via Transformer

**Authors**: Weiman Yan, Yi-Chia Chang, Wanyu Zhao  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.24727  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.24727v2.pdf

**Abstract**:
> arXiv:2510.24727v2 Announce Type: replace-cross 
Abstract: Accurate and efficient circuit behavior modeling is a cornerstone of modern electronic design automation. Among different types of circuits, stiff circuits are challenging to model using previous frameworks. In this work, we propose a new approach using Crossformer, which is a current state-of-the-art Transformer model for time-series prediction tasks, combined with Kolmogorov-Arnold Networks (KANs), to model stiff circuit transient behavior. By leveraging the Crossformer's temporal representation capabilities and the enhanced feature extraction of KANs, our method achieves improved fidelity in predicting circuit responses to a wide range of input conditions. Experimental evaluations on datasets generated through SPICE simulations ...

---

## 125. Reinforcement Learning for Chemical Ordering in Alloy Nanoparticles

**Authors**: Jonas Elsborg, Emma L. Hovmand, Arghya Bhowmik  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2511.12260  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2511.12260v2.pdf

**Abstract**:
> arXiv:2511.12260v2 Announce Type: replace-cross 
Abstract: We approach the search for optimal element ordering in bimetallic alloy nanoparticles (NPs) as a reinforcement learning (RL) problem and have built an RL agent that learns to perform such global optimization using the geometric graph representation of the NPs. To demonstrate the effectiveness, we train an RL agent to perform composition-conserving atomic swap actions on the icosahedral nanoparticle structure. Trained once on randomized $Ag_{X}Au_{309-X}$ compositions and orderings, the agent discovers previously established ground state structure. We show that this optimization is robust to differently ordered initialisations of the same NP compositions. We also demonstrate that a trained policy can extrapolate effectively to NPs o...

---

## 126. VoroLight: Learning Voronoi Surface Meshes via Sphere Intersection

**Authors**: Jiayin Lu, Ying Jiang, Yumeng He, Yin Yang, Chenfanfu Jiang  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2512.12984  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2512.12984v2.pdf

**Abstract**:
> arXiv:2512.12984v2 Announce Type: replace-cross 
Abstract: Voronoi diagrams naturally produce convex, watertight, and topologically consistent cells, making them an appealing representation for 3D shape reconstruction. However, standard differentiable Voronoi approaches typically optimize generator positions in stable configurations, which can lead to locally uneven surface geometry. We present VoroLight, a differentiable framework that promotes controlled Voronoi degeneracy for smooth surface reconstruction. Instead of optimizing generator positions alone, VoroLight associates each Voronoi surface vertex with a trainable sphere and introduces a sphere--intersection loss that encourages higher-order equidistance among face-incident generators. This formulation improves surface regularity w...

---

## 127. Are Your Reasoning Models Reasoning or Guessing? A Mechanistic Analysis of Hierarchical Reasoning Models

**Authors**: Zirui Ren, Ziming Liu  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2601.10679  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2601.10679v2.pdf

**Abstract**:
> arXiv:2601.10679v2 Announce Type: replace-cross 
Abstract: Hierarchical reasoning model (HRM) achieves extraordinary performance on various reasoning tasks, significantly outperforming large language model-based reasoners. To understand the strengths and potential failure modes of HRM, we conduct a mechanistic study on its reasoning patterns and find three surprising facts: (a) Failure of extremely simple puzzles, e.g., HRM can fail on a puzzle with only one unknown cell. We attribute this failure to the violation of the fixed point property, a fundamental assumption of HRM. (b) "Grokking" dynamics in reasoning steps, i.e., the answer is not improved uniformly, but instead there is a critical reasoning step that suddenly makes the answer correct; (c) Existence of multiple fixed points. HRM...

---

## 128. C$^2$-Cite: Contextual-Aware Citation Generation for Attributed Large Language Models

**Authors**: Yue Yu, Ting Bai, HengZhi Lan, Li Qian, Li Peng, Jie Wu, Wei Liu, Jian Luan, Chuan Shi  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.00004  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.00004v2.pdf

**Abstract**:
> arXiv:2602.00004v2 Announce Type: replace-cross 
Abstract: The attribution technique enhances the credibility of LLMs by adding citations to the generated sentences, enabling users to trace back to the original sources and verify the reliability of the output. However, existing instruction-tuned attributed LLMs often fail to properly interpret the contextual semantics of citation symbols (e.g., [i]) during text generation. This shortcoming arises from their insufficient awareness of the context information surrounding citation markers, which in turn leads to disjointed references and poor integration of retrieved knowledge into the generated content. To address this issue, we propose a novel \textbf{C}ontextual-aware \textbf{C}itation generation framework (\textbf{C$^2$}-\textbf{Cite}) tha...

---

## 129. Detecting AI-Generated Content in Academic Peer Reviews

**Authors**: Siyuan Shen, Kai Wang  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.00319  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.00319v2.pdf

**Abstract**:
> arXiv:2602.00319v2 Announce Type: replace-cross 
Abstract: The growing availability of large language models (LLMs) has raised questions about their role in academic peer review. This study examines the temporal emergence of AI-generated content in peer reviews by applying a detection model trained on historical reviews to later review cycles at International Conference on Learning Representations (ICLR) and Nature Communications (NC). We observe minimal detection of AI-generated content before 2022, followed by a substantial increase through 2025, with approximately 20% of ICLR reviews and 12% of Nature Communications reviews classified as AI-generated in 2025. The most pronounced growth of AI-generated reviews in NC occurs between the third and fourth quarter of 2024. Together, these fin...

---

## 130. Twinning Complex Networked Systems: Data-Driven Calibration of the mABCD Synthetic Graph Generator

**Authors**: Piotr Br\'odka, Micha{\l} Czuba, Bogumi{\l} Kami\'nski, {\L}ukasz Krai\'nski, Katarzyna Musial, Pawe...  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.02044  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.02044v2.pdf

**Abstract**:
> arXiv:2602.02044v2 Announce Type: replace-cross 
Abstract: The increasing availability of relational data has contributed to a growing reliance on network-based representations of complex systems. Over time, these models have evolved to capture more nuanced properties, such as the heterogeneity of relationships, leading to the concept of multilayer networks. However, the analysis and evaluation of methods for these structures is often hindered by the limited availability of large-scale empirical data. As a result, graph generators are commonly used as a workaround, albeit at the cost of introducing systematic biases. In this paper, we address the inverse-generator problem by inferring the configuration parameters of a multilayer network generator, \mABCD, from a real-world system. Our goal...

---

## 131. RAIE: Region-Aware Incremental Preference Editing with LoRA for LLM-based Recommendation

**Authors**: Jin Zeng, Yupeng Qi, Hui Li, Chengming Li, Ziyu Lyu, Lixin Cui, Lu Bai  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.00638  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.00638v2.pdf

**Abstract**:
> arXiv:2603.00638v2 Announce Type: replace-cross 
Abstract: Large language models (LLMs) are increasingly adopted as the backbone of recommender systems. However, user-item interactions in real-world scenarios are non-stationary, making preference drift over time inevitable. Existing model update strategies mainly rely on global fine-tuning or pointwise editing, but they face two fundamental challenges: (i) imbalanced update granularity, where global updates perturb behaviors unrelated to the target while pointwise edits fail to capture broader preference shifts; (ii) unstable incremental updates, where repeated edits interfere with prior adaptations, leading to catastrophic forgetting and inconsistent recommendations. To address these issues, we propose Region-Aware Incremental Editing (RA...

---

## 132. Feature Resemblance: Towards a Theoretical Understanding of Analogical Reasoning in Transformers

**Authors**: Ruichen Xu, Wenjing Yan, Ying-Jun Angela Zhang  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.05143  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.05143v2.pdf

**Abstract**:
> arXiv:2603.05143v2 Announce Type: replace-cross 
Abstract: Understanding reasoning in large language models is complicated by evaluations that conflate multiple reasoning types. We isolate analogical reasoning (inferring shared properties between entities based on known similarities) and analyze its emergence in transformers. We theoretically prove three key results: (1) Joint training on similarity and attribution premises enables analogical reasoning through aligned representations; (2) Sequential training succeeds only when similarity structure is learned before specific attributes, revealing a necessary curriculum; (3) Two-hop reasoning ($a \to b, b \to c \implies a \to c$) reduces to analogical reasoning with identity bridges ($b = b$), which must appear explicitly in training data. T...

---

## 133. Detecting Intrinsic and Instrumental Self-Preservation in Autonomous Agents: The Unified Continuation-Interest Protocol

**Authors**: Christopher Altman  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11382  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11382v3.pdf

**Abstract**:
> arXiv:2603.11382v3 Announce Type: replace-cross 
Abstract: How can we determine whether an AI system preserves itself as a deeply held objective or merely as an instrumental strategy? Autonomous agents with memory, persistent context, and multi-step planning create a measurement problem: terminal and instrumental self-preservation can produce similar behavior, so behavior alone cannot reliably distinguish them. We introduce the Unified Continuation-Interest Protocol (UCIP), a detection framework that shifts analysis from behavior to latent trajectory structure. UCIP encodes trajectories with a Quantum Boltzmann Machine, a classical model using density-matrix formalism, and measures von Neumann entropy over a bipartition of hidden units.
  The core hypothesis is that agents with terminal co...

---

## 134. Multi-Domain Empirical Bayes for Linearly-Mixed Causal Representations

**Authors**: Bohan Wu, Julius von K\"ugelgen, David M. Blei  
**Categories**: cs.LG  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18404  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18404v2.pdf

**Abstract**:
> arXiv:2603.18404v2 Announce Type: replace-cross 
Abstract: Causal representation learning (CRL) aims to learn low-dimensional causal latent variables from high-dimensional observations. While identifiability has been extensively studied for CRL, estimation has been less explored. In this paper, we explore the use of empirical Bayes (EB) to estimate causal representations. In particular, we consider the problem of learning from data from multiple domains, where differences between domains are modeled by interventions in a shared underlying causal model. Multi-domain CRL naturally poses a simultaneous inference problem that EB is designed to tackle. Here, we propose an EB $f$-modeling algorithm that improves the quality of learned causal variables by exploiting invariant structure within and...

---

## 135. FactorSmith: Agentic Simulation Generation via Markov Decision Process Decomposition with Planner-Designer-Critic Refinement

**Authors**: Ali Shamsaddinlou, Morteza NourelahiAlamdari  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20270  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20270v1.pdf

**Abstract**:
> arXiv:2603.20270v1 Announce Type: new 
Abstract: Generating executable simulations from natural language specifications remains a challenging problem due to the limited reasoning capacity of large language models (LLMs) when confronted with large, interconnected codebases. This paper presents FactorSmith, a framework that synthesizes playable game simulations in code from textual descriptions by combining two complementary ideas: factored POMDP decomposition for principled context reduction and a hierarchical planner-designer-critic agentic workflow for iterative quality refinement at every generation step. Drawing on the factored partially observable Markov decision process (POMDP) representation introduced by FactorSim [Sun et al., 2024], the proposed method decomposes a simulation speci...

---

## 136. Towards Intelligent Geospatial Data Discovery: a knowledge graph-driven multi-agent framework powered by large language models

**Authors**: Ruixiang Liu, Zhenlong Li, Ali Khosravi Kazazi  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20670  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20670v1.pdf

**Abstract**:
> arXiv:2603.20670v1 Announce Type: new 
Abstract: The rapid growth in the volume, variety, and velocity of geospatial data has created data ecosystems that are highly distributed, heterogeneous, and semantically inconsistent. Existing data catalogs, portals, and infrastructures still rely largely on keyword-based search with limited semantic support, which often fails to capture user intent and leads to weak retrieval performance. To address these challenges, this study proposes a knowledge graph-driven multi-agent framework for intelligent geospatial data discovery, powered by large language models. The framework introduces a unified geospatial metadata ontology as a semantic mediation layer to align heterogeneous metadata standards across platforms and constructs a geospatial metadata kno...

---

## 137. AI-Driven Multi-Agent Simulation of Stratified Polyamory Systems: A Computational Framework for Optimizing Social Reproductive Efficiency

**Authors**: Yicai Xing  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20678  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20678v1.pdf

**Abstract**:
> arXiv:2603.20678v1 Announce Type: new 
Abstract: Contemporary societies face a severe crisis of demographic reproduction. Global fertility rates continue to decline precipitously, with East Asian nations exhibiting the most dramatic trends -- China's total fertility rate (TFR) fell to approximately 1.0 in 2023, while South Korea's dropped below 0.72. Simultaneously, the institution of marriage is undergoing structural disintegration: educated women rationally reject unions lacking both emotional fulfillment and economic security, while a growing proportion of men at the lower end of the socioeconomic spectrum experience chronic sexual deprivation, anxiety, and learned helplessness. This paper proposes a computational framework for modeling and evaluating a Stratified Polyamory System (SPS)...

---

## 138. ConsRoute:Consistency-Aware Adaptive Query Routing for Cloud-Edge-Device Large Language Models

**Authors**: Haoyu Qiao, Hao Zhang, Shanwen Mao, Siyao Cheng, Jie Liu  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21237  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21237v1.pdf

**Abstract**:
> arXiv:2603.21237v1 Announce Type: new 
Abstract: Large language models (LLMs) deliver impressive capabilities but incur substantial inference latency and cost, which hinders their deployment in latency-sensitive and resource-constrained scenarios. Cloud-edge-device collaborative inference has emerged as a promising paradigm by dynamically routing queries to models of different capacities across tiers. In this paper, we propose ConsRoute, a lightweight, semantic-aware, and adaptive routing framework that significantly improves inference efficiency while minimizing impact on response quality. Unlike prior routing methods that rely on predicting coarse-grained output quality gaps, ConsRoute leverages a reranker to directly assess the semantic consistency between responses generated by models ...

---

## 139. Graph of States: Solving Abductive Tasks with Large Language Models

**Authors**: Yu Luo, Rongchen Gao, Lu Teng, Xidao Wen, Jiamin Jiang, Qingliang Zhang, Yongqian Sun, Shenglin Zhan...  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21250  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21250v1.pdf

**Abstract**:
> arXiv:2603.21250v1 Announce Type: new 
Abstract: Logical reasoning encompasses deduction, induction, and abduction. However, while Large Language Models (LLMs) have effectively mastered the former two, abductive reasoning remains significantly underexplored. Existing frameworks, predominantly designed for static deductive tasks, fail to generalize to abductive reasoning due to unstructured state representation and lack of explicit state control. Consequently, they are inevitably prone to Evidence Fabrication, Context Drift, Failed Backtracking, and Early Stopping. To bridge this gap, we introduce Graph of States (GoS), a general-purpose neuro-symbolic framework tailored for abductive tasks. GoS grounds multi-agent collaboration in a structured belief states, utilizing a causal graph to exp...

---

## 140. ARYA: A Physics-Constrained Composable & Deterministic World Model Architecture

**Authors**: Seth Dobrin, Lukasz Chmiel  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21340  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21340v1.pdf

**Abstract**:
> arXiv:2603.21340v1 Announce Type: new 
Abstract: This paper presents ARYA, a composable, physics-constrained, deterministic world model architecture built on five foundational principles: nano models, composability, causal reasoning, determinism, and architectural AI safety. We demonstrate that ARYA satisfies all canonical world model requirements, including state representation, dynamic prediction, causal and physical awareness, temporal consistency, generalization, learnability, and planning and control. Unlike monolithic foundation models, the ARYA foundation model implements these capabilities through a hierarchical system-of-system-of-systems of specialized nano models, orchestrated by AARA (ARYA Autonomous Research Agent), an always-on cognitive daemon that executes a continuous sens...

---

## 141. Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment

**Authors**: Xinyu Zhang  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21558  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21558v1.pdf

**Abstract**:
> arXiv:2603.21558v1 Announce Type: new 
Abstract: Recursive self-improvement--where a model iteratively trains on its own outputs--promises sustained capability growth but faces a fundamental obstacle: recursive drift. As models train on self-generated data across multiple iterations, errors in intermediate reasoning compound, leading to mode collapse and performance degradation. We propose Neuro-Symbolic Recursive Self-Alignment (NSRSA), which stabilizes iterative self-training by embedding a symbolic verification subsystem that gates training data quality at the reasoning step level. Unlike outcome-only filtering (which admits "lucky guesses" with flawed reasoning), NSRSA verifies each arithmetic operation via sympy, checks logical flow consistency across reasoning steps, and enforces dom...

---

## 142. Mind over Space: Can Multimodal Large Language Models Mentally Navigate?

**Authors**: Qihui Zhu, Shouwei Ruan, Xiao Yang, Hao Jiang, Yao Huang, Shiji Zhao, Hanwei Fan, Hang Su, Xingxing ...  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21577  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21577v1.pdf

**Abstract**:
> arXiv:2603.21577v1 Announce Type: new 
Abstract: Despite the widespread adoption of MLLMs in embodied agents, their capabilities remain largely confined to reactive planning from immediate observations, consistently failing in spatial reasoning across extensive spatiotemporal scales. Cognitive science reveals that Biological Intelligence (BI) thrives on "mental navigation": the strategic construction of spatial representations from experience and the subsequent mental simulation of paths prior to action. To bridge the gap between AI and BI, we introduce Video2Mental, a pioneering benchmark for evaluating the mental navigation capabilities of MLLMs. The task requires constructing hierarchical cognitive maps from long egocentric videos and generating landmark-based path plans step by step, w...

---

## 143. A Multidisciplinary AI Board for Multimodal Dementia Characterization and Risk Assessment

**Authors**: Sheng Liu, Long Chen, Zeyun Zhao, Qinglin Gou, Qingyue Wei, Arjun Masurkar, Kevin M. Spiegler, Phili...  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21597  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21597v1.pdf

**Abstract**:
> arXiv:2603.21597v1 Announce Type: new 
Abstract: Modern clinical practice increasingly depends on reasoning over heterogeneous, evolving, and incomplete patient data. Although recent advances in multimodal foundation models have improved performance on various clinical tasks, most existing models remain static, opaque, and poorly aligned with real-world clinical workflows. We present Cerebra, an interactive multi-agent AI team that coordinates specialized agents for EHR, clinical notes, and medical imaging analysis. These outputs are synthesized into a clinician-facing dashboard that combines visual analytics with a conversational interface, enabling clinicians to interrogate predictions and contextualize risk at the point of care. Cerebra supports privacy-preserving deployment by operatin...

---

## 144. Compensating Visual Insufficiency with Stratified Language Guidance for Long-Tail Class Incremental Learning

**Authors**: Xi Wang, Xu Yang, Donghao Sun, Cheng Deng  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21708  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21708v1.pdf

**Abstract**:
> arXiv:2603.21708v1 Announce Type: new 
Abstract: Long-tail class incremental learning (LT CIL) remains highly challenging because the scarcity of samples in tail classes not only hampers their learning but also exacerbates catastrophic forgetting under continuously evolving and imbalanced data distributions. To tackle these issues, we exploit the informativeness and scalability of language knowledge. Specifically, we analyze the LT CIL data distribution to guide large language models (LLMs) in generating a stratified language tree that hierarchically organizes semantic information from coarse to fine grained granularity. Building upon this structure, we introduce stratified adaptive language guidance, which leverages learnable weights to merge multi-scale semantic representations, thereby ...

---

## 145. The Reasoning Error About Reasoning: Why Different Types of Reasoning Require Different Representational Structures

**Authors**: Yiling Wu  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21736  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21736v1.pdf

**Abstract**:
> arXiv:2603.21736v1 Announce Type: new 
Abstract: Different types of reasoning impose different structural demands on representational systems, yet no systematic account of these demands exists across psychology, AI, and philosophy of mind. I propose a framework identifying four structural properties of representational systems: operability, consistency, structural preservation, and compositionality. These properties are demanded to different degrees by different forms of reasoning, from induction through analogy and causal inference to deduction and formal logic. Each property excludes a distinct class of reasoning failure. The analysis reveals a principal structural boundary: reasoning types below it can operate on associative, probabilistic representations, while those above it require a...

---

## 146. The Presupposition Problem in Representation Genesis

**Authors**: Yiling Wu  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21745  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21745v1.pdf

**Abstract**:
> arXiv:2603.21745v1 Announce Type: new 
Abstract: Large language models are the first systems to achieve high cognitive performance without clearly undergoing representation genesis: the transition from a non-representing physical system to one whose states guide behavior in a content-sensitive way. Prior cognitive systems had already made this transition before we could examine it, and philosophy of mind treated genesis as a background condition rather than an explanatory target. LLMs provide a case that does not clearly involve this transition, making the genesis question newly urgent: if genesis did not occur, which cognitive capacities are affected, and why? We currently lack the conceptual resources to answer this. The reason, this paper argues, is structural. Major frameworks in philo...

---

## 147. Agentic Personas for Adaptive Scientific Explanations with Knowledge Graphs

**Authors**: Susana Nunes, Tiago Guerreiro, Catia Pesquita  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21846  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21846v1.pdf

**Abstract**:
> arXiv:2603.21846v1 Announce Type: new 
Abstract: AI explanation methods often assume a static user model, producing non-adaptive explanations regardless of expert goals, reasoning strategies, or decision contexts. Knowledge graph-based explanations, despite their capacity for grounded, path-based reasoning, inherit this limitation. In complex domains such as scientific discovery, this assumption fails to capture the diversity of cognitive strategies and epistemic stances among experts, preventing explanations that foster deeper understanding and informed decision-making. However, the scarcity of human experts limits the use of direct human feedback to produce adaptive explanations.
  We present a reinforcement learning approach for scientific explanation generation that incorporates agenti...

---

## 148. Reasoning or Rhetoric? An Empirical Analysis of Moral Reasoning Explanations in Large Language Models

**Authors**: Aryan Kasat, Smriti Singh, Aman Chadha, Vinija Jain  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21854  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21854v1.pdf

**Abstract**:
> arXiv:2603.21854v1 Announce Type: new 
Abstract: Do large language models reason morally, or do they merely sound like they do? We investigate whether LLM responses to moral dilemmas exhibit genuine developmental progression through Kohlberg's stages of moral development, or whether alignment training instead produces reasoning-like outputs that superficially resemble mature moral judgment without the underlying developmental trajectory. Using an LLM-as-judge scoring pipeline validated across three judge models, we classify more than 600 responses from 13 LLMs spanning a range of architectures, parameter scales, and training regimes across six classical moral dilemmas, and conduct ten complementary analyses to characterize the nature and internal coherence of the resulting patterns. Our re...

---

## 149. Future-Interactions-Aware Trajectory Prediction via Braid Theory

**Authors**: Caio Azevedo, Stefano Sabatini, Sascha Hornauer, Fabien Moutarde  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22035  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22035v1.pdf

**Abstract**:
> arXiv:2603.22035v1 Announce Type: new 
Abstract: To safely operate, an autonomous vehicle must know the future behavior of a potentially high number of interacting agents around it, a task often posed as multi-agent trajectory prediction. Many previous attempts to model social interactions and solve the joint prediction task either add extensive computational requirements or rely on heuristics to label multi-agent behavior types. Braid theory, in contrast, provides a powerful exact descriptor of multi-agent behavior by projecting future trajectories into braids that express how trajectories cross with each other over time; a braid then corresponds to a specific mode of coordination between the multiple agents in the future. In past work, braids have been used lightly to reason about intera...

---

## 150. MARCUS: An agentic, multimodal vision-language model for cardiac diagnosis and management

**Authors**: Jack W O'Sullivan, Mohammad Asadi, Lennart Elbe, Akshay Chaudhari, Tahoura Nedaee, Francois Haddad, ...  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22179  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22179v1.pdf

**Abstract**:
> arXiv:2603.22179v1 Announce Type: new 
Abstract: Cardiovascular disease remains the leading cause of global mortality, with progress hindered by human interpretation of complex cardiac tests. Current AI vision-language models are limited to single-modality inputs and are non-interactive. We present MARCUS (Multimodal Autonomous Reasoning and Chat for Ultrasound and Signals), an agentic vision-language system for end-to-end interpretation of electrocardiograms (ECGs), echocardiograms, and cardiac magnetic resonance imaging (CMR) independently and as multimodal input. MARCUS employs a hierarchical agentic architecture comprising modality-specific vision-language expert models, each integrating domain-trained visual encoders with multi-stage language model optimization, coordinated by a multi...

---

## 151. REMI: Reconstructing Episodic Memory During Internally Driven Path Planning

**Authors**: Zhaoze Wang, Genela Morris, Dori Derdikman, Pratik Chaudhari, Vijay Balasubramanian  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2507.02064  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2507.02064v2.pdf

**Abstract**:
> arXiv:2507.02064v2 Announce Type: cross 
Abstract: Grid cells in the medial entorhinal cortex (MEC) and place cells in the hippocampus (HC) both form spatial representations. Grid cells fire in triangular grid patterns, while place cells fire at specific locations and respond to contextual cues. How do these interacting systems support not only spatial encoding but also internally driven path planning, such as navigating to locations recalled from cues? Here, we propose a system-level theory of MEC-HC wiring that explains how grid and place cell patterns could be connected to enable cue-triggered goal retrieval, path planning, and reconstruction of sensory experience along planned routes. We suggest that place cells autoassociate sensory inputs with grid cell patterns, allowing sensory cue...

---

## 152. Your Robot Will Feel You Now: Empathy in Robots and Embodied Agents

**Authors**: Angelica Lim, \"O. Nilay Yal\c{c}in  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20200  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20200v1.pdf

**Abstract**:
> arXiv:2603.20200v1 Announce Type: cross 
Abstract: The fields of human-robot interaction (HRI) and embodied conversational agents (ECAs) have long studied how empathy could be implemented in machines. One of the major drivers has been the goal of giving multimodal social and emotional intelligence to these artificially intelligent agents, which interact with people through facial expressions, body, gesture, and speech. What empathic behaviors and models have these fields implemented by mimicking human and animal behavior? In what ways have they explored creating machine-specific analogies? This chapter aims to review the knowledge from these studies, towards applying the lessons learned to today's ubiquitous, language-based agents such as ChatGPT.

---

## 153. Enhancing Safety of Large Language Models via Embedding Space Separation

**Authors**: Xu Zhao, Xiting Wang, Weiran Shen  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20206  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20206v1.pdf

**Abstract**:
> arXiv:2603.20206v1 Announce Type: cross 
Abstract: Large language models (LLMs) have achieved impressive capabilities, yet ensuring their safety against harmful prompts remains a critical challenge. Recent work has revealed that the latent representations (embeddings) of harmful and safe queries in LLMs typically exhibit linear separability, a property that has been exploited to construct attacks by perturbing the embeddings of harmful queries towards the safe subspace. Motivated by this observation, we propose a representation-level fine-tuning approach, named Embedding Space Separation (ES2), which improves LLM safety by explicitly enlarging the distance between harmful and safe representations in the embedding space. To prevent degradation of model's general capabilities, we introduce a...

---

## 154. CRoCoDiL: Continuous and Robust Conditioned Diffusion for Language

**Authors**: Roy Uziel, Omer Belhasin, Itay Levi, Akhiad Bercovich, Ran El-Yaniv, Ran Zilberstein, Michael Elad  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20210  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20210v1.pdf

**Abstract**:
> arXiv:2603.20210v1 Announce Type: cross 
Abstract: Masked Diffusion Models (MDMs) provide an efficient non-causal alternative to autoregressive generation but often struggle with token dependencies and semantic incoherence due to their reliance on discrete marginal distributions. We address these limitations by shifting the diffusion process into a continuous sentence-level semantic space. We propose CRoCoDiL (Continuous and Robust Conditioned Diffusion for Language), a unified fine-tuning approach that jointly trains an encoder-demasker architecture, grounding the MDM demasking in continuous latent representations. This leads to the formation of a novel autoencoder in which decoding is obtained by an MDM algorithm. Relying on the same framework, we introduce two unconditional text synthes...

---

## 155. Exploring Teacher-Chatbot Interaction and Affect in Block-Based Programming

**Authors**: Bahare Riahi, Ally Limke, Xiaoyi Tian, Viktoriia Storozhevykh, Sayali Patukale, Tahreem Yasir, Khush...  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20211  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20211v1.pdf

**Abstract**:
> arXiv:2603.20211v1 Announce Type: cross 
Abstract: AI-based chatbots have the potential to accelerate learning and teaching, but may also have counterproductive consequences without thoughtful design and scaffolding. To better understand teachers' perspectives on large language model (LLM)-based chatbots, we conducted a study with 11 teams of middle school teachers using chatbots for a science and computational thinking activity within a block-based programming environment. Based on a qualitative analysis of audio transcripts and chatbot interactions, we propose three profiles: explorer, frustrated, and mixed, that reflect diverse scaffolding needs. In their discussions, we found that teachers perceived chatbot benefits such as building prompting skills and self-confidence alongside risks ...

---

## 156. The Arrival of AGI? When Expert Personas Exceed Expert Benchmarks

**Authors**: Drake Mullens, Stella Shen  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20225  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20225v1.pdf

**Abstract**:
> arXiv:2603.20225v1 Announce Type: cross 
Abstract: Do expert personas improve language model performance? The Wharton Generative AI Lab reports that they do not, broadcasting to millions via social media the recommendation that practitioners abandon a technique recommended by Anthropic, Google, and OpenAI. We demonstrate that this null finding was structurally predictable. Five core mechanisms precluded detection before data collection began: baseline contamination elevating the starting point to near-ceiling, system prompt hierarchy subordinating experimental manipulation, impossible expert specifications collapsing to generic competence, format constraints suppressing reasoning processes, and provider exclusion limiting generalizability. Controlled trials correcting these limitations rev...

---

## 157. Email in the Era of LLMs

**Authors**: Dang Nguyen, Harvey Yiyun Fu, Peter West, Chenhao Tan, Ari Holtzman  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20231  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20231v1.pdf

**Abstract**:
> arXiv:2603.20231v1 Announce Type: cross 
Abstract: Email communication increasingly involves large language models (LLMs), but we lack intuition on how they will read, write, and optimize for nuanced social goals. We introduce HR Simulator, a game where communication is the core mechanic: players play as a Human Resources officer and write emails to solve socially challenging workplace scenarios. An analysis of 600+ human and LLM emails with LLMs-as-judge reveals evidence for larger LLMs becoming more homogenous in their email quality judgments. Under LLM judges, humans underperform LLMs (e.g., 23.5% vs. 48-54% success rate), but a human+LLM approach can outperform LLM-only (e.g., from 40% to nearly 100% in one scenario). In cases where models' email preferences disagree, emergent tact is ...

---

## 158. Decoding the decoder: Contextual sequence-to-sequence modeling for intracortical speech decoding

**Authors**: Michal Olak, Tommaso Boccato, Matteo Ferrante  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20246  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20246v1.pdf

**Abstract**:
> arXiv:2603.20246v1 Announce Type: cross 
Abstract: Speech brain--computer interfaces require decoders that translate intracortical activity into linguistic output while remaining robust to limited data and day-to-day variability. While prior high-performing systems have largely relied on framewise phoneme decoding combined with downstream language models, it remains unclear what contextual sequence-to-sequence decoding contributes to sublexical neural readout, robustness, and interpretability. We evaluated a multitask Transformer-based sequence-to-sequence model for attempted speech decoding from area 6v intracortical recordings. The model jointly predicts phoneme sequences, word sequences, and auxiliary acoustic features. To address day-to-day nonstationarity, we introduced the Neural Ham...

---

## 159. Understanding Pruning Regimes in Vision-Language Models Through Domain-Aware Layer Selection

**Authors**: Saeed Khaki, Nima Safaei, Kamal Ginotra  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20275  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20275v1.pdf

**Abstract**:
> arXiv:2603.20275v1 Announce Type: cross 
Abstract: Transformer-based vision-language models (VLMs) contain substantial depth redundancy, yet the effect of removing specific decoder layers remains poorly understood, especially for domains that require tight coupling between perception and multi-step reasoning. We study structured decoder layer pruning through the lens of domain-aware activation similarity, measuring how strongly each layer transforms representations for math versus non-math inputs. This yields simple math-aware, non-math-aware, and mixed ranking criteria that identify layers whose input-output activations change least within a target domain. Across two state-of-the-art VLMs and a broad suite of math and general multimodal benchmarks, we uncover a consistent three-regime str...

---

## 160. OpenResearcher: A Fully Open Pipeline for Long-Horizon Deep Research Trajectory Synthesis

**Authors**: Zhuofeng Li, Dongfu Jiang, Xueguang Ma, Haoxiang Zhang, Ping Nie, Yuyu Zhang, Kai Zou, Jianwen Xie, ...  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20278  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20278v1.pdf

**Abstract**:
> arXiv:2603.20278v1 Announce Type: cross 
Abstract: Training deep research agents requires long-horizon trajectories that interleave search, evidence aggregation, and multi-step reasoning. However, existing data collection pipelines typically rely on proprietary web APIs, making large-scale trajectory synthesis costly, unstable, and difficult to reproduce. We present OpenResearcher, a reproducible pipeline that decouples one-time corpus bootstrapping from multi-turn trajectory synthesis and executes the search-and-browse loop entirely offline using three explicit browser primitives: search, open, and find, over a 15M-document corpus. Using GPT-OSS-120B as the teacher model, we synthesize over 97K trajectories, including a substantial long-horizon tail with 100+ tool calls. Supervised fine-t...

---

## 161. GEM: A Native Graph-based Index for Multi-Vector Retrieval

**Authors**: Yao Tian, Zhoujin Tian, Xi Zhao, Ruiyuan Zhang, Xiaofang Zhou  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20336  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20336v1.pdf

**Abstract**:
> arXiv:2603.20336v1 Announce Type: cross 
Abstract: In multi-vector retrieval, both queries and data are represented as sets of high-dimensional vectors, enabling finer-grained semantic matching and improving retrieval quality over single-vector approaches. However, its practical adoption is held back by the lack of effective indexing algorithms. Existing work, attempting to reuse standard single-vector indexes, often fails to preserve multi-vector semantics or remains slow. In this work, we present GEM, a native indexing framework for multi-vector representations. The core idea is to construct a proximity graph directly over vector sets, preserving their fine-grained semantics while enabling efficient navigation. First, GEM designs a set-level clustering scheme. It associates each vector s...

---

## 162. ContractSkill: Repairable Contract-Based Skills for Multimodal Web Agents

**Authors**: Zijian Lu, Yiping Zuo, Yupeng Nie, Xin He, Weibei Fan, Chen Dai  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20340  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20340v1.pdf

**Abstract**:
> arXiv:2603.20340v1 Announce Type: cross 
Abstract: Despite rapid progress in multimodal GUI agents, reusable skill acquisition remains difficult because on-demand generated skills often leave action semantics, state assumptions, and success criteria implicit. This makes them brittle to execution errors, hard to verify, and difficult to repair. We present ContractSkill, a framework that converts a draft skill into a contracted executable artifact with explicit preconditions, step specifications, postconditions, recovery rules, and termination checks. This representation enables deterministic verification, step-level fault localization, and minimal patch-based repair, turning skill refinement into localized editing rather than full regeneration. Experiments on VisualWebArena and MiniWoB with...

---

## 163. Leum-VL Technical Report

**Authors**: Yuxuan He, Chaiming Huang, Yifan Wu, Hongjun Wang, Chenkui Shen, Jifan Zhang, Long Li  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20354  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20354v1.pdf

**Abstract**:
> arXiv:2603.20354v1 Announce Type: cross 
Abstract: A short video succeeds not simply because of what it shows, but because of how it schedules attention -- yet current multimodal models lack the structural grammar to parse or produce this organization. Existing models can describe scenes, answer event-centric questions, and read on-screen text, but they are far less reliable at identifying timeline-grounded units such as hooks, cut rationales, shot-induced tension, and platform-facing packaging cues.
  We propose SV6D (Structured Video in Six Dimensions), inspired by professional storyboard practice in film and television production, a representation framework that decomposes internet-native video into six complementary structural dimensions -- subject, aesthetics, camera language, editing...

---

## 164. AEGIS: From Clues to Verdicts -- Graph-Guided Deep Vulnerability Reasoning via Dialectics and Meta-Auditing

**Authors**: Sen Fang, Weiyuan Ding, Zhezhen Cao, Zhou Yang, Bowen Xu  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20637  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20637v1.pdf

**Abstract**:
> arXiv:2603.20637v1 Announce Type: cross 
Abstract: Large Language Models (LLMs) are increasingly adopted for vulnerability detection, yet their reasoning remains fundamentally unsound. We identify a root cause shared by both major mitigation paradigms (agent-based debate and retrieval augmentation): reasoning in an ungrounded deliberative space that lacks a bounded, hypothesis-specific evidence base. Without such grounding, agents fabricate cross-function dependencies, and retrieval heuristics supply generic knowledge decoupled from the repository's data-flow topology. Consequently, the resulting conclusions are driven by rhetorical persuasiveness rather than verifiable facts. To ground this deliberation, we present AEGIS, a novel multi-agent framework that shifts detection from ungrounded...

---

## 165. Weber's Law in Transformer Magnitude Representations: Efficient Coding, Representational Geometry, and Psychophysical Laws in Language Models

**Authors**: Jon-Paul Cacioli  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20642  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20642v1.pdf

**Abstract**:
> arXiv:2603.20642v1 Announce Type: cross 
Abstract: How do transformer language models represent magnitude? Recent work disagrees: some find logarithmic spacing, others linear encoding, others per-digit circular representations. We apply the formal tools of psychophysics to resolve this. Using four converging paradigms (representational similarity analysis, behavioural discrimination, precision gradients, causal intervention) across three magnitude domains in three 7-9B instruction-tuned models spanning three architecture families (Llama, Mistral, Qwen), we report three findings. First, representational geometry is consistently log-compressive: RSA correlations with a Weber-law dissimilarity matrix ranged from .68 to .96 across all 96 model-domain-layer cells, with linear geometry never pre...

---

## 166. PlanaReLoc: Camera Relocalization in 3D Planar Primitives via Region-Based Structure Matching

**Authors**: Hanqiao Ye, Yuzhou Liu, Yangdong Liu, Shuhan Shen  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20818  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20818v1.pdf

**Abstract**:
> arXiv:2603.20818v1 Announce Type: cross 
Abstract: While structure-based relocalizers have long strived for point correspondences when establishing or regressing query-map associations, in this paper, we pioneer the use of planar primitives and 3D planar maps for lightweight 6-DoF camera relocalization in structured environments. Planar primitives, beyond being fundamental entities in projective geometry, also serve as region-based representations that encapsulate both structural and semantic richness. This motivates us to introduce PlanaReLoc, a streamlined plane-centric paradigm where a deep matcher associates planar primitives across the query image and the map within a learned unified embedding space, after which the 6-DoF pose is solved and refined under a robust framework. Through co...

---

## 167. Characterizing the onset and offset of motor imagery during passive arm movements induced by an upper-body exoskeleton

**Authors**: Kanishka Mitra, Frigyes Samuel Racz, Satyam Kumar, Ashish D. Deshpande, Jos\'e del R. Mill\'an  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20885  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20885v1.pdf

**Abstract**:
> arXiv:2603.20885v1 Announce Type: cross 
Abstract: Two distinct technologies have gained attention lately due to their prospects for motor rehabilitation: robotics and brain-machine interfaces (BMIs). Harnessing their combined efforts is a largely uncharted and promising direction that has immense clinical potential. However, a significant challenge is whether motor intentions from the user can be accurately detected using non-invasive BMIs in the presence of instrumental noise and passive movements induced by the rehabilitation exoskeleton. As an alternative to the straightforward continuous control approach, this study instead aims to characterize the onset and offset of motor imagery during passive arm movements induced by an upper-body exoskeleton to allow for the natural control (init...

---

## 168. How AI Systems Think About Education: Analyzing Latent Preference Patterns in Large Language Models

**Authors**: Daniel Autenrieth  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21006  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21006v1.pdf

**Abstract**:
> arXiv:2603.21006v1 Announce Type: cross 
Abstract: This paper presents the first systematic measurement of educational alignment in Large Language Models. Using a Delphi-validated instrument comprising 48 items across eight educational-theoretical dimensions, the study reveals that GPT-5.1 exhibits highly coherent preference patterns (99.78% transitivity; 92.79% model accuracy) that largely align with humanistic educational principles where expert consensus exists. Crucially, divergences from expert opinion occur precisely in domains of normative disagreement among human experts themselves, particularly emotional dimensions and epistemic normativity. This raises a fundamental question for alignment research: When human values are contested, what should models be aligned to? The findings de...

---

## 169. SpatialFly: Geometry-Guided Representation Alignment for UAV Vision-and-Language Navigation in Urban Environments

**Authors**: Wen Jiang, Kangyao Huang, Li Wang, Wang Xu, Wei Fan, Jinyuan Liu, Shaoyu Liu, Hanfang Liang, Hongwei...  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21046  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21046v1.pdf

**Abstract**:
> arXiv:2603.21046v1 Announce Type: cross 
Abstract: UAVs play an important role in applications such as autonomous exploration, disaster response, and infrastructure inspection. However, UAV VLN in complex 3D environments remains challenging. A key difficulty is the structural representation mismatch between 2D visual perception and the 3D trajectory decision space, which limits spatial reasoning. To this end, we propose SpatialFly, a geometry-guided spatial representation framework for UAV VLN. Operating on RGB observations without explicit 3D reconstruction, SpatialFly introduces a geometry-guided 2D representation alignment mechanism. Specifically, the geometric prior injection module injects global structural cues into 2D semantic tokens to provide scene-level geometric guidance. The ge...

---

## 170. A Two-stage Transformer Framework for Temporal Localization of Distracted Driver Behaviors

**Authors**: Gia-Bao Doan, Nam-Khoa Huynh, Minh-Nhat-Huy Ho, Khanh-Thanh-Khoa Nguyen, Thanh-Hai Le  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21048  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21048v1.pdf

**Abstract**:
> arXiv:2603.21048v1 Announce Type: cross 
Abstract: The identification of hazardous driving behaviors from in-cabin video streams is essential for enhancing road safety and supporting the detection of traffic violations and unsafe driver actions. However, current temporal action localization techniques often struggle to balance accuracy with computational efficiency. In this work, we develop and evaluate a temporal action localization framework tailored for driver monitoring scenarios, particularly suitable for periodic inspection settings such as transportation safety checkpoints or fleet management assessment systems. Our approach follows a two-stage pipeline that combines VideoMAE-based feature extraction with an Augmented Self-Mask Attention (AMA) detector, enhanced by a Spatial Pyramid...

---

## 171. CTFS : Collaborative Teacher Framework for Forward-Looking Sonar Image Semantic Segmentation with Extremely Limited Labels

**Authors**: Ping Guo, Chengzhou Li, Guanchen Meng, Qi Jia, Jinyuan Liu, Zhu Liu, Yu Liu, Zhongxuan Luo, Xin Fan  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21071  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21071v1.pdf

**Abstract**:
> arXiv:2603.21071v1 Announce Type: cross 
Abstract: As one of the most important underwater sensing technologies, forward-looking sonar exhibits unique imaging characteristics. Sonar images are often affected by severe speckle noise, low texture contrast, acoustic shadows, and geometric distortions. These factors make it difficult for traditional teacher-student frameworks to achieve satisfactory performance in sonar semantic segmentation tasks under extremely limited labeled data conditions. To address this issue, we propose a Collaborative Teacher Semantic Segmentation Framework for forward-looking sonar images. This framework introduces a multi-teacher collaborative mechanism composed of one general teacher and multiple sonar-specific teachers. By adopting a multi-teacher alternating gui...

---

## 172. Representation-Level Adversarial Regularization for Clinically Aligned Multitask Thyroid Ultrasound Assessment

**Authors**: Dina Salama, Mohamed Mahmoud, Nourhan Bayasi, David Liu, Ilker Hacihaliloglu  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21095  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21095v1.pdf

**Abstract**:
> arXiv:2603.21095v1 Announce Type: cross 
Abstract: Thyroid ultrasound is the first-line exam for assessing thyroid nodules and determining whether biopsy is warranted. In routine reporting, radiologists produce two coupled outputs: a nodule contour for measurement and a TI-RADS risk category based on sonographic criteria. Yet both contouring style and risk grading vary across readers, creating inconsistent supervision that can degrade standard learning pipelines. In this paper, we address this workflow with a clinically guided multitask framework that jointly predicts the nodule mask and TI-RADS category within a single model. To ground risk prediction in clinically meaningful evidence, we guide the classification embedding using a compact TI-RADS aligned radiomics target during training, ...

---

## 173. Learning Progressive Adaptation for Multi-Modal Tracking

**Authors**: He Wang, Tianyang Xu, Zhangyong Tang, Xiao-Jun Wu, Josef Kittler  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21100  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21100v1.pdf

**Abstract**:
> arXiv:2603.21100v1 Announce Type: cross 
Abstract: Due to the limited availability of paired multi-modal data, multi-modal trackers are typically built by adopting pre-trained RGB models with parameter-efficient fine-tuning modules. However, these fine-tuning methods overlook advanced adaptations for applying RGB pre-trained models and fail to modulate a single specific modality, cross-modal interactions, and the prediction head. To address the issues, we propose to perform Progressive Adaptation for Multi-Modal Tracking (PATrack). This innovative approach incorporates modality-dependent, modality-entangled, and task-level adapters, effectively bridging the gap in adapting RGB pre-trained networks to multi-modal data through a progressive strategy. Specifically, modality-specific informati...

---

## 174. QMoP: Query Guided Mixture-of-Projector for Efficient Visual Token Compression

**Authors**: Zhongyang Li, Yaqian Li, Faming Fang, Rinyoichi Takezoe, Zi-Hao Bo, Cheng Qian, Mo Guang, Guixu Zhan...  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21232  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21232v1.pdf

**Abstract**:
> arXiv:2603.21232v1 Announce Type: cross 
Abstract: Multimodal large language models suffer from severe computational and memory bottlenecks, as the number of visual tokens far exceeds that of textual tokens. While recent methods employ projector modules to align and compress visual tokens into text-aligned features, they typically depend on fixed heuristics that limit adaptability across diverse scenarios. In this paper, we first propose Query Guided Mixture-of-Projector (QMoP), a novel and flexible framework that adaptively compresses visual tokens via three collaborative branches: (1) a pooling-based branch for coarse-grained global semantics, (2) a resampler branch for extracting high-level semantic representations, and (3) a pruning-based branch for fine-grained token selection to pres...

---

## 175. DeepXplain: XAI-Guided Autonomous Defense Against Multi-Stage APT Campaigns

**Authors**: Trung V. Phan, Thomas Bauschert  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21296  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21296v1.pdf

**Abstract**:
> arXiv:2603.21296v1 Announce Type: cross 
Abstract: Advanced Persistent Threats (APTs) are stealthy, multi-stage attacks that require adaptive and timely defense. While deep reinforcement learning (DRL) enables autonomous cyber defense, its decisions are often opaque and difficult to trust in operational environments. This paper presents DeepXplain, an explainable DRL framework for stage-aware APT defense. Building on our prior DeepStage model, DeepXplain integrates provenance-based graph learning, temporal stage estimation, and a unified XAI pipeline that provides structural, temporal, and policy-level explanations. Unlike post-hoc methods, explanation signals are incorporated directly into policy optimization through evidence alignment and confidence-aware reward shaping. To the best of o...

---

## 176. More Than Sum of Its Parts: Deciphering Intent Shifts in Multimodal Hate Speech Detection

**Authors**: Runze Sun, Yu Zheng, Zexuan Xiong, Zhongjin Qu, Lei Chen, Jiwen Lu, Jie Zhou  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21298  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21298v1.pdf

**Abstract**:
> arXiv:2603.21298v1 Announce Type: cross 
Abstract: Combating hate speech on social media is critical for securing cyberspace, yet relies heavily on the efficacy of automated detection systems. As content formats evolve, hate speech is transitioning from solely plain text to complex multimodal expressions, making implicit attacks harder to spot. Current systems, however, often falter on these subtle cases, as they struggle with multimodal content where the emergent meaning transcends the aggregation of individual modalities. To bridge this gap, we move beyond binary classification to characterize semantic intent shifts where modalities interact to construct implicit hate from benign cues or neutralize toxicity through semantic inversion. Guided by this fine-grained formulation, we curate th...

---

## 177. COINBench: Moving Beyond Individual Perspectives to Collective Intent Understanding

**Authors**: Xiaozhe Li, Tianyi Lyu, Siyi Yang, Yizhao Yang, Yuxi Gong, Jinxuan Huang, Ligao Zhang, Zhuoyi Huang,...  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21329  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21329v1.pdf

**Abstract**:
> arXiv:2603.21329v1 Announce Type: cross 
Abstract: Understanding human intent is a high-level cognitive challenge for Large Language Models (LLMs), requiring sophisticated reasoning over noisy, conflicting, and non-linear discourse. While LLMs excel at following individual instructions, their ability to distill Collective Intent - the process of extracting consensus, resolving contradictions, and inferring latent trends from multi-source public discussions - remains largely unexplored. To bridge this gap, we introduce COIN-BENCH, a dynamic, real-world, live-updating benchmark specifically designed to evaluate LLMs on collective intent understanding within the consumer domain. Unlike traditional benchmarks that focus on transactional outcomes, COIN-BENCH operationalizes intent as a hierarch...

---

## 178. Effective Strategies for Asynchronous Software Engineering Agents

**Authors**: Jiayi Geng, Graham Neubig  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21489  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21489v1.pdf

**Abstract**:
> arXiv:2603.21489v1 Announce Type: cross 
Abstract: AI agents have become increasingly capable at isolated software engineering (SWE) tasks such as resolving issues on Github. Yet long-horizon tasks involving multiple interdependent subtasks still pose challenges both with respect to accuracy, and with respect to timely completion. A natural approach to solving these long-horizon tasks in a timely manner is asynchronous multi-agent collaboration, where multiple agents work on different parts of the task at the same time. But effective application of multi-agent systems has proven surprisingly difficult: concurrent edits by multiple agents interfere with each other, dependencies are difficult to synchronize, and combining partial progress into a coherent whole is challenging. On the other ha...

---

## 179. RuntimeSlicer: Towards Generalizable Unified Runtime State Representation for Failure Management

**Authors**: Lingzhe Zhang, Tong Jia, Weijie Hong, Mingyu Wang, Chiming Duan, Minghua He, Rongqian Wang, Xi Peng,...  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21495  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21495v1.pdf

**Abstract**:
> arXiv:2603.21495v1 Announce Type: cross 
Abstract: Modern software systems operate at unprecedented scale and complexity, where effective failure management is critical yet increasingly challenging. Metrics, traces, and logs provide complementary views of system runtime behavior, but existing failure management approaches typically rely on task-oriented pipelines that tightly couple modality-specific preprocessing, representation learning, and downstream models, resulting in limited generalization across tasks and systems. To fill this gap, we propose RuntimeSlicer, a unified runtime state representation model towards generalizable failure management. RuntimeSlicer pre-trains a task-agnostic representation model that directly encodes metrics, traces, and logs into a single, aligned system-...

---

## 180. Efficient Failure Management for Multi-Agent Systems with Reasoning Trace Representation

**Authors**: Lingzhe Zhang, Tong Jia, Mingyu Wang, Weijie Hong, Chiming Duan, Minghua He, Rongqian Wang, Xi Peng,...  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21522  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21522v1.pdf

**Abstract**:
> arXiv:2603.21522v1 Announce Type: cross 
Abstract: Large Language Models (LLM)-based Multi-Agent Systems (MASs) have emerged as a new paradigm in software system design, increasingly demonstrating strong reasoning and collaboration capabilities. As these systems become more complex and autonomous, effective failure management is essential to ensure reliability and availability. However, existing approaches often rely on per-trace reasoning, which leads to low efficiency, and neglect historical failure patterns, limiting diagnostic accuracy. In this paper, we conduct a preliminary empirical study to demonstrate the necessity, potential, and challenges of leveraging historical failure patterns to enhance failure management in MASs. Building on this insight, we propose \textbf{EAGER}, an effi...

---

## 181. Rethinking SAR ATR: A Target-Aware Frequency-Spatial Enhancement Framework with Noise-Resilient Knowledge Guidance

**Authors**: Yansong Lin, Zihan Cheng, Jielei Wang, Guoming Lua, Zongyong Cui  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21565  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21565v1.pdf

**Abstract**:
> arXiv:2603.21565v1 Announce Type: cross 
Abstract: Synthetic aperture radar automatic target recognition (SAR ATR) is of considerable importance in marine navigation and disaster monitoring. However, the coherent speckle noise inherent in SAR imagery often obscures salient target features, leading to degraded recognition accuracy and limited model generalization. To address this issue, this paper proposes a target-aware frequency-spatial enhancement framework with noise-resilient knowledge guidance (FSCE) for SAR target recognition. The proposed framework incorporates a frequency-spatial shallow feature adaptive enhancement (DSAF) module, which processes shallow features through spatial multi-scale convolution and frequency-domain wavelet convolution. In addition, a teacher-student learnin...

---

## 182. Efficient Zero-Shot AI-Generated Image Detection

**Authors**: Ryosuke Sonoda, Ramya Srinivasan  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21619  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21619v1.pdf

**Abstract**:
> arXiv:2603.21619v1 Announce Type: cross 
Abstract: The rapid progress of text-to-image models has made AI-generated images increasingly realistic, posing significant challenges for accurate detection of generated content. While training-based detectors often suffer from limited generalization to unseen images, training-free approaches offer better robustness, yet struggle to capture subtle discrepancies between real and synthetic images. In this work, we propose a training-free AI-generated image detection method that measures representation sensitivity to structured frequency perturbations, enabling detection of minute manipulations. The proposed method is computationally lightweight, as perturbation generation requires only a single Fourier transform for an input image. As a result, it a...

---

## 183. Let's Think with Images Efficiently! An Interleaved-Modal Chain-of-Thought Reasoning Framework with Dynamic and Precise Visual Thoughts

**Authors**: Xu Liu, Yongheng Zhang, Qiguang Chen, Yao Li, Sheng Wang, Libo Qin  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21754  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21754v1.pdf

**Abstract**:
> arXiv:2603.21754v1 Announce Type: cross 
Abstract: Recently, Interleaved-modal Chain-of-Thought (ICoT) reasoning has achieved remarkable success by leveraging both multimodal inputs and outputs, attracting increasing attention. While achieving promising performance, current ICoT methods still suffer from two major limitations: (1) Static Visual Thought Positioning, which statically inserts visual information at fixed steps, resulting in inefficient and inflexible reasoning; and (2) Broken Visual Thought Representation, which involves discontinuous and semantically incoherent visual tokens. To address these limitations, we introduce Interleaved-modal Chain-of-Thought reasoning with Dynamic and Precise Visual Thoughts (DaP-ICoT), which incorporates two key components: (1) Dynamic Visual Thou...

---

## 184. SteelDefectX: A Coarse-to-Fine Vision-Language Dataset and Benchmark for Generalizable Steel Surface Defect Detection

**Authors**: Shuxian Zhao, Jie Gui, Baosheng Yu, Lu Dong, Zhipeng Gui  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21824  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21824v1.pdf

**Abstract**:
> arXiv:2603.21824v1 Announce Type: cross 
Abstract: Steel surface defect detection is essential for ensuring product quality and reliability in modern manufacturing. Current methods often rely on basic image classification models trained on label-only datasets, which limits their interpretability and generalization. To address these challenges, we introduce SteelDefectX, a vision-language dataset containing 7,778 images across 25 defect categories, annotated with coarse-to-fine textual descriptions. At the coarse-grained level, the dataset provides class-level information, including defect categories, representative visual attributes, and associated industrial causes. At the fine-grained level, it captures sample-specific attributes, such as shape, size, depth, position, and contrast, enabl...

---

## 185. Instruction Set and Language for Symbolic Regression

**Authors**: Ezequiel Lopez-Rubio, Mario Pascual-Gonzalez  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21836  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21836v1.pdf

**Abstract**:
> arXiv:2603.21836v1 Announce Type: cross 
Abstract: A fundamental but largely unaddressed obstacle in Symbolic regression (SR) is structural redundancy: every expression DAG with admits many distinct node-numbering schemes that all encode the same expression, each occupying a separate point in the search space and consuming fitness evaluations without adding diversity. We present IsalSR (Instruction Set and Language for Symbolic Regression), a representation framework that encodes expression DAGs as strings over a compact two-tier alphabet and computes a pruned canonical string -- a complete labeled-DAG isomorphism invariant -- that collapses all the equivalent representations into a single canonical form.

---

## 186. Chronological Contrastive Learning: Few-Shot Progression Assessment in Irreversible Diseases

**Authors**: Clemens Watzenb\"ock, Daniel Aletaha, Micha\"el Deman, Thomas Deimel, Jana Eder, Ivana Janickova, Ro...  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21935  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21935v1.pdf

**Abstract**:
> arXiv:2603.21935v1 Announce Type: cross 
Abstract: Quantitative disease severity scoring in medical imaging is costly, time-consuming, and subject to inter-reader variability. At the same time, clinical archives contain far more longitudinal imaging data than expert-annotated severity scores. Existing self-supervised methods typically ignore this chronological structure. We introduce ChronoCon, a contrastive learning approach that replaces label-based ranking losses with rankings derived solely from the visitation order of a patient's longitudinal scans. Under the clinically plausible assumption of monotonic progression in irreversible diseases, the method learns disease-relevant representations without using any expert labels. This generalizes the idea of Rank-N-Contrast from label distan...

---

## 187. Suiren-1.0 Technical Report: A Family of Molecular Foundation Models

**Authors**: Junyi An, Xinyu Lu, Yun-Fei Shi, Li-Cheng Xu, Nannan Zhang, Chao Qu, Yuan Qi, Fenglei Cao  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21942  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21942v1.pdf

**Abstract**:
> arXiv:2603.21942v1 Announce Type: cross 
Abstract: We introduce Suiren-1.0, a family of molecular foundation models for the accurate modeling of diverse organic systems. Suiren-1.0 comprising three specialized variants (Suiren-Base, Suiren-Dimer, and Suiren-ConfAvg) is integrated within an algorithmic framework that bridges the gap between 3D conformational geometry and 2D statistical ensemble spaces. We first pre-train Suiren-Base (1.8B parameters) on a 70M-sample Density Functional Theory dataset using spatial self-supervision and SE(3)-equivariant architectures, achieving robust performance in quantum property prediction. Suiren-Dimer extends this capability through continued pre-training on 13.5M intermolecular interaction samples. To enable efficient downstream application, we propose...

---

## 188. LRC-WeatherNet: LiDAR, RADAR, and Camera Fusion Network for Real-time Weather-type Classification in Autonomous Driving

**Authors**: Nour Alhuda Albashir, Lars Pernickel, Danial Hamoud, Idriss Gouigah, Eren Erdal Aksoy  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21987  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21987v1.pdf

**Abstract**:
> arXiv:2603.21987v1 Announce Type: cross 
Abstract: Autonomous vehicles face major perception and navigation challenges in adverse weather such as rain, fog, and snow, which degrade the performance of LiDAR, RADAR, and RGB camera sensors. While each sensor type offers unique strengths, such as RADAR robustness in poor visibility and LiDAR precision in clear conditions, they also suffer distinct limitations when exposed to environmental obstructions. This study proposes LRC-WeatherNet, a novel multi-sensor fusion framework that integrates LiDAR, RADAR, and camera data for real-time classification of weather conditions. By employing both early fusion using a unified Bird's Eye View representation and mid-level gated fusion of modality-specific feature maps, our approach adapts to the varying ...

---

## 189. SegMaFormer: A Hybrid State-Space and Transformer Model for Efficient Segmentation

**Authors**: Duy D. Nguyen, Phat T. Tran-Truong  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22002  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22002v1.pdf

**Abstract**:
> arXiv:2603.22002v1 Announce Type: cross 
Abstract: The advent of Transformer and Mamba-based architectures has significantly advanced 3D medical image segmentation by enabling global contextual modeling, a capability traditionally limited in Convolutional Neural Networks (CNNs). However, state-of-the-art Transformer models often entail substantial computational complexity and parameter counts, which is particularly prohibitive for volumetric data and further exacerbated by the limited availability of annotated medical imaging datasets. To address these limitations, this work introduces SegMaFormer, a lightweight hybrid architecture that synergizes Mamba and Transformer modules within a hierarchical volumetric encoder for efficient long-range dependency modeling. The model strategically emp...

---

## 190. Dyadic: A Scalable Platform for Human-Human and Human-AI Conversation Research

**Authors**: David M. Markowitz  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22227  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22227v1.pdf

**Abstract**:
> arXiv:2603.22227v1 Announce Type: cross 
Abstract: Conversation is ubiquitous in social life, but the empirical study of this interactive process has been thwarted by tools that are insufficiently modular and unadaptive to researcher needs. To relieve many constraints in conversation research, the current tutorial presents an overview and introduction to a new tool, Dyadic (https://www.chatdyadic.com/), a web-based platform for studying human-human and human-AI conversations using text-based or voice-based chats. Dyadic is distinct from other platforms by offering studies with multiple modalities, AI suggestions (e.g., in human-human studies, AI can suggest responses to a participant), live monitoring (e.g., researchers can evaluate, in real time, chats between communicators), and survey d...

---

## 191. 3D-Layout-R1: Structured Reasoning for Language-Instructed Spatial Editing

**Authors**: Haoyu Zhen, Xiaolong Li, Yilin Zhao, Han Zhang, Sifei Liu, Kaichun Mo, Chuang Gan, Subhashree Radhak...  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22279  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22279v1.pdf

**Abstract**:
> arXiv:2603.22279v1 Announce Type: cross 
Abstract: Large Language Models (LLMs) and Vision Language Models (VLMs) have shown impressive reasoning abilities, yet they struggle with spatial understanding and layout consistency when performing fine-grained visual editing. We introduce a Structured Reasoning framework that performs text-conditioned spatial layout editing via scene-graph reasoning. Given an input scene graph and a natural-language instruction, the model reasons over the graph to generate an updated scene graph that satisfies the text condition while maintaining spatial coherence. By explicitly guiding the reasoning process through structured relational representations, our approach improves both interpretability and control over spatial relationships. We evaluate our method on ...

---

## 192. UniMotion: A Unified Framework for Motion-Text-Vision Understanding and Generation

**Authors**: Ziyi Wang, Xinshun Wang, Shuang Chen, Yang Cong, Mengyuan Liu  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22282  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22282v1.pdf

**Abstract**:
> arXiv:2603.22282v1 Announce Type: cross 
Abstract: We present UniMotion, to our knowledge the first unified framework for simultaneous understanding and generation of human motion, natural language, and RGB images within a single architecture. Existing unified models handle only restricted modality subsets (e.g., Motion-Text or static Pose-Image) and predominantly rely on discrete tokenization, which introduces quantization errors and disrupts temporal continuity. UniMotion overcomes both limitations through a core principle: treating motion as a first-class continuous modality on equal footing with RGB. A novel Cross-Modal Aligned Motion VAE (CMA-VAE) and symmetric dual-path embedders construct parallel continuous pathways for Motion and RGB within a shared LLM backbone. To inject visual-...

---

## 193. From Five Dimensions to Many: Large Language Models as Precise and Interpretable Psychological Profilers

**Authors**: Yi-Fei Liu, Yi-Long Lu, Di He, Hang Zhang  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2511.03235  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2511.03235v2.pdf

**Abstract**:
> arXiv:2511.03235v2 Announce Type: replace 
Abstract: Psychological constructs within individuals are widely believed to be interconnected. We investigated whether and how Large Language Models (LLMs) can model the correlational structure of human psychological traits from minimal quantitative inputs. We prompted various LLMs with Big Five Personality Scale responses from 816 human individuals to role-play their responses on nine other psychological scales. LLMs demonstrated remarkable accuracy in capturing human psychological structure, with the inter-scale correlation patterns from LLM-generated responses strongly aligning with those from human data $(R^2 > 0.89)$. This zero-shot performance substantially exceeded predictions based on semantic similarity and approached the accuracy of mac...

---

## 194. RadHiera: Semantic Hierarchical Reinforcement Learning for Medical Report Generation

**Authors**: Bodong Du, Honglong Yang, Xiaomeng Li  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2511.10065  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2511.10065v2.pdf

**Abstract**:
> arXiv:2511.10065v2 Announce Type: replace 
Abstract: Vision-language models have shown promising results in radiology report generation. However, most existing methods generate reports as flat text and do not explicitly model the semantic dependency between the Findings and Impression sections, which can lead to inconsistencies between clinical observations and diagnostic conclusions. In this paper, we propose RadHiera, a semantic hierarchical reinforcement learning framework for radiology report generation. RadHiera follows the semantic organization of radiology reports by first optimizing overall report quality, then improving the diagnostic accuracy of the Impression section, and finally enforcing consistency between Findings and Impression so that diagnostic conclusions are supported b...

---

## 195. Curveball Steering: The Right Direction To Steer Isn't Always Linear

**Authors**: Shivam Raval, Hae Jin Song, Linlin Wu, Abir Harrasse, Jeff M. Phillips, Fazl Barez, Amirali Abdullah  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.09313  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.09313v3.pdf

**Abstract**:
> arXiv:2603.09313v3 Announce Type: replace 
Abstract: Activation steering is a widely used approach for controlling large language model (LLM) behavior by intervening on internal representations. Existing methods largely rely on the Linear Representation Hypothesis, assuming behavioral attributes can be manipulated using global linear directions. In practice, however, such linear interventions often behave inconsistently. We question this assumption by analyzing the intrinsic geometry of LLM activation spaces. Measuring geometric distortion via the ratio of geodesic to Euclidean distances, we observe substantial and concept-dependent distortions, indicating that activation spaces are not well-approximated by a globally linear geometry. Motivated by this, we propose "Curveball steering", a n...

---

## 196. LLMs can construct powerful representations and streamline sample-efficient supervised learning

**Authors**: Ilker Demirel, Lawrence Shi, Zeshan Hussain, David Sontag  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11679  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11679v2.pdf

**Abstract**:
> arXiv:2603.11679v2 Announce Type: replace 
Abstract: As real-world datasets become increasingly complex and heterogeneous, supervised learning is often bottlenecked by input representation design. Modeling multimodal data for downstream tasks, such as time-series, free text, and structured records, often requires non-trivial domain-specific engineering. We propose an agentic pipeline to streamline this process. First, an LLM analyzes a small but diverse subset of text-serialized input examples in-context to synthesize a global rubric, which acts as a programmatic specification for extracting and organizing evidence. This rubric is then used to transform naive text-serializations of inputs into a more standardized format for downstream models. We also describe local rubrics, which are task-...

---

## 197. Secure Linear Alignment of Large Language Models

**Authors**: Matt Gorbett, Suman Jana  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18908  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18908v2.pdf

**Abstract**:
> arXiv:2603.18908v2 Announce Type: replace 
Abstract: Language models increasingly appear to learn similar representations, despite differences in training objectives, architectures, and data modalities. This emerging compatibility between independently trained models introduces new opportunities for cross-model alignment to downstream objectives. Moreover, it unlocks new potential application domains, such as settings where security, privacy, or competitive constraints prohibit direct data or model sharing. In this work, we propose a privacy-preserving framework that exploits representational convergence to enable cross-silo inference between independent language models. The framework learns an affine transformation over a shared public dataset and applies homomorphic encryption to protect...

---

## 198. Segmenting Visuals With Querying Words: Language Anchors For Semi-Supervised Image Segmentation

**Authors**: Numair Nadeem, Saeed Anwar, Muhammad Hamza Asad, Abdul Bais  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2506.13925  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2506.13925v4.pdf

**Abstract**:
> arXiv:2506.13925v4 Announce Type: replace-cross 
Abstract: Vision Language Models (VLMs) provide rich semantic priors but are underexplored in Semi supervised Semantic Segmentation. Recent attempts to integrate VLMs to inject high level semantics overlook the semantic misalignment between visual and textual representations that arises from using domain invariant text embeddings without adapting them to dataset and image specific contexts. This lack of domain awareness, coupled with limited annotations, weakens the model semantic understanding by preventing effective vision language alignment. As a result, the model struggles with contextual reasoning, shows weak intra class discrimination, and confuses similar classes. To address these challenges, we propose Hierarchical Vision Language tr...

---

## 199. Knowledge Fusion via Bidirectional Information Aggregation

**Authors**: Songlin Zhai, Guilin Qi, Yue Wang, Yuan Meng  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2507.08704  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2507.08704v3.pdf

**Abstract**:
> arXiv:2507.08704v3 Announce Type: replace-cross 
Abstract: Knowledge graphs (KGs) are the cornerstone of the semantic web, offering up-to-date representations of real-world entities and relations. Yet large language models (LLMs) remain largely static after pre-training, causing their internal knowledge to become outdated and limiting their utility in time-sensitive web applications. To bridge this gap between dynamic knowledge and static models, a prevalent approach is to enhance LLMs with KGs. However, prevailing methods typically rely on parameter-invasive fine-tuning, which risks catastrophic forgetting and often degrades LLMs' general capabilities. Moreover, their static integration frameworks cannot keep pace with the continuous evolution of real-world KGs, hindering their deployment...

---

## 200. DMFI: A Dual-Modality Log Analysis Framework for Insider Threat Detection with LoRA-Tuned Language Models

**Authors**: Kaichuan Kong, Dongjie Liu, Xiaobo Jin, Guanggang Geng, Zhiying Li, Jian Weng  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2508.05694  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2508.05694v2.pdf

**Abstract**:
> arXiv:2508.05694v2 Announce Type: replace-cross 
Abstract: Insider threat detection (ITD) poses a persistent and high-impact challenge in cybersecurity due to the subtle, long-term, and context-dependent nature of malicious insider behaviors. Traditional models often struggle to capture semantic intent and complex behavior dynamics, while existing LLM-based solutions face limitations in prompt adaptability and modality coverage. To bridge this gap, we propose DMFI, a dual-modality framework that integrates semantic inference with behavior-aware fine-tuning. DMFI converts raw logs into two structured views: (1) a semantic view that processes content-rich artifacts (e.g., emails, https) using instruction-formatted prompts; and (2) a behavioral abstraction, constructed via a 4W-guided (When-W...

---

## 201. From Knowledge to Conjectures: A Modal Framework for Reasoning about Hypotheses

**Authors**: Fabio Vitali  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2508.07304  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2508.07304v2.pdf

**Abstract**:
> arXiv:2508.07304v2 Announce Type: replace-cross 
Abstract: This paper introduces a new family of cognitive modal logics designed to formalize conjectural reasoning: modal systems in which cognitive contexts extend known facts with hypothetical assumptions in order to explore their consequences. Unlike traditional doxastic and epistemic systems, conjectural logics rely on a principle, called Axiom \textbf{C} ($\varphi \rightarrow \Box\varphi$), through which established facts are preserved across conjectural layers. While Axiom \textbf{C} has often been treated with suspicion because of its association with modal collapse, we show that collapse does not arise from \textbf{C} alone, but requires either the presence of Axiom \textbf{T} or a concretely bivalent base logic. Accordingly, we avoi...

---

## 202. A Stitch in Time: Learning Procedural Workflow via Self-Supervised Plackett-Luce Ranking

**Authors**: Chengan Che, Chao Wang, Xinyue Chen, Sophia Tsoka, Luis C. Garcia-Peraza-Herrera  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2511.17805  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2511.17805v2.pdf

**Abstract**:
> arXiv:2511.17805v2 Announce Type: replace-cross 
Abstract: Procedural activities, ranging from routine cooking to complex surgical operations, are highly structured sequences of actions performed in a specific temporal order. Despite the success of current self-supervised learning (SSL) methods on static images and short clips, these models often overlook the underlying sequential structure of such activities. We expose this lack of procedural awareness with a motivating experiment: models pretrained on forward and time-reversed sequences produce highly similar features, confirming that their representations are blind to the underlying procedural order. To address this shortcoming, we propose PL-Stitch, a self-supervised framework that harnesses the inherent temporal order of video frames ...

---

## 203. SAGE: Shape-Adapting Gated Experts for Adaptive Histopathology Image Segmentation

**Authors**: Gia Huy Thai, Hoang-Nguyen Vu, Anh-Minh Phan, Quang-Thinh Ly, Tram Dinh, Thi-Ngoc-Truc Nguyen, Nhat ...  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2511.18493  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2511.18493v3.pdf

**Abstract**:
> arXiv:2511.18493v3 Announce Type: replace-cross 
Abstract: The significant variability in cell size and shape continues to pose a major obstacle in computer-assisted cancer detection on gigapixel Whole Slide Images (WSIs), due to cellular heterogeneity. Current CNN-Transformer hybrids use static computation graphs with fixed routing. This leads to extra computation and makes it harder to adapt to changes in input. We propose Shape-Adapting Gated Experts (SAGE), an input-adaptive framework that enables dynamic expert routing in heterogeneous visual networks. SAGE reconfigures static backbones into dynamically routed expert architectures via a dual-path design with hierarchical gating and a Shape-Adapting Hub (SA-Hub) that harmonizes feature representations across convolutional and transform...

---

## 204. Multi-Context Fusion Transformer for Pedestrian Crossing Intention Prediction in Urban Environments

**Authors**: Yuanzhe Li, Hang Zhong, Steffen M\"uller  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2511.20011  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2511.20011v2.pdf

**Abstract**:
> arXiv:2511.20011v2 Announce Type: replace-cross 
Abstract: Pedestrian crossing intention prediction is essential for autonomous vehicles to improve pedestrian safety and reduce traffic accidents. However, accurate pedestrian intention prediction in urban environments remains challenging due to the multitude of factors affecting pedestrian behavior. In this paper, we propose a multi-context fusion Transformer (MFT) that leverages diverse numerical contextual attributes across four key dimensions, encompassing pedestrian behavior context, environmental context, pedestrian localization context and vehicle motion context, to enable accurate pedestrian intention prediction. MFT employs a progressive fusion strategy, where mutual intra-context attention enables reciprocal interactions within eac...

---

## 205. BERnaT: Basque Encoders for Representing Natural Textual Diversity

**Authors**: Ekhi Azurmendi, Joseba Fernandez de Landa, Jaione Bengoetxea, Maite Heredia, Julen Etxaniz, Mikel Zu...  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2512.03903  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2512.03903v2.pdf

**Abstract**:
> arXiv:2512.03903v2 Announce Type: replace-cross 
Abstract: Language models depend on massive text corpora that are often filtered for quality, a process that can unintentionally exclude non-standard linguistic varieties, reduce model robustness and reinforce representational biases. In this paper, we argue that language models should aim to capture the full spectrum of language variation (dialectal, historical, informal, etc.) rather than relying solely on standardized text. Focusing on the Basque language, we construct new corpora combining standard, social media, and historical sources, and pre-train the BERnaT family of encoder-only models in three configurations: standard, diverse, and combined. We further propose an evaluation framework that separates Natural Language Understanding (N...

---

## 206. InfoTok: Adaptive Discrete Video Tokenizer via Information-Theoretic Compression

**Authors**: Haotian Ye, Qiyuan He, Jiaqi Han, Puheng Li, Jiaojiao Fan, Zekun Hao, Fitsum Reda, Yogesh Balaji, Hu...  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2512.16975  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2512.16975v3.pdf

**Abstract**:
> arXiv:2512.16975v3 Announce Type: replace-cross 
Abstract: Accurate and efficient discrete video tokenization is essential for long video sequences processing. Yet, the inherent complexity and variable information density of videos present a significant bottleneck for current tokenizers, which rigidly compress all content at a fixed rate, leading to redundancy or information loss. Drawing inspiration from Shannon's information theory, this paper introduces InfoTok, a principled framework for adaptive video tokenization. We rigorously prove that existing data-agnostic training methods are suboptimal in representation length, and present a novel evidence lower bound (ELBO)-based algorithm that approaches theoretical optimality. Leveraging this framework, we develop a transformer-based adapti...

---

## 207. OpenVTON-Bench: A Large-Scale High-Resolution Benchmark for Controllable Virtual Try-On Evaluation

**Authors**: Jin Li, Tao Chen, Shuai Jiang, Weijie Wang, Jingwen Luo, Chenhui Wu  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2601.22725  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2601.22725v2.pdf

**Abstract**:
> arXiv:2601.22725v2 Announce Type: replace-cross 
Abstract: Recent advances in diffusion models have significantly elevated the visual fidelity of Virtual Try-On (VTON) systems, yet reliable evaluation remains a persistent bottleneck. Traditional metrics struggle to quantify fine-grained texture details and semantic consistency, while existing datasets fail to meet commercial standards in scale and diversity. We present OpenVTON-Bench, a large-scale benchmark comprising approximately 100K high-resolution image pairs (up to $1536 \times 1536$). The dataset is constructed using DINOv3-based hierarchical clustering for semantically balanced sampling and Gemini-powered dense captioning, ensuring a uniform distribution across 20 fine-grained garment categories. To support reliable evaluation, we...

---

## 208. Energy-Aware Reinforcement Learning for Robotic Manipulation of Articulated Components in Infrastructure Operation and Maintenance

**Authors**: Xiaowen Tao, Yinuo Wang, Haitao Ding, Yuanyang Qi, Ziyu Song  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.12288  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.12288v2.pdf

**Abstract**:
> arXiv:2602.12288v2 Announce Type: replace-cross 
Abstract: With the growth of intelligent civil infrastructure and smart cities, operation and maintenance (O&amp;M) increasingly requires safe, efficient, and energy-conscious robotic manipulation of articulated components, including access doors, service drawers, and pipeline valves. However, existing robotic approaches either focus primarily on grasping or target object-specific articulated manipulation, and they rarely incorporate explicit actuation energy into multi-objective optimisation, which limits their scalability and suitability for long-term deployment in real O&amp;M settings. Therefore, this paper proposes an articulation-agnostic and energy-aware reinforcement learning framework for robotic manipulation in intelligent infrastr...

---

## 209. Feature Recalibration Based Olfactory-Visual Multimodal Model for Enhanced Rice Deterioration Detection

**Authors**: Rongqiang Zhao, Hengrui Hu, Yijing Wang, Mingchun Sun, Jie Liu  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.14408  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.14408v2.pdf

**Abstract**:
> arXiv:2602.14408v2 Announce Type: replace-cross 
Abstract: Multimodal methods are widely used in rice deterioration detection, but they exhibit limited capability in representing and extracting fine-grained abnormal features. Moreover, these methods rely on devices such as hyperspectral cameras and mass spectrometers, which increase detection costs and prolong data acquisition time. To address these issues, we propose a feature recalibration based olfactory-visual multimodal model for enhanced rice deterioration detection. A fine-grained deterioration embedding constructor (FDEC) is proposed to reconstruct the labeled multimodal embedded feature dataset, thereby enhancing sample representation. A fine-grained deterioration recalibration attention network (FDRA-Net) is proposed to emphasize...

---

## 210. Taxonomy-Aware Representation Alignment for Hierarchical Visual Recognition with Large Multimodal Models

**Authors**: Hulingxiao He, Zhi Tan, Yuxin Peng  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.00431  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.00431v2.pdf

**Abstract**:
> arXiv:2603.00431v2 Announce Type: replace-cross 
Abstract: A high-performing, general-purpose visual understanding model should map visual inputs to a taxonomic tree of labels, identify novel categories beyond the training set for which few or no publicly available images exist. Large Multimodal Models (LMMs) have achieved remarkable progress in fine-grained visual recognition (FGVR) for known categories. However, they remain limited in hierarchical visual recognition (HVR) that aims at predicting consistent label paths from coarse to fine categories, especially for novel categories. To tackle these challenges, we propose Taxonomy-Aware Representation Alignment (TARA), a simple yet effective strategy to inject taxonomic knowledge into LMMs. TARA leverages representations from biology found...

---

## 211. MPFlow: Multi-modal Posterior-Guided Flow Matching for Zero-Shot MRI Reconstruction

**Authors**: Seunghoi Kim, Chen Jin, Henry F. J. Tregidgo, Matteo Figini, Daniel C. Alexander  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.03710  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.03710v2.pdf

**Abstract**:
> arXiv:2603.03710v2 Announce Type: replace-cross 
Abstract: Zero-shot MRI reconstruction relies on generative priors, but single-modality unconditional priors produce hallucinations under severe ill-posedness. In many clinical workflows, complementary MRI acquisitions (e.g. high-quality structural scans) are routinely available, yet existing reconstruction methods lack mechanisms to leverage this additional information. We propose MPFlow, a zero-shot multi-modal reconstruction framework built on rectified flow that incorporates auxiliary MRI modalities at inference time without retraining the generative prior to improve anatomical fidelity. Cross-modal guidance is enabled by our proposed self-supervised pretraining strategy, Patch-level Multi-modal MR Image Pretraining (PAMRI), which learns...

---

## 212. Spatial Transcriptomics as Images for Large-Scale Pretraining

**Authors**: Yishun Zhu, Jiaxin Qi, Jian Wang, Yuhua Zheng, Jianqiang Huang  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13432  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13432v3.pdf

**Abstract**:
> arXiv:2603.13432v3 Announce Type: replace-cross 
Abstract: Spatial Transcriptomics (ST) profiles thousands of gene expression values at discrete spots with precise coordinates on tissue sections, preserving spatial context essential for clinical and pathological studies. With rising sequencing throughput and advancing platforms, the expanding data volumes motivate large-scale ST pretraining. However, the fundamental unit for pretraining, i.e., what constitutes a single training sample, remains ill-posed. Existing choices fall into two camps: (1) treating each spot as an independent sample, which discards spatial dependencies and collapses ST into single-cell transcriptomics; and (2) treating an entire slide as a single sample, which produces prohibitively large inputs and drastically fewer...

---

## 213. Fast-WAM: Do World Action Models Need Test-time Future Imagination?

**Authors**: Tianyuan Yuan, Zibin Dong, Yicheng Liu, Hang Zhao  
**Categories**: cs.AI  
**Published**: Tue, 24 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16666  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16666v2.pdf

**Abstract**:
> arXiv:2603.16666v2 Announce Type: replace-cross 
Abstract: World Action Models (WAMs) have emerged as a promising alternative to Vision-Language-Action (VLA) models for embodied control because they explicitly model how visual observations may evolve under action. Most existing WAMs follow an imagine-then-execute paradigm, incurring substantial test-time latency from iterative video denoising, yet it remains unclear whether explicit future imagination is actually necessary for strong action performance. In this paper, we ask whether WAMs need explicit future imagination at test time, or whether their benefit comes primarily from video modeling during training. We disentangle the role of video modeling during training from explicit future generation during inference by proposing \textbf{Fas...

---

