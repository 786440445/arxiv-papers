# arXiv Papers - 2026-03-13

**来源**: arXiv (cs.SD, eess.AS, cs.LG, cs.AI)  
**关键词**: speech, audio, music, voice, sound, Mel, representation, self-supervised  
**今日新论文**: 136 篇

---

## 1. V2A-DPO: Omni-Preference Optimization for Video-to-Audio Generation

**Authors**: Nolan Chan, Timmy Gang, Yongqian Wang, Yuzhe Liang, Dingdong Wang  
**Categories**: cs.SD  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11089  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11089v1.pdf

**Abstract**:
> arXiv:2603.11089v1 Announce Type: new 
Abstract: This paper introduces V2A-DPO, a novel Direct Preference Optimization (DPO) framework tailored for flow-based video-to-audio generation (V2A) models, incorporating key adaptations to effectively align generated audio with human preferences. Our approach incorporates three core innovations: (1) AudioScore-a comprehensive human preference-aligned scoring system for assessing semantic consistency, temporal alignment, and perceptual quality of synthesized audio; (2) an automated AudioScore-driven pipeline for generating large-scale preference pair data for DPO optimization; (3) a curriculum learning-empowered DPO optimization strategy specifically tailored for flow-based generative models. Experiments on benchmark VGGSound dataset demonstrate th...

---

## 2. Fair-Gate: Fairness-Aware Interpretable Risk Gating for Sex-Fair Voice Biometrics

**Authors**: Yangyang Qu, Todisco Massimiliano, Galdi Chiara, Evans Nicholas  
**Categories**: cs.SD  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11360  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11360v1.pdf

**Abstract**:
> arXiv:2603.11360v1 Announce Type: new 
Abstract: Voice biometric systems can exhibit sex-related performance gaps even when overall verification accuracy is strong. We attribute these gaps to two practical mechanisms: (i) demographic shortcut learning, where speaker classification training exploits spurious correlations between sex and speaker identity, and (ii) feature entanglement, where sex-linked acoustic variation overlaps with identity cues and cannot be removed without degrading speaker discrimination. We propose Fair-Gate, a fairness-aware and interpretable risk-gating framework that addresses both mechanisms in a single pipeline. Fair-Gate applies risk extrapolation to reduce variation in speaker-classification risk across proxy sex groups, and introduces a local complementary gat...

---

## 3. Edge-Cloud Collaborative Speech Emotion Captioning via Token-Level Speculative Decoding in Audio-Language Models

**Authors**: Xiangyuan Xue, Jiajun Lu, Yan Gao, Gongping Huang, Ting Dang, Hong Jia  
**Categories**: cs.SD  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11397  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11397v1.pdf

**Abstract**:
> arXiv:2603.11397v1 Announce Type: new 
Abstract: Speech Emotion Captioning (SEC) leverages large audio-language models to generate rich, context-aware affective descriptions from speech. However, real-world deployment remains challenging due to the substantial computational demands on resource-constrained edge devices and the privacy risks of transmitting biometric audio. While smaller audio-language models enable efficient on-device SEC, their limited capacity often weakens subtle paralinguistic modeling and fine-grained affective grounding. We propose an edge-cloud collaborative framework based on Uncertainty-Guided Speculative Decoding (UGSD). A lightweight edge model drafts captions locally, and only high-uncertainty token blocks are selectively escalated to a stronger cloud verifier f...

---

## 4. AnimeScore: A Preference-Based Dataset and Framework for Evaluating Anime-Like Speech Style

**Authors**: Joonyong Park, Jerry Li  
**Categories**: cs.SD  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11482  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11482v1.pdf

**Abstract**:
> arXiv:2603.11482v1 Announce Type: new 
Abstract: Evaluating 'anime-like' voices currently relies on costly subjective judgments, yet no standardized objective metric exists. A key challenge is that anime-likeness, unlike naturalness, lacks a shared absolute scale, making conventional Mean Opinion Score (MOS) protocols unreliable. To address this gap, we propose AnimeScore, a preference-based framework for automatic anime-likeness evaluation via pairwise ranking. We collect 15,000 pairwise judgments from 187 evaluators with free-form descriptions, and acoustic analysis reveals that perceived anime-likeness is driven by controlled resonance shaping, prosodic continuity, and deliberate articulation rather than simple heuristics such as high pitch. We show that handcrafted acoustic features re...

---

## 5. Toward Complex-Valued Neural Networks for Waveform Generation

**Authors**: Hyung-Seok Oh, Deok-Hyeon Cho, Seung-Bin Kim, Seong-Whan Lee  
**Categories**: cs.SD  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11589  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11589v1.pdf

**Abstract**:
> arXiv:2603.11589v1 Announce Type: new 
Abstract: Neural vocoders have recently advanced waveform generation, yielding natural and expressive audio. Among these approaches, iSTFT-based vocoders have recently gained attention. They predict a complex-valued spectrogram and then synthesize the waveform via iSTFT, thereby avoiding learned upsampling stages that can increase computational cost. However, current approaches use real-valued networks that process the real and imaginary parts independently. This separation limits their ability to capture the inherent structure of complex spectrograms. We present ComVo, a Complex-valued neural Vocoder whose generator and discriminator use native complex arithmetic. This enables an adversarial training framework that provides structured feedback in com...

---

## 6. Resonate: Reinforcing Text-to-Audio Generation via Online Feedback from Large Audio Language Models

**Authors**: Xiquan Li, Junxi Liu, Wenxi Chen, Haina Zhu, Ziyang Ma, Xie Chen  
**Categories**: cs.SD  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11661  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11661v1.pdf

**Abstract**:
> arXiv:2603.11661v1 Announce Type: new 
Abstract: Reinforcement Learning (RL) has become an effective paradigm for enhancing Large Language Models (LLMs) and visual generative models. However, its application in text-to-audio (TTA) generation remains largely under-explored. Prior work typically employs offline methods like Direct Preference Optimization (DPO) and leverages Contrastive Language-Audio Pretraining (CLAP) models as reward functions. In this study, we investigate the integration of online Group Relative Policy Optimization (GRPO) into TTA generation. We adapt the algorithm for Flow Matching-based audio models and demonstrate that online RL significantly outperforms its offline counterparts. Furthermore, we incorporate rewards derived from Large Audio Language Models (LALMs), whi...

---

## 7. Resurfacing Paralinguistic Awareness in Large Audio Language Models

**Authors**: Hao Yang, Minghan Wang, Tongtong Wu, Lizhen Qu, Ehsan Shareghi, Gholamreza Haffari  
**Categories**: cs.SD  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11947  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11947v1.pdf

**Abstract**:
> arXiv:2603.11947v1 Announce Type: new 
Abstract: Large Audio Language Models (LALMs) have expanded the interaction with human to speech modality, which introduces great interactive potential, due to the paralinguistic cues implicitly indicating the user context. However, building on the current content-centred paradigm, LALMs usually neglect such paralinguistic cues and respond solely based on query content. In this work, to resurface the paralinguistic awareness in LALMs, we introduce five diverse layer-wise analyses to jointly identify paralinguistic layers and semantic understanding layers. Based on these insights, we propose a paralinguistic-enhanced fine-tuning (PE-FT) protocol accordingly to equip LALMs with paralinguistic-aware capabilities, including (1) selective-layer fine-tuning...

---

## 8. Multimodal Self-Attention Network with Temporal Alignment for Audio-Visual Emotion Recognition

**Authors**: Inyong Koo, yeeun Seong, Minseok Son, Jaehyuk Jang, Changick Kim  
**Categories**: cs.SD  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11095  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11095v1.pdf

**Abstract**:
> arXiv:2603.11095v1 Announce Type: cross 
Abstract: Audio-visual emotion recognition (AVER) methods typically fuse utterance-level features, and even frame-level attention models seldom address the frame-rate mismatch across modalities. In this paper, we propose a Transformer-based framework focusing on the temporal alignment of multimodal features. Our design employs a multimodal self-attention encoder that simultaneously captures intra- and inter-modal dependencies within a shared feature space. To address heterogeneous sampling rates, we incorporate Temporally-aligned Rotary Position Embeddings (TaRoPE), which implicitly synchronize audio and video tokens. Furthermore, we introduce a Cross-Temporal Matching (CTM) loss that enforces consistency among temporally proximate pairs, guiding th...

---

## 9. Can LLMs Help Localize Fake Words in Partially Fake Speech?

**Authors**: Lin Zhang, Thomas Thebaud, Zexin Cai, Sanjeev Khudanpur, Daniel Povey, Leibny Paola Garc\'ia-Perera,...  
**Categories**: cs.SD  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11205  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11205v1.pdf

**Abstract**:
> arXiv:2603.11205v1 Announce Type: cross 
Abstract: Large language models (LLMs), trained on large-scale text, have recently attracted significant attention for their strong performance across many tasks. Motivated by this, we investigate whether a text-trained LLM can help localize fake words in partially fake speech, where only specific words within a speech are edited. We build a speech LLM to perform fake word localization via next token prediction. Experiments and analyses on AV-Deepfake1M and PartialEdit indicates that the model frequently leverages editing-style pattern learned from the training data, particularly word-level polarity substitutions for those two databases we discussed, as cues for localizing fake words. Although such particular patterns provide useful information in a...

---

## 10. Cough activity detection for automatic tuberculosis screening

**Authors**: Joshua Jansen van V\"uren, Devendra Singh Parihar, Daphne Naidoo, Kimsey Zajac, Willy Ssengooba, Gra...  
**Categories**: cs.SD  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11241  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11241v1.pdf

**Abstract**:
> arXiv:2603.11241v1 Announce Type: cross 
Abstract: The automatic identification of cough segments in audio through the determination of start and end points is pivotal to building scalable screening tools in health technologies for pulmonary related diseases. We propose the application of two current pre-trained architectures to the task of cough activity detection. A dataset of recordings containing cough from patients symptomatic for tuberculosis (TB) who self-present at community-level care centres in South Africa and Uganda is employed. When automatic start and end points are determined using XLS-R, an average precision of 0.96 and an area under the receiver-operating characteristic of 0.99 are achieved for the test set. We show that best average precision is achieved by utilising only...

---

## 11. Stage-Adaptive Reliability Modeling for Continuous Valence-Arousal Estimation

**Authors**: Yubeen Lee, Sangeun Lee, Junyeop Cha, Eunil Park  
**Categories**: cs.SD  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11468  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11468v1.pdf

**Abstract**:
> arXiv:2603.11468v1 Announce Type: cross 
Abstract: Continuous valence-arousal estimation in real-world environments is challenging due to inconsistent modality reliability and interaction-dependent variability in audio-visual signals. Existing approaches primarily focus on modeling temporal dynamics, often overlooking the fact that modality reliability can vary substantially across interaction stages. To address this issue, we propose SAGE, a Stage-Adaptive reliability modeling framework that explicitly estimates and calibrates modality-wise confidence during multimodal integration. SAGE introduces a reliability-aware fusion mechanism that dynamically rebalances audio and visual representations according to their stage-dependent informativeness, preventing unreliable signals from dominatin...

---

## 12. OmniForcing: Unleashing Real-time Joint Audio-Visual Generation

**Authors**: Yaofeng Su, Yuming Li, Zeyue Xue, Jie Huang, Siming Fu, Haoran Li, Ying Li, Zezhong Qian, Haoyang Hu...  
**Categories**: cs.SD  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11647  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11647v1.pdf

**Abstract**:
> arXiv:2603.11647v1 Announce Type: cross 
Abstract: Recent joint audio-visual diffusion models achieve remarkable generation quality but suffer from high latency due to their bidirectional attention dependencies, hindering real-time applications. We propose OmniForcing, the first framework to distill an offline, dual-stream bidirectional diffusion model into a high-fidelity streaming autoregressive generator. However, naively applying causal distillation to such dual-stream architectures triggers severe training instability, due to the extreme temporal asymmetry between modalities and the resulting token sparsity. We address the inherent information density gap by introducing an Asymmetric Block-Causal Alignment with a zero-truncation Global Prefix that prevents multi-modal synchronization ...

---

## 13. SEMamba++: A General Speech Restoration Framework Leveraging Global, Local, and Periodic Spectral Patterns

**Authors**: Yongjoon Lee, Jung-Woo Choi  
**Categories**: cs.SD  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11669  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11669v1.pdf

**Abstract**:
> arXiv:2603.11669v1 Announce Type: cross 
Abstract: General speech restoration demands techniques that can interpret complex speech structures under various distortions. While State-Space Models like SEMamba have advanced the state-of-the-art in speech denoising, they are not inherently optimized for critical speech characteristics, such as spectral periodicity or multi-resolution frequency analysis. In this work, we introduce an architecture tailored to incorporate speech-specific features as inductive biases. In particular, we propose Frequency GLP, a frequency feature extraction block that effectively and efficiently leverages the properties of frequency bins. Then, we design a multi-resolution parallel time-frequency dual-processing block to capture diverse spectral patterns, and a lear...

---

## 14. RAF: Relativistic Adversarial Feedback For Universal Speech Synthesis

**Authors**: Yongjoon Lee, Jung-Woo Choi  
**Categories**: cs.SD  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11678  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11678v1.pdf

**Abstract**:
> arXiv:2603.11678v1 Announce Type: cross 
Abstract: We propose Relativistic Adversarial Feedback (RAF), a novel training objective for GAN vocoders that improves in-domain fidelity and generalization to unseen scenarios. Although modern GAN vocoders employ advanced architectures, their training objectives often fail to promote generalizable representations. RAF addresses this problem by leveraging speech self-supervised learning models to assist discriminators in evaluating sample quality, encouraging the generator to learn richer representations. Furthermore, we utilize relativistic pairing for real and fake waveforms to improve the modeling of the training data distribution. Experiments across multiple datasets show consistent gains in both objective and subjective metrics on GAN-based vo...

---

## 15. Affect Decoding in Phonated and Silent Speech Production from Surface EMG

**Authors**: Simon Pistrosch, Kleanthis Avramidis, Tiantian Feng, Jihwan Lee, Monica Gonzalez-Machorro, Shrikanth...  
**Categories**: cs.SD  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11715  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11715v1.pdf

**Abstract**:
> arXiv:2603.11715v1 Announce Type: cross 
Abstract: The expression of affect is integral to spoken communication, yet, its link to underlying articulatory execution remains unclear. Measures of articulatory muscle activity such as EMG could reveal how speech production is modulated by emotion alongside acoustic speech analyses. We investigate affect decoding from facial and neck surface electromyography (sEMG) during phonated and silent speech production. For this purpose, we introduce a dataset comprising 2,780 utterances from 12 participants across 3 tasks, on which we evaluate both intra- and inter-subject decoding using a range of features and model embeddings. Our results reveal that EMG representations reliably discriminate frustration with up to 0.845 AUC, and generalize well across ...

---

## 16. Audio-Language Models for Audio-Centric Tasks: A Systematic Survey

**Authors**: Yi Su, Jisheng Bai, Qisheng Xu, Kele Xu, Yong Dou  
**Categories**: cs.SD  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2501.15177  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2501.15177v2.pdf

**Abstract**:
> arXiv:2501.15177v2 Announce Type: replace 
Abstract: Audio-Language Models (ALMs), trained on paired audio-text data, are designed to process, understand, and reason about audio-centric multimodal content. Unlike traditional supervised approaches that use predefined labels, ALMs leverage natural language supervision to better handle complex real-world audio scenes with multiple overlapping events. While demonstrating impressive zero-shot and task generalization capabilities, there is still a notable lack of systematic surveys that comprehensively organize and analyze developments. In this paper, we present the first systematic review of ALMs with three main contributions: (1) comprehensive coverage of ALM works across speech, music, and sound from a general audio perspective; (2) a unified...

---

## 17. AudioTrust: Benchmarking the Multifaceted Trustworthiness of Audio Large Language Models

**Authors**: Kai Li, Can Shen, Yile Liu, Jirui Han, Kelong Zheng, Xuechao Zou, Lionel Z. Wang, Shun Zhang, Xingji...  
**Categories**: cs.SD  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2505.16211  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2505.16211v4.pdf

**Abstract**:
> arXiv:2505.16211v4 Announce Type: replace 
Abstract: The rapid development and widespread adoption of Audio Large Language Models (ALLMs) demand rigorous evaluation of their trustworthiness. However, existing evaluation frameworks are primarily designed for text and fail to capture vulnerabilities introduced by the acoustic properties of audio. We find that significant trustworthiness risks in ALLMs arise from non-semantic acoustic cues, such as timbre, accent, and background noise, which can be exploited to manipulate model behavior. To address this gap, we propose AudioTrust, the first large-scale and systematic framework for evaluating ALLM trustworthiness under audio-specific risks. AudioTrust covers six key dimensions: fairness, hallucination, safety, privacy, robustness, and authenti...

---

## 18. Towards Robust Speech Deepfake Detection via Human-Inspired Reasoning

**Authors**: Artem Dvirniak, Evgeny Kushnir, Dmitrii Tarasov, Artem Iudin, Oleg Kiriukhin, Mikhail Pautov, Dmitri...  
**Categories**: cs.SD  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10725  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10725v2.pdf

**Abstract**:
> arXiv:2603.10725v2 Announce Type: replace 
Abstract: The modern generative audio models can be used by an adversary in an unlawful manner, specifically, to impersonate other people to gain access to private information. To mitigate this issue, speech deepfake detection (SDD) methods started to evolve. Unfortunately, current SDD methods generally suffer from the lack of generalization to new audio domains and generators. More than that, they lack interpretability, especially human-like reasoning that would naturally explain the attribution of a given audio to the bona fide or spoof class and provide human-perceptible cues. In this paper, we propose HIR-SDD, a novel SDD framework that combines the strengths of Large Audio Language Models (LALMs) with the chain-of-thought reasoning derived fr...

---

## 19. [b]=[d]-[t]+[p]: Self-supervised Speech Models Discover Phonological Vector Arithmetic

**Authors**: Kwanghee Choi, Eunjung Yeo, Cheol Jun Cho, David Harwath, David R. Mortensen  
**Categories**: cs.SD  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.18899  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.18899v2.pdf

**Abstract**:
> arXiv:2602.18899v2 Announce Type: replace-cross 
Abstract: Self-supervised speech models (S3Ms) are known to encode rich phonetic information, yet how this information is structured remains underexplored. We conduct a comprehensive study across 96 languages to analyze the underlying structure of S3M representations, with particular attention to phonological vectors. We first show that there exist linear directions within the model's representation space that correspond to phonological features. We further demonstrate that the scale of these phonological vectors correlate to the degree of acoustic realization of their corresponding phonological features in a continuous manner. For example, the difference between [d] and [t] yields a voicing vector: adding this vector to [p] produces [b], wh...

---

## 20. Self-Speculative Decoding for LLM-based ASR with CTC Encoder Drafts

**Authors**: George Saon, Samuel Thomas, Takashi Fukuda, Tohru Nagano, Avihu Dekel, Luis Lastras  
**Categories**: eess.AS  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11243  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11243v1.pdf

**Abstract**:
> arXiv:2603.11243v1 Announce Type: new 
Abstract: We propose self-speculative decoding for speech-aware LLMs by using the CTC encoder as a draft model to accelerate auto-regressive (AR) inference and improve ASR accuracy. Our three-step procedure works as follows: (1) if the frame entropies of the CTC output distributions are below a threshold, the greedy CTC hypothesis is accepted as final; (2) otherwise, the CTC hypothesis is verified in a single LLM forward pass using a relaxed acceptance criterion based on token likelihoods; (3) if verification fails, AR decoding resumes from the accepted CTC prefix. Experiments on nine corpora and five languages show that this approach can simultaneously accelerate decoding and reduce WER. On the HuggingFace Open ASR benchmark with a 1B parameter LLM a...

---

## 21. ReDimNet2: Scaling Speaker Verification via Time-Pooled Dimension Reshaping

**Authors**: Ivan Yakovlev, Anton Okhotnikov  
**Categories**: eess.AS  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11841  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11841v1.pdf

**Abstract**:
> arXiv:2603.11841v1 Announce Type: new 
Abstract: We present ReDimNet2, an improved neural network architecture for extracting utterance-level speaker representations that builds upon the ReDimNet dimension-reshaping framework. The key modification in ReDimNet2 is the introduction of pooling over the time dimension within the 1D processing pathway. This operation preserves the nature of the 1D feature space, since 1D features remain a reshaped version of 2D features regardless of temporal resolution, while enabling significantly more aggressive scaling of the channel dimension without proportional compute increase. We introduce a family of seven model configurations (B0-B6) ranging from 1.1M to 12.3M parameters and 0.33 to 13 GMACS. Experimental results on VoxCeleb1 benchmarks demonstrate t...

---

## 22. Acoustic-to-Articulatory Inversion of Clean Speech Using an MRI-Trained Model

**Authors**: Sofiane Azzouz, Pierre-Andr\'e Vuissoz, Yves Laprie  
**Categories**: eess.AS  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11845  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11845v1.pdf

**Abstract**:
> arXiv:2603.11845v1 Announce Type: new 
Abstract: Articulatory acoustic inversion reconstructs vocal tract shapes from speech. Real-time magnetic resonance imaging (rt-MRI) allows simultaneous acquisition of both the acoustic speech signal and articulatory information. Besides the complexity of rt-MRI acquisition, the recorded audio is heavily corrupted by scanner noise and requires denoising to be usable. For practical use, it must be possible to invert speech recorded without MRI noise. In this study, we investigate the use of speech recorded in a clean acoustic environment as an alternative to denoised MRI speech. To this end we compare two signals from the same speaker with identical sentences which are aligned using phonetic segmentation. A model trained on denoised MRI speech is evalu...

---

## 23. Reconstruction of the Vocal Tract from Speech via Phonetic Representations Using MRI Data

**Authors**: Sofiane Azzouz, Pierre-Andr\'e Vuissoz, Yves Laprie  
**Categories**: eess.AS  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11847  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11847v1.pdf

**Abstract**:
> arXiv:2603.11847v1 Announce Type: new 
Abstract: Articulatory acoustic inversion aims to reconstruct the complete geometry of the vocal tract from the speech signal. In this paper, we present a comparative study of several levels of phonetic segmentation accuracy, together with a comparison to the baseline introduced in our previous work, which is based on Mel-Frequency Cepstral Coefficients (MFCCs). All the approaches considered are based on a denoised speech signal and aim to investigate the impact of incorporating phonetic information through three successive levels: an uncorrected automatic transcription, a temporally aligned phonetic segmentation, and an expert manual correction following alignment. The models are trained to predict articulatory contours extracted from vocal tract MRI...

---

## 24. Silent Speech Interfaces in the Era of Large Language Models: A Comprehensive Taxonomy and Systematic Review

**Authors**: Kele Xu, Yifan Wang, Ming Feng, Qisheng Xu, Wuyang Chen, Yutao Dou, Cheng Yang, Huaimin Wang  
**Categories**: eess.AS  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11877  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11877v1.pdf

**Abstract**:
> arXiv:2603.11877v1 Announce Type: new 
Abstract: Human-computer interaction has traditionally relied on the acoustic channel, a dependency that introduces systemic vulnerabilities to environmental noise, privacy constraints, and physiological speech impairments. Silent Speech Interfaces (SSIs) emerge as a transformative paradigm that bypasses the acoustic stage by decoding linguistic intent directly from the neuro-muscular-articulatory continuum. This review provides a high-level synthesis of the SSI landscape, transitioning from traditional transducer-centric analysis to a holistic intent-to-execution taxonomy. We systematically evaluate sensing modalities across four critical physiological interception points: neural oscillations, neuromuscular activation, articulatory kinematics (ultras...

---

## 25. Fingerprinting Concepts in Data Streams with Supervised and Unsupervised Meta-Information

**Authors**: Ben Halstead, Yun Sing Koh, Patricia Riddle, Mykola Pechenizkiy, Albert Bifet, Russel Pears  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11094  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11094v1.pdf

**Abstract**:
> arXiv:2603.11094v1 Announce Type: new 
Abstract: Streaming sources of data are becoming more common as the ability to collect data in real-time grows. A major concern in dealing with data streams is concept drift, a change in the distribution of data over time, for example, due to changes in environmental conditions. Representing concepts (stationary periods featuring similar behaviour) is a key idea in adapting to concept drift. By testing the similarity of a concept representation to a window of observations, we can detect concept drift to a new or previously seen recurring concept. Concept representations are constructed using meta-information features, values describing aspects of concept behaviour. We find that previously proposed concept representations rely on small numbers of meta-...

---

## 26. Graph Tokenization for Bridging Graphs and Transformers

**Authors**: Zeyuan Guo, Enmao Diao, Cheng Yang, Chuan Shi  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11099  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11099v1.pdf

**Abstract**:
> arXiv:2603.11099v1 Announce Type: new 
Abstract: The success of large pretrained Transformers is closely tied to tokenizers, which convert raw input into discrete symbols. Extending these models to graph-structured data remains a significant challenge. In this work, we introduce a graph tokenization framework that generates sequential representations of graphs by combining reversible graph serialization, which preserves graph information, with Byte Pair Encoding (BPE), a widely adopted tokenizer in large language models (LLMs). To better capture structural information, the graph serialization process is guided by global statistics of graph substructures, ensuring that frequently occurring substructures appear more often in the sequence and can be merged by BPE into meaningful tokens. Empir...

---

## 27. Task-Conditioned Routing Signatures in Sparse Mixture-of-Experts Transformers

**Authors**: Mynampati Sri Ranganadha Avinash  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11114  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11114v1.pdf

**Abstract**:
> arXiv:2603.11114v1 Announce Type: new 
Abstract: Sparse Mixture-of-Experts (MoE) architectures enable efficient scaling of large language models through conditional computation, yet the routing mechanisms responsible for expert selection remain poorly understood. In this work, we introduce routing signatures, a vector representation summarizing expert activation patterns across layers for a given prompt, and use them to study whether MoE routing exhibits task-conditioned structure. Using OLMoE-1B-7B-0125-Instruct as an empirical testbed, we show that prompts from the same task category induce highly similar routing signatures, while prompts from different categories exhibit substantially lower similarity. Within-category routing similarity (0.8435 +/- 0.0879) significantly exceeds across-c...

---

## 28. Learning Tree-Based Models with Gradient Descent

**Authors**: Sascha Marton  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11117  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11117v1.pdf

**Abstract**:
> arXiv:2603.11117v1 Announce Type: new 
Abstract: Tree-based models are widely recognized for their interpretability and have proven effective in various application domains, particularly in high-stakes domains. However, learning decision trees (DTs) poses a significant challenge due to their combinatorial complexity and discrete, non-differentiable nature. As a result, traditional methods such as CART, which rely on greedy search procedures, remain the most widely used approaches. These methods make locally optimal decisions at each node, constraining the search space and often leading to suboptimal tree structures. Additionally, their demand for custom training methods precludes a seamless integration into modern machine learning (ML) approaches.
  In this thesis, we propose a novel metho...

---

## 29. A Learning-Based Superposition Operator for Non-Renewal Arrival Processes in Queueing Networks

**Authors**: Eliran Sherzer  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11118  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11118v1.pdf

**Abstract**:
> arXiv:2603.11118v1 Announce Type: new 
Abstract: The superposition of arrival processes is a fundamental yet analytically intractable operation in queueing networks when inputs are general non-renewal streams. Classical methods either reduce merged flows to renewal surrogates, rely on computationally prohibitive Markovian representations, or focus solely on mean-value performance measures.
  We propose a scalable data-driven superposition operator that maps low-order moments and autocorrelation descriptors of multiple arrival streams to those of their merged process. The operator is a deep learning model trained on synthetically generated Markovian Arrival Processes (MAPs), for which exact superposition is available, and learns a compact representation that accurately reconstructs the firs...

---

## 30. Higher-Order Modular Attention: Fusing Pairwise and Triadic Interactions for Protein Sequences

**Authors**: Shirin Amiraslani, Xin Gao  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11133  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11133v1.pdf

**Abstract**:
> arXiv:2603.11133v1 Announce Type: new 
Abstract: Transformer self-attention computes pairwise token interactions, yet protein sequence to phenotype relationships often involve cooperative dependencies among three or more residues that dot product attention does not capture explicitly. We introduce Higher-Order Modular Attention, HOMA, a unified attention operator that fuses pairwise attention with an explicit triadic interaction pathway. To make triadic attention practical on long sequences, HOMA employs block-structured, windowed triadic attention. We evaluate on three TAPE benchmarks for Secondary Structure, Fluorescence, and Stability. Our attention mechanism yields consistent improvements across all tasks compared with standard self-attention and efficient variants including block-wise...

---

## 31. Attention Gathers, MLPs Compose: A Causal Analysis of an Action-Outcome Circuit in VideoViT

**Authors**: Sai V R Chereddy  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11142  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11142v1.pdf

**Abstract**:
> arXiv:2603.11142v1 Announce Type: new 
Abstract: The paper explores how video models trained for classification tasks represent nuanced, hidden semantic information that may not affect the final outcome, a key challenge for Trustworthy AI models. Through Explainable and Interpretable AI methods, specifically mechanistic interpretability techniques, the internal circuit responsible for representing the action's outcome is reverse-engineered in a pre-trained video vision transformer, revealing that the "Success vs Failure" signal is computed through a distinct amplification cascade. While there are low-level differences observed from layer 0, the abstract and semantic representation of the outcome is progressively amplified from layers 5 through 11. Causal analysis, primarily using activatio...

---

## 32. Representation Finetuning for Continual Learning

**Authors**: Haihua Luo, Xuming Ran, Tommi K\"arkk\"ainen, Huiyan Xue, Zhonghua Chen, Qi Xu, Fengyu Cong  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11201  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11201v1.pdf

**Abstract**:
> arXiv:2603.11201v1 Announce Type: new 
Abstract: The world is inherently dynamic, and continual learning aims to enable models to adapt to ever-evolving data streams. While pre-trained models have shown powerful performance in continual learning, they still require finetuning to adapt effectively to downstream tasks. However, prevailing Parameter-Efficient Fine-Tuning (PEFT) methods operate through empirical, black-box optimization at the weight level. These approaches lack explicit control over representation drift, leading to sensitivity to domain shifts and catastrophic forgetting in continual learning scenarios. In this work, we introduce Continual Representation Learning (CoRe), a novel framework that for the first time shifts the finetuning paradigm from weight space to representatio...

---

## 33. Single molecule localization microscopy challenge: a biologically inspired benchmark for long-sequence modeling

**Authors**: Fatemeh Valeh, Monika Farsang, Radu Grosu, Gerhard Sch\"utz  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11296  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11296v1.pdf

**Abstract**:
> arXiv:2603.11296v1 Announce Type: new 
Abstract: State space models (SSMs) have recently achieved strong performance on long sequence modeling tasks while offering improved memory and computational efficiency compared to transformer based architectures. However, their evaluation has been largely limited to synthetic benchmarks and application domains such as language and audio, leaving their behavior on sparse and stochastic temporal processes in biological imaging unexplored. In this work, we introduce the Single Molecule Localization Microscopy Challenge (SMLM-C), a benchmark dataset consisting of ten SMLM simulations spanning dSTORM and DNA-PAINT modalities with varying hyperparameter designed to evaluate state space models on biologically realistic spatiotemporal point process data wit...

---

## 34. UniHetCO: A Unified Heterogeneous Representation for Multi-Problem Learning in Unsupervised Neural Combinatorial Optimization

**Authors**: Kien X. Nguyen, Ilya Safro  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11456  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11456v1.pdf

**Abstract**:
> arXiv:2603.11456v1 Announce Type: new 
Abstract: Unsupervised neural combinatorial optimization (NCO) offers an appealing alternative to supervised approaches by training learning-based solvers without ground-truth solutions, directly minimizing instance objectives and constraint violations. Yet for graph node subset-selection problems (e.g., Maximum Clique and Maximum Independent Set), existing unsupervised methods are typically specialized to a single problem class and rely on problem-specific surrogate losses, which hinders learning across classes within a unified framework. In this work, we propose UniHetCO, a unified heterogeneous graph representation for constrained quadratic programming-based combinatorial optimization that encodes problem structure, objective terms, and linear cons...

---

## 35. Bridging Discrete Marks and Continuous Dynamics: Dual-Path Cross-Interaction for Marked Temporal Point Processes

**Authors**: Yuxiang Liu, Qiao Liu, Tong Luo, Yanglei Gan, Peng He, Yao LIu  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11462  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11462v1.pdf

**Abstract**:
> arXiv:2603.11462v1 Announce Type: new 
Abstract: Predicting irregularly spaced event sequences with discrete marks poses significant challenges due to the complex, asynchronous dependencies embedded within continuous-time data streams.Existing sequential approaches capture dependencies among event tokens but ignore the continuous evolution between events, while Neural Ordinary Differential Equation (Neural ODE) methods model smooth dynamics yet fail to account for how event types influence future timing.To overcome these limitations, we propose NEXTPP, a dual-channel framework that unifies discrete and continuous representations via Event-granular Neural Evolution with Cross-Interaction for Marked Temporal Point Processes. Specifically, NEXTPP encodes discrete event marks via a self-attent...

---

## 36. Grammar of the Wave: Towards Explainable Multivariate Time Series Event Detection via Neuro-Symbolic VLM Agents

**Authors**: Sky Chenwei Wan, Tianjun Hou, Yifei Wang, Xiqing Chang, Aymeric Jan  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11479  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11479v1.pdf

**Abstract**:
> arXiv:2603.11479v1 Announce Type: new 
Abstract: Time Series Event Detection (TSED) has long been an important task with critical applications across many high-stakes domains. Unlike statistical anomalies, events are defined by semantics with complex internal structures, which are difficult to learn inductively from scarce labeled data in real-world settings. In light of this, we introduce Knowledge-Guided TSED, a new setting where a model is given a natural-language event description and must ground it to intervals in multivariate signals with little or no training data. To tackle this challenge, we introduce Event Logic Tree (ELT), a novel knowledge representation framework to bridge linguistic descriptions and physical time series data via modeling the intrinsic temporal-logic structure...

---

## 37. Attention Sinks Are Provably Necessary in Softmax Transformers: Evidence from Trigger-Conditional Tasks

**Authors**: Yuval Ran-Milo  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11487  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11487v1.pdf

**Abstract**:
> arXiv:2603.11487v1 Announce Type: new 
Abstract: Transformers often display an attention sink: probability mass concentrates on a fixed, content-agnostic position. We prove that computing a simple trigger-conditional behavior necessarily induces a sink in softmax self-attention models. Our results formalize a familiar intuition: normalization over a probability simplex must force attention to collapse onto a stable anchor to realize a default state (e.g., when the model needs to ignore the input). We instantiate this with a concrete task: when a designated trigger token appears, the model must return the average of all preceding token representations, and otherwise output zero, a task which mirrors the functionality of attention heads in the wild (Barbero et al., 2025; Guo et al., 2024). W...

---

## 38. KEPo: Knowledge Evolution Poison on Graph-based Retrieval-Augmented Generation

**Authors**: Qizhi Chen, Chao Qi, Yihong Huang, Muquan Li, Rongzheng Wang, Dongyang Zhang, Ke Qin, Shuang Liang  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11501  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11501v1.pdf

**Abstract**:
> arXiv:2603.11501v1 Announce Type: new 
Abstract: Graph-based Retrieval-Augmented Generation (GraphRAG) constructs the Knowledge Graph (KG) from external databases to enhance the timeliness and accuracy of Large Language Model (LLM) generations.However,this reliance on external data introduces new attack surfaces.Attackers can inject poisoned texts into databases to manipulate LLMs into producing harmful target responses for attacker-chosen queries.Existing research primarily focuses on attacking conventional RAG systems.However,such methods are ineffective against GraphRAG.This robustness derives from the KG abstraction of GraphRAG,which reorganizes injected text into a graph before retrieval,thereby enabling the LLM to reason based on the restructured context instead of raw poisoned passa...

---

## 39. CFD-HAR: User-controllable Privacy through Conditional Feature Disentanglement

**Authors**: Alex Gn, Fan Li, S Kuniyilh, Ada Axan  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11526  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11526v1.pdf

**Abstract**:
> arXiv:2603.11526v1 Announce Type: new 
Abstract: Modern wearable and mobile devices are equipped with inertial measurement units (IMUs). Human Activity Recognition (HAR) applications running on such devices use machine-learning-based, data-driven techniques that leverage such sensor data. However, sensor-data-driven HAR deployments face two critical challenges: protecting sensitive user information embedded in sensor data in accordance with users' privacy preferences and maintaining high recognition performance with limited labeled samples. This paper proposes a technique for user-controllable privacy through feature disentanglement-based representation learning at the granular level for dynamic privacy filtering. We also compare the efficacy of our technique against few-shot HAR using aut...

---

## 40. CAETC: Causal Autoencoding and Treatment Conditioning for Counterfactual Estimation over Time

**Authors**: Nghia D. Nguyen, Pablo Robles-Granda, Lav R. Varshney  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11565  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11565v1.pdf

**Abstract**:
> arXiv:2603.11565v1 Announce Type: new 
Abstract: Counterfactual estimation over time is important in various applications, such as personalized medicine. However, time-dependent confounding bias in observational data still poses a significant challenge in achieving accurate and efficient estimation. We introduce causal autoencoding and treatment conditioning (CAETC), a novel method for this problem. Built on adversarial representation learning, our method leverages an autoencoding architecture to learn a partially invertible and treatment-invariant representation, where the outcome prediction task is cast as applying a treatment-specific conditioning on the representation. Our design is independent of the underlying sequence model and can be applied to existing architectures such as long s...

---

## 41. Personalized Federated Learning via Gaussian Generative Modeling

**Authors**: Peng Hu, Jianwei Ma  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11620  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11620v1.pdf

**Abstract**:
> arXiv:2603.11620v1 Announce Type: new 
Abstract: Federated learning has emerged as a paradigm to train models collaboratively on inherently distributed client data while safeguarding privacy. In this context, personalized federated learning tackles the challenge of data heterogeneity by equipping each client with a dedicated model. A prevalent strategy decouples the model into a shared feature extractor and a personalized classifier head, where the latter actively guides the representation learning. However, previous works have focused on classifier head-guided personalization, neglecting the potential personalized characteristics in the representation distribution. Building on this insight, we propose pFedGM, a method based on Gaussian generative modeling. The approach begins by training ...

---

## 42. Context-dependent manifold learning: A neuromodulated constrained autoencoder approach

**Authors**: J\'er\^ome Adriaens (Neuroengineering Lab, Department of Electrical Engineering and Computer Science...  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11673  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11673v1.pdf

**Abstract**:
> arXiv:2603.11673v1 Announce Type: new 
Abstract: Constrained autoencoders (cAE) provide a successful path towards interpretable dimensionality reduction by enforcing geometric structure on latent spaces. However, standard cAEs cannot adapt to varying physical parameters or environmental conditions without conflating these contextual shifts with the primary input. To address this, we integrated a neuromodulatory mechanism into the cAE framework to allow for context-dependent manifold learning. This paper introduces the Neuromodulated Constrained Autoencoder (NcAE), which adaptively parameterizes geometric constraints via gain and bias tuning conditioned on static contextual information. Experimental results on dynamical systems show that the NcAE accurately captures how manifold geometry va...

---

## 43. Disentangled Representation Learning through Unsupervised Symmetry Group Discovery

**Authors**: Dang-Nhu Barth\'el\'emy, Annabi Louis, Argentieri Sylvain  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11790  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11790v1.pdf

**Abstract**:
> arXiv:2603.11790v1 Announce Type: new 
Abstract: Symmetry-based disentangled representation learning leverages the group structure of environment transformations to uncover the latent factors of variation. Prior approaches to symmetry-based disentanglement have required strong prior knowledge of the symmetry group's structure, or restrictive assumptions about the subgroup properties. In this work, we remove these constraints by proposing a method whereby an embodied agent autonomously discovers the group structure of its action space through unsupervised interaction with the environment. We prove the identifiability of the true symmetry group decomposition under minimal assumptions, and derive two algorithms: one for discovering the group decomposition from interaction data, and another fo...

---

## 44. Multi-Station WiFi CSI Sensing Framework Robust to Station-wise Feature Missingness and Limited Labeled Data

**Authors**: Keita Kayano, Takayuki Nishio, Daiki Yoda, Yuta Hirai, Tomoko Adachi  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11858  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11858v1.pdf

**Abstract**:
> arXiv:2603.11858v1 Announce Type: new 
Abstract: We propose a WiFi Channel State Information (CSI) sensing framework for multi-station deployments that addresses two fundamental challenges in practical CSI sensing: station-wise feature missingness and limited labeled data. Feature missingness is commonly handled by resampling unevenly spaced CSI measurements or by reconstructing missing samples, while label scarcity is mitigated by data augmentation or self-supervised representation learning. However, these techniques are typically developed in isolation and do not jointly address long-term, structured station unavailability together with label scarcity. To bridge this gap, we explicitly incorporate station unavailability into both representation learning and downstream model training. Spe...

---

## 45. Causal Representation Learning with Optimal Compression under Complex Treatments

**Authors**: Wanting Liang, Haoang Chi, Zhiheng Zhang  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11907  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11907v1.pdf

**Abstract**:
> arXiv:2603.11907v1 Announce Type: new 
Abstract: Estimating Individual Treatment Effects (ITE) in multi-treatment scenarios faces two critical challenges: the Hyperparameter Selection Dilemma for balancing weights and the Curse of Dimensionality in computational scalability. This paper derives a novel multi-treatment generalization bound and proposes a theoretical estimator for the optimal balancing weight $\alpha$, eliminating expensive heuristic tuning. We investigate three balancing strategies: Pairwise, One-vs-All (OVA), and Treatment Aggregation. While OVA achieves superior precision in low-dimensional settings, our proposed Treatment Aggregation ensures both accuracy and O(1) scalability as the treatment space expands. Furthermore, we extend our framework to a generative architecture...

---

## 46. EnTransformer: A Deep Generative Transformer for Multivariate Probabilistic Forecasting

**Authors**: Rajdeep Pathak, Rahul Goswami, Madhurima Panja, Palash Ghosh, Tanujit Chakraborty  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11909  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11909v1.pdf

**Abstract**:
> arXiv:2603.11909v1 Announce Type: new 
Abstract: Reliable uncertainty quantification is critical in multivariate time series forecasting problems arising in domains such as energy systems and transportation networks, among many others. Although Transformer-based architectures have recently achieved strong performance for sequence modeling, most probabilistic forecasting approaches rely on restrictive parametric likelihoods or quantile-based objectives. They can struggle to capture complex joint predictive distributions across multiple correlated time series. This work proposes EnTransformer, a deep generative forecasting framework that integrates engression, a stochastic learning paradigm for modeling conditional distributions, with the expressive sequence modeling capabilities of Transfor...

---

## 47. Chem4DLLM: 4D Multimodal LLMs for Chemical Dynamics Understanding

**Authors**: Xinyu Li, Zhen Zhang, Qi Chen, Anton van den Hengel, Lina Yao, Javen Qinfeng Shi  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11924  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11924v1.pdf

**Abstract**:
> arXiv:2603.11924v1 Announce Type: new 
Abstract: Existing chemical understanding tasks primarily rely on static molecular representations, limiting their ability to model inherently dynamic phenomena such as bond breaking or conformational changes, which are essential for a chemist to understand chemical reactions. To address this gap, we introduce Chemical Dynamics Understanding (ChemDU), a new task that translates 4D molecular trajectories into interpretable natural-language explanations. ChemDU focuses on fundamental dynamic scenarios, including gas-phase and catalytic reactions, and requires models to reason about key events along molecular trajectories, such as bond formation and dissociation, and to generate coherent, mechanistically grounded narratives. To benchmark this capability,...

---

## 48. Effective Resistance Rewiring: A Simple Topological Correction for Over-Squashing

**Authors**: Bertran Miquel-Oliver, Manel Gil-Sorribes, Victor Guallar, Alexis Molina  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11944  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11944v1.pdf

**Abstract**:
> arXiv:2603.11944v1 Announce Type: new 
Abstract: Graph Neural Networks struggle to capture long-range dependencies due to over-squashing, where information from exponentially growing neighborhoods must pass through a small number of structural bottlenecks. While recent rewiring methods attempt to alleviate this limitation, many rely on local criteria such as curvature, which can overlook global connectivity constraints that restrict information flow. We introduce Effective Resistance Rewiring (ERR), a simple topology correction strategy that uses effective resistance as a global signal to detect structural bottlenecks. ERR iteratively adds edges between node pairs with the largest resistance while removing edges with minimal resistance, strengthening weak communication pathways while contr...

---

## 49. Statistical and structural identifiability in representation learning

**Authors**: Walter Nelson, Marco Fumero, Theofanis Karaletsos, Francesco Locatello  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11970  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11970v1.pdf

**Abstract**:
> arXiv:2603.11970v1 Announce Type: new 
Abstract: Representation learning models exhibit a surprising stability in their internal representations. Whereas most prior work treats this stability as a single property, we formalize it as two distinct concepts: statistical identifiability (consistency of representations across runs) and structural identifiability (alignment of representations with some unobserved ground truth). Recognizing that perfect pointwise identifiability is generally unrealistic for modern representation learning models, we propose new model-agnostic definitions of statistical and structural near-identifiability of representations up to some error tolerance $\epsilon$. Leveraging these definitions, we prove a statistical $\epsilon$-near-identifiability result for the repr...

---

## 50. Cornserve: A Distributed Serving System for Any-to-Any Multimodal Models

**Authors**: Jae-Won Chung, Jeff J. Ma, Jisang Ahn, Yizhuo Liang, Akshay Jajoo, Myungjin Lee, Mosharaf Chowdhury  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12118  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12118v1.pdf

**Abstract**:
> arXiv:2603.12118v1 Announce Type: new 
Abstract: Any-to-Any models are an emerging class of multimodal models that accept combinations of multimodal data (e.g., text, image, video, audio) as input and generate them as output. Serving these models are challenging; different requests with different input and output modalities traverse different paths through the model computation graph, and each component of the model have different scaling characteristics.
  We present Cornserve, a distributed serving system for generic Any-to-Any models. Cornserve provides a flexible task abstraction for expressing Any-to-Any model computation graphs, enabling component disaggregation and independent scaling. The distributed runtime dispatches compute to the data plane via an efficient record-and-replay ex...

---

## 51. Temporal Straightening for Latent Planning

**Authors**: Ying Wang, Oumayma Bounou, Gaoyue Zhou, Randall Balestriero, Tim G. J. Rudner, Yann LeCun, Mengye Re...  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12231  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12231v1.pdf

**Abstract**:
> arXiv:2603.12231v1 Announce Type: new 
Abstract: Learning good representations is essential for latent planning with world models. While pretrained visual encoders produce strong semantic visual features, they are not tailored to planning and contain information irrelevant -- or even detrimental -- to planning. Inspired by the perceptual straightening hypothesis in human visual processing, we introduce temporal straightening to improve representation learning for latent planning. Using a curvature regularizer that encourages locally straightened latent trajectories, we jointly learn an encoder and a predictor. We show that reducing curvature this way makes the Euclidean distance in latent space a better proxy for the geodesic distance and improves the conditioning of the planning objective...

---

## 52. STAMP: Selective Task-Aware Mechanism for Text Privacy

**Authors**: Fengwei Tian, Payel Bhattacharjee, Heidi Hanson, Geoffrey D. Rubin, Joseph Y. Lo, Ravi Tandon  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12237  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12237v1.pdf

**Abstract**:
> arXiv:2603.12237v1 Announce Type: new 
Abstract: We present STAMP (Selective Task-Aware Mechanism for Text Privacy), a new framework for task-aware text privatization that achieves an improved privacy-utility trade-off. STAMP selectively allocates privacy budgets across tokens by jointly considering (i) each token's importance to the downstream task (as measured via a task- or query-specific representation), and (ii) its privacy sensitivity (e.g., names, dates, identifiers). This token-level partitioning enables fine-grained, group-wise control over the level of noise applied to different parts of the input, balancing privacy protection with task relevance. To privatize individual token embeddings, we introduce the polar mechanism, which perturbs only the direction of embeddings on the uni...

---

## 53. Separable neural architectures as a primitive for unified predictive and generative intelligence

**Authors**: Reza T. Batley, Apurba Sarker, Rajib Mostakim, Andrew Klichine, Sourav Saha  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12244  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12244v1.pdf

**Abstract**:
> arXiv:2603.12244v1 Announce Type: new 
Abstract: Intelligent systems across physics, language and perception often exhibit factorisable structure, yet are typically modelled by monolithic neural architectures that do not explicitly exploit this structure. The separable neural architecture (SNA) addresses this by formalising a representational class that unifies additive, quadratic and tensor-decomposed neural models. By constraining interaction order and tensor rank, SNAs impose a structural inductive bias that factorises high-dimensional mappings into low-arity components. Separability need not be a property of the system itself: it often emerges in the coordinates or representations through which the system is expressed. Crucially, this coordinate-aware formulation reveals a structural a...

---

## 54. The Latent Color Subspace: Emergent Order in High-Dimensional Chaos

**Authors**: Mateusz Pach, Jessica Bader, Quentin Bouniot, Serge Belongie, Zeynep Akata  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12261  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12261v1.pdf

**Abstract**:
> arXiv:2603.12261v1 Announce Type: new 
Abstract: Text-to-image generation models have advanced rapidly, yet achieving fine-grained control over generated images remains difficult, largely due to limited understanding of how semantic information is encoded. We develop an interpretation of the color representation in the Variational Autoencoder latent space of FLUX.1 [Dev], revealing a structure reflecting Hue, Saturation, and Lightness. We verify our Latent Color Subspace (LCS) interpretation by demonstrating that it can both predict and explicitly control color, introducing a fully training-free method in FLUX based solely on closed-form latent-space manipulation. Code is available at https://github.com/ExplainableML/LCS.

---

## 55. Co-Diffusion: An Affinity-Aware Two-Stage Latent Diffusion Framework for Generalizable Drug-Target Affinity Prediction

**Authors**: Yining Qian, Pengjie Wang, Yixiao Li, An-Yang Lu, Cheng Tan, Shuang Li, Lijun Liu  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11125  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11125v1.pdf

**Abstract**:
> arXiv:2603.11125v1 Announce Type: cross 
Abstract: Predicting drug-target affinity is fundamental to virtual screening and lead optimization. However, existing deep models often suffer from representation collapse in stringent cold-start regimes, where the scarcity of labels and domain shifts prevent the learning of transferable pharmacophores and binding motifs. In this paper, we propose Co-Diffusion, a novel affinity-aware framework that redefines DTA prediction as a constrained latent denoising process to enhance generalization. Co-Diffusion employs a two-stage paradigm: Stage I establishes an affinity-steered latent manifold by aligning drug and target embeddings under an explicit supervised objective, ensuring that the latent space reflects the intrinsic binding landscape. Stage II in...

---

## 56. Efficient Approximation to Analytic and $L^p$ functions by Height-Augmented ReLU Networks

**Authors**: ZeYu Li, FengLei Fan, TieYong Zeng  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11128  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11128v1.pdf

**Abstract**:
> arXiv:2603.11128v1 Announce Type: cross 
Abstract: This work addresses two fundamental limitations in neural network approximation theory. We demonstrate that a three-dimensional network architecture enables a significantly more efficient representation of sawtooth functions, which serves as the cornerstone in the approximation of analytic and $L^p$ functions. First, we establish substantially improved exponential approximation rates for several important classes of analytic functions and offer a parameter-efficient network design. Second, for the first time, we derive a quantitative and non-asymptotic approximation of high orders for general $L^p$ functions. Our techniques advance the theoretical understanding of the neural network approximation in fundamental function spaces and offer a ...

---

## 57. Catalogue Grounded Multimodal Attribution for Museum Video under Resource and Regulatory Constraints

**Authors**: Minsak Nanang, Adrian Hilton, Armin Mustafa  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11147  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11147v1.pdf

**Abstract**:
> arXiv:2603.11147v1 Announce Type: cross 
Abstract: Audiovisual (AV) archives in museums and galleries are growing rapidly, but much of this material remains effectively locked away because it lacks consistent, searchable metadata. Existing method for archiving requires extensive manual effort. We address this by automating the most labour intensive part of the workflow: catalogue style metadata curation for in gallery video, grounded in an existing collection database. Concretely, we propose catalogue-grounded multimodal attribution for museum AV content using an open, locally deployable video language model. We design a multi pass pipeline that (i) summarises artworks in a video, (ii) generates catalogue style descriptions and genre labels, and (iii) attempts to attribute title and artist...

---

## 58. Learning to Unscramble: Simplifying Symbolic Expressions via Self-Supervised Oracle Trajectories

**Authors**: David Shih  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11164  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11164v1.pdf

**Abstract**:
> arXiv:2603.11164v1 Announce Type: cross 
Abstract: We present a new self-supervised machine learning approach for symbolic simplification of complex mathematical expressions. Training data is generated by scrambling simple expressions and recording the inverse operations, creating oracle trajectories that provide both goal states and explicit paths to reach them. A permutation-equivariant, transformer-based policy network is then trained on this data step-wise to predict the oracle action given the input expression. We demonstrate this approach on two problems in high-energy physics: dilogarithm reduction and spinor-helicity scattering amplitude simplification. In both cases, our trained policy network achieves near perfect solve rates across a wide range of difficulty levels, substantiall...

---

## 59. DNS-GT: A Graph-based Transformer Approach to Learn Embeddings of Domain Names from DNS Queries

**Authors**: Massimiliano Altieri, Ronan Hamon, Roberto Corizzo, Michelangelo Ceci, Ignacio Sanchez  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11200  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11200v1.pdf

**Abstract**:
> arXiv:2603.11200v1 Announce Type: cross 
Abstract: Network intrusion detection systems play a crucial role in the security strategy employed by organisations to detect and prevent cyberattacks. Such systems usually combine pattern detection signatures with anomaly detection techniques powered by machine learning methods. However, the commonly proposed machine learning methods present drawbacks such as over-reliance on labeled data and limited generalization capabilities. To address these issues, embedding-based methods have been introduced to learn representations from network data, such as DNS traffic, mainly due to its large availability, that generalise effectively to many downstream tasks. However, current approaches do not properly consider contextual information among DNS queries. In...

---

## 60. Security-by-Design for LLM-Based Code Generation: Leveraging Internal Representations for Concept-Driven Steering Mechanisms

**Authors**: Maximilian Wendlinger, Daniel Kowatsch, Konstantin B\"ottinger, Philip Sperl  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11212  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11212v1.pdf

**Abstract**:
> arXiv:2603.11212v1 Announce Type: cross 
Abstract: Large Language Models (LLMs) show remarkable capabilities in understanding natural language and generating complex code. However, as practitioners adopt CodeLLMs for increasingly critical development tasks, research reveals that these models frequently generate functionally correct yet insecure code, posing significant security risks. While multiple approaches have been proposed to improve security in AI-based code generation, combined benchmarks show these methods remain insufficient for practical use, achieving only limited improvements in both functional correctness and security. This stems from a fundamental gap in understanding the internal mechanisms of code generation and the root causes of security vulnerabilities, forcing research...

---

## 61. A Unified Latent Space Disentanglement VAE Framework with Robust Disentanglement Effectiveness Evaluation

**Authors**: Xiaoan Lang, Fang Liu  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11242  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11242v1.pdf

**Abstract**:
> arXiv:2603.11242v1 Announce Type: cross 
Abstract: Evaluating and interpreting latent representations, such as variational autoencoders (VAEs), remains a significant challenge for diverse data types, especially when ground-truth generative factors are unknown. To address this, we propose a general framework -- bfVAE -- that unifies several state-of-the-art disentangled VAE approaches and generates effective latent space disentanglement, especially for tabular data. To assess the effectiveness of a VAE disentanglement technique, we propose two procedures - Feature Variance Heterogeneity via Latent Traversal (FVH-LT) and Dirty Block Sparse Regression in Latent Space (DBSR-LS) for disentanglement assessment, along with the latent space disentanglement index (LSDI) which uses the outputs of FV...

---

## 62. Ill-Conditioning in Dictionary-Based Dynamic-Equation Learning: A Systems Biology Case Study

**Authors**: Yuxiang Feng, Niall M Mangan, Manu Jayadharan  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11330  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11330v1.pdf

**Abstract**:
> arXiv:2603.11330v1 Announce Type: cross 
Abstract: Data-driven discovery of governing equations from time-series data provides a powerful framework for understanding complex biological systems. Library-based approaches that use sparse regression over candidate functions have shown considerable promise, but they face a critical challenge when candidate functions become strongly correlated: numerical ill-conditioning. Poor or restricted sampling, together with particular choices of candidate libraries, can produce strong multicollinearity and numerical instability. In such cases, measurement noise may lead to widely different recovered models, obscuring the true underlying dynamics and hindering accurate system identification. Although sparse regularization promotes parsimonious solutions an...

---

## 63. Detecting Intrinsic and Instrumental Self-Preservation in Autonomous Agents: The Unified Continuation-Interest Protocol

**Authors**: Christopher Altman  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11382  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11382v1.pdf

**Abstract**:
> arXiv:2603.11382v1 Announce Type: cross 
Abstract: Autonomous agents, especially delegated systems with memory, persistent context, and multi-step planning, pose a measurement problem not present in stateless models: an agent that preserves continued operation as a terminal objective and one that does so merely instrumentally can produce observationally similar trajectories. External behavioral monitoring cannot reliably distinguish between them. We introduce the Unified Continuation-Interest Protocol (UCIP), a multi-criterion detection framework that moves this distinction from behavior to the latent structure of agent trajectories. UCIP encodes trajectories with a Quantum Boltzmann Machine (QBM), a classical algorithm based on the density-matrix formalism of quantum statistical mechanics...

---

## 64. Zero-Shot Cross-City Generalization in End-to-End Autonomous Driving: Self-Supervised versus Supervised Representations

**Authors**: Fatemeh Naeinian, Ali Hamza, Haoran Zhu, Anna Choromanska  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11417  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11417v1.pdf

**Abstract**:
> arXiv:2603.11417v1 Announce Type: cross 
Abstract: End-to-end autonomous driving models are typically trained on multi-city datasets using supervised ImageNet-pretrained backbones, yet their ability to generalize to unseen cities remains largely unexamined. When training and evaluation data are geographically mixed, models may implicitly rely on city-specific cues, masking failure modes that would occur under real domain shifts when generalizing to new locations. In this work we investigate zero-shot cross-city generalization in end-to-end trajectory planning and ask whether self-supervised visual representations improve transfer across cities. We conduct a comprehensive study by integrating self-supervised backbones (I-JEPA, DINOv2, and MAE) into planning frameworks. We evaluate performan...

---

## 65. HawkesRank: Event-Driven Centrality for Real-Time Importance Ranking

**Authors**: Didier Sornette, Yishan Luo, Sandro Claudio Lera  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11472  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11472v1.pdf

**Abstract**:
> arXiv:2603.11472v1 Announce Type: cross 
Abstract: Quantifying influence in networks is important across science, economics, and public health, yet widely used centrality measures remain limited: they rely on static representations, heuristic network constructions, and purely endogenous notions of importance, while offering little semantic connection to observable activity. We introduce HawkesRank, a dynamic framework grounded in multivariate Hawkes point processes that models exogenous drivers (intrinsic contributions) and endogenous amplification (self- and cross-excitation). This yields a principled, empirically calibrated, and adaptive importance measure. Classical indices such as Katz centrality and PageRank emerge as mean-field limits of the framework, clarifying both their validity ...

---

## 66. One Supervisor, Many Modalities: Adaptive Tool Orchestration for Autonomous Queries

**Authors**: Mayank Saini Arit Kumar Bishwas  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11545  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11545v1.pdf

**Abstract**:
> arXiv:2603.11545v1 Announce Type: cross 
Abstract: We present an agentic AI framework for autonomous multimodal query processing that coordinates specialized tools across text, image, audio, video, and document modalities. A central Supervisor dynamically decomposes user queries, delegates subtasks to modality-appropriate tools (e.g., object detection, OCR, speech transcription), and synthesizes results through adaptive routing strategies rather than predetermined decision trees. For text-only queries, the framework uses learned routing via RouteLLM, while non-text paths use SLM-assisted modality decomposition. Evaluated on 2,847 queries across 15 task categories, our framework achieves 72% reduction in time-to-accurate-answer, 85% reduction in conversational rework, and 67% cost reduction...

---

## 67. Cross-Resolution Attention Network for High-Resolution PM2.5 Prediction

**Authors**: Ammar Kheder, Helmi Toropainen, Wenqing Peng, Samuel Ant\~ao, Zhi-Song Liu, Michael Boy  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11725  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11725v1.pdf

**Abstract**:
> arXiv:2603.11725v1 Announce Type: cross 
Abstract: Vision Transformers have achieved remarkable success in spatio-temporal prediction, but their scalability remains limited for ultra-high-resolution, continent-scale domains required in real-world environmental monitoring. A single European air-quality map at 1 km resolution comprises 29 million pixels, far beyond the limits of naive self-attention. We introduce CRAN-PM, a dual-branch Vision Transformer that leverages cross-resolution attention to efficiently fuse global meteorological data (25 km) with local high-resolution PM2.5 at the current time (1 km). Instead of including physically driven factors like temperature and topography as input, we further introduce elevation-aware self-attention and wind-guided cross-attention to force the...

---

## 68. Anomaly detection in time-series via inductive biases in the latent space of conditional normalizing flows

**Authors**: David Baumgartner, Eliezer de Souza da Silva, I\~nigo Urteaga  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11756  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11756v1.pdf

**Abstract**:
> arXiv:2603.11756v1 Announce Type: cross 
Abstract: Deep generative models for anomaly detection in multivariate time-series are typically trained by maximizing data likelihood. However, likelihood in observation space measures marginal density rather than conformity to structured temporal dynamics, and therefore can assign high probability to anomalous or out-of-distribution samples. We address this structural limitation by relocating the notion of anomaly to a prescribed latent space. We introduce explicit inductive biases in conditional normalizing flows, modeling time-series observations within a discrete-time state-space framework that constrains latent representations to evolve according to prescribed temporal dynamics. Under this formulation, expected behavior corresponds to complian...

---

## 69. Learning Transferable Sensor Models via Language-Informed Pretraining

**Authors**: Yuliang Chen, Arvind Pillai, Yu Yvonne Wu, Tess Z. Griffin, Lisa Marsch, Michael V. Heinz, Nicholas ...  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11950  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11950v1.pdf

**Abstract**:
> arXiv:2603.11950v1 Announce Type: cross 
Abstract: Modern sensing systems generate large volumes of unlabeled multivariate time-series data. This abundance of unlabeled data makes self-supervised learning (SSL) a natural approach for learning transferable representations. However, most existing approaches are optimized for reconstruction or forecasting objectives and often fail to capture the semantic structure required for downstream classification and reasoning tasks. While recent sensor-language alignment methods improve semantic generalization through captioning and zero-shot transfer, they are limited to fixed sensor configurations, such as predefined channel sets, signal lengths, or temporal resolutions, which hinders cross-domain applicability. To address these gaps, we introduce \t...

---

## 70. AGMARL-DKS: An Adaptive Graph-Enhanced Multi-Agent Reinforcement Learning for Dynamic Kubernetes Scheduling

**Authors**: Hamed Hamzeh  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12031  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12031v1.pdf

**Abstract**:
> arXiv:2603.12031v1 Announce Type: cross 
Abstract: State-of-the-art cloud-native applications require intelligent schedulers that can effectively balance system stability, resource utilisation, and associated costs. While Kubernetes provides feasibility-based placement by default, recent research efforts have explored the use of reinforcement learning (RL) for more intelligent scheduling decisions. However, current RL-based schedulers have three major limitations. First, most of these schedulers use monolithic centralised agents, which are non-scalable for large heterogeneous clusters. Second, the ones that use multi-objective reward functions assume simple, static, linear combinations of the objectives. Third, no previous work has produced a stress-aware scheduler that can react adaptivel...

---

## 71. Interpreting Contrastive Embeddings in Specific Domains with Fuzzy Rules

**Authors**: Javier Fumanal-Idocin, Mohammadreza Jamalifard, Javier Andreu-Perez  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12227  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12227v1.pdf

**Abstract**:
> arXiv:2603.12227v1 Announce Type: cross 
Abstract: Free-style text is still one of the common ways in which data is registered in real environments, like legal procedures and medical records. Because of that, there have been significant efforts in the area of natural language processing to convert these texts into a structured format, which standard machine learning methods can then exploit. One of the most popular methods to embed text into a vectorial representation is the Contrastive Language-Image Pre-training model (CLIP), which was trained using both image and text. Although the representations computed by CLIP have been very successful in zero-show and few-shot learning problems, they still have problems when applied to a particular domain. In this work, we use a fuzzy rule-based cl...

---

## 72. BiGain: Unified Token Compression for Joint Generation and Classification

**Authors**: Jiacheng Liu, Shengkun Tang, Jiacheng Cui, Dongkuan Xu, Zhiqiang Shen  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12240  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12240v1.pdf

**Abstract**:
> arXiv:2603.12240v1 Announce Type: cross 
Abstract: Acceleration methods for diffusion models (e.g., token merging or downsampling) typically optimize synthesis quality under reduced compute, yet often ignore discriminative capacity. We revisit token compression with a joint objective and present BiGain, a training-free, plug-and-play framework that preserves generation quality while improving classification in accelerated diffusion models. Our key insight is frequency separation: mapping feature-space signals into a frequency-aware representation disentangles fine detail from global semantics, enabling compression that respects both generative fidelity and discriminative utility. BiGain reflects this principle with two frequency-aware operators: (1) Laplacian-gated token merging, which enc...

---

## 73. Quantifying Aleatoric Uncertainty of the Treatment Effect: A Novel Orthogonal Learner

**Authors**: Valentyn Melnychuk, Stefan Feuerriegel, Mihaela van der Schaar  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2411.03387  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2411.03387v3.pdf

**Abstract**:
> arXiv:2411.03387v3 Announce Type: replace 
Abstract: Estimating causal quantities from observational data is crucial for understanding the safety and effectiveness of medical treatments. However, to make reliable inferences, medical practitioners require not only estimating averaged causal quantities, such as the conditional average treatment effect, but also understanding the randomness of the treatment effect as a random variable. This randomness is referred to as aleatoric uncertainty and is necessary for understanding the probability of benefit from treatment or quantiles of the treatment effect. Yet, the aleatoric uncertainty of the treatment effect has received surprisingly little attention in the causal machine learning community. To fill this gap, we aim to quantify the aleatoric u...

---

## 74. Finance-Informed Neural Network: Learning the Geometry of Option Pricing

**Authors**: Amine M. Aboussalah, Xuanze Li, Cheng Chi, Raj Patel  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2412.12213  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2412.12213v2.pdf

**Abstract**:
> arXiv:2412.12213v2 Announce Type: replace 
Abstract: We propose a Finance-Informed Neural Network (FINN) for option pricing and hedging that integrates financial theory directly into machine learning. Instead of training on observed option prices, FINN is learned through a self-supervised replication objective based on dynamic hedging, ensuring economic consistency by construction. We show theoretically that minimizing replication error recovers the arbitrage-free pricing operator and yields economically meaningful sensitivities. Empirically, FINN accurately recovers classical Black--Scholes prices and performs robustly in stochastic volatility environments, including the Heston model, while remaining stable in settings where analytical solutions are unavailable or unreliable. Fundamental ...

---

## 75. GTM: A General Time-series Model for Enhanced Representation Learning of Time-Series Data

**Authors**: Cheng He, Xu Huang, Gangwei Jiang, Zhaoyi Li, Defu Lian, Hong Xie, Enhong Chen, Xijie Liang, Zengron...  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2502.03264  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2502.03264v2.pdf

**Abstract**:
> arXiv:2502.03264v2 Announce Type: replace 
Abstract: Despite recent progress in time-series foundation models, challenges persist in improving representation learning and adapting to diverse downstream tasks. We introduce a General Time-series Model (GTM), which advances representation learning via a novel frequency-domain attention mechanism that captures time-granularity-aware features, an aspect underexplored in prior research. We further propose a novel pre-training strategy that unifies reconstruction and autoregressive objectives through a hybrid masking mechanism. Our pre-training strategy, combined with 2D positional encoding and span shuffling, enhances the robustness and generalization of representations. GTM is established as the first generative-task-agnostic model for time-ser...

---

## 76. Domain Feature Collapse: Implications for Out-of-Distribution Detection and Solutions

**Authors**: Hong Yang, Devroop Kar, Qi Yu, Alex Ororbia, Travis Desell  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2512.04034  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2512.04034v2.pdf

**Abstract**:
> arXiv:2512.04034v2 Announce Type: replace 
Abstract: Why do state-of-the-art OOD detection methods exhibit catastrophic failure when models are trained on single-domain datasets? We provide the first theoretical explanation for this phenomenon through the lens of information theory. We prove that supervised learning on single-domain data inevitably produces domain feature collapse -- representations where I(x_d; z) = 0, meaning domain-specific information is completely discarded. This is a fundamental consequence of information bottleneck optimization: models trained on single domains (e.g., medical images) learn to rely solely on class-specific features while discarding domain features, leading to catastrophic failure when detecting out-of-domain samples (e.g., achieving only 53% FPR@95 o...

---

## 77. A Learnable Wavelet Transformer for Long-Short Equity Trading and Risk-Adjusted Return Optimization

**Authors**: Shuozhe Li, Du Cheng, Leqi Liu  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2601.13435  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2601.13435v4.pdf

**Abstract**:
> arXiv:2601.13435v4 Announce Type: replace 
Abstract: Learning profitable intraday trading policies from financial time series is challenging due to heavy noise, non-stationarity, and strong cross-sectional dependence among related assets. We propose \emph{WaveLSFormer}, a learnable wavelet-based long-short Transformer that jointly performs multi-scale decomposition and return-oriented decision learning. Unlike standard time-series forecasting that optimizes prediction error and typically requires a separate position-sizing or portfolio-construction step, our model directly outputs a market-neutral long/short portfolio and is trained end-to-end on a trading objective with risk-aware regularization. Specifically, a learnable wavelet front-end generates low-/high-frequency components via an e...

---

## 78. De novo molecular structure elucidation from mass spectra via flow matching

**Authors**: Ghaith Mqawass (TUM School of Life Sciences Weihenstephan, Technical University of Munich, Germany, ...  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.19912  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.19912v2.pdf

**Abstract**:
> arXiv:2602.19912v2 Announce Type: replace 
Abstract: Mass spectrometry is a powerful and widely used tool for identifying molecular structures due to its sensitivity and ability to profile complex samples. However, translating spectra into full molecular structures is a difficult, under-defined inverse problem. Overcoming this problem is crucial for enabling biological insight, discovering new metabolites, and advancing chemical research across multiple fields. To this end, we develop MSFlow, a two-stage encoder-decoder flow-matching generative model that achieves state-of-the-art performance on the structure elucidation task for small molecules. In the first stage, we adopt a formula-restricted transformer model for encoding mass spectra into a continuous and chemically informative embedd...

---

## 79. On the Value of Tokeniser Pretraining in Physics Foundation Models

**Authors**: Hadi Sotoudeh, Payel Mukhopadhyay, Ruben Ohana, Michael McCabe, Neil D. Lawrence, Shirley Ho, Miles ...  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.05598  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.05598v2.pdf

**Abstract**:
> arXiv:2603.05598v2 Announce Type: replace 
Abstract: We investigate the impact of tokeniser pretraining on the accuracy and efficiency of physics emulation. Modern high-resolution simulations produce vast volumes of data spanning diverse physical regimes and scales. Training foundation models to learn the dynamics underlying such data enables the modelling of complex multiphysics phenomena, especially in data-limited settings. The emerging class of physics foundation models typically aims to learn two tasks jointly: (i) extracting compact representations of high-resolution spatiotemporal data, and (ii) capturing governing physical dynamics. However, learning both tasks from scratch simultaneously can impede the effectiveness of either process. We show that pretraining the tokeniser with an...

---

## 80. Rethinking the Harmonic Loss via Non-Euclidean Distance Layers

**Authors**: Maxwell Miller-Golub, Collin Coil, Kamil Faber, Marcin Pietron, Panpan Zheng, Pasquale Minervini, Ro...  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10225  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10225v2.pdf

**Abstract**:
> arXiv:2603.10225v2 Announce Type: replace 
Abstract: Cross-entropy loss has long been the standard choice for training deep neural networks, yet it suffers from interpretability limitations, unbounded weight growth, and inefficiencies that can contribute to costly training dynamics. The harmonic loss is a distance-based alternative grounded in Euclidean geometry that improves interpretability and mitigates phenomena such as grokking, or delayed generalization on the test set. However, the study of harmonic loss remains narrow: only Euclidean distance is explored, and no systematic evaluation of computational efficiency or sustainability was conducted. We extend harmonic loss by systematically investigating a broad spectrum of distance metrics as replacements for the Euclidean distance. We ...

---

## 81. Historical Consensus: Preventing Posterior Collapse via Iterative Selection of Gaussian Mixture Priors

**Authors**: Zegu Zhang, Jian Zhang  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10935  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10935v2.pdf

**Abstract**:
> arXiv:2603.10935v2 Announce Type: replace 
Abstract: Variational autoencoders (VAEs) frequently suffer from posterior collapse, where latent variables become uninformative and the approximate posterior degenerates to the prior. Recent work has characterized this phenomenon as a phase transition governed by the spectral properties of the data covariance matrix. In this paper, we propose a fundamentally different approach: instead of avoiding collapse through architectural constraints or hyperparameter tuning, we eliminate the possibility of collapse altogether by leveraging the multiplicity of Gaussian mixture model (GMM) clusterings. We introduce Historical Consensus Training, an iterative selection procedure that progressively refines a set of candidate GMM priors through alternating opti...

---

## 82. Bounds on Representation-Induced Confounding Bias for Treatment Effect Estimation

**Authors**: Valentyn Melnychuk, Dennis Frauen, Stefan Feuerriegel  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2311.11321  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2311.11321v4.pdf

**Abstract**:
> arXiv:2311.11321v4 Announce Type: replace-cross 
Abstract: State-of-the-art methods for conditional average treatment effect (CATE) estimation make widespread use of representation learning. Here, the idea is to reduce the variance of the low-sample CATE estimation by a (potentially constrained) low-dimensional representation. However, low-dimensional representations can lose information about the observed confounders and thus lead to bias, because of which the validity of representation learning for CATE estimation is typically violated. In this paper, we propose a new, representation-agnostic refutation framework for estimating bounds on the representation-induced confounding bias that comes from dimensionality reduction (or other constraints on the representations) in CATE estimation. F...

---

## 83. Mini-batch Estimation for Deep Cox Models: Statistical Foundations and Practical Guidance

**Authors**: Lang Zeng, Weijing Tang, Zhao Ren, Ying Ding  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2408.02839  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2408.02839v4.pdf

**Abstract**:
> arXiv:2408.02839v4 Announce Type: replace-cross 
Abstract: The stochastic gradient descent (SGD) algorithm has been widely used to optimize deep Cox neural network (Cox-NN) by updating model parameters using mini-batches of data. We show that SGD aims to optimize the average of mini-batch partial-likelihood, which is different from the standard partial-likelihood. This distinction requires developing new statistical properties for the global optimizer, namely, the mini-batch maximum partial-likelihood estimator (mb-MPLE). We establish that mb-MPLE for Cox-NN is consistent and achieves the optimal minimax convergence rate up to a polylogarithmic factor. For Cox regression with linear covariate effects, we further show that mb-MPLE is $\sqrt{n}$-consistent and asymptotically normal with asym...

---

## 84. Testability of Instrumental Variables in Additive Nonlinear, Non-Constant Effects Models

**Authors**: Xichen Guo, Zheng Li, Biwei Huang, Yan Zeng, Zhi Geng, Feng Xie  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2411.12184  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2411.12184v2.pdf

**Abstract**:
> arXiv:2411.12184v2 Announce Type: replace-cross 
Abstract: We address the issue of the testability of instrumental variables derived from observational data. Most existing testable implications are centered on scenarios where the treatment is a discrete variable, e.g., instrumental inequality (Pearl, 1995), or where the effect is assumed to be constant, e.g., instrumental variables condition based on the principle of independent mechanisms (Burauel, 2023). However, treatments can often be continuous variables, such as drug dosages or nutritional content levels, and non-constant effects may occur in many real-world scenarios. In this paper, we consider an additive nonlinear, non-constant effects model with unmeasured confounders, in which treatments can be either discrete or continuous, and...

---

## 85. Refine-POI: Reinforcement Fine-Tuned Large Language Models for Next Point-of-Interest Recommendation

**Authors**: Peibo Li, Shuang Ao, Hao Xue, Yang Song, Maarten de Rijke, Johan Barth\'elemy, Tomasz Bednarz, Flora...  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2506.21599  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2506.21599v4.pdf

**Abstract**:
> arXiv:2506.21599v4 Announce Type: replace-cross 
Abstract: Advancing large language models (LLMs) for the next point-of-interest (POI) recommendation task faces two fundamental challenges: (i) although existing methods produce semantic IDs that incorporate semantic information, their topology-blind indexing fails to preserve semantic continuity, meaning that proximity in ID values does not mirror the coherence of the underlying semantics; and (ii) supervised fine-tuning (SFT)-based methods restrict model outputs to top-1 predictions. These approaches suffer from "answer fixation" and neglect the need for top-k ranked lists and reasoning due to the scarcity of supervision. We propose Refine-POI, a framework that addresses these challenges through topology-aware ID generation and reinforceme...

---

## 86. On the Theoretical Limitations of Embedding-Based Retrieval

**Authors**: Orion Weller, Michael Boratko, Iftekhar Naim, Jinhyuk Lee  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2508.21038  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2508.21038v2.pdf

**Abstract**:
> arXiv:2508.21038v2 Announce Type: replace-cross 
Abstract: Vector embeddings have been tasked with an ever-increasing set of retrieval tasks over the years, with a nascent rise in using them for reasoning, instruction-following, coding, and more. These new benchmarks push embeddings to work for any query and any notion of relevance that could be given. While prior works have pointed out theoretical limitations of vector embeddings, there is a common assumption that these difficulties are exclusively due to unrealistic queries, and those that are not can be overcome with better training data and larger models. In this work, we demonstrate that we may encounter these theoretical limitations in realistic settings with extremely simple queries. We connect known results in learning theory, show...

---

## 87. UniFField: A Generalizable Unified Neural Feature Field for Visual, Semantic, and Spatial Uncertainties in Any Scene

**Authors**: Christian Maurer, Snehal Jauhri, Sophie Lueth, Georgia Chalvatzaki  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.06754  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.06754v2.pdf

**Abstract**:
> arXiv:2510.06754v2 Announce Type: replace-cross 
Abstract: Comprehensive visual, geometric, and semantic understanding of a 3D scene is crucial for successful execution of robotic tasks, especially in unstructured and complex environments. Additionally, to make robust decisions, it is necessary for the robot to evaluate the reliability of perceived information. While recent advances in 3D neural feature fields have enabled robots to leverage features from pretrained foundation models for tasks such as language-guided manipulation and navigation, existing methods suffer from two critical limitations: (i) they are typically scene-specific, and (ii) they lack the ability to model uncertainty in their predictions. We present UniFField, a unified uncertainty-aware neural feature field that comb...

---

## 88. A Foundational Theory of Quantitative Abstraction: Adjunctions, Duality, and Logic for Probabilistic Systems

**Authors**: Nivar Anwer (Georgia Institute of Technology, USA), Ezequiel L\'opez-Rubio (University of M\'alaga, ...  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.19444  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.19444v3.pdf

**Abstract**:
> arXiv:2510.19444v3 Announce Type: replace-cross 
Abstract: The analysis and control of stochastic dynamical systems rely on probabilistic models such as (continuous-space) Markov decision processes, but large or continuous state spaces make exact analysis intractable and call for principled quantitative abstraction. This work develops a unified theory of such abstraction by integrating category theory, coalgebra, quantitative logic, and optimal transport, centred on a canonical $\varepsilon$-quotient of the behavioral pseudo-metric with a universal property: among all abstractions that collapse behavioral differences below $\varepsilon$, it is the most detailed, and every other abstraction achieving the same discounted value-loss guarantee factors uniquely through it. Categorically, a quot...

---

## 89. RefTr: Recurrent Refinement of Confluent Trajectories for 3D Vascular Tree Centerlines

**Authors**: Roman Naeem, David Hagerman, Jennifer Alv\'en, Fredrik Kahl  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2511.20823  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2511.20823v2.pdf

**Abstract**:
> arXiv:2511.20823v2 Announce Type: replace-cross 
Abstract: Tubular tree structures such as blood vessels and lung airways are central to many clinical tasks, including diagnosis, treatment planning, and surgical navigation. Accurate centerline extraction with correct topology is essential, as missing small branches can lead to incomplete assessments or overlooked abnormalities. We propose RefTr, a 3D image-to-graph framework that generates vascular centerlines via recurrent refinement of confluent trajectories. RefTr adopts a Transformer-based Producer-Refiner architecture in which the Producer predicts candidate trajectories and a shared Refiner iteratively refines them toward the target branches. The confluent trajectory representation enables whole-branch refinement while explicitly enf...

---

## 90. Forests of Uncertaint(r)ees: Using tree-based ensembles to estimate probability distributions of future conflict

**Authors**: Daniel Mittermaier, Tobias Bohne, Martin Hofer, Daniel Racek  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2512.06210  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2512.06210v2.pdf

**Abstract**:
> arXiv:2512.06210v2 Announce Type: replace-cross 
Abstract: Predictions of fatalities from violent conflict on the PRIO-GRID-month (pgm) level are characterized by high levels of uncertainty, limiting their usefulness in practical applications. We discuss the two main sources of uncertainty for this prediction task, the nature of violent conflict and data limitations, embedding conflict prediction in the wider literature on uncertainty quantification in machine learning. Based on this, we develop a strategy to quantify uncertainty in conflict forecasting, shifting from traditional point predictions to full predictive distributions. Our approach combines multiple tree-based classifiers and distributional regressors in a custom AutoML setup, estimating distributions for each pgm individually....

---

## 91. LatentChem: From Textual CoT to Latent Thinking in Chemical Reasoning

**Authors**: Xinwu Ye, Yicheng Mao, Jia Zhang, Yimeng Liu, Li Hao, Fang Wu, Zhiwei Li, Yuxuan Liao, Zehong Wang, ...  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.07075  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.07075v3.pdf

**Abstract**:
> arXiv:2602.07075v3 Announce Type: replace-cross 
Abstract: Chemical large language models (LLMs) predominantly rely on explicit Chain-of-Thought (CoT) in natural language to perform complex reasoning. However, chemical reasoning is inherently continuous and structural, and forcing it into discrete linguistic tokens introduces a fundamental representation mismatch that constrains both efficiency and performance. We introduce LatentChem, a latent reasoning interface that decouples chemical computation from textual generation, enabling models to perform multi-step reasoning directly in continuous latent space while emitting language only for final outputs. Remarkably, we observe a consistent emergent behavior: when optimized solely for task success, models spontaneously internalize reasoning,...

---

## 92. Kernel-based optimization of measurement operators for quantum reservoir computers

**Authors**: Markus Gross, Hans-Martin Rieser  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.14677  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.14677v2.pdf

**Abstract**:
> arXiv:2602.14677v2 Announce Type: replace-cross 
Abstract: Finding optimal measurement operators is crucial for the performance of quantum reservoir computers (QRCs), since they employ a fixed quantum feature map. We formulate the training of both stateless (quantum extreme learning machines, QELMs) and stateful (memory dependent) QRCs in the framework of kernel ridge regression. We thus extend the kernel viewpoint of supervised quantum models to recurrent QRCs by deriving an exact Hilbert--Schmidt kernel representation of the optimal readout observable on history space. This approach renders an optimal measurement operator that minimizes prediction error for a given reservoir and training dataset. For large qubit numbers, this method is more efficient than the conventional training of QRC...

---

## 93. ECHOSAT: Estimating Canopy Height Over Space And Time

**Authors**: Jan Pauls, Karsten Schr\"odter, Sven Ligensa, Martin Schwartz, Berkant Turan, Max Zimmer, Sassan Saa...  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.21421  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.21421v2.pdf

**Abstract**:
> arXiv:2602.21421v2 Announce Type: replace-cross 
Abstract: Forest monitoring is critical for climate change mitigation. However, existing global tree height maps provide only static snapshots and do not capture temporal forest dynamics, which are essential for accurate carbon accounting. We introduce ECHOSAT, a global and temporally consistent tree height map at 10 m resolution spanning multiple years. To this end, we resort to multi-sensor satellite data to train a specialized vision transformer model, which performs pixel-level temporal regression. A self-supervised growth loss regularizes the predictions to follow growth curves that are in line with natural tree development, including gradual height increases over time, but also abrupt declines due to forest loss events such as fires. O...

---

## 94. Unsupervised Discovery of Intermediate Phase Order in the Frustrated $J_1$-$J_2$ Heisenberg Model via Prometheus Framework

**Authors**: Brandon Yee, Wilson Collins, Maximilian Rutkowski  
**Categories**: cs.LG  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.21468  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.21468v3.pdf

**Abstract**:
> arXiv:2602.21468v3 Announce Type: replace-cross 
Abstract: The spin-$1/2$ $J_1$-$J_2$ Heisenberg model on the square lattice exhibits a debated intermediate phase between N\'eel antiferromagnetic and stripe ordered regimes, with competing theories proposing plaquette valence bond, nematic, and quantum spin liquid ground states. We apply the Prometheus variational autoencoder framework -- previously validated on classical (2D, 3D Ising) and quantum (disordered transverse field Ising) phase transitions -- to systematically explore the $J_1$-$J_2$ phase diagram using a multi-scale approach. For $L=4$, we employ exact diagonalization with full wavefunction analysis via quantum-aware VAE. For larger systems ($L=6, 8$), we introduce a reduced density matrix (RDM) based methodology using DMRG gro...

---

## 95. A Survey of Reasoning in Autonomous Driving Systems: Open Challenges and Emerging Paradigms

**Authors**: Kejin Yu, Yuhan Sun, Taiqiang Wu, Ruixu Zhang, Zhiqiang Lin, Yuxin Meng, Junjie Wang, Yujiu Yang  
**Categories**: cs.AI  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11093  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11093v1.pdf

**Abstract**:
> arXiv:2603.11093v1 Announce Type: new 
Abstract: The development of high-level autonomous driving (AD) is shifting from perception-centric limitations to a more fundamental bottleneck, namely, a deficit in robust and generalizable reasoning. Although current AD systems manage structured environments, they consistently falter in long-tail scenarios and complex social interactions that require human-like judgment. Meanwhile, the advent of large language and multimodal models (LLMs and MLLMs) presents a transformative opportunity to integrate a powerful cognitive engine into AD systems, moving beyond pattern matching toward genuine comprehension. However, a systematic framework to guide this integration is critically lacking. To bridge this gap, we provide a comprehensive review of this emerg...

---

## 96. Improving LLM Performance Through Black-Box Online Tuning: A Case for Adding System Specs to Factsheets for Trusted AI

**Authors**: Yonas Atinafu, Henry Lin, Robin Cohen  
**Categories**: cs.AI  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11340  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11340v1.pdf

**Abstract**:
> arXiv:2603.11340v1 Announce Type: new 
Abstract: In this paper, we present a novel black-box online controller that uses only end-to-end measurements over short segments, without internal instrumentation, and hill climbing to maximize goodput, defined as the throughput of requests that satisfy the service-level objective. We provide empirical evidence that this design is well-founded. Using this advance in LLM serving as a concrete example, we then discuss the importance of integrating system performance and sustainability metrics into Factsheets for organizations adopting AI systems.

---

## 97. Speak or Stay Silent: Context-Aware Turn-Taking in Multi-Party Dialogue

**Authors**: Kratika Bhagtani, Mrinal Anand, Yu Chen Xu, Amit Kumar Singh Yadav  
**Categories**: cs.AI  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11409  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11409v1.pdf

**Abstract**:
> arXiv:2603.11409v1 Announce Type: new 
Abstract: Existing voice AI assistants treat every detected pause as an invitation to speak. This works in dyadic dialogue, but in multi-party settings, where an AI assistant participates alongside multiple speakers, pauses are abundant and ambiguous. An assistant that speaks on every pause becomes disruptive rather than useful. In this work, we formulate context-aware turn-taking: at every detected pause, given the full conversation context, our method decides whether the assistant should speak or stay silent. We introduce a benchmark of over 120K labeled conversations spanning three multi-party corpora. Evaluating eight recent large language models, we find that they consistently fail at context-aware turn-taking under zero-shot prompting. We then p...

---

## 98. See, Symbolize, Act: Grounding VLMs with Spatial Representations for Better Gameplay

**Authors**: Ashish Baghel, Paras Chopra  
**Categories**: cs.AI  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11601  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11601v1.pdf

**Abstract**:
> arXiv:2603.11601v1 Announce Type: new 
Abstract: Vision-Language Models (VLMs) excel at describing visual scenes, yet struggle to translate perception into precise, grounded actions. We investigate whether providing VLMs with both the visual frame and the symbolic representation of the scene can improve their performance in interactive environments. We evaluate three state-of-the-art VLMs across Atari games, VizDoom, and AI2-THOR, comparing frame-only, frame with self-extracted symbols, frame with ground-truth symbols, and symbol-only pipelines. Our results indicate that all models benefit when the symbolic information is accurate. However, when VLMs extract symbols themselves, performance becomes dependent on model capability and scene complexity. We further investigate how accurately VLM...

---

## 99. VisDoT : Enhancing Visual Reasoning through Human-Like Interpretation Grounding and Decomposition of Thought

**Authors**: Eunsoo Lee, Jeongwoo Lee, Minki Hong, Jangho Choi, Jihie Kim  
**Categories**: cs.AI  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11631  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11631v1.pdf

**Abstract**:
> arXiv:2603.11631v1 Announce Type: new 
Abstract: Large vision-language models (LVLMs) struggle to reliably detect visual primitives in charts and align them with semantic representations, which severely limits their performance on complex visual reasoning. This lack of perceptual grounding constitutes a major bottleneck for chart-based reasoning. We propose VisDoT, a framework that enhances visual reasoning through human-like interpretation grounding. We formalize four perceptual tasks based on the theory of graphical perception, including position and length. Building on this foundation, we introduce Decomposition-of-Thought (DoT) prompting, which sequentially separates questions into visual perception sub-questions and logic sub-questions. Fine-tuning InternVL with VisDoT achieves a +11....

---

## 100. LLMs can construct powerful representations and streamline sample-efficient supervised learning

**Authors**: Ilker Demirel, Larry Shi, Zeshan Hussain, David Sontag  
**Categories**: cs.AI  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11679  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11679v1.pdf

**Abstract**:
> arXiv:2603.11679v1 Announce Type: new 
Abstract: As real-world datasets become increasingly complex and heterogeneous, supervised learning is often bottlenecked by input representation design. Modeling multimodal data for downstream tasks, such as time-series, free text, and structured records, often requires non-trivial domain-specific engineering. We propose an agentic pipeline to streamline this process. First, an LLM analyzes a small but diverse subset of text-serialized input examples in-context to synthesize a global rubric, which acts as a programmatic specification for extracting and organizing evidence. This rubric is then used to transform naive text-serializations of inputs into a more standardized format for downstream models. We also describe local rubrics, which are task-cond...

---

## 101. DocSage: An Information Structuring Agent for Multi-Doc Multi-Entity Question Answering

**Authors**: Teng Lin, Yizhang Zhu, Zhengxuan Zhang, Yuyu Luo, Nan Tang  
**Categories**: cs.AI  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11798  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11798v1.pdf

**Abstract**:
> arXiv:2603.11798v1 Announce Type: new 
Abstract: Multi-document Multi-entity Question Answering inherently demands models to track implicit logic between multiple entities across scattered documents. However, existing Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG) frameworks suffer from critical limitations: standard RAG's vector similarity-based coarse-grained retrieval often omits critical facts, graph-based RAG fails to efficiently integrate fragmented complex relationship networks, and both lack schema awareness, leading to inadequate cross-document evidence chain construction and inaccurate entity relationship deduction. To address these challenges, we propose DocSage, an end-to-end agentic framework that integrates dynamic schema discovery, structured informati...

---

## 102. Increasing intelligence in AI agents can worsen collective outcomes

**Authors**: Neil F. Johnson  
**Categories**: cs.AI  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12129  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12129v1.pdf

**Abstract**:
> arXiv:2603.12129v1 Announce Type: new 
Abstract: When resources are scarce, will a population of AI agents coordinate in harmony, or descend into tribal chaos? Diverse decision-making AI from different developers is entering everyday devices -- from phones and medical devices to battlefield drones and cars -- and these AI agents typically compete for finite shared resources such as charging slots, relay bandwidth, and traffic priority. Yet their collective dynamics and hence risks to users and society are poorly understood. Here we study AI-agent populations as the first system of real agents in which four key variables governing collective behaviour can be independently toggled: nature (innate LLM diversity), nurture (individual reinforcement learning), culture (emergent tribe formation),...

---

## 103. TopoBench: Benchmarking LLMs on Hard Topological Reasoning

**Authors**: Mayug Maniparambil, Nils Hoehing, Janak Kapuriya, Arjun Karuvally, Ellen Rushe, Anthony Ventresque, ...  
**Categories**: cs.AI  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12133  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12133v1.pdf

**Abstract**:
> arXiv:2603.12133v1 Announce Type: new 
Abstract: Solving topological grid puzzles requires reasoning over global spatial invariants such as connectivity, loop closure, and region symmetry and remains challenging for even the most powerful large language models (LLMs). To study these abilities under controlled settings, we introduce TopoBench, a benchmark of six puzzle families across three difficulty levels. We evaluate strong reasoning LLMs on TopoBench and find that even frontier models solve fewer than one quarter of hard instances, with two families nearly unsolved. To investigate whether these failures stem from reasoning limitations or from difficulty extracting and maintaining spatial constraints, we annotate 750 chain of thought traces with an error taxonomy that surfaces four cand...

---

## 104. Hybrid Quantum-Classical Encoding for Accurate Residue-Level pKa Prediction

**Authors**: Van Le, Tan Le  
**Categories**: cs.AI  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11061  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11061v1.pdf

**Abstract**:
> arXiv:2603.11061v1 Announce Type: cross 
Abstract: Accurate prediction of residue-level pKa values is essential for understanding protein function, stability, and reactivity. While existing resources such as DeepKaDB and CpHMD-derived datasets provide valuable training data, their descriptors remain primarily classical and often struggle to generalize across diverse biochemical environments. We introduce a reproducible hybrid quantum-classical framework that enriches residue-level representations with a Gaussian kernel-based quantum-inspired feature mapping. These quantum-enhanced descriptors are combined with normalized structural features to form a unified hybrid encoding processed by a Deep Quantum Neural Network (DQNN). This architecture captures nonlinear relationships in residue micr...

---

## 105. Exploring Collatz Dynamics with Human-LLM Collaboration

**Authors**: Edward Y. Chang  
**Categories**: cs.AI  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11066  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11066v1.pdf

**Abstract**:
> arXiv:2603.11066v1 Announce Type: cross 
Abstract: We investigate structural properties of the Collatz iteration through two phenomena observed in large computational exploration: modular scrambling of residue classes and a burst--gap decomposition of trajectories. We prove several structural results, including a modular scrambling lemma showing that the gap-return map acts as an exact bijection on high bits, a persistent exit lemma characterizing gap structure after persistent states, and a decay property for known portions of binary representations under gap-return dynamics. We further prove that, in the modular model, gap lengths and $2$-adic valuations follow geometric distributions, while persistent run lengths are geometric with expected burst length $E[B]=2$; together these predict ...

---

## 106. Unifying Logical and Physical Layout Representations via Heterogeneous Graphs for Circuit Congestion Prediction

**Authors**: Runbang Hu, Bo Fang, Bingzhe Li, Yuede Ji  
**Categories**: cs.AI  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11075  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11075v1.pdf

**Abstract**:
> arXiv:2603.11075v1 Announce Type: cross 
Abstract: As Very Large Scale Integration (VLSI) designs continue to scale in size and complexity, layout verification has become a central challenge in modern Electronic Design Automation (EDA) workflows. In practice, congestion can only be accurately identified after detailed routing, making traditional verification both time-consuming and costly. Learning-based approaches have therefore been explored to enable early-stage congestion prediction and reduce routing iterations. However, although prior methods incorporate both netlist connectivity and layout features, they often model the two in a loosely coupled manner and primarily produce numerical congestion estimates. We propose VeriHGN, a verification framework built on an enhanced heterogeneous...

---

## 107. CR-Bench: Evaluating the Real-World Utility of AI Code Review Agents

**Authors**: Kristen Pereira, Neelabh Sinha, Rajat Ghosh, Debojyoti Dutta  
**Categories**: cs.AI  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11078  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11078v1.pdf

**Abstract**:
> arXiv:2603.11078v1 Announce Type: cross 
Abstract: Recent advances in frontier large language models have enabled code review agents that operate in open-ended, reasoning-intensive settings. However, the lack of standardized benchmarks and granular evaluation protocols makes it difficult to assess behavior of code review agents beyond coarse success metrics, particularly for tasks where false positives are costly. To address this gap, we introduce CR-Bench, a benchmarking dataset, and CR-Evaluator, a fine-grained evaluation pipeline for code review agents. Using these tools, we conduct a preliminary study evaluating both a single-shot agent and a Reflexion-based agent across two frontier models. We find that code review agents can exhibit a low signal-to-noise ratio when designed to identi...

---

## 108. ResWM: Residual-Action World Model for Visual RL

**Authors**: Jseen Zhang, Gabriel Adineera, Jinzhou Tan, Jinoh Kim  
**Categories**: cs.AI  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11110  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11110v1.pdf

**Abstract**:
> arXiv:2603.11110v1 Announce Type: cross 
Abstract: Learning predictive world models from raw visual observations is a central challenge in reinforcement learning (RL), especially for robotics and continuous control. Conventional model-based RL frameworks directly condition future predictions on absolute actions, which makes optimization unstable: the optimal action distributions are task-dependent, unknown a priori, and often lead to oscillatory or inefficient control. To address this, we introduce the Residual-Action World Model (ResWM), a new framework that reformulates the control variable from absolute actions to residual actions -- incremental adjustments relative to the previous step. This design aligns with the inherent smoothness of real-world control, reduces the effective search ...

---

## 109. Artificial Intelligence for Sentiment Analysis of Persian Poetry

**Authors**: Arash Zargar, Abolfazl Moshiri, Mitra Shafaei, Shabnam Rahimi-Golkhandan, Mohamad Tavakoli-Targhi, F...  
**Categories**: cs.AI  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11254  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11254v1.pdf

**Abstract**:
> arXiv:2603.11254v1 Announce Type: cross 
Abstract: Recent advancements of the Artificial Intelligence (AI) have led to the development of large language models (LLMs) that are capable of understanding, analysing, and creating textual data. These language models open a significant opportunity in analyzing the literature and more specifically poetry. In the present work, we employ multiple Bidirectional encoder representations from transformers (BERT) and Generative Pre-trained Transformer (GPT) based language models to analyze the works of two prominent Persian poets: Jalal al-Din Muhammad Rumi (Rumi) and Parvin E'tesami. The main objective of this research is to investigate the capability of the modern language models in grasping complexities of the Persian poetry and explore potential cor...

---

## 110. Evaluating Explainable AI Attribution Methods in Neural Machine Translation via Attention-Guided Knowledge Distillation

**Authors**: Aria Nourbakhsh, Salima Lamsiyah, Adelaide Danilov, Christoph Schommer  
**Categories**: cs.AI  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11342  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11342v1.pdf

**Abstract**:
> arXiv:2603.11342v1 Announce Type: cross 
Abstract: The study of the attribution of input features to the output of neural network models is an active area of research. While numerous Explainable AI (XAI) techniques have been proposed to interpret these models, the systematic and automated evaluation of these methods in sequence-to-sequence (seq2seq) models is less explored. This paper introduces a new approach for evaluating explainability methods in transformer-based seq2seq models. We use teacher-derived attribution maps as a structured side signal to guide a student model, and quantify the utility of different attribution methods through the student's ability to simulate targets. Using the Inseq library, we extract attribution scores over source-target sequence pairs and inject these sc...

---

## 111. SPEGC: Continual Test-Time Adaptation via Semantic-Prompt-Enhanced Graph Clustering for Medical Image Segmentation

**Authors**: Xiaogang Du, Jiawei Zhang, Tongfei Liu, Tao Lei, Yingbo Wang  
**Categories**: cs.AI  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11492  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11492v1.pdf

**Abstract**:
> arXiv:2603.11492v1 Announce Type: cross 
Abstract: In medical image segmentation tasks, the domain gap caused by the difference in data collection between training and testing data seriously hinders the deployment of pre-trained models in clinical practice. Continual Test-Time Adaptation (CTTA) aims to enable pre-trained models to adapt to continuously changing unlabeled domains, providing an effective approach to solving this problem. However, existing CTTA methods often rely on unreliable supervisory signals, igniting a self-reinforcing cycle of error accumulation that culminates in catastrophic performance degradation. To overcome these challenges, we propose a CTTA via Semantic-Prompt-Enhanced Graph Clustering (SPEGC) for medical image segmentation. First, we design a semantic prompt f...

---

## 112. ReHARK: Refined Hybrid Adaptive RBF Kernels for Robust One-Shot Vision-Language Adaptation

**Authors**: Md Jahidul Islam  
**Categories**: cs.AI  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11542  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11542v1.pdf

**Abstract**:
> arXiv:2603.11542v1 Announce Type: cross 
Abstract: The adaptation of large-scale Vision-Language Models (VLMs) like CLIP to downstream tasks with extremely limited data -- specifically in the one-shot regime -- is often hindered by a significant "Stability-Plasticity" dilemma. While efficient caching mechanisms have been introduced by training-free methods such as Tip-Adapter, these approaches often function as local Nadaraya-Watson estimators. Such estimators are characterized by inherent boundary bias and a lack of global structural regularization. In this paper, ReHARK (Refined Hybrid Adaptive RBF Kernels) is proposed as a synergistic training-free framework that reinterprets few-shot adaptation through global proximal regularization in a Reproducing Kernel Hilbert Space (RKHS). A multi...

---

## 113. IDRL: An Individual-Aware Multimodal Depression-Related Representation Learning Framework for Depression Diagnosis

**Authors**: Chongxiao Wang, Junjie Liang, Peng Cao, Jinzhu Yang, Osmar R. Zaiane  
**Categories**: cs.AI  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11644  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11644v1.pdf

**Abstract**:
> arXiv:2603.11644v1 Announce Type: cross 
Abstract: Depression is a severe mental disorder, and reliable identification plays a critical role in early intervention and treatment. Multimodal depression detection aims to improve diagnostic performance by jointly modeling complementary information from multiple modalities. Recently, numerous multimodal learning approaches have been proposed for depression analysis; however, these methods suffer from the following limitations: 1) inter-modal inconsistency and depression-unrelated interference, where depression-related cues may conflict across modalities while substantial irrelevant content obscures critical depressive signals, and 2) diverse individual depressive presentations, leading to individual differences in modality and cue importance th...

---

## 114. Stable Spike: Dual Consistency Optimization via Bitwise AND Operations for Spiking Neural Networks

**Authors**: Yongqi Ding, Kunshan Yang, Linze Li, Yiyang Zhang, Mengmeng Jing, Lin Zuo  
**Categories**: cs.AI  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11676  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11676v1.pdf

**Abstract**:
> arXiv:2603.11676v1 Announce Type: cross 
Abstract: Although the temporal spike dynamics of spiking neural networks (SNNs) enable low-power temporal pattern capture capabilities, they also incur inherent inconsistencies that severely compromise representation. In this paper, we perform dual consistency optimization via Stable Spike to mitigate this problem, thereby improving the recognition performance of SNNs. With the hardware-friendly ``AND" bit operation, we efficiently decouple the stable spike skeleton from the multi-timestep spike maps, thereby capturing critical semantics while reducing inconsistencies from variable noise spikes. Enforcing the unstable spike maps to converge to the stable spike skeleton significantly improves the inherent consistency across timesteps. Furthermore, w...

---

## 115. Adapting Dijkstra for Buffers and Unlimited Transfers

**Authors**: Denys Katkalo, Andrii Rohovyi, Toby Walsh  
**Categories**: cs.AI  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11729  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11729v1.pdf

**Abstract**:
> arXiv:2603.11729v1 Announce Type: cross 
Abstract: In recent years, RAPTOR based algorithms have been considered the state-of-the-art for path-finding with unlimited transfers without preprocessing. However, this status largely stems from the evolution of routing research, where Dijkstra-based solutions were superseded by timetable-based algorithms without a systematic comparison. In this work, we revisit classical Dijkstra-based approaches for public transit routing with unlimited transfers and demonstrate that Time-Dependent Dijkstra (TD-Dijkstra) outperforms MR. However, efficient TD-Dijkstra implementations rely on filtering dominated connections during preprocessing, which assumes passengers can always switch to a faster connection. We show that this filtering is unsound when stops ha...

---

## 116. HELM: Hierarchical and Explicit Label Modeling with Graph Learning for Multi-Label Image Classification

**Authors**: Marjan Stoimchev, Boshko Koloski, Jurica Levati\'c, Dragi Kocev, Sa\v{s}o D\v{z}eroski  
**Categories**: cs.AI  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11783  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11783v1.pdf

**Abstract**:
> arXiv:2603.11783v1 Announce Type: cross 
Abstract: Hierarchical multi-label classification (HMLC) is essential for modeling complex label dependencies in remote sensing. Existing methods, however, struggle with multi-path hierarchies where instances belong to multiple branches, and they rarely exploit unlabeled data. We introduce HELM (\textit{Hierarchical and Explicit Label Modeling}), a novel framework that overcomes these limitations. HELM: (i) uses hierarchy-specific class tokens within a Vision Transformer to capture nuanced label interactions; (ii) employs graph convolutional networks to explicitly encode the hierarchical structure and generate hierarchy-aware embeddings; and (iii) integrates a self-supervised branch to effectively leverage unlabeled imagery. We perform a comprehensi...

---

## 117. ELISA: An Interpretable Hybrid Generative AI Agent for Expression-Grounded Discovery in Single-Cell Genomics

**Authors**: Omar Coser  
**Categories**: cs.AI  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11872  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11872v1.pdf

**Abstract**:
> arXiv:2603.11872v1 Announce Type: cross 
Abstract: Translating single-cell RNA sequencing (scRNA-seq) data into mechanistic biological hypotheses remains a critical bottleneck, as agentic AI systems lack direct access to transcriptomic representations while expression foundation models remain opaque to natural language. Here we introduce ELISA (Embedding-Linked Interactive Single-cell Agent), an interpretable framework that unifies scGPT expression embeddings with BioBERT-based semantic retrieval and LLM-mediated interpretation for interactive single-cell discovery. An automatic query classifier routes inputs to gene marker scoring, semantic matching, or reciprocal rank fusion pipelines depending on whether the query is a gene signature, natural language concept, or mixture of both. Integr...

---

## 118. Multimodal Emotion Recognition via Bi-directional Cross-Attention and Temporal Modeling

**Authors**: Junhyeong Byeon, Jeongyeol Kim, Sejoon Lim  
**Categories**: cs.AI  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11971  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11971v1.pdf

**Abstract**:
> arXiv:2603.11971v1 Announce Type: cross 
Abstract: Emotion recognition in in-the-wild video data remains a challenging problem due to large variations in facial appearance, head pose, illumination, background noise, and the inherently dynamic nature of human affect. Relying on a single modality, such as facial expressions or speech, is often insufficient to capture these complex emotional cues. To address this issue, we propose a multimodal emotion recognition framework for the Expression (EXPR) Recognition task in the 10th Affective Behavior Analysis in-the-wild (ABAW) Challenge.
  Our approach leverages large-scale pre-trained models, namely CLIP for visual encoding and Wav2Vec 2.0 for audio representation learning, as frozen backbone networks. To model temporal dependencies in facial ex...

---

## 119. Beyond Convolution: A Taxonomy of Structured Operators for Learning-Based Image Processing

**Authors**: Simone Cammarasana  
**Categories**: cs.AI  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12067  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12067v1.pdf

**Abstract**:
> arXiv:2603.12067v1 Announce Type: cross 
Abstract: The convolution operator is the fundamental building block of modern convolutional neural networks (CNNs), owing to its simplicity, translational equivariance, and efficient implementation. However, its structure as a fixed, linear, locally-averaging operator limits its ability to capture structured signal properties such as low-rank decompositions, adaptive basis representations, and non-uniform spatial dependencies. This paper presents a systematic taxonomy of operators that extend or replace the standard convolution in learning-based image processing pipelines. We organise the landscape of alternative operators into five families: (i) decomposition-based operators, which separate structural and noise components through singular value or...

---

## 120. SommBench: Assessing Sommelier Expertise of Language Models

**Authors**: William Brach, Tomas Bedej, Jacob Nielsen, Jacob Pichna, Juraj Bedej, Eemeli Saarensilta, Julie Dupo...  
**Categories**: cs.AI  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12117  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12117v1.pdf

**Abstract**:
> arXiv:2603.12117v1 Announce Type: cross 
Abstract: With the rapid advances of large language models, it becomes increasingly important to systematically evaluate their multilingual and multicultural capabilities. Previous cultural evaluation benchmarks focus mainly on basic cultural knowledge that can be encoded in linguistic form. Here, we propose SommBench, a multilingual benchmark to assess sommelier expertise, a domain deeply grounded in the senses of smell and taste. While language models learn about sensory properties exclusively through textual descriptions, SommBench tests whether this textual grounding is sufficient to emulate expert-level sensory judgment. SommBench comprises three main tasks: Wine Theory Question Answering (WTQA), Wine Feature Completion (WFC), and Food-Wine Pai...

---

## 121. WORKSWORLD: A Domain for Integrated Numeric Planning and Scheduling of Distributed Pipelined Workflows

**Authors**: Taylor Paul, William Regli  
**Categories**: cs.AI  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12214  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12214v1.pdf

**Abstract**:
> arXiv:2603.12214v1 Announce Type: cross 
Abstract: This work pursues automated planning and scheduling of distributed data pipelines, or workflows. We develop a general workflow and resource graph representation that includes both data processing and sharing components with corresponding network interfaces for scheduling. Leveraging these graphs, we introduce WORKSWORLD, a new domain for numeric domain-independent planners designed for permanently scheduled workflows, like ingest pipelines. Our framework permits users to define data sources, available workflow components, and desired data destinations and formats without explicitly declaring the entire workflow graph as a goal. The planner solves a joint planning and scheduling problem, producing a plan that both builds the workflow graph ...

---

## 122. Incremental Neural Network Verification via Learned Conflicts

**Authors**: Raya Elsaleh, Liam Davis, Haoze Wu, Guy Katz  
**Categories**: cs.AI  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12232  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12232v1.pdf

**Abstract**:
> arXiv:2603.12232v1 Announce Type: cross 
Abstract: Neural network verification is often used as a core component within larger analysis procedures, which generate sequences of closely related verification queries over the same network. In existing neural network verifiers, each query is typically solved independently, and information learned during previous runs is discarded, leading to repeated exploration of the same infeasible regions of the search space. In this work, we aim to expedite verification by reducing this redundancy. We propose an incremental verification technique that reuses learned conflicts across related verification queries. The technique can be added on top of any branch-and-bound-based neural network verifier. During verification, the verifier records conflicts corre...

---

## 123. Adaptive Hyperbolic Kernels: Modulated Embedding in de Branges-Rovnyak Spaces

**Authors**: Leping Si, Meimei Yang, Hui Xue, Shipeng Zhu, Pengfei Fang  
**Categories**: cs.AI  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2511.09921  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2511.09921v2.pdf

**Abstract**:
> arXiv:2511.09921v2 Announce Type: replace 
Abstract: Hierarchical data pervades diverse machine learning applications, including natural language processing, computer vision, and social network analysis. Hyperbolic space, characterized by its negative curvature, has demonstrated strong potential in such tasks due to its capacity to embed hierarchical structures with minimal distortion. Previous evidence indicates that the hyperbolic representation capacity can be further enhanced through kernel methods. However, existing hyperbolic kernels still suffer from mild geometric distortion or lack adaptability. This paper addresses these issues by introducing a curvature-aware de Branges-Rovnyak space, a reproducing kernel Hilbert space (RKHS) that is isometric to a Poincare ball. We design an ad...

---

## 124. Evolving Beyond Snapshots: Harmonizing Structure and Sequence via Entity State Tuning for Temporal Knowledge Graph Forecasting

**Authors**: Siyuan Li, Yunjia Wu, Yiyong Xiao, Pingyang Huang, Peize Li, Ruitong Liu, Yan Wen, Te Sun, Fangyi Pe...  
**Categories**: cs.AI  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.12389  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.12389v2.pdf

**Abstract**:
> arXiv:2602.12389v2 Announce Type: replace 
Abstract: Temporal knowledge graph (TKG) forecasting requires predicting future facts by jointly modeling structural dependencies within each snapshot and temporal evolution across snapshots. However, most existing methods are stateless: they recompute entity representations at each timestamp from a limited query window, leading to episodic amnesia and rapid decay of long-term dependencies. To address this limitation, we propose Entity State Tuning (EST), an encoder-agnostic framework that endows TKG forecasters with persistent and continuously evolving entity states. EST maintains a global state buffer and progressively aligns structural evidence with sequential signals via a closed-loop design. Specifically, a topology-aware state perceiver firs...

---

## 125. Expectation and Acoustic Neural Network Representations Enhance Music Identification from Brain Activity

**Authors**: Shogo Noguchi, Taketo Akama, Tai Nakamura, Shun Minamikawa, Natalia Polouliakh  
**Categories**: cs.AI  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.03190  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.03190v2.pdf

**Abstract**:
> arXiv:2603.03190v2 Announce Type: replace 
Abstract: During music listening, cortical activity encodes both acoustic and expectation-related information. Prior work has shown that ANN representations resemble cortical representations and can serve as supervisory signals for EEG recognition. Here we show that distinguishing acoustic and expectation-related ANN representations as teacher targets improves EEG-based music identification. Models pretrained to predict either representation outperform non-pretrained baselines, and combining them yields complementary gains that exceed strong seed ensembles formed by varying random initializations. These findings show that teacher representation type shapes downstream performance and that representation learning can be guided by neural encoding. Th...

---

## 126. AgentOS: From Application Silos to a Natural Language-Driven Data Ecosystem

**Authors**: Rui Liu, Tao Zhe, Dongjie Wang, Zijun Yao, Kunpeng Liu, Yanjie Fu, Huan Liu, Jian Pei  
**Categories**: cs.AI  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.08938  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.08938v2.pdf

**Abstract**:
> arXiv:2603.08938v2 Announce Type: replace 
Abstract: The rapid emergence of open-source, locally hosted intelligent agents marks a critical inflection point in human-computer interaction. Systems such as OpenClaw demonstrate that Large Language Model (LLM)-based agents can autonomously operate local computing environments, orchestrate workflows, and integrate external tools. However, within the current paradigm, these agents remain conventional applications running on legacy operating systems originally designed for Graphical User Interfaces (GUIs) or Command Line Interfaces (CLIs). This architectural mismatch leads to fragmented interaction models, poorly structured permission management (often described as "Shadow AI"), and severe context fragmentation. This paper proposes a new paradigm...

---

## 127. Logics-Parsing-Omni Technical Report

**Authors**: Xin An, Jingyi Cai, Xiangyang Chen, Huayao Liu, Peiting Liu, Peng Wang, Bei Yang, Xiuwen Zhu, Yongfa...  
**Categories**: cs.AI  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.09677  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.09677v2.pdf

**Abstract**:
> arXiv:2603.09677v2 Announce Type: replace 
Abstract: Addressing the challenges of fragmented task definitions and the heterogeneity of unstructured data in multimodal parsing, this paper proposes the Omni Parsing framework. This framework establishes a Unified Taxonomy covering documents, images, and audio-visual streams, introducing a progressive parsing paradigm that bridges perception and cognition. Specifically, the framework integrates three hierarchical levels: 1) Holistic Detection, which achieves precise spatial-temporal grounding of objects or events to establish a geometric baseline for perception; 2) Fine-grained Recognition, which performs symbolization (e.g., OCR/ASR) and attribute extraction on localized objects to complete structured entity parsing; and 3) Multi-level Interp...

---

## 128. Partially Recentralization Softmax Loss for Vision-Language Models Robustness

**Authors**: Hao Wang, Jinzhe Jiang, Xin Zhang, Chen Li  
**Categories**: cs.AI  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2402.03627  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2402.03627v3.pdf

**Abstract**:
> arXiv:2402.03627v3 Announce Type: replace-cross 
Abstract: As Large Language Models make a breakthrough in natural language processing tasks (NLP), multimodal technique becomes extremely popular. However, it has been shown that multimodal NLP are vulnerable to adversarial attacks, where the outputs of a model can be dramatically changed by a perturbation to the input. While several defense techniques have been proposed both in computer vision and NLP models, the multimodal robustness of models have not been fully explored. In this paper, we study the adversarial robustness provided by modifying loss function of pre-trained multimodal models, by restricting top K softmax outputs. Based on the evaluation and scoring, our experiments show that after a fine-tuning, adversarial robustness of pr...

---

## 129. Let's Verify Math Questions Step by Step

**Authors**: Chengyu Shen, Zhen Hao Wong, Runming He, Hao Liang, Meiyi Qiang, Zimo Meng, Zhengyang Zhao, Bohan Ze...  
**Categories**: cs.AI  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2505.13903  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2505.13903v2.pdf

**Abstract**:
> arXiv:2505.13903v2 Announce Type: replace-cross 
Abstract: Large Language Models (LLMs) have recently achieved remarkable progress in mathematical reasoning. To enable such capabilities, many existing works distill strong reasoning models into long chains of thought or design algorithms to construct high-quality math question-answer (QA) data for training. However, these efforts primarily focus on generating correct reasoning paths and answers, while largely overlooking the correctness of the questions themselves. In this work, we present ValiMath, a benchmark consisting of 2147 human-verified mathematical questions covering a wide range of domains such as arithmetic, algebra, and geometry, which are synthesized and curated from the NuminaMath dataset. Each question is annotated with its l...

---

## 130. Hope Speech Detection in code-mixed Roman Urdu tweets: A Positive Turn in Natural Language Processing

**Authors**: Muhammad Ahmad, Muhammad Waqas, Ameer Hamza, Ildar Batyrshin, Grigori Sidorov  
**Categories**: cs.AI  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2506.21583  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2506.21583v2.pdf

**Abstract**:
> arXiv:2506.21583v2 Announce Type: replace-cross 
Abstract: Hope is a positive emotional state involving the expectation of favorable future outcomes, while hope speech refers to communication that promotes optimism, resilience, and support, particularly in adverse contexts. Although hope speech detection has gained attention in Natural Language Processing (NLP), existing research mainly focuses on high-resource languages and standardized scripts, often overlooking informal and underrepresented forms such as Roman Urdu. To the best of our knowledge, this is the first study to address hope speech detection in code-mixed Roman Urdu by introducing a carefully annotated dataset, thereby filling a critical gap in inclusive NLP research for low-resource, informal language varieties. This study ma...

---

## 131. Efficient Construction of Implicit Surface Models From a Single Image for Motion Generation

**Authors**: Wei-Teng Chu, Tianyi Zhang, Matthew Johnson-Roberson, Weiming Zhi  
**Categories**: cs.AI  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2509.20681  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2509.20681v3.pdf

**Abstract**:
> arXiv:2509.20681v3 Announce Type: replace-cross 
Abstract: Implicit representations have been widely applied in robotics for obstacle avoidance and path planning. In this paper, we explore the problem of constructing an implicit distance representation from a single image. Past methods for implicit surface reconstruction, such as NeuS and its variants generally require a large set of multi-view images as input, and require long training times. In this work, we propose Fast Image-to-Neural Surface (FINS), a lightweight framework that can reconstruct high-fidelity surfaces and SDF fields based on a single or a small set of images. FINS integrates a multi-resolution hash grid encoder with lightweight geometry and color heads, making the training via an approximate second-order optimizer highl...

---

## 132. Think with 3D: Geometric Imagination Grounded Spatial Reasoning from Limited Views

**Authors**: Zhangquan Chen, Manyuan Zhang, Xinlei Yu, Xufang Luo, Mingze Sun, Zihao Pan, Xiang An, Yan Feng, Pen...  
**Categories**: cs.AI  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.18632  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.18632v3.pdf

**Abstract**:
> arXiv:2510.18632v3 Announce Type: replace-cross 
Abstract: Though recent advances in vision-language models (VLMs) have achieved remarkable progress across a wide range of multimodal tasks, understanding 3D spatial relationships from limited views remains a significant challenge. Previous reasoning methods typically rely on pure text (e.g., topological cognitive maps) or on 2D visual cues. However, their limited representational capacity hinders performance in specific tasks that require 3D spatial imagination. To address this limitation, we propose 3DThinker, a framework that can effectively exploits the rich geometric information embedded within images while reasoning, like humans do. Our framework is the first to enable 3D mentaling during reasoning without any 3D prior input, and it do...

---

## 133. Knowledge Distillation with Structured Chain-of-Thought for Text-to-SQL

**Authors**: Khushboo Thaker, Yony Bresler  
**Categories**: cs.AI  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2512.17053  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2512.17053v3.pdf

**Abstract**:
> arXiv:2512.17053v3 Announce Type: replace-cross 
Abstract: Deploying accurate Text-to-SQL systems at the enterprise level faces a difficult trilemma involving cost, security and performance. Current solutions force enterprises to choose between expensive, proprietary Large Language Models (LLMs) and low-performing Small Language Models (SLMs). Efforts to improve SLMs often rely on distilling reasoning from large LLMs using unstructured Chain-of-Thought (CoT) traces, a process that remains inherently ambiguous. Instead, we hypothesize that a formal, structured reasoning representation provides a clearer, more reliable teaching signal, as the Text-to-SQL task requires explicit and precise logical steps. To evaluate this hypothesis, we propose Struct-SQL, a novel Knowledge Distillation (KD) f...

---

## 134. From Toil to Thought: Designing for Strategic Exploration and Responsible AI in Systematic Literature Reviews

**Authors**: Runlong Ye, Naaz Sibia, Angela Zavaleta Bernuy, Tingting Zhu, Carolina Nobre, Viktoria Pammer-Schind...  
**Categories**: cs.AI  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.05514  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.05514v2.pdf

**Abstract**:
> arXiv:2603.05514v2 Announce Type: replace-cross 
Abstract: Systematic Literature Reviews (SLRs) are fundamental to scientific progress, yet the process is hindered by a fragmented tool ecosystem that imposes a high cognitive load. This friction suppresses the iterative, exploratory nature of scholarly work. To investigate these challenges, we conducted an exploratory design study with 20 experienced researchers. This study identified key friction points: 1) the high cognitive load of managing iterative query refinement across multiple databases, 2) the overwhelming scale and pace of publication of modern literature, and 3) the tension between automation and scholarly agency. Informed by these findings, we developed ARC, a design probe that operationalizes solutions for multi-database integ...

---

## 135. Evaluating LLM-Based Grant Proposal Review via Structured Perturbations

**Authors**: William Thorne, Joseph James, Yang Wang, Chenghua Lin, Diana Maynard  
**Categories**: cs.AI  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.08281  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.08281v2.pdf

**Abstract**:
> arXiv:2603.08281v2 Announce Type: replace-cross 
Abstract: As AI-assisted grant proposals outpace manual review capacity in a kind of ``Malthusian trap'' for the research ecosystem, this paper investigates the capabilities and limitations of LLM-based grant reviewing for high-stakes evaluation. Using six EPSRC proposals, we develop a perturbation-based framework probing LLM sensitivity across six quality axes: funding, timeline, competency, alignment, clarity, and impact. We compare three review architectures: single-pass review, section-by-section analysis, and a 'Council of Personas' ensemble emulating expert panels. The section-level approach significantly outperforms alternatives in both detection rate and scoring reliability, while the computationally expensive council method performs...

---

## 136. Human-Aware Robot Behaviour in Self-Driving Labs

**Authors**: Satheeshkumar Veeramani, Anna Kisil, Abigail Bentley, Hatem Fakhruldeen, Gabriella Pizzuto, Andrew I...  
**Categories**: cs.AI  
**Published**: Fri, 13 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.08420  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.08420v2.pdf

**Abstract**:
> arXiv:2603.08420v2 Announce Type: replace-cross 
Abstract: Self-driving laboratories (SDLs) are rapidly transforming research in chemistry and materials science to accelerate new discoveries. Mobile robot chemists (MRCs) play a pivotal role by autonomously navigating the lab to transport samples, effectively connecting synthesis, analysis, and characterisation equipment. The instruments within an SDL are typically designed or retrofitted to be accessed by both human and robotic chemists, ensuring operational flexibility and integration between manual and automated workflows. In many scenarios, human and robotic chemists may need to use the same equipment simultaneously. Currently, MRCs rely on simple LiDAR-based obstruction detection, which forces the robot to passively wait if a human is ...

---

