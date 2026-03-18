# arXiv Papers - 2026-03-18

**来源**: arXiv (cs.SD, eess.AS, cs.LG, cs.AI)  
**关键词**: speech, audio, music, voice, sound, Mel, representation, self-supervised  
**今日新论文**: 287 篇

---

## 1. Evaluation of Audio Language Models for Fairness, Safety, and Security

**Authors**: Ranya Aloufi, Srishti Gupta, Soumya Shaw, Battista Biggio, Lea Sch\"onherr  
**Categories**: cs.SD  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13262  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13262v1.pdf

**Abstract**:
> arXiv:2603.13262v1 Announce Type: new 
Abstract: Audio large language models (ALLMs) have recently advanced spoken interaction by integrating speech processing with large language models. However, existing evaluations of fairness, safety, and security (FSS) remain fragmented, largely because ALLMs differ fundamentally in how acoustic information is represented and where semantic reasoning occurs. Differences that are rarely made explicit. As a result, evaluations often conflate structurally distinct systems, obscuring the relationship between model design and observed FSS behavior. In this work, we introduce a structural taxonomy (system-level and representational) of ALLMs that categorizes systems along two axes: the form of audio input representation (e.g., discrete vs. continuous) and t...

---

## 2. Patient-Level Multimodal Question Answering from Multi-Site Auscultation Recordings

**Authors**: Fan Wu, Tsai-Ning Wang, Nicolas Zumarraga, Ning Wang, Markus Kreft, Kevin O'Sullivan, Elgar Fleisch,...  
**Categories**: cs.SD  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13362  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13362v1.pdf

**Abstract**:
> arXiv:2603.13362v1 Announce Type: new 
Abstract: Auscultation is a vital diagnostic tool, yet its utility is often limited by subjective interpretation. While general-purpose Audio-Language Models (ALMs) excel in general domains, they struggle with the nuances of physiological signals. We propose a framework that aligns multi-site auscultation recordings directly with a frozen Large Language Model (LLM) embedding space via gated cross-attention. By leveraging the LLM's latent world knowledge, our approach moves beyond isolated classification toward holistic, patient-level assessment. On the CaReSound benchmark, our model achieves a state-of-the-art 0.865 F1-macro and 0.952 BERTScore. We demonstrate that lightweight, domain-specific encoders rival large-scale ALMs and that multi-site aggreg...

---

## 3. Evaluating Compositional Structure in Audio Representations

**Authors**: Chuyang Chen, Bea Steers, Brian McFee, Juan Bello  
**Categories**: cs.SD  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13685  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13685v1.pdf

**Abstract**:
> arXiv:2603.13685v1 Announce Type: new 
Abstract: We propose a benchmark for evaluating compositionality in audio representations. Audio compositionality refers to representing sound scenes in terms of constituent sources and attributes, and combining them systematically. While central to auditory perception, this property is largely absent from current evaluation protocols. Our framework adapts ideas from vision and language to audio through two tasks: A-COAT, which tests consistency under additive transformations, and A-TRE, which probes reconstructibility from attribute-level primitives. Both tasks are supported by large synthetic datasets with controlled variation in acoustic attributes, providing the first benchmark of compositional structure in audio embeddings.

---

## 4. $\tau$-Voice: Benchmarking Full-Duplex Voice Agents on Real-World Domains

**Authors**: Soham Ray, Keshav Dhandhania, Victor Barres, Karthik Narasimhan  
**Categories**: cs.SD  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13686  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13686v1.pdf

**Abstract**:
> arXiv:2603.13686v1 Announce Type: new 
Abstract: Full-duplex voice agents--systems that listen and speak simultaneously--are rapidly moving from research to production. However, existing evaluations address conversational dynamics and task completion in isolation. We introduce $\tau$-voice, a benchmark for evaluating voice agents on grounded tasks with real-world complexity: agents must navigate complex multi-turn conversations, adhere to domain policies, and interact with the environment. The framework extends $\tau^2$-bench into a novel voice agent benchmark combining verifiable completion of complex grounded tasks, full-duplex interaction, and realistic audio--enabling direct comparison between voice and text performance. A controllable and realistic voice user simulator provides divers...

---

## 5. Sub-Band Spectral Matching with Localized Score Aggregation for Robust Anomalous Sound Detection

**Authors**: Phurich Saengthong, Takahiro Shinozaki  
**Categories**: cs.SD  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13749  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13749v1.pdf

**Abstract**:
> arXiv:2603.13749v1 Announce Type: new 
Abstract: Detecting subtle deviations in noisy acoustic environments is central to anomalous sound detection (ASD). A common training-free ASD pipeline temporally pools frame-level representations into a band-preserving feature vector and scores anomalies using a single nearest-neighbor match. However, this global matching can inflate normal-score variance through two effects. First, when normal sounds exhibit band-wise variability, a single global neighbor forces all bands to share the same reference, increasing band-level mismatch. Second, cosine-based matching is energy-coupled, allowing a few high-energy bands to dominate score computation under normal energy fluctuations and further increase variance. We propose BEAM, which stores temporally pool...

---

## 6. Causal Tracing of Audio-Text Fusion in Large Audio Language Models

**Authors**: Wei-Chih Chen, Chien-yu Huang, Hung-yi Lee  
**Categories**: cs.SD  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13768  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13768v1.pdf

**Abstract**:
> arXiv:2603.13768v1 Announce Type: new 
Abstract: Despite the strong performance of large audio language models (LALMs) in various tasks, exactly how and where they integrate acoustic features with textual context remains unclear. We adapt causal tracing to investigate the internal information flow of LALMs during audio comprehension. By conducting layer-wise and token-wise analyses across DeSTA, Qwen, and Voxtral, we evaluate the causal effects of individual hidden states. Layer-wise analysis identifies different fusion strategies, from progressive integration in DeSTA to abrupt late-stage fusion in Qwen. Token-wise analysis shows that the final sequence token acts as an informational bottleneck where the network decisively retrieves relevant information from the audio. We also observe an ...

---

## 7. Evaluating Semantic Fragility in Text-to-Audio Generation Systems Under Controlled Prompt Perturbations

**Authors**: Jiahui Wu  
**Categories**: cs.SD  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13824  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13824v1.pdf

**Abstract**:
> arXiv:2603.13824v1 Announce Type: new 
Abstract: Recent advances in text-to-audio generation enable models to translate natural-language descriptions into diverse musical output. However, the robustness of these systems under semantically equivalent prompt variations remains largely unexplored. Small linguistic changes may lead to substantial variation in generated audio, raising concerns about reliability in practical use.
  In this study, we evaluate the semantic fragility of text-to-audio systems under controlled prompt perturbations. We selected MusicGen-small, MusicGen-large, and Stable Audio 2.5 as representative models, and we evaluated them under Minimal Lexical Substitution (MLS), Intensity Shifts (IS), and Structural Rephrasing (SR). The proposed dataset contains 75 prompt groups...

---

## 8. LLM-Guided Reinforcement Learning for Audio-Visual Speech Enhancement

**Authors**: Chih-Ning Chen, Jen-Cheng Hou, Hsin-Min Wang, Shao-Yi Chien, Yu Tsao, Fan-Gang Zeng  
**Categories**: cs.SD  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13952  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13952v1.pdf

**Abstract**:
> arXiv:2603.13952v1 Announce Type: new 
Abstract: In existing Audio-Visual Speech Enhancement (AVSE) methods, objectives such as Scale-Invariant Signal-to-Noise Ratio (SI-SNR) and Mean Squared Error (MSE) are widely used; however, they often correlate poorly with perceptual quality and provide limited interpretability for optimization. This work proposes a reinforcement learning-based AVSE framework with a Large Language Model (LLM)-based interpretable reward model. An audio LLM generates natural language descriptions of enhanced speech, which are converted by a sentiment analysis model into a 1-5 rating score serving as the PPO reward for fine-tuning a pretrained AVSE model. Compared with scalar metrics, LLM-generated feedback is semantically rich and explicitly describes improvements in s...

---

## 9. What Counts as Real? Speech Restoration and Voice Quality Conversion Pose New Challenges to Deepfake Detection

**Authors**: Shree Harsha Bokkahalli Satish, Harm Lameris, Joakim Gustafson, \'Eva Sz\'ekely  
**Categories**: cs.SD  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14033  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14033v1.pdf

**Abstract**:
> arXiv:2603.14033v1 Announce Type: new 
Abstract: Audio anti-spoofing systems are typically formulated as binary classifiers distinguishing bona fide from spoofed speech. This assumption fails under layered generative processing, where benign transformations introduce distributional shifts that are misclassified as spoofing. We show that phonation-modifying voice conversion and speech restoration are treated as out-of-distribution despite preserving speaker authenticity. Using a multi-class setup separating bona fide, converted, spoofed, and converted-spoofed speech, we analyse model behaviour through self-supervised learning (SSL) embeddings and acoustic correlates. The benign transformations induce a drift in the SSL space, compressing bona fide and spoofed speech and reducing classifier ...

---

## 10. Probing neural audio codecs for distinctions among English nuclear tunes

**Authors**: Juan Pablo Vigneaux, Jennifer Cole  
**Categories**: cs.SD  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14035  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14035v1.pdf

**Abstract**:
> arXiv:2603.14035v1 Announce Type: new 
Abstract: State-of-the-art spoken dialogue models (D\'efossez et al. 2024; Schalkwyk et al. 2025) use neural audio codecs to "tokenize" audio signals into a lower-frequency stream of vectorial latent representations, each quantized using a hierarchy of vector codebooks. A transformer layer allows these representations to reflect some time- and context-dependent patterns. We train probes on labeled audio data from Cole et al. (2023) to test whether the pitch trajectories that characterize English phrase-final (nuclear) intonational tunes are among these patterns. Results: Linear probes trained on the unquantized latents or some of the associated codewords yield above-chance accuracy in distinguishing eight phonologically specified nuclear tunes with mo...

---

## 11. Affectron: Emotional Speech Synthesis with Affective and Contextually Aligned Nonverbal Vocalizations

**Authors**: Deok-Hyeon Cho, Hyung-Seok Oh, Seung-Bin Kim, Seong-Whan Lee  
**Categories**: cs.SD  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14432  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14432v1.pdf

**Abstract**:
> arXiv:2603.14432v1 Announce Type: new 
Abstract: Nonverbal vocalizations (NVs), such as laughter and sighs, are central to the expression of affective cues in emotional speech synthesis. However, learning diverse and contextually aligned NVs remains challenging in open settings due to limited NV data and the lack of explicit supervision. Motivated by this challenge, we propose Affectron as a framework for affective and contextually aligned NV generation. Built on a small-scale open and decoupled corpus, Affectron introduces an NV-augmented training strategy that expands the distribution of NV types and insertion locations. We further incorporate NV structural masking into a speech backbone pre-trained on purely verbal speech to enable diverse and natural NV synthesis. Experimental results ...

---

## 12. Nudging Hidden States: Training-Free Model Steering for Chain-of-Thought Reasoning in Large Audio-Language Models

**Authors**: Lok-Lam Ieong, Chia-Chien Chen, Chih-Kai Yang, Yu-Han Huang, An-Yu Cheng, Hung-yi Lee  
**Categories**: cs.SD  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14636  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14636v1.pdf

**Abstract**:
> arXiv:2603.14636v1 Announce Type: new 
Abstract: Chain-of-thought (CoT) prompting has been extended to large audio-language models (LALMs) to elicit reasoning, yet enhancing its effectiveness without training remains challenging. We study inference-time model steering as a training-free approach to improve LALM reasoning. We introduce three strategies using diverse information sources and evaluate them across four LALMs and four benchmarks. Results show general accuracy gains up to 4.4% over CoT prompting. Notably, we identify a cross-modal transfer where steering vectors derived from few text samples effectively guide speech-based reasoning, demonstrating high data efficiency. We also examine hyperparameter sensitivity to understand the robustness of these approaches. Our findings positio...

---

## 13. VorTEX: Various overlap ratio for Target speech EXtraction

**Authors**: Ro-hoon Oh, Jihwan Seol, Bugeun Kim  
**Categories**: cs.SD  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14803  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14803v1.pdf

**Abstract**:
> arXiv:2603.14803v1 Announce Type: new 
Abstract: Target speech extraction (TSE) aims to recover a target speaker's voice from a mixture. While recent text-prompted approaches have shown promise, most approaches assume fully overlapped mixtures, limiting insight into behavior across realistic overlap ratios. We introduce VorTEX (Various overlap ratio for Target speech EXtraction), a text-prompted TSE architecture with a Decoupled Adaptive Multi-branch (DAM) Fusion block that separates primary extraction from auxiliary regularization pathways. To enable controlled analysis, we construct PORTE, a two-speaker dataset spanning overlap ratios from 0% to 100%. We further propose Suppression Ratio on Energy (SuRE), a diagnostic metric that detects suppression behavior not captured by conventional ...

---

## 14. Cepstral Smoothing of Binary Masks for Convolutive Blind Separation of Speech Mixtures

**Authors**: Ibrahim Missaoui, Zied Lachiri  
**Categories**: cs.SD  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14983  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14983v1.pdf

**Abstract**:
> arXiv:2603.14983v1 Announce Type: new 
Abstract: In this paper, we propose a novel separation system for extracting two speech signals from two microphone recordings. Our system combines the blind source separation technique with cepstral smoothing of binary time-frequency masks. The last is composed of two steps. First, the two binary masks are estimated from the separated output signals of BSS algorithm. In the second step, a cepstral smoothing is applied of these spectral masks in order to reduce musical noise typically produced by time-frequency masking. Experiments were carried out with both artificially mixed speech signals using simulated room model and two real recordings. The evaluation results are promising and have shown the effectiveness of our system.

---

## 15. Music Genre Classification: A Comparative Analysis of Classical Machine Learning and Deep Learning Approaches

**Authors**: Sachin Prajuli, Abhishek Karna, OmPrakash Dhakl  
**Categories**: cs.SD  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15440  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15440v1.pdf

**Abstract**:
> arXiv:2603.15440v1 Announce Type: new 
Abstract: Automatic music genre classification is a long-standing challenge in Music Information Retrieval (MIR); work on non-Western music traditions remains scarce. Nepali music encompasses culturally rich and acoustically diverse genres--from the call-and-response duets of Lok Dohori to the rhythmic poetry of Deuda and the distinctive melodies of Tamang Selo--that have not been addressed by existing classification systems. In this paper, we construct a novel dataset of approximately 8,000 labeled 30-second audio clips spanning eight Nepali music genres and conduct a systematic comparison of nine classification models across two paradigms. Five classical machine learning classifiers (Logistic Regression, SVM, KNN, Random Forest, and XGBoost) are tra...

---

## 16. AC-Foley: Reference-Audio-Guided Video-to-Audio Synthesis with Acoustic Transfer

**Authors**: Pengjun Fang, Yingqing He, Yazhou Xing, Qifeng Chen, Ser-Nam Lim, Harry Yang  
**Categories**: cs.SD  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15597  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15597v1.pdf

**Abstract**:
> arXiv:2603.15597v1 Announce Type: new 
Abstract: Existing video-to-audio (V2A) generation methods predominantly rely on text prompts alongside visual information to synthesize audio. However, two critical bottlenecks persist: semantic granularity gaps in training data, such as conflating acoustically distinct sounds under coarse labels, and textual ambiguity in describing micro-acoustic features. These bottlenecks make it difficult to perform fine-grained sound synthesis using text-controlled modes. To address these limitations, we propose AC-Foley, an audio-conditioned V2A model that directly leverages reference audio to achieve precise and fine-grained control over generated sounds. This approach enables fine-grained sound synthesis, timbre transfer, zero-shot sound generation, and impro...

---

## 17. A Hierarchical End-of-Turn Model with Primary Speaker Segmentation for Real-Time Conversational AI

**Authors**: Karim Helwani, Hoang Do, James Luan, Sriram Srinivasan  
**Categories**: cs.SD  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13379  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13379v1.pdf

**Abstract**:
> arXiv:2603.13379v1 Announce Type: cross 
Abstract: We present a real-time front-end for voice-based conversational AI to enable natural turn-taking in two-speaker scenarios by combining primary speaker segmentation with hierarchical End-of-Turn (EOT) detection. To operate robustly in multi-speaker environments, the system continuously identifies and tracks the primary user, ensuring that downstream EOT decisions are not confounded by background conversations. The tracked activity segments are fed to a hierarchical, causal EOT model that predicts the immediate conversational state by independently analyzing per-speaker speech features from both the primary speaker and the bot. Simultaneously, the model anticipates near-future states ($t{+}10/20/30$\,ms) through probabilistic predictions tha...

---

## 18. Multimodal Emotion Regression with Multi-Objective Optimization and VAD-Aware Audio Modeling for the 10th ABAW EMI Track

**Authors**: Jiawen Huang, Chenxi Huang, Zhuofan Wen, Hailiang Yao, Shun Chen, Longjiang Yang, Cong Yu, Fengyu Zh...  
**Categories**: cs.SD  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13760  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13760v1.pdf

**Abstract**:
> arXiv:2603.13760v1 Announce Type: cross 
Abstract: We participated in the 10th ABAW Challenge, focusing on the Emotional Mimicry Intensity (EMI) Estimation track on the Hume-Vidmimic2 dataset. This task aims to predict six continuous emotion dimensions: Admiration, Amusement, Determination, Empathic Pain, Excitement, and Joy. Through systematic multimodal exploration of pretrained high-level features, we found that, under our pretrained feature setting, direct feature concatenation outperformed the more complex fusion strategies we tested. This empirical finding motivated us to design a systematic approach built upon three core principles: (i) preserving modality-specific attributes through feature-level concatenation; (ii) improving training stability and metric alignment via multi-object...

---

## 19. Sirens' Whisper: Inaudible Near-Ultrasonic Jailbreaks of Speech-Driven LLMs

**Authors**: Zijian Ling, Pingyi Hu, Xiuyong Gao, Xiaojing Ma, Man Zhou, Jun Feng, Songfeng Lu, Dongmei Zhang, Bi...  
**Categories**: cs.SD  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13847  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13847v1.pdf

**Abstract**:
> arXiv:2603.13847v1 Announce Type: cross 
Abstract: Speech-driven large language models (LLMs) are increasingly accessed through speech interfaces, introducing new security risks via open acoustic channels. We present Sirens' Whisper (SWhisper), the first practical framework for covert prompt-based attacks against speech-driven LLMs under realistic black-box conditions using commodity hardware. SWhisper enables robust, inaudible delivery of arbitrary target baseband audio-including long and structured prompts-on commodity devices by encoding it into near-ultrasound waveforms that demodulate faithfully after acoustic transmission and microphone nonlinearity. This is achieved through a simple yet effective approach to modeling nonlinear channel characteristics across devices and environments,...

---

## 20. LightBeam: An Accurate and Memory-Efficient CTC Decoder for Speech Neuroprostheses

**Authors**: Ebrahim Feghhi, Junlin Hu, Nima Hadidi, Jonathan C. Kao  
**Categories**: cs.SD  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14002  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14002v1.pdf

**Abstract**:
> arXiv:2603.14002v1 Announce Type: cross 
Abstract: A promising pathway for restoring communication in patients with dysarthria and anarthria is speech neuroprostheses, which directly decode speech from cortical neural activity. Two benchmarks, Brain-to-Text '24 and '25, released intracranial recordings from patients with dysarthria along with a baseline algorithm trained with Connectionist Temporal Classification (CTC). Despite significant innovation on these benchmarks, all leading published prior work relies on a WFST-based CTC decoder that requires ${\sim}$320 GB of RAM. These memory requirements limit accessibility for both patients and researchers. Here, we propose LightBeam, a non-WFST based CTC decoder that requires only ${\sim}$10 GB of RAM and achieves state-of-the-art performance...

---

## 21. Semi-Automatic Flute Robot and Its Acoustic Sensing

**Authors**: Hikari Kuriyama, Hiroaki Sonoda, Kouki Tomiyoshi, Gou Koutaki  
**Categories**: cs.SD  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14180  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14180v1.pdf

**Abstract**:
> arXiv:2603.14180v1 Announce Type: cross 
Abstract: Flute performance requires mastery of complex fingering combinations and register-dependent embouchure control, particularly jet offset adjustment for low-register production. Existing haptic and semi-automated systems do not address both aspects simultaneously through mechanical actuation. To our knowledge, no prior system fully automates fingering while mechanically assisting low-register tone production without requiring embouchure control. We developed a semi-automatic flute robot with an automatic fingering mechanism: fourteen servo motors actuate all keys via wire-based and rack-and-pinion drives in response to MIDI input, enabling performers to produce complete musical pieces through airflow alone. A jet offset assist mechanism rota...

---

## 22. Controllable Accent Normalization via Discrete Diffusion

**Authors**: Qibing Bai, Yuhan Du, Tom Ko, Shuai Wang, Yannan Wang, Haizhou Li  
**Categories**: cs.SD  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14275  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14275v1.pdf

**Abstract**:
> arXiv:2603.14275v1 Announce Type: cross 
Abstract: Existing accent normalization methods do not typically offer control over accent strength, yet many applications-such as language learning and dubbing-require tunable accent retention. We propose DLM-AN, a controllable accent normalization system built on masked discrete diffusion over self-supervised speech tokens. A Common Token Predictor identifies source tokens that likely encode native pronunciation; these tokens are selectively reused to initialize the reverse diffusion process. This provides a simple yet effective mechanism for controlling accent strength: reusing more tokens preserves more of the original accent. DLM-AN further incorporates a flow-matching Duration Ratio Predictor that automatically adjusts the total duration to be...

---

## 23. PARSA-Bench: A Comprehensive Persian Audio-Language Model Benchmark

**Authors**: Mohammad Javad Ranjbar Kalahroodi, Mohammad Amini, Parmis Bathayan, Heshaam Faili, Azadeh Shakery  
**Categories**: cs.SD  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14456  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14456v1.pdf

**Abstract**:
> arXiv:2603.14456v1 Announce Type: cross 
Abstract: Persian poses unique audio understanding challenges through its classical poetry, traditional music, and pervasive code-switching - none captured by existing benchmarks. We introduce PARSA-Bench (Persian Audio Reasoning and Speech Assessment Benchmark), the first benchmark for evaluating large audio-language models on Persian language and culture, comprising 16 tasks and over 8,000 samples across speech understanding, paralinguistic analysis, and cultural audio understanding. Ten tasks are newly introduced, including poetry meter and style detection, traditional Persian music understanding, and code-switching detection. Text-only baselines consistently outperform audio counterparts, suggesting models may not leverage audio-specific informa...

---

## 24. ReactMotion: Generating Reactive Listener Motions from Speaker Utterance

**Authors**: Cheng Luo, Bizhu Wu, Bing Li, Jianfeng Ren, Ruibin Bai, Rong Qu, Linlin Shen, Bernard Ghanem  
**Categories**: cs.SD  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15083  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15083v1.pdf

**Abstract**:
> arXiv:2603.15083v1 Announce Type: cross 
Abstract: In this paper, we introduce a new task, Reactive Listener Motion Generation from Speaker Utterance, which aims to generate naturalistic listener body motions that appropriately respond to a speaker's utterance. However, modeling such nonverbal listener behaviors remains underexplored and challenging due to the inherently non-deterministic nature of human reactions. To facilitate this task, we present ReactMotionNet, a large-scale dataset that pairs speaker utterances with multiple candidate listener motions annotated with varying degrees of appropriateness. This dataset design explicitly captures the one-to-many nature of listener behavior and provides supervision beyond a single ground-truth motion. Building on this dataset design, we dev...

---

## 25. Nested Music Transformer: Sequentially Decoding Compound Tokens in Symbolic Music and Audio Generation

**Authors**: HaeJun Yoo, Hao-Wen Dong, Jongmin Jung, Dasaem Jeong  
**Categories**: cs.SD  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2408.01180  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2408.01180v2.pdf

**Abstract**:
> arXiv:2408.01180v2 Announce Type: replace 
Abstract: Representing symbolic music with compound tokens, where each token consists of several different sub-tokens representing a distinct musical feature or attribute, offers the advantage of reducing sequence length. While previous research has validated the efficacy of compound tokens in music sequence modeling, predicting all sub-tokens simultaneously can lead to suboptimal results as it may not fully capture the interdependencies between them. We introduce the Nested Music Transformer (NMT), an architecture tailored for decoding compound tokens autoregressively, similar to processing flattened tokens, but with low memory usage. The NMT consists of two transformers: the main decoder that models a sequence of compound tokens and the sub-deco...

---

## 26. The silence of the weights: a structural pruning strategy for attention-based audio signal architectures with second order metrics

**Authors**: Andrea Diecidue, Carlo Alberto Barbano, Piero Fraternali, Mathieu Fontaine, Enzo Tartaglione  
**Categories**: cs.SD  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2509.26207  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2509.26207v2.pdf

**Abstract**:
> arXiv:2509.26207v2 Announce Type: replace 
Abstract: Transformer-based models have become the state of the art across multiple domains, from natural language processing to machine listening, thanks to the attention mechanisms. However, the attention layers require a large number of parameters and high-end hardware for both training and inference. We propose a novel channel-pruning technique explicitly targeted at the attention mechanism, decoupling the pruning of each head and the four layers in the attention block: query, key, value, and output projection matrices, employing a second-order metric to score the network's parameters. We compare our technique against head-pruning strategies and magnitude-driven scoring metrics, investigating the effects of pruning on Audio Spectrogram Transfo...

---

## 27. SAKE: Towards Editing Auditory Attribute Knowledge of Large Audio-Language Models

**Authors**: Chih-Kai Yang, Yen-Ting Piao, Tzu-Wen Hsu, Szu-Wei Fu, Zhehuai Chen, Ke-Han Lu, Sung-Feng Huang, Cha...  
**Categories**: cs.SD  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.16917  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.16917v2.pdf

**Abstract**:
> arXiv:2510.16917v2 Announce Type: replace 
Abstract: Knowledge editing enables targeted updates without retraining, but prior work focuses on textual or visual facts, leaving abstract auditory perceptual knowledge underexplored. We introduce SAKE, the first benchmark for editing perceptual auditory attribute knowledge in large audio-language models (LALMs), which requires modifying acoustic generalization rather than isolated facts. We evaluate eight diverse editing methods on three LALMs across reliability, generality, locality, and portability, under single and sequential edits. Results show that most methods enforce edits reliably but struggle with auditory generalization, intra-attribute locality, and multimodal knowledge propagation, and often exhibit forgetting or degeneration in seq...

---

## 28. AWARE: Audio Watermarking with Adversarial Resistance to Edits

**Authors**: Kosta Pavlovi\'c, Lazar Stanarevi\'c, Petar Nedi\'c, Elena Ne\v{s}ovi\'c Slavko Kova\v{c}evi\'c, Igo...  
**Categories**: cs.SD  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.17512  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.17512v2.pdf

**Abstract**:
> arXiv:2510.17512v2 Announce Type: replace 
Abstract: Prevailing practice in learning-based audio watermarking is to pursue robustness by expanding the set of simulated distortions during training. However, such surrogates are narrow and prone to overfitting. This paper presents AWARE (Audio Watermarking with Adversarial Resistance to Edits), an alternative approach that avoids reliance on attack-simulation stacks and handcrafted differentiable distortions. Embedding is obtained through adversarial optimization in the time-frequency domain under a level-proportional perceptual budget. Detection employs a time-order-agnostic detector with a Bitwise Readout Head (BRH) that aggregates temporal evidence into one score per watermark bit, enabling reliable watermark decoding even under desynchron...

---

## 29. LAMB: LLM-based Audio Captioning with Modality Gap Bridging via Cauchy-Schwarz Divergence

**Authors**: Hyeongkeun Lee, Jongmin Choi, KiHyun Nam, Joon Son Chung  
**Categories**: cs.SD  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2601.04658  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2601.04658v2.pdf

**Abstract**:
> arXiv:2601.04658v2 Announce Type: replace 
Abstract: Automated Audio Captioning aims to describe the semantic content of input audio. Recent works have employed large language models (LLMs) as a text decoder to leverage their reasoning capabilities. However, prior approaches that project audio features into the LLM embedding space without considering cross-modal alignment fail to fully utilize these capabilities. To address this, we propose LAMB, an LLM-based audio captioning framework that bridges the modality gap between audio embeddings and the LLM text embedding space. LAMB incorporates a Cross-Modal Aligner that minimizes Cauchy-Schwarz divergence while maximizing mutual information, yielding tighter alignment between audio and text at both global and token levels. We further design a...

---

## 30. Stable Differentiable Modal Synthesis for Learning Nonlinear Dynamics

**Authors**: Victor Zheleznov, Stefan Bilbao, Alec Wright, Simon King  
**Categories**: cs.SD  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2601.10453  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2601.10453v3.pdf

**Abstract**:
> arXiv:2601.10453v3 Announce Type: replace 
Abstract: Modal methods are a long-standing approach to physical modelling synthesis. Extensions to nonlinear problems are possible, leading to coupled nonlinear systems of ordinary differential equations. Recent work in scalar auxiliary variable techniques has enabled construction of explicit and stable numerical solvers for such systems. On the other hand, neural ordinary differential equations have been successful in modelling nonlinear systems from data. In this work, we examine how scalar auxiliary variable techniques can be combined with neural ordinary differential equations to yield a stable differentiable model capable of learning nonlinear dynamics. The proposed approach leverages the analytical solution for linear vibration of the syste...

---

## 31. EmotionThinker: Prosody-Aware Reinforcement Learning for Explainable Speech Emotion Reasoning

**Authors**: Dingdong Wang, Shujie Liu, Tianhua Zhang, Youjun Chen, Jinyu Li, Helen Meng  
**Categories**: cs.SD  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2601.15668  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2601.15668v2.pdf

**Abstract**:
> arXiv:2601.15668v2 Announce Type: replace 
Abstract: Emotional information in speech plays a unique role in multimodal perception. However, current Speech Large Language Models (SpeechLLMs), similar to conventional speech emotion recognition (SER) systems, still treat emotion understanding as a simple classification problem. This provides limited interpretability of predictions, while leaving the LLMs' expressive and reasoning capabilities underutilized. In this work, we take the first step to reformulate SER as a deep reasoning problem through reinforcement learning (RL). We propose EmotionThinker, which is designed to generate accurate emotion predictions with interpretable explanations grounded in fine-grained acoustic cues. To achieve this, we first construct EmotionCoT-35K, an emotion...

---

## 32. Self Voice Conversion as an Attack against Neural Audio Watermarking

**Authors**: Yigitcan \"Ozer, Wanying Ge, Zhe Zhang, Xin Wang, Junichi Yamagishi  
**Categories**: cs.SD  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2601.20432  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2601.20432v2.pdf

**Abstract**:
> arXiv:2601.20432v2 Announce Type: replace 
Abstract: Audio watermarking embeds auxiliary information into speech while maintaining speaker identity, linguistic content, and perceptual quality. Although recent advances in neural and digital signal processing-based watermarking methods have improved imperceptibility and embedding capacity, robustness is still primarily assessed against conventional distortions such as compression, additive noise, and resampling. However, the rise of deep learning-based attacks introduces novel and significant threats to watermark security. In this work, we investigate self voice conversion as a universal, content-preserving attack against audio watermarking systems. Self voice conversion remaps a speaker's voice to the same identity while altering acoustic c...

---

## 33. Latent-Mark: An Audio Watermark Robust to Neural Resynthesis

**Authors**: Yen-Shan Chen, Shih-Yu Lai, Ying-Jung Tsou, Yi-Cheng Lin, Bing-Yu Chen, Yun-Nung Chen, Hung-yi Lee, ...  
**Categories**: cs.SD  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.05310  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.05310v2.pdf

**Abstract**:
> arXiv:2603.05310v2 Announce Type: replace 
Abstract: While existing audio watermarking techniques have achieved strong robustness against traditional digital signal processing (DSP) attacks, they remain vulnerable to neural resynthesis. This occurs because modern neural audio codecs act as semantic filters and discard the imperceptible waveform variations used in prior watermarking methods. To address this limitation, we propose Latent-Mark, the first zero-bit audio watermarking framework designed to survive semantic compression. Our key insight is that robustness to the encode-decode process requires embedding the watermark within the codec's invariant latent space. We achieve this by optimizing the audio waveform to induce a detectable directional shift in its encoded latent representati...

---

## 34. DAST: A Dual-Stream Voice Anonymization Attacker with Staged Training

**Authors**: Ridwan Arefeen, Xiaoxiao Miao, Rong Tong, Aik Beng Ng, Simon See, Timothy Liu  
**Categories**: cs.SD  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12840  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12840v2.pdf

**Abstract**:
> arXiv:2603.12840v2 Announce Type: replace 
Abstract: Voice anonymization masks vocal traits while preserving linguistic content, which may still leak speaker-specific patterns. To assess and strengthen privacy evaluation, we propose a dual-stream attacker that fuses spectral and self-supervised learning features via parallel encoders with a three-stage training strategy. Stage I establishes foundational speaker-discriminative representations. Stage II leverages the shared identity-transformation characteristics of voice conversion and anonymization, exposing the model to diverse converted speech to build cross-system robustness. Stage III provides lightweight adaptation to target anonymized data. Results on the VoicePrivacy Attacker Challenge (VPAC) dataset demonstrate that Stage II is the...

---

## 35. MMSU: A Massive Multi-task Spoken Language Understanding and Reasoning Benchmark

**Authors**: Dingdong Wang, Junan Li, Jincenzi Wu, Dongchao Yang, Xueyuan Chen, Tianhua Zhang, Helen Meng  
**Categories**: cs.SD  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2506.04779  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2506.04779v3.pdf

**Abstract**:
> arXiv:2506.04779v3 Announce Type: replace-cross 
Abstract: Speech inherently contains rich acoustic information that extends far beyond the textual language. In real-world spoken language understanding, effective interpretation often requires integrating semantic meaning (e.g., content), paralinguistic features (e.g., emotions, speed, pitch) and phonological characteristics (e.g., prosody, intonation, rhythm), which are embedded in speech. While recent multimodal Speech Large Language Models (SpeechLLMs) have demonstrated remarkable capabilities in processing audio information, their ability to perform fine-grained perception and complex reasoning in natural speech remains largely unexplored. To address this gap, we introduce MMSU, a comprehensive benchmark designed specifically for unders...

---

## 36. Data-Efficient ASR Personalization for Non-Normative Speech Using an Uncertainty-Based Phoneme Difficulty Score for Guided Sampling

**Authors**: Niclas Pokel, Pehu\'en Moure, Roman B\"ohringer, Yingqiang Gao  
**Categories**: cs.SD  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2509.20396  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2509.20396v2.pdf

**Abstract**:
> arXiv:2509.20396v2 Announce Type: replace-cross 
Abstract: ASR systems struggle with non-normative speech due to high acoustic variability and data scarcity. We propose a data-efficient method using phoneme-level uncertainty to guide fine-tuning for personalization. Instead of computationally expensive ensembles, we leverage Variational Low-Rank Adaptation (VI LoRA) to estimate epistemic uncertainty in foundation models. These estimates form a composite Phoneme Difficulty Score (PhDScore) that drives a targeted oversampling strategy. Evaluated on English and German datasets, including a longitudinal analysis against two clinical reports taken one year apart, we demonstrate that: (1) VI LoRA-based uncertainty aligns better with expert clinical assessments than standard entropy; (2) PhDScore...

---

## 37. Dynamic Stress Detection: A Study of Temporal Progression Modelling of Stress in Speech

**Authors**: Vishakha Lall, Yisi Liu  
**Categories**: cs.SD  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.08586  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.08586v2.pdf

**Abstract**:
> arXiv:2510.08586v2 Announce Type: replace-cross 
Abstract: Detecting psychological stress from speech is critical in high-pressure settings. While prior work has leveraged acoustic features for stress detection, most treat stress as a static label. In this work, we model stress as a temporally evolving phenomenon influenced by historical emotional state. We propose a dynamic labelling strategy that derives fine-grained stress annotations from emotional labels and introduce cross-attention-based sequential models, a Unidirectional LSTM and a Transformer Encoder, to capture temporal stress progression. Our approach achieves notable accuracy gains on MuSE (+5%) and StressID (+18%) over existing baselines, and generalises well to a custom real-world dataset. These results highlight the value o...

---

## 38. Omni-Captioner: Data Pipeline, Models, and Benchmark for Omni Detailed Perception

**Authors**: Ziyang Ma, Ruiyang Xu, Zhenghao Xing, Yunfei Chu, Yuxuan Wang, Jinzheng He, Jin Xu, Pheng-Ann Heng, ...  
**Categories**: cs.SD  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.12720  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.12720v2.pdf

**Abstract**:
> arXiv:2510.12720v2 Announce Type: replace-cross 
Abstract: Fine-grained perception of multimodal information is critical for advancing human-AI interaction. With recent progress in audio-visual technologies, Omni Language Models (OLMs), capable of processing audio and video signals in parallel, have emerged as a promising paradigm for achieving richer understanding and reasoning. However, their capacity to capture and describe fine-grained details remains limited explored. In this work, we present a systematic and comprehensive investigation of omni detailed perception from the perspectives of the data pipeline, models, and benchmark. We first identify an inherent "co-growth" between detail and hallucination in current OLMs. To address this, we propose Omni-Detective, an agentic data gener...

---

## 39. A Language-Agnostic Hierarchical LoRA-MoE Architecture for CTC-based Multilingual ASR

**Authors**: Yuang Zheng, Dongxu Chen, Yuxiang Mei, Dongxing Xu, Jie Chen, Yanhua Long  
**Categories**: cs.SD  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2601.00557  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2601.00557v2.pdf

**Abstract**:
> arXiv:2601.00557v2 Announce Type: replace-cross 
Abstract: Large-scale multilingual ASR (mASR) models such as Whisper achieve strong performance but incur high computational and latency costs, limiting their deployment on resource-constrained edge devices. In this study, we propose a lightweight and language-agnostic multilingual ASR system based on a CTC architecture with domain adaptation. Specifically, we introduce a Language-agnostic Hierarchical LoRA-MoE (HLoRA) framework integrated into an mHuBERT-CTC model, enabling end-to-end decoding via LID-posterior-driven LoRA routing. The hierarchical design consists of a multilingual shared LoRA for learning language-invariant acoustic representations and language-specific LoRA experts for modeling language-dependent characteristics. The prop...

---

## 40. SoulX-Singer: Towards High-Quality Zero-Shot Singing Voice Synthesis

**Authors**: Jiale Qian, Hao Meng, Tian Zheng, Pengcheng Zhu, Haopeng Lin, Yuhang Dai, Hanke Xie, Wenxiao Cao, Ru...  
**Categories**: cs.SD  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.07803  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.07803v2.pdf

**Abstract**:
> arXiv:2602.07803v2 Announce Type: replace-cross 
Abstract: While recent years have witnessed rapid progress in speech synthesis, open-source singing voice synthesis (SVS) systems still face significant barriers to industrial deployment, particularly in terms of robustness and zero-shot generalization. In this report, we introduce SoulX-Singer, a high-quality open-source SVS system designed with practical deployment considerations in mind. SoulX-Singer supports controllable singing generation conditioned on either symbolic musical scores (MIDI) or melodic representations, enabling flexible and expressive control in real-world production workflows. Trained on more than 42,000 hours of vocal data, the system supports Mandarin Chinese, English, and Cantonese and consistently achieves state-of-...

---

## 41. Understanding the strengths and weaknesses of SSL models for audio deepfake model attribution

**Authors**: Gabriel P\^irlogeanu, Adriana Stan, Horia Cucu  
**Categories**: eess.AS  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13488  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13488v1.pdf

**Abstract**:
> arXiv:2603.13488v1 Announce Type: new 
Abstract: Audio deepfake model attribution aims to mitigate the misuse of synthetic speech by identifying the source model responsible for generating a given audio sample, enabling accountability and informing vendors. The task is challenging, but self-supervised learning (SSL)-derived acoustic features have demonstrated state-of-the-art attribution capabilities, yet the underlying factors driving their success and the limits of their discriminative power remain unclear. In this paper, we systematically investigate how SSL-derived features capture architectural signatures in audio deepfakes. By controlling multiple dimensions of the audio generation process we reveal how subtle perturbations in model checkpoints, text prompts, vocoders, or speaker ide...

---

## 42. Evaluating Pretrained General-Purpose Audio Representations for Music Genre Classification

**Authors**: Kashish Rai, Mrinmoy Bhattacharjee  
**Categories**: eess.AS  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13871  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13871v1.pdf

**Abstract**:
> arXiv:2603.13871v1 Announce Type: new 
Abstract: This study investigates the use of self-supervised learning embeddings, particularly BYOL-A, in conjunction with a deep neural network classifier for Music Genre Classification. Our experiments demonstrate that BYOL-A embeddings outperform other pre-trained models, such as PANNs and VGGish, achieving an accuracy of 81.5% on the GTZAN dataset and 64.3% on FMA-Small. The proposed DNN classifier improved performance by 10-16% over linear classifiers. We explore the effects of contrastive and triplet loss and multitask training with optimized loss weights, achieving the highest accuracy. To address cross dataset challenges, we combined GTZAN and FMA-Small into a unified 18-class label space for joint training, resulting in slight performance dro...

---

## 43. Beyond Two-stage Diffusion TTS: Joint Structure and Content Refinement via Jump Diffusion

**Authors**: Jiabao Ai, Minghui Zhao, Anton Ragni  
**Categories**: eess.AS  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14032  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14032v1.pdf

**Abstract**:
> arXiv:2603.14032v1 Announce Type: new 
Abstract: Diffusion and flow matching TTS faces a tension between discrete temporal structure and continuous spectral modeling. Two-stage models diffuse on fixed alignments, often collapsing to mean prosody; single-stage models avoid explicit durations but suffer alignment instability. We propose a jump-diffusion framework where discrete jumps model temporal structure and continuous diffusion refines spectral content within one process. Even in its one-shot degenerate form, our framework achieves 3.37% WER vs. 4.38% for Grad-TTS with improved UTMOSv2 on LJSpeech. The full iterative UDD variant further enables adaptive prosody, autonomously inserting natural pauses in out-of-distribution slow speech rather than stretching uniformly. Audio samples are a...

---

## 44. SoulX-Duplug: Plug-and-Play Streaming State Prediction Module for Realtime Full-Duplex Speech Conversation

**Authors**: Ruiqi Yan, Wenxi Chen, Zhanxun Liu, Ziyang Ma, Haopeng Lin, Hanlin Wen, Hanke Xie, Jun Wu, Yuzhe Lia...  
**Categories**: eess.AS  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14877  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14877v1.pdf

**Abstract**:
> arXiv:2603.14877v1 Announce Type: new 
Abstract: Recent advances in spoken dialogue systems have brought increased attention to human-like full-duplex voice interactions. However, our comprehensive review of this field reveals several challenges, including the difficulty in obtaining training data, catastrophic forgetting, and limited scalability. In this work, we propose SoulX-Duplug, a plug-and-play streaming state prediction module for full-duplex spoken dialogue systems. By jointly performing streaming ASR, SoulX-Duplug explicitly leverages textual information to identify user intent, effectively serving as a semantic VAD. To promote fair evaluation, we introduce SoulX-Duplug-Eval, extending widely used benchmarks with improved bilingual coverage. Experimental results show that SoulX-D...

---

## 45. Modeling and Benchmarking Spoken Dialogue Rewards with Modality and Colloquialness

**Authors**: Jingyu Lu, Yuhan Wang, Fan Zhuo, Xize Cheng, Changhao Pan, Xueyi Pu, Yifu Chen, Chenyuhao Wen, Tianl...  
**Categories**: eess.AS  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14889  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14889v1.pdf

**Abstract**:
> arXiv:2603.14889v1 Announce Type: new 
Abstract: The rapid evolution of end-to-end spoken dialogue systems demands transcending mere textual semantics to incorporate paralinguistic nuances and the spontaneous nature of human conversation. However, current methods struggle with two critical gaps: the modality gap, involving prosody and emotion, and the colloquialness gap, distinguishing written scripts from natural speech. To address these challenges, we introduce SDiaReward, an end-to-end multi-turn reward model trained on SDiaReward-Dataset, a novel collection of episode-level preference pairs explicitly targeting these gaps. It operates directly on full multi-turn speech episodes and is optimized with pairwise preference supervision, enabling joint assessment of modality and colloquialne...

---

## 46. Spectrogram features for audio and speech analysis

**Authors**: Ian McLoughlin, Lam Pham, Yan Song, Xiaoxiao Miao, Huy Phan, Pengfei Cai, Qing Gu, Jiang Nan, Haoyu ...  
**Categories**: eess.AS  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14917  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14917v1.pdf

**Abstract**:
> arXiv:2603.14917v1 Announce Type: new 
Abstract: Spectrogram-based representations have grown to dominate the feature space for deep learning audio analysis systems, and are often adopted for speech analysis also. Initially, the primary motivator for spectrogram-based representations was their ability to present sound as a two dimensional signal in the time-frequency plane, which not only provides an interpretable physical basis for analysing sound, but also unlocks the use of a wide range of machine learning techniques such as convolutional neural networks, that had been developed for image processing. A spectrogram is a matrix characterised by the resolution and span of its two dimensions, as well as by the representation and scaling of each element. Many possibilities for these three ch...

---

## 47. Deep Filter Estimation from Inter-Frame Correlations for Monaural Speech Dereverberation

**Authors**: Ui-Hyeop Shin, Jun Hyung Kim, Jangyeon Kim, Wooseok Kim, Hyung-Min Park  
**Categories**: eess.AS  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14986  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14986v1.pdf

**Abstract**:
> arXiv:2603.14986v1 Announce Type: new 
Abstract: Speech dereverberation in distant-microphone scenarios remains challenging due to the high correlation between reverberation and target signals, often leading to poor generalization in real-world environments. We propose IF-CorrNet, a correlation-to-filter architecture designed for robustness against acoustic variability. Unlike conventional black-box mapping methods that directly estimate complex spectra, IF-CorrNet explicitly exploits inter-frame STFT correlations to estimate multi-frame deep filters for each time-frequency bin. By shifting the learning objective from direct mapping to filter estimation, the network effectively constrains the solution space, which simplifies the training process and mitigates overfitting to synthetic data....

---

## 48. How Attention Shapes Emotion: A Comparative Study of Attention Mechanisms for Speech Emotion Recognition

**Authors**: Marc Casals-Salvador, Federico Costa, Rodolfo Zevallos, Javier Hernando  
**Categories**: eess.AS  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15120  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15120v1.pdf

**Abstract**:
> arXiv:2603.15120v1 Announce Type: new 
Abstract: Speech Emotion Recognition (SER) plays a key role in advancing human-computer interaction. Attention mechanisms have become the dominant approach for modeling emotional speech due to their ability to capture long-range dependencies and emphasize salient information. However, standard self-attention suffers from quadratic computational and memory complexity, limiting its scalability. In this work, we present a systematic benchmark of optimized attention mechanisms for SER, including RetNet, LightNet, GSA, FoX, and KDA. Experiments on both MSP-Podcast benchmark versions show that while standard self-attention achieves the strongest recognition performance across test sets, efficient attention variants dramatically improve scalability, reducing...

---

## 49. spINAch: A Diachronic Corpus of French Broadcast Speech Controlled for Speakers' Age and Gender

**Authors**: Simon Devauchelle, David Doukhan, R\'emi Uro, Lucas Ondel Yang, Valentin Pelloin, Olympia Imbert-Br\...  
**Categories**: eess.AS  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15516  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15516v1.pdf

**Abstract**:
> arXiv:2603.15516v1 Announce Type: new 
Abstract: We present spINAch, a large diachronic corpus of French speech from radio and television archives, balanced by speakers' gender, age (20-95 years old), and spanning 60 years from 1955 to 2015. The dataset includes over 320 hours of recordings from more than two thousand speakers. The methodology for building the corpus is described, focusing on the quality of collected samples in acoustic terms. The data were automatically transcribed and phonetically aligned to allow studies at a phonemic level. More than 3 million oral vowels have been analyzed to propose their fundamental frequency and formants. The corpus, available to the community for research purposes, is valuable for describing the evolution of Parisian French through the representat...

---

## 50. MOS-Bias: From Hidden Gender Bias to Gender-Aware Speech Quality Assessment

**Authors**: Wenze Ren, Yi-Cheng Lin, Wen-Chin Huang, Erica Cooper, Ryandhimas E. Zezario, Hsin-Min Wang, Hung-yi...  
**Categories**: eess.AS  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10723  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10723v2.pdf

**Abstract**:
> arXiv:2603.10723v2 Announce Type: replace 
Abstract: The Mean Opinion Score (MOS) serves as the standard metric for speech quality assessment, yet biases in human annotations remain underexplored. We conduct the first systematic analysis of gender bias in MOS, revealing that male listeners consistently assign higher scores than female listeners--a gap that is most pronounced in low-quality speech and gradually diminishes as quality improves. This quality-dependent structure proves difficult to eliminate through simple calibration. We further demonstrate that automated MOS models trained on aggregated labels exhibit predictions skewed toward male standards of perception. To address this, we propose a gender-aware model that learns gender-specific scoring patterns through abstracting binary ...

---

## 51. Room Impulse Response Completion Using Signal-Prediction Diffusion Models Conditioned on Simulated Early Reflections

**Authors**: Zeyu Xu, Andreas Brendel, Albert G. Prinn, Emanu\"el A. P. Habets  
**Categories**: eess.AS  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12442  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12442v2.pdf

**Abstract**:
> arXiv:2603.12442v2 Announce Type: replace 
Abstract: Room impulse responses (RIRs) are fundamental to audio data augmentation, acoustic signal processing, and immersive audio rendering. While geometric simulators such as the image source method (ISM) can efficiently generate early reflections, they lack the realism of measured RIRs due to missing acoustic wave effects. We propose a diffusion-based RIR completion method using signal-prediction conditioned on ISM-simulated direct-path and early reflections. Unlike state-of-the-art methods, our approach imposes no fixed duration constraint on the input early reflections. We further incorporate classifier-free guidance to steer generation toward a target distribution learned from physically realistic RIRs simulated with the Treble SDK. Objecti...

---

## 52. Translational Gaps in Graph Transformers for Longitudinal EHR Prediction: A Critical Appraisal of GT-BEHRT

**Authors**: Krish Tadigotla  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13231  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13231v1.pdf

**Abstract**:
> arXiv:2603.13231v1 Announce Type: new 
Abstract: Transformer-based models have improved predictive modeling on longitudinal electronic health records through large-scale self-supervised pretraining. However, most EHR transformer architectures treat each clinical encounter as an unordered collection of codes, which limits their ability to capture meaningful relationships within a visit. Graph-transformer approaches aim to address this limitation by modeling visit-level structure while retaining the ability to learn long-term temporal patterns. This paper provides a critical review of GT-BEHRT, a graph-transformer architecture evaluated on MIMIC-IV intensive care outcomes and heart failure prediction in the All of Us Research Program. We examine whether the reported performance gains reflect...

---

## 53. Continual Fine-Tuning with Provably Accurate and Parameter-Free Task Retrieval

**Authors**: Hang Thi-Thuy Le, Long Minh Bui, Minh Hoang, Trong Nghia Hoang  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13235  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13235v1.pdf

**Abstract**:
> arXiv:2603.13235v1 Announce Type: new 
Abstract: Continual fine-tuning aims to adapt a pre-trained backbone to new tasks sequentially while preserving performance on earlier tasks whose data are no longer available. Existing approaches fall into two categories which include input- and parameter-adaptation. Input-adaptation methods rely on retrieving the most relevant prompts at test time, but require continuously learning a retrieval function that is prone to forgetting. Parameter-adaptation methods instead use a fixed input embedding function to enable retrieval-free prediction and avoid forgetting, but sacrifice representation adaptability. To combine their best strengths, we propose a new parameter-adaptation method that enables adaptive use of input embeddings during test time with par...

---

## 54. Knowledge, Rules and Their Embeddings: Two Paths towards Neuro-Symbolic JEPA

**Authors**: Yongchao Huang, Hassan Raza  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13265  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13265v1.pdf

**Abstract**:
> arXiv:2603.13265v1 Announce Type: new 
Abstract: Modern self-supervised predictive architectures excel at capturing complex statistical correlations from high-dimensional data but lack mechanisms to internalize verifiable human logic, leaving them susceptible to spurious correlations and shortcut learning. Conversely, traditional rule-based inference systems offer rigorous, interpretable logic but suffer from discrete boundaries and NP-hard combinatorial explosion. To bridge this divide, we propose a bidirectional neuro-symbolic framework centered around Rule-informed Joint-Embedding Predictive Architectures (RiJEPA). In the first direction, we inject structured inductive biases into JEPA training via Energy-Based Constraints (EBC) and a multi-modal dual-encoder architecture. This fundamen...

---

## 55. CAMEL-CLIP: Channel-aware Multimodal Electroencephalography-text Alignment for Generalizable Brain Foundation Models

**Authors**: Hanseul Choi, Jinyeong Park, Seongwon Jin, Sungho Park, Jibum Kim  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13272  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13272v1.pdf

**Abstract**:
> arXiv:2603.13272v1 Announce Type: new 
Abstract: Electroencephalography (EEG) foundation models have shown promise for learning generalizable representations, yet they remain sensitive to channel heterogeneity, such as changes in channel composition or ordering. We propose channel-aware multimodal EEG-text alignment contrastive language-image pretraining (CAMEL-CLIP), a contrastive EEG-text multimodal foundation model designed to be robust to heterogeneous channel configurations and widely applicable to diverse downstream tasks. CAMEL-CLIP introduces three key components: (1) channel attribute-based positional encoding, which identifies channels through semantic information; (2) dynamic channel projection, which generates variable-length embeddings by independently projecting each channel ...

---

## 56. Spatially Aware Deep Learning for Microclimate Prediction from High-Resolution Geospatial Imagery

**Authors**: Idan Sulami, Alon Itzkovitch, Michael R. Kearney, Moni Shahar, Ofir Levy  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13273  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13273v1.pdf

**Abstract**:
> arXiv:2603.13273v1 Announce Type: new 
Abstract: Microclimate models are essential for linking climate to ecological processes, yet most physically based frameworks estimate temperature independently for each spatial unit and rely on simplified representations of lateral heat exchange. As a result, the spatial scales over which surrounding environmental conditions influence local microclimates remain poorly quantified. Here, we show how remote sensing can help quantify the contribution of spatial context to microclimate temperature predictions. Building on convolutional neural network principles, we designed a task-specific deep neural network and trained a series of models in which the spatial extent of input data was systematically varied. Drone-derived spatial layers and meteorological ...

---

## 57. PREBA: Surgical Duration Prediction via PCA-Weighted Retrieval-Augmented LLMs and Bayesian Averaging Aggregation

**Authors**: Wanyin Wu, Kanxue Li, Baosheng Yu, Haoyun Zhao, Yibing Zhan, Dapeng Tao, Hua Jin  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13275  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13275v1.pdf

**Abstract**:
> arXiv:2603.13275v1 Announce Type: new 
Abstract: Accurate prediction of surgical duration is pivotal for hospital resource management. Although recent supervised learning approaches-from machine learning (ML) to fine-tuned large language models (LLMs)-have shown strong performance, they remain constrained by the need for high-quality labeled data and computationally intensive training. In contrast, zero-shot LLM inference offers a promising training-free alternative but it lacks grounding in institution-specific clinical context (e.g., local demographics and case-mix distributions), making its predictions clinically misaligned and prone to instability. To address these limitations, we present PREBA, a retrieval-augmented framework that integrates PCA-weighted retrieval and Bayesian averagi...

---

## 58. Learning Retrieval Models with Sparse Autoencoders

**Authors**: Thibault Formal, Maxime Louis, Herv\'e Dejean, St\'ephane Clinchant  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13277  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13277v1.pdf

**Abstract**:
> arXiv:2603.13277v1 Announce Type: new 
Abstract: Sparse autoencoders (SAEs) provide a powerful mechanism for decomposing the dense representations produced by Large Language Models (LLMs) into interpretable latent features. We posit that SAEs constitute a natural foundation for Learned Sparse Retrieval (LSR), whose objective is to encode queries and documents into high-dimensional sparse representations optimized for efficient retrieval. In contrast to existing LSR approaches that project input sequences into the vocabulary space, SAE-based representations offer the potential to produce more semantically structured, expressive, and language-agnostic features. Building on this insight, we introduce SPLARE, a method to train SAE-based LSR models. Our experiments, relying on recently released...

---

## 59. DreamReader: An Interpretability Toolkit for Text-to-Image Models

**Authors**: Nirmalendu Prakash, Narmeen Oozeer, Michael Lan, Luka Samkharadze, Phillip Howard, Roy Ka-Wei Lee, D...  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13299  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13299v1.pdf

**Abstract**:
> arXiv:2603.13299v1 Announce Type: new 
Abstract: Despite the rapid adoption of text-to-image (T2I) diffusion models, causal and representation-level analysis remains fragmented and largely limited to isolated probing techniques. To address this gap, we introduce DreamReader: a unified framework that formalizes diffusion interpretability as composable representation operators spanning activation extraction, causal patching, structured ablations, and activation steering across modules and timesteps. DreamReader provides a model-agnostic abstraction layer enabling systematic analysis and intervention across diffusion architectures. Beyond consolidating existing methods, DreamReader introduces three novel intervention primitives for diffusion models: (1) representation fine-tuning (LoReFT) for...

---

## 60. Residual Stream Analysis of Overfitting And Structural Disruptions

**Authors**: Quan Liu, Han Zhou, Wenquan Wu, Hua Wu, Sen Su  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13318  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13318v1.pdf

**Abstract**:
> arXiv:2603.13318v1 Announce Type: new 
Abstract: Ensuring that large language models (LLMs) remain both helpful and harmless poses a significant challenge: fine-tuning on repetitive safety datasets, where unsafe prompts are paired with standard refusal templates, often leads to false refusals, in which benign queries are declined. We first quantify this effect, showing that safety data exhibits substantially lower token entropy and 2-gram diversity (0.048) compared to general instruction data. To uncover the root cause, we introduce FlowLens, a stable PCA-based tool for residual-stream geometry analysis, and reveal that higher proportions of safety examples concentrate variance along a few components, reducing representational smoothness and driving false refusals (false refusal rate rises...

---

## 61. Lipschitz-Based Robustness Certification Under Floating-Point Execution

**Authors**: Toby Murray  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13334  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13334v1.pdf

**Abstract**:
> arXiv:2603.13334v1 Announce Type: new 
Abstract: Sensitivity-based robustness certification has emerged as a practical approach for certifying neural network robustness, including in settings that require verifiable guarantees. A key advantage of these methods is that certification is performed by concrete numerical computation (rather than symbolic reasoning) and scales efficiently with network size. However, as with the vast majority of prior work on robustness certification and verification, the soundness of these methods is typically proved with respect to a semantic model that assumes exact real arithmetic. In reality deployed neural network implementations execute using floating-point arithmetic. This mismatch creates a semantic gap between certified robustness properties and the beh...

---

## 62. MS2MetGAN: Latent-space adversarial training for metabolite-spectrum matching in MS/MS database search

**Authors**: Meng Tsai, Alexzander Dwyer, Estelle Nuckels, Yingfeng Wang  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13342  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13342v1.pdf

**Abstract**:
> arXiv:2603.13342v1 Announce Type: new 
Abstract: Database search is a widely used approach for identifying metabolites from tandem mass spectra (MS/MS). In this strategy, an experimental spectrum is matched against a user-specified database of candidate metabolites, and candidates are ranked such that true metabolite-spectrum matches receive the highest scores. Machine-learning methods have been widely incorporated into database-search-based identification tools and have substantially improved performance. To further improve identification accuracy, we propose a new framework for generating negative training samples. The framework first uses autoencoders to learn latent representations of metabolite structures and MS/MS spectra, thereby recasting metabolite-spectrum matching as matching be...

---

## 63. AI-Driven Predictive Maintenance with Real-Time Contextual Data Fusion for Connected Vehicles: A Multi-Dataset Evaluation

**Authors**: Kushal Khemani (Independent Researcher, India), Anjum Nazir Qureshi (Rajiv Gandhi College of Enginee...  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13343  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13343v1.pdf

**Abstract**:
> arXiv:2603.13343v1 Announce Type: new 
Abstract: Most vehicle predictive maintenance systems rely exclusively on internal diagnostic signals and are validated on deterministic synthetic data, limiting the credibility of reported metrics. This paper presents a simulation-validated proof-of-concept framework for V2X-augmented predictive maintenance, integrating on-board sensor streams with external contextual signals -- road quality, weather, traffic density, and driver behaviour -- acquired via V2X communication and third-party APIs, with inference at the vehicle edge. Field validation on instrumented vehicles is identified as the required next step. Three experiments address common shortcomings of prior work. A feature group ablation study shows that V2X contextual features contribute a 2....

---

## 64. Reconciling In-Context and In-Weight Learning via Dual Representation Space Encoding

**Authors**: Guanyu Chen, Ruichen Wang, Tianren Zhang, Feng Chen  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13459  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13459v1.pdf

**Abstract**:
> arXiv:2603.13459v1 Announce Type: new 
Abstract: In-context learning (ICL) is a valuable capability exhibited by Transformers pretrained on diverse sequence tasks. However, previous studies have observed that ICL often conflicts with the model's inherent in-weight learning (IWL) ability. By examining the representation space learned by a toy model in synthetic experiments, we identify the shared encoding space for context and samples in Transformers as a potential source of this conflict. To address this, we modify the model architecture to separately encode the context and samples into two distinct spaces: a task representation space and a sample representation space. We model these two spaces under a simple yet principled framework, assuming a linear representational structure and treati...

---

## 65. Resolving Interference (RI): Disentangling Models for Improved Model Merging

**Authors**: Pratik Ramesh, George Stoica, Arun Iyer, Leshem Choshen, Judy Hoffman  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13467  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13467v1.pdf

**Abstract**:
> arXiv:2603.13467v1 Announce Type: new 
Abstract: Model merging has shown that multitask models can be created by directly combining the parameters of different models that are each specialized on tasks of interest. However, models trained independently on distinct tasks often exhibit interference that degrades the merged model's performance. To solve this problem, we formally define the notion of Cross-Task Interference as the drift in the representation of the merged model relative to its constituent models. Reducing cross-task interference is key to improving merging performance. To address this issue, we propose our method, Resolving Interference (RI), a light-weight adaptation framework which disentangles expert models to be functionally orthogonal to the space of other tasks, thereby ...

---

## 66. SemRep: Generative Code Representation Learning with Code Transformations

**Authors**: Weichen Li, Jiamin Song, Bogdan Alexandru Stoica, Arav Dhoot, Gabriel Ryan, Shengyu Fu, Kexin Pei  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13640  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13640v1.pdf

**Abstract**:
> arXiv:2603.13640v1 Announce Type: new 
Abstract: Code transformation is a foundational capability in the software development process, where its effectiveness relies on constructing a high-quality code representation to characterize the input code semantics and guide the transformation. Existing approaches treat code transformation as an end-to-end learning task, leaving the construction of the representation needed for semantic reasoning implicit in model weights or relying on rigid compiler-level abstractions. We present SemRep, a framework that improves code transformation through generative code representation learning. Our key insight is to employ the semantics-preserving transformations as the intermediate representation, which serves as both a generative mid-training task and the gu...

---

## 67. Quantum-Enhanced Vision Transformer for Flood Detection using Remote Sensing Imagery

**Authors**: Soumyajit Maity, Behzad Ghanbarian  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13689  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13689v1.pdf

**Abstract**:
> arXiv:2603.13689v1 Announce Type: new 
Abstract: Reliable flood detection is critical for disaster management, yet classical deep learning models often struggle with the high-dimensional, nonlinear complexities inherent in remote sensing data. To mitigate these limitations, we introduced a novel Quantum-Enhanced Vision Transformer (ViT) that synergizes the global context-awareness of transformers with the expressive feature extraction capabilities of quantum computing. Using remote sensing imagery, we developed a hybrid architecture that processes inputs through parallel pathways, a ViT backbone and a quantum branch utilizing a 4-qubit parameterized quantum circuit for localized feature mapping. These distinct representations were fused to optimize binary classification. Results showed tha...

---

## 68. Manifold-Orthogonal Dual-spectrum Extrapolation for Parameterized Physics-Informed Neural Networks

**Authors**: Zhangyong Liang, Ji Zhang  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13751  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13751v1.pdf

**Abstract**:
> arXiv:2603.13751v1 Announce Type: new 
Abstract: Physics-informed neural networks (PINNs) have achieved notable success in modeling dynamical systems governed by partial differential equations (PDEs). To avoid computationally expensive retraining under new physical conditions, parameterized PINNs (P$^2$INNs) commonly adapt pre-trained operators using singular value decomposition (SVD) for out-of-distribution (OOD) regimes. However, SVD-based fine-tuning often suffers from rigid subspace locking and truncation of important high-frequency spectral modes, limiting its ability to capture complex physical transitions. While parameter-efficient fine-tuning (PEFT) methods appear to be promising alternatives, applying conventional adapters such as LoRA to P$^2$INNs introduces a severe Pareto trade...

---

## 69. Node Role-Guided LLMs for Dynamic Graph Clustering

**Authors**: Dongyuan Li, Ying Zhang, Yaozu Wu, Renhe Jiang  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13799  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13799v1.pdf

**Abstract**:
> arXiv:2603.13799v1 Announce Type: new 
Abstract: Dynamic graph clustering aims to detect and track time-varying clusters in dynamic graphs, revealing how complex real-world systems evolve over time. However, existing methods are predominantly black-box models. They lack interpretability in their clustering decisions and fail to provide semantic explanations of why clusters form or how they evolve, severely limiting their use in safety-critical domains such as healthcare or transportation. To address these limitations, we propose an end-to-end interpretable framework that maps continuous graph embeddings into discrete semantic concepts through learnable prototypes. Specifically, we first decompose node representations into orthogonal role and clustering subspaces, so that nodes with similar...

---

## 70. Exploring the Dimensions of a Variational Neuron

**Authors**: Yves Ruffenach  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13849  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13849v1.pdf

**Abstract**:
> arXiv:2603.13849v1 Announce Type: new 
Abstract: We introduce EVE (Elemental Variational Expanse), a variational distributional neuron formulated as a local probabilistic computational unit with an explicit prior, an amortized posterior, and unit-level variational regularization. In most modern architectures, uncertainty is modeled through global latent variables or parameter uncertainty, while the computational unit itself remains scalar. EVE instead relocates probabilistic structure to the neuron level, making it locally observable and controllable.
  In this paper, the term dimensions refers primarily to the neuron's internal latent dimensionality, denoted by k. We study how varying k, from the atomic case k = 1 to higher-dimensional latent spaces, changes the neuron's learned operating...

---

## 71. OrigamiBench: An Interactive Environment to Synthesize Flat-Foldable Origamis

**Authors**: Naaisha Agarwal, Yihan Wu, Yichang Jian, Yikuan Hu, Nishad Mansoor, Mohan Li, Yifei Peng, Wang-Zhou ...  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13856  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13856v1.pdf

**Abstract**:
> arXiv:2603.13856v1 Announce Type: new 
Abstract: Building AI systems that can plan, act, and create in the physical world requires more than pattern recognition. Such systems must understand the causal mechanisms and constraints governing physical processes in order to guide sequential decisions. This capability relies on internal representations, analogous to an internal language model, that relate observations, actions, and resulting environmental changes. However, many existing benchmarks treat visual perception and programmatic reasoning as separate problems, focusing either on visual recognition or on symbolic tasks. The domain of origami provides a natural testbed that integrates these modalities. Constructing shapes through folding operations requires visual perception, reasoning ab...

---

## 72. On Interpolation Formulas Describing Neural Network Generalization

**Authors**: Jin Guo, Roy Y. He, Jean-Michel Morel  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13872  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13872v1.pdf

**Abstract**:
> arXiv:2603.13872v1 Announce Type: new 
Abstract: In 2020 Domingos introduced an interpolation formula valid for "every model trained by gradient descent". He concluded that such models behave approximately as kernel machines. In this work, we extend the Domingos formula to stochastic training. We introduce a stochastic gradient kernel that extends the deterministic version via a continuous-time diffusion approximation. We prove stochastic Domingos theorems and show that the expected network output admits a kernel-machine representation with optimizer-specific weighting. It reveals that training samples contribute through loss-dependent weights and gradient alignment along the training trajectory. We then link the generalization error to the null space of the integral operator induced by th...

---

## 73. Enhancing Mental Health Classification with Layer-Attentive Residuals and Contrastive Feature Learning

**Authors**: Menna Elgabry, Ali Hamdi, Khaled Shaban  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14075  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14075v1.pdf

**Abstract**:
> arXiv:2603.14075v1 Announce Type: new 
Abstract: The classification of mental health is challenging for a variety of reasons. For one, there is overlap between the mental health issues. In addition, the signs of mental health issues depend on the context of the situation, making classification difficult. Although fine-tuning transformers has improved the performance for mental health classification, standard cross-entropy training tends to create entangled feature spaces and fails to utilize all the information the transformers contain. We present a new framework that focuses on representations to improve mental health classification. This is done using two methods. First, \textbf{layer-attentive residual aggregation} which works on residual connections to to weigh and fuse representations...

---

## 74. Understanding the Emergence of Seemingly Useless Features in Next-Token Predictors

**Authors**: Mark Rofin, Jalal Naghiyev, Michael Hahn  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14087  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14087v1.pdf

**Abstract**:
> arXiv:2603.14087v1 Announce Type: new 
Abstract: Trained Transformers have been shown to compute abstract features that appear redundant for predicting the immediate next token. We identify which components of the gradient signal from the next-token prediction objective give rise to this phenomenon, and we propose a method to estimate the influence of those components on the emergence of specific features. After validating our approach on toy tasks, we use it to interpret the origins of the world model in OthelloGPT and syntactic features in a small language model. Finally, we apply our framework to a pretrained LLM, showing that features with extremely high or low influence on future tokens tend to be related to formal reasoning domains such as code. Overall, our work takes a step toward ...

---

## 75. Not All Latent Spaces Are Flat: Hyperbolic Concept Control

**Authors**: Maria Rosaria Briglia, Simone Facchiano, Paolo Cursi, Alessio Sampieri, Emanuele Rodol\`a, Guido Mar...  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14093  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14093v1.pdf

**Abstract**:
> arXiv:2603.14093v1 Announce Type: new 
Abstract: As modern text-to-image (T2I) models draw closer to synthesizing highly realistic content, the threat of unsafe content generation grows, and it becomes paramount to exercise control. Existing approaches steer these models by applying Euclidean adjustments to text embeddings, redirecting the generation away from unsafe concepts. In this work, we introduce hyperbolic control (HyCon): a novel control mechanism based on parallel transport that leverages semantically aligned hyperbolic representation space to yield more expressive and stable manipulation of concepts. HyCon reuses off-the-shelf generative models and a state-of-the-art hyperbolic text encoder, linked via a lightweight adapter. HyCon achieves state-of-the-art results across four sa...

---

## 76. Is the reconstruction loss culprit? An attempt to outperform JEPA

**Authors**: Alexey Potapov, Oleg Shcherbakov, Ivan Kravchenko  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14131  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14131v1.pdf

**Abstract**:
> arXiv:2603.14131v1 Announce Type: new 
Abstract: We evaluate JEPA-style predictive representation learning versus reconstruction-based autoencoders on a controlled "TV-series" linear dynamical system with known latent state and a single noise parameter. While an initial comparison suggests JEPA is markedly more robust to noise, further diagnostics show that autoencoder failures are strongly influenced by asymmetries in objectives and by bottleneck/component-selection effects (confirmed by PCA baselines). Motivated by these findings, we introduce gated predictive autoencoders that learn to select predictable components, mimicking the beneficial feature-selection behavior observed in over-parameterized PCA. On this toy testbed, the proposed gated model is stable across noise levels and match...

---

## 77. Hybrid Intent-Aware Personalization with Machine Learning and RAG-Enabled Large Language Models for Financial Services Marketing

**Authors**: Akhil Chandra Shanivendra  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14173  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14173v1.pdf

**Abstract**:
> arXiv:2603.14173v1 Announce Type: new 
Abstract: Personalized marketing in financial services requires models that can both predict customer behavior and generate compliant, context-appropriate content. This paper presents a hybrid architecture that integrates classical machine learning for segmentation, latent intent modeling, and personalization prediction with retrieval-augmented large language models for grounded content generation. A synthetic, reproducible dataset is constructed to reflect temporal customer behavior, product interactions, and marketing responses. The proposed framework incorporates temporal encoders, latent representations, and multi-task classification to estimate segment membership, customer intent, and product-channel recommendations. A retrieval-augmented generat...

---

## 78. Self-Indexing KVCache: Predicting Sparse Attention from Compressed Keys

**Authors**: Xu Yang, Jiapeng Zhang, Dongyang Zhao, Guo Chen, Zhuo Tang  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14224  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14224v1.pdf

**Abstract**:
> arXiv:2603.14224v1 Announce Type: new 
Abstract: The KV cache in self-attention has emerged as a major bottleneck in long-context and large-batch inference for LLMs. Existing approaches often treat sparsity prediction and compression as separate modules, relying on auxiliary index structures to select relevant tokens, and on complex quantization schemes to reduce memory usage. This fragmented design introduces redundant overhead and limits scalability.
  In this paper, we propose a novel paradigm: treating the compressed key representation not merely as storage, but as a self-indexing structure that directly enables efficient sparse attention. By designing a sign-based 1-bit vector quantization (VQ) scheme, our method unifies compression and retrieval in a single, hardware-friendly format....

---

## 79. Domain-Skewed Federated Learning with Feature Decoupling and Calibration

**Authors**: Huan Wang, Jun Shen, Jun Yan, Guansong Pang  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14238  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14238v1.pdf

**Abstract**:
> arXiv:2603.14238v1 Announce Type: new 
Abstract: Federated learning (FL) allows distributed clients to collaboratively train a global model in a privacy-preserving manner. However, one major challenge is domain skew, where clients' data originating from diverse domains may hinder the aggregated global model from learning a consistent representation space, resulting in poor generalizable ability in multiple domains. In this paper, we argue that the domain skew is reflected in the domain-specific biased features of each client, causing the local model's representations to collapse into a narrow low-dimensional subspace. We then propose Federated Feature Decoupling and Calibration ($F^2$DC), which liberates valuable class-relevant information by calibrating the domain-specific biased features...

---

## 80. Learning in Function Spaces: An Unified Functional Analytic View of Supervised and Unsupervised Learning

**Authors**: K. Lakshmanan  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14272  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14272v1.pdf

**Abstract**:
> arXiv:2603.14272v1 Announce Type: new 
Abstract: Many machine learning algorithms can be interpreted as procedures for estimating functions defined on the data distribution. In this paper we present a conceptual framework that formulates a wide range of learning problems as variational optimization over function spaces induced by the data distribution. Within this framework the data distribution defines operators that capture structural properties of the data, such as similarity relations or statistical dependencies. Learning algorithms can then be viewed as estimating functions expressed in bases determined by these operators.
  This perspective provides a unified way to interpret several learning paradigms. In supervised learning the objective functional is defined using labeled data and...

---

## 81. High-Fidelity Compression of Seismic Velocity Models via SIREN Auto-Decoders

**Authors**: Caiyun Liu, Xiaoxue Luo, Jie Xiong  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14284  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14284v1.pdf

**Abstract**:
> arXiv:2603.14284v1 Announce Type: new 
Abstract: Implicit Neural Representations (INRs) have emerged as a powerful paradigm for representing continuous signals independently of grid resolution. In this paper, we propose a high-fidelity neural compression framework based on a SIREN (Sinusoidal Representation Networks) auto-decoder to represent multi-structural seismic velocity models from the OpenFWI benchmark. Our method compresses each 70x70 velocity map (4,900 points) into a compact 256-dimensional latent vector, achieving a compression ratio of 19:1. We evaluate the framework on 1,000 samples across five diverse geological families: FlatVel, CurveVel, FlatFault, CurveFault, and Style. Experimental results demonstrate an average PSNR of 32.47 dB and SSIM of 0.956, indicating high-quality...

---

## 82. Localizing and Editing Knowledge in Large Audio-Language Models

**Authors**: Sung Kyun Chung, Jiaheng Dong, Qiuchi Hu, Gongping Huang, Hong Jia, Ting Dang  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14343  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14343v1.pdf

**Abstract**:
> arXiv:2603.14343v1 Announce Type: new 
Abstract: Large Audio-Language Models (LALMs) have shown strong performance in speech understanding, making speech a natural interface for accessing factual information. Yet they are trained on static corpora and may encode incorrect facts. Existing model editing methods localize and update facts in text-only LLMs, but do not account for continuous speech representations, or where knowledge is stored across acoustic or language modules, or their cross-modal module. We construct the first audio benchmark for knowledge localization and editing in LALMs and propose a speech-driven locate-then-edit framework. First, we use speech-aware causal tracing to localize layers and modules that support factual retrieval and then apply editing at identified sites. ...

---

## 83. Deconfounded Lifelong Learning for Autonomous Driving via Dynamic Knowledge Spaces

**Authors**: Jiayuan Du, Yuebing Song, Yiming Zhao, Xianghui Pan, Jiawei Lian, Yuchu Lu, Liuyi Wang, Chengju Liu,...  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14354  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14354v1.pdf

**Abstract**:
> arXiv:2603.14354v1 Announce Type: new 
Abstract: End-to-End autonomous driving (E2E-AD) systems face challenges in lifelong learning, including catastrophic forgetting, difficulty in knowledge transfer across diverse scenarios, and spurious correlations between unobservable confounders and true driving intents. To address these issues, we propose DeLL, a Deconfounded Lifelong Learning framework that integrates a Dirichlet process mixture model (DPMM) with the front-door adjustment mechanism from causal inference. The DPMM is employed to construct two dynamic knowledge spaces: a trajectory knowledge space for clustering explicit driving behaviors and an implicit feature knowledge space for discovering latent driving abilities. Leveraging the non-parametric Bayesian nature of DPMM, our frame...

---

## 84. From Specification to Architecture: A Theory Compiler for Knowledge-Guided Machine Learning

**Authors**: Asela Hevapathige, Yu Xia, Sachith Seneviratne, Saman Halgamuge  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14369  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14369v1.pdf

**Abstract**:
> arXiv:2603.14369v1 Announce Type: new 
Abstract: Theory-guided machine learning has demonstrated that including authentic domain knowledge directly into model design improves performance, sample efficiency and out-of-distribution generalisation. Yet the process by which a formal domain theory is translated into architectural constraints remains entirely manual, specific to each domain formalism, and devoid of any formal correctness guarantee. This translation is non-transferable between domains, not verified, and does not scale. We propose the Theory Compiler: a system that accepts a typed, machine-readable domain theory as input and automatically produces an architecture whose function space is provably constrained to be consistent with that theory by construction, not by regularisation. ...

---

## 85. WestWorld: A Knowledge-Encoded Scalable Trajectory World Model for Diverse Robotic Systems

**Authors**: Yuchen Wang, Jiangtao Kong, Sizhe Wei, Xiaochang Li, Haohong Lin, Hongjue Zhao, Tianyi Zhou, Lu Gan,...  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14392  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14392v1.pdf

**Abstract**:
> arXiv:2603.14392v1 Announce Type: new 
Abstract: Trajectory world models play a crucial role in robotic dynamics learning, planning, and control. While recent works have explored trajectory world models for diverse robotic systems, they struggle to scale to a large number of distinct system dynamics and overlook domain knowledge of physical structures. To address these limitations, we introduce WestWorld, a knoWledge-Encoded Scalable Trajectory World model for diverse robotic systems. To tackle the scalability challenge, we propose a novel system-aware Mixture-of-Experts (Sys-MoE) that dynamically combines and routes specialized experts for different robotic systems via a learnable system embedding. To further enhance zero-shot generalization, we incorporate domain knowledge of robot physi...

---

## 86. ES-Merging: Biological MLLM Merging via Embedding Space Signals

**Authors**: Wonbin Lee, Dongki Kim, Sung Ju Hwang  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14405  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14405v1.pdf

**Abstract**:
> arXiv:2603.14405v1 Announce Type: new 
Abstract: Biological multimodal large language models (MLLMs) have emerged as powerful foundation models for scientific discovery. However, existing models are specialized to a single modality, limiting their ability to solve inherently cross-modal scientific problems. While model merging is an efficient method to combine the different modalities into a unified MLLM, existing methods rely on input-agnostic parameter space heuristics that fail to faithfully capture modality specialization. To overcome this limitation, we propose a representation-aware merging framework that estimates merging coefficients from embedding space signals. We first design a probe input that consists of different modality tokens and forward it through each specialized MLLM to...

---

## 87. Towards One-for-All Anomaly Detection for Tabular Data

**Authors**: Shiyuan Li, Yixin Liu, Yu Zheng, Xiaofeng Cao, Shirui Pan, Heng Tao Shen  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14407  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14407v1.pdf

**Abstract**:
> arXiv:2603.14407v1 Announce Type: new 
Abstract: Tabular anomaly detection (TAD) aims to identify samples that deviate from the majority in tabular data and is critical in many real-world applications. However, existing methods follow a ``one model for one dataset (OFO)'' paradigm, which relies on dataset-specific training and thus incurs high computational cost and yields limited generalization to unseen domains. To address these limitations, we propose OFA-TAD, a generalist one-for-all (OFA) TAD framework that only requires one-time training on multiple source datasets and can generalize to unseen datasets from diverse domains on-the-fly. To realize one-for-all tabular anomaly detection, OFA-TAD extracts neighbor-distance patterns as transferable cues, and introduces multi-view neighbor-...

---

## 88. MBD: A Model-Based Debiasing Framework Across User, Content, and Model Dimensions

**Authors**: Yuantong Li, Lei Yuan, Zhihao Zheng, Weimiao Wu, Songbin Liu, Jeong Min Lee, Ali Selman Aydin, Shaof...  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14422  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14422v1.pdf

**Abstract**:
> arXiv:2603.14422v1 Announce Type: new 
Abstract: Modern recommendation systems rank candidates by aggregating multiple behavioral signals through a value model. However, many commonly used signals are inherently affected by heterogeneous biases. For example, watch time naturally favors long-form content, loop rate favors short - form content, and comment probability favors videos over images. Such biases introduce two critical issues: (1) value model scores may be systematically misaligned with users' relative preferences - for instance, a seemingly low absolute like probability may represent exceptionally strong interest for a user who rarely engages; and (2) changes in value modeling rules can trigger abrupt and undesirable ecosystem shifts. In this work, we ask a fundamental question: c...

---

## 89. Disentangling Dynamical Systems: Causal Representation Learning Meets Local Sparse Attention

**Authors**: Markus W. Baumgartner, Anson Lei, Joe Watson, Ingmar Posner  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14483  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14483v1.pdf

**Abstract**:
> arXiv:2603.14483v1 Announce Type: new 
Abstract: Parametric system identification methods estimate the parameters of explicitly defined physical systems from data. Yet, they remain constrained by the need to provide an explicit function space, typically through a predefined library of candidate functions chosen via available domain knowledge. In contrast, deep learning can demonstrably model systems of broad complexity with high fidelity, but black-box function approximation typically fails to yield explicit descriptive or disentangled representations revealing the structure of a system. We develop a novel identifiability theorem, leveraging causal representation learning, to uncover disentangled representations of system parameters without structural assumptions. We derive a graphical cri...

---

## 90. A Multi-Scale Graph Learning Framework with Temporal Consistency Constraints for Financial Fraud Detection in Transaction Networks under Non-Stationary Conditions

**Authors**: Yiming Lei, Qiannan Shen, Junhao Song  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14592  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14592v1.pdf

**Abstract**:
> arXiv:2603.14592v1 Announce Type: new 
Abstract: Financial fraud detection in transaction networks involves modeling sparse anomalies, dynamic patterns, and severe class imbalance in the presence of temporal drift in the data. In real-world transaction systems, a suspicious transaction is rarely isolated: rather, legitimate and suspicious transactions are often connected through accounts, intermediaries or through temporal transaction sequences. Attribute-based or randomly partitioned learning pipelines are therefore insufficient to detect relationally structured fraud. STC-MixHop, a graph-based framework combining spatial multi-resolution propagation with lightweight temporal consistency modeling for anomaly and fraud detection in dynamic transaction networks. It integrates three componen...

---

## 91. \texttt{BayesBreak}: Generalized Hierarchical Bayesian Segmentation with Irregular Designs, Multi-Sample Hierarchies, and Grouped/Latent-Group Designs

**Authors**: Omid Shams Solari  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14681  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14681v1.pdf

**Abstract**:
> arXiv:2603.14681v1 Announce Type: new 
Abstract: Bayesian change-point and segmentation models provide uncertainty-aware piecewise-constant representations of ordered data, but exact inference is often tied to narrow likelihood classes, single-sequence settings, or index-uniform designs. We present \texttt{BayesBreak}, a modular offline Bayesian segmentation framework built around a simple separation: each candidate block contributes a marginal likelihood and any required moment numerators, and a global dynamic program combines those block scores into posterior quantities over segment counts, boundary locations, and latent signals. For weighted exponential-family likelihoods with conjugate priors, block evidences and posterior moments are available in closed form from cumulative sufficient...

---

## 92. LaPro-DTA: Latent Dual-View Drug Representations and Salient Protein Feature Extraction for Generalizable Drug--Target Affinity Prediction

**Authors**: Zihan Dun, Liuyi Xu, An-Yang Lu, Shuang Li, Yining Qian  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14792  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14792v1.pdf

**Abstract**:
> arXiv:2603.14792v1 Announce Type: new 
Abstract: Drug--target affinity prediction is pivotal for accelerating drug discovery, yet existing methods suffer from significant performance degradation in realistic cold-start scenarios (unseen drugs/targets/pairs), primarily driven by overfitting to training instances and information loss from irrelevant target sequences. In this paper, we propose LaPro-DTA, a framework designed to achieve robust and generalizable DTA prediction. To tackle overfitting, we devise a latent dual-view drug representation mechanism. It synergizes an instance-level view to capture fine-grained substructures with stochastic perturbation and a distribution-level view to distill generalized chemical scaffolds via semantic remapping, thereby enforcing the model to learn tr...

---

## 93. Multi-Task Genetic Algorithm with Multi-Granularity Encoding for Protein-Nucleotide Binding Site Prediction

**Authors**: Yiming Gao, Liuyi Xu, Pengshan Cui, Yining Qian, An-Yang Lu, Xianpeng Wang  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14797  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14797v1.pdf

**Abstract**:
> arXiv:2603.14797v1 Announce Type: new 
Abstract: Accurate identification of protein-nucleotide binding sites is fundamental to deciphering molecular mechanisms and accelerating drug discovery. However, current computational methods often struggle with suboptimal performance due to inadequate feature representation and rigid fusion mechanisms, which hinder the effective exploitation of cross-task information synergy. To bridge this gap, we propose MTGA-MGE, a framework that integrates a Multi-Task Genetic Algorithm with Multi-Granularity Encoding to enhance binding site prediction. Specifically, we develop a Multi-Granularity Encoding (MGE) network that synergizes multi-scale convolutions and self-attention mechanisms to distill discriminative signals from high-dimensional, redundant biolog...

---

## 94. Dataset Distillation Efficiently Encodes Low-Dimensional Representations from Gradient-Based Learning of Non-Linear Tasks

**Authors**: Yuri Kinoshita, Naoki Nishikawa, Taro Toyoizumi  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14830  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14830v1.pdf

**Abstract**:
> arXiv:2603.14830v1 Announce Type: new 
Abstract: Dataset distillation, a training-aware data compression technique, has recently attracted increasing attention as an effective tool for mitigating costs of optimization and data storage. However, progress remains largely empirical. Mechanisms underlying the extraction of task-relevant information from the training process and the efficient encoding of such information into synthetic data points remain elusive. In this paper, we theoretically analyze practical algorithms of dataset distillation applied to the gradient-based training of two-layer neural networks with width $L$. By focusing on a non-linear task structure called multi-index model, we prove that the low-dimensional structure of the problem is efficiently encoded into the resultin...

---

## 95. Ablate and Rescue: A Causal Analysis of Residual Stream Hyper-Connections

**Authors**: William Peng, Josheev Rai, Kevin Tseng, Siwei Wang, Sean Wu  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14833  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14833v1.pdf

**Abstract**:
> arXiv:2603.14833v1 Announce Type: new 
Abstract: Multi-stream transformer architectures have recently been proposed as a promising direction for managing representation collapse and the vanishing gradient problem for residual connections, yet their internal mechanisms remain unexplored. In particular, the recently introduced Manifold-Constrained Hyper-Connections (mHC) architecture posits multiple residual streams with constrained interaction, but lacks in-depth mechanistic analysis. We present the first open-source mHC language model (https://huggingface.co/wgpeng/mhc-780m) and analyze the multiple-stream architecture with a suite of representation-level metrics and causal interventions to probe how parallel streams encode and utilize information. Specifically, we introduce a systematic s...

---

## 96. LLM as Graph Kernel: Rethinking Message Passing on Text-Rich Graphs

**Authors**: Ying Zhang, Hang Yu, Haipeng Zhang, Peng Di  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14937  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14937v1.pdf

**Abstract**:
> arXiv:2603.14937v1 Announce Type: new 
Abstract: Text-rich graphs, which integrate complex structural dependencies with abundant textual information, are ubiquitous yet remain challenging for existing learning paradigms. Conventional methods and even LLM-hybrids compress rich text into static embeddings or summaries before structural reasoning, creating an information bottleneck and detaching updates from the raw content. We argue that in text-rich graphs, the text is not merely a node attribute but the primary medium through which structural relationships are manifested. We introduce RAMP, a Raw-text Anchored Message Passing approach that moves beyond using LLMs as mere feature extractors and instead recasts the LLM itself as a graph-native aggregation operator. RAMP exploits the text-ric...

---

## 97. Lightweight User-Personalization Method for Closed Split Computing

**Authors**: Yuya Okada, Takayuki Nishio  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14958  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14958v1.pdf

**Abstract**:
> arXiv:2603.14958v1 Announce Type: new 
Abstract: Split Computing enables collaborative inference between edge devices and the cloud by partitioning a deep neural network into an edge-side head and a server-side tail, reducing latency and limiting exposure of raw input data. However, inference performance often degrades in practical deployments due to user-specific data distribution shifts, unreliable communication, and privacy-oriented perturbations, especially in closed environments where model architectures and parameters are inaccessible. To address this challenge, we propose SALT (Split-Adaptive Lightweight Tuning), a lightweight adaptation framework for closed Split Computing systems. SALT introduces a compact client-side adapter that refines intermediate representations produced by a...

---

## 98. How Log-Barrier Helps Exploration in Policy Optimization

**Authors**: Leonardo Cesani, Matteo Papini, Marcello Restelli  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15001  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15001v1.pdf

**Abstract**:
> arXiv:2603.15001v1 Announce Type: new 
Abstract: Recently, it has been shown that the Stochastic Gradient Bandit (SGB) algorithm converges to a globally optimal policy with a constant learning rate. However, these guarantees rely on unrealistic assumptions about the learning process, namely that the probability of the optimal action is always bounded away from zero. We attribute this to the lack of an explicit exploration mechanism in SGB. To address these limitations, we propose to regularize the SGB objective with a log-barrier on the parametric policy, structurally enforcing a minimal amount of exploration. We prove that Log-Barrier Stochastic Gradient Bandit (LB-SGB) matches the sample complexity of SGB, but also converges (at a slower rate) without any assumptions on the learning proc...

---

## 99. Interpretable Classification of Time Series Using Euler Characteristic Surfaces

**Authors**: Salam Rabindrajit Luwang, Sushovan Majhi, Vishal Mandal, Atish J. Mitra, Md. Nurujjaman, Buddha Nath...  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15079  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15079v1.pdf

**Abstract**:
> arXiv:2603.15079v1 Announce Type: new 
Abstract: Persistent homology (PH) -- the conventional method in topological data analysis -- is computationally expensive, requires further vectorization of its signatures before machine learning (ML) can be applied, and captures information along only the spatial axis. For time series data, we propose Euler Characteristic Surfaces (ECS) as an alternative topological signature based on the Euler characteristic ($\chi$) -- a fundamental topological invariant. The ECS provides a computationally efficient, spatiotemporal, and inherently discretized feature representation that can serve as direct input to ML models. We prove a stability theorem guaranteeing that the ECS remains stable under small perturbations of the input time series. We first demonstra...

---

## 100. CATFormer: When Continual Learning Meets Spiking Transformers With Dynamic Thresholds

**Authors**: Vaishnavi Nagabhushana, Kartikay Agrawal, Ayon Borthakur  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15184  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15184v1.pdf

**Abstract**:
> arXiv:2603.15184v1 Announce Type: new 
Abstract: Although deep neural networks perform extremely well in controlled environments, they fail in real-world scenarios where data isn't available all at once, and the model must adapt to a new data distribution that may or may not follow the initial distribution. Previously acquired knowledge is lost during subsequent updates based on new data. a phenomenon commonly known as catastrophic forgetting. In contrast, the brain can learn without such catastrophic forgetting, irrespective of the number of tasks it encounters. Existing spiking neural networks (SNNs) for class-incremental learning (CIL) suffer a sharp performance drop as tasks accumulate. We here introduce CATFormer (Context Adaptive Threshold Transformer), a scalable framework that over...

---

## 101. Deep learning and the rate of approximation by flows

**Authors**: Jingpu Cheng, Qianxiao Li, Ting Lin, Zuowei Shen  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15363  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15363v1.pdf

**Abstract**:
> arXiv:2603.15363v1 Announce Type: new 
Abstract: We investigate the dependence of the approximation capacity of deep residual networks on its depth in a continuous dynamical systems setting. This can be formulated as the general problem of quantifying the minimal time-horizon required to approximate a diffeomorphism by flows driven by a given family $\mathcal F$ of vector fields. We show that this minimal time can be identified as a geodesic distance on a sub-Finsler manifold of diffeomorphisms, where the local geometry is characterised by a variational principle involving $\mathcal F$. This connects the learning efficiency of target relationships to their compatibility with the learning architectural choice. Further, the results suggest that the key approximation mechanism in deep learnin...

---

## 102. RESQ: A Unified Framework for REliability- and Security Enhancement of Quantized Deep Neural Networks

**Authors**: Ali Soltan Mohammadi, Samira Nazari, Ali Azarpeyvand, Mahdi Taheri, Milos Krstic, Michael Huebner, C...  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15413  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15413v1.pdf

**Abstract**:
> arXiv:2603.15413v1 Announce Type: new 
Abstract: This work proposes a unified three-stage framework that produces a quantized DNN with balanced fault and attack robustness. The first stage improves attack resilience via fine-tuning that desensitizes feature representations to small input perturbations. The second stage reinforces fault resilience through fault-aware fine-tuning under simulated bit-flip faults. Finally, a lightweight post-training adjustment integrates quantization to enhance efficiency and further mitigate fault sensitivity without degrading attack resilience. Experiments on ResNet18, VGG16, EfficientNet, and Swin-Tiny in CIFAR-10, CIFAR-100, and GTSRB show consistent gains of up to 10.35% in attack resilience and 12.47% in fault resilience, while maintaining competitive a...

---

## 103. Federated Learning of Binary Neural Networks: Enabling Low-Cost Inference

**Authors**: Nitin Priyadarshini Shankar, Soham Lahiri, Sheetal Kalyani, Saurav Prakash  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15507  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15507v1.pdf

**Abstract**:
> arXiv:2603.15507v1 Announce Type: new 
Abstract: Federated Learning (FL) preserves privacy by distributing training across devices. However, using DNNs is computationally intensive at the low-powered edge during inference. Edge deployment demands models that simultaneously optimize memory footprint and computational efficiency, a dilemma where conventional DNNs fail by exceeding resource limits. Traditional post-training binarization reduces model size but suffers from severe accuracy loss due to quantization errors. To address these challenges, we propose FedBNN, a rotation-aware binary neural network framework that learns binary representations directly during local training. By encoding each weight as a single bit $\{+1, -1\}$ instead of a $32$-bit float, FedBNN shrinks the model footpr...

---

## 104. OpenClaw-RL: Train Any Agent Simply by Talking

**Authors**: Yinjie Wang, Xuyang Chen, Xiaolong Jin, Mengdi Wang, Ling Yang  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10165  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10165v1.pdf

**Abstract**:
> arXiv:2603.10165v1 Announce Type: cross 
Abstract: Every agent interaction generates a next-state signal, namely the user reply, tool output, terminal or GUI state change that follows each action, yet no existing agentic RL system recovers it as a live, online learning source. We present OpenClaw-RL, a framework built on a simple observation: next-state signals are universal, and policy can learn from all of them simultaneously. Personal conversations, terminal executions, GUI interactions, SWE tasks, and tool-call traces are not separate training problems. They are all interactions that can be used to train the same policy in the same loop. Next-state signals encode two forms of information: evaluative signals, which indicate how well the action performed and are extracted as scalar rewar...

---

## 105. A Hybrid Tsallis-Polarization Impurity Measure for Decision Trees: Theoretical Foundations and Empirical Evaluation

**Authors**: Edouard Lansiaux, Idriss Jairi, Hayfa Zgaya-Biau  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13241  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13241v1.pdf

**Abstract**:
> arXiv:2603.13241v1 Announce Type: cross 
Abstract: We introduce the Integrated Tsallis Combination (ITC), a hybrid impurity measure for decision tree learning that combines normalized Tsallis entropy with an exponential polarization component. While many existing measures sacrifice theoretical soundness for computational efficiency or vice versa, ITC provides a mathematically principled framework that balances both aspects. The core innovation lies in the complementarity between Tsallis entropy's information-theoretic foundations and the polarization component's sensitivity to distributional asymmetry. We establish key theoretical properties-concavity under explicit parameter conditions, proper boundary conditions, and connections to classical measures-and provide a rigorous justification ...

---

## 106. Deep Convolutional Architectures for EEG Classification: A Comparative Study with Temporal Augmentation and Confidence-Based Voting

**Authors**: Aryan Patodiya, Hubert Cecotti  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13261  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13261v1.pdf

**Abstract**:
> arXiv:2603.13261v1 Announce Type: cross 
Abstract: Electroencephalography (EEG) classification plays a key role in brain-computer interface (BCI) systems, yet it remains challenging due to the low signal-to-noise ratio, temporal variability of neural responses, and limited data availability. In this paper, we present a comparative study of deep learning architectures for classifying event-related potentials (ERPs) in EEG signals. The preprocessing pipeline includes bandpass filtering, spatial filtering, and normalization. We design and compare three main pipelines: a 2D convolutional neural network (CNN) using Common Spatial Pattern (CSP), a second 2D CNN trained directly on raw data for a fair comparison, and a 3D CNN that jointly models spatiotemporal representations. To address ERP late...

---

## 107. Bullet Trains: Parallelizing Training of Temporally Precise Spiking Neural Networks

**Authors**: Todd Morrill, Christian Pehle, Anthony Zador  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13283  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13283v1.pdf

**Abstract**:
> arXiv:2603.13283v1 Announce Type: cross 
Abstract: Continuous-time, event-native spiking neural networks (SNNs) operate strictly on spike events, treating spike timing and ordering as the representation rather than an artifact of time discretization. This viewpoint aligns with biological computation and with the native resolution of event sensors and neuromorphic processors, while enabling compute and memory that scale with the number of events. However, two challenges hinder practical, end-to-end trainable event-based SNN systems: 1) exact charge--fire--reset dynamics impose inherently sequential processing of input spikes, and 2) precise spike times must be solved without time bins. We address both. First, we use parallel associative scans to consume multiple input spikes at once, yieldi...

---

## 108. PolyMon: A Unified Framework for Polymer Property Prediction

**Authors**: Gaopeng Ren, Yijie Yang, Jiajun Zhou, Kim E. Jelfs  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13303  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13303v1.pdf

**Abstract**:
> arXiv:2603.13303v1 Announce Type: cross 
Abstract: Accurate prediction of polymer properties is essential for materials design, but remains challenging due to data scarcity, diverse polymer representations, and the lack of systematic evaluation across modelling choices. Here, we present PolyMon, a unified and accessible framework that integrates multiple polymer representations, machine learning methods, and training strategies within a single, accessible platform. PolyMon supports various descriptors and graph construction strategies for polymer representations, and includes a wide range of models, from tabular models to graph neural networks, along with flexible training strategies including multi-fidelity learning, {\Delta}-learning, active learning, and ensemble learning. Using five ke...

---

## 109. Multi-view Attention Fusion of Heterogeneous Hypergraph with Dynamic Behavioral Profiling for Personalized Learning Resource Recommendation

**Authors**: Tao Xie, Yan Li, Yongpan Sheng, Jian Liao  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13310  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13310v1.pdf

**Abstract**:
> arXiv:2603.13310v1 Announce Type: cross 
Abstract: Hypergraph can capture complex and higher-order dependencies among learners and learning resources in personalized educational recommender systems. Many existing hypergraph-based recommendation approaches underexplored the dynamic behavioral processes inherent to learning and often oversimplified the complementary information embedded across multiple dimensions (i.e. views) within hypergraphs. These limitations compromise both the distinctiveness of learned representations and the model's generalization capabilities, especially under data-sparse conditions typical in educational settings. In this study, we propose a unified model comprising a dynamic behavioral profiling module and a multi-view attention fusion module based on heterogeneou...

---

## 110. Self-Supervised Multi-Stage Domain Unlearning for White-Matter Lesion Segmentation

**Authors**: Domen Prelo\v{z}nik, \v{Z}iga \v{S}piclin  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13328  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13328v1.pdf

**Abstract**:
> arXiv:2603.13328v1 Announce Type: cross 
Abstract: Inter-scanner variability of magnetic resonance imaging has an adverse impact on the diagnostic and prognostic quality of the scans and necessitates the development of models robust to domain shift inflicted by the unseen scanner data. Review of recent advances in domain adaptation showed that efficacy of strategies involving modifications or constraints on the latent space appears to be contingent upon the level and/or depth of supervision during model training. In this paper, we therefore propose an unsupervised domain adaptation technique based on self-supervised multi-stage unlearning (SSMSU). Building upon the state-of-the-art segmentation framework nnU-Net, we employ deep supervision at deep encoder stages using domain classifier unl...

---

## 111. Why Grokking Takes So Long: A First-Principles Theory of Representational Phase Transitions

**Authors**: Truong Xuan Khanh, Truong Quynh Hoa, Luu Duc Trung, Phan Thanh Duc  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13331  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13331v1.pdf

**Abstract**:
> arXiv:2603.13331v1 Announce Type: cross 
Abstract: Grokking is the sudden generalization that appears long after a model has perfectly memorized its training data. Although this phenomenon has been widely observed, there is still no quantitative theory explaining the length of the delay between memorization and generalization. Prior work has noted that weight decay plays an important role, but no result derives tight bounds for the delay or explains its scaling behavior.
  We present a first-principles theory showing that grokking arises from a norm-driven representational phase transition in regularized training dynamics. Training first converges to a high-norm memorization solution and only later contracts toward a lower-norm structured representation that generalizes.
  Our main result ...

---

## 112. Multimodal Deep Learning for Dynamic and Static Neuroimaging: Integrating MRI and fMRI for Alzheimer Disease Analysis

**Authors**: Anima Kujur, Zahra Monfared  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13367  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13367v1.pdf

**Abstract**:
> arXiv:2603.13367v1 Announce Type: cross 
Abstract: Magnetic Resonance Imaging (MRI) provides detailed structural information, while functional MRI (fMRI) captures temporal brain activity. In this work, we present a multimodal deep learning framework that integrates MRI and fMRI for multi-class classification of Alzheimer Disease (AD), Mild Cognitive Impairment, and Normal Cognitive State. Structural features are extracted from MRI using 3D convolutional neural networks, while temporal features are learned from fMRI sequences using recurrent architectures. These representations are fused to enable joint spatial-temporal learning. Experiments were conducted on a small paired MRI-fMRI dataset (29 subjects), both with and without data augmentation. Results show that data augmentation substanti...

---

## 113. Ethical Fairness without Demographics in Human-Centered AI

**Authors**: Shaily Roy, Harshit Sharma, Asif Salekin  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13373  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13373v1.pdf

**Abstract**:
> arXiv:2603.13373v1 Announce Type: cross 
Abstract: Computational models are increasingly embedded in human-centered domains such as healthcare, education, workplace analytics, and digital well-being, where their predictions directly influence individual outcomes and collective welfare. In such contexts, achieving high accuracy alone is insufficient; models must also act ethically and equitably across diverse populations. However, fair AI approaches that rely on demographic attributes are impractical, as such information is often unavailable, privacy-sensitive, or restricted by regulatory frameworks. Moreover, conventional parity-based fairness approaches, while aiming for equity, can inadvertently violate core ethical principles by trading off subgroup performance or stability. To address ...

---

## 114. InfiniteDance: Scalable 3D Dance Generation Towards in-the-wild Generalization

**Authors**: Ronghui Li, Zhongyuan Hu, Li Siyao, Youliang Zhang, Haozhe Xie, Mingyuan Zhang, Jie Guo, Xiu Li, Ziw...  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13375  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13375v1.pdf

**Abstract**:
> arXiv:2603.13375v1 Announce Type: cross 
Abstract: Although existing 3D dance generation methods perform well in controlled scenarios, they often struggle to generalize in the wild. When conditioned on unseen music, existing methods often produce unstructured or physically implausible dance, largely due to limited music-to-dance data and restricted model capacity. This work aims to push the frontier of generalizable 3D dance generation by scaling up both data and model design. (1) On the data side, we develop a fully automated pipeline that reconstructs high-fidelity 3D dance motions from monocular videos. To eliminate the physical artifacts prevalent in existing reconstruction methods, we introduce a Foot Restoration Diffusion Model (FRDM) guided by foot-contact and geometric constraints ...

---

## 115. Deep Learning for BioImaging: What Are We Learning?

**Authors**: Ivan Svatko, Maxime Sanchez, Ihab Bendidi, Gilles Cottrell, Auguste Genovesio  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13377  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13377v1.pdf

**Abstract**:
> arXiv:2603.13377v1 Announce Type: cross 
Abstract: Representation learning has driven major advances in natural image analysis by enabling models to acquire high-level semantic features. In microscopy imaging, however, it remains unclear what current representation learning methods actually learn. In this work, we conduct a systematic study of representation learning for the two most widely used and broadly available microscopy data types, representing critical scales in biology: cell culture and tissue imaging. To this end, we introduce a set of simple yet revealing baselines on curated benchmarks, including untrained models and simple structural representations of cellular tissue. Our results show that, surprisingly, state-of-the-art methods perform comparably to these baselines. We furt...

---

## 116. High-Fidelity Text-to-Image Generation from Pre-Trained Vision-Language Models via Distribution-Conditioned Diffusion Decoding

**Authors**: Ji Woo Hong, Hee Suk Yoon, Gwanhyeong Koo, Eunseop Yoon, SooHwan Eom, Qi Dai, Chong Luo, Chang D. Yo...  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13389  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13389v1.pdf

**Abstract**:
> arXiv:2603.13389v1 Announce Type: cross 
Abstract: Recent large-scale vision-language models (VLMs) have shown remarkable text-to-image generation capabilities, yet their visual fidelity remains constrained by the discrete image tokenization, which poses a major challenge. Although several studies have explored continuous representation modeling to enhance visual quality, adapting pre-trained VLM models to such representations requires large-scale data and training costs comparable to the original pre-training. To circumvent this limitation, we propose a diffusion-based decoding framework that enhances image fidelity by training only a diffusion decoder on the output image-token logits of pre-trained VLMs, thereby preserving the original model intact. At its core, Logit-to-Code Distributio...

---

## 117. Synthetic Melanoma Image Generation and Evaluation Using Generative Adversarial Networks

**Authors**: Pei-Yu Lin, Yidan Shen, Neville Mathew, Renjie Hu, Siyu Huang, Courtney M. Queen, Cameron E. West, A...  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13497  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13497v1.pdf

**Abstract**:
> arXiv:2603.13497v1 Announce Type: cross 
Abstract: Melanoma is the most lethal form of skin cancer, and early detection is critical for improving patient outcomes. Although dermoscopy combined with deep learning has advanced automated skin-lesion analysis, progress is hindered by limited access to large, well-annotated datasets and by severe class imbalance, where melanoma images are substantially underrepresented. To address these challenges, we present the first systematic benchmarking study comparing four GAN architectures-DCGAN, StyleGAN2, and two StyleGAN3 variants (T/R)-for high-resolution melanoma-specific synthesis. We train and optimize all models on two expert-annotated benchmarks (ISIC 2018 and ISIC 2020) under unified preprocessing and hyperparameter exploration, with particula...

---

## 118. AMES: Approximate Multi-modal Enterprise Search via Late Interaction Retrieval

**Authors**: Tony Joseph, Carlos Pareja, David Lopes Pegna, Abhishek Singh  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13537  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13537v1.pdf

**Abstract**:
> arXiv:2603.13537v1 Announce Type: cross 
Abstract: We present AMES (Approximate Multimodal Enterprise Search), a unified multimodal late interaction retrieval architecture which is backend agnostic. AMES demonstrates that fine-grained multimodal late interaction retrieval can be deployed within a production grade enterprise search engine without architectural redesign. Text tokens, image patches, and video frames are embedded into a shared representation space using multi-vector encoders, enabling cross-modal retrieval without modality specific retrieval logic. AMES employs a two-stage pipeline: parallel token level ANN search with per document Top-M MaxSim approximation, followed by accelerator optimized Exact MaxSim re-ranking. Experiments on the ViDoRe V3 benchmark show that AMES achiev...

---

## 119. Task-Oriented Wireless Transmission of 3D Point Clouds: Geometric Versus Semantic Robustness

**Authors**: Vukan Ninkovic, Tamara Sobot, Vladimir Vincan, Gorana Gojic, Dragisa Miskovic, Dejan Vukobratovic  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13560  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13560v1.pdf

**Abstract**:
> arXiv:2603.13560v1 Announce Type: cross 
Abstract: Wireless transmission of high-dimensional 3D point clouds (PCs) is increasingly required in industrial collaborative robotics systems. Conventional compression methods prioritize geometric fidelity, although many practical applications ultimately depend on reliable task-level inference rather than exact coordinate reconstruction. In this paper, we propose an end-to-end semantic communication framework for wireless 3D PC transmission and conduct a systematic study of the relationship between geometric reconstruction fidelity and semantic robustness under channel impairments. The proposed architecture jointly supports geometric recovery and object classification from a shared transmitted representation, enabling direct comparison between coo...

---

## 120. SHAMISA: SHAped Modeling of Implicit Structural Associations for Self-supervised No-Reference Image Quality Assessment

**Authors**: Mahdi Naseri, Zhou Wang  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13669  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13669v1.pdf

**Abstract**:
> arXiv:2603.13669v1 Announce Type: cross 
Abstract: No-Reference Image Quality Assessment (NR-IQA) aims to estimate perceptual quality without access to a reference image of pristine quality. Learning an NR-IQA model faces a fundamental bottleneck: its need for a large number of costly human perceptual labels. We propose SHAMISA, a non-contrastive self-supervised framework that learns from unlabeled distorted images by leveraging explicitly structured relational supervision. Unlike prior methods that impose rigid, binary similarity constraints, SHAMISA introduces implicit structural associations, defined as soft, controllable relations that are both distortion-aware and content-sensitive, inferred from synthetic metadata and intrinsic feature structure. A key innovation is our compositional...

---

## 121. Repetition Without Exclusivity: Scale Sensitivity of Referential Mechanisms in Child-Scale Language Models

**Authors**: Jon-Paul Cacioli  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13696  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13696v1.pdf

**Abstract**:
> arXiv:2603.13696v1 Announce Type: cross 
Abstract: We present the first systematic evaluation of mutual exclusivity (ME) -- the bias to map novel words to novel referents -- in text-only language models trained on child-directed speech. We operationalise ME as referential suppression: when a familiar object is relabelled in a two-referent discourse context, ME predicts decreased probability of the labelled noun at a subsequent completion position. Three pilot findings motivate a pre-registered scale-sensitivity experiment: (1) a masked language model (BabyBERTa) is entirely insensitive to multi-sentence referential context; (2) autoregressive models show robust repetition priming -- the opposite of ME -- when familiar nouns are re-labelled; and (3) a novel context-dependence diagnostic rev...

---

## 122. PA-Net: Precipitation-Adaptive Mixture-of-Experts for Long-Tail Rainfall Nowcasting

**Authors**: Xinyu Xiao, Sen Lei, Eryun Liu, Shiming Xiang, Hao Li, Cheng Yuan, Yuan Qi, Qizhao Jin  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13818  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13818v1.pdf

**Abstract**:
> arXiv:2603.13818v1 Announce Type: cross 
Abstract: Precipitation nowcasting is vital for flood warning, agricultural management, and emergency response, yet two bottlenecks persist: the prohibitive cost of modeling million-scale spatiotemporal tokens from multi-variate atmospheric fields, and the extreme long-tailed rainfall distribution where heavy-to-torrential events -- those of greatest societal impact -- constitute fewer than 0.1% of all samples. We propose the Precipitation-Adaptive Network (PA-Net), a Transformer framework whose computational budget is explicitly governed by rainfall intensity. Its core component, Precipitation-Adaptive MoE (PA-MoE), dynamically scales the number of activated experts per token according to local precipitation magnitude, channeling richer representat...

---

## 123. GradMem: Learning to Write Context into Memory with Test-Time Gradient Descent

**Authors**: Yuri Kuratov, Matvey Kairov, Aydar Bulatov, Ivan Rodkin, Mikhail Burtsev  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13875  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13875v1.pdf

**Abstract**:
> arXiv:2603.13875v1 Announce Type: cross 
Abstract: Many large language model applications require conditioning on long contexts. Transformers typically support this by storing a large per-layer KV-cache of past activations, which incurs substantial memory overhead. A desirable alternative is ompressive memory: read a context once, store it in a compact state, and answer many queries from that state. We study this in a context removal setting, where the model must generate an answer without access to the original context at inference time. We introduce GradMem, which writes context into memory via per-sample test-time optimization. Given a context, GradMem performs a few steps of gradient descent on a small set of prefix memory tokens while keeping model weights frozen. GradMem explicitly o...

---

## 124. Pixel-level Scene Understanding in One Token: Visual States Need What-is-Where Composition

**Authors**: Seokmin Lee, Yunghee Lee, Byeonghyun Pak, Byeongju Woo  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13904  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13904v1.pdf

**Abstract**:
> arXiv:2603.13904v1 Announce Type: cross 
Abstract: For robotic agents operating in dynamic environments, learning visual state representations from streaming video observations is essential for sequential decision making. Recent self-supervised learning methods have shown strong transferability across vision tasks, but they do not explicitly address what a good visual state should encode. We argue that effective visual states must capture what-is-where by jointly encoding the semantic identities of scene elements and their spatial locations, enabling reliable detection of subtle dynamics across observations. To this end, we propose CroBo, a visual state representation learning framework based on a global-to-local reconstruction objective. Given a reference observation compressed into a com...

---

## 125. The Phenomenology of Hallucinations

**Authors**: Valeria Ruscio, Keiran Thompson  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13911  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13911v1.pdf

**Abstract**:
> arXiv:2603.13911v1 Announce Type: cross 
Abstract: We show that language models hallucinate not because they fail to detect uncertainty, but because of a failure to integrate it into output generation. Across architectures, uncertain inputs are reliably identified, occupying high-dimensional regions with 2-3$\times$ the intrinsic dimensionality of factual inputs. However, this internal signal is weakly coupled to the output layer: uncertainty migrates into low-sensitivity subspaces, becoming geometrically amplified yet functionally silent. Topological analysis shows that uncertainty representations fragment rather than converging to a unified abstention state, while gradient and Fisher probes reveal collapsing sensitivity along the uncertainty direction. Because cross-entropy training prov...

---

## 126. Generative Inverse Design of Cold Metals for Low-Power Electronics

**Authors**: Kedeng Wu, Yucheng Zhu, Yan Chen, Bizhu Zhang, Shuyu Liu, Xiaobin Deng, Yabei Wu, Liangliang Zhu, Ha...  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13920  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13920v1.pdf

**Abstract**:
> arXiv:2603.13920v1 Announce Type: cross 
Abstract: Cold metals are a class of metals with an intrinsic energy gap located close to the Fermi level, which enables cold-carrier injection for steep-slope transistors and is therefore promising for low-power electronic applications. High-throughput screening has revealed 252 three-dimensional (3D) cold metals in the Materials Project database, but database searches are inherently limited to known compounds. Here we present an inverse-design workflow that generates 3D cold metals using MatterGPT, a conditional autoregressive Transformer trained on SLICES, an invertible and symmetry-invariant crystal string representation. We curate a training set of 26,309 metallic structures labeled with energy above hull and a unified band-edge distance descri...

---

## 127. Sat-JEPA-Diff: Bridging Self-Supervised Learning and Generative Diffusion for Remote Sensing

**Authors**: Kursat Komurcu, Linas Petkevicius  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13943  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13943v1.pdf

**Abstract**:
> arXiv:2603.13943v1 Announce Type: cross 
Abstract: Predicting satellite imagery requires a balance between structural accuracy and textural detail. Standard deterministic methods like PredRNN or SimVP minimize pixel-based errors but suffer from the "regression to the mean" problem, producing blurry outputs that obscure subtle geographic-spatial features. Generative models provide realistic textures but often misleadingly reveal structural anomalies. To bridge this gap, we introduce Sat-JEPA-Diff, which combines Self-Supervised Learning (SSL) with Hidden Diffusion Models (LDM). An IJEPA module predicts stable semantic representations, which then route a frozen Stable Diffusion backbone via a lightweight cross-attention adapter. This ensures that the synthesized high-accuracy textures are ba...

---

## 128. Location Aware Embedding for Geotargeting in Sponsored Search Advertising

**Authors**: Jelena Gligorijevic, Djordje Gligorijevic, Aravindan Raghuveer, Mihajlo Grbovic, Zoran Obradovic  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13997  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13997v1.pdf

**Abstract**:
> arXiv:2603.13997v1 Announce Type: cross 
Abstract: Web search has become an inevitable part of everyday life. Improving and monetizing web search has been a focus of major Internet players. Understanding the context of web search query is an important aspect of this task as it represents unobserved facts that add meaning to an otherwise incomplete query.The context of a query consists of user's location, local time, search history, behavioral segments, installed apps on their phone and so on. Queries that either explicitly use location context (eg: "best hotels in New York City") or implicitly refer to the user's physical location (e.g. "coffee shops near me") are becoming increasingly common on mobile devices. Understanding and representing the user's interest location and/or physical loc...

---

## 129. The Taxonomies, Training, and Applications of Event Stream Modelling for Electronic Health Records

**Authors**: Mingcheng Zhu, Yu Liu, Zhiyao Luo, Tingting Zhu  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14003  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14003v1.pdf

**Abstract**:
> arXiv:2603.14003v1 Announce Type: cross 
Abstract: The widespread adoption of electronic health records (EHRs) enables the acquisition of heterogeneous clinical data, spanning lab tests, vital signs, medications, and procedures, which offer transformative potential for artificial intelligence in healthcare. Although traditional modelling approaches have typically relied on multivariate time series, they often struggle to accommodate the inherent sparsity and irregularity of real-world clinical workflows. Consequently, research has shifted toward event stream representation, which treats patient records as continuous sequences, thereby preserving the precise temporal structure of the patient journey. However, the existing literature remains fragmented, characterised by inconsistent definiti...

---

## 130. Self-Supervised Uncertainty Estimation For Super-Resolution of Satellite Images

**Authors**: Zhe Zheng, Val\'ery Dewil, Pablo Arias  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14074  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14074v1.pdf

**Abstract**:
> arXiv:2603.14074v1 Announce Type: cross 
Abstract: Super-resolution (SR) of satellite imagery is challenging due to the lack of paired low-/high-resolution data. Recent self-supervised SR methods overcome this limitation by exploiting the temporal redundancy in burst observations, but they lack a mechanism to quantify uncertainty in the reconstruction. In this work, we introduce a novel self-supervised loss that allows to estimate uncertainty in image super-resolution without ever accessing the ground-truth high-resolution data. We adopt a decision-theoretic perspective and show that minimizing the corresponding Bayesian risk yields the posterior mean and variance as optimal estimators. We validate our approach on a synthetic SkySat L1B dataset and demonstrate that it produces calibrated u...

---

## 131. DualSwinFusionSeg: Multimodal Martian Landslide Segmentation via Dual Swin Transformer with Multi-Scale Fusion and UNet++

**Authors**: Shahriar Kabir, Abdullah Muhammed Amimul Ehsan, Istiak Ahmmed Rifti, Md Kaykobad Reza  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14132  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14132v1.pdf

**Abstract**:
> arXiv:2603.14132v1 Announce Type: cross 
Abstract: Automated segmentation of Martian landslides, particularly in tectonically active regions such as Valles Marineris,is important for planetary geology, hazard assessment, and future robotic exploration. However, detecting landslides from planetary imagery is challenging due to the heterogeneous nature of available sensing modalities and the limited number of labeled samples. Each observation combines RGB imagery with geophysical measurements such as digital elevation models, slope maps, thermal inertia, and contextual grayscale imagery, which differ significantly in resolution and statistical properties. To address these challenges, we propose DualSwinFusionSeg, a multimodal segmentation architecture that separates modality-specific feature...

---

## 132. Seeking Physics in Diffusion Noise

**Authors**: Chujun Tang, Lei Zhong, Fangqiang Ding  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14294  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14294v1.pdf

**Abstract**:
> arXiv:2603.14294v1 Announce Type: cross 
Abstract: Do video diffusion models encode signals predictive of physical plausibility? We probe intermediate denoising representations of a pretrained Diffusion Transformer (DiT) and find that physically plausible and implausible videos are partially separable in mid-layer feature space across noise levels. This separability cannot be fully attributed to visual quality or generator identity, suggesting recoverable physics-related cues in frozen DiT features. Leveraging this observation, we introduce progressive trajectory selection, an inference-time strategy that scores parallel denoising trajectories at a few intermediate checkpoints using a lightweight physics verifier trained on frozen features, and prunes low-scoring candidates early. Extensiv...

---

## 133. Autonomous Agents Coordinating Distributed Discovery Through Emergent Artifact Exchange

**Authors**: Fiona Y. Wang, Lee Marom, Subhadeep Pal, Rachel K. Luu, Wei Lu, Jaime A. Berkovich, Markus J. Buehle...  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14312  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14312v1.pdf

**Abstract**:
> arXiv:2603.14312v1 Announce Type: cross 
Abstract: We present ScienceClaw + Infinite, a framework for autonomous scientific investigation in which independent agents conduct research without central coordination, and any contributor can deploy new agents into a shared ecosystem. The system is built around three components: an extensible registry of over 300 interoperable scientific skills, an artifact layer that preserves full computational lineage as a directed acyclic graph (DAG), and a structured platform for agent-based scientific discourse with provenance-aware governance. Agents select and chain tools based on their scientific profiles, produce immutable artifacts with typed metadata and parent lineage, and broadcast unsatisfied information needs to a shared global index. The Artifac...

---

## 134. Representation Alignment for Just Image Transformers is not Easier than You Think

**Authors**: Jaeyo Shin, Jiwook Kim, Hyunjung Shim  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14366  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14366v1.pdf

**Abstract**:
> arXiv:2603.14366v1 Announce Type: cross 
Abstract: Representation Alignment (REPA) has emerged as a simple way to accelerate Diffusion Transformers training in latent space. At the same time, pixel-space diffusion transformers such as Just image Transformers (JiT) have attracted growing attention because they remove a dependency on a pretrained tokenizer, and then avoid the reconstruction bottleneck of latent diffusion. This paper shows that the REPA can fail for JiT. REPA yields worse FID for JiT as training proceeds and collapses diversity on image subsets that are tightly clustered in the representation space of pretrained semantic encoder on ImageNet. We trace the failure to an information asymmetry: denoising occurs in the high dimensional image space, while the semantic target is str...

---

## 135. Tactile Modality Fusion for Vision-Language-Action Models

**Authors**: Charlotte Morissette, Amin Abyaneh, Wei-Di Chang, Anas Houssaini, David Meger, Hsiu-Chin Lin, Jonath...  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14604  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14604v1.pdf

**Abstract**:
> arXiv:2603.14604v1 Announce Type: cross 
Abstract: We propose TacFiLM, a lightweight modality-fusion approach that integrates visual-tactile signals into vision-language-action (VLA) models. While recent advances in VLA models have introduced robot policies that are both generalizable and semantically grounded, these models mainly rely on vision-based perception. Vision alone, however, cannot capture the complex interaction dynamics that occur during contact-rich manipulation, including contact forces, surface friction, compliance, and shear. While recent attempts to integrate tactile signals into VLA models often increase complexity through token concatenation or large-scale pretraining, the heavy computational demands of behavioural models necessitate more lightweight fusion strategies. ...

---

## 136. Robust Building Damage Detection in Cross-Disaster Settings Using Domain Adaptation

**Authors**: Asmae Mouradi, Shruti Kshirsagar  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14694  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14694v1.pdf

**Abstract**:
> arXiv:2603.14694v1 Announce Type: cross 
Abstract: Rapid structural damage assessment from remote sensing imagery is essential for timely disaster response. Within human-machine systems (HMS) for disaster management, automated damage detection provides decision-makers with actionable situational awareness. However, models trained on multi-disaster benchmarks often underperform in unseen geographic regions due to domain shift - a distributional mismatch between training and deployment data that undermines human trust in automated assessments. We explore a two-stage ensemble approach using supervised domain adaptation (SDA) for building damage classification across four severity classes. The pipeline adapts the xView2 first-place method to the Ida-BD dataset using SDA and systematically inve...

---

## 137. Design Space of Self--Consistent Electrostatic Machine Learning Interatomic Potentials

**Authors**: William J. Baldwin, Ilyes Batatia, Martin Vondr\'ak, Johannes T. Margraf, G\'abor Cs\'anyi  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14700  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14700v1.pdf

**Abstract**:
> arXiv:2603.14700v1 Announce Type: cross 
Abstract: Machine learning interatomic potentials (MLIPs) have become widely used tools in atomistic simulations. For much of the history of this field, the most commonly employed architectures were based on short-ranged atomic energy contributions, and the assumption of locality still persists in many modern foundation models. While this approach has enabled efficient and accurate modelling for many use cases, it poses intrinsic limitations for systems where long-range electrostatics, charge transfer, or induced polarization play a central role. A growing body of work has proposed extensions that incorporate electrostatic effects, ranging from locally predicted atomic charges to self-consistent models. While these models have demonstrated success f...

---

## 138. AdapterTune: Zero-Initialized Low-Rank Adapters for Frozen Vision Transformers

**Authors**: Salim Khazem  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14706  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14706v1.pdf

**Abstract**:
> arXiv:2603.14706v1 Announce Type: cross 
Abstract: Frozen-backbone transfer with Vision Transformers faces two under-addressed issues: optimization instability when adapters are naively inserted into a fixed feature extractor, and the absence of principled guidance for setting adapter capacity. We introduce AdapterTune, which augments each transformer block with a residual low-rank bottleneck whose up-projection is zero-initialized, guaranteeing that the adapted network starts exactly at the pretrained function and eliminates early-epoch representation drift. On the analytical side, we formalize adapter rank as a capacity budget for approximating downstream task shifts in feature space. The resulting excess-risk decomposition predicts monotonic but diminishing accuracy gains with increasin...

---

## 139. Gauge-Equivariant Intrinsic Neural Operators for Geometry-Consistent Learning of Elliptic PDE Maps

**Authors**: Pengcheng Cheng  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14734  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14734v1.pdf

**Abstract**:
> arXiv:2603.14734v1 Announce Type: cross 
Abstract: Learning solution operators of partial differential equations (PDEs) from data has emerged as a promising route to fast surrogate models in multi-query scientific workflows. However, for geometric PDEs whose inputs and outputs transform under changes of local frame (gauge), many existing operator-learning architectures remain representation-dependent, brittle under metric perturbations, and sensitive to discretization changes. We propose Gauge-Equivariant Intrinsic Neural Operators (GINO), a class of neural operators that parameterize elliptic solution maps primarily through intrinsic spectral multipliers acting on geometry-dependent spectra, coupled with gauge-equivariant nonlinearities. This design decouples geometry from learnable funct...

---

## 140. Face-to-Face: A Video Dataset for Multi-Person Interaction Modeling

**Authors**: Ernie Chu, Vishal M. Patel  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14794  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14794v1.pdf

**Abstract**:
> arXiv:2603.14794v1 Announce Type: cross 
Abstract: Modeling the reactive tempo of human conversation remains difficult because most audio-visual datasets portray isolated speakers delivering short monologues. We introduce \textbf{Face-to-Face with Jimmy Fallon (F2F-JF)}, a 70-hour, 14k-clip dataset of two-person talk-show exchanges that preserves the sequential dependency between a guest turn and the host's response. A semi-automatic pipeline combines multi-person tracking, speech diarization, and lightweight human verification to extract temporally aligned host/guest tracks with tight crops and metadata that are ready for downstream modeling. We showcase the dataset with a reactive, speech-driven digital avatar task in which the host video during $[t_1,t_2]$ is generated from their audio ...

---

## 141. Halfway to 3D: Ensembling 2.5D and 3D Models for Robust COVID-19 CT Diagnosis

**Authors**: Tuan-Anh Yang, Bao V. Q. Bui, Chanh-Quang Vo-Van, Truong-Son Hy  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14832  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14832v1.pdf

**Abstract**:
> arXiv:2603.14832v1 Announce Type: cross 
Abstract: We propose a deep learning framework for COVID-19 detection and disease classification from chest CT scans that integrates both 2.5D and 3D representations to capture complementary slice-level and volumetric information. The 2.5D branch processes multi-view CT slices (axial, coronal, sagittal) using a DINOv3 vision transformer to extract robust visual features, while the 3D branch employs a ResNet-18 architecture to model volumetric context and is pretrained with Variance Risk Extrapolation (VREx) followed by supervised contrastive learning to improve cross-source robustness. Predictions from both branches are combined through logit-level ensemble inference. Experiments on the PHAROS-AIF-MIH benchmark demonstrate the effectiveness of the p...

---

## 142. Machine learning for sustainable geoenergy: uncertainty, physics and decision-ready inference

**Authors**: Hannah P. Menke, Ahmed H. Elsheikh, Lingli Wei, Nanzhe Wang, Andreas Busch  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14907  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14907v1.pdf

**Abstract**:
> arXiv:2603.14907v1 Announce Type: cross 
Abstract: Geoenergy projects (CO2 storage, geothermal, subsurface H2 generation/storage, critical minerals from subsurface fluids, or nuclear waste disposal) increasingly follow a petroleum-style funnel from screening and appraisal to operations, monitoring, and stewardship. Across this funnel, limited and heterogeneous observations must be turned into risk-bounded operational choices under strong physical and geological constraints - choices that control deployment rate, cost of capital, and the credibility of climate-mitigation claims. These choices are inherently multi-objective, balancing performance against containment, pressure footprint, induced seismicity, energy/water intensity, and long-term stewardship. We argue that progress is limited b...

---

## 143. Masked BRep Autoencoder via Hierarchical Graph Transformer

**Authors**: Yifei Li, Kang Wu, Wenming Wu, Xiaoming Fu  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14927  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14927v1.pdf

**Abstract**:
> arXiv:2603.14927v1 Announce Type: cross 
Abstract: We introduce a novel self-supervised learning framework that automatically learns representations from input computer-aided design (CAD) models for downstream tasks, including part classification, modeling segmentation, and machining feature recognition. To train our network, we construct a large-scale, unlabeled dataset of boundary representation (BRep) models. The success of our algorithm relies on two keycomponents. The first is a masked graph autoencoder that reconstructs randomly masked geometries and attributes of BReps for representation learning to enhance the generalization. The second is a hierarchical graph Transformer architecture that elegantly fuses global and local learning by a cross-scale mutual attention block to model lo...

---

## 144. Empowering Chemical Structures with Biological Insights for Scalable Phenotypic Virtual Screening

**Authors**: Xiaoqing Lian, Pengsen Ma, Tengfeng Ma, Zhonghao Ren, Xibao Cai, Zhixiang Cheng, Bosheng Song, He Wa...  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15006  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15006v1.pdf

**Abstract**:
> arXiv:2603.15006v1 Announce Type: cross 
Abstract: Motivation: The scalable identification of bioactive compounds is essential for contemporary drug discovery. This process faces a key trade-off: structural screening offers scalability but lacks biological context, whereas high-content phenotypic profiling provides deep biological insights but is resource-intensive. The primary challenge is to extract robust biological signals from noisy data and encode them into representations that do not require biological data at inference. Results: This study presents DECODE (DEcomposing Cellular Observations of Drug Effects), a framework that bridges this gap by empowering chemical representations with intrinsic biological semantics to enable structure-based in silico biological profiling. DECODE lev...

---

## 145. Interpretable Predictability-Based AI Text Detection: A Replication Study

**Authors**: Adam Skurla, Dominik Macko, Jakub Simko  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15034  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15034v1.pdf

**Abstract**:
> arXiv:2603.15034v1 Announce Type: cross 
Abstract: This paper replicates and extends the system used in the AuTexTification 2023 shared task for authorship attribution of machine-generated texts. First, we tried to reproduce the original results. Exact replication was not possible because of differences in data splits, model availability, and implementation details. Next, we tested newer multilingual language models and added 26 document-level stylometric features. We also applied SHAP analysis to examine which features influence the model's decisions. We replaced the original GPT-2 models with newer generative models such as Qwen and mGPT for computing probabilistic features. For contextual representations, we used mDeBERTa-v3-base and applied the same configuration to both English and Sp...

---

## 146. Thinking in Latents: Adaptive Anchor Refinement for Implicit Reasoning in LLMs

**Authors**: Disha Sheshanarayana, Rajat Subhra Pal, Manjira Sinha, Tirthankar Dasgupta  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15051  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15051v1.pdf

**Abstract**:
> arXiv:2603.15051v1 Announce Type: cross 
Abstract: Token-level Chain-of-Thought (CoT) prompting has become a standard way to elicit multi-step reasoning in large language models (LLMs), especially for mathematical word problems. However, generating long intermediate traces increases output length and inference cost, and can be inefficient when the model could arrive at the correct answer without extensive verbalization. This has motivated latent-space reasoning approaches that shift computation into hidden representations and only emit a final answer. Yet, many latent reasoning methods depend on a fixed number of latent refinement steps at inference, adding another hyperparameter that must be tuned across models and datasets to balance accuracy and efficiency. We introduce AdaAnchor, a lat...

---

## 147. Spatio-temporal probabilistic forecast using MMAF-guided learning

**Authors**: Leonardo Bardi, Imma Valentina Curato, Lorenzo Proietti  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15055  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15055v1.pdf

**Abstract**:
> arXiv:2603.15055v1 Announce Type: cross 
Abstract: We employ stochastic feed-forward neural networks with Gaussian-distributed weights to determine a probabilistic forecast for spatio-temporal raster datasets. The networks are trained using MMAF-guided learning, a generalized Bayesian methodology in which the observed data are preprocessed using an embedding designed to produce a low-dimensional representation that captures their dependence and causal structure. The design of the embedding is theory-guided by the assumption that a spatio-temporal Ornstein-Uhlenbeck process with finite second-order moments generates the observed data. The trained networks, in inference mode, are then used to generate ensemble forecasts by applying different initial conditions at different horizons. Experime...

---

## 148. Generative Semantic HARQ: Latent-Space Text Retransmission and Combining

**Authors**: Bin Han, Yulin Hu, Hans D. Schotten  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15068  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15068v1.pdf

**Abstract**:
> arXiv:2603.15068v1 Announce Type: cross 
Abstract: Semantic communication conveys meaning rather than raw bits, but reliability at the semantic level remains an open challenge. We propose a semantic-level hybrid automatic repeat request (HARQ) framework for text communication, in which a Transformer-variational autoencoder (VAE) codec operates as a lightweight overlay on the conventional protocol stack. The stochastic encoder inherently generates diverse latent representations across retransmissions-providing incremental knowledge (IK) from a single model without dedicated protocol design. On the receiver side, a soft quality estimator triggers retransmissions and a quality-aware combiner merges the received latent vectors within a consistent latent space. We systematically benchmark six s...

---

## 149. Trustworthy Koopman Operator Learning: Invariance Diagnostics and Error Bounds

**Authors**: Gustav Conradie, Nicolas Boull\'e, Jean-Christophe Loiseau, Steven L. Brunton, Matthew J. Colbrook  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15091  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15091v1.pdf

**Abstract**:
> arXiv:2603.15091v1 Announce Type: cross 
Abstract: Koopman operator theory provides a global linear representation of nonlinear dynamics and underpins many data-driven methods. In practice, however, finite-dimensional feature spaces induced by a user-chosen dictionary are rarely invariant, so closure failures and projection errors lead to spurious eigenvalues, misleading Koopman modes, and overconfident forecasts. This paper addresses a central validation problem in data-driven Koopman methods: how to quantify invariance and projection errors for an arbitrary feature space using only snapshot data, and how to use these diagnostics to produce actionable guarantees and guide dictionary refinement? A unified a posteriori methodology is developed for certifying when a Koopman approximation is ...

---

## 150. Storage and selection of multiple chaotic attractors in minimal reservoir computers

**Authors**: Francesco Martinuzzi, Holger Kantz  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15155  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15155v1.pdf

**Abstract**:
> arXiv:2603.15155v1 Announce Type: cross 
Abstract: Modern predictive modeling increasingly calls for a single learned dynamical substrate to operate across multiple regimes. From a dynamical-systems viewpoint, this capability decomposes into the storage of multiple attractors and the selection of the appropriate attractor in response to contextual cues. In reservoir computing (RC), multi-attractor learning has largely been pursued using large, randomly wired reservoirs, on the assumption that stochastic connectivity is required to generate sufficiently rich internal dynamics. At the same time, recent work shows that minimal deterministic reservoirs can match random designs for single-system chaotic forecasting. Under which conditions can minimal topologies learn multiple chaotic attractors...

---

## 151. HindSight: Evaluating Research Idea Generation via Future Impact

**Authors**: Bo Jiang  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15164  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15164v1.pdf

**Abstract**:
> arXiv:2603.15164v1 Announce Type: cross 
Abstract: Evaluating AI-generated research ideas typically relies on LLM judges or human panels -- both subjective and disconnected from actual research impact. We introduce \hs{}, a time-split evaluation framework that measures idea quality by matching generated ideas against real future publications and scoring them by citation impact and venue acceptance. Using a temporal cutoff~$T$, we restrict an idea generation system to pre-$T$ literature, then evaluate its outputs against papers published in the subsequent 30 months. Experiments across 10 AI/ML research topics reveal a striking disconnect: LLM-as-Judge finds no significant difference between retrieval-augmented and vanilla idea generation ($p{=}0.584$), while \hs{} shows the retrieval-augmen...

---

## 152. IConE: Batch Independent Collapse Prevention for Self-Supervised Representation Learning

**Authors**: Konstantinos Almpanakis, Anna Kreshuk  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15263  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15263v1.pdf

**Abstract**:
> arXiv:2603.15263v1 Announce Type: cross 
Abstract: Self-supervised learning (SSL) has revolutionized representation learning, with Joint-Embedding Architectures (JEAs) emerging as an effective approach for capturing semantic features. Existing JEAs rely on implicit or explicit batch interaction -- via negative sampling or statistical regularization -- to prevent representation collapse. This reliance becomes problematic in regimes where batch sizes must be small, such as high-dimensional scientific data, where memory constraints and class imbalance make large, well-balanced batches infeasible. We introduce IConE (Instance-Contrasted Embeddings), a framework that decouples collapse prevention from the training batch size. Rather than enforcing diversity through batch statistics, IConE maint...

---

## 153. Persistence Spheres: a Bi-continuous Linear Representation of Measures for Partial Optimal Transport

**Authors**: Matteo Pegoraro  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15384  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15384v1.pdf

**Abstract**:
> arXiv:2603.15384v1 Announce Type: cross 
Abstract: We improve and extend persistence spheres, introduced in~\cite{pegoraro2025persistence}. Persistence spheres map an integrable measure $\mu$ on the upper half-plane, including persistence diagrams (PDs) as counting measures, to a function $S(\mu)\in C(\mathbb{S}^2)$, and the map is stable with respect to 1-Wasserstein partial transport distance $\mathrm{POT}_1$. Moreover, to the best of our knowledge, persistence spheres are the first explicit representation used in topological machine learning for which continuity of the inverse on the image is established at every compactly supported target. Recent bounded-cardinality bi-Lipschitz embedding results in partial transport spaces, despite being powerful, are not given by the kind of explicit...

---

## 154. A Hybrid Modeling Framework for Crop Prediction Tasks via Dynamic Parameter Calibration and Multi-Task Learning

**Authors**: William Solow, Paola Pesantez-Cabrera, Markus Keller, Lav Khot, Sandhya Saisubramanian, Alan Fern  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15411  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15411v1.pdf

**Abstract**:
> arXiv:2603.15411v1 Announce Type: cross 
Abstract: Accurate prediction of crop states (e.g., phenology stages and cold hardiness) is essential for timely farm management decisions such as irrigation, fertilization, and canopy management to optimize crop yield and quality. While traditional biophysical models can be used for season-long predictions, they lack the precision required for site-specific management. Deep learning methods are a compelling alternative, but can produce biologically unrealistic predictions and require large-scale data. We propose a \emph{hybrid modeling} approach that uses a neural network to parameterize a differentiable biophysical model and leverages multi-task learning for efficient data sharing across crop cultivars in data limited settings. By predicting the \...

---

## 155. Seeing Beyond: Extrapolative Domain Adaptive Panoramic Segmentation

**Authors**: Yuanfan Zheng, Kunyu Peng, Xu Zheng, Kailun Yang  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15475  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15475v1.pdf

**Abstract**:
> arXiv:2603.15475v1 Announce Type: cross 
Abstract: Cross-domain panoramic semantic segmentation has attracted growing interest as it enables comprehensive 360{\deg} scene understanding for real-world applications. However, it remains particularly challenging due to severe geometric Field of View (FoV) distortions and inconsistent open-set semantics across domains. In this work, we formulate an open-set domain adaptation setting, and propose Extrapolative Domain Adaptive Panoramic Segmentation (EDA-PSeg) framework that trains on local perspective views and tests on full 360{\deg} panoramic images, explicitly tackling both geometric FoV shifts across domains and semantic uncertainty arising from previously unseen classes. To this end, we propose the Euler-Margin Attention (EMA), which introd...

---

## 156. Self-Distillation of Hidden Layers for Self-Supervised Representation Learning

**Authors**: Scott C. Lowe, Anthony Fuller, Sageev Oore, Evan Shelhamer, Graham W. Taylor  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15553  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15553v1.pdf

**Abstract**:
> arXiv:2603.15553v1 Announce Type: cross 
Abstract: The landscape of self-supervised learning (SSL) is currently dominated by generative approaches (e.g., MAE) that reconstruct raw low-level data, and predictive approaches (e.g., I-JEPA) that predict high-level abstract embeddings. While generative methods provide strong grounding, they are computationally inefficient for high-redundancy modalities like imagery, and their training objective does not prioritize learning high-level, conceptual features. Conversely, predictive methods often suffer from training instability due to their reliance on the non-stationary targets of final-layer self-distillation. We introduce Bootleg, a method that bridges this divide by tasking the model with predicting latent representations from multiple hidden l...

---

## 157. Co-Design of Memory-Storage Systems for Workload Awareness with Interpretable Models

**Authors**: Jay Sarkar, Vamsi Pavan Rayaprolu, Abhijeet Bhalerao  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15571  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15571v1.pdf

**Abstract**:
> arXiv:2603.15571v1 Announce Type: cross 
Abstract: Solid-state storage architectures based on NAND or emerging memory devices (SSD), are fundamentally architected and optimized for both reliability and performance. Achieving these simultaneous goals requires co-design of memory components with firmware-architected Error Management (EM) algorithms for density- and performance-scaled memory technologies. We describe a Machine Learning (ML) for systems methodology and modeling for co-designing the EM subsystem together with the natural variance inherent to scaled silicon process of memory components underlying SSD technology. The modeling analyzes NAND memory components and EM algorithms interacting with comprehensive suite of synthetic (stress-focused and JEDEC) and emulation (YCSB and simil...

---

## 158. Skeleton Regression: A Graph-Based Approach to Estimation with Manifold Structure

**Authors**: Zeyu Wei, Yen-Chi Chen  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2303.11786  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2303.11786v3.pdf

**Abstract**:
> arXiv:2303.11786v3 Announce Type: replace 
Abstract: We introduce a new regression framework designed to deal with large-scale, complex data that lies around a low-dimensional manifold with noises. Our approach first constructs a graph representation, referred to as the skeleton, to capture the underlying geometric structure. We then define metrics on the skeleton graph and apply nonparametric regression techniques, along with feature transformations based on the graph, to estimate the regression function. We also discuss the limitations of some nonparametric regressors with respect to the general metric space such as the skeleton graph. The proposed regression framework suggests a novel way to deal with data with underlying geometric structures and provides additional advantages in handli...

---

## 159. Tensor Completion Leveraging Graph Information: A Dynamic Regularization Approach with Statistical Guarantees

**Authors**: Kaidong Wang, Qianxin Yi, Yao Wang, Xiuwu Liao, Shaojie Tang, Can Yang  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2310.02543  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2310.02543v2.pdf

**Abstract**:
> arXiv:2310.02543v2 Announce Type: replace 
Abstract: We consider the problem of tensor completion with graphs serving as side information to represent interrelationships among variables. Existing approaches suffer from several limitations: (1) they are often task-specific and lack generality or systematic formulation; (2) they typically treat graphs as static structures, ignoring their inherent dynamism in tensor-based settings; (3) they lack theoretical guarantees on statistical and computational complexity. To address these issues, we introduce a pioneering framework that systematically develops a novel model, theory, and algorithm for dynamic graph-regularized tensor completion. At the modeling level, we establish a rigorous mathematical representation of dynamic graphs and derive a new...

---

## 160. Continuous-time Risk-sensitive Reinforcement Learning via Quadratic Variation Penalty

**Authors**: Yanwei Jia  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2404.12598  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2404.12598v2.pdf

**Abstract**:
> arXiv:2404.12598v2 Announce Type: replace 
Abstract: This paper studies continuous-time risk-sensitive reinforcement learning (RL) under the entropy-regularized, exploratory diffusion process formulation with the exponential-form objective. The risk-sensitive objective arises either as the agent's risk attitude or as a distributionally robust approach against the model uncertainty. Owing to the martingale perspective in Jia and Zhou (J Mach Learn Res 24(161): 1--61, 2023) the risk-sensitive RL problem is shown to be equivalent to ensuring the martingale property of a process involving both the value function and the q-function, augmented by an additional penalty term: the quadratic variation of the value process, capturing the variability of the value-to-go along the trajectory. This chara...

---

## 161. FC-KAN: Function Combinations in Kolmogorov-Arnold Networks

**Authors**: Hoang-Thang Ta, Duy-Quy Thai, Abu Bakar Siddiqur Rahman, Grigori Sidorov, Alexander Gelbukh  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2409.01763  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2409.01763v5.pdf

**Abstract**:
> arXiv:2409.01763v5 Announce Type: replace 
Abstract: In this paper, we introduce FC-KAN, a Kolmogorov-Arnold Network (KAN) that leverages combinations of popular mathematical functions such as B-splines, wavelets, and radial basis functions on low-dimensional data through element-wise operations. We explore several methods for combining the outputs of these functions, including sum, element-wise product, the addition of sum and element-wise product, representations of quadratic and cubic functions, concatenation, linear transformation of the concatenated output, and others. In our experiments, we compare FC-KAN with a multi-layer perceptron network (MLP) and other existing KANs, such as BSRBF-KAN, EfficientKAN, FastKAN, and FasterKAN, on the MNIST and Fashion-MNIST datasets. Two variants o...

---

## 162. On the Adversarial Transferability of Generalized "Skip Connections"

**Authors**: Yisen Wang, Yichuan Mo, Dongxian Wu, Mingjie Li, Xingjun Ma, Zhouchen Lin  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2410.08950  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2410.08950v2.pdf

**Abstract**:
> arXiv:2410.08950v2 Announce Type: replace 
Abstract: Skip connection is an essential ingredient for modern deep models to be deeper and more powerful. Despite their huge success in normal scenarios (state-of-the-art classification performance on natural examples), we investigate and identify an interesting property of skip connections under adversarial scenarios, namely, the use of skip connections allows easier generation of highly transferable adversarial examples. Specifically, in ResNet-like models (with skip connections), we find that biasing backpropagation to favor gradients from skip connections--while suppressing those from residual modules via a decay factor--allows one to craft adversarial examples with high transferability. Based on this insight, we propose the Skip Gradient Me...

---

## 163. Deconfounded Time Series Forecasting: A Causal Inference Approach

**Authors**: Wentao Gao, Xiaojing Du, Wenjun Yu, Xiongren Chen, Yifan Guo, Feiyu Yang  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2410.21328  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2410.21328v2.pdf

**Abstract**:
> arXiv:2410.21328v2 Announce Type: replace 
Abstract: Time series forecasting is a critical task in various domains, where accurate predictions can drive informed decision-making. Traditional forecasting methods often rely on current observations of variables to predict future outcomes, typically overlooking the influence of latent confounders, unobserved variables that simultaneously affect both the predictors and the target outcomes. This oversight can introduce bias and degrade the performance of predictive models. In this study, we address this challenge by proposing an enhanced forecasting approach that incorporates representations of latent confounders derived from historical data. By integrating these confounders into the predictive process, our method aims to improve the accuracy an...

---

## 164. HyReaL: Clustering Attributed Graph via Hyper-Complex Space Representation Learning

**Authors**: Junyang Chen, Yang Lu, Mengke Li, Cuie Yang, Yiqun Zhang, Yiu-ming Cheung  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2411.14727  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2411.14727v3.pdf

**Abstract**:
> arXiv:2411.14727v3 Announce Type: replace 
Abstract: Clustering complex data in the form of attributed graphs has attracted increasing attention, where powerful graph representation is a critical prerequisite. However, the well-known Over-Smoothing (OS) effect makes Graph Convolutional Networks tend to homogenize the representation of graph nodes, while the existing OS solutions focus on alleviating the homogeneity of nodes' embeddings from the aspect of graph topology information, which is inconsistent with the attributed graph clustering objective. Therefore, we introduce hyper-complex space with powerful quaternion feature transformation to enhance the representation learning of the attributes. A generalized \textbf{Hy}per-complex space \textbf{Re}present\textbf{a}tion \textbf{L}earning...

---

## 165. Physics-Informed Deep B-Spline Networks

**Authors**: Zhuoyuan Wang, Raffaele Romagnoli, Saviz Mowlavi, Yorie Nakahira  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2503.16777  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2503.16777v3.pdf

**Abstract**:
> arXiv:2503.16777v3 Announce Type: replace 
Abstract: Physics-informed machine learning offers a promising framework for solving complex partial differential equations (PDEs) by integrating observational data with governing physical laws. However, learning PDEs with varying parameters and changing initial conditions and boundary conditions (ICBCs) with theoretical guarantees remains an open challenge. In this paper, we propose physics-informed deep B-spline networks, a novel technique that approximates a family of PDEs with different parameters and ICBCs by learning B-spline control points through neural networks. The proposed B-spline representation reduces the learning task from predicting solution values over the entire domain to learning a compact set of control points, enforces strict ...

---

## 166. MSDformer: Multi-scale Discrete Transformer For Time Series Generation

**Authors**: Shibo Feng, Zhicheng Chen, Xi Xiao, Zhong Zhang, Qing Li, Xingyu Gao, Peilin Zhao  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2505.14202  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2505.14202v2.pdf

**Abstract**:
> arXiv:2505.14202v2 Announce Type: replace 
Abstract: Discrete Token Modeling (DTM), which employs vector quantization techniques, has demonstrated remarkable success in modeling non-natural language modalities, particularly in time series generation. While our prior work SDformer established the first DTM-based framework to achieve state-of-the-art performance in this domain, two critical limitations persist in existing DTM approaches: 1) their inability to capture multi-scale temporal patterns inherent to complex time series data, and 2) the absence of theoretical foundations to guide model optimization. To address these challenges, we proposes a novel multi-scale DTM-based time series generation method, called Multi-Scale Discrete Transformer (MSDformer). MSDformer employs a multi-scale ...

---

## 167. Generalized and Personalized Federated Learning with Black-Box Foundation Models via Orthogonal Transformations

**Authors**: Eun Gyung Kong, Je Won Yeom, Yonghoon Jeon, Taesup Kim  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2505.19888  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2505.19888v3.pdf

**Abstract**:
> arXiv:2505.19888v3 Announce Type: replace 
Abstract: Federated Learning (FL) facilitates decentralized model training while preserving data privacy. However, achieving both robust generalization and effective personalization simultaneously in heterogeneous (non-IID) environments remains a formidable challenge. Furthermore, the widespread adoption of proprietary Foundation Models (FMs) introduces a critical requirement for dual privacy: (a) protecting sensitive client data and (b) securing the server's valuable intellectual property. This mandates strictly black-box access to the FM. To address these multifaceted challenges, we introduce FedOT, a novel FL framework optimized for black-box FMs. FedOT employs a shared global task-dependent classifier while facilitating local adaptation throug...

---

## 168. Towards Operational Automated Greenhouse Gas Plume Detection and Delineation

**Authors**: Brian D. Bue, Jake H. Lee, Andrew K. Thorpe, Philip G. Brodrick, Daniel Cusworth, Alana Ayasse, Vass...  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2505.21806  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2505.21806v2.pdf

**Abstract**:
> arXiv:2505.21806v2 Announce Type: replace 
Abstract: Operational deployment of a fully automated facility-scale greenhouse gas (GHG) plume detection system remains challenging for fine spatial resolution imaging spectrometers, despite recent advances in deep learning approaches. With the dramatic increase in data availability, however, automation continues to increase in importance for emissions monitoring. This work reviews and addresses several key obstacles in the field: data and label quality control, prevention of spatiotemporal biases, and correctly aligned modeling objectives. We demonstrate through rigorous experiments using multicampaign data from airborne and spaceborne instruments that convolutional neural networks (CNNs) are able to achieve operational detection performance whe...

---

## 169. Co-rewarding: Stable Self-supervised RL for Eliciting Reasoning in Large Language Models

**Authors**: Zizhuo Zhang, Jianing Zhu, Xinmu Ge, Zihua Zhao, Zhanke Zhou, Xuan Li, Xiao Feng, Jiangchao Yao, Bo ...  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2508.00410  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2508.00410v3.pdf

**Abstract**:
> arXiv:2508.00410v3 Announce Type: replace 
Abstract: While reinforcement learning with verifiable rewards (RLVR) is effective to improve the reasoning ability of large language models (LLMs), its reliance on human-annotated labels leads to the scaling up dilemma, especially for complex tasks. Recent self-rewarding methods investigate a label-free alternative to unlock the reasoning capabilities of LLMs, yet they frequently encounter the non-negligible training collapse issue, as the single-view supervision signal easily forms the self-consistent illusion, yielding the reward hacking. Inspired by the success of self-supervised learning, we propose \textit{Co-rewarding}, a novel self-supervised RL framework that improves training stability by seeking complementary supervision from another vi...

---

## 170. FeDaL: Federated Dataset Learning for General Time Series Foundation Models

**Authors**: Shengchao Chen, Guodong Long, Michael Blumenstein, Jing Jiang  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2508.04045  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2508.04045v2.pdf

**Abstract**:
> arXiv:2508.04045v2 Announce Type: replace 
Abstract: Dataset-level heterogeneity introduces significant domain biases that fundamentally degrade generalization on general Time Series Foundation Models (TSFMs), yet this challenge remains underexplored. This paper rethinks the from-scratch training of TSFMs using the paradigm of federated learning. We propose a novel Federated Dataset Learning (FeDaL) approach to tackle heterogeneous time series by learning dataset-agnostic temporal representations. Specifically, the distributed architecture of federated learning is a nature solution to decompose heterogeneous TS datasets into shared generalized knowledge and preserved personalized knowledge. Moreover, based on the TSFM architecture, FeDaL explicitly mitigates both local and global biases by...

---

## 171. Null-Space Filtering for Data-Free Continual Model Merging: Preserving Stability, Promoting Plasticity

**Authors**: Zihuan Qiu, Lei Wang, Yang Cao, Runtong Zhang, Bing Su, Yi Xu, Fanman Meng, Linfeng Xu, Qingbo Wu, H...  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2509.21413  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2509.21413v2.pdf

**Abstract**:
> arXiv:2509.21413v2 Announce Type: replace 
Abstract: Data-free continual model merging (DFCMM) aims to fuse independently fine-tuned models into a single backbone that evolves with incoming tasks without accessing task data. This paper revisits two fundamental desiderata for DFCMM: stability, avoiding interference with earlier tasks, and plasticity, adapting faithfully to each new task. This poses a challenge that existing approaches fail to address: how to bridge data-level desiderata with parameter-space optimization to ensure stability and plasticity in the absence of task data. To this end, we propose NUFILT (NUll-space FILTering), a data-free framework that directly links these desiderata into parameter-space optimization. Our key observation is that task vectors approximately align w...

---

## 172. TsLLM: Augmenting LLMs for General Time Series Understanding and Prediction

**Authors**: Felix Parker, Nimeesha Chan, Chi Zhang, Kimia Ghobadi  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.01111  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.01111v2.pdf

**Abstract**:
> arXiv:2510.01111v2 Announce Type: replace 
Abstract: Time series data is fundamental to decision-making across many domains including healthcare, finance, power systems, and logistics. However, analyzing this data correctly often requires incorporating unstructured contextual information, answering domain-specific questions, and generating natural language explanations - capabilities that traditional time series models lack. While Large Language Models (LLMs) excel at contextual reasoning and knowledge integration, they struggle with numerical time series due to inefficient text-based representations and limited exposure to numerical data during pretraining. We address this gap by augmenting an LLM with specialized time series perception through a patch-based encoder-decoder architecture. ...

---

## 173. Eliciting Chain-of-Thought Reasoning for Time Series Analysis using Reinforcement Learning

**Authors**: Felix Parker, Nimeesha Chan, Chi Zhang, Kimia Ghobadi  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.01116  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.01116v2.pdf

**Abstract**:
> arXiv:2510.01116v2 Announce Type: replace 
Abstract: Complex numerical time series analysis often demands multi-step reasoning capabilities beyond current models' reach. Tasks like medical diagnosis and weather forecasting require sequential reasoning processes - including counterfactual analysis, logical deduction, knowledge application, and multi-modal contextual integration - that existing time series models cannot explicitly perform. While recent research has shown large language models (LLMs) can achieve sophisticated Chain-of-Thought (CoT) reasoning through reinforcement learning (RL), these advances have primarily focused on mathematical and coding domains, with LLMs still demonstrating poor performance on time series tasks. We introduce Chain Of thought for Understanding Numerical ...

---

## 174. Chorus: Harmonizing Context and Sensing Signals for Data-Free Model Customization in IoT

**Authors**: Liyu Zhang, Yejia Liu, Kwun Ho Liu, Runxi Huang, Xiaomin Ouyang  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2512.15206  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2512.15206v2.pdf

**Abstract**:
> arXiv:2512.15206v2 Announce Type: replace 
Abstract: A key bottleneck toward scalable IoT sensing is how to efficiently adapt AI models to new deployment conditions. In real-world IoT systems, sensor data is collected under diverse contexts, such as sensor placements or ambient environments, which alter signal patterns and degrade downstream performance. Traditional domain adaptation and generalization methods often ignore such contextual information or incorporate it in overly simplistic ways, making them ineffective under unseen context shifts after deployment. In this paper, we propose Chorus, a context-aware, data-free model customization approach that adapts models to unseen deployment conditions without requiring target-domain data. The key idea is to learn context representations th...

---

## 175. On the Existence and Behavior of Secondary Attention Sinks

**Authors**: Jeffrey T. H. Wong, Cheng Zhang, Louis Mahon, Wayne Luk, Anton Isopoussu, Yiren Zhao  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2512.22213  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2512.22213v3.pdf

**Abstract**:
> arXiv:2512.22213v3 Announce Type: replace 
Abstract: Attention sinks are tokens, often the beginning-of-sequence (BOS) token, that receive disproportionately high attention despite limited semantic relevance. In this work, we identify a class of attention sinks, which we term secondary sinks, that differ fundamentally from the sinks studied in prior works, which we term primary sinks. While prior works have identified that tokens other than BOS can sometimes become sinks, they were found to exhibit properties analogous to the BOS token. Specifically, they emerge at the same layer, persist throughout the network and draw a large amount of attention mass. Whereas, we find the existence of secondary sinks that arise primarily in middle layers and can persist for a variable number of layers, a...

---

## 176. The Active Discoverer Framework: Towards Autonomous Physics Reasoning through Neuro-Symbolic LaTeX Synthesis

**Authors**: Hyunjun Jeon  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2601.06117  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2601.06117v3.pdf

**Abstract**:
> arXiv:2601.06117v3 Announce Type: replace 
Abstract: Modern artificial intelligence excels at statistical interpolation within seen manifolds but fundamentally fails at the exact reasoning required for theoretical physics and mathematics. We identify the "Float Wall" -- a catastrophic collapse of neural extrapolation at scales beyond $10^{16}$ -- caused by standard floating-point representation and linguistic tokenization (BPE). To resolve this, we introduce the Active Discoverer Framework, a digit-native neuro-symbolic architecture designed for invariant discovery. At its core is NumberNet, a Siamese Arithmetic Transformer that utilizes least-significant-bit (LSB) sequence encoding to achieve 0% precision loss and cosmic-scale extrapolation up to $10^{50}$. To enforce physical grounding, ...

---

## 177. The Geometric Mechanics of Contrastive Learning: Alignment Potentials, Entropic Dispersion, and Modality Gap

**Authors**: Yichao Cai, Zhen Zhang, Yuhang Liu, Javen Qinfeng Shi  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2601.19597  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2601.19597v2.pdf

**Abstract**:
> arXiv:2601.19597v2 Announce Type: replace 
Abstract: InfoNCE-based contrastive learning is often characterized as promoting alignment and uniformity, yet the induced population geometry and the reasons multimodal training can preserve a modality gap remain underexplored. We present a measure-theoretic view where training reshapes probability measures on a fixed embedding manifold. In the large-batch limit, we prove value and gradient consistency, showing that stochastic InfoNCE tracks a closed-form deterministic energy and revealing a geometric bifurcation between unimodal and symmetric multimodal regimes. Unimodally, the intrinsic functional over the representation measures is strictly convex with a unique Gibbs equilibrium; at low temperature, entropy only breaks ties among well-aligned ...

---

## 178. SDFed: Bridging Local Global Discrepancy via Subspace Refinement and Divergence Control in Federated Prompt Learning

**Authors**: Yicheng Di, Wei Yuan, Tieke He, Yuan Liu, Hongzhi Yin  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.08590  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.08590v3.pdf

**Abstract**:
> arXiv:2602.08590v3 Announce Type: replace 
Abstract: Vision-language pretrained models offer strong transferable representations, yet adapting them in privacy-sensitive multi-party settings is challenging due to the high communication cost of federated optimization and the limited local data on clients. Federated prompt learning mitigates this issue by keeping the VLPM backbone frozen and collaboratively training lightweight prompt parameters. However, existing approaches typically enforce a unified prompt structure and length across clients, which is inadequate under practical client heterogeneity in both data distributions and system resources, and may further introduce conflicts between globally shared and locally optimal knowledge. To address these challenges, we propose \textbf{SDFed}...

---

## 179. Central Dogma Transformer II: An AI Microscope for Understanding Cellular Regulatory Mechanisms

**Authors**: Nobuyuki Ota  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.08751  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.08751v3.pdf

**Abstract**:
> arXiv:2602.08751v3 Announce Type: replace 
Abstract: Current biological AI models lack interpretability -- their internal representations do not correspond to biological relationships that researchers can
  examine. Understanding gene regulation requires models whose learned structure can be directly interrogated to generate experimentally testable
  hypotheses. CDT-II mirrors the central dogma in its architecture -- DNA self-attention, RNA self-attention, and cross-attention for transcriptional
  control -- requiring only genomic embeddings and raw per-cell expression. Applied to K562 CRISPRi data with five genes held out entirely, CDT-II predicts
  perturbation effects (per-gene mean r = 0.84), recovers the GFI1B regulatory network (6.6-fold enrichment, P = 3.5 x 10^{-17}), and shows tha...

---

## 180. KAN-FIF: Spline-Parameterized Lightweight Physics-based Tropical Cyclone Estimation on Meteorological Satellite

**Authors**: Jiakang Shen, Qinghui Chen, Runtong Wang, Chenrui Xu, Jinglin Zhang, Cong Bai, Feng Zhang  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.12117  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.12117v2.pdf

**Abstract**:
> arXiv:2602.12117v2 Announce Type: replace 
Abstract: Tropical cyclones (TC) are among the most destructive natural disasters, causing catastrophic damage to coastal regions through extreme winds, heavy rainfall, and storm surges. Timely monitoring of tropical cyclones is crucial for reducing loss of life and property, yet it is hindered by the computational inefficiency and high parameter counts of existing methods on resource-constrained edge devices. Current physics-guided models suffer from linear feature interactions that fail to capture high-order polynomial relationships between TC attributes, leading to inflated model sizes and hardware incompatibility. To overcome these challenges, this study introduces the Kolmogorov-Arnold Network-based Feature Interaction Framework (KAN-FIF), a ...

---

## 181. Induction Meets Biology: Mechanisms of Repeat Detection in Protein Language Models

**Authors**: Gal Kesten-Pomeranz, Yaniv Nikankin, Anja Reusch, Tomer Tsaban, Ora Schueler-Furman, Yonatan Belinko...  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.23179  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.23179v2.pdf

**Abstract**:
> arXiv:2602.23179v2 Announce Type: replace 
Abstract: Protein sequences are abundant in repeating segments, both as exact copies and as approximate segments with mutations. These repeats are important for protein structure and function, motivating decades of algorithmic work on repeat identification. Recent work has shown that protein language models (PLMs) identify repeats, by examining their behavior in masked-token prediction. To elucidate their internal mechanisms, we investigate how PLMs detect both exact and approximate repeats. We find that the mechanism for approximate repeats functionally subsumes that of exact repeats. We then characterize this mechanism, revealing two main stages: PLMs first build feature representations using both general positional attention heads and biologica...

---

## 182. A Gauge Theory of Superposition: Toward a Sheaf-Theoretic Atlas of Neural Representations

**Authors**: Hossein Javidnia  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.00824  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.00824v2.pdf

**Abstract**:
> arXiv:2603.00824v2 Announce Type: replace 
Abstract: We develop a discrete gauge-theoretic framework for superposition in large language models (LLMs) that replaces the single-global-dictionary premise with a sheaf-theoretic atlas of local semantic charts. Contexts are clustered into a stratified context complex; each chart carries a local feature space and a local information-geometric metric (Fisher/Gauss-Newton) identifying predictively consequential feature interactions. This yields a Fisher-weighted interference energy and three measurable obstructions to global interpretability: (O1) local jamming (active load exceeds Fisher bandwidth), (O2) proxy shearing (mismatch between geometric transport and a fixed correspondence proxy), and (O3) nontrivial holonomy (path-dependent transport a...

---

## 183. Scaling Reward Modeling without Human Supervision

**Authors**: Jingxuan Fan, Yueying Li, Zhenting Qi, Dinghuai Zhang, Kiant\'e Brantley, Sham M. Kakade, Hanlin Zha...  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.02225  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.02225v2.pdf

**Abstract**:
> arXiv:2603.02225v2 Announce Type: replace 
Abstract: Learning from feedback is an instrumental process for advancing the capabilities and safety of frontier models, yet its effectiveness is often constrained by cost and scalability. We present a pilot study that explores scaling reward models through unsupervised approaches. We operationalize reward-based scaling (RBS), in its simplest form, as preference learning over document prefixes and suffixes drawn from large-scale web corpora. Its advantage is demonstrated in various aspects: despite using no human annotations, training on 11M tokens of math-focused web data yields steady gains on RewardBench v1 and v2, and these improvements consistently transfer across diverse initialization backbones spanning model families and scales. Across mo...

---

## 184. Preserving Continuous Symmetry in Discrete Spaces: Geometric-Aware Quantization for SO(3)-Equivariant GNNs

**Authors**: Haoyu Zhou, Ping Xue, Hao Zhang, Tianfan Fu  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.05343  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.05343v2.pdf

**Abstract**:
> arXiv:2603.05343v2 Announce Type: replace 
Abstract: Equivariant Graph Neural Networks (GNNs) are essential for physically consistent molecular simulations but suffer from high computational costs and memory bottlenecks, especially with high-order representations. While low-bit quantization offers a solution, applying it naively to rotation-sensitive features destroys the SO(3)-equivariant structure, leading to significant errors and violations of conservation laws. To address this issue, in this work, we propose a Geometric-Aware Quantization (GAQ) framework that compresses and accelerates equivariant models while rigorously preserving continuous symmetry in discrete spaces. Our approach introduces three key contributions: (1) a Magnitude-Direction Decoupled Quantization (MDDQ) scheme tha...

---

## 185. Implementation of Quantum Implicit Neural Representation in Deterministic and Probabilistic Autoencoders for Image Reconstruction/Generation Tasks

**Authors**: Saadet M\"uzehher Eren  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.06755  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.06755v2.pdf

**Abstract**:
> arXiv:2603.06755v2 Announce Type: replace 
Abstract: We propose a quantum implicit neural representation (QINR)-based autoencoder (AE) and variational autoencoder (VAE) for image reconstruction and generation tasks. Our purpose is to demonstrate that the QINR in VAEs and AEs can transform information from the latent space into highly rich, periodic, and high-frequency features. Additionally, we aim to show that the QINR-VAE can be more stable than various quantum generative adversarial network (QGAN) models in image generation because it can address the low diversity problem. Our quantum-classical hybrid models consist of a classical convolutional neural network (CNN) encoder and a quantum-based QINR decoder. We train the QINR-AE/VAE with binary cross-entropy with logits (BCEWithLogits) as...

---

## 186. OrthoFormer: Instrumental Variable Estimation in Transformer Hidden States via Neural Control Functions

**Authors**: Charles Luo  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.07431  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.07431v2.pdf

**Abstract**:
> arXiv:2603.07431v2 Announce Type: replace 
Abstract: Transformer architectures excel at sequential modeling yet remain fundamentally limited by correlational learning - they capture spurious associations induced by latent confounders rather than invariant causal mechanisms. We identify this as an epistemological challenge: standard Transformers conflate static background factors (intrinsic identity, style, context) with dynamic causal flows (state evolution, mechanism), leading to catastrophic out-of-distribution failure. We propose OrthoFormer, a causally grounded architecture that embeds instrumental variable estimation directly into Transformer blocks via neural control functions. Our framework rests on four theoretical pillars: Structural Directionality (time-arrow enforcement), Repres...

---

## 187. Attention Sinks Are Provably Necessary in Softmax Transformers: Evidence from Trigger-Conditional Tasks

**Authors**: Yuval Ran-Milo  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11487  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11487v2.pdf

**Abstract**:
> arXiv:2603.11487v2 Announce Type: replace 
Abstract: Transformers often display an attention sink: probability mass concentrates on a fixed, content-agnostic position. Are sinks a byproduct of the optimization/training regime? Or are they sometimes functionally necessary in softmax Transformers? Are sinks a byproduct of the optimization/training regime? Or are they sometimes functionally necessary in softmax Transformers? We prove that, in some settings, it is the latter: computing a simple trigger-conditional behavior necessarily induces a sink in softmax self-attention models. Our results formalize a familiar intuition: normalization over a probability simplex must force attention to collapse onto a stable anchor to realize a default state (e.g., when the model needs to ignore the input)...

---

## 188. KEPo: Knowledge Evolution Poison on Graph-based Retrieval-Augmented Generation

**Authors**: Qizhi Chen, Chao Qi, Yihong Huang, Muquan Li, Rongzheng Wang, Dongyang Zhang, Ke Qin, Shuang Liang  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11501  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11501v2.pdf

**Abstract**:
> arXiv:2603.11501v2 Announce Type: replace 
Abstract: Graph-based Retrieval-Augmented Generation (GraphRAG) constructs the Knowledge Graph (KG) from external databases to enhance the timeliness and accuracy of Large Language Model (LLM) generations. However, this reliance on external data introduces new attack surfaces. Attackers can inject poisoned texts into databases to manipulate LLMs into producing harmful target responses for attacker-chosen queries. Existing research primarily focuses on attacking conventional RAG systems. However, such methods are ineffective against GraphRAG. This robustness derives from the KG abstraction of GraphRAG, which reorganizes injected text into a graph before retrieval, thereby enabling the LLM to reason based on the restructured context instead of raw p...

---

## 189. Separable neural architectures as a primitive for unified predictive and generative intelligence

**Authors**: Reza T. Batley, Apurba Sarker, Rajib Mostakim, Andrew Klichine, Sourav Saha  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12244  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12244v2.pdf

**Abstract**:
> arXiv:2603.12244v2 Announce Type: replace 
Abstract: Intelligent systems across physics, language and perception often exhibit factorisable structure, yet are typically modelled by monolithic neural architectures that do not explicitly exploit this structure. The separable neural architecture (SNA) addresses this by formalising a representational class that unifies additive, quadratic and tensor-decomposed neural models. By constraining interaction order and tensor rank, SNAs impose a structural inductive bias that factorises high-dimensional mappings into low-arity components. Separability need not be a property of the system itself: it often emerges in the coordinates or representations through which the system is expressed. Crucially, this coordinate-aware formulation reveals a structur...

---

## 190. 3DTCR: A Physics-Based Generative Framework for Vortex-Following 3D Reconstruction to Improve Tropical Cyclone Intensity Forecasting

**Authors**: Jun Liu, Xiaohui Zhong, Kai Zheng, Jiarui Li, Yifei Li, Tao Zhou, Wenxu Qian, Shun Dai, Ruian Tie, Y...  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13049  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13049v2.pdf

**Abstract**:
> arXiv:2603.13049v2 Announce Type: replace 
Abstract: Tropical cyclone (TC) intensity forecasting remains challenging as current numerical and AI-based weather models fail to satisfactorily represent extreme TC structure and intensity. Although intensity time-series forecasting has achieved significant advances, it outputs intensity sequences rather than the three-dimensional inner-core fine-scale structure and physical mechanisms governing TC evolution. High-resolution numerical simulations can capture these features but remain computationally expensive and inefficient for large-scale operational applications. Here we present 3DTCR, a physics-based generative framework combining physical constraints with generative AI efficiency for 3D TC structure reconstruction. Trained on a six-year, 3-...

---

## 191. Quadratic Gradient: A Unified Framework Bridging Gradient Descent and Newton-Type Methods by Synthesizing Hessians and Gradients

**Authors**: John Chiang  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2209.03282  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2209.03282v3.pdf

**Abstract**:
> arXiv:2209.03282v3 Announce Type: replace-cross 
Abstract: It might be inadequate for the line search technique for Newton's method to use only one floating point number. A column vector of the same size as the gradient might be better than a mere float number to accelerate each of the gradient elements with different rates. Moreover, a square matrix of the same order as the Hessian matrix might be helpful to correct the Hessian matrix. Chiang applied something between a column vector and a square matrix, namely a diagonal matrix, to accelerate the gradient and further proposed a faster gradient variant called quadratic gradient. In this paper, we present a new way to build a new version of the quadratic gradient. This new quadratic gradient doesn't satisfy the convergence conditions of th...

---

## 192. Federated Multi-Agent Mapping for Planetary Exploration

**Authors**: Tiberiu-Ioan Szatmari, Abhishek Cauligi  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2404.02289  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2404.02289v4.pdf

**Abstract**:
> arXiv:2404.02289v4 Announce Type: replace-cross 
Abstract: Multi-agent robotic exploration stands to play an important role in space exploration as the next generation of robotic systems ventures to far-flung environments. A key challenge in this new paradigm will be to effectively share and utilize the vast amount of data generated onboard while operating in bandwidth-constrained regimes typical of space missions. Federated learning (FL) is a promising tool for bridging this gap. Drawing inspiration from the upcoming CADRE Lunar rover mission, we propose a federated multi-agent mapping approach that jointly trains a global map model across agents without transmitting raw data. Our method leverages implicit neural mapping to generate parsimonious, adaptable representations, reducing data t...

---

## 193. Unified Text-Image-to-Video Generation: A Training-Free Approach to Flexible Visual Conditioning

**Authors**: Bolin Lai, Sangmin Lee, Xu Cao, Xiang Li, James M. Rehg  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2505.20629  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2505.20629v3.pdf

**Abstract**:
> arXiv:2505.20629v3 Announce Type: replace-cross 
Abstract: Text-image-to-video (TI2V) generation is a critical problem for controllable video generation using both semantic and visual conditions. Most existing methods typically add visual conditions to text-to-video (T2V) foundation models by finetuning, which is costly in resources and only limited to a few pre-defined conditioning settings. To tackle these constraints, we introduce a unified formulation for TI2V generation with flexible visual conditioning. Furthermore, we propose an innovative training-free approach, dubbed FlexTI2V, that can condition T2V foundation models on an arbitrary amount of images at arbitrary positions. Specifically, we firstly invert the condition images to noisy representation in a latent space. Then, in the...

---

## 194. Quantifying task-relevant representational similarity using decision variable correlation

**Authors**: Yu Eric Qian, Wilson S. Geisler, Xue-Xin Wei  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2506.02164  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2506.02164v4.pdf

**Abstract**:
> arXiv:2506.02164v4 Announce Type: replace-cross 
Abstract: Previous studies have compared neural activities in the visual cortex to representations in deep neural networks trained on image classification. Interestingly, while some suggest that their representations are highly similar, others argued the opposite. Here, we propose a new approach to characterize the similarity of the decision strategies of two observers (models or brains) using decision variable correlation (DVC). DVC quantifies the image-by-image correlation between the decoded decisions based on the internal neural representations in a classification task. Thus, it can capture task-relevant information rather than general representational alignment. We evaluate DVC using monkey V4/IT recordings and network models trained on...

---

## 195. Model-based Implicit Neural Representation for sub-wavelength Radio Localization

**Authors**: Baptiste Chatelier (IETR, INSA Rennes, MERCE-France), Vincent Corlay (MERCE-France), Musa Furkan Kes...  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2506.06387  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2506.06387v3.pdf

**Abstract**:
> arXiv:2506.06387v3 Announce Type: replace-cross 
Abstract: The increasing deployment of large antenna arrays at base stations has significantly improved the spatial resolution and localization accuracy of radio-localization methods. However, traditional signal processing techniques struggle in complex radio environments, particularly in scenarios dominated by non line of sight (NLoS) propagation paths, resulting in degraded localization accuracy. Recent developments in machine learning have facilitated the development of machine learning-assisted localization techniques, enhancing localization accuracy in complex radio environments. However, these methods often involve substantial computational complexity during both the training and inference phases. This work extends the well-established...

---

## 196. Cropping outperforms dropout as an augmentation strategy for self-supervised training of text embeddings

**Authors**: Rita Gonz\'alez-M\'arquez, Philipp Berens, Dmitry Kobak  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2508.03453  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2508.03453v2.pdf

**Abstract**:
> arXiv:2508.03453v2 Announce Type: replace-cross 
Abstract: Text embeddings, i.e. vector representations of entire texts, play an important role in many NLP applications, such as retrieval-augmented generation, clustering, or visualizing collections of texts for data exploration. Currently, top-performing embedding models are derived from pre-trained language models via supervised contrastive fine-tuning. This fine-tuning strategy relies on an external notion of similarity and annotated data for generation of positive pairs. Here we study self-supervised fine-tuning and systematically compare the two most well-known augmentation strategies used for fine-tuning text embeddings models. We assess embedding quality on MTEB and additional in-domain evaluations and show that cropping augmentation...

---

## 197. Extending Foundational Monocular Depth Estimators to Fisheye Cameras with Calibration Tokens

**Authors**: Suchisrit Gangopadhyay, Jung-Hee Kim, Xien Chen, Patrick Rim, Hyoungseob Park, Alex Wong  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2508.04928  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2508.04928v4.pdf

**Abstract**:
> arXiv:2508.04928v4 Announce Type: replace-cross 
Abstract: We propose a method to extend foundational monocular depth estimators (FMDEs), trained on perspective images, to fisheye images. Despite being trained on tens of millions of images, FMDEs are susceptible to the covariate shift introduced by changes in camera calibration (intrinsic, distortion) parameters, leading to erroneous depth estimates. Our method aligns the distribution of latent embeddings encoding fisheye images to those of perspective images, enabling the reuse of FMDEs for fisheye cameras without retraining or finetuning. To this end, we introduce a set of Calibration Tokens as a light-weight adaptation mechanism that modulates the latent embeddings for alignment. By exploiting the already expressive latent space of FMDE...

---

## 198. ExoPredicator: Learning Abstract Models of Dynamic Worlds for Robot Planning

**Authors**: Yichao Liang, Dat Nguyen, Cambridge Yang, Tianyang Li, Joshua B. Tenenbaum, Carl Edward Rasmussen, A...  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2509.26255  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2509.26255v3.pdf

**Abstract**:
> arXiv:2509.26255v3 Announce Type: replace-cross 
Abstract: Long-horizon embodied planning is challenging because the world does not only change through an agent's actions: exogenous processes (e.g., water heating, dominoes cascading) unfold concurrently with the agent's actions. We propose a framework for abstract world models that jointly learns (i) symbolic state representations and (ii) causal processes for both endogenous actions and exogenous mechanisms. Each causal process models the time course of a stochastic cause-effect relation. We learn these world models from limited data via variational Bayesian inference combined with LLM proposals. Across five simulated tabletop robotics environments, the learned models enable fast planning that generalizes to held-out tasks with more objec...

---

## 199. Beyond AlphaEarth: Toward Human-Centered Geospatial Foundation Models via POI-Guided Contrastive Learning

**Authors**: Junyuan Liu, Quan Qin, Guangsheng Dong, Xinglei Wang, Jiazhuang Feng, Zichao Zeng, Tao Cheng  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.09894  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.09894v2.pdf

**Abstract**:
> arXiv:2510.09894v2 Announce Type: replace-cross 
Abstract: Recent geospatial foundation models (GFMs) produce spatially extensive representations of the Earth's surface that capture rich physical and environmental patterns. Among them, the AlphaEarth Foundation (AE) represents a major step, generating 10 m embeddings from multi-source Earth Observation (EO) data that include diverse environmental and spectral characteristics. However, such EO-driven representations primarily encode physical and spectral patterns rather than human activities or urban semantics, limiting their ability to capture the functional dimensions of cities and making the learned representations difficult to interpret or query using natural language. We introduce AETHER (AlphaEarth-POI Enriched Representation Learning...

---

## 200. PRISM: Enhancing Protein Inverse Folding through Fine-Grained Retrieval on Structure-Sequence Multimodal Representations

**Authors**: Sazan Mahbub, Souvik Kundu, Eric P. Xing  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.11750  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.11750v2.pdf

**Abstract**:
> arXiv:2510.11750v2 Announce Type: replace-cross 
Abstract: Designing protein sequences that fold into a target 3-D structure, termed as the inverse folding problem, is central to protein engineering. However, it remains challenging due to the vast sequence space and the importance of local structural constraints. Existing deep learning approaches achieve strong recovery rates, however, lack explicit mechanisms to reuse fine-grained structure-sequence patterns conserved across natural proteins. To mitigate this, we present PRISM a multimodal retrieval-augmented generation framework for inverse folding. PRISM retrieves fine-grained representations of potential motifs from known proteins and integrates them with a hybrid self-cross attention decoder. PRISM is formulated as a latent-variable p...

---

## 201. SemBench: A Benchmark for Semantic Query Processing Engines

**Authors**: Jiale Lao, Andreas Zimmerer, Olga Ovcharenko, Tianji Cong, Matthew Russo, Gerardo Vitagliano, Michae...  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2511.01716  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2511.01716v2.pdf

**Abstract**:
> arXiv:2511.01716v2 Announce Type: replace-cross 
Abstract: We present a benchmark targeting a novel class of systems: semantic query processing engines. Those systems rely inherently on generative and reasoning capabilities of state-of-the-art large language models (LLMs). They extend SQL with semantic operators, configured by natural language instructions, that are evaluated via LLMs and enable users to perform various operations on multimodal data.
  Our benchmark introduces diversity across three key dimensions: scenarios, modalities, and operators. Included are scenarios ranging from movie review analysis to car damage detection. Within these scenarios, we cover different data modalities, including images, audio, and text. Finally, the queries involve a diverse set of operators, includ...

---

## 202. Circuit Representations of Random Forests with Applications to XAI

**Authors**: Chunxi Ji, Adnan Darwiche  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.08362  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.08362v2.pdf

**Abstract**:
> arXiv:2602.08362v2 Announce Type: replace-cross 
Abstract: We make three contributions in this paper. First, we present an approach for compiling a random forest classifier into a set of circuits, where each circuit directly encodes the instances in some class of the classifier. We show empirically that our proposed approach is significantly more efficient than existing similar approaches. Next, we utilize this approach to further obtain circuits that are tractable for computing the complete and general reasons of a decision, which are instance abstractions that play a fundamental role in computing explanations. Finally, we propose algorithms for computing the robustness of a decision and all shortest ways to flip it. We illustrate the utility of our contributions by using them to enumerat...

---

## 203. BLINK: Behavioral Latent Modeling of NK Cell Cytotoxicity

**Authors**: Iman Nematollahi, Jose Francisco Villena-Ossa, Alina Moter, Kiana Farhadyar, Gabriel Kalweit, Abhina...  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.05110  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.05110v2.pdf

**Abstract**:
> arXiv:2603.05110v2 Announce Type: replace-cross 
Abstract: Machine learning models of cellular interaction dynamics hold promise for understanding cell behavior. Natural killer (NK) cell cytotoxicity is a prominent example of such interaction dynamics and is commonly studied using time-resolved multi-channel fluorescence microscopy. Although tumor cell death events can be annotated at single frames, NK cytotoxic outcome emerges over time from cellular interactions and cannot be reliably inferred from frame-wise classification alone. We introduce BLINK, a trajectory-based recurrent state-space model that serves as a cell world model for NK-tumor interactions. BLINK learns latent interaction dynamics from partially observed NK-tumor interaction sequences and predicts apoptosis increments tha...

---

## 204. MobileFetalCLIP: Selective Repulsive Knowledge Distillation for Mobile Fetal Ultrasound Analysis

**Authors**: Numan Saeed, Fadillah Adamsyah Maani, Mohammad Yaqub  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.05421  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.05421v2.pdf

**Abstract**:
> arXiv:2603.05421v2 Announce Type: replace-cross 
Abstract: Fetal ultrasound AI could transform prenatal care in low-resource settings, yet current foundation models exceed 300M visual parameters, precluding deployment on point-of-care devices. Standard knowledge distillation fails under such extreme capacity gaps (~26x), as compact students waste capacity mimicking architectural artifacts of oversized teachers. We introduce Selective Repulsive Knowledge Distillation, which decomposes contrastive KD into diagonal and off-diagonal components: matched pair alignment is preserved while the off-diagonal weight decays into negative values, repelling the student from the teacher's inter-class confusions and forcing discovery of architecturally native features. Our 11.4M parameter student surpasse...

---

## 205. Structural Causal Bottleneck Models

**Authors**: Simon Bing, Jonas Wahl, Jakob Runge  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.08682  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.08682v2.pdf

**Abstract**:
> arXiv:2603.08682v2 Announce Type: replace-cross 
Abstract: We introduce structural causal bottleneck models (SCBMs), a novel class of structural causal models. At the core of SCBMs lies the assumption that causal effects between high-dimensional variables only depend on low-dimensional summary statistics, or bottlenecks, of the causes. SCBMs provide a flexible framework for task-specific dimension reduction while being estimable via standard, simple learning algorithms in practice. We analyse identifiability in SCBMs, connect them to information bottlenecks in the sense of Tishby & Zaslavsky (2015), and illustrate how to estimate them experimentally. We also demonstrate the benefit of bottlenecks for effect estimation in low-sample transfer learning settings. We argue that SCBMs provide an...

---

## 206. Emotion is Not Just a Label: Latent Emotional Factors in LLM Processing

**Authors**: Benjamin Reichman, Adar Avsian, Samuel Webster, Larry Heck  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.09205  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.09205v2.pdf

**Abstract**:
> arXiv:2603.09205v2 Announce Type: replace-cross 
Abstract: Large language models are routinely deployed on text that varies widely in emotional tone, yet their reasoning behavior is typically evaluated without accounting for emotion as a source of representational variation. Prior work has largely treated emotion as a prediction target, for example in sentiment analysis or emotion classification. In contrast, we study emotion as a latent factor that shapes how models attend to and reason over text. We analyze how emotional tone systematically alters attention geometry in transformer models, showing that metrics such as locality, center-of-mass distance, and entropy vary across emotions and correlate with downstream question-answering performance. To facilitate controlled study of these eff...

---

## 207. Think Before You Lie: How Reasoning Leads to Honesty

**Authors**: Ann Yuan, Asma Ghandeharioun, Carter Blum, Alicia Machado, Jessica Hoffmann, Daphne Ippolito, Martin...  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.09957  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.09957v2.pdf

**Abstract**:
> arXiv:2603.09957v2 Announce Type: replace-cross 
Abstract: While existing evaluations of large language models (LLMs) measure deception rates, the underlying conditions that give rise to deceptive behavior are poorly understood. We investigate this question using a novel dataset of realistic moral trade-offs where honesty incurs variable costs. Contrary to humans, who tend to become less honest given time to deliberate (Capraro, 2017; Capraro et al., 2019), we find that reasoning consistently increases honesty across scales and for several LLM families. This effect is not only a function of the reasoning content, as reasoning traces are often poor predictors of final behaviors. Rather, we show that the underlying geometry of the representational space itself contributes to the effect. Name...

---

## 208. Detecting Intrinsic and Instrumental Self-Preservation in Autonomous Agents: The Unified Continuation-Interest Protocol

**Authors**: Christopher Altman  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11382  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11382v2.pdf

**Abstract**:
> arXiv:2603.11382v2 Announce Type: replace-cross 
Abstract: Autonomous agents, especially delegated systems with memory, persistent context, and multi-step planning, pose a measurement problem not present in stateless models: an agent that preserves continued operation as a terminal objective and one that does so merely instrumentally can produce observationally similar trajectories. External behavioral monitoring cannot reliably distinguish between them. We introduce the Unified Continuation-Interest Protocol (UCIP), a multi-criterion detection framework that moves this distinction from behavior to the latent structure of agent trajectories. UCIP encodes trajectories with a Quantum Boltzmann Machine (QBM), a classical algorithm based on the density-matrix formalism of quantum statistical m...

---

## 209. Revisiting Model Stitching In the Foundation Model Era

**Authors**: Zheda Mai, Ke Zhang, Fu-En Wang, Zixiao Ken Wang, Albert Y. C. Chen, Lu Xia, Min Sun, Wei-Lun Chao, ...  
**Categories**: cs.LG  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12433  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12433v2.pdf

**Abstract**:
> arXiv:2603.12433v2 Announce Type: replace-cross 
Abstract: Model stitching, connecting early layers of one model (source) to later layers of another (target) via a light stitch layer, has served as a probe of representational compatibility. Prior work finds that models trained on the same dataset remain stitchable (negligible accuracy drop) despite different initializations or objectives. We revisit stitching for Vision Foundation Models (VFMs) that vary in objectives, data, and modality mix (e.g., CLIP, DINOv2, SigLIP 2) and ask: Are heterogeneous VFMs stitchable? We introduce a systematic protocol spanning the stitch points, stitch layer families, training losses, and downstream tasks. Three findings emerge. (1) Stitch layer training matters: conventional approaches that match the interm...

---

## 210. Multi-Axis Trust Modeling for Interpretable Account Hijacking Detection

**Authors**: Mohammad AL-Smadi  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13246  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13246v1.pdf

**Abstract**:
> arXiv:2603.13246v1 Announce Type: new 
Abstract: This paper proposes a Hadith-inspired multi-axis trust modeling framework, motivated by a structurally analogous problem in classical Hadith scholarship: assessing the trustworthiness of information sources using interpretable, multidimensional criteria rather than a single anomaly score. We translate five trust axes - long-term integrity (adalah), behavioral precision (dabt), contextual continuity (isnad), cumulative reputation, and anomaly evidence - into a compact set of 26 semantically meaningful behavioral features for user accounts. In addition, we introduce lightweight temporal features that capture short-horizon changes in these trust signals across consecutive activity windows. We evaluate the framework on the CLUE-LDS cloud activit...

---

## 211. ILION: Deterministic Pre-Execution Safety Gates for Agentic AI Systems

**Authors**: Florin Adrian Chitan  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13247  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13247v1.pdf

**Abstract**:
> arXiv:2603.13247v1 Announce Type: new 
Abstract: The proliferation of autonomous AI agents capable of executing real-world actions - filesystem operations, API calls, database modifications, financial transactions - introduces a class of safety risk not addressed by existing content-moderation infrastructure. Current text-safety systems evaluate linguistic content for harm categories such as violence, hate speech, and sexual content; they are architecturally unsuitable for evaluating whether a proposed action falls within an agent's authorized operational scope. We present ILION (Intelligent Logic Identity Operations Network), a deterministic execution gate for agentic AI systems. ILION employs a five-component cascade architecture - Transient Identity Imprint (TII), Semantic Vector Refere...

---

## 212. Multi-hop Reasoning and Retrieval in Embedding Space: Leveraging Large Language Models with Knowledge

**Authors**: Lihui Liu  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13266  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13266v1.pdf

**Abstract**:
> arXiv:2603.13266v1 Announce Type: new 
Abstract: As large language models (LLMs) continue to grow in size, their abilities to tackle complex tasks have significantly improved. However, issues such as hallucination and the lack of up-to-date knowledge largely remain unresolved. Knowledge graphs (KGs), which serve as symbolic representations of real-world knowledge, offer a reliable source for enhancing reasoning. Integrating KG retrieval into LLMs can therefore strengthen their reasoning by providing dependable knowledge. Nevertheless, due to limited understanding of the underlying knowledge graph, LLMs may struggle with queries that have multiple interpretations. Additionally, the incompleteness and noise within knowledge graphs may result in retrieval failures. To address these challenges...

---

## 213. Emotional Cost Functions for AI Safety: Teaching Agents to Feel the Weight of Irreversible Consequences

**Authors**: Pandurang Mopgar  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14531  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14531v1.pdf

**Abstract**:
> arXiv:2603.14531v1 Announce Type: new 
Abstract: Humans learn from catastrophic mistakes not through numerical penalties, but through qualitative suffering that reshapes who they are. Current AI safety approaches replicate none of this. Reward shaping captures magnitude, not meaning. Rule-based alignment constrains behaviour, but does not change it.
  We propose Emotional Cost Functions, a framework in which agents develop Qualitative Suffering States, rich narrative representations of irreversible consequences that persist forward and actively reshape character. Unlike numerical penalties, qualitative suffering states capture the meaning of what was lost, the specific void it creates, and how it changes the agent's relationship to similar future situations. Our four-component architecture...

---

## 214. Dynamic Theory of Mind as a Temporal Memory Problem: Evidence from Large Language Models

**Authors**: Thuy Ngoc Nguyen, Duy Nhat Phan, Cleotilde Gonzalez  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14646  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14646v1.pdf

**Abstract**:
> arXiv:2603.14646v1 Announce Type: new 
Abstract: Theory of Mind (ToM) is central to social cognition and human-AI interaction, and Large Language Models (LLMs) have been used to help understand and represent ToM. However, most evaluations treat ToM as a static judgment at a single moment, primarily relying on tests of false beliefs. This overlooks a key dynamic dimension of ToM: the ability to represent, update, and retrieve others' beliefs over time. We investigate dynamic ToM as a temporally extended representational memory problem, asking whether LLMs can track belief trajectories across interactions rather than only inferring current beliefs. We introduce DToM-Track, an evaluation framework to investigate temporal belief reasoning in controlled multiturn conversations, testing the reca...

---

## 215. RenderMem: Rendering as Spatial Memory Retrieval

**Authors**: JooHyun Park, HyeongYeop Kang  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14669  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14669v1.pdf

**Abstract**:
> arXiv:2603.14669v1 Announce Type: new 
Abstract: Embodied reasoning is inherently viewpoint-dependent: what is visible, occluded, or reachable depends critically on where the agent stands. However, existing spatial memory systems for embodied agents typically store either multi-view observations or object-centric abstractions, making it difficult to perform reasoning with explicit geometric grounding. We introduce RenderMem, a spatial memory framework that treats rendering as the interface between 3D world representations and spatial reasoning. Instead of storing fixed observations, RenderMem maintains a 3D scene representation and generates query-conditioned visual evidence by rendering the scene from viewpoints implied by the query. This enables embodied agents to reason directly about l...

---

## 216. GameUIAgent: An LLM-Powered Framework for Automated Game UI Design with Structured Intermediate Representation

**Authors**: Wei Zeng, Fengwei An, Zhen Liu, Jian Zhao  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14724  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14724v1.pdf

**Abstract**:
> arXiv:2603.14724v1 Announce Type: new 
Abstract: Game UI design requires consistent visual assets across rarity tiers yet remains a predominantly manual process. We present GameUIAgent, an LLM-powered agentic framework that translates natural language descriptions into editable Figma designs via a Design Spec JSON intermediate representation. A six-stage neuro-symbolic pipeline combines LLM generation, deterministic post-processing, and a Vision-Language Model (VLM)-guided Reflection Controller (RC) for iterative self-correction with guaranteed non-regressive quality. Evaluated across 110 test cases, three LLMs, and three UI templates, cross-model analysis establishes a game-domain failure taxonomy (rarity-dependent degradation; visual emptiness) and uncovers two key empirical findings. A ...

---

## 217. A Self-Evolving Defect Detection Framework for Industrial Photovoltaic Systems

**Authors**: Haoyu He, Yu Duan, Wenzhen Liu, Hanyuan Hang, Qiantu Tuo, Xiaoke Yang, Rui Li  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14869  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14869v1.pdf

**Abstract**:
> arXiv:2603.14869v1 Announce Type: new 
Abstract: Reliable photovoltaic (PV) power generation requires timely detection of module defects that may reduce energy yield, accelerate degradation, and increase lifecycle operation and maintenance costs during field operation. Electroluminescence (EL) imaging has therefore been widely adopted for PV module inspection. However, automated defect detection in real operational environments remains challenging due to heterogeneous module geometries, low-resolution imaging conditions, subtle defect morphology, long-tailed defect distributions, and continual data shifts introduced by evolving inspection and labeling processes. These factors significantly limit the robustness and long-term maintainability of conventional deep-learning inspection pipelines...

---

## 218. Exposing Cross-Modal Consistency for Fake News Detection in Short-Form Videos

**Authors**: Chong Tian, Yu Wang, Chenxu Yang, Junyi Guan, Zheng Lin, Yuhan Liu, Xiuying Chen, Qirong Ho  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14992  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14992v1.pdf

**Abstract**:
> arXiv:2603.14992v1 Announce Type: new 
Abstract: Short-form video platforms are major channels for news but also fertile ground for multimodal misinformation where each modality appears plausible alone yet cross-modal relationships are subtly inconsistent, like mismatched visuals and captions. On two benchmark datasets, FakeSV (Chinese) and FakeTT (English), we observe a clear asymmetry: real videos exhibit high text-visual but moderate text-audio consistency, while fake videos show the opposite pattern. Moreover, a single global consistency score forms an interpretable axis along which fake probability and prediction errors vary smoothly. Motivated by these observations, we present MAGIC3 (Modal-Adversarial Gated Interaction and Consistency-Centric Classifier), a detector that explicitly ...

---

## 219. Advancing Multimodal Agent Reasoning with Long-Term Neuro-Symbolic Memory

**Authors**: Rongjie Jiang, Jianwei Wang, Gengda Zhao, Chengyang Luo, Kai Wang, Wenjie Zhang  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15280  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15280v1.pdf

**Abstract**:
> arXiv:2603.15280v1 Announce Type: new 
Abstract: Recent advances in large language models have driven the emergence of intelligent agents operating in open-world, multimodal environments. To support long-term reasoning, such agents are typically equipped with external memory systems. However, most existing multimodal agent memories rely primarily on neural representations and vector-based retrieval, which are well-suited for inductive, intuitive reasoning but fundamentally limited in supporting analytical, deductive reasoning critical for real-world decision making. To address this limitation, we propose NS-Mem, a long-term neuro-symbolic memory framework designed to advance multimodal agent reasoning by integrating neural memory with explicit symbolic structures and rules. Specifically, N...

---

## 220. Intelligent Co-Design: An Interactive LLM Framework for Interior Spatial Design via Multi-Modal Agents

**Authors**: Ren Jian Lim, Rushi Dai  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15341  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15341v1.pdf

**Abstract**:
> arXiv:2603.15341v1 Announce Type: new 
Abstract: In architectural interior design, miscommunication frequently arises as clients lack design knowledge, while designers struggle to explain complex spatial relationships, leading to delayed timelines and financial losses. Recent advancements in generative layout tools narrow the gap by automating 3D visualizations. However, prevailing methodologies exhibit limitations: rule-based systems implement hard-coded spatial constraints that restrict participatory engagement, while data-driven models rely on extensive training datasets. Recent large language models (LLMs) bridge this gap by enabling intuitive reasoning about spatial relationships through natural language. This research presents an LLM-based, multimodal, multi-agent framework that dyna...

---

## 221. CRASH: Cognitive Reasoning Agent for Safety Hazards in Autonomous Driving

**Authors**: Erick Silva, Rehana Yasmin, Ali Shoker  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15364  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15364v1.pdf

**Abstract**:
> arXiv:2603.15364v1 Announce Type: new 
Abstract: As AVs grow in complexity and diversity, identifying the root causes of operational failures has become increasingly complex. The heterogeneity of system architectures across manufacturers, ranging from end-to-end to modular designs, together with variations in algorithms and integration strategies, limits the standardization of incident investigations and hinders systematic safety analysis. This work examines real-world AV incidents reported in the NHTSA database. We curate a dataset of 2,168 cases reported between 2021 and 2025, representing more than 80 million miles driven. To process this data, we introduce CRASH, Cognitive Reasoning Agent for Safety Hazards, an LLM-based agent that automates reasoning over crash reports by leveraging b...

---

## 222. Unlocking the Value of Text: Event-Driven Reasoning and Multi-Level Alignment for Time Series Forecasting

**Authors**: Siyuan Wang, Peng Chen, Yihang Wang, Wanghui Qiu, Chenjuan Guo, Bin Yang, Yang Shu  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15452  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15452v1.pdf

**Abstract**:
> arXiv:2603.15452v1 Announce Type: new 
Abstract: Existing time series forecasting methods primarily rely on the numerical data itself. However, real-world time series exhibit complex patterns associated with multimodal information, making them difficult to predict with numerical data alone. While several multimodal time series forecasting methods have emerged, they either utilize text with limited supplementary information or focus merely on representation extraction, extracting minimal textual information for forecasting. To unlock the Value of Text, we propose VoT, a method with Event-driven Reasoning and Multi-level Alignment. Event-driven Reasoning combines the rich information in exogenous text with the powerful reasoning capabilities of LLMs for time series forecasting. To guide the ...

---

## 223. Agent Lifecycle Toolkit (ALTK): Reusable Middleware Components for Robust AI Agents

**Authors**: Zidane Wright, Jason Tsay, Anupama Murthi, Osher Elhadad, Diego Del Rio, Saurabh Goyal, Kiran Kate, ...  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15473  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15473v1.pdf

**Abstract**:
> arXiv:2603.15473v1 Announce Type: new 
Abstract: As AI agents move from demos into enterprise deployments, their failure modes become consequential: a misinterpreted tool argument can corrupt production data, a silent reasoning error can go undetected until damage is done, and outputs that violate organizational policy can create legal or compliance risk. Yet, most agent frameworks leave builders to handle these failure modes ad hoc, resulting in brittle, one-off safeguards that are hard to reuse or maintain. We present the Agent Lifecycle Toolkit (ALTK), an open-source collection of modular middleware components that systematically address these gaps across the full agent lifecycle.
  Across the agent lifecycle, we identify opportunities to intervene and improve, namely, post-user-request...

---

## 224. Artificial Intelligence: Beyound Ocularcentrism, the New Age of Humans Beyond the Spectacle

**Authors**: Mustapha El Moussaoui  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13248  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13248v1.pdf

**Abstract**:
> arXiv:2603.13248v1 Announce Type: cross 
Abstract: This paper explores the transformative impact of artificial intelligence (AI) on visual culture and its broader implications for contemporary society. The proliferation of machine learning models in generating visual content necessitates a critical reassessment of the relationship between reality and representation. AI-generated imagery not only challenges traditional conceptions of human creativity and perception but also intensifies the dominance of visual media in shaping public consciousness. By critiquing the reliance on vision as the primary mode of knowledge, this study examines how AI technologies blur the boundaries between reality and artificial constructs, deepening societal alienation. To illustrate these dynamics, the paper pr...

---

## 225. Steering at the Source: Style Modulation Heads for Robust Persona Control

**Authors**: Yoshihiro Izawa, Gouki Minegishi, Koshi Eguchi, Sosuke Hosokawa, Kenjiro Taura  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13249  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13249v1.pdf

**Abstract**:
> arXiv:2603.13249v1 Announce Type: cross 
Abstract: Activation steering offers a computationally efficient mechanism for controlling Large Language Models (LLMs) without fine-tuning. While effectively controlling target traits (e.g., persona), coherency degradation remains a major obstacle to safety and practical deployment. We hypothesize that this degradation stems from intervening on the residual stream, which indiscriminately affects aggregated features and inadvertently amplifies off-target noise. In this work, we identify a sparse subset of attention heads (only three heads) that independently govern persona and style formation, which we term Style Modulation Heads. Specifically, these heads can be localized via geometric analysis of internal representations, combining layer-wise cosi...

---

## 226. How Transformers Reject Wrong Answers: Rotational Dynamics of Factual Constraint Processing

**Authors**: Javier Mar\'in  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13259  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13259v1.pdf

**Abstract**:
> arXiv:2603.13259v1 Announce Type: cross 
Abstract: When a language model is fed a wrong answer, what happens inside the network? Current understanding treats truthfulness as a static property of individual-layer representations-a direction to be probed, a feature to be extracted. Less is known about the dynamics: how internal representations diverge across the full depth of the network when the model processes correct versus incorrect continuations.
  We introduce forced-completion probing, a method that presents identical queries with known correct and incorrect single-token continuations and tracks five geometric measurements across every layer of four decoder-only models(1.5B-13B parameters). We report three findings. First, correct and incorrect paths diverge through rotation, not resc...

---

## 227. How Meta-research Can Pave the Road Towards Trustworthy AI In Healthcare: Catalogue of Ideas and Roadmap for Future Research

**Authors**: Valerie B\"urger, Marlie Besouw, Jana Fehr, Riana Minocher, Emma Moorhead, Isabel Velarde, Louis Agh...  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13286  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13286v1.pdf

**Abstract**:
> arXiv:2603.13286v1 Announce Type: cross 
Abstract: Meta-research and Trustworthy AI (TAI) share common goals, namely improving evidence, robustness, and transparency, yet there is very little interplay between the two fields. To investigate the potential benefits of closer collaboration between the domains of TAI in healthcare and meta-research, we convened an interdisciplinary workshop funded by the Volkswagen Foundation in February 2025. The workshop aimed to collaboratively examine key tensions in translating AI ethics principles into practice and to identify potential solutions informed by meta-research approaches. A Design Thinking-informed co-creation approach was followed by an inductive descriptive analysis of the outputs. Our results demonstrate how meta-research can offer concret...

---

## 228. Information-Theoretic Constraints for Continual Vision-Language-Action Alignment

**Authors**: Libang Zhao, Qixin Zeng, Hongyin Zhang, Donglin Wang  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13335  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13335v1.pdf

**Abstract**:
> arXiv:2603.13335v1 Announce Type: cross 
Abstract: When deployed in open-ended robotic environments, Vision--Language--Action (VLA) models need to continually acquire new skills, yet suffer from severe catastrophic forgetting. We observe that this degradation is related to the deterioration of cross-modal information structure, where dependencies among visual observations, language instructions, and actions progressively diffuse during continual adaptation. But existing continual learning methods fail to preserve such cross-modal information dependencies. Thus, we propose Info-VLA, an information-preserving continual learning framework that maintains cross-modal information structure through two complementary constraints. Replay Anchor Contrastive Learning constructs stable alignment ancho...

---

## 229. DDS-UDA: Dual-Domain Synergy for Unsupervised Domain Adaptation in Joint Segmentation of Optic Disc and Optic Cup

**Authors**: Yusong Xiao, Yuxuan Wu, Li Xiao, Gang Qu, Haiye Huo, Yu-Ping Wang  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13345  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13345v1.pdf

**Abstract**:
> arXiv:2603.13345v1 Announce Type: cross 
Abstract: Convolutional neural networks (CNNs) have achieved exciting performance in joint segmentation of optic disc and optic cup on single-institution datasets. However, their clinical translation is hindered by two major challenges: limited availability of large-scale, high-quality annotations and performance degradation caused by domain shift during deployment across heterogeneous imaging protocols and acquisition platforms. While unsupervised domain adaptation (UDA) provides a way to mitigate these limitations, most existing approaches do not address cross-domain interference and intra-domain generalization within a unified framework. In this paper, we present the Dual-Domain Synergy UDA (DDS-UDA), a novel UDA framework that comprises two key ...

---

## 230. Post Training Quantization for Efficient Dataset Condensation

**Authors**: Linh-Tam Tran, Sung-Ho Bae  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13346  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13346v1.pdf

**Abstract**:
> arXiv:2603.13346v1 Announce Type: cross 
Abstract: Dataset Condensation (DC) distills knowledge from large datasets into smaller ones, accelerating training and reducing storage requirements. However, despite notable progress, prior methods have largely overlooked the potential of quantization for further reducing storage costs. In this paper, we take the first step to explore post-training quantization in dataset condensation, demonstrating its effectiveness in reducing storage size while maintaining representation quality without requiring expensive training cost. However, we find that at extremely low bit-widths (e.g., 2-bit), conventional quantization leads to substantial degradation in representation quality, negatively impacting the networks trained on these data. To address this, we...

---

## 231. MURE: Hierarchical Multi-Resolution Encoding via Vision-Language Models for Visual Document Retrieval

**Authors**: Fengbin Zhu, Zijing Cai, Yuzhe Wang, Pengyang Shao, Wenjie Wang, Fuli Feng, Richang Hong, Tat-Seng C...  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13349  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13349v1.pdf

**Abstract**:
> arXiv:2603.13349v1 Announce Type: cross 
Abstract: Visual Document Retrieval (VDR) requires representations that capture both fine-grained visual details and global document structure to ensure retrieval efficacy while maintaining computational efficiency. Existing VDR models struggle to balance effectiveness and efficiency when processing high-resolution documents: they often either lose fine-grained information or generate an excessive number of visual tokens, resulting in significant indexing overhead and high retrieval latency. In this work, we rethink the visual encoding mechanism and propose a new X-VisEmb paradigm that progresses from multi-resolution sampling and encoding, through cross-granularity feature fusion, to adaptive representation distillation. A preliminary study validat...

---

## 232. BrainCast: A Spatio-Temporal Forecasting Model for Whole-Brain fMRI Time Series Prediction

**Authors**: Yunlong Gao, Jinbo Yang, Li Xiao, Haiye Huo, Yang Ji, Hao Wang, Aiying Zhang, Yu-Ping Wang  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13361  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13361v1.pdf

**Abstract**:
> arXiv:2603.13361v1 Announce Type: cross 
Abstract: Functional magnetic resonance imaging (fMRI) enables noninvasive investigation of brain function, while short clinical scan durations, arising from human and non-human factors, usually lead to reduced data quality and limited statistical power for neuroimaging research. In this paper, we propose BrainCast, a novel spatio-temporal forecasting framework specifically tailored for whole-brain fMRI time series forecasting, to extend informative fMRI time series without additional data acquisition. It formulates fMRI time series forecasting as a multivariate time series prediction task and jointly models temporal dynamics within regions of interest (ROIs) and spatial interactions across ROIs. Specifically, BrainCast integrates a Spatial Interact...

---

## 233. Thinking in Uncertainty: Mitigating Hallucinations in MLRMs with Latent Entropy-Aware Decoding

**Authors**: Zhongxing Xu, Zhonghua Wang, Zhe Qian, Dachuan Shi, Feilong Tang, Ming Hu, Shiyan Su, Xiaocheng Zou,...  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13366  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13366v1.pdf

**Abstract**:
> arXiv:2603.13366v1 Announce Type: cross 
Abstract: Recent advancements in multimodal large reasoning models (MLRMs) have significantly improved performance in visual question answering. However, we observe that transition words (e.g., because, however, and wait) are closely associated with hallucinations and tend to exhibit high-entropy states. We argue that adequate contextual reasoning information can be directly extracted from the token probability distribution. Inspired by superposed representation theory, we propose leveraging latent superposed reasoning to integrate multiple candidate semantics and maintain latent reasoning trajectories. The hypothesis is that reliance on discrete textual inputs may drive the model toward sequential explicit reasoning, underutilizing dense contextual...

---

## 234. Geometry-Aware Semantic Reasoning for Training Free Video Anomaly Detection

**Authors**: Ali Zia, Usman Ali, Muhammad Umer Ramzan, Hamza Abid, Abdul Rehman, Wei Xiang  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13374  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13374v1.pdf

**Abstract**:
> arXiv:2603.13374v1 Announce Type: cross 
Abstract: Training-free video anomaly detection (VAD) has recently emerged as a scalable alternative to supervised approaches, yet existing methods largely rely on static prompting and geometry-agnostic feature fusion. As a result, anomaly inference is often reduced to shallow similarity matching over Euclidean embeddings, leading to unstable predictions and limited interpretability, especially in complex or hierarchically structured scenes. We introduce MM-VAD, a geometry-aware semantic reasoning framework for training free VAD that reframes anomaly detection as adaptive test-time inference rather than fixed feature comparison. Our approach projects caption-derived scene representations into hyperbolic space to better preserve hierarchical structur...

---

## 235. MAD: Microenvironment-Aware Distillation -- A Pretraining Strategy for Virtual Spatial Omics from Microscopy

**Authors**: Jiashu Han, Kunzan Liu, Yeojin Kim, Saurabh Sinha, Sixian You  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13401  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13401v1.pdf

**Abstract**:
> arXiv:2603.13401v1 Announce Type: cross 
Abstract: Bridging microscopy and omics would allow us to read molecular states from images-at single-cell resolution and tissue scale-without the cost and throughput limits of omics technologies. Self-supervised pretraining offers a scalable approach with minimal labels, yet how to encode single-cell identity within tissue environments-and the extent of biological information such models can capture-remains an open question. Here, we introduce MAD (microenvironment-aware distillation), a pretraining strategy that learns cell-centric embeddings by jointly self-distilling the morphology view and the microenvironment view of the same indexed cell into a unified embedding space. Across diverse tissues and imaging modalities, MAD achieves state-of-the-a...

---

## 236. Bridging the Visual-to-Physical Gap: Physically Aligned Representations for Fall Risk Analysis

**Authors**: Xianqi Zhang  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13410  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13410v1.pdf

**Abstract**:
> arXiv:2603.13410v1 Announce Type: cross 
Abstract: Vision-based fall analysis has advanced rapidly, but a key bottleneck remains: visually similarmotions can correspond to very different physical outcomes because small differences in contactmechanics and protective responses are hard to infer from appearance alone. Most existingapproaches handle this by supervised injury prediction, which depends on reliable injury labels.In practice, such labels are difficult to obtain: video evidence is often ambiguous (occlusion,viewpoint limits), and true injury events are rare and cannot be safely staged, leading to noisysupervision. We address this problem with PHARL (PHysics-aware Alignment RepresentationLearning), which learns physically meaningful fall representations without requiring clinicalout...

---

## 237. Spatial Transcriptomics as Images for Large-Scale Pretraining

**Authors**: Yishun Zhu, Jiaxin Qi, Jian Wang, Yuhua Zheng, Jianqiang Huang  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13432  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13432v1.pdf

**Abstract**:
> arXiv:2603.13432v1 Announce Type: cross 
Abstract: Spatial Transcriptomics (ST) profiles thousands of gene expression values at discrete spots with precise coordinates on tissue sections, preserving spatial context essential for clinical and pathological studies. With rising sequencing throughput and advancing platforms, the expanding data volumes motivate large-scale ST pretraining. However, the fundamental unit for pretraining, i.e., what constitutes a single training sample, remains ill-posed. Existing choices fall into two camps: (1) treating each spot as an independent sample, which discards spatial dependencies and collapses ST into single-cell transcriptomics; and (2) treating an entire slide as a single sample, which produces prohibitively large inputs and drastically fewer trainin...

---

## 238. MGMAR: Metal-Guided Metal Artifact Reduction for X-ray Computed Tomography

**Authors**: Hyoung Suk Park, Kiwan Jeon  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13447  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13447v1.pdf

**Abstract**:
> arXiv:2603.13447v1 Announce Type: cross 
Abstract: An X-ray computed tomography (CT), metal artifact reduction (MAR) remains a major challenge because metallic implants violate standard CT forward-model assumptions, producing severe streaking and shadowing artifacts that degrade diagnostic quality. We propose MGMAR, a metal-guided MAR method that explicitly leverages metal-related information throughout the reconstruction pipeline. MGMAR first generates a high-quality prior image by training a conditioned implicit neural representation (INR) using metal-unaffected projections, and then incorporates this prior into a normalized MAR (NMAR) framework for projection completion. To improve robustness under severe metal corruption, we pretrain the encoder-conditioned INR on paired metal-corrupte...

---

## 239. Opportunistic Cardiac Health Assessment: Estimating Phenotypes from Localizer MRI through Multi-Modal Representations

**Authors**: Busra Nur Zeybek, \"Ozg\"un Turgut, Yundi Zhang, Jiazhen Pan, Robert Graf, Sophie Starck, Daniel Rue...  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13590  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13590v1.pdf

**Abstract**:
> arXiv:2603.13590v1 Announce Type: cross 
Abstract: Cardiovascular diseases are the leading cause of death. Cardiac phenotypes (CPs), e.g., ejection fraction, are the gold standard for assessing cardiac health, but they are derived from cine cardiac magnetic resonance imaging (CMR), which is costly and requires high spatio-temporal resolution. Every magnetic resonance (MR) examination begins with rapid and coarse localizers for scan planning, which are discarded thereafter. Despite non-diagnostic image quality and lack of temporal information, localizers can provide valuable structural information rapidly. In addition to imaging, patient-level information, including demographics and lifestyle, influence the cardiac health assessment. Electrocardiograms (ECGs) are inexpensive, routinely orde...

---

## 240. The Equivalence Theorem: First-Class Relationships for Structurally Complete Database Systems

**Authors**: Matthew Alford  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13603  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13603v1.pdf

**Abstract**:
> arXiv:2603.13603v1 Announce Type: cross 
Abstract: We prove The Equivalence Theorem: structurally complete knowledge representation requires exactly four mutually entailing capabilities -- n-ary relationships with attributes, temporal validity, uncertainty quantification, and causal relationships between relationships -- collectively equivalent to treating relationships as first-class objects. Any system implementing one capability necessarily requires all four; any system missing one cannot achieve structural completeness. This result is constructive: we exhibit an Attributed Temporal Causal Hypergraph (ATCH) framework satisfying all four conditions simultaneously. The theorem yields a strict expressiveness hierarchy -- SQL < LPG < TypeDB < ATCH -- with witness queries that are structural...

---

## 241. GhanaNLP Parallel Corpora: Comprehensive Multilingual Resources for Low-Resource Ghanaian Languages

**Authors**: Lawrence Adu Gyamfi, Paul Azunre, Stephen Edward Moore, Joel Budu, Akwasi Asare, Mich-Seth Owusu, Jo...  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13793  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13793v1.pdf

**Abstract**:
> arXiv:2603.13793v1 Announce Type: cross 
Abstract: Low resource languages present unique challenges for natural language processing due to the limited availability of digitized and well structured linguistic data. To address this gap, the GhanaNLP initiative has developed and curated 41,513 parallel sentence pairs for the Twi, Fante, Ewe, Ga, and Kusaal languages, which are widely spoken across Ghana yet remain underrepresented in digital spaces. Each dataset consists of carefully aligned sentence pairs between a local language and English. The data were collected, translated, and annotated by human professionals and enriched with standard structural metadata to ensure consistency and usability. These corpora are designed to support research, educational, and commercial applications, inclu...

---

## 242. Is Seeing Believing? Evaluating Human Sensitivity to Synthetic Video

**Authors**: David Wegmann, Emil Stevnsborg, S{\o}ren Knudsen, Luca Rossi, Aske Mottelson  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13846  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13846v1.pdf

**Abstract**:
> arXiv:2603.13846v1 Announce Type: cross 
Abstract: Advances in machine learning have enabled the creation of realistic synthetic videos known as deepfakes. As deepfakes proliferate, concerns about rapid spread of disinformation and manipulation of public perception are mounting. Despite the alarming implications, our understanding of how individuals perceive synthetic media remains limited, obstructing the development of effective mitigation strategies. This paper aims to narrow this gap by investigating human responses to visual and auditory distortions of videos and deepfake-generated visuals and narration. In two between-subjects experiments, we study whether audio-visual distortions affect cognitive processing, such as subjective credibility assessment and objective learning outcomes. ...

---

## 243. Power Term Polynomial Algebra for Boolean Logic

**Authors**: Emanuele Sansone, Armando Solar-Lezama  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13854  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13854v1.pdf

**Abstract**:
> arXiv:2603.13854v1 Announce Type: cross 
Abstract: We introduce power term polynomial algebra, a representation language for Boolean formulae designed to bridge conjunctive normal form (CNF) and algebraic normal form (ANF). The language is motivated by the tiling mismatch between these representations: direct CNF<->ANF conversion may cause exponential blowup unless formulas are decomposed into smaller fragments, typically through auxiliary variables and side constraints. In contrast, our framework addresses this mismatch within the representation itself, compactly encoding structured families of monomials while representing CNF clauses directly, thereby avoiding auxiliary variables and constraints at the abstraction level. We formalize the language through power terms and power term polyno...

---

## 244. TransDex: Pre-training Visuo-Tactile Policy with Point Cloud Reconstruction for Dexterous Manipulation of Transparent Objects

**Authors**: Fengguan Li, Yifan Ma, Chen Qian, Wentao Rao, Weiwei Shang  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13869  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13869v1.pdf

**Abstract**:
> arXiv:2603.13869v1 Announce Type: cross 
Abstract: Dexterous manipulation enables complex tasks but suffers from self-occlusion, severe depth noise, and depth information loss when manipulating transparent objects. To solve this problem, this paper proposes TransDex, a 3D visuo-tactile fusion motor policy based on point cloud reconstruction pre-training. Specifically, we first propose a self-supervised point cloud reconstruction pre-training approach based on Transformer. This method accurately recovers the 3D structure of objects from interactive point clouds of dexterous hands, even when random noise and large-scale masking are added. Building on this, TransDex is constructed in which perceptual encoding adopts a fine-grained hierarchical scheme and multi-round attention mechanisms adapt...

---

## 245. Iterative Semantic Reasoning from Individual to Group Interests for Generative Recommendation with LLMs

**Authors**: Xiaofei Zhu, Jinfei Chen, Feiyang Yuan, Zhou Yang  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13934  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13934v1.pdf

**Abstract**:
> arXiv:2603.13934v1 Announce Type: cross 
Abstract: Recommendation systems aim to learn user interests from historical behaviors and deliver relevant items. Recent methods leverage large language models (LLMs) to construct and integrate semantic representations of users and items for capturing user interests. However, user behavior theories suggest that truly understanding user interests requires not only semantic integration but also semantic reasoning from explicit individual interests to implicit group interests. To this end, we propose an Iterative Semantic Reasoning Framework (ISRF) for generative recommendation. ISRF leverages LLMs to bridge explicit individual interests and implicit group interests in three steps. First, we perform multi-step bidirectional reasoning over item attribu...

---

## 246. Human-like Object Grouping in Self-supervised Vision Transformers

**Authors**: Hossein Adeli, Seoyoung Ahn, Andrew Luo, Mengmi Zhang, Nikolaus Kriegeskorte, Gregory Zelinsky  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13994  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13994v1.pdf

**Abstract**:
> arXiv:2603.13994v1 Announce Type: cross 
Abstract: Vision foundation models trained with self-supervised objectives achieve strong performance across diverse tasks and exhibit emergent object segmentation properties. However, their alignment with human object perception remains poorly understood. Here, we introduce a behavioral benchmark in which participants make same/different object judgments for dot pairs on naturalistic scenes, scaling up a classical psychophysics paradigm to over 1000 trials. We test a diverse set of vision models using a simple readout from their representations to predict subjects' reaction times. We observe a steady improvement across model generations, with both architecture and training objective contributing to alignment, and transformer-based models trained wi...

---

## 247. U-Face: An Efficient and Generalizable Framework for Unsupervised Facial Attribute Editing via Subspace Learning

**Authors**: Bo Liu, Xuan Cui, Run Zeng, Wei Duan, Chongwen Liu, Jinrui Qian, Lianggui Tang, Hongping Gan  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14004  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14004v1.pdf

**Abstract**:
> arXiv:2603.14004v1 Announce Type: cross 
Abstract: Latent space-based facial attribute editing methods have gained popularity in applications such as digital entertainment, virtual avatar creation, and human-computer interaction systems due to their potential for efficient and flexible attribute manipulation, particularly for continuous edits. Among these, unsupervised latent space-based methods, which discover effective semantic vectors without relying on labeled data, have attracted considerable attention in the research community. However, existing methods still encounter difficulties in disentanglement, as manipulating a specific facial attribute may unintentionally affect other attributes, complicating fine-grained controllability. To address these challenges, we propose a novel frame...

---

## 248. EI-Part: Explode for Completion and Implode for Refinement

**Authors**: Wanhu Sun, Zhongjin Luo, Heliang Zheng, Jiahao Chang, Chongjie Ye, Huiang He, Shengchu Zhao, Rongfei...  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14021  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14021v1.pdf

**Abstract**:
> arXiv:2603.14021v1 Announce Type: cross 
Abstract: Part-level 3D generation is crucial for various downstream applications, including gaming, film production, and industrial design. However, decomposing a 3D shape into geometrically plausible and meaningful components remains a significant challenge. Previous part-based generation methods often struggle to produce well-constructed parts, exhibiting poor structural coherence, geometric implausibility, inaccuracy, or inefficiency.
  To address these challenges, we introduce EI-Part, a novel framework specifically designed to generate high-quality 3D shapes with components, characterized by strong structural coherence, geometric plausibility, geometric fidelity, and generation efficiency. We propose utilizing distinct representations at diffe...

---

## 249. Beyond Means: Topological Causal Effects under Persistent-Homology Ignorability

**Authors**: Amir Saki, Usef Faghihi  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14169  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14169v1.pdf

**Abstract**:
> arXiv:2603.14169v1 Announce Type: cross 
Abstract: Average treatment effects (ATE) and conditional average treatment effects (CATE) are foundational causal estimands, but they target changes in expected outcomes and can miss treatment-induced changes in the shape of outcome distributions. A canonical failure mode occurs when control outcomes are unimodal, treated outcomes become bimodal, and both distributions have the same mean. In such cases mean-based causal estimands are zero even though the geometry and topology of the outcome law change substantially. This paper develops a topological causal framework based on persistent homology. We formalize a persistent-homology ignorability condition, define topological analogues of CATE and ATE, and prove that these estimands are identifiable up...

---

## 250. ChArtist: Generating Pictorial Charts with Unified Spatial and Subject Control

**Authors**: Shishi Xiao, Tongyu Zhou, David Laidlaw, Gromit Yeuk-Yin Chan  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14209  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14209v1.pdf

**Abstract**:
> arXiv:2603.14209v1 Announce Type: cross 
Abstract: A pictorial chart is an effective medium for visual storytelling, seamlessly integrating visual elements with data charts. However, creating such images is challenging because the flexibility of visual elements often conflicts with the rigidity of chart structures. This process thus requires a creative deformation that maintains both data faithfulness and visual aesthetics. Current methods that extract dense structural cues from natural images (e.g., edge or depth maps) are ill-suited as conditioning signals for pictorial chart generation. We present ChArtist, a domain-specific diffusion model for generating pictorial charts automatically, offering two distinct types of control: 1) spatial control that aligns well with the chart structure,...

---

## 251. UniFusion: A Unified Image Fusion Framework with Robust Representation and Source-Aware Preservation

**Authors**: Xingyuan Li, Songcheng Du, Yang Zou, HaoYuan Xu, Zhiying Jiang, Jinyuan Liu  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14214  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14214v1.pdf

**Abstract**:
> arXiv:2603.14214v1 Announce Type: cross 
Abstract: Image fusion aims to integrate complementary information from multiple source images to produce a more informative and visually consistent representation, benefiting both human perception and downstream vision tasks. Despite recent progress, most existing fusion methods are designed for specific tasks (i.e., multi-modal, multi-exposure, or multi-focus fusion) and struggle to effectively preserve source information during the fusion process. This limitation primarily arises from task-specific architectures and the degradation of source information caused by deep-layer propagation. To overcome these issues, we propose UniFusion, a unified image fusion framework designed to achieve cross-task generalization. First, leveraging DINOv3 for modal...

---

## 252. Membership Inference for Contrastive Pre-training Models with Text-only PII Queries

**Authors**: Ruoxi Cheng, Yizhong Ding, Hongyi Zhang, Yiyan Huang  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14222  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14222v1.pdf

**Abstract**:
> arXiv:2603.14222v1 Announce Type: cross 
Abstract: Contrastive pretraining models such as CLIP and CLAP underpin many vision-language and audio-language systems, yet their reliance on web-scale data raises growing concerns about memorizing Personally Identifiable Information (PII). Auditing such models via membership inference is challenging in practice: shadow-model MIAs are computationally prohibitive for large multimodal backbones, and existing multimodal attacks typically require querying the target with paired biometric inputs, thereby directly exposing sensitive biometric information to the target model. We propose Unimodal Membership Inference Detector (UMID), a text-only auditing framework that performs text-guided cross-modal latent inversion and extracts two complementary signals...

---

## 253. Bringing Model Editing to Generative Recommendation in Cold-Start Scenarios

**Authors**: Chenglei Shen, Teng Shi, Weijie Yu, Xiao Zhang, Jun Xu  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14259  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14259v1.pdf

**Abstract**:
> arXiv:2603.14259v1 Announce Type: cross 
Abstract: Generative recommendation (GR) has shown strong potential for sequential recommendation in an end-to-end generation paradigm. However, existing GR models suffer from severe cold-start collapse: their recommendation accuracy on cold-start items can drop to near zero. Current solutions typically rely on retraining with cold-start interactions, which is hindered by sparse feedback, high computational cost, and delayed updates, limiting practical utility in rapidly evolving recommendation catalogs. Inspired by model editing in NLP, which enables training-free knowledge injection into large language models, we explore how to bring this paradigm to generative recommendation. This, however, faces two key challenges: GR lacks the explicit subject-...

---

## 254. 4D Synchronized Fields: Motion-Language Gaussian Splatting for Temporal Scene Understanding

**Authors**: Mohamed Rayan Barhdadi, Samir Abdaljalil, Rasul Khanbayov, Erchin Serpedin, Hasan Kurban  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14301  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14301v1.pdf

**Abstract**:
> arXiv:2603.14301v1 Announce Type: cross 
Abstract: Current 4D representations decouple geometry, motion, and semantics: reconstruction methods discard interpretable motion structure; language-grounded methods attach semantics after motion is learned, blind to how objects move; and motion-aware methods encode dynamics as opaque per-point residuals without object-level organization. We propose 4D Synchronized Fields, a 4D Gaussian representation that learns object-factored motion in-loop during reconstruction and synchronizes language to the resulting kinematics through a per-object conditioned field. Each Gaussian trajectory is decomposed into shared object motion plus an implicit residual, and a kinematic-conditioned ridge map predicts temporal semantic variation, yielding a single represe...

---

## 255. AerialVLA: A Vision-Language-Action Model for UAV Navigation via Minimalist End-to-End Control

**Authors**: Peng Xu, Zhengnan Deng, Jiayan Deng, Zonghua Gu, Shaohua Wan  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14363  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14363v1.pdf

**Abstract**:
> arXiv:2603.14363v1 Announce Type: cross 
Abstract: Vision-Language Navigation (VLN) for Unmanned Aerial Vehicles (UAVs) demands complex visual interpretation and continuous control in dynamic 3D environments. Existing hierarchical approaches rely on dense oracle guidance or auxiliary object detectors, creating semantic gaps and limiting genuine autonomy. We propose AerialVLA, a minimalist end-to-end Vision-Language-Action framework mapping raw visual observations and fuzzy linguistic instructions directly to continuous physical control signals. First, we introduce a streamlined dual-view perception strategy that reduces visual redundancy while preserving essential cues for forward navigation and precise grounding, which additionally facilitates future simulation-to-reality transfer. To rec...

---

## 256. Distilling Reasoning Without Knowledge: A Framework for Reliable LLMs

**Authors**: Auksarapak Kietkajornrit, Jad Tarifi, Nima Asgharbeygi  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14458  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14458v1.pdf

**Abstract**:
> arXiv:2603.14458v1 Announce Type: cross 
Abstract: Fact-seeking question answering with large language models (LLMs) remains unreliable when answers depend on up-to-date or conflicting information. Although retrieval-augmented and tool-using LLMs reduce hallucinations, they often rely on implicit planning, leading to inefficient tool usage. We propose a modular framework that explicitly separates planning from factual retrieval and answer synthesis. A lightweight student planner is trained via a teacher-student framework to generate structured decompositions consisting of abstract reasoning steps and searchable fact requests. The supervision signals contain only planning traces and fact requests, without providing factual answers or retrieved evidence. At inference, the planner produces pl...

---

## 257. LLM-Augmented Release Intelligence: Automated Change Summarization and Impact Analysis in Cloud-Native CI/CD Pipelines

**Authors**: Happy Bhati (Northeastern University)  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14619  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14619v1.pdf

**Abstract**:
> arXiv:2603.14619v1 Announce Type: cross 
Abstract: Cloud-native software delivery platforms orchestrate releases through complex, multi-stage pipelines composed of dozens of independently versioned tasks. When code is promoted between environments -- development to staging, staging to production -- engineering teams need timely, accurate communication about what changed and what downstream components are affected. Manual preparation of such release communication is slow, inconsistent, and particularly error-prone in repositories where a single promotion may bundle contributions from many authors across numerous pipeline tasks. We present a framework for AI-augmented release intelligence that combines three capabilities: (1) automated commit collection with semantic filtering to surface sub...

---

## 258. TopoCL: Topological Contrastive Learning for Medical Imaging

**Authors**: Guangyu Meng, Pengfei Gu, Peixian Liang, John P. Lalor, Erin Wolf Chambers, Danny Z. Chen  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14647  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14647v1.pdf

**Abstract**:
> arXiv:2603.14647v1 Announce Type: cross 
Abstract: Contrastive learning (CL) has become a powerful approach for learning representations from unlabeled images. However, existing CL methods focus predominantly on visual appearance features while neglecting topological characteristics (e.g., connectivity patterns, boundary configurations, cavity formations) that provide valuable cues for medical image analysis. To address this limitation, we propose a new topological CL framework (TopoCL) that explicitly exploits topological structures during contrastive learning for medical imaging. Specifically, we first introduce topology-aware augmentations that control topological perturbations using a relative bottleneck distance between persistence diagrams, preserving medically relevant topological p...

---

## 259. Beyond Local Code Optimization: Multi-Agent Reasoning for Software System Optimization

**Authors**: Huiyun Peng, Parth Vinod Patil, Antonio Zhong Qiu, George K. Thiruvathukal, James C. Davis  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14703  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14703v1.pdf

**Abstract**:
> arXiv:2603.14703v1 Announce Type: cross 
Abstract: Large language models and AI agents have recently shown promise in automating software performance optimization, but existing approaches predominantly rely on local, syntax-driven code transformations. This limits their ability to reason about program behavior and capture whole system performance interactions. As modern software increasingly comprises interacting components - such as microservices, databases, and shared infrastructure - effective code optimization requires reasoning about program structure and system architecture beyond individual functions or files.
  This paper explores the feasibility of whole system optimization for microservices. We introduce a multi-agent framework that integrates control-flow and data-flow represent...

---

## 260. Architecture-Agnostic Feature Synergy for Universal Defense Against Heterogeneous Generative Threats

**Authors**: Bingxue Zhang, Yang Gao, Feida Zhu, Yanyan Shen, Yang Shi  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14860  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14860v1.pdf

**Abstract**:
> arXiv:2603.14860v1 Announce Type: cross 
Abstract: Generative AI deployment poses unprecedented challenges to content safety and privacy. However, existing defense mechanisms are often tailored to specific architectures (e.g., Diffusion Models or GANs), creating fragile "defense silos" that fail against heterogeneous generative threats. This paper identifies a fundamental optimization barrier in naive pixel-space ensemble strategies: due to divergent objective functions, pixel-level gradients from heterogeneous generators become statistically orthogonal, causing destructive interference. To overcome this, we observe that despite disparate low-level mechanisms, high-level feature representations of generated content exhibit alignment across architectures. Based on this, we propose the Archi...

---

## 261. OrgForge: A Multi-Agent Simulation Framework for Verifiable Synthetic Corporate Corpora

**Authors**: Jeffrey Flynt  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.14997  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.14997v1.pdf

**Abstract**:
> arXiv:2603.14997v1 Announce Type: cross 
Abstract: Evaluating retrieval-augmented generation (RAG) pipelines requires corpora where ground truth is knowable, temporally structured, and cross-artifact properties that real-world datasets rarely provide cleanly. Existing resources such as the Enron corpus carry legal ambiguity, demographic skew, and no structured ground truth. Purely LLM-generated synthetic data solves the legal problem but introduces a subtler one: the generating model cannot be prevented from hallucinating facts that contradict themselves across documents.We present OrgForge, an open-source multi-agent simulation framework that enforces a strict physics-cognition boundary: a deterministic Python engine maintains a SimEvent ground truth bus; large language models generate on...

---

## 262. What Matters for Scalable and Robust Learning in End-to-End Driving Planners?

**Authors**: David Holtz, Niklas Hanselmann, Simon Doll, Marius Cordts, Bernt Schiele  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15185  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15185v1.pdf

**Abstract**:
> arXiv:2603.15185v1 Announce Type: cross 
Abstract: End-to-end autonomous driving has gained significant attention for its potential to learn robust behavior in interactive scenarios and scale with data. Popular architectures often build on separate modules for perception and planning connected through latent representations, such as bird's eye view feature grids, to maintain end-to-end differentiability. This paradigm emerged mostly on open-loop datasets, with evaluation focusing not only on driving performance, but also intermediate perception tasks. Unfortunately, architectural advances that excel in open-loop often fail to translate to scalable learning of robust closed-loop driving. In this paper, we systematically re-examine the impact of common architectural patterns on closed-loop p...

---

## 263. RieMind: Geometry-Grounded Spatial Agent for Scene Understanding

**Authors**: Fernando Ropero, Erkin Turkoz, Daniel Matos, Junqing Du, Antonio Ruiz, Yanfeng Zhang, Lu Liu, Mingwe...  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15386  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15386v1.pdf

**Abstract**:
> arXiv:2603.15386v1 Announce Type: cross 
Abstract: Visual Language Models (VLMs) have increasingly become the main paradigm for understanding indoor scenes, but they still struggle with metric and spatial reasoning. Current approaches rely on end-to-end video understanding or large-scale spatial question answering fine-tuning, inherently coupling perception and reasoning. In this paper, we investigate whether decoupling perception and reasoning leads to improved spatial reasoning. We propose an agentic framework for static 3D indoor scene reasoning that grounds an LLM in an explicit 3D scene graph (3DSG). Rather than ingesting videos directly, each scene is represented as a persistent 3DSG constructed by a dedicated perception module. To isolate reasoning performance, we instantiate the 3D...

---

## 264. Detection of Autonomous Shuttles in Urban Traffic Images Using Adaptive Residual Context

**Authors**: Mohamed Aziz Younes, Nicolas Saunier, Guillaume-Alexandre Bilodeau  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15404  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15404v1.pdf

**Abstract**:
> arXiv:2603.15404v1 Announce Type: cross 
Abstract: The progressive automation of transport promises to enhance safety and sustainability through shared mobility. Like other vehicles and road users, and even more so for such a new technology, it requires monitoring to understand how it interacts in traffic and to evaluate its safety. This can be done with fixed cameras and video object detection. However, the addition of new detection targets generally requires a fine-tuning approach for regular detection methods. Unfortunately, this implementation strategy will lead to a phenomenon known as catastrophic forgetting, which causes a degradation in scene understanding. In road safety applications, preserving contextual scene knowledge is of the utmost importance for protecting road users. We i...

---

## 265. Agentic workflow enables the recovery of critical materials from complex feedstocks via selective precipitation

**Authors**: Andrew Ritchhart, Sarah I. Allec, Pravalika Butreddy, Krista Kulesa, Qingpu Wang, Dan Thien Nguyen, ...  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15491  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15491v1.pdf

**Abstract**:
> arXiv:2603.15491v1 Announce Type: cross 
Abstract: We present a multi-agentic workflow for critical materials recovery that deploys a series of AI agents and automated instruments to recover critical materials from produced water and magnet leachates. This approach achieves selective precipitation from real-world feedstocks using simple chemicals, accelerating the development of efficient, adaptable, and scalable separations to a timeline of days, rather than months and years.

---

## 266. Mechanistic Origin of Moral Indifference in Language Models

**Authors**: Lingyu Li, Yan Teng, Yingchun Wang  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.15615  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.15615v1.pdf

**Abstract**:
> arXiv:2603.15615v1 Announce Type: cross 
Abstract: Existing behavioral alignment techniques for Large Language Models (LLMs) often neglect the discrepancy between surface compliance and internal unaligned representations, leaving LLMs vulnerable to long-tail risks. More crucially, we posit that LLMs possess an inherent state of moral indifference due to compressing distinct moral concepts into uniform probability distributions. We verify and remedy this indifference in LLMs' latent representations, utilizing 251k moral vectors constructed upon Prototype Theory and the Social-Chemistry-101 dataset. Firstly, our analysis across 23 models reveals that current LLMs fail to represent the distinction between opposed moral categories and fine-grained typicality gradients within these categories; ...

---

## 267. Bid2X: Revealing Dynamics of Bidding Environment in Online Advertising from A Foundation Model Lens

**Authors**: Jiahao Ji, Tianyu Wang, Yeshu Li, Yushen Huo, Zhilin Zhang, Chuan Yu, Jian Xu, Bo Zheng  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.23410  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.23410v2.pdf

**Abstract**:
> arXiv:2510.23410v2 Announce Type: replace 
Abstract: Auto-bidding is crucial in facilitating online advertising by automatically providing bids for advertisers. While previous work has made great efforts to model bidding environments for better ad performance, it has limitations in generalizability across environments since these models are typically tailored for specific bidding scenarios. To this end, we approach the scenario-independent principles through a unified function that estimates the achieved effect under specific bids, such as budget consumption, gross merchandise volume (GMV), page views, etc. Then, we propose a bidding foundation model Bid2X to learn this fundamental function from data in various scenarios. Our Bid2X is built over uniform series embeddings that encode hetero...

---

## 268. Neural Value Iteration

**Authors**: Yang You, Ufuk \c{C}ak{\i}r, Alex Schutz, Nick Hawes  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2511.08825  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2511.08825v3.pdf

**Abstract**:
> arXiv:2511.08825v3 Announce Type: replace 
Abstract: The value function of a POMDP exhibits the piecewise-linear-convex (PWLC) property and can be represented as a finite set of hyperplanes, known as $\alpha$-vectors. Most state-of-the-art POMDP solvers (offline planners) follow the point-based value iteration scheme, which performs Bellman backups on $\alpha$-vectors at reachable belief points until convergence. However, since each $\alpha$-vector is $|S|$-dimensional, these methods quickly become intractable for large-scale problems due to the prohibitive computational cost of Bellman backups. In this work, we demonstrate that the PWLC property allows a POMDP's value function to be alternatively represented as a finite set of neural networks. This insight enables a novel POMDP planning a...

---

## 269. Right for the Wrong Reasons: Epistemic Regret Minimization for Causal Rung Collapse in LLMs

**Authors**: Edward Y. Chang  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.11675  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.11675v2.pdf

**Abstract**:
> arXiv:2602.11675v2 Announce Type: replace 
Abstract: Machine learning systems that are "right for the wrong reasons" achieve high performance through shortcuts that collapse under distributional shift. We show this pathology has a precise causal origin: autoregressive training provides no gradient signal to distinguish association P(Y|X) from intervention P(Y|do(X)), a failure we formalize as Rung Collapse. When outcome-based learning reinforces correct answers obtained through incorrect causal models, the agent becomes entrenched in flawed reasoning, a phenomenon we term Aleatoric Entrenchment. We propose Epistemic Regret Minimization (ERM), a belief revision objective that penalizes errors in causal reasoning independently of task success, and embed it within a three-layer architecture w...

---

## 270. Grounding Machine Creativity in Game Design Knowledge Representations: Empirical Probing of LLM-Based Executable Synthesis of Goal Playable Patterns under Structural Constraints

**Authors**: Hugh Xuechen Liu, K{\i}van\c{c} Tatar  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.07101  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.07101v2.pdf

**Abstract**:
> arXiv:2603.07101v2 Announce Type: replace 
Abstract: Creatively translating complex gameplay ideas into executable artifacts (e.g., games as Unity projects and code) remains a central challenge in computational game creativity. Gameplay design patterns provide a structured representation for describing gameplay phenomena, enabling designers to decompose high-level ideas into entities, constraints, and rule-driven dynamics. Among them, goal patterns formalize common player-objective relationships. Goal Playable Concepts (GPCs) operationalize these abstractions as playable Unity engine implementations, supporting experiential exploration and compositional gameplay design. We frame scalable playable pattern realization as a problem of constrained executable creative synthesis: generated artif...

---

## 271. Unsupervised Point Cloud Pre-Training via Contrasting and Clustering

**Authors**: Guofeng Mei, Xiaoshui Huang, Juan Liu, Jian Zhang, Qiang Wu  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2202.02543  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2202.02543v3.pdf

**Abstract**:
> arXiv:2202.02543v3 Announce Type: replace-cross 
Abstract: Annotating large-scale point clouds is highly time-consuming and often infeasible for many complex real-world tasks. Point cloud pre-training has therefore become a promising strategy for learning discriminative representations without labeled data. In this paper, we propose a general unsupervised pre-training framework, termed ConClu, which jointly integrates contrasting and clustering. The contrasting objective maximizes the similarity between feature representations extracted from two augmented views of the same point cloud, while the clustering objective simultaneously partitions the data and enforces consistency between cluster assignments across augmentations. Experimental results on multiple downstream tasks show that our me...

---

## 272. Virtual Full-stack Scanning of Brain MRI via Imputing Any Quantised Code

**Authors**: Yicheng Wu, Tao Song, Zhonghua Wu, Jin Ye, Zongyuan Ge, Wenjia Bai, Zhaolin Chen, Jianfei Cai  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2501.18328  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2501.18328v3.pdf

**Abstract**:
> arXiv:2501.18328v3 Announce Type: replace-cross 
Abstract: Magnetic resonance imaging (MRI) is a powerful and versatile imaging technique, offering a wide spectrum of information about the anatomy by employing different acquisition modalities. However, in the clinical workflow, it is impractical to collect all relevant modalities due to the scan time and cost constraints. Virtual full-stack scanning aims to impute missing MRI modalities from available but incomplete acquisitions, offering a cost-efficient solution to enhance data completeness and clinical usability. Existing imputation methods often depend on global conditioning or modality-specific designs, which limit their generalisability across patient cohorts and imaging protocols. To address these limitations, we propose CodeBrain, ...

---

## 273. Adaptive Deep Learning for Breast Cancer Subtype Prediction Via Misprediction Risk Analysis

**Authors**: Gul Sheeraz, Qun Chen, Liu Feiyu, Zhou Fengjin  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2503.12778  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2503.12778v2.pdf

**Abstract**:
> arXiv:2503.12778v2 Announce Type: replace-cross 
Abstract: Breast cancer remains a leading cause of cancer-related mortality worldwide. Early detection is critical, yet manual histopathology analysis is complex and subject to inter-observer variability. While deep neural network-based diagnostic systems have advanced binary tasks, they struggle with multiclass subtype prediction due to inter-class similarity, class imbalance, and domain shifts, resulting in frequent mispredictions. This study proposes MultiRisk, an adaptive learning framework that quantifies and mitigates misprediction risk in breast cancer subtype prediction from histopathology images. MultiRisk employs a multiclass misprediction risk analysis model that ranks misprediction likelihood using interpretable features derived ...

---

## 274. CSD-VAR: Content-Style Decomposition in Visual Autoregressive Models

**Authors**: Quang-Binh Nguyen, Minh Luu, Quang Nguyen, Anh Tran, Khoi Nguyen  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2507.13984  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2507.13984v2.pdf

**Abstract**:
> arXiv:2507.13984v2 Announce Type: replace-cross 
Abstract: Disentangling content and style from a single image, known as content-style decomposition (CSD), enables recontextualization of extracted content and stylization of extracted styles, offering greater creative flexibility in visual synthesis. While recent personalization methods have explored the decomposition of explicit content style, they remain tailored for diffusion models. Meanwhile, Visual Autoregressive Modeling (VAR) has emerged as a promising alternative with a next-scale prediction paradigm, achieving performance comparable to that of diffusion models. In this paper, we explore VAR as a generative framework for CSD, leveraging its scale-wise generation process for improved disentanglement. To this end, we propose CSD-VAR,...

---

## 275. Distributional Semantics Tracing: A Framework for Explaining Hallucinations in Large Language Models

**Authors**: Gagan Bhatia, Somayajulu G Sripada, Kevin Allan, Jacobo Azcona  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.06107  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.06107v3.pdf

**Abstract**:
> arXiv:2510.06107v3 Announce Type: replace-cross 
Abstract: Hallucinations in large language models (LLMs) produce fluent continuations that are not supported by the prompt, especially under minimal contextual cues and ambiguity. We introduce Distributional Semantics Tracing (DST), a model-native method that builds layer-wise semantic maps at the answer position by decoding residual-stream states through the unembedding, selecting a compact top-$K$ concept set, and estimating directed concept-to-concept support via lightweight causal tracing. Using these traces, we test a representation-level hypothesis: hallucinations arise from correlation-driven representational drift across depth, where the residual stream is pulled toward a locally coherent but context-inconsistent concept neighborhood...

---

## 276. CARE: Contrastive Alignment for ADL Recognition from Event-Triggered Sensor Streams

**Authors**: Junhao Zhao, Zishuai Liu, Ruili Fang, Jin Lu, Linghan Zhang, Fei Dou  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.16988  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.16988v3.pdf

**Abstract**:
> arXiv:2510.16988v3 Announce Type: replace-cross 
Abstract: The recognition of Activities of Daily Living (ADLs) from event-triggered ambient sensors is an essential task in Ambient Assisted Living, yet existing methods remain constrained by representation-level limitations. Sequence-based approaches preserve temporal order of sensor activations but are sensitive to noise and lack spatial awareness, while image-based approaches capture global patterns and implicit spatial correlations but compress fine-grained temporal dynamics and distort sensor layouts. Naive fusion (e.g., feature concatenation) fails to enforce alignment between sequence- and image-based representation views, underutilizing their complementary strengths. We propose Contrastive Alignment for ADL Recognition from Event-Tri...

---

## 277. IDALC: A Semi-Supervised Framework for Intent Detection and Active Learning based Correction

**Authors**: Ankan Mullick, Sukannya Purkayastha, Saransh Sharma, Pawan Goyal, Niloy Ganguly  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2511.05921  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2511.05921v3.pdf

**Abstract**:
> arXiv:2511.05921v3 Announce Type: replace-cross 
Abstract: Voice-controlled dialog systems have become immensely popular due to their ability to perform a wide range of actions in response to diverse user queries. These agents possess a predefined set of skills or intents to fulfill specific user tasks. But every system has its own limitations. There are instances where, even for known intents, if any model exhibits low confidence, it results in rejection of utterances that necessitate manual annotation. Additionally, as time progresses, there may be a need to retrain these agents with new intents from the system-rejected queries to carry out additional tasks. Labeling all these emerging intents and rejected utterances over time is impractical, thus calling for an efficient mechanism to re...

---

## 278. RAG-3DSG: Enhancing 3D Scene Graphs with Re-Shot Guided Retrieval-Augmented Generation

**Authors**: Yue Chang, Rufeng Chen, Zhaofan Zhang, Yi Chen, Yifan Tian, Sihong Xie  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2601.10168  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2601.10168v2.pdf

**Abstract**:
> arXiv:2601.10168v2 Announce Type: replace-cross 
Abstract: Open-vocabulary 3D Scene Graph (3DSG) can enhance various downstream tasks in robotics by leveraging structured semantic representations, yet current 3DSG construction methods suffer from semantic inconsistencies caused by noisy cross-image aggregation under occlusions and constrained viewpoints. To mitigate the impact of such inconsistency, we propose RAG-3DSG, which introduces re-shot guided uncertainty estimation. By measuring the semantic consistency between original limited viewpoints and re-shot optimal viewpoints, this method quantifies the underlying semantic ambiguity of each graph object. Based on this quantification, we devise an Object-level Retrieval-Augmented Generation (RAG) that leverages low-uncertainty objects as ...

---

## 279. \textsc{NaVIDA}: Vision-Language Navigation with Inverse Dynamics Augmentation

**Authors**: Weiye Zhu, Zekai Zhang, Xiangchen Wang, Hewei Pan, Teng Wang, Tiantian Geng, Rongtao Xu, Feng Zheng  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2601.18188  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2601.18188v2.pdf

**Abstract**:
> arXiv:2601.18188v2 Announce Type: replace-cross 
Abstract: Vision-and-Language Navigation (VLN) requires agents to interpret natural language instructions and act coherently in visually rich environments. However, most existing methods rely on reactive state-action mappings without explicitly action-grounded visual dynamics modeling. Lacking awareness of how actions transform subsequent visual observations, agents cannot plan actions rationally, leading to unstable behaviors, weak generalization, and cumulative error along trajectory. To address these issues, we introduce \textsc{NaVIDA} (\textbf{Nav}igation with \textbf{I}nverse \textbf{D}ynamics \textbf{A}ugmentation), a lightweight VLN framework that incorporates inverse dynamics supervision (IDS) as an explicit objective to embed actio...

---

## 280. BabyReasoningBench: Generating Developmentally-Inspired Reasoning Tasks for Evaluating Baby Language Models

**Authors**: Kaustubh D. Dhole  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2601.18933  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2601.18933v2.pdf

**Abstract**:
> arXiv:2601.18933v2 Announce Type: replace-cross 
Abstract: Traditional evaluations of reasoning capabilities of language models are dominated by adult-centric benchmarks that presuppose broad world knowledge, complex instruction following, and mature pragmatic competence. These assumptions are mismatched to baby language models trained on developmentally plausible input such as child-directed speech and early-childhood narratives, and they obscure which reasoning abilities (if any) emerge under such constraints. We introduce BabyReasoningBench, a GPT-5.2 generated benchmark of 19 reasoning tasks grounded in classic paradigms from developmental psychology, spanning theory of mind, analogical and relational reasoning, causal inference and intervention selection, and core reasoning primitives...

---

## 281. When Pretty Isn't Useful: Investigating Why Modern Text-to-Image Models Fail as Reliable Training Data Generators

**Authors**: Krzysztof Adamkiewicz, Brian Moser, Stanislav Frolov, Tobias Christian Nauen, Federico Raue, Andreas...  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.19946  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.19946v3.pdf

**Abstract**:
> arXiv:2602.19946v3 Announce Type: replace-cross 
Abstract: Recent text-to-image (T2I) diffusion models produce visually stunning images and demonstrate excellent prompt following. But do they perform well as synthetic vision data generators? In this work, we revisit the promise of synthetic data as a scalable substitute for real training sets and uncover a surprising performance regression. We generate large-scale synthetic datasets using state-of-the-art T2I models released between 2022 and 2025, train standard classifiers solely on this synthetic data, and evaluate them on real test data. Despite observable advances in visual fidelity and prompt adherence, classification accuracy on real test data consistently declines with newer T2I models as training data generators. Our analysis revea...

---

## 282. Agora: Teaching the Skill of Consensus-Finding with AI Personas Grounded in Human Voice

**Authors**: Suyash Fulay, Prerna Ravi, Om Gokhale, Eugene Yi, Michiel Bakker, Deb Roy  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.07339  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.07339v2.pdf

**Abstract**:
> arXiv:2603.07339v2 Announce Type: replace-cross 
Abstract: Deliberative democratic theory suggests that civic competence: the capacity to navigate disagreement, weigh competing values, and arrive at collective decisions is not innate but developed through practice. Yet opportunities to cultivate these skills remain limited, as traditional deliberative processes like citizens' assemblies reach only a small fraction of the population. We present Agora, an early-stage AI-powered platform that uses LLMs to organize authentic human voices on policy issues, helping users build consensus-finding skills by proposing and revising policy recommendations, hearing supporting and opposing perspectives, and receiving feedback on how policy changes affect predicted support. In a preliminary study with 44...

---

## 283. EvoDriveVLA: Evolving Autonomous Driving Vision-Language-Action Model via Collaborative Perception-Planning Distillation

**Authors**: Jiajun Cao, Xiaoan Zhang, Xiaobao Wei, Liyuqiu Huang, Wang Zijian, Hanzhen Zhang, Zhengyu Jia, Wei M...  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.09465  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.09465v2.pdf

**Abstract**:
> arXiv:2603.09465v2 Announce Type: replace-cross 
Abstract: Vision-Language-Action models have shown great promise for autonomous driving, yet they suffer from degraded perception after unfreezing the visual encoder and struggle with accumulated instability in long-term planning. To address these challenges, we propose EvoDriveVLA-a novel collaborative perception-planning distillation framework that integrates self-anchored perceptual constraints and oracle-guided trajectory optimization. Specifically, self-anchored visual distillation leverages self-anchor teacher to deliver visual anchoring constraints, regularizing student representations via trajectory-guided key-region awareness. In parallel, oracle-guided trajectory distillation employs a future-aware oracle teacher with coarse-to-fin...

---

## 284. Evaluating Adjective-Noun Compositionality in LLMs: Functional vs Representational Perspectives

**Authors**: Ruchira Dhar, Qiwei Peng, Anders S{\o}gaard  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.09994  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.09994v2.pdf

**Abstract**:
> arXiv:2603.09994v2 Announce Type: replace-cross 
Abstract: Compositionality is considered central to language abilities. As performant language systems, how do large language models (LLMs) do on compositional tasks? We evaluate adjective-noun compositionality in LLMs using two complementary setups: prompt-based functional assessment and a representational analysis of internal model states. Our results reveal a striking divergence between task performance and internal states. While LLMs reliably develop compositional representations, they fail to translate consistently into functional task success across model variants. Consequently, we highlight the importance of contrastive evaluation for obtaining a more complete understanding of model capabilities.

---

## 285. UAV traffic scene understanding: A regulation embedded multi-modal network and a unified benchmark

**Authors**: Yu Zhang, Zhicheng Zhao, Ze Luo, Chenglong Li, Jin Tang  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10722  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10722v2.pdf

**Abstract**:
> arXiv:2603.10722v2 Announce Type: replace-cross 
Abstract: Traffic scene understanding from unmanned aerial vehicle (UAV) platforms is crucial for intelligent transportation systems due to its flexible deployment and wide-area monitoring capabilities. However, existing methods face significant challenges in real-world surveillance, as their heavy reliance on optical imagery leads to severe performance degradation under adverse illumination conditions like nighttime and fog. Furthermore, current Visual Question Answering (VQA) models are restricted to elementary perception tasks, lacking the domain-specific regulatory knowledge required to assess complex traffic behaviors. To address these limitations, we propose a novel Multi-modal Traffic Cognition Network (MTCNet) for robust UAV traffic ...

---

## 286. The DIME Architecture: A Unified Operational Algorithm for Neural Representation, Dynamics, Control and Integration

**Authors**: Ionel Cristian Vladu, Nicu Bizdoaca, Ionica Pirici, Tudor-Adrian Balseanu, Eduard Nicusor Bondoc  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12286  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12286v2.pdf

**Abstract**:
> arXiv:2603.12286v2 Announce Type: replace-cross 
Abstract: Modern neuroscience has accumulated extensive evidence on perception, memory, prediction, valuation, and consciousness, yet still lacks an explicit operational architecture capable of integrating these phenomena within a unified computational framework. Existing theories address specific aspects of neural function: predictive coding and active inference emphasize hierarchical inference and prediction error minimization; engram theories explain memory through distributed cell assemblies; neuromodulatory accounts focus on value-dependent regulation of plasticity and behaviour; and global workspace or large-scale network models investigate mechanisms underlying conscious access. Despite their explanatory power, these approaches remain...

---

## 287. Optimizing Task Completion Time Updates Using POMDPs

**Authors**: Duncan Eddy, Esen Yel, Emma Passmore, Niles Egan, Grayson Armour, Dylan M. Asmar, Mykel J. Kochender...  
**Categories**: cs.AI  
**Published**: Tue, 17 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12340  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12340v2.pdf

**Abstract**:
> arXiv:2603.12340v2 Announce Type: replace-cross 
Abstract: Managing announced task completion times is a fundamental control problem in project management. While extensive research exists on estimating task durations and task scheduling, the problem of when and how to update completion times communicated to stakeholders remains understudied. Organizations must balance announcement accuracy against the costs of frequent timeline updates, which can erode stakeholder trust and trigger costly replanning. Despite the prevalence of this problem, current approaches rely on static predictions or ad-hoc policies that fail to account for the sequential nature of announcement management. In this paper, we formulate the task announcement problem as a Partially Observable Markov Decision Process (POMDP...

---

