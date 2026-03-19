# arXiv Papers - 2026-03-19

**来源**: arXiv (cs.SD, eess.AS, cs.LG, cs.AI)  
**关键词**: speech, audio, music, voice, sound, Mel, representation, self-supervised  
**今日新论文**: 137 篇

---

## 1. PulmoVec: A Two-Stage Stacking Meta-Learning Architecture Built on the HeAR Foundation Model for Multi-Task Classification of Pediatric Respiratory Sounds

**Authors**: Izzet Turkalp Akbasli, Oguzhan Serin  
**Categories**: cs.SD  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15688  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15688v1.pdf

**Abstract**:
> arXiv:2603.15688v1 Announce Type: new 
Abstract: Background: Respiratory diseases are a leading cause of childhood morbidity and mortality, yet lung auscultation remains subjective and limited by inter-listener variability, particularly in pediatric populations. Existing AI approaches are further constrained by small datasets and single-task designs. We developed PulmoVec, a multi-task framework built on the Health Acoustic Representations (HeAR) foundation model for classification of pediatric respiratory sounds. Methods: In this retrospective analysis of the SPRSound database, 24,808 event-level annotated segments from 1,652 pediatric patients were analyzed. Three task-specific classifiers were trained for screening, sound-pattern recognition, and disease-group prediction. Their out-of-f...

---

## 2. INSTRUMENTAL: Automatic Synthesizer Parameter Recovery from Audio via Evolutionary Optimization

**Authors**: Philipp Bogdan  
**Categories**: cs.SD  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15905  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15905v1.pdf

**Abstract**:
> arXiv:2603.15905v1 Announce Type: new 
Abstract: Existing audio-to-MIDI tools extract notes but discard the timbral characteristics that define an instrument's identity. We present Instrumental, a system that recovers continuous synthesizer parameters from audio by coupling a differentiable 28-parameter subtractive synthesizer with CMA-ES, a derivative-free evolutionary optimizer. We optimize a composite perceptual loss combining mel-scaled STFT, spectral centroid, and MFCC divergence, achieving a matching loss of 2.09 on real recorded audio. We systematically evaluate eight hypotheses for improving convergence and find that only parametric EQ boosting yields meaningful improvement. Our results show that CMA-ES outperforms gradient descent on this non-convex landscape, that more parameters...

---

## 3. Diffusion Models for Joint Audio-Video Generation

**Authors**: Alejandro Paredes La Torre  
**Categories**: cs.SD  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16093  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16093v1.pdf

**Abstract**:
> arXiv:2603.16093v1 Announce Type: new 
Abstract: Multimodal generative models have shown remarkable progress in single-modality video and audio synthesis, yet truly joint audio-video generation remains an open challenge. In this paper, I explore four key contributions to advance this field. First, I release two high-quality, paired audio-video datasets. The datasets consisting on 13 hours of video-game clips and 64 hours of concert performances, each segmented into consistent 34-second samples to facilitate reproducible research. Second, I train the MM-Diffusion architecture from scratch on our datasets, demonstrating its ability to produce semantically coherent audio-video pairs and quantitatively evaluating alignment on rapid actions and musical cues. Third, I investigate joint latent di...

---

## 4. A Semantic Timbre Dataset for the Electric Guitar

**Authors**: Joseph Cameron, Alan Blackwell  
**Categories**: cs.SD  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16682  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16682v1.pdf

**Abstract**:
> arXiv:2603.16682v1 Announce Type: new 
Abstract: Understanding and manipulating timbre is central to audio synthesis, yet this remains under-explored in machine learning due to a lack of annotated datasets linking perceptual timbre dimensions to semantic descriptors. We present the Semantic Timbre Dataset, a curated collection of monophonic electric guitar sounds, each labeled with one of 19 semantic timbre descriptors and corresponding magnitudes. These descriptors were derived from a qualitative analysis of physical and virtual guitar effect units and applied systematically to clean guitar tones. The dataset bridges perceptual timbre and machine learning representations, supporting learning for timbre control and semantic audio generation. We validate the dataset by training a variationa...

---

## 5. Evaluating Latent Space Structure in Timbre VAEs: A Comparative Study of Unsupervised, Descriptor-Conditioned, and Perceptual Feature-Conditioned Models

**Authors**: Joseph Cameron, Alan Blackwell  
**Categories**: cs.SD  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16713  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16713v1.pdf

**Abstract**:
> arXiv:2603.16713v1 Announce Type: new 
Abstract: We present a comparative evaluation of latent space organization in three Variational Autoencoders (VAEs) for musical timbre generation: an unsupervised VAE, a descriptor-conditioned VAE, and a VAE conditioned on continuous perceptual features from the AudioCommons timbral models. Using a curated dataset of electric guitar sounds labeled with 19 semantic descriptors across four intensity levels, we assess each model's latent structure with a suite of clustering and interpretability metrics. These include silhouette scores, timbre descriptor compactness, pitch-conditional separation, trajectory linearity, and cross-pitch consistency. Our findings show that conditioning on perceptual features yields a more compact, discriminative, and pitch-in...

---

## 6. Making Separation-First Multi-Stream Audio Watermarking Feasible via Joint Training

**Authors**: Houmin Sun, Zi Hu, Linxi Li, Yechen Wang, Liwei Jin, Ming Li  
**Categories**: cs.SD  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16805  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16805v1.pdf

**Abstract**:
> arXiv:2603.16805v1 Announce Type: new 
Abstract: Modern audio is created by mixing stems from different sources, raising the question: can we independently watermark each stem and recover all watermarks after separation? We study a separation-first, multi-stream watermarking framework-embedding distinct information into stems using unique keys but a shared structure, mixing, separating, and decoding from each output. A naive pipeline (robust watermarking + off-the-shelf separation) yields poor bit recovery, showing robustness to generic distortions does not ensure robustness to separation artifacts. To enable this, we jointly train the watermark system and the separator in an end-to-end manner, encouraging the separator to preserve watermark cues while adapting embedding to separation-spec...

---

## 7. DASH: Dynamic Audio-Driven Semantic Chunking for Efficient Omnimodal Token Compression

**Authors**: Bingzhou Li, Tao Huang  
**Categories**: cs.SD  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15685  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15685v1.pdf

**Abstract**:
> arXiv:2603.15685v1 Announce Type: cross 
Abstract: Omnimodal large language models (OmniLLMs) jointly process audio and visual streams, but the resulting long multimodal token sequences make inference prohibitively expensive. Existing compression methods typically rely on fixed window partitioning and attention-based pruning, which overlook the piecewise semantic structure of audio-visual signals and become fragile under aggressive token reduction. We propose Dynamic Audio-driven Semantic cHunking (DASH), a training-free framework that aligns token compression with semantic structure. DASH treats audio embeddings as a semantic anchor and detects boundary candidates via cosine-similarity discontinuities, inducing dynamic, variable-length segments that approximate the underlying piecewise-co...

---

## 8. Towards the Vision-Sound-Language-Action Paradigm: The HEAR Framework for Sound-Centric Manipulation

**Authors**: Chang Nie, Tianchen Deng, Guangming Wang, Zhe Liu, Hesheng Wang  
**Categories**: cs.SD  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16086  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16086v1.pdf

**Abstract**:
> arXiv:2603.16086v1 Announce Type: cross 
Abstract: While recent Vision-Language-Action (VLA) models have begun to incorporate audio, they typically treat sound as static pre-execution prompts or focus exclusively on human speech. This leaves a significant gap in real-time, sound-centric manipulation where fleeting environmental acoustics provide critical state verification during task execution. Consequently, key sounds are easily missed due to low-frequency updates or system latency. This problem is exacerbated by action chunking with open-loop execution, which creates a Blind Execution Interval where acoustic events are lost between discrete audio observation windows. Recognizing the necessity of continuous auditory awareness, we formalize Vision-Sound-Language-Action (VSLA) as a continu...

---

## 9. Robust Generative Audio Quality Assessment: Disentangling Quality from Spurious Correlations

**Authors**: Kuan-Tang Huang, Chien-Chun Wang, Cheng-Yeh Yang, Hung-Shin Lee, Hsin-Min Wang, Berlin Chen  
**Categories**: cs.SD  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16201  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16201v1.pdf

**Abstract**:
> arXiv:2603.16201v1 Announce Type: cross 
Abstract: The rapid proliferation of AI-Generated Content (AIGC) has necessitated robust metrics for perceptual quality assessment. However, automatic Mean Opinion Score (MOS) prediction models are often compromised by data scarcity, predisposing them to learn spurious correlations-- such as dataset-specific acoustic signatures-- rather than generalized quality features. To address this, we leverage domain adversarial training (DAT) to disentangle true quality perception from these nuisance factors. Unlike prior works that rely on static domain priors, we systematically investigate domain definition strategies ranging from explicit metadata-driven labels to implicit data-driven clusters. Our findings reveal that there is no "one-size-fits-all" domai...

---

## 10. HRTF-guided Binaural Target Speaker Extraction with Real-World Validation

**Authors**: Yoav Ellinson, Sharon Gannot  
**Categories**: cs.SD  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16668  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16668v1.pdf

**Abstract**:
> arXiv:2603.16668v1 Announce Type: cross 
Abstract: This paper presents a Head-Related Transfer Function (HRTF)-guided framework for binaural Target Speaker Extraction (TSE) from mixtures of concurrent sources. Unlike conventional TSE methods based on Direction of Arrival (DOA) estimation or enrollment signals, which often distort perceived spatial location, the proposed approach leverages the listener's HRTF as an explicit spatial prior. The proposed framework is built upon a multi-channel deep blind source separation backbone, adapted to the binaural TSE setting. It is trained on measured HRTFs from a diverse population, enabling cross-listener generalization rather than subject-specific tuning. By conditioning the extraction on HRTF-derived spatial information, the method preserves binau...

---

## 11. When Silence Matters: The Impact of Irrelevant Audio on Text Reasoning in Large Audio-Language Models

**Authors**: Chen-An Li, Tzu-Han Lin, Hung-yi Lee  
**Categories**: cs.SD  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.00626  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.00626v2.pdf

**Abstract**:
> arXiv:2510.00626v2 Announce Type: replace 
Abstract: Large audio-language models (LALMs) unify speech and text processing, but their robustness in noisy real-world settings remains underexplored. We investigate how irrelevant audio, such as silence, synthetic noise, and environmental sounds, affects text reasoning tasks where audio is unnecessary. Across three text-based benchmarks, we find that even non-informative audio reduces accuracy and increases prediction volatility; the severity of interference scales with longer durations, higher amplitudes, and elevated decoding temperatures. Silence, often assumed neutral, destabilizes outputs as strongly as synthetic noise. While larger models show greater resilience, vulnerabilities persist across all evaluated systems. We further test mitiga...

---

## 12. Building Enterprise Realtime Voice Agents from Scratch: A Technical Tutorial

**Authors**: Jielin Qiu, Zixiang Chen, Liangwei Yang, Ming Zhu, Zhiwei Liu, Juntao Tan, Wenting Zhao, Rithesh Mur...  
**Categories**: cs.SD  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.05413  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.05413v2.pdf

**Abstract**:
> arXiv:2603.05413v2 Announce Type: replace 
Abstract: We present a technical tutorial for building enterprise-grade realtime voice agents from first principles. While end-to-end speech-to-speech models may ultimately provide the best latency for voice agents, fully self-hosted end-to-end solutions are not yet available. We evaluate the closest candidate, Qwen3-Omni, across three configurations: its cloud-only DashScope Realtime API achieves $\sim$702ms audio-to-audio latency with streaming, but is not self-hostable; its local vLLM deployment supports only the Thinker (text generation from audio, 516ms), not the Talker (audio synthesis); and its local Transformers deployment runs the full pipeline but at $\sim$146s -- far too slow for realtime. The cascaded streaming pipeline (STT $\rightarr...

---

## 13. LLM-Guided Reinforcement Learning for Audio-Visual Speech Enhancement

**Authors**: Chih-Ning Chen, Jen-Cheng Hou, Hsin-Min Wang, Shao-Yi Chien, Yu Tsao, Fan-Gang Zeng  
**Categories**: cs.SD  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13952  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13952v2.pdf

**Abstract**:
> arXiv:2603.13952v2 Announce Type: replace 
Abstract: In existing Audio-Visual Speech Enhancement (AVSE) methods, objectives such as Scale-Invariant Signal-to-Noise Ratio (SI-SNR) and Mean Squared Error (MSE) are widely used; however, they often correlate poorly with perceptual quality and provide limited interpretability for optimization. This work proposes a reinforcement learning-based AVSE framework with a Large Language Model (LLM)-based interpretable reward model. An audio LLM generates natural language descriptions of enhanced speech, which are converted by a sentiment analysis model into a 1-5 rating score serving as the PPO reward for fine-tuning a pretrained AVSE model. Compared with scalar metrics, LLM-generated feedback is semantically rich and explicitly describes improvements ...

---

## 14. VorTEX: Various overlap ratio for Target speech EXtraction

**Authors**: Ro-hoon Oh, Jihwan Seol, Bugeun Kim  
**Categories**: cs.SD  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14803  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14803v2.pdf

**Abstract**:
> arXiv:2603.14803v2 Announce Type: replace 
Abstract: Target speech extraction (TSE) aims to recover a target speaker's voice from a mixture. While recent text-prompted approaches have shown promise, most approaches assume fully overlapped mixtures, limiting insight into behavior across realistic overlap ratios. We introduce VorTEX (Various overlap ratio for Target speech EXtraction), a text-prompted TSE architecture with a Decoupled Adaptive Multi-branch (DAM) Fusion block that separates primary extraction from auxiliary regularization pathways. To enable controlled analysis, we construct PORTE, a two-speaker dataset spanning overlap ratios from 0% to 100%. We further propose Suppression Ratio on Energy (SuRE), a diagnostic metric that detects suppression behavior not captured by conventio...

---

## 15. Coherent Audio-Visual Editing via Conditional Audio Generation Following Video Edits

**Authors**: Masato Ishii, Akio Hayakawa, Takashi Shibuya, Yuki Mitsufuji  
**Categories**: cs.SD  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2512.07209  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2512.07209v2.pdf

**Abstract**:
> arXiv:2512.07209v2 Announce Type: replace-cross 
Abstract: We introduce a novel pipeline for joint audio-visual editing that enhances the coherence between edited video and its accompanying audio. Our approach first applies state-of-the-art video editing techniques to produce the target video, then performs audio editing to align with the visual changes. To achieve this, we present a new video-to-audio generation model that conditions on the source audio, target video, and a text prompt. We extend the model architecture to incorporate conditional audio input and propose a data augmentation strategy that improves training efficiency. Furthermore, our model dynamically adjusts the influence of the source audio based on the complexity of the edits, preserving the original audio structure wher...

---

## 16. Mathematical Foundations of Polyphonic Music Generation via Structural Inductive Bias

**Authors**: Joonwon Seo  
**Categories**: cs.SD  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2601.03612  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2601.03612v5.pdf

**Abstract**:
> arXiv:2601.03612v5 Announce Type: replace-cross 
Abstract: This monograph introduces a novel approach to polyphonic music generation by addressing the "Missing Middle" problem through structural inductive bias. Focusing on Beethoven's piano sonatas as a case study, we empirically verify the independence of pitch and hand attributes using normalized mutual information (NMI=0.167) and propose the Smart Embedding architecture, achieving a 48.30% reduction in parameters. We provide rigorous mathematical proofs using information theory (negligible loss bounded at 0.153 bits), Rademacher complexity (28.09% tighter generalization bound), and category theory to demonstrate improved stability and generalization. Empirical results show a 9.47% reduction in validation loss, confirmed by SVD analysis ...

---

## 17. Something from Nothing: Data Augmentation for Robust Severity Level Estimation of Dysarthric Speech

**Authors**: Jaesung Bae, Xiuwen Zheng, Minje Kim, Chang D. Yoo, Mark Hasegawa-Johnson  
**Categories**: eess.AS  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15988  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15988v1.pdf

**Abstract**:
> arXiv:2603.15988v1 Announce Type: new 
Abstract: Dysarthric speech quality assessment (DSQA) is critical for clinical diagnostics and inclusive speech technologies. However, subjective evaluation is costly and difficult to scale, and the scarcity of labeled data limits robust objective modeling. To address this, we propose a three-stage framework that leverages unlabeled dysarthric speech and large-scale typical speech datasets to scale training. A teacher model first generates pseudo-labels for unlabeled samples, followed by weakly supervised pretraining using a label-aware contrastive learning strategy that exposes the model to diverse speakers and acoustic conditions. The pretrained model is then fine-tuned for the downstream DSQA task. Experiments on five unseen datasets spanning multi...

---

## 18. AILive Mixer: A Deep Learning based Zero Latency Automatic Music Mixer for Live Music Performances

**Authors**: Devansh Zurale, Iris Lorente, Michael Lester, Alex Mitchell  
**Categories**: eess.AS  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15995  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15995v1.pdf

**Abstract**:
> arXiv:2603.15995v1 Announce Type: new 
Abstract: In this work, we present a deep learning-based automatic multitrack music mixing system catered towards live performances. In a live performance, channels are often corrupted with acoustic bleeds of co-located instruments. Moreover, audio-visual synchronization is of critical importance thus putting a tight constraint on the audio latency. In this work we primarily tackle these two challenges of handling bleeds in the input channels to produce the music mix with zero latency. Although there have been several developments in the field of automatic music mixing in recent times, most or all previous works focus on offline production for isolated instrument signals and to the best of our knowledge, this is the first end-to-end deep learning syst...

---

## 19. Tokenization Tradeoffs in Structured EHR Foundation Models

**Authors**: Lin Lawrence Guo, Santiago Eduardo Arciniegas, Joseph Jihyung Lee, Adam Paul Yan, George Tomlinson, ...  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15644  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15644v1.pdf

**Abstract**:
> arXiv:2603.15644v1 Announce Type: new 
Abstract: Foundation models for structured electronic health records (EHRs) are pretrained on longitudinal sequences of timestamped clinical events to learn adaptable patient representations. Tokenization -- how these timelines are converted into discrete model inputs -- determines what information is preserved, how efficiently it is encoded, and which relationships must be learned versus precomputed. Yet the impact of tokenization design choices on downstream performance and computational efficiency remains largely unexplored. Here, we pretrained a transformer on pediatric EHR data under a factorial design, varying tokenization along event encoding, time encoding, and workflow annotation. We evaluated area-under-the-receiver-operating-characteristic ...

---

## 20. How to Achieve Prototypical Birth and Death for OOD Detection?

**Authors**: Ningkang Peng, Qianfeng Yu, Xiaoqian Peng, Linjing Qian, Yafei Liu, Canran Xiao, Xinyu Lu, Tingyu Lu...  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15650  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15650v1.pdf

**Abstract**:
> arXiv:2603.15650v1 Announce Type: new 
Abstract: Out-of-Distribution (OOD) detection is crucial for the secure deployment of machine learning models, and prototype-based learning methods are among the mainstream strategies for achieving OOD detection. Existing prototype-based learning methods generally rely on a fixed number of prototypes. This static assumption fails to adapt to the inherent complexity differences across various categories. Currently, there is still a lack of a mechanism that can adaptively adjust the number of prototypes based on data complexity. Inspired by the processes of cell birth and death in biology, we propose a novel method named PID (Prototype bIrth and Death) to adaptively adjust the prototype count based on data complexity. This method relies on two dynamic m...

---

## 21. Beyond Reward Suppression: Reshaping Steganographic Communication Protocols in MARL via Dynamic Representational Circuit Breaking

**Authors**: Liu Hung Ming  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15655  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15655v1.pdf

**Abstract**:
> arXiv:2603.15655v1 Announce Type: new 
Abstract: In decentralized Multi-Agent Reinforcement Learning (MARL), steganographic collusion -- where agents develop private protocols to evade monitoring -- presents a critical AI safety threat. Existing defenses, limited to behavioral or reward layers, fail to detect coordination in latent communication channels. We introduce the Dynamic Representational Circuit Breaker (DRCB), an architectural defense operating at the optimization substrate.
  Building on the AI Mother Tongue (AIM) framework, DRCB utilizes a Vector Quantized Variational Autoencoder (VQ-VAE) bottleneck to convert unobservable messages into auditable statistical objects. DRCB monitors signals including Jensen-Shannon Divergence drift, L2-norm codebook displacement, and Randomized O...

---

## 22. Tackling Over-smoothing on Hypergraphs: A Ricci Flow-guided Neural Diffusion Approach

**Authors**: Mengyao Zhou, Zhiheng Zhou, Xiao Han, Xingqin Qi, Guanghui Wang, Guiying Yan  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15696  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15696v1.pdf

**Abstract**:
> arXiv:2603.15696v1 Announce Type: new 
Abstract: Hypergraph neural networks (HGNNs) have demonstrated strong capabilities in modeling complex higher-order relationships. However, existing HGNNs often suffer from over-smoothing as the number of layers increases and lack effective control over message passing among nodes. Inspired by the theory of Ricci flow in differential geometry, we theoretically establish that introducing discrete Ricci flow into hypergraph structures can effectively regulate node feature evolution and thereby alleviate over-smoothing. Building on this insight, we propose Ricci Flow-guided Hypergraph Neural Diffusion(RFHND), a novel message passing paradigm for hypergraphs guided by discrete Ricci flow. Specifically, RFHND is based on a PDE system that describes the con...

---

## 23. Embedding-Aware Feature Discovery: Bridging Latent Representations and Interpretable Features in Event Sequences

**Authors**: Artem Sakhno, Ivan Sergeev, Alexey Shestov, Omar Zoloev, Elizaveta Kovtun, Gleb Gusev, Andrey Savche...  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15713  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15713v1.pdf

**Abstract**:
> arXiv:2603.15713v1 Announce Type: new 
Abstract: Industrial financial systems operate on temporal event sequences such as transactions, user actions, and system logs. While recent research emphasizes representation learning and large language models, production systems continue to rely heavily on handcrafted statistical features due to their interpretability, robustness under limited supervision, and strict latency constraints. This creates a persistent disconnect between learned embeddings and feature-based pipelines. We introduce Embedding-Aware Feature Discovery (EAFD), a unified framework that bridges this gap by coupling pretrained event-sequence embeddings with a self-reflective LLM-driven feature generation agent. EAFD iteratively discovers, evaluates, and refines features directly ...

---

## 24. Time-Aware Prior Fitted Networks for Zero-Shot Forecasting with Exogenous Variables

**Authors**: Andres Potapczynski, Ravi Kiran Selvam, Tatiana Konstantinova, Shankar Ramasubramanian, Malcolm Wolf...  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15802  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15802v1.pdf

**Abstract**:
> arXiv:2603.15802v1 Announce Type: new 
Abstract: In many time series forecasting settings, the target time series is accompanied by exogenous covariates, such as promotions and prices in retail demand; temperature in energy load; calendar and holiday indicators for traffic or sales; and grid load or fuel costs in electricity pricing. Ignoring these exogenous signals can substantially degrade forecasting accuracy, particularly when they drive spikes, discontinuities, or regime and phase changes in the target series. Most current time series foundation models (e.g., Chronos, Sundial, TimesFM, TimeMoE, TimeLLM, and LagLlama) ignore exogenous covariates and make forecasts solely from the numerical time series history, thereby limiting their performance. In this paper, we develop ApolloPFN, a p...

---

## 25. Informationally Compressive Anonymization: Non-Degrading Sensitive Input Protection for Privacy-Preserving Supervised Machine Learning

**Authors**: Jeremy J Samuelson  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15842  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15842v1.pdf

**Abstract**:
> arXiv:2603.15842v1 Announce Type: new 
Abstract: Modern machine learning systems increasingly rely on sensitive data, creating significant privacy, security, and regulatory risks that existing privacy-preserving machine learning (ppML) techniques, such as Differential Privacy (DP) and Homomorphic Encryption (HE), address only at the cost of degraded performance, increased complexity, or prohibitive computational overhead. This paper introduces Informationally Compressive Anonymization (ICA) and the VEIL architecture, a privacy-preserving ML framework that achieves strong privacy guarantees through architectural and mathematical design rather than noise injection or cryptography. ICA embeds a supervised, multi-objective encoder within a trusted Source Environment to transform raw inputs int...

---

## 26. Counteractive RL: Rethinking Core Principles for Efficient and Scalable Deep Reinforcement Learning

**Authors**: Ezgi Korkmaz  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15871  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15871v1.pdf

**Abstract**:
> arXiv:2603.15871v1 Announce Type: new 
Abstract: Following the pivotal success of learning strategies to win at tasks, solely by interacting with an environment without any supervision, agents have gained the ability to make sequential decisions in complex MDPs. Yet, reinforcement learning policies face exponentially growing state spaces in high dimensional MDPs resulting in a dichotomy between computational complexity and policy success. In our paper we focus on the agent's interaction with the environment in a high-dimensional MDP during the learning phase and we introduce a theoretically-founded novel paradigm based on experiences obtained through counteractive actions. Our analysis and method provide a theoretical basis for efficient, effective, scalable and accelerated learning, and f...

---

## 27. Data-Local Autonomous LLM-Guided Neural Architecture Search for Multiclass Multimodal Time-Series Classification

**Authors**: Emil Hardarson, Luka Biedebach, \'Omar Bessi \'Omarsson, Teitur Hr\'olfsson, Anna Sigridur Islind, M...  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15939  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15939v1.pdf

**Abstract**:
> arXiv:2603.15939v1 Announce Type: new 
Abstract: Applying machine learning to sensitive time-series data is often bottlenecked by the iteration loop: Performance depends strongly on preprocessing and architecture, yet training often has to run on-premise under strict data-local constraints. This is a common problem in healthcare and other privacy-constrained domains (e.g., a hospital developing deep learning models on patient EEG). This bottleneck is particularly challenging in multimodal fusion, where sensor modalities must be individually preprocessed and then combined. LLM-guided neural architecture search (NAS) can automate this exploration, but most existing workflows assume cloud execution or access to data-derived artifacts that cannot be exposed.
  We present a novel data-local, LL...

---

## 28. Determinism in the Undetermined: Deterministic Output in Charge-Conserving Continuous-Time Neuromorphic Systems with Temporal Stochasticity

**Authors**: Jing Yan, Kang You, Zhezhi He, Yaoyu Zhang  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15987  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15987v1.pdf

**Abstract**:
> arXiv:2603.15987v1 Announce Type: new 
Abstract: Achieving deterministic computation results in asynchronous neuromorphic systems remains a fundamental challenge due to the inherent temporal stochasticity of continuous-time hardware. To address this, we develop a unified continuous-time framework for spiking neural networks (SNNs) that couples the Law of Charge Conservation with minimal neuron-level constraints. This integration ensures that the terminal state depends solely on the aggregate input charge, providing a unique cumulated output invariant to temporal stochasticity. We prove that this mapping is strictly invariant to spike timing in acyclic networks, whereas recurrent connectivity can introduce temporal sensitivity. Furthermore, we establish an exact representational corresponde...

---

## 29. W2T: LoRA Weights Already Know What They Can Do

**Authors**: Xiaolong Han, Ferrante Neri, Zijian Jiang, Fang Wu, Yanfang Ye, Lu Yin, Zehong Wang  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15990  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15990v1.pdf

**Abstract**:
> arXiv:2603.15990v1 Announce Type: new 
Abstract: Each LoRA checkpoint compactly stores task-specific updates in low-rank weight matrices, offering an efficient way to adapt large language models to new tasks and domains. In principle, these weights already encode what the adapter does and how well it performs. In this paper, we ask whether this information can be read directly from the weights, without running the base model or accessing training data. A key obstacle is that a single LoRA update can be factorized in infinitely many ways. Without resolving this ambiguity, models trained on the factors may fit the particular factorization rather than the underlying update. To this end, we propose \methodfull, which maps each LoRA update to a provably canonical form via QR decomposition follo...

---

## 30. Residual Stream Duality in Modern Transformer Architectures

**Authors**: Yifan Zhang  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16039  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16039v1.pdf

**Abstract**:
> arXiv:2603.16039v1 Announce Type: new 
Abstract: Recent work has made clear that the residual pathway is not mere optimization plumbing; it is part of the model's representational machinery. We agree, but argue that the cleanest way to organize this design space is through a two-axis view of the Transformer. A decoder evolves information along two ordered dimensions: sequence position and layer depth. Self-attention already provides adaptive mixing along the sequence axis, whereas the residual stream usually performs fixed addition along the depth axis. If we fix a token position and treat layer index as the ordered variable, then a causal depth-wise residual attention read is exactly the same local operator as causal short sliding-window attention (ShortSWA), except written over depth rat...

---

## 31. Execution-Grounded Credit Assignment for GRPO in Code Generation

**Authors**: Abhijit Kumar, Natalya Kumar, Shikhar Gupta  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16158  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16158v1.pdf

**Abstract**:
> arXiv:2603.16158v1 Announce Type: new 
Abstract: Critic-free reinforcement learning with verifiable rewards (RLVR) improves code generation by optimizing unit-test pass rates, but GRPO-style updates suffer from coarse credit assignment: a single outcome signal is spread uniformly across long programs even when failure stems from a localized semantic error. We propose Execution-Grounded Credit Assignment (EGCA), which localizes GRPO updates using execution traces. For programs that satisfy algorithmic constraints but fail tests, EGCA executes the candidate and a canonical reference solution (curated once offline; used for analysis, not supervision) under identical instrumentation, identifies the earliest semantic divergence, and assigns advantage only to the corresponding token span while m...

---

## 32. The Finetuner's Fallacy: When to Pretrain with Your Finetuning Data

**Authors**: Christina Baek, Ricardo Pio Monti, David Schwab, Amro Abbas, Rishabh Adiga, Cody Blakeney, Maximilia...  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16177  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16177v1.pdf

**Abstract**:
> arXiv:2603.16177v1 Announce Type: new 
Abstract: Real-world model deployments demand strong performance on narrow domains where data is often scarce. Typically, practitioners finetune models to specialize them, but this risks overfitting to the domain and forgetting general knowledge. We study a simple strategy, specialized pretraining (SPT), where a small domain dataset, typically reserved for finetuning, is repeated starting from pretraining as a fraction of the total tokens. Across three specialized domains (ChemPile, MusicPile, and ProofPile), SPT improves domain performance and preserves general capabilities after finetuning compared to standard pretraining. In our experiments, SPT reduces the pretraining tokens needed to reach a given domain performance by up to 1.75x. These gains gr...

---

## 33. Sample-Efficient Adaptation of Drug-Response Models to Patient Tumors under Strong Biological Domain Shift

**Authors**: Camille Jimenez Cortes, Philippe Lalanda, German Vega  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16185  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16185v1.pdf

**Abstract**:
> arXiv:2603.16185v1 Announce Type: new 
Abstract: Predicting drug response in patients from preclinical data remains a major challenge in precision oncology due to the substantial biological gap between in vitro cell lines and patient tumors. Rather than aiming to improve absolute in vitro prediction accuracy, this work examines whether explicitly separating representation learning from task supervision enables more sample-efficient adaptation of drug-response models to patient data under strong biological domain shift. We propose a staged transfer-learning framework in which cellular and drug representations are first learned independently from large collections of unlabeled pharmacogenomic data using autoencoder-based representation learning. These representations are then aligned with dr...

---

## 34. Dual Consensus: Escaping from Spurious Majority in Unsupervised RLVR via Two-Stage Vote Mechanism

**Authors**: Kaixuan Du, Meng Cao, Hang Zhang, Yukun Wang, Xiangzhou Huang, Ni Li  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16223  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16223v1.pdf

**Abstract**:
> arXiv:2603.16223v1 Announce Type: new 
Abstract: Current label-free RLVR approaches for large language models (LLMs), such as TTRL and Self-reward, have demonstrated effectiveness in improving the performance of LLMs on complex reasoning tasks. However, these methods rely heavily on accurate pseudo-label estimation and converge on spurious yet popular answers, thereby trapping in a dominant mode and limiting further improvements. Building on this, we propose Dual Consensus Reinforcement Learning (DCRL), a novel self-supervised training method which is capable of generating more reliable learning signals through a two-stage consensus mechanism. The model initially acts as an anchor, producing dominant responses; then it serves as an explorer, generating diverse auxiliary signals via a tempo...

---

## 35. Physics-integrated neural differentiable modeling for immersed boundary systems

**Authors**: Chenglin Li, Hang Xu, Jianting Chen, Yanfei Zhang  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16277  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16277v1.pdf

**Abstract**:
> arXiv:2603.16277v1 Announce Type: new 
Abstract: Accurately, efficiently, and stably computing complex fluid flows and their evolution near solid boundaries over long horizons remains challenging. Conventional numerical solvers require fine grids and small time steps to resolve near-wall dynamics, resulting in high computational costs, while purely data-driven surrogate models accumulate rollout errors and lack robustness under extrapolative conditions. To address these issues, this study extends existing neural PDE solvers by developing a physics-integrated differentiable framework for long-horizon prediction of immersed-boundary flows. A key design aspect of the framework includes an important improvement, namely the structural integration of physical principles into an end-to-end differ...

---

## 36. Laya: A LeJEPA Approach to EEG via Latent Prediction over Reconstruction

**Authors**: Saarang Panchavati, Uddhav Panchavati, Corey Arnold, William Speier  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16281  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16281v1.pdf

**Abstract**:
> arXiv:2603.16281v1 Announce Type: new 
Abstract: Electroencephalography (EEG) is a widely used tool for studying brain function, with applications in clinical neuroscience, diagnosis, and brain-computer interfaces (BCIs). Recent EEG foundation models trained on large unlabeled corpora aim to learn transferable representations, but their effectiveness remains unclear; reported improvements over smaller task-specific models are often modest, sensitive to downstream adaptation and fine-tuning strategies, and limited under linear probing. We hypothesize that one contributing factor is the reliance on signal reconstruction as the primary self-supervised learning (SSL) objective, which biases representations toward high-variance artifacts rather than task-relevant neural structure. To address th...

---

## 37. Decoding the Critique Mechanism in Large Reasoning Models

**Authors**: Hoang Phan, Quang H. Nguyen, Hung T. Q. Le, Xiusi Chen, Heng Ji, Khoa D. Doan  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16331  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16331v1.pdf

**Abstract**:
> arXiv:2603.16331v1 Announce Type: new 
Abstract: Large Reasoning Models (LRMs) exhibit backtracking and self-verification mechanisms that enable them to revise intermediate steps and reach correct solutions, yielding strong performance on complex logical benchmarks. We hypothesize that such behaviors are beneficial only when the model has sufficiently strong "critique" ability to detect its own mistakes. This work systematically investigates how current LRMs recover from errors by inserting arithmetic mistakes in their intermediate reasoning steps. Notably, we discover a peculiar yet important phenomenon: despite the error propagating through the chain-of-thought (CoT), resulting in an incorrect intermediate conclusion, the model still reaches the correct final answer. This recovery implie...

---

## 38. DynamicGate MLP Conditional Computation via Learned Structural Dropout and Input Dependent Gating for Functional Plasticity

**Authors**: Yong Il Choi  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16367  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16367v1.pdf

**Abstract**:
> arXiv:2603.16367v1 Announce Type: new 
Abstract: Dropout is a representative regularization technique that stochastically deactivates hidden units during training to mitigate overfitting. In contrast, standard inference executes the full network with dense computation, so its goal and mechanism differ from conditional computation, where the executed operations depend on the input. This paper organizes DynamicGate-MLP into a single framework that simultaneously satisfies both the regularization view and the conditional-computation view. Instead of a random mask, the proposed model learns gates that decide whether to use each unit (or block), suppressing unnecessary computation while implementing sample-dependent execution that concentrates computation on the parts needed for each input. To ...

---

## 39. FederatedFactory: Generative One-Shot Learning for Extremely Non-IID Distributed Scenarios

**Authors**: Andrea Moleri, Christian Intern\`o, Ali Raza, Markus Olhofer, David Klindt, Fabio Stella, Barbara Ha...  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16370  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16370v1.pdf

**Abstract**:
> arXiv:2603.16370v1 Announce Type: new 
Abstract: Federated Learning (FL) enables distributed optimization without compromising data sovereignty. Yet, where local label distributions are mutually exclusive, standard weight aggregation fails due to conflicting optimization trajectories. Often, FL methods rely on pretrained foundation models, introducing unrealistic assumptions. We introduce FederatedFactory, a zero-dependency framework that inverts the unit of federation from discriminative parameters to generative priors. By exchanging generative modules in a single communication round, our architecture supports ex nihilo synthesis of universally class balanced datasets, eliminating gradient conflict and external prior bias entirely. Evaluations across diverse medical imagery benchmarks, in...

---

## 40. Age Predictors Through the Lens of Generalization, Bias Mitigation, and Interpretability: Reflections on Causal Implications

**Authors**: Debdas Paul, Elisa Ferrari, Irene Gravili, Alessandro Cellerino  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16377  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16377v1.pdf

**Abstract**:
> arXiv:2603.16377v1 Announce Type: new 
Abstract: Chronological age predictors often fail to achieve out-of-distribution (OOD) gen- eralization due to exogenous attributes such as race, gender, or tissue. Learning an invariant representation with respect to those attributes is therefore essential to improve OOD generalization and prevent overly optimistic results. In predic- tive settings, these attributes motivate bias mitigation; in causal analyses, they appear as confounders; and when protected, their suppression leads to fairness. We coherently explore these concepts with theoretical rigor and discuss the scope of an interpretable neural network model based on adversarial representation learning. Using publicly available mouse transcriptomic datasets, we illustrate the behavior of this ...

---

## 41. Trained Persistent Memory for Frozen Encoder--Decoder LLMs: Six Architectural Methods

**Authors**: Hong Jeong  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16413  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16413v1.pdf

**Abstract**:
> arXiv:2603.16413v1 Announce Type: new 
Abstract: Frozen encoder--decoder language models are stateless: the latent representation is discarded after every forward pass, so no information persists across sessions. This paper presents a \textbf{proof-of-concept pilot study} showing that persistent memory in the \emph{continuous latent space} of a frozen LLM is feasible -- even under severe resource constraints (a single frozen Flan-T5-XL backbone, small trainable adapters, a single dataset). We implement six architectural methods spanning three injection points and four write mechanisms; unlike text-level memory systems, every write and read is a differentiable operation on dense vectors. After training only the adapter, the memory bank continues to accumulate at inference time without gradi...

---

## 42. Capability-Guided Compression: Toward Interpretability-Aware Budget Allocation for Large Language Models

**Authors**: Rishaank Gupta  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16440  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16440v1.pdf

**Abstract**:
> arXiv:2603.16440v1 Announce Type: new 
Abstract: Large language model compression has made substantial progress through pruning, quantization, and low-rank decomposition, yet a fundamental limitation persists across all existing methods: compression budgets are allocated without any representation of what individual model components functionally encode. We term this the capability-blind compression problem and argue it is a root cause of two well-documented failures -- the insensitivity of perplexity-based evaluation to reasoning capability loss, and the abrupt phase transitions in model performance recently characterized by Ma et al. (2026). We propose Capability-Guided Compression (CGC), a framework that addresses this by using Sparse Autoencoder (SAE)-derived capability density maps to ...

---

## 43. FEAT: A Linear-Complexity Foundation Model for Extremely Large Structured Data

**Authors**: Zhenghang Song, Tang Qian, Lu Chen, Yushuai Li, Zhengke Hu, Bingbing Fang, Yumeng Song, Junbo Zhao, ...  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16513  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16513v1.pdf

**Abstract**:
> arXiv:2603.16513v1 Announce Type: new 
Abstract: Structured data is foundational to healthcare, finance, e-commerce, and scientific data management. Large structured-data models (LDMs) extend the foundation model paradigm to unify heterogeneous datasets for tasks such as classification, regression, and decision support. However, existing LDMs face major limitations. First, most rely on sample-wise self-attention, whose O(N^2) complexity limits the sample count. Second, linear sequence models often degrade representations due to hidden-state compression and artificial causal bias. Third, synthetic-only pre-training often fails to match real-world distributions. We propose FEAT, a linear-complexity foundation model for extremely large structured data. FEAT introduces a multi-layer dual-axis ...

---

## 44. Manifold-Matching Autoencoders

**Authors**: Laurent Cheret, Vincent L\'etourneau, Isar Nejadgholi, Chris Drummond, Hussein Al Osman, Maia Fraser  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16568  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16568v1.pdf

**Abstract**:
> arXiv:2603.16568v1 Announce Type: new 
Abstract: We study a simple unsupervised regularization scheme for autoencoders called Manifold-Matching (MMAE): we align the pairwise distances in the latent space to those of the input data space by minimizing mean squared error. Because alignment occurs on pairwise distances rather than coordinates, it can also be extended to a lower-dimensional representation of the data, adding flexibility to the method. We find that this regularization outperforms similar methods on metrics based on preservation of nearest-neighbor distances and persistent homology-based measures. We also observe that MMAE provides a scalable approximation of Multi-Dimensional Scaling (MDS).

---

## 45. Deep Tabular Representation Corrector

**Authors**: Hangting Ye, Peng Wang, Wei Fan, Xiaozhuang Song, He Zhao, Dandan Gun, Yi Chang  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16569  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16569v1.pdf

**Abstract**:
> arXiv:2603.16569v1 Announce Type: new 
Abstract: Tabular data have been playing a mostly important role in diverse real-world fields, such as healthcare, engineering, finance, etc. The recent success of deep learning has fostered many deep networks (e.g., Transformer, ResNet) based tabular learning methods. Generally, existing deep tabular machine learning methods are along with the two paradigms, i.e., in-learning and pre-learning. In-learning methods need to train networks from scratch or impose extra constraints to regulate the representations which nonetheless train multiple tasks simultaneously and make learning more difficult, while pre-learning methods design several pretext tasks for pre-training and then conduct task-specific fine-tuning, which however need much extra training eff...

---

## 46. Simplex-to-Euclidean Bijection for Conjugate and Calibrated Multiclass Gaussian Process

**Authors**: Bernardo Williams, Harsha Vardhan Tetali, Arto Klami, Marcelo Hartmann  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16621  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16621v1.pdf

**Abstract**:
> arXiv:2603.16621v1 Announce Type: new 
Abstract: We propose a conjugate and calibrated Gaussian process (GP) model for multi-class classification by exploiting the geometry of the probability simplex. Our approach uses Aitchison geometry to map simplex-valued class probabilities to an unconstrained Euclidean representation, turning classification into a GP regression problem with fewer latent dimensions than standard multi-class GP classifiers. This yields conjugate inference and reliable predictive probabilities without relying on distributional approximations in the model construction. The method is compatible with standard sparse GP regression techniques, enabling scalable inference on larger datasets. Empirical results show well-calibrated and competitive performance across synthetic a...

---

## 47. Grid-World Representations in Transformers Reflect Predictive Geometry

**Authors**: Sasha Brenner, Thomas R. Kn\"osche, Nico Scherf  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16689  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16689v1.pdf

**Abstract**:
> arXiv:2603.16689v1 Announce Type: new 
Abstract: Next-token predictors often appear to develop internal representations of the latent world and its rules. The probabilistic nature of these models suggests a deep connection between the structure of the world and the geometry of probability distributions. In order to understand this link more precisely, we use a minimal stochastic process as a controlled setting: constrained random walks on a two-dimensional lattice that must reach a fixed endpoint after a predetermined number of steps. Optimal prediction of this process solely depends on a sufficient vector determined by the walker's position relative to the target and the remaining time horizon; in other words, the probability distributions are parametrized by the world's geometry. We trai...

---

## 48. Novelty-Driven Target-Space Discovery in Automated Electron and Scanning Probe Microscopy

**Authors**: Utkarsh Pratiush, Kamyar Barakati, Boris N. Slautin, Catherine C. Bodinger, Christopher D. Lowe, Bra...  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16715  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16715v1.pdf

**Abstract**:
> arXiv:2603.16715v1 Announce Type: new 
Abstract: Modern automated microscopy faces a fundamental discovery challenge: in many systems, the most important scientific information does not reside in the immediately visible image features, but in the target space of sequentially acquired spectra or functional responses, making it essential to develop strategies that can actively search for new behaviors rather than simply optimize known objectives. Here, we developed a deep-kernel-learning BEACON framework that is explicitly designed to guide discovery in the target space by learning structure-property relationships during the experiment and using that evolving model to seek diverse response regimes. We first established the method through demonstration workflows built on pre-acquired ground-t...

---

## 49. SpecMoE: Spectral Mixture-of-Experts Foundation Model for Cross-Species EEG Decoding

**Authors**: D. Darankoum, C. Habermacher, J. Volle, S. Grudinin  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16739  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16739v1.pdf

**Abstract**:
> arXiv:2603.16739v1 Announce Type: new 
Abstract: Decoding the orchestration of neural activity in electroencephalography (EEG) signals is a central challenge in bridging neuroscience with artificial intelligence. Foundation models have made strides in generalized EEG decoding, yet many existing frameworks primarily relying on separate temporal and spectral masking of raw signals during self-supervised pretraining. Such strategies often tend to bias learning toward high-frequency oscillations, as low-frequency rhythmic patterns can be easily inferred from the unmasked signal. We introduce a foundation model that utilizes a novel Gaussian-smoothed masking scheme applied to short-time Fourier transform (STFT) maps. By jointly applying time, frequency, and time-frequency Gaussian masks, we mak...

---

## 50. pADAM: A Plug-and-Play All-in-One Diffusion Architecture for Multi-Physics Learning

**Authors**: Amirhossein Mollaali, Bongseok Kim, Christian Moya, Guang Lin  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16757  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16757v1.pdf

**Abstract**:
> arXiv:2603.16757v1 Announce Type: new 
Abstract: Generalizing across disparate physical laws remains a fundamental challenge for artificial intelligence in science. Existing deep-learning solvers are largely confined to single-equation settings, limiting transfer across physical regimes and inference tasks. Here we introduce pADAM, a unified generative framework that learns a shared probabilistic prior across heterogeneous partial differential equation families. Through a learned joint distribution of system states and, where applicable, physical parameters, pADAM supports forward prediction and inverse inference within a single architecture without retraining. Across benchmarks ranging from scalar diffusion to nonlinear Navier--Stokes equations, pADAM achieves accurate inference even unde...

---

## 51. Improving Generative Adversarial Network Generalization for Facial Expression Synthesis

**Authors**: Arbish Akram, Nazar Khan, Arif Mahmood  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15648  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15648v1.pdf

**Abstract**:
> arXiv:2603.15648v1 Announce Type: cross 
Abstract: Facial expression synthesis aims to generate realistic facial expressions while preserving identity. Existing conditional generative adversarial networks (GANs) achieve excellent image-to-image translation results, but their performance often degrades when test images differ from the training dataset. We present Regression GAN (RegGAN), a model that learns an intermediate representation to improve generalization beyond the training distribution. RegGAN consists of two components: a regression layer with local receptive fields that learns expression details by minimizing the reconstruction error through a ridge regression loss, and a refinement network trained adversarially to enhance the realism of generated images. We train RegGAN on the ...

---

## 52. I Know What I Don't Know: Latent Posterior Factor Models for Multi-Evidence Probabilistic Reasoning

**Authors**: Aliyu Agboola Alege  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15670  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15670v1.pdf

**Abstract**:
> arXiv:2603.15670v1 Announce Type: cross 
Abstract: Real-world decision-making, from tax compliance assessment to medical diagnosis, requires aggregating multiple noisy and potentially contradictory evidence sources. Existing approaches either lack explicit uncertainty quantification (neural aggregation methods) or rely on manually engineered discrete predicates (probabilistic logic frameworks), limiting scalability to unstructured data.
  We introduce Latent Posterior Factors (LPF), a framework that transforms Variational Autoencoder (VAE) latent posteriors into soft likelihood factors for Sum-Product Network (SPN) inference, enabling tractable probabilistic reasoning over unstructured evidence while preserving calibrated uncertainty estimates. We instantiate LPF as LPF-SPN (structured fac...

---

## 53. FEEL (Force-Enhanced Egocentric Learning): A Dataset for Physical Action Understanding

**Authors**: Eadom Dessalene, Botao He, Michael Maynord, Yonatan Tussa, Pavan Mantripragada, Yianni Karabati, Nir...  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15847  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15847v1.pdf

**Abstract**:
> arXiv:2603.15847v1 Announce Type: cross 
Abstract: We introduce FEEL (Force-Enhanced Egocentric Learning), the first large-scale dataset pairing force measurements gathered from custom piezoresistive gloves with egocentric video. Our gloves enable scalable data collection, and FEEL contains approximately 3 million force-synchronized frames of natural unscripted manipulation in kitchen environments, with 45% of frames involving hand-object contact. Because force is the underlying cause that drives physical interaction, it is a critical primitive for physical action understanding. We demonstrate the utility of force for physical action understanding through application of FEEL to two families of tasks: (1) contact understanding, where we jointly perform temporal contact segmentation and pixe...

---

## 54. Regularized Latent Dynamics Prediction is a Strong Baseline For Behavioral Foundation Models

**Authors**: Pranaya Jajoo, Harshit Sikchi, Siddhant Agarwal, Amy Zhang, Scott Niekum, Martha White  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15857  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15857v1.pdf

**Abstract**:
> arXiv:2603.15857v1 Announce Type: cross 
Abstract: Behavioral Foundation Models (BFMs) produce agents with the capability to adapt to any unknown reward or task. These methods, however, are only able to produce near-optimal policies for the reward functions that are in the span of some pre-existing state features, making the choice of state features crucial to the expressivity of the BFM. As a result, BFMs are trained using a variety of complex objectives and require sufficient dataset coverage, to train task-useful spanning features. In this work, we examine the question: are these complex representation learning objectives necessary for zero-shot RL? Specifically, we revisit the objective of self-supervised next-state prediction in latent space for state feature learning, but observe tha...

---

## 55. Self-supervised Disentanglement of Disease Effects from Aging in 3D Medical Shapes

**Authors**: Jakaria Rabbi, Nilanjan Ray, Dana Cobzas  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15862  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15862v1.pdf

**Abstract**:
> arXiv:2603.15862v1 Announce Type: cross 
Abstract: Disentangling pathological changes from physiological aging in 3D medical shapes is crucial for developing interpretable biomarkers and patient stratification. However, this separation is challenging when diagnosis labels are limited or unavailable, since disease and aging often produce overlapping effects on shape changes, obscuring clinically relevant shape patterns. To address this challenge, we propose a two-stage framework combining unsupervised disease discovery with self-supervised disentanglement of implicit shape representations. In the first stage, we train an implicit neural model with signed distance functions to learn stable shape embeddings. We then apply clustering on the shape latent space, which yields pseudo disease label...

---

## 56. Neural Pushforward Samplers for the Fokker-Planck Equation on Embedded Riemannian Manifolds

**Authors**: Andrew Qing He, Wei Cai  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16239  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16239v1.pdf

**Abstract**:
> arXiv:2603.16239v1 Announce Type: cross 
Abstract: We extend the Weak Adversarial Neural Pushforward (WANPF) Method to the Fokker--Planck equation posed on a compact, smoothly embedded Riemannian manifold M in $R^n$. The key observation is that the weak formulation of the Fokker--Planck equation, together with the ambient-space representation of the Laplace--Beltrami operator via the tangential projection $P(x)$ and the mean-curvature vector $H(x)$, permits all integrals to be evaluated as expectations over samples lying on M, using test functions defined globally on $R^n$. A neural pushforward map is constrained to map the support of a base distribution into M at all times through a manifold retraction, so that probability conservation and manifold membership are enforced by construction....

---

## 57. Bridging the Simulation-to-Reality Gap in Electron Microscope Calibration via VAE-EM Estimation

**Authors**: Jilles S. van Hulst (Maurice), W. P. M. H. (Maurice),  Heemels, Duarte J. Antunes  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16549  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16549v1.pdf

**Abstract**:
> arXiv:2603.16549v1 Announce Type: cross 
Abstract: Electron microscopy has enabled many scientific breakthroughs across multiple fields. A key challenge is the tuning of microscope parameters based on images to overcome optical aberrations that deteriorate image quality. This calibration problem is challenging due to the high-dimensional and noisy nature of the diagnostic images, and the fact that optimal parameters cannot be identified from a single image. We tackle the calibration problem for Scanning Transmission Electron Microscopes (STEM) by employing variational autoencoders (VAEs), trained on simulated data, to learn low-dimensional representations of images, whereas most existing methods extract only scalar values. We then simultaneously estimate the model that maps calibration par...

---

## 58. Data-driven forced response analysis with min-max representations of nonlinear restoring forces

**Authors**: Akira Saito, Hiromu Fujita  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16746  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16746v1.pdf

**Abstract**:
> arXiv:2603.16746v1 Announce Type: cross 
Abstract: This paper discusses a novel data-driven nonlinearity identification method for mechanical systems with nonlinear restoring forces such as polynomial, piecewise-linear, and general displacement-dependent nonlinearities. The proposed method is built upon the universal approximation theorem that states that a nonlinear function can be approximated by a linear combination of activation functions in artificial neural network framework. The proposed approach utilizes piecewise linear springs with initial gaps to act as the activation functions of the neurons of artificial neural networks. A library of piecewise linear springs with initial gaps are constructed, and the contributions of the springs on the nonlinear restoring force are determined ...

---

## 59. Probing Cultural Signals in Large Language Models through Author Profiling

**Authors**: Valentin Lafargue, Ariel Guerra-Adames, Emmanuelle Claeys, Elouan Vuichard, Jean-Michel Loubes  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16749  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16749v1.pdf

**Abstract**:
> arXiv:2603.16749v1 Announce Type: cross 
Abstract: Large language models (LLMs) are increasingly deployed in applications with societal impact, raising concerns about the cultural biases they encode. We probe these representations by evaluating whether LLMs can perform author profiling from song lyrics in a zero-shot setting, inferring singers' gender and ethnicity without task-specific fine-tuning. Across several open-source models evaluated on more than 10,000 lyrics, we find that LLMs achieve non-trivial profiling performance but demonstrate systematic cultural alignment: most models default toward North American ethnicity, while DeepSeek-1.5B aligns more strongly with Asian ethnicity. This finding emerges from both the models' prediction distributions and an analysis of their generated...

---

## 60. Learning-based Sketches for Frequency Estimation in Data Streams without Ground Truth

**Authors**: Xinyu Yuan, Yan Qiao, Meng Li, Zhenchun Wei, Cuiying Feng, Zonghui Wang, Wenzhi Chen  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2412.03611  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2412.03611v5.pdf

**Abstract**:
> arXiv:2412.03611v5 Announce Type: replace 
Abstract: Estimating the frequency of items on the high-volume, fast data stream has been extensively studied in many areas, such as database and network measurement. Traditional sketches provide only coarse estimates under strict memory constraints. Although some learning-augmented methods have emerged recently, they typically rely on offline training with real frequencies or/and labels, which are often unavailable. Moreover, these methods suffer from slow update speeds, limiting their suitability for real-time processing despite offering only marginal accuracy improvements. To overcome these challenges, we propose UCL-sketch, a practical learning-based paradigm for per-key frequency estimation. Our design introduces two key innovations: (i) an o...

---

## 61. VERINA: Benchmarking Verifiable Code Generation

**Authors**: Zhe Ye, Zhengxu Yan, Jingxuan He, Timothe Kasriel, Kaiyu Yang, Dawn Song  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2505.23135  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2505.23135v3.pdf

**Abstract**:
> arXiv:2505.23135v3 Announce Type: replace 
Abstract: Large language models (LLMs) are increasingly integrated in software development, but ensuring correctness in LLM-generated code remains challenging and often requires costly manual review. Verifiable code generation -- jointly generating code, specifications, and proofs of code-specification alignment -- offers a promising path to address this limitation and further unleash LLMs' benefits in coding. Yet, there exists a significant gap in evaluation: current benchmarks often focus on only individual components rather than providing a holistic evaluation framework of all tasks. In this paper, we introduce VERINA (Verifiable Code Generation Arena), a high-quality benchmark enabling a comprehensive and modular evaluation of code, specificat...

---

## 62. Scalable Feature Learning on Huge Knowledge Graphs for Downstream Machine Learning

**Authors**: F\'elix Lefebvre, Ga\"el Varoquaux  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2507.00965  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2507.00965v3.pdf

**Abstract**:
> arXiv:2507.00965v3 Announce Type: replace 
Abstract: Many machine learning tasks can benefit from external knowledge. Large knowledge graphs store such knowledge, and embedding methods can be used to distill it into ready-to-use vector representations for downstream applications. For this purpose, current models have however two limitations: they are primarily optimized for link prediction, via local contrastive learning, and their application to the largest graphs requires significant engineering effort due to GPU memory limits. To address these, we introduce SEPAL: a Scalable Embedding Propagation ALgorithm for large knowledge graphs designed to produce high-quality embeddings for downstream tasks at scale. The key idea of SEPAL is to ensure global embedding consistency by optimizing emb...

---

## 63. PolyGraph Discrepancy: a classifier-based metric for graph generation

**Authors**: Markus Krimmel, Philip Hartout, Karsten Borgwardt, Dexiong Chen  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.06122  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.06122v2.pdf

**Abstract**:
> arXiv:2510.06122v2 Announce Type: replace 
Abstract: Existing methods for evaluating graph generative models primarily rely on Maximum Mean Discrepancy (MMD) metrics based on graph descriptors. While these metrics can rank generative models, they do not provide an absolute measure of performance. Their values are also highly sensitive to extrinsic parameters, namely kernel and descriptor parametrization, making them incomparable across different graph descriptors. We introduce PolyGraph Discrepancy (PGD), a new evaluation framework that addresses these limitations. It approximates the Jensen-Shannon distance of graph distributions by fitting binary classifiers to distinguish between real and generated graphs, featurized by these descriptors. The data log-likelihood of these classifiers app...

---

## 64. Connecting Jensen-Shannon and Kullback-Leibler Divergences: A New Bound for Representation Learning

**Authors**: Reuben Dorent, Polina Golland, William Wells III  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.20644  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.20644v2.pdf

**Abstract**:
> arXiv:2510.20644v2 Announce Type: replace 
Abstract: Mutual Information (MI) is a fundamental measure of statistical dependence widely used in representation learning. While direct optimization of MI via its definition as a Kullback-Leibler divergence (KLD) is often intractable, many recent methods have instead maximized alternative dependence measures, most notably, the Jensen-Shannon divergence (JSD) between joint and product of marginal distributions via discriminative losses. However, the connection between these surrogate objectives and MI remains poorly understood. In this work, we bridge this gap by deriving a new, tight, and tractable lower bound on KLD as a function of JSD in the general case. By specializing this bound to joint and marginal distributions, we demonstrate that maxi...

---

## 65. FedSDWC: Federated Synergistic Dual-Representation Weak Causal Learning for OOD

**Authors**: Zhenyuan Huang, Hui Zhang, Wenzhong Tang, Haijun Yang  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2511.09036  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2511.09036v2.pdf

**Abstract**:
> arXiv:2511.09036v2 Announce Type: replace 
Abstract: Amid growing demands for data privacy and advances in computational infrastructure, federated learning (FL) has emerged as a prominent distributed learning paradigm. Nevertheless, differences in data distribution (such as covariate and semantic shifts) severely affect its reliability in real-world deployments. To address this issue, we propose FedSDWC, a causal inference method that integrates both invariant and variant features. FedSDWC infers causal semantic representations by modeling the weak causal influence between invariant and variant features, effectively overcoming the limitations of existing invariant learning methods in accurately capturing invariant features and directly constructing causal representations. This approach sig...

---

## 66. Language as a Wave Phenomenon: Semantic Phase Locking and Interference in Neural Networks

**Authors**: Alper Y{\i}ld{\i}r{\i}m, \.Ibrahim Y\"uceda\u{g}  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2512.01208  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2512.01208v4.pdf

**Abstract**:
> arXiv:2512.01208v4 Announce Type: replace 
Abstract: The role of phase in neural sequence models remains poorly understood. To isolate this question, we introduce PRISM, a complex-valued encoder that enforces a unit-norm constraint ($|z| = 1$) and replaces attention with gated spectral filtering. Under this constraint, the model cannot use activation magnitude to distinguish signal from noise, and must instead rely on phase angles. We find that semantic relationships correlate with measurable phase structure: synonym pairs exhibit significantly higher phase coherence than random pairs ($R = 0.198$ vs.\ $0.072$, $p < 0.001$), and the model resolves lexical ambiguity via layer-specific phase rotations while maintaining near-unit gain. These phase representations are robust to scalar attenuat...

---

## 67. Exposing Hidden Biases in Text-to-Image Models via Automated Prompt Search

**Authors**: Manos Plitsis, Giorgos Bouritsas, Vassilis Katsouros, Yannis Panagakis  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2512.08724  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2512.08724v2.pdf

**Abstract**:
> arXiv:2512.08724v2 Announce Type: replace 
Abstract: Text-to-image (TTI) diffusion models have achieved remarkable visual quality, yet they have been repeatedly shown to exhibit social biases across sensitive attributes such as gender, race and age. To mitigate these biases, existing approaches frequently depend on curated prompt datasets - either manually constructed or generated with large language models (LLMs) - as part of their training and/or evaluation procedures. Beside the curation cost, this also risks overlooking unanticipated, less obvious prompts that trigger biased generation, even in models that have undergone debiasing. In this work, we introduce Bias-Guided Prompt Search (BGPS), a framework that automatically generates prompts that aim to maximize the presence of biases in...

---

## 68. Transit Network Design with Two-Level Demand Uncertainties: A Machine Learning and Contextual Stochastic Optimization Framework

**Authors**: Hongzhao Guan, Beste Basciftci, Pascal Van Hentenryck  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.00010  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.00010v2.pdf

**Abstract**:
> arXiv:2603.00010v2 Announce Type: replace 
Abstract: Transit Network Design is a well-studied problem in the field of transportation, typically addressed by solving optimization models under fixed demand assumptions. Considering the limitations of these assumptions, this paper proposes a new framework, namely the Two-Level Rider Choice Transit Network Design (2LRC-TND), that leverages machine learning and contextual stochastic optimization (CSO) through constraint programming (CP) to incorporate two layers of demand uncertainties into the network design process. The first level identifies travelers who rely on public transit (core demand), while the second level captures the conditional adoption behavior of those who do not (latent demand), based on the availability and quality of transit ...

---

## 69. Thin Keys, Full Values: Reducing KV Cache via Low-Dimensional Attention Selection

**Authors**: Hengshuai Yao, Xing Chen, Ahmed Murtadha, Guan Wang  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.04427  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.04427v2.pdf

**Abstract**:
> arXiv:2603.04427v2 Announce Type: replace 
Abstract: Standard transformer attention uses identical dimensionality for queries, keys, and values, yet these components serve
  different roles: queries and keys produce scalar attention weights (selection), while values carry rich representations
  (value transfer). We show that selection requires only $O(\log N)$ dimensions to distinguish among $N$ relevant token
  categories (e.g., syntactic roles, semantic clusters, positional patterns) -- far fewer than value transfer needs.
  We introduce factored keys, which exploit this asymmetry to physically shrink the KV cache of any pretrained model without
  retraining from scratch -- unlike GQA and MLA, which must be designed into the architecture before pretraining. We factorize
  each key projec...

---

## 70. Attention Sinks Are Provably Necessary in Softmax Transformers: Evidence from Trigger-Conditional Tasks

**Authors**: Yuval Ran-Milo  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11487  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11487v3.pdf

**Abstract**:
> arXiv:2603.11487v3 Announce Type: replace 
Abstract: Transformers often display an attention sink: probability mass concentrates on a fixed, content-agnostic position. Are sinks a byproduct of the optimization/training regime? Or are they sometimes functionally necessary in softmax Transformers? Are sinks a byproduct of the optimization/training regime? Or are they sometimes functionally necessary in softmax Transformers? We prove that, in some settings, it is the latter: computing a simple trigger-conditional behavior necessarily induces a sink in softmax self-attention models. Our results formalize a familiar intuition: normalization over a probability simplex must force attention to collapse onto a stable anchor to realize a default state (e.g., when the model needs to ignore the input)...

---

## 71. Lipschitz-Based Robustness Certification Under Floating-Point Execution

**Authors**: Toby Murray  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13334  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13334v2.pdf

**Abstract**:
> arXiv:2603.13334v2 Announce Type: replace 
Abstract: Sensitivity-based robustness certification has emerged as a practical approach for certifying neural network robustness, including in settings that require verifiable guarantees. A key advantage of these methods is that certification is performed by concrete numerical computation (rather than symbolic reasoning) and scales efficiently with network size. However, as with the vast majority of prior work on robustness certification and verification, the soundness of these methods is typically proved with respect to a semantic model that assumes exact real arithmetic. In reality deployed neural network implementations execute using floating-point arithmetic. This mismatch creates a semantic gap between certified robustness properties and the...

---

## 72. OrigamiBench: An Interactive Environment to Synthesize Flat-Foldable Origamis

**Authors**: Naaisha Agarwal, Yihan Wu, Yichang Jian, Yikuan Hu, Nishad Mansoor, Mohan Li, Yifei Peng, Wang-Zhou ...  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13856  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13856v2.pdf

**Abstract**:
> arXiv:2603.13856v2 Announce Type: replace 
Abstract: Building AI systems that can plan, act, and create in the physical world requires more than pattern recognition. Such systems must understand the causal mechanisms and constraints governing physical processes in order to guide sequential decisions. This capability relies on internal representations, analogous to an internal language model, that relate observations, actions, and resulting environmental changes. However, many existing benchmarks treat visual perception and programmatic reasoning as separate problems, focusing either on visual recognition or on symbolic tasks. The domain of origami provides a natural testbed that integrates these modalities. Constructing shapes through folding operations requires visual perception, reasonin...

---

## 73. High-Fidelity Compression of Seismic Velocity Models via SIREN Auto-Decoders

**Authors**: Caiyun Liu, Xiaoxue Luo, Jie Xiong  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14284  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14284v2.pdf

**Abstract**:
> arXiv:2603.14284v2 Announce Type: replace 
Abstract: Implicit Neural Representations (INRs) have emerged as a powerful paradigm for representing continuous signals independently of grid resolution. In this paper, we propose a high-fidelity neural compression framework based on a SIREN (Sinusoidal Representation Networks) auto-decoder to represent multi-structural seismic velocity models from the OpenFWI benchmark. Our method compresses each 70x70 velocity map (4,900 points) into a compact 256-dimensional latent vector, achieving a compression ratio of 19:1. We evaluate the framework on 1,000 samples across five diverse geological families: FlatVel, CurveVel, FlatFault, CurveFault, and Style. Experimental results demonstrate an average PSNR of 32.47 dB and SSIM of 0.956, indicating high-qua...

---

## 74. Towards Robust Multimodal Physiological Foundation Models: Handling Arbitrary Missing Modalities

**Authors**: Wei-Bang Jiang, Xi Fu, Yi Ding, Cuntai Guan  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2504.19596  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2504.19596v3.pdf

**Abstract**:
> arXiv:2504.19596v3 Announce Type: replace-cross 
Abstract: Multimodal physiological signals, such as EEG, ECG, EOG, and EMG, are crucial for healthcare and brain-computer interfaces. While existing methods rely on specialized architectures and dataset-specific fusion strategies, they struggle to learn universal representations that generalize across datasets and handle missing modalities at inference time. To address these issues, we propose PhysioOmni, a foundation model for multimodal physiological signal analysis that models both homogeneous and heterogeneous features to decouple multimodal signals and extract generic representations while maintaining compatibility with arbitrary missing modalities. PhysioOmni trains a decoupled multimodal tokenizer, enabling masked signal pre-training ...

---

## 75. Strategic Costs of Perceived Bias in Fair Selection

**Authors**: L. Elisa Celis, Lingxiao Huang, Milind Sohoni, Nisheeth K. Vishnoi  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.20606  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.20606v2.pdf

**Abstract**:
> arXiv:2510.20606v2 Announce Type: replace-cross 
Abstract: Meritocratic systems, from admissions to hiring, aim to impartially reward skill and effort. Yet persistent disparities across race, gender, and class challenge this ideal. Some attribute these gaps to structural inequality; others to individual choice. We develop a game-theoretic model in which candidates from different socioeconomic groups differ in their perceived post-selection value--shaped by social context and, increasingly, by AI-powered tools offering personalized career or salary guidance. Each candidate strategically chooses effort, balancing its cost against expected reward; effort translates into observable merit, and selection is based solely on merit. We characterize the unique Nash equilibrium in the large-agent lim...

---

## 76. SARMAE: Masked Autoencoder for SAR Representation Learning

**Authors**: Danxu Liu, Di Wang, Hebaixu Wang, Haoyang Chen, Wentao Jiang, Yilin Cheng, Haonan Guo, Wei Cui, Jing...  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2512.16635  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2512.16635v2.pdf

**Abstract**:
> arXiv:2512.16635v2 Announce Type: replace-cross 
Abstract: Synthetic Aperture Radar (SAR) imagery plays a critical role in all-weather, day-and-night remote sensing applications. However, existing SAR-oriented deep learning is constrained by data scarcity, while the physically grounded speckle noise in SAR imagery further hampers fine-grained semantic representation learning. To address these challenges, we propose SARMAE, a Noise-Aware Masked Autoencoder for self-supervised SAR representation learning. Specifically, we construct SAR-1M, the first million-scale SAR dataset, with additional paired optical images, to enable large-scale pre-training. Building upon this, we design Speckle-Aware Representation Enhancement (SARE), which injects SAR-specific speckle noise into masked autoencoders...

---

## 77. CFM: Language-aligned Concept Foundation Model for Vision

**Authors**: Kai Wittenmayer, Sukrut Rao, Amin Parchami-Araghi, Bernt Schiele, Jonas Fischer  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2601.13798  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2601.13798v2.pdf

**Abstract**:
> arXiv:2601.13798v2 Announce Type: replace-cross 
Abstract: Language-aligned vision foundation models perform strongly across diverse downstream tasks. Yet, their learned representations remain opaque, making interpreting their decision-making difficult. Recent work decompose these representations into human-interpretable concepts, but provide poor spatial grounding and are limited to image classification tasks. In this work, we propose CFM, a language-aligned concept foundation model for vision that provides fine-grained concepts, which are human-interpretable and spatially grounded in the input image. When paired with a foundation model with strong semantic representations, we get explanations for any of its downstream tasks. Examining local co-occurrence dependencies of concepts allows u...

---

## 78. Functional Stochastic Localization

**Authors**: Anming Gu, Bobby Shi, Kevin Tian  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.03999  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.03999v2.pdf

**Abstract**:
> arXiv:2602.03999v2 Announce Type: replace-cross 
Abstract: Eldan's stochastic localization is a probabilistic construction that has proved instrumental to modern breakthroughs in high-dimensional geometry and the design of sampling algorithms. Motivated by sampling under non-Euclidean geometries and the mirror descent algorithm in optimization, we develop a functional generalization of Eldan's process that replaces Gaussian regularization with regularization by any positive integer multiple of a log-Laplace transform. We further give a mixing time bound on the Markov chain induced by our localization process, which holds if our target distribution satisfies a functional Poincar\'e inequality. Finally, we apply our framework to differentially private convex optimization in $\ell_p$ norms fo...

---

## 79. LLMs Encode Their Failures: Predicting Success from Pre-Generation Activations

**Authors**: William Lugoloobi, Thomas Foster, William Bankes, Chris Russell  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.09924  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.09924v2.pdf

**Abstract**:
> arXiv:2602.09924v2 Announce Type: replace-cross 
Abstract: Running LLMs with extended reasoning on every problem is expensive, but determining which inputs actually require additional compute remains challenging. We investigate whether their own likelihood of success is recoverable from their internal representations before generation, and if this signal can guide more efficient inference. We train linear probes on pre-generation activations to predict policy-specific success on math and coding tasks, substantially outperforming surface features such as question length and TF-IDF. Using E2H-AMC, which provides both human and model performance on identical problems, we show that models encode a model-specific notion of difficulty that is distinct from human difficulty, and that this distinc...

---

## 80. Foundation-Model Surrogates Enable Data-Efficient Active Learning for Materials Discovery

**Authors**: Jeffrey Hu, Rongzhi Dong, Ying Feng, Ming Hu, Jianjun Hu  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12567  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12567v2.pdf

**Abstract**:
> arXiv:2603.12567v2 Announce Type: replace-cross 
Abstract: Active learning (AL) has emerged as a powerful paradigm for accelerating materials discovery by iteratively steering experiments toward promising candidates, reducing the number of costly synthesis-and-characterization cycles needed to identify optimal materials. However, current AL relies predominantly on Gaussian Process (GP) and Random Forest (RF) surrogates, which suffer from complementary limitations: GP underfits complex composition-property landscapes due to rigid kernel assumptions, while RF produces unreliable heuristic uncertainty estimates in small-data regimes. This small-data challenge is pervasive in materials science, making reliable surrogate modeling extremely difficult with models trained from scratch on each new ...

---

## 81. SHAMISA: SHAped Modeling of Implicit Structural Associations for Self-supervised No-Reference Image Quality Assessment

**Authors**: Mahdi Naseri, Zhou Wang  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13669  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13669v2.pdf

**Abstract**:
> arXiv:2603.13669v2 Announce Type: replace-cross 
Abstract: No-Reference Image Quality Assessment (NR-IQA) aims to estimate perceptual quality without access to a reference image of pristine quality. Learning an NR-IQA model faces a fundamental bottleneck: its need for a large number of costly human perceptual labels. We propose SHAMISA, a non-contrastive self-supervised framework that learns from unlabeled distorted images by leveraging explicitly structured relational supervision. Unlike prior methods that impose rigid, binary similarity constraints, SHAMISA introduces implicit structural associations, defined as soft, controllable relations that are both distortion-aware and content-sensitive, inferred from synthetic metadata and intrinsic feature structure. A key innovation is our compo...

---

## 82. Masked BRep Autoencoder via Hierarchical Graph Transformer

**Authors**: Yifei Li, Kang Wu, Wenming Wu, Xiao-Ming Fu  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14927  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14927v2.pdf

**Abstract**:
> arXiv:2603.14927v2 Announce Type: replace-cross 
Abstract: We introduce a novel self-supervised learning framework that automatically learns representations from input computer-aided design (CAD) models for downstream tasks, including part classification, modeling segmentation, and machining feature recognition. To train our network, we construct a large-scale, unlabeled dataset of boundary representation (BRep) models. The success of our algorithm relies on two keycomponents. The first is a masked graph autoencoder that reconstructs randomly masked geometries and attributes of BReps for representation learning to enhance the generalization. The second is a hierarchical graph Transformer architecture that elegantly fuses global and local learning by a cross-scale mutual attention block to ...

---

## 83. HindSight: Evaluating LLM-Generated Research Ideas via Future Impact

**Authors**: Bo Jiang  
**Categories**: cs.LG  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15164  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15164v2.pdf

**Abstract**:
> arXiv:2603.15164v2 Announce Type: replace-cross 
Abstract: Evaluating AI-generated research ideas typically relies on LLM judges or human panels -- both subjective and disconnected from actual research impact. We introduce HindSight, a time-split evaluation framework that measures idea quality by matching generated ideas against real future publications and scoring them by citation impact and venue acceptance. Using a temporal cutoff~$T$, we restrict an idea generation system to pre-$T$ literature, then evaluate its outputs against papers published in the subsequent 30 months. Experiments across 10 AI/ML research topics reveal a striking disconnect: LLM-as-Judge finds no significant difference between retrieval-augmented and vanilla idea generation ($p{=}0.584$), while HindSight shows the ...

---

## 84. Neural-Symbolic Logic Query Answering in Non-Euclidean Space

**Authors**: Lihui Liu  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15633  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15633v1.pdf

**Abstract**:
> arXiv:2603.15633v1 Announce Type: new 
Abstract: Answering complex first-order logic (FOL) queries on knowledge graphs is essential for reasoning. Symbolic methods offer interpretability but struggle with incomplete graphs, while neural approaches generalize better but lack transparency. Neural-symbolic models aim to integrate both strengths but often fail to capture the hierarchical structure of logical queries, limiting their effectiveness. We propose HYQNET, a neural-symbolic model for logic query reasoning that fully leverages hyperbolic space. HYQNET decomposes FOL queries into relation projections and logical operations over fuzzy sets, enhancing interpretability. To address missing links, it employs a hyperbolic GNN-based approach for knowledge graph completion in hyperbolic space, ...

---

## 85. QV May Be Enough: Toward the Essence of Attention in LLMs

**Authors**: Zhang Edward  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15665  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15665v1.pdf

**Abstract**:
> arXiv:2603.15665v1 Announce Type: new 
Abstract: Starting from first principles and a linguistic perspective centered on part-of-speech (POS) and syntactic analysis, this paper explores and derives the underlying essence of the Query-Key-Value (QKV) mechanism within the Transformer architecture. Based on this theoretical foundation, we provide a unified explanatory framework for the efficacy of contemporary architectures, including MQA, GQA, and MLA, while identifying their inherent trade-offs and potential optimization trajectories. We introduce the QV paradigm and provide empirical evidence for its validity. Building upon this, we propose the QV-Ka optimization scheme, which is further substantiated through experimental validation. The interpretable theoretical analysis of the QKV mechan...

---

## 86. IRAM-Omega-Q: A Computational Architecture for Uncertainty Regulation in Artificial Agents

**Authors**: Veronique Ziegler  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16020  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16020v1.pdf

**Abstract**:
> arXiv:2603.16020v1 Announce Type: new 
Abstract: Artificial agents can achieve strong task performance while remaining opaque with respect to internal regulation, uncertainty management, and stability under stochastic perturbation. We present IRAM-Omega-Q, a computational architecture that models internal regulation as closed-loop control over a quantum-like state representation. The framework uses density matrices instrumentally as abstract state descriptors, enabling direct computation of entropy, purity, and coherence-related metrics without invoking physical quantum processes. A central adaptive gain is updated continuously to maintain a target uncertainty regime under noise. Using systematic parameter sweeps, fixed-seed publication-mode simulations, and susceptibility-based phase-diag...

---

## 87. VIGIL: Towards Edge-Extended Agentic AI for Enterprise IT Support

**Authors**: Sarthak Ahuja, Neda Kordjazi, Evren Yortucboylu, Vishaal Kapoor, Mariam Dundua, Yiming Li, Derek Ho,...  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16110  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16110v1.pdf

**Abstract**:
> arXiv:2603.16110v1 Announce Type: new 
Abstract: Enterprise IT support is constrained by heterogeneous devices, evolving policies, and long-tail failure modes that are difficult to resolve centrally. We present VIGIL, an edge-extended agentic AI system that deploys desktop-resident agents to perform situated diagnosis, retrieval over enterprise knowledge, and policy-governed remediation directly on user devices with explicit consent and end-to-end observability. In a 10-week pilot of VIGIL's operational loop on 100 resource-constrained endpoints, VIGIL reduces interaction rounds by 39%, achieves at least 4 times faster diagnosis, and supports self-service resolution in 82% of matched cases. Users report excellent usability, high trust, and low cognitive workload across four validated instr...

---

## 88. From Natural Language to Executable Option Strategies via Large Language Models

**Authors**: Haochen Luo, Zhengzhao Lai, Junjie Xu, Yifan Li, Tang Pok Hin, Yuan Zhang, Chen Liu  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16434  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16434v1.pdf

**Abstract**:
> arXiv:2603.16434v1 Announce Type: new 
Abstract: Large Language Models (LLMs) excel at general code generation, yet translating natural-language trading intents into correct option strategies remains challenging. Real-world option design requires reasoning over massive, multi-dimensional option chain data with strict constraints, which often overwhelms direct generation methods. We introduce the Option Query Language (OQL), a domain-specific intermediate representation that abstracts option markets into high-level primitives under grammatical rules, enabling LLMs to function as reliable semantic parsers rather than free-form programmers. OQL queries are then validated and executed deterministically by an engine to instantiate executable strategies. We also present a new dataset for this ta...

---

## 89. ExpressMind: A Multimodal Pretrained Large Language Model for Expressway Operation

**Authors**: Zihe Wang, Yihuan Wang, Haiyang Yu. Zhiyong Cui, Xiaojian Liao, Chengcheng Wang, Yonglin Tian, Yongx...  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16495  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16495v1.pdf

**Abstract**:
> arXiv:2603.16495v1 Announce Type: new 
Abstract: The current expressway operation relies on rule-based and isolated models, which limits the ability to jointly analyze knowledge across different systems. Meanwhile, Large Language Models (LLMs) are increasingly applied in intelligent transportation, advancing traffic models from algorithmic to cognitive intelligence. However, general LLMs are unable to effectively understand the regulations and causal relationships of events in unconventional scenarios in the expressway field. Therefore, this paper constructs a pre-trained multimodal large language model (MLLM) for expressways, ExpressMind, which serves as the cognitive core for intelligent expressway operations. This paper constructs the industry's first full-stack expressway dataset, enco...

---

## 90. Domain-Independent Dynamic Programming with Constraint Propagation

**Authors**: Imko Marijnissen, J. Christopher Beck, Emir Demirovi\'c, Ryo Kuroiwa  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16648  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16648v1.pdf

**Abstract**:
> arXiv:2603.16648v1 Announce Type: new 
Abstract: There are two prevalent model-based paradigms for combinatorial problems: 1) state-based representations, such as heuristic search, dynamic programming (DP), and decision diagrams, and 2) constraint and domain-based representations, such as constraint programming (CP), (mixed-)integer programming, and Boolean satisfiability. In this paper, we bridge the gap between the DP and CP paradigms by integrating constraint propagation into DP, enabling a DP solver to prune states and transitions using constraint propagation. To this end, we implement constraint propagation using a general-purpose CP solver in the Domain-Independent Dynamic Programming framework and evaluate using heuristic search on three combinatorial optimisation problems: Single M...

---

## 91. IQuest-Coder-V1 Technical Report

**Authors**: Jian Yang, Wei Zhang, Shawn Guo, Zhengmao Ye, Lin Jing, Shark Liu, Yizhi Li, Jiajun Wu, Cening Liu, ...  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16733  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16733v1.pdf

**Abstract**:
> arXiv:2603.16733v1 Announce Type: new 
Abstract: In this report, we introduce the IQuest-Coder-V1 series-(7B/14B/40B/40B-Loop), a new family of code large language models (LLMs). Moving beyond static code representations, we propose the code-flow multi-stage training paradigm, which captures the dynamic evolution of software logic through different phases of the pipeline. Our models are developed through the evolutionary pipeline, starting with the initial pre-training consisting of code facts, repository, and completion data. Following that, we implement a specialized mid-training stage that integrates reasoning and agentic trajectories in 32k-context and repository-scale in 128k-context to forge deep logical foundations. The models are then finalized with post-training of specialized cod...

---

## 92. SocialOmni: Benchmarking Audio-Visual Social Interactivity in Omni Models

**Authors**: Tianyu Xie, Jinfa Huang, Yuexiao Ma, Rongfang Luo, Yan Yang, Wang Chen, Yuhui Zeng, Ruize Fang, Yixu...  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16859  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16859v1.pdf

**Abstract**:
> arXiv:2603.16859v1 Announce Type: new 
Abstract: Omni-modal large language models (OLMs) redefine human-machine interaction by natively integrating audio, vision, and text. However, existing OLM benchmarks remain anchored to static, accuracy-centric tasks, leaving a critical gap in assessing social interactivity, the fundamental capacity to navigate dynamic cues in natural dialogues. To this end, we propose SocialOmni, a comprehensive benchmark that operationalizes the evaluation of this conversational interactivity across three core dimensions: (i) speaker separation and identification (who is speaking), (ii) interruption timing control (when to interject), and (iii) natural interruption generation (how to phrase the interruption). SocialOmni features 2,000 perception samples and a qualit...

---

## 93. Finder: A Multimodal AI-Powered Search Framework for Pharmaceutical Data Retrieval

**Authors**: Suyash Mishra, Srikanth Patil, Satyanarayan Pati, Sagar Sahu, Baddu Narendra  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15623  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15623v1.pdf

**Abstract**:
> arXiv:2603.15623v1 Announce Type: cross 
Abstract: AI is transforming pharmaceutical search, where traditional systems struggle with multimodal content and manual curation. Finder is a scalable AI-powered framework that unifies retrieval across text, images, audio, and video using hybrid vector search, combining sparse lexical and dense semantic models. Its modular pipeline ingests diverse formats, enriches metadata, and stores content in a vector-native backend. Finder supports reasoning-aware natural language search, improving precision and contextual relevance. The system has processed over 291,400 documents, 31,070 videos, and 1,192 audio files in 98 languages. Techniques like hybrid fusion, chunking, and metadata-aware routing enable intelligent access across regulatory, research, and...

---

## 94. State-Dependent Safety Failures in Multi-Turn Language Model Interaction

**Authors**: Pengcheng Li, Jie Zhang, Tianwei Zhang, Han Qiu, Zhang kejun, Weiming Zhang, Nenghai Yu, Wenbo Zhou  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15684  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15684v1.pdf

**Abstract**:
> arXiv:2603.15684v1 Announce Type: cross 
Abstract: Safety alignment in large language models is typically evaluated under isolated queries, yet real-world use is inherently multi-turn. Although multi-turn jailbreaks are empirically effective, the structure of conversational safety failure remains insufficiently understood. In this work, we study safety failures from a state-space perspective and show that many multi-turn failures arise from structured contextual state evolution rather than isolated prompt vulnerabilities. We introduce STAR, a state-oriented diagnostic framework that treats dialogue history as a state transition operator and enables controlled analysis of safety behavior along interaction trajectories. Rather than optimizing attack strength, STAR provides a principled probe...

---

## 95. CorrectionPlanner: Self-Correction Planner with Reinforcement Learning in Autonomous Driving

**Authors**: Yihong Guo, Dongqiangzi Ye, Sijia Chen, Anqi Liu, Xianming Liu  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15771  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15771v1.pdf

**Abstract**:
> arXiv:2603.15771v1 Announce Type: cross 
Abstract: Autonomous driving requires safe planning, but most learning-based planners lack explicit self-correction ability: once an unsafe action is proposed, there is no mechanism to correct it. Thus, we propose CorrectionPlanner, an autoregressive planner with self-correction that models planning as motion-token generation within a propose, evaluate, and correct loop. At each planning step, the policy proposes an action, namely a motion token, and a learned collision critic predicts whether it will induce a collision within a short horizon. If the critic predicts a collision, we retain the sequence of historical unsafe motion tokens as a self-correction trace, generate the next motion token conditioned on it, and repeat this process until a safe ...

---

## 96. Interpretative Interfaces: Designing for AI-Mediated Reading Practices and the Knowledge Commons

**Authors**: Gabrielle Benabdallah  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15863  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15863v1.pdf

**Abstract**:
> arXiv:2603.15863v1 Announce Type: cross 
Abstract: Explainable AI (XAI) interfaces seek to make large language models more transparent, yet explanation alone does not produce understanding. Explaining a system's behavior is not the same as being able to engage with it, to probe and interpret its operations through direct manipulation. This distinction matters for scientific disciplines in particular: scientists who increasingly rely on LLMs for reading, citing, and producing literature reviews have little means of directly engaging with how these models process and transform the texts they generate. In this ongoing design research project, I argue for a shift from explainability to interpretative engagement. This shift moves away from accounts of system behavior to instead enable users to ...

---

## 97. 100x Cost & Latency Reduction: Performance Analysis of AI Query Approximation using Lightweight Proxy Models

**Authors**: Yeounoh Chung, Rushabh Desai, Jian He, Yu Xiao, Thibaud Hottelier, Yves-Laurent Kom Samo, Pushkar Ka...  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15970  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15970v1.pdf

**Abstract**:
> arXiv:2603.15970v1 Announce Type: cross 
Abstract: Several data warehouse and database providers have recently introduced extensions to SQL called AI Queries, enabling users to specify functions and conditions in SQL that are evaluated by LLMs, thereby broadening significantly the kinds of queries one can express over the combination of structured and unstructured data. LLMs offer remarkable semantic reasoning capabilities, making them an essential tool for complex and nuanced queries that blend structured and unstructured data. While extremely powerful, these AI queries can become prohibitively costly when invoked thousands of times.
  This paper provides an extensive evaluation of a recent AI query approximation approach that enables low cost analytics and database applications to benefi...

---

## 98. Standardizing Medical Images at Scale for AI

**Authors**: Callen MacPhee, Yiming Zhou, Koichiro Kishima, Bahram Jalali  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15980  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15980v1.pdf

**Abstract**:
> arXiv:2603.15980v1 Announce Type: cross 
Abstract: Deep learning has achieved remarkable success in medical image analysis, yet its performance remains highly sensitive to the heterogeneity of clinical data. Differences in imaging hardware, staining protocols, and acquisition conditions produce substantial domain shifts that degrade model generalization across institutions. Here we present a physics-based data preprocessing framework based on the PhyCV (Physics-Inspired Computer Vision) family of algorithms, which standardizes medical images through deterministic transformations derived from optical physics. The framework models images as spatially varying optical fields that undergo a virtual diffractive propagation followed by coherent phase detection. This process suppresses non-semanti...

---

## 99. Aligning Paralinguistic Understanding and Generation in Speech LLMs via Multi-Task Reinforcement Learning

**Authors**: Jingxiang Chen, Minseok Kim, Seong-Gyun Leem, Yin Huang, Rashi Rungta, Zhicheng Ouyang, Haibin Wu, S...  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15981  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15981v1.pdf

**Abstract**:
> arXiv:2603.15981v1 Announce Type: cross 
Abstract: Speech large language models (LLMs) observe paralinguistic cues such as prosody, emotion, and non-verbal sounds--crucial for intent understanding. However, leveraging these cues faces challenges: limited training data, annotation difficulty, and models exploiting lexical shortcuts over paralinguistic signals. We propose multi-task reinforcement learning (RL) with chain-of-thought prompting that elicits explicit affective reasoning. To address data scarcity, we introduce a paralinguistics-aware speech LLM (PALLM) that jointly optimizes sentiment classification from audio and paralinguistics-aware response generation via a two-stage pipeline. Experiments demonstrate that our approach improves paralinguistics understanding over both supervise...

---

## 100. Understanding Moral Reasoning Trajectories in Large Language Models: Toward Probing-Based Explainability

**Authors**: Fan Huang, Haewoon Kwak, Jisun An  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16017  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16017v1.pdf

**Abstract**:
> arXiv:2603.16017v1 Announce Type: cross 
Abstract: Large language models (LLMs) increasingly participate in morally sensitive decision-making, yet how they organize ethical frameworks across reasoning steps remains underexplored. We introduce \textit{moral reasoning trajectories}, sequences of ethical framework invocations across intermediate reasoning steps, and analyze their dynamics across six models and three benchmarks. We find that moral reasoning involves systematic multi-framework deliberation: 55.4--57.7\% of consecutive steps involve framework switches, and only 16.4--17.8\% of trajectories remain framework-consistent. Unstable trajectories remain 1.29$\times$ more susceptible to persuasive attacks ($p=0.015$). At the representation level, linear probes localize framework-specifi...

---

## 101. SEAHateCheck: Functional Tests for Detecting Hate Speech in Low-Resource Languages of Southeast Asia

**Authors**: Ri Chi Ng, Aditi Kumaresan, Yujia Hu, Roy Ka-Wei Lee  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16070  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16070v1.pdf

**Abstract**:
> arXiv:2603.16070v1 Announce Type: cross 
Abstract: Hate speech detection relies heavily on linguistic resources, which are primarily available in high-resource languages such as English and Chinese, creating barriers for researchers and platforms developing tools for low-resource languages in Southeast Asia, where diverse socio-linguistic contexts complicate online hate moderation. To address this, we introduce SEAHateCheck, a pioneering dataset tailored to Indonesia, Thailand, the Philippines, and Vietnam, covering Indonesian, Tagalog, Thai, and Vietnamese. Building on HateCheck's functional testing framework and refining SGHateCheck's methods, SEAHateCheck provides culturally relevant test cases, augmented by large language models and validated by local experts for accuracy. Experiments ...

---

## 102. RecBundle: A Next-Generation Geometric Paradigm for Explainable Recommender Systems

**Authors**: Hui Wang, Tianzhu Hu, Mingming Li, Xi Zhou, Chun Gan, Jiao Dai, Jizhong Han, Songlin Hu, Tao Guo  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16088  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16088v1.pdf

**Abstract**:
> arXiv:2603.16088v1 Announce Type: cross 
Abstract: Recommender systems are inherently dynamic feedback loops where prolonged local interactions accumulate into macroscopic structural degradation such as information cocoons. Existing representation learning paradigms are universally constrained by the assumption of a single flat space, forcing topologically grounded user associations and semantically driven historical interactions to be fitted within the same vector space. This excessive coupling of heterogeneous information renders it impossible for researchers to mechanistically distinguish and identify the sources of systemic bias. To overcome this theoretical bottleneck, we introduce Fiber Bundle from modern differential geometry and propose a novel geometric analysis paradigm for recom...

---

## 103. Structure-Aware Multimodal LLM Framework for Trustworthy Near-Field Beam Prediction

**Authors**: Mengyuan Li, Qianfan Lu, Jiachen Tian, Hongjun Hu, Yu Han, Xiao Li, Chao-kai Wen, Shi Jin  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16143  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16143v1.pdf

**Abstract**:
> arXiv:2603.16143v1 Announce Type: cross 
Abstract: In near-field extremely large-scale multiple-input multiple-output (XL-MIMO) systems, spherical wavefront propagation expands the traditional beam codebook into the joint angular-distance domain, rendering conventional beam training prohibitively inefficient, especially in complex 3-dimensional (3D) low-altitude environments. Furthermore, since near-field beam variations are deeply coupled not only with user positions but also with the physical surroundings, precise beam alignment demands profound environmental understanding capabilities. To address this, we propose a large language model (LLM)-driven multimodal framework that fuses historical GPS data, RGB image, LiDAR data, and strategically designed task-specific textual prompts. By uti...

---

## 104. GATS: Gaussian Aware Temporal Scaling Transformer for Invariant 4D Spatio-Temporal Point Cloud Representation

**Authors**: Jiayi Tian, Jiaze Wang  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16154  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16154v1.pdf

**Abstract**:
> arXiv:2603.16154v1 Announce Type: cross 
Abstract: Understanding 4D point cloud videos is essential for enabling intelligent agents to perceive dynamic environments. However, temporal scale bias across varying frame rates and distributional uncertainty in irregular point clouds make it highly challenging to design a unified and robust 4D backbone. Existing CNN or Transformer based methods are constrained either by limited receptive fields or by quadratic computational complexity, while neglecting these implicit distortions. To address this problem, we propose a novel dual invariant framework, termed \textbf{Gaussian Aware Temporal Scaling (GATS)}, which explicitly resolves both distributional inconsistencies and temporal. The proposed \emph{Uncertainty Guided Gaussian Convolution (UGGC)} i...

---

## 105. 360{\deg} Image Perception with MLLMs: A Comprehensive Benchmark and a Training-Free Method

**Authors**: Huyen T. T. Tran, Van-Quang Nguyen, Farros Alferro, Kang-Jun Liu, Takayuki Okatani  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16179  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16179v1.pdf

**Abstract**:
> arXiv:2603.16179v1 Announce Type: cross 
Abstract: Multimodal Large Language Models (MLLMs) have shown impressive abilities in understanding and reasoning over conventional images. However, their perception of 360{\deg} images remains largely underexplored. Unlike conventional images, 360{\deg} images capture the entire surrounding environment, enabling holistic spatial reasoning but introducing challenges such as geometric distortion and complex spatial relations. To comprehensively assess MLLMs' capabilities to perceive 360{\deg} images, we introduce 360Bench, a Visual Question Answering (VQA) benchmark featuring 7K-resolution 360{\deg} images, seven representative (sub)tasks with annotations carefully curated by human annotators. Using 360Bench, we systematically evaluate seven MLLMs an...

---

## 106. A Scoping Review of AI-Driven Digital Interventions in Mental Health Care: Mapping Applications Across Screening, Support, Monitoring, Prevention, and Clinical Education

**Authors**: Yang Ni, Fanli Jia  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16204  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16204v1.pdf

**Abstract**:
> arXiv:2603.16204v1 Announce Type: cross 
Abstract: Artificial intelligence (AI)-enabled digital interventions, including Generative AI (GenAI) and Human-Centered AI (HCAI), are increasingly used to expand access to digital psychiatry and mental health care. This PRISMA-ScR scoping review maps the landscape of AI-driven mental health (mHealth) technologies across five critical phases: pre-treatment (screening/triage), treatment (therapeutic support), post-treatment (remote patient monitoring), clinical education, and population-level prevention. We synthesized 36 empirical studies implemented through early 2024, focusing on Large Language Models (LLMs), machine learning (ML) models, and autonomous conversational agents. Key use cases involve referral triage, empathic communication enhanceme...

---

## 107. RASLF: Representation-Aware State Space Model for Light Field Super-Resolution

**Authors**: Zeqiang Wei, Kai Jin, Kuan Song, Xiuzhuang Zhou, Wenlong Chen, Min Xu  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16243  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16243v1.pdf

**Abstract**:
> arXiv:2603.16243v1 Announce Type: cross 
Abstract: Current SSM-based light field super-resolution (LFSR) methods often fail to fully leverage the complementarity among various LF representations, leading to the loss of fine textures and geometric misalignments across views. To address these issues, we propose RASLF, a representation-aware state-space framework that explicitly models structural correlations across multiple LF representations. Specifically, a Progressive Geometric Refinement (PGR) block is created that uses a panoramic epipolar representation to explicitly encode multi-view parallax differences, thereby enabling integration across different LF representations. Furthermore, we introduce a Representation Aware Asymmetric Scanning (RAAS) mechanism that dynamically adjusts scann...

---

## 108. Attention-guided Evidence Grounding for Spoken Question Answering

**Authors**: Ke Yang, Bolin Chen, Yuejie Li, Yueying Hua, Jianhao Nie, Yueping He, Bowen Li, Chengjun Mao  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16292  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16292v1.pdf

**Abstract**:
> arXiv:2603.16292v1 Announce Type: cross 
Abstract: Spoken Question Answering (Spoken QA) presents a challenging cross-modal problem: effectively aligning acoustic queries with textual knowledge while avoiding the latency and error propagation inherent in cascaded ASR-based systems. In this paper, we introduce Attention-guided Evidence Grounding (AEG), a novel end-to-end framework that leverages the internal cross-modal attention of Speech Large Language Models (SpeechLLMs) to explicitly locate and ground key evidence in the model's latent space. To address the diffuse attention distribution in pre-trained models, we propose Learning to Focus on Evidence (LFE), a supervised fine-tuning paradigm that calibrates the model's attention mechanism to distinguish query-relevant segments from irrel...

---

## 109. Fanar 2.0: Arabic Generative AI Stack

**Authors**: FANAR TEAM, Ummar Abbas, Mohammad Shahmeer Ahmad, Minhaj Ahmad, Abdulaziz Al-Homaid, Anas Al-Nuaimi,...  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16397  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16397v1.pdf

**Abstract**:
> arXiv:2603.16397v1 Announce Type: cross 
Abstract: We present Fanar 2.0, the second generation of Qatar's Arabic-centric Generative AI platform. Sovereignty is a first-class design principle: every component, from data pipelines to deployment infrastructure, was designed and operated entirely at QCRI, Hamad Bin Khalifa University. Fanar 2.0 is a story of resource-constrained excellence: the effort ran on 256 NVIDIA H100 GPUs, with Arabic having only ~0.5% of web data despite 400 million native speakers. Fanar 2.0 adopts a disciplined strategy of data quality over quantity, targeted continual pre-training, and model merging to achieve substantial gains within these constraints. At the core is Fanar-27B, continually pre-trained from a Gemma-3-27B backbone on a curated corpus of 120 billion h...

---

## 110. DST-Net: A Dual-Stream Transformer with Illumination-Independent Feature Guidance and Multi-Scale Spatial Convolution for Low-Light Image Enhancement

**Authors**: Yicui Shi, Yuhan Chen, Xiangfei Huang, Zhenguo Wang, Wenxuan Yu, Ying Fang  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16482  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16482v1.pdf

**Abstract**:
> arXiv:2603.16482v1 Announce Type: cross 
Abstract: Low-light image enhancement aims to restore the visibility of images captured by visual sensors in dim environments by addressing their inherent signal degradations, such as luminance attenuation and structural corruption. Although numerous algorithms attempt to improve image quality, existing methods often cause a severe loss of intrinsic signal priors. To overcome these challenges, we propose a Dual-Stream Transformer Network (DST-Net) based on illumination-agnostic signal prior guidance and multi-scale spatial convolutions. First, to address the loss of critical signal features under low-light conditions, we design a feature extraction module. This module integrates Difference of Gaussians (DoG), LAB color space transformations, and VGG...

---

## 111. CompDiff: Hierarchical Compositional Diffusion for Fair and Zero-Shot Intersectional Medical Image Generation

**Authors**: Mahmoud Ibrahim, Bart Elen, Chang Sun, Gokhan Ertaylan, Michel Dumontier  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16551  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16551v1.pdf

**Abstract**:
> arXiv:2603.16551v1 Announce Type: cross 
Abstract: Generative models are increasingly used to augment medical imaging datasets for fairer AI. Yet a key assumption often goes unexamined: that generators themselves produce equally high-quality images across demographic groups. Models trained on imbalanced data can inherit these imbalances, yielding degraded synthesis quality for rare subgroups and struggling with demographic intersections absent from training. We refer to this as the imbalanced generator problem. Existing remedies such as loss reweighting operate at the optimization level and provide limited benefit when training signal is scarce or absent for certain combinations. We propose CompDiff, a hierarchical compositional diffusion framework that addresses this problem at the repres...

---

## 112. Malicious Or Not: Adding Repository Context to Agent Skill Classification

**Authors**: Florian Holzbauer, David Schmidt, Gabriel Gegenhuber, Sebastian Schrittwieser, Johanna Ullrich  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16572  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16572v1.pdf

**Abstract**:
> arXiv:2603.16572v1 Announce Type: cross 
Abstract: Agent skills extend local AI agents, such as Claude Code or Open Claw, with additional functionality, and their popularity has led to the emergence of dedicated skill marketplaces, similar to app stores for mobile applications. Simultaneously, automated skill scanners were introduced, analyzing the skill description available in SKILL.md, to verify their benign behavior. The results for individual market places mark up to 46.8% of skills as malicious. In this paper, we present the largest empirical security analysis of the AI agent skill ecosystem, questioning this high classification of malicious skills. Therefore, we collect 238,180 unique skills from three major distribution platforms and GitHub to systematically analyze their type and ...

---

## 113. Can Linguistically Related Languages Guide LLM Translation in Low-Resource Settings?

**Authors**: Aishwarya Ramasethu, Niyathi Allu, Rohin Garg, Harshwardhan Fartale, Dun Li Chan  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16660  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16660v1.pdf

**Abstract**:
> arXiv:2603.16660v1 Announce Type: cross 
Abstract: Large Language Models (LLMs) have achieved strong performance across many downstream tasks, yet their effectiveness in extremely low-resource machine translation remains limited. Standard adaptation techniques typically rely on large-scale parallel data or extensive fine-tuning, which are infeasible for the long tail of underrepresented languages. In this work, we investigate a more constrained question: in data-scarce settings, to what extent can linguistically similar pivot languages and few-shot demonstrations provide useful guidance for on-the-fly adaptation in LLMs? We study a data-efficient experimental setup that combines linguistically related pivot languages with few-shot in-context examples, without any parameter updates, and eva...

---

## 114. Fast-WAM: Do World Action Models Need Test-time Future Imagination?

**Authors**: Tianyuan Yuan, Zibin Dong, Yicheng Liu, Hang Zhao  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16666  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16666v1.pdf

**Abstract**:
> arXiv:2603.16666v1 Announce Type: cross 
Abstract: World Action Models (WAMs) have emerged as a promising alternative to Vision-Language-Action (VLA) models for embodied control because they explicitly model how visual observations may evolve under action. Most existing WAMs follow an imagine-then-execute paradigm, incurring substantial test-time latency from iterative video denoising, yet it remains unclear whether explicit future imagination is actually necessary for strong action performance. In this paper, we ask whether WAMs need explicit future imagination at test time, or whether their benefit comes primarily from video modeling during training. We disentangle the role of video modeling during training from explicit future generation during inference by proposing \textbf{Fast-WAM}, ...

---

## 115. V-Co: A Closer Look at Visual Representation Alignment via Co-Denoising

**Authors**: Han Lin, Xichen Pan, Zun Wang, Yue Zhang, Chu Wang, Jaemin Cho, Mohit Bansal  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16792  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16792v1.pdf

**Abstract**:
> arXiv:2603.16792v1 Announce Type: cross 
Abstract: Pixel-space diffusion has recently re-emerged as a strong alternative to latent diffusion, enabling high-quality generation without pretrained autoencoders. However, standard pixel-space diffusion models receive relatively weak semantic supervision and are not explicitly designed to capture high-level visual structure. Recent representation-alignment methods (e.g., REPA) suggest that pretrained visual features can substantially improve diffusion training, and visual co-denoising has emerged as a promising direction for incorporating such features into the generative process. However, existing co-denoising approaches often entangle multiple design choices, making it unclear which design choices are truly essential. Therefore, we present V-C...

---

## 116. DexGrasp-Zero: A Morphology-Aligned Policy for Zero-Shot Cross-Embodiment Dexterous Grasping

**Authors**: Yuliang Wu, Yanhan Lin, WengKit Lao, Yuhao Lin, Yi-Lin Wei, Wei-Shi Zheng, Ancong Wu  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16806  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16806v1.pdf

**Abstract**:
> arXiv:2603.16806v1 Announce Type: cross 
Abstract: To meet the demands of increasingly diverse dexterous hand hardware, it is crucial to develop a policy that enables zero-shot cross-embodiment grasping without redundant re-learning. Cross-embodiment alignment is challenging due to heterogeneous hand kinematics and physical constraints. Existing approaches typically predict intermediate motion targets and retarget them to each embodiment, which may introduce errors and violate embodiment-specific limits, hindering transfer across diverse hands. To overcome these limitations, we propose \textit{DexGrasp-Zero}, a policy that learns universal grasping skills from diverse embodiments, enabling zero-shot transfer to unseen hands. We first introduce a morphology-aligned graph representation that...

---

## 117. Real-Time Decoding of Movement Onset and Offset for Brain-Controlled Rehabilitation Exoskeleton

**Authors**: Kanishka Mitra, Satyam Kumar, Frigyes Samuel Racz, Deland Liu, Ashish D. Deshpande, Jos\'e del R. Mi...  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16825  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16825v1.pdf

**Abstract**:
> arXiv:2603.16825v1 Announce Type: cross 
Abstract: Robot-assisted therapy can deliver high-dose, task-specific training after neurologic injury, but most systems act primarily at the limb level-engaging the impaired neural circuits only indirectly-which remains a key barrier to truly contingent, neuroplasticity-targeted rehabilitation. We address this gap by implementing online, dual-state motor imagery control of an upper-limb exoskeleton, enabling goal-directed reaches to be both initiated and terminated directly from non-invasive EEG. Eight participants used EEG to initiate assistance and then volitionally halt the robot mid-trajectory. Across two online sessions, group-mean hit rates were 61.5% for onset and 64.5% for offset, demonstrating reliable start-stop command delivery despite i...

---

## 118. SOMA: Unifying Parametric Human Body Models

**Authors**: Jun Saito, Jiefeng Li, Michael de Ruyter, Miguel Guerrero, Edy Lim, Ehsan Hassani, Roger Blanco Ribe...  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16858  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16858v1.pdf

**Abstract**:
> arXiv:2603.16858v1 Announce Type: cross 
Abstract: Parametric human body models are foundational to human reconstruction, animation, and simulation, yet they remain mutually incompatible: SMPL, SMPL-X, MHR, Anny, and related models each diverge in mesh topology, skeletal structure, shape parameterization, and unit convention, making it impractical to exploit their complementary strengths within a single pipeline. We present SOMA, a unified body layer that bridges these heterogeneous representations through three abstraction layers. Mesh topology abstraction maps any source model's identity to a shared canonical mesh in constant time per vertex. Skeletal abstraction recovers a full set of identity-adapted joint transforms from any body shape, whether in rest pose or an arbitrary posed confi...

---

## 119. Demystifing Video Reasoning

**Authors**: Ruisi Wang, Zhongang Cai, Fanyi Pu, Junxiang Xu, Wanqi Yin, Maijunxian Wang, Ran Ji, Chenyang Gu, Bo...  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16870  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16870v1.pdf

**Abstract**:
> arXiv:2603.16870v1 Announce Type: cross 
Abstract: Recent advances in video generation have revealed an unexpected phenomenon: diffusion-based video models exhibit non-trivial reasoning capabilities. Prior work attributes this to a Chain-of-Frames (CoF) mechanism, where reasoning is assumed to unfold sequentially across video frames. In this work, we challenge this assumption and uncover a fundamentally different mechanism. We show that reasoning in video models instead primarily emerges along the diffusion denoising steps. Through qualitative analysis and targeted probing experiments, we find that models explore multiple candidate solutions in early denoising steps and progressively converge to a final answer, a process we term Chain-of-Steps (CoS). Beyond this core mechanism, we identify...

---

## 120. IMAIA: Interactive Maps AI Assistant for Travel Planning and Geo-Spatial Intelligence

**Authors**: Jieren Deng, Zhizhang Hu, Ziyan He, Aleksandar Cvetkovic, Pak Kiu Chung, Dragomir Yankov, Chiqun Zha...  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2507.06993  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2507.06993v4.pdf

**Abstract**:
> arXiv:2507.06993v4 Announce Type: replace 
Abstract: Map applications are still largely point-and-click, making it difficult to ask map-centric questions or connect what a camera sees to the surrounding geospatial context with view-conditioned inputs. We introduce IMAIA, an interactive Maps AI Assistant that enables natural-language interaction with both vector (street) maps and satellite imagery, and augments camera inputs with geospatial intelligence to help users understand the world. IMAIA comprises two complementary components. Maps Plus treats the map as first-class context by parsing tiled vector/satellite views into a grid-aligned representation that a language model can query to resolve deictic references (e.g., ``the flower-shaped building next to the park in the top-right''). Pl...

---

## 121. The DeepLog Neurosymbolic Machine

**Authors**: Vincent Derkinderen, Robin Manhaeve, Rik Adriaensen, Lucas Van Praet, Lennert De Smet, Giuseppe Marr...  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2508.13697  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2508.13697v2.pdf

**Abstract**:
> arXiv:2508.13697v2 Announce Type: replace 
Abstract: We contribute a theoretical and operational framework for neurosymbolic AI called DeepLog. DeepLog introduces building blocks and primitives for neurosymbolic AI that make abstraction of commonly used representations and computational mechanisms in neurosymbolic AI. DeepLog can represent and emulate a wide range of neurosymbolic systems. It consists of two key components. The first is the DeepLog language for specifying neurosymbolic models and inference tasks. This language consists of an annotated neural extension of grounded first-order logic, and makes abstraction of the type of logic, e.g. Boolean, fuzzy or probabilistic, and whether logic is used in the architecture or in the loss function. The second DeepLog component is situated ...

---

## 122. Dynamics Within Latent Chain-of-Thought: An Empirical Study of Causal Structure

**Authors**: Zirui Li, Xuefeng Bai, Kehai Chen, Yizhi Li, Jian Yang, Chenghua Lin, Min Zhang  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.08783  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.08783v2.pdf

**Abstract**:
> arXiv:2602.08783v2 Announce Type: replace 
Abstract: Latent or continuous chain-of-thought methods replace explicit textual rationales with a number of internal latent steps, but these intermediate computations are difficult to evaluate beyond correlation-based probes. In this paper, we view latent chain-of-thought as a manipulable causal process in representation space by modeling latent steps as variables in a structural causal model (SCM) and analyzing their effects through step-wise $\mathrm{do}$-interventions. We study two representative paradigms (i.e., Coconut and CODI) on both mathematical and general reasoning tasks to investigate three key questions: (1) which steps are causally necessary for correctness and when answers become decidable early; (2) how does influence propagate ac...

---

## 123. Laplace-Beltrami Operator for Gaussian Splatting

**Authors**: Hongyu Zhou, Zorah L\"ahner  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2502.17531  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2502.17531v2.pdf

**Abstract**:
> arXiv:2502.17531v2 Announce Type: replace-cross 
Abstract: With the rising popularity of 3D Gaussian splatting and the expanse of applications from rendering to 3D reconstruction, there comes also a need for geometry processing applications directly on this new representation. While considering the centers of Gaussians as a point cloud or meshing them is an option that allows to apply existing algorithms, this might ignore information present in the data or be unnecessarily expensive. Additionally, Gaussian splatting tends to contain a large number of outliers which do not affect the rendering quality but need to be handled correctly in order not to produce noisy results in geometry processing applications. In this work, we propose a formulation to compute the Laplace-Beltrami operator, a ...

---

## 124. Boosting Text-to-Chart Retrieval through Training with Synthesized Semantic Insights

**Authors**: Yifan Wu, Lutao Yan, Yizhang Zhu, Yenchi Tseng, Yinan Mei, Yong Wang, Jiannan Wang, Nan Tang, Yuyu L...  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2505.10043  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2505.10043v4.pdf

**Abstract**:
> arXiv:2505.10043v4 Announce Type: replace-cross 
Abstract: Text-to-chart retrieval, enabling users to find relevant charts via natural language queries, has gained significant attention. However, evaluating models in real-world business intelligence (BI) scenarios is challenging, as current benchmarks fail to simulate realistic user queries or test for deep semantic understanding with static chart images.To address this gap, we introduce CRBench, the first real-world BI-sourced benchmark comprising 21,862 charts and 326 queries, utilizing a Target-and-Distractor paradigm to evaluate discriminative retrieval among highly similar candidates. Testing on CRBench reveals that existing methods, which rely primarily on visual features, perform poorly and fail to capture the rich analytical semant...

---

## 125. Improved Iterative Refinement for Chart-to-Code Generation via Structured Instruction

**Authors**: Chengzhi Xu, Yuyang Wang, Lai Wei, Lichao Sun, Weiran Huang  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2506.14837  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2506.14837v2.pdf

**Abstract**:
> arXiv:2506.14837v2 Announce Type: replace-cross 
Abstract: Recently, multimodal large language models (MLLMs) have attracted increasing research attention due to their powerful visual understanding capabilities. While they have achieved impressive results on various vision tasks, their performance on chart-to-code generation remains suboptimal. This task requires MLLMs to generate executable code that can reproduce a given chart, demanding not only precise visual understanding but also accurate translation of visual elements into structured code. Directly prompting MLLMs to perform this complex task often yields unsatisfactory results. To address this challenge, we propose {ChartIR}, an iterative refinement method based on structured instruction. First, we distinguish two tasks: visual und...

---

## 126. Can large language models assist choice modelling? Insights into prompting strategies and current models capabilities

**Authors**: Georges Sfeir, Gabriel Nova, Stephane Hess, Sander van Cranenburgh  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2507.21790  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2507.21790v2.pdf

**Abstract**:
> arXiv:2507.21790v2 Announce Type: replace-cross 
Abstract: Large Language Models (LLMs) are becoming widely used to support various workflows across different disciplines, yet their potential in discrete choice modelling remains relatively unexplored. This work examines the potential of LLMs as assistive agents in the specification and, where technically feasible, estimation of Multinomial Logit models. We implement a systematic experimental framework involving twelve versions of seven leading LLMs (ChatGPT, Claude, DeepSeek, Gemini, Gemma, Llama, and Mistral) evaluated under five experimental configurations. These configurations vary along three dimensions: (i) modelling goal (suggesting vs. suggesting and estimating MNL models); (ii) prompting strategy (Zero-Shot vs. Chain-of-Thoughts (C...

---

## 127. Can LLMs Detect Their Confabulations? Estimating Reliability in Uncertainty-Aware Language Models

**Authors**: Tianyi Zhou, Johanne Medina, Sanjay Chawla  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2508.08139  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2508.08139v3.pdf

**Abstract**:
> arXiv:2508.08139v3 Announce Type: replace-cross 
Abstract: Large Language Models (LLMs) are prone to generating fluent but incorrect content, known as confabulation, which poses increasing risks in multi-turn or agentic applications where outputs may be reused as context. In this work, we investigate how in-context information influences model behavior and whether LLMs can identify their unreliable responses. We propose a reliability estimation that leverages token-level uncertainty to guide the aggregation of internal model representations. Specifically, we compute aleatoric and epistemic uncertainty from output logits to identify salient tokens and aggregate their hidden states into compact representations for response-level reliability prediction. Through controlled experiments on open ...

---

## 128. Traj2Action: A Co-Denoising Framework for Trajectory-Guided Human-to-Robot Skill Transfer

**Authors**: Han Zhou, Jinjin Cao, Liyuan Ma, Xueji Fang, Guo-jun Qi  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.00491  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.00491v2.pdf

**Abstract**:
> arXiv:2510.00491v2 Announce Type: replace-cross 
Abstract: Learning diverse manipulation skills for real-world robots is severely bottlenecked by the reliance on costly and hard-to-scale teleoperated demonstrations. While human videos offer a scalable alternative, effectively transferring manipulation knowledge is fundamentally hindered by the significant morphological gap between human and robotic embodiments. To address this challenge and facilitate skill transfer from human to robot, we introduce Traj2Action, a novel framework that bridges this embodiment gap by using the 3D trajectory of the operational endpoint as a unified intermediate representation, and then transfers the manipulation knowledge embedded in this trajectory to the robot's actions. Our policy first learns to generate ...

---

## 129. Representing Beauty: Towards a Participatory but Objective Latent Aesthetics

**Authors**: Alexander Michael Rusnak  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.02869  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.02869v2.pdf

**Abstract**:
> arXiv:2510.02869v2 Announce Type: replace-cross 
Abstract: What does it mean for a machine to recognize beauty? While beauty remains a culturally and experientially compelling but philosophically elusive concept, deep learning systems increasingly appear capable of modeling aesthetic judgment. In this paper, we explore the capacity of neural networks to represent beauty despite the immense formal diversity of objects for which the term applies. By drawing on recent work on cross-model representational convergence, we show how aesthetic content produces more similar and aligned representations between models which have been trained on distinct data and modalities - while unaesthetic images do not produce more aligned representations. This finding implies that the formal structure of beautif...

---

## 130. Readers Prefer Outputs of AI Trained on Copyrighted Books over Expert Human Writers

**Authors**: Tuhin Chakrabarty, Jane C. Ginsburg, Paramveer Dhillon  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.13939  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.13939v4.pdf

**Abstract**:
> arXiv:2510.13939v4 Announce Type: replace-cross 
Abstract: The use of copyrighted books for training AI has sparked lawsuits from authors concerned about AI generating derivative content. Yet whether these models can produce high-quality literary text emulating authors' voices remains unclear. We conducted a preregistered study comparing MFA-trained writers with three frontier models (ChatGPT, Claude, Gemini) writing up to 450-word excerpts emulating 50 award-winning authors' styles. In blind pairwise evaluations by 28 MFA-trained readers and 516 college-educated general readers, AI text from in-context prompting was strongly disfavored by MFA readers for stylistic fidelity (OR=0.16) and quality (OR=0.13), while general readers showed no fidelity preference (OR=1.06) but favored AI for qua...

---

## 131. Learning Topology-Driven Multi-Subspace Fusion for Grassmannian Deep Network

**Authors**: Xuan Yu, Tianyang Xu  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2511.08628  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2511.08628v3.pdf

**Abstract**:
> arXiv:2511.08628v3 Announce Type: replace-cross 
Abstract: Grassmannian manifold offers a powerful carrier for geometric representation learning by modelling high-dimensional data as low-dimensional subspaces. However, existing approaches predominantly rely on static single-subspace representations, neglecting the dynamic interplay between multiple subspaces critical for capturing complex geometric structures. To address this limitation, we propose a topology-driven multi-subspace fusion framework that enables adaptive subspace collaboration on the Grassmannian. Our solution introduces two key innovations: (1) Inspired by the Kolmogorov-Arnold representation theorem, an adaptive multi-subspace modelling mechanism is proposed that dynamically selects and weights task-relevant subspaces via ...

---

## 132. From Passive to Persuasive: Localized Activation Injection for Empathy and Negotiation

**Authors**: Niranjan Chebrolu, Kokil Jaidka, Gerard Christopher Yeo  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2511.12832  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2511.12832v3.pdf

**Abstract**:
> arXiv:2511.12832v3 Announce Type: replace-cross 
Abstract: Complex social behaviors, such as empathy and strategic politeness, are widely assumed to resist the directional decomposition that makes activation steering effective for coarse attributes like sentiment or toxicity. We present STAR: Steering via Attribution and Representation, which tests this assumption by using attribution patching to identify the layer--token positions where each behavioral trait causally originates, then injecting contrastive activation vectors at precisely those locations. Evaluated on emotional dialogue and negotiation in both single- and multi-turn settings, localized injection consistently outperforms global steering and instruction priming; human evaluation confirms that gains reflect genuine improvement...

---

## 133. Political Alignment in Large Language Models: A Multidimensional Audit of Psychometric Identity and Behavioral Bias

**Authors**: Adib Sakhawat, Tahsin Islam, Takia Farhin, Syed Rifat Raiyan, Hasan Mahmud, Md Kamrul Hasan  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2601.06194  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2601.06194v2.pdf

**Abstract**:
> arXiv:2601.06194v2 Announce Type: replace-cross 
Abstract: As large language models (LLMs) are increasingly deployed, understanding how they express political positioning is important for evaluating alignment and downstream effects. We audit 26 contemporary LLMs using three political psychometric inventories (Political Compass, SapplyValues, 8Values) and a news bias labeling task. To test robustness, inventories are administered across multiple semantic prompt variants and analyzed with a two-way ANOVA separating model and prompt effects. Most models cluster in a similar ideological region, with 96.3% located in the Libertarian-Left quadrant of the Political Compass, and model identity explaining most variance across prompt variants ($\eta^2 > 0.90$). Cross-instrument comparisons suggest t...

---

## 134. A Novel Evolutionary Method for Automated Skull-Face Overlay in Computer-Aided Craniofacial Superimposition

**Authors**: Pr\'axedes Mart\'inez-Moreno, Andrea Valsecchi, Pablo Mesejo, Pilar Navarro-Ram\'irez, Valentino Lug...  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.00170  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.00170v3.pdf

**Abstract**:
> arXiv:2603.00170v3 Announce Type: replace-cross 
Abstract: Craniofacial Superimposition is a forensic technique for identifying skeletal remains by comparing a post-mortem skull with ante-mortem facial photographs. A critical step in this process is Skull-Face Overlay (SFO). This stage involves aligning a 3D skull model with a 2D facial image, typically guided by cranial and facial landmarks' correspondence. However, its accuracy is undermined by individual variability in soft-tissue thickness, introducing significant uncertainty into the overlay. This paper introduces Lilium, an automated evolutionary method to enhance the accuracy and robustness of SFO. Lilium explicitly models soft-tissue variability using a 3D cone-based representation whose parameters are optimized via a Differential ...

---

## 135. Closed-Loop Action Chunks with Dynamic Corrections for Training-Free Diffusion Policy

**Authors**: Pengyuan Wu, Pingrui Zhang, Zhigang Wang, Dong Wang, Bin Zhao, Xuelong Li  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.01953  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.01953v2.pdf

**Abstract**:
> arXiv:2603.01953v2 Announce Type: replace-cross 
Abstract: Diffusion-based policies have achieved remarkable results in robotic manipulation but often struggle to adapt rapidly in dynamic scenarios, leading to delayed responses or task failures. We present DCDP, a Dynamic Closed-Loop Diffusion Policy framework that integrates chunk-based action generation with real-time correction. DCDP integrates a self-supervised dynamic feature encoder, cross-attention fusion, and an asymmetric action encoder-decoder to inject environmental dynamics before action execution, achieving real-time closed-loop action correction and enhancing the system's adaptability in dynamic scenarios. In dynamic PushT simulations, DCDP improves adaptability by 19\% without retraining while requiring only 5\% additional c...

---

## 136. ELISA: An Interpretable Hybrid Generative AI Agent for Expression-Grounded Discovery in Single-Cell Genomics

**Authors**: Omar Coser  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11872  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11872v2.pdf

**Abstract**:
> arXiv:2603.11872v2 Announce Type: replace-cross 
Abstract: Translating single-cell RNA sequencing (scRNA-seq) data into mechanistic biological hypotheses remains a critical bottleneck, as agentic AI systems lack direct access to transcriptomic representations while expression foundation models remain opaque to natural language. Here we introduce ELISA (Embedding-Linked Interactive Single-cell Agent), an interpretable framework that unifies scGPT expression embeddings with BioBERT-based semantic retrieval and LLM-mediated interpretation for interactive single-cell discovery. An automatic query classifier routes inputs to gene marker scoring, semantic matching, or reciprocal rank fusion pipelines depending on whether the query is a gene signature, natural language concept, or mixture of both...

---

## 137. Is Seeing Believing? Evaluating Human Sensitivity to Synthetic Video

**Authors**: David Wegmann, Emil Stevnsborg, S{\o}ren Knudsen, Luca Rossi, Aske Mottelson  
**Categories**: cs.AI  
**Published**: Wed, 18 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13846  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13846v2.pdf

**Abstract**:
> arXiv:2603.13846v2 Announce Type: replace-cross 
Abstract: Advances in machine learning have enabled the creation of realistic synthetic videos known as deepfakes. As deepfakes proliferate, concerns about rapid spread of disinformation and manipulation of public perception are mounting. Despite the alarming implications, our understanding of how individuals perceive synthetic media remains limited, obstructing the development of effective mitigation strategies. This paper aims to narrow this gap by investigating human responses to visual and auditory distortions of videos and deepfake-generated visuals and narration. In two between-subjects experiments, we study whether audio-visual distortions affect cognitive processing, such as subjective credibility assessment and objective learning ou...

---

