# arXiv Papers - 2026-03-26

**来源**: arXiv (cs.SD, eess.AS, cs.LG, cs.AI)  
**关键词**: speech, audio, music, voice, sound, Mel, representation, self-supervised  
**今日新论文**: 140 篇

---

## 1. Velocity Potential Neural Field for Efficient Ambisonics Impulse Response Modeling

**Authors**: Yoshiki Masuyama, Francois G. Germain, Gordon Wichern, Chiori Hori, Jonathan Le Roux  
**Categories**: cs.SD  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22589  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22589v1.pdf

**Abstract**:
> arXiv:2603.22589v1 Announce Type: new 
Abstract: First-order Ambisonics (FOA) is a standard spatial audio format based on spherical harmonic decomposition. Its zeroth- and first-order components capture the sound pressure and particle velocity, respectively. Recently, physics-informed neural networks have been applied to the spatial interpolation of FOA signals, regularizing the network outputs based on soft penalty terms derived from physical principles, e.g., the linearized momentum equation. In this paper, we reformulate the task so that the predicted FOA signal automatically satisfies the linearized momentum equation. Our network approximates a scalar function called velocity potential, rather than the FOA signal itself. Then, the FOA signal can be readily recovered through the partial...

---

## 2. The Interspeech 2026 Audio Encoder Capability Challenge for Large Audio Language Models

**Authors**: Heinrich Dinkel, Jiahao Zhou, Guanbo Wang, Yadong Niu, Junbo Zhang, Yufeng Hao, Ying Liu, Ke Li, Wen...  
**Categories**: cs.SD  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22728  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22728v1.pdf

**Abstract**:
> arXiv:2603.22728v1 Announce Type: new 
Abstract: This paper presents the Interspeech 2026 Audio Encoder Capability Challenge, a benchmark specifically designed to evaluate and advance the performance of pre-trained audio encoders as front-end modules for Large Audio Language Models (LALMs). While LALMs have shown remarkable understanding of complex acoustic scenes, their performance depends on the semantic richness of the underlying audio encoder representations. This challenge addresses the integration gap by providing a unified generative evaluation framework, XARES-LLM, which assesses submitted encoders across a diverse suite of downstream classification and generation tasks. By decoupling encoder development from LLM fine-tuning, the challenge establishes a standardized protocol for ge...

---

## 3. ST-GDance++: A Scalable Spatial-Temporal Diffusion for Long-Duration Group Choreography

**Authors**: Jing Xu, Weiqiang Wang, Cunjian Chen, Jun Liu, Qiuhong Ke  
**Categories**: cs.SD  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22316  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22316v1.pdf

**Abstract**:
> arXiv:2603.22316v1 Announce Type: cross 
Abstract: Group dance generation from music requires synchronizing multiple dancers while maintaining spatial coordination, making it highly relevant to applications such as film production, gaming, and animation. Recent group dance generation models have achieved promising generation quality, but they remain difficult to deploy in interactive scenarios due to bidirectional attention dependencies. As the number of dancers and the sequence length increase, the attention computation required for aligning music conditions with motion sequences grows quadratically, leading to reduced efficiency and increased risk of motion collisions. Effectively modeling dense spatial-temporal interactions is therefore essential, yet existing methods often struggle to ...

---

## 4. MSP-Conversation: A Corpus for Naturalistic, Time-Continuous Emotion Recognition

**Authors**: Luz Martinez-Lucas, Pravin Mote, Abinay Reddy Naini, Mohammed Abdelwahab, Carlos Busso  
**Categories**: cs.SD  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22536  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22536v1.pdf

**Abstract**:
> arXiv:2603.22536v1 Announce Type: cross 
Abstract: Affective computing aims to understand and model human emotions for computational systems. Within this field, speech emotion recognition (SER) focuses on predicting emotions conveyed through speech. While early SER systems relied on limited datasets and traditional machine learning models, recent deep learning approaches demand largescale, naturalistic emotional corpora. To address this need, we introduce the MSP-Conversation corpus: a dataset of more than 70 hours of conversational audio with time-continuous emotional annotations and detailed speaker diarizations. The time-continuous annotations capture the dynamic and contextdependent nature of emotional expression. The annotations in the corpus include fine-grained temporal traces of va...

---

## 5. MuQ-Eval: An Open-Source Per-Sample Quality Metric for AI Music Generation Evaluation

**Authors**: Di Zhu, Zixuan Li  
**Categories**: cs.SD  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22677  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22677v1.pdf

**Abstract**:
> arXiv:2603.22677v1 Announce Type: cross 
Abstract: Distributional metrics such as Fr\'echet Audio Distance cannot score individual music clips and correlate poorly with human judgments, while the only per-sample learned metric achieving high human correlation is closed-source. We introduce MUQ-EVAL, an open-source per-sample quality metric for AIgenerated music built by training lightweight prediction heads on frozen MuQ-310M features using MusicEval, a dataset of generated clips from 31 text-to-music systems with expert quality ratings. Our simplest model, frozen features with attention pooling and a two-layer MLP, achieves system-level SRCC = 0.957 and utterance-level SRCC = 0.838 with human mean opinion scores. A systematic ablation over training objectives and adaptation strategies sho...

---

## 6. Structural and Statistical Audio Texture Knowledge Distillation for Acoustic Classification

**Authors**: Jarin Ritu, Amirmohammad Mohammadi, Davelle Carreiro, Alexandra Van Dine, Joshua Peeples  
**Categories**: cs.SD  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2501.01921  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2501.01921v3.pdf

**Abstract**:
> arXiv:2501.01921v3 Announce Type: replace 
Abstract: While knowledge distillation has shown success in various audio tasks, its application to environmental sound classification often overlooks essential low-level audio texture features needed to capture local patterns in complex acoustic environments. To address this gap, the Structural and Statistical Audio Texture Knowledge Distillation (SSATKD) framework is proposed, which combines high-level contextual information with low-level structural and statistical audio textures extracted from intermediate layers. To evaluate its generalizability across diverse acoustic domains, SSATKD is tested on four datasets within the environmental sound classification domain, including two passive sonar datasets (DeepShip and Vessel Type Underwater Acous...

---

## 7. DreamAudio: Customized Text-to-Audio Generation with Diffusion Models

**Authors**: Yi Yuan, Xubo Liu, Haohe Liu, Xiyuan Kang, Zhuo Chen, Yuxuan Wang, Mark D. Plumbley, Wenwu Wang  
**Categories**: cs.SD  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2509.06027  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2509.06027v2.pdf

**Abstract**:
> arXiv:2509.06027v2 Announce Type: replace 
Abstract: With the development of large-scale diffusion-based and language-modeling-based generative models, impressive progress has been achieved in text-to-audio generation. Despite producing high-quality outputs, existing text-to-audio models mainly aim to generate semantically aligned sound and fall short of controlling fine-grained acoustic characteristics of specific sounds. As a result, users who need specific sound content may find it difficult to generate the desired audio clips. In this paper, we present DreamAudio for customized text-to-audio generation (CTTA). Specifically, we introduce a new framework that is designed to enable the model to identify auditory information from user-provided reference concepts for audio generation. Given...

---

## 8. U3-xi: Pushing the Boundaries of Speaker Recognition by Incorporating Uncertainty

**Authors**: Junjie Li, Kong Aik Lee  
**Categories**: cs.SD  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2601.15719  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2601.15719v3.pdf

**Abstract**:
> arXiv:2601.15719v3 Announce Type: replace 
Abstract: An utterance-level speaker embedding is typically obtained by aggregating a sequence of frame-level representations. However, in real-world scenarios, individual frames encode not only speaker-relevant information but also various nuisance factors. As a result, different frames contribute unequally to the final utterance-level speaker representation for Automatic Speaker Verification systems. To address this issue, we propose to estimate the inherent uncertainty of each frame and assign adaptive weights accordingly, where frames with higher uncertainty receive lower attention. Based on this idea, we present U3-xi, a comprehensive framework designed to produce more reliable and interpretable uncertainty estimates for speaker embeddings. S...

---

## 9. Voice Privacy from an Attribute-based Perspective

**Authors**: Mehtab Ur Rahman, Martha Larson, Cristian Tejedor-Garcia  
**Categories**: cs.SD  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20301  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20301v2.pdf

**Abstract**:
> arXiv:2603.20301v2 Announce Type: replace 
Abstract: Voice privacy approaches that preserve the anonymity of speakers modify speech in an attempt to break the link with the true identity of the speaker. Current benchmarks measure speaker protection based on signal-to-signal comparisons. In this paper, we introduce an attribute-based perspective, where we measure privacy protection in terms of comparisons between sets of speaker attributes. First, we analyze privacy impact by calculating speaker uniqueness for ground truth attributes, attributes inferred on the original speech, and attributes inferred on speech protected with standard anonymization. Next, we examine a threat scenario involving only a single utterance per speaker and calculate attack error rates. Overall, we observe that inf...

---

## 10. Do Modern Video-LLMs Need to Listen? A Benchmark Audit and Scalable Remedy

**Authors**: Geewook Kim, Minjoon Seo  
**Categories**: cs.SD  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2509.17901  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2509.17901v3.pdf

**Abstract**:
> arXiv:2509.17901v3 Announce Type: replace-cross 
Abstract: Speech and audio encoders developed over years of community effort are routinely excluded from video understanding pipelines -- not because they fail, but because benchmarks never required listening. We audit 10 video benchmarks and find items largely solvable from visual cues alone: a single-frame probe answers ~76% of AVQA without audio, suggesting poor measurement of audio-visual reasoning. Building on LLaVA-OneVision, we attach a speech/audio encoder and compare five compressor architectures under 25x token reduction (25 Hz to 1 Hz). Across 10 benchmarks -- with and without filtering -- audio yields clear gains on tasks requiring speech comprehension or cross-modal grounding, while vision-centric suites remain largely unaffecte...

---

## 11. Investigating self-supervised representations for audio-visual deepfake detection

**Authors**: Dragos-Alexandru Boldisor, Stefan Smeu, Dan Oneata, Elisabeta Oneata  
**Categories**: cs.SD  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2511.17181  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2511.17181v2.pdf

**Abstract**:
> arXiv:2511.17181v2 Announce Type: replace-cross 
Abstract: Self-supervised representations excel at many vision and speech tasks, but their potential for audio-visual deepfake detection remains underexplored. Unlike prior work that uses these features in isolation or buried within complex architectures, we systematically evaluate them across modalities (audio, video, multimodal) and domains (lip movements, generic visual content). We assess three key dimensions: detection effectiveness, interpretability of encoded information, and cross-modal complementarity. We find that most self-supervised features capture deepfake-relevant information, and that this information is complementary. Moreover, models primarily attend to semantically meaningful regions rather than spurious artifacts (such as...

---

## 12. ASK: Adaptive Self-improving Knowledge Framework for Audio Text Retrieval

**Authors**: Siyuan Fu, Xuchen Guo, Mingjun Liu, Hongxiang Li, Boyin Tan, Gongxi Zhu, Xianwei Zhuang, Jinghan Ru,...  
**Categories**: cs.SD  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2512.19703  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2512.19703v2.pdf

**Abstract**:
> arXiv:2512.19703v2 Announce Type: replace-cross 
Abstract: The dominant paradigm for Audio-Text Retrieval (ATR) relies on dual-encoder architectures optimized via mini-batch contrastive learning. However, restricting optimization to local in-batch samples creates a fundamental limitation we term the Gradient Locality Bottleneck (GLB), which prevents the resolution of acoustic ambiguities and hinders the learning of rare long-tail concepts. While external knowledge injection can break this bottleneck, it often triggers a problem called Representation-Drift Mismatch (RDM), where a static knowledge base becomes misaligned with evolving encoders, degrading guidance into noise. To address these intertwined challenges, we propose the Adaptive Self-improving Knowledge (ASK) framework. ASK breaks ...

---

## 13. When Audio-LLMs Don't Listen: A Cross-Linguistic Study of Modality Arbitration

**Authors**: Jayadev Billa  
**Categories**: cs.SD  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.11488  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.11488v3.pdf

**Abstract**:
> arXiv:2602.11488v3 Announce Type: replace-cross 
Abstract: When audio and text conflict, speech-enabled language models follow text far more often than they do when arbitrating between two conflicting text sources, even under explicit instructions to trust the audio. We introduce ALME (Audio-LLM Modality Evaluation), a dataset of 57,602 controlled audio-text conflict stimuli across eight languages, together with Text Dominance Ratio (TDR), which measures how often a model follows conflicting text when instructed to follow audio. Gemini 2.0 Flash and GPT-4o show TDR 10--26$\times$ higher than a baseline that replaces audio with its transcript under otherwise identical conditions (Gemini 2.0 Flash: 16.6% vs. 1.6%; GPT-4o: 23.2% vs. 0.9%). These results suggest that text dominance reflects no...

---

## 14. Adapting Self-Supervised Speech Representations for Cross-lingual Dysarthria Detection in Parkinson's Disease

**Authors**: Abner Hernandez, Eunjung Yeo, Kwanghee Choi, Chin-Jou Li, Zhengjun Yue, Rohan Kumar Das, Jan Rusz, M...  
**Categories**: cs.SD  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22225  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22225v2.pdf

**Abstract**:
> arXiv:2603.22225v2 Announce Type: replace-cross 
Abstract: The limited availability of dysarthric speech data makes cross-lingual detection an important but challenging problem. A key difficulty is that speech representations often encode language-dependent structure that can confound dysarthria detection. We propose a representation-level language shift (LS) that aligns source-language self-supervised speech representations with the target-language distribution using centroid-based vector adaptation estimated from healthy-control speech. We evaluate the approach on oral DDK recordings from Parkinson's disease speech datasets in Czech, German, and Spanish under both cross-lingual and multilingual settings. LS substantially improves sensitivity and F1 in cross-lingual settings, while yieldi...

---

## 15. Prompt Amplification and Zero-Shot Late Fusion in Audio-Language Models for Speech Emotion Recognition

**Authors**: Saurabh Kataria, Xiao Hu  
**Categories**: eess.AS  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.23057  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.23057v1.pdf

**Abstract**:
> arXiv:2603.23057v1 Announce Type: new 
Abstract: Audio-Language Models (ALMs) are making strides in understanding speech and non-speech audio. However, domain-specialist Foundation Models (FMs) remain the best for closed-ended speech processing tasks such as Speech Emotion Recognition (SER). Using ALMs for Zero-shot SER is a popular choice, but their potential to work with specialists to achieve state-of-the-art (SOTA) performance remains unexplored. We propose ZS-Fuse, a late-fusion method that combines zero-shot emotion estimates from a dual-encoder ALM with specialist FMs. To handle ambiguity in emotions and sensitivity to prompt choice, 1) we use a simple prompt ensemble and 2) suggest a novel technique called prompt amplification, which repeats audio and text queries to discover stron...

---

## 16. Between the Layers Lies the Truth: Uncertainty Estimation in LLMs Using Intra-Layer Local Information Scores

**Authors**: Zvi N. Badash, Yonatan Belinkov, Moti Freiman  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22299  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22299v1.pdf

**Abstract**:
> arXiv:2603.22299v1 Announce Type: new 
Abstract: Large language models (LLMs) are often confidently wrong, making reliable uncertainty estimation (UE) essential. Output-based heuristics are cheap but brittle, while probing internal representations is effective yet high-dimensional and hard to transfer.
  We propose a compact, per-instance UE method that scores cross-layer agreement patterns in internal representations using a single forward pass.
  Across three models, our method matches probing in-distribution, with mean diagonal differences of at most $-1.8$ AUPRC percentage points and $+4.9$ Brier score points. Under cross-dataset transfer, it consistently outperforms probing, achieving off-diagonal gains up to $+2.86$ AUPRC and $+21.02$ Brier points. Under 4-bit weight-only quantizatio...

---

## 17. Latent Semantic Manifolds in Large Language Models

**Authors**: Mohamed A. Mabrok  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22301  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22301v1.pdf

**Abstract**:
> arXiv:2603.22301v1 Announce Type: new 
Abstract: Large Language Models (LLMs) perform internal computations in continuous vector spaces yet produce discrete tokens -- a fundamental mismatch whose geometric consequences remain poorly understood. We develop a mathematical framework that interprets LLM hidden states as points on a latent semantic manifold: a Riemannian submanifold equipped with the Fisher information metric, where tokens correspond to Voronoi regions partitioning the manifold. We define the expressibility gap, a geometric measure of the semantic distortion from vocabulary discretization, and prove two theorems: a rate-distortion lower bound on distortion for any finite vocabulary, and a linear volume scaling law for the expressibility gap via the coarea formula. We validate t...

---

## 18. UniFluids: Unified Neural Operator Learning with Conditional Flow-matching

**Authors**: Haosen Li, Qi Meng, Jiahao Li, Rui Zhang, Ruihua Song, Liang Ma, Zhi-Ming Ma  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22309  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22309v1.pdf

**Abstract**:
> arXiv:2603.22309v1 Announce Type: new 
Abstract: Partial differential equation (PDE) simulation holds extensive significance in scientific research. Currently, the integration of deep neural networks to learn solution operators of PDEs has introduced great potential. In this paper, we present UniFluids, a conditional flow-matching framework that harnesses the scalability of diffusion Transformer to unify learning of solution operators across diverse PDEs with varying dimensionality and physical variables. Unlike the autoregressive PDE foundation models, UniFluids adopts flow-matching to achieve parallel sequence generation, making it the first such approach for unified operator learning. Specifically, the introduction of a unified four-dimensional spatiotemporal representation for the hete...

---

## 19. Enhancing AI-Based Tropical Cyclone Track and Intensity Forecasting via Systematic Bias Correction

**Authors**: Peisong Niu, Haifan Zhang, Yang Zhao, Tian Zhou, Ziqing Ma, Wenqiang Shen, Junping Zhao, Huiling Yua...  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22314  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22314v1.pdf

**Abstract**:
> arXiv:2603.22314v1 Announce Type: new 
Abstract: Tropical cyclones (TCs) pose severe threats to life, infrastructure, and economies in tropical and subtropical regions, underscoring the critical need for accurate and timely forecasts of both track and intensity. Recent advances in AI-based weather forecasting have shown promise in improving TC track forecasts. However, these systems are typically trained on coarse-resolution reanalysis data (e.g., ERA5 at 0.25 degree), which constrains predicted TC positions to a fixed grid and introduces significant discretization errors. Moreover, intensity forecasting remains limited especially for strong TCs by the smoothing effect of coarse meteorological fields and the use of regression losses that bias predictions toward conditional means. To addres...

---

## 20. Geometric Mixture-of-Experts with Curvature-Guided Adaptive Routing for Graph Representation Learning

**Authors**: Haifang Cao, Yu Wang, Timing Li, Xinjie Yao, Pengfei Zhu  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22317  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22317v1.pdf

**Abstract**:
> arXiv:2603.22317v1 Announce Type: new 
Abstract: Graph-structured data typically exhibits complex topological heterogeneity, making it difficult to model accurately within a single Riemannian manifold. While emerging mixed-curvature methods attempt to capture such diversity, they often rely on implicit, task-driven routing that lacks fundamental geometric grounding. To address this challenge, we propose a Geometric Mixture-of-Experts framework (GeoMoE) that adaptively fuses node representations across diverse Riemannian spaces to better accommodate multi-scale topological structures. At its core, GeoMoE leverages Ollivier-Ricci Curvature (ORC) as an intrinsic geometric prior to orchestrate the collaboration of specialized experts. Specifically, we design a graph-aware gating network that a...

---

## 21. Sparsely-Supervised Data Assimilation via Physics-Informed Schr\"odinger Bridge

**Authors**: Dohyun Bu, Chanho Kim, Seokun Choi, Jong-Seok Lee  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22319  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22319v1.pdf

**Abstract**:
> arXiv:2603.22319v1 Announce Type: new 
Abstract: Data assimilation (DA) for systems governed by partial differential equations (PDE) aims to reconstruct full spatiotemporal fields from sparse high-fidelity (HF) observations while respecting physical constraints. While full-grid low-fidelity (LF) simulations provide informative priors in multi-fidelity settings, recovering an HF field consistent with both sparse observations and the governing PDE typically requires per-instance test-time optimization, which becomes a major bottleneck in time-critical applications. To alleviate this, amortized reconstruction using generative models has recently been proposed; however, such approaches rely on full-field HF supervision during training, which is often impractical in real-world settings. From a ...

---

## 22. A Direct Classification Approach for Reliable Wind Ramp Event Forecasting under Severe Class Imbalance

**Authors**: Alejandro Morales-Hern\'andez, Fabrizio De Caroa, Gian Marco Paldino, Pascal Tribel, Alfredo Vaccaro...  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22326  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22326v1.pdf

**Abstract**:
> arXiv:2603.22326v1 Announce Type: new 
Abstract: Decision support systems are essential for maintaining grid stability in low-carbon power systems, such as wind power plants, by providing real-time alerts to control room operators regarding potential events, including Wind Power Ramp Events (WPREs). These early warnings enable the timely initiation of more detailed system stability assessments and preventive actions. However, forecasting these events is challenging due to the inherent class imbalance in WPRE datasets, where ramp events are less frequent (typically less than 15\% of observed events) compared to normal conditions. Ignoring this characteristic undermines the performance of conventional machine learning models, which often favor the majority class. This paper introduces a nove...

---

## 23. Beyond the Mean: Distribution-Aware Loss Functions for Bimodal Regression

**Authors**: Abolfazl Mohammadi-Seif, Carlos Soares, Rita P. Ribeiro, Ricardo Baeza-Yates  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22328  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22328v1.pdf

**Abstract**:
> arXiv:2603.22328v1 Announce Type: new 
Abstract: Despite the strong predictive performance achieved by machine learning models across many application domains, assessing their trustworthiness through reliable estimates of predictive confidence remains a critical challenge. This issue arises in scenarios where the likelihood of error inferred from learned representations follows a bimodal distribution, resulting from the coexistence of confident and ambiguous predictions. Standard regression approaches often struggle to adequately express this predictive uncertainty, as they implicitly assume unimodal Gaussian noise, leading to mean-collapse behavior in such settings. Although Mixture Density Networks (MDNs) can represent different distributions, they suffer from severe optimization instabi...

---

## 24. Trained Persistent Memory for Frozen Decoder-Only LLMs

**Authors**: Hong Jeong  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22329  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22329v1.pdf

**Abstract**:
> arXiv:2603.22329v1 Announce Type: new 
Abstract: Decoder-only language models are stateless: hidden representations are discarded after every forward pass and nothing persists across sessions. Jeong (2026a) showed that trained memory adapters give a frozen encoder-decoder backbone persistent latent-space memory, building on the lateral-memory framework of Jeong (2026b,c). Here we ask whether the same principle transfers to the decoder-only setting, where no cross-attention pathway exists and memory must enter through self-attention alone. We adapt six methods -- prefix, parallel cross-attention, KV extension, Hebbian memory, context-gated branch, and slot-based sparse write -- to a frozen GPT-2, training only a small adapter $\theta_{mem}$. The write rule is shared; only the read injection...

---

## 25. Unveiling the Mechanism of Continuous Representation Full-Waveform Inversion: A Wave Based Neural Tangent Kernel Framework

**Authors**: Ruihua Chen, Yisi Luo, Bangyu Wu, Deyu Meng  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22362  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22362v1.pdf

**Abstract**:
> arXiv:2603.22362v1 Announce Type: new 
Abstract: Full-waveform inversion (FWI) estimates physical parameters in the wave equation from limited measurements and has been widely applied in geophysical exploration, medical imaging, and non-destructive testing. Conventional FWI methods are limited by their notorious sensitivity to the accuracy of the initial models. Recent progress in continuous representation FWI (CR-FWI) demonstrates that representing parameter models with a coordinate-based neural network, such as implicit neural representation (INR), can mitigate the dependence on initial models. However, its underlying mechanism remains unclear, and INR-based FWI shows slower high-frequency convergence. In this work, we investigate the general CR-FWI framework and develop a unified theore...

---

## 26. FAAR: Format-Aware Adaptive Rounding for NVFP4

**Authors**: Hanglin Li, Shuchang Tian, Chen Lin, Zhiyong Zhao, Kun Zhan  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22370  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22370v1.pdf

**Abstract**:
> arXiv:2603.22370v1 Announce Type: new 
Abstract: Deploying large language models (LLMs) on edge devices requires extremely low-bit quantization. Ultra-low precision formats such as NVFP4 offer a promising solution for reducing memory footprint and accelerating computation. However, existing quantization methods typically rely on conventional rounding strategies and fail to account for the non-uniformity of the NVFP4 numerical grid, resulting in suboptimal rounding decisions and amplified quantization errors. To address this, we propose Format-Aware Adaptive Rounding (FAAR), a learnable rounding strategy tailored for the NVFP4 format. Unlike conventional quantization paradigms, FAAR explicitly incorporates the non-uniform NVFP4 grid into the optimization process. By adaptively adjusting rou...

---

## 27. Rethinking Multimodal Fusion for Time Series: Auxiliary Modalities Need Constrained Fusion

**Authors**: Seunghan Lee, Jun Seo, Jaehoon Lee, Sungdong Yoo, Minjae Kim, Tae Yoon Lim, Dongwan Kang, Hwanil Cho...  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22372  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22372v1.pdf

**Abstract**:
> arXiv:2603.22372v1 Announce Type: new 
Abstract: Recent advances in multimodal learning have motivated the integration of auxiliary modalities such as text or vision into time series (TS) forecasting. However, most existing methods provide limited gains, often improving performance only in specific datasets or relying on architecture-specific designs that limit generalization. In this paper, we show that multimodal models with naive fusion strategies (e.g., simple addition or concatenation) often underperform unimodal TS models, which we attribute to the uncontrolled integration of auxiliary modalities which may introduce irrelevant information. Motivated by this observation, we explore various constrained fusion methods designed to control such integration and find that they consistently ...

---

## 28. Symbolic Graph Networks for Robust PDE Discovery from Noisy Sparse Data

**Authors**: Xingyu Chen, Junxiu An, Jun Guo, Yuqian Zhou  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22380  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22380v1.pdf

**Abstract**:
> arXiv:2603.22380v1 Announce Type: new 
Abstract: Data-driven discovery of partial differential equations (PDEs) offers a promising paradigm for uncovering governing physical laws from observational data. However, in practical scenarios, measurements are often contaminated by noise and limited by sparse sampling, which poses significant challenges to existing approaches based on numerical differentiation or integral formulations. In this work, we propose a Symbolic Graph Network (SGN) framework for PDE discovery under noisy and sparse conditions. Instead of relying on local differential approximations, SGN leverages graph message passing to model spatial interactions, providing a non-local representation that is less sensitive to high frequency noise. Based on this representation, the learn...

---

## 29. Neural Structure Embedding for Symbolic Regression via Continuous Structure Search and Coefficient Optimization

**Authors**: Fateme Memar, Tao Zhe, Dongjie Wang  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22429  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22429v1.pdf

**Abstract**:
> arXiv:2603.22429v1 Announce Type: new 
Abstract: Symbolic regression aims to discover human-interpretable equations that explain observational data. However, existing approaches rely heavily on discrete structure search (e.g., genetic programming), which often leads to high computational cost, unstable performance, and limited scalability to large equation spaces. To address these challenges, we propose SRCO, a unified embedding-driven framework for symbolic regression that transforms symbolic structures into a continuous, optimizable representation space. The framework consists of three key components: (1) structure embedding: we first generate a large pool of exploratory equations using traditional symbolic regression algorithms and train a Transformer model to compress symbolic structur...

---

## 30. Adversarial Vulnerabilities in Neural Operator Digital Twins: Gradient-Free Attacks on Nuclear Thermal-Hydraulic Surrogates

**Authors**: Samrendra Roy, Kazuma Kobayashi, Souvik Chakraborty,  Rizwan-uddin, Syed Bahauddin Alam  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22525  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22525v1.pdf

**Abstract**:
> arXiv:2603.22525v1 Announce Type: new 
Abstract: Operator learning models are rapidly emerging as the predictive core of digital twins for nuclear and energy systems, promising real-time field reconstruction from sparse sensor measurements. Yet their robustness to adversarial perturbations remains uncharacterized, a critical gap for deployment in safety-critical systems. Here we show that neural operators are acutely vulnerable to extremely sparse (fewer than 1% of inputs), physically plausible perturbations that exploit their sensitivity to boundary conditions. Using gradient-free differential evolution across four operator architectures, we demonstrate that minimal modifications trigger catastrophic prediction failures, increasing relative $L_2$ error from $\sim$1.5% (validated accuracy)...

---

## 31. A Foundation Model for Instruction-Conditioned In-Context Time Series Tasks

**Authors**: Anish Saha, Konstantin Shmakov  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22586  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22586v1.pdf

**Abstract**:
> arXiv:2603.22586v1 Announce Type: new 
Abstract: In-context learning (ICL) allows a model to adapt at inference time by conditioning on examples rather than updating parameters. Existing time-series foundation models use implicit positional context, retrieval, or task-specific objectives, but rarely explicit instruction-conditioned demonstrations. We present a foundation model for instruction-conditioned in-context time-series tasks based on a quantile-regression T5 encoder-decoder. Historical examples and queries are encoded with a structured tokenization scheme that marks target series, covariates, context, and task-specific future information. A hierarchical Transformer with per-example encoding, example-level fusion, and cross-example attention conditions decoding on demonstration pair...

---

## 32. Transfer learning via interpolating structures

**Authors**: T. A. Dardeno, A. J. Hughes, L. A. Bull, R. S. Mills, N. Dervilis, K. Worden  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22621  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22621v1.pdf

**Abstract**:
> arXiv:2603.22621v1 Announce Type: new 
Abstract: Despite recent advances in population-based structural health monitoring (PBSHM), knowledge transfer between highly-disparate structures (i.e., heterogeneous populations) remains a challenge. The current work proposes that heterogeneous transfer may be accomplished via intermediate structures that bridge the gap in information between the structures of interest. A key aspect of the technique is the idea that by varying parameters such as material properties and geometry, one structure can be continuously morphed into another. The approach is demonstrated via a case study involving the parameterisation of (and transfer between) simulated heterogeneous bridge designs (Case 1). Transfer between simplified physical representations of a 'bridge' ...

---

## 33. Generalizing Dynamics Modeling More Easily from Representation Perspective

**Authors**: Yiming Wang, Zhengnan Zhang, Genghe Zhang, Jiawen Dan, Changchun Li, Chenlong Hu, Chris Nugent, Jun ...  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22655  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22655v1.pdf

**Abstract**:
> arXiv:2603.22655v1 Announce Type: new 
Abstract: Learning system dynamics from observations is a critical problem in many applications over various real-world complex systems, e.g., climate, ecology, and fluid systems. Recently, neural dynamics modeling method have become a prevalent solution that embeds the object's observations into a latent space before learning dynamics using neural methods such as neural Ordinary Differential Equations (ODE). Existing dynamics modeling methods induce a specific model for each observation of different complex systems, resulting in poor generalization across systems. Inspired by the great success of pre-trained models, we conduct a generalized Pre-trained Dynamics EncoDER (PDEDER) which can embed the original state observations into a latent space where...

---

## 34. Bounding Box Anomaly Scoring for simple and efficient Out-of-Distribution detection

**Authors**: Mohamed Bahi Yahiaoui, Geoffrey Daniel, Lo\"ic Giraldi, J\'er\'emie Bruyelle, Julyan Arbel  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22660  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22660v1.pdf

**Abstract**:
> arXiv:2603.22660v1 Announce Type: new 
Abstract: Out-of-distribution (OOD) detection aims to identify inputs that differ from the training distribution in order to reduce unreliable predictions by deep neural networks. Among post-hoc feature-space approaches, OOD detection is commonly performed by approximating the in-distribution support in the representation space of a pretrained network. Existing methods often reflect a trade-off between compact parametric models, such as Mahalanobis-based scores, and more flexible but reference-based methods, such as k-nearest neighbors. Bounding-box abstraction provides an attractive intermediate perspective by representing in-distribution support through compact axis-aligned summaries of hidden activations. In this paper, we introduce Bounding Box An...

---

## 35. Vision-based Deep Learning Analysis of Unordered Biomedical Tabular Datasets via Optimal Spatial Cartography

**Authors**: Sakib Mostafa, Tarik Massoud, Maximilian Diehn, Lei Xing, Md Tauhidul Islam  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22675  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22675v1.pdf

**Abstract**:
> arXiv:2603.22675v1 Announce Type: new 
Abstract: Tabular data are central to biomedical research, from liquid biopsy and bulk and single-cell transcriptomics to electronic health records and phenotypic profiling. Unlike images or sequences, however, tabular datasets lack intrinsic spatial organization: features are treated as unordered dimensions, and their relationships must be inferred implicitly by the model. This limits the ability of vision architectures to exploit local structure and higher-order feature interactions in non-spatial biomedical data. Here we introduce Dynamic Feature Mapping (Dynomap), an end-to-end deep learning framework that learns a task-optimized spatial topology of features directly from data. Dynomap jointly optimizes feature placement and prediction through a f...

---

## 36. Behavioral Heterogeneity as Quantum-Inspired Representation

**Authors**: Mohammad Elayan, Wissam Kontar  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22729  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22729v1.pdf

**Abstract**:
> arXiv:2603.22729v1 Announce Type: new 
Abstract: Driver heterogeneity is often reduced to labels or discrete regimes, compressing what is inherently dynamic into static categories. We introduce quantum-inspired representation that models each driver as an evolving latent state, presented as a density matrix with structured mathematical properties. Behavioral observations are embedded via non-linear Random Fourier Features, while state evolution blends temporal persistence of behavior with context-dependent profile activation. We evaluate our approach on empirical driving data, Third Generation Simulation Data (TGSIM), showing how driving profiles are extracted and analyzed.

---

## 37. Caterpillar of Thoughts: The Optimal Test-Time Algorithm for Large Language Models

**Authors**: Amir Azarmehr, Soheil Behnezhad, Alma Ghafari  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22784  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22784v1.pdf

**Abstract**:
> arXiv:2603.22784v1 Announce Type: new 
Abstract: Large language models (LLMs) can often produce substantially better outputs when allowed to use additional test-time computation, such as sampling, chain of thought, backtracking, or revising partial solutions. Despite the growing empirical success of such techniques, there is limited theoretical understanding of how inference time computation should be structured, or what constitutes an optimal use of a fixed computation budget.
  We model test-time computation as an algorithm interacting with a Markov chain: at any point, the algorithm may resume generation from any previously observed state. That is, unlike standard Markov chains where the states are drawn passively, we allow the algorithm to backtrack to any previously observed state of ...

---

## 38. Universal and efficient graph neural networks with dynamic attention for machine learning interatomic potentials

**Authors**: Shuyu Bi, Zhede Zhao, Qiangchao Sun, Tao Hu, Xionggang Lu, Hongwei Cheng  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22810  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22810v1.pdf

**Abstract**:
> arXiv:2603.22810v1 Announce Type: new 
Abstract: The core of molecular dynamics simulation fundamentally lies in the interatomic potential. Traditional empirical potentials lack accuracy, while first-principles methods are computationally prohibitive. Machine learning interatomic potentials (MLIPs) promise near-quantum accuracy at linear cost, but existing models still face challenges in efficiency and stability. We presents Machine Learning Advances Neural Network (MLANet), an efficient and robust graph neural network framework. MLANet introduces a dual-path dynamic attention mechanism for geometry-aware message passing and a multi-perspective pooling strategy to construct comprehensive system representations. This design enables highly accurate modeling of atomic environments while achie...

---

## 39. Conditionally Identifiable Latent Representation for Multivariate Time Series with Structural Dynamics

**Authors**: Minkey Chang, Jae-Young Kim  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22886  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22886v1.pdf

**Abstract**:
> arXiv:2603.22886v1 Announce Type: new 
Abstract: We propose the Identifiable Variational Dynamic Factor Model (iVDFM), which learns latent factors from multivariate time series with identifiability guarantees. By applying iVAE-style conditioning to the innovation process driving the dynamics rather than to the latent states, we show that factors are identifiable up to permutation and component-wise affine (or monotone invertible) transformations. Linear diagonal dynamics preserve this identifiability and admit scalable computation via companion-matrix and Krylov methods. We demonstrate improved factor recovery on synthetic data, stable intervention accuracy on synthetic SCMs, and competitive probabilistic forecasting on real-world benchmarks.

---

## 40. SynForceNet: A Force-Driven Global-Local Latent Representation Framework for Lithium-Ion Battery Fault Diagnosis

**Authors**: Rongxiu Chen, Yuting Su  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.23265  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.23265v1.pdf

**Abstract**:
> arXiv:2603.23265v1 Announce Type: new 
Abstract: Online safety fault diagnosis is essential for lithium-ion batteries in electric vehicles(EVs), particularly under complex and rare safety-critical conditions in real-world operation. In this work, we develop an online battery fault diagnosis network based on a deep anomaly detection framework combining kernel one-class classification and minimum-volume estimation. Mechanical constraints and spike-timing-dependent plasticity(STDP)-based dynamic representations are introduced to improve complex fault characterization and enable a more compact normal-state boundary. The proposed method is validated using 8.6 million valid data points collected from 20 EVs. Compared with several advanced baseline methods, it achieves average improvements of 7.5...

---

## 41. Central Dogma Transformer III: Interpretable AI Across DNA, RNA, and Protein

**Authors**: Nobuyuki Ota  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.23361  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.23361v1.pdf

**Abstract**:
> arXiv:2603.23361v1 Announce Type: new 
Abstract: Biological AI models increasingly predict complex cellular responses, yet their learned representations remain disconnected from the molecular processes they aim to capture. We present CDT-III, which extends mechanism-oriented AI across the full central dogma: DNA, RNA, and protein. Its two-stage Virtual Cell Embedder architecture mirrors the spatial compartmentalization of the cell: VCE-N models transcription in the nucleus and VCE-C models translation in the cytosol. On five held-out genes, CDT-III achieves per-gene RNA r=0.843 and protein r=0.969. Adding protein prediction improves RNA performance (r=0.804 to 0.843), demonstrating that downstream tasks regularize upstream representations. Protein supervision sharpens DNA-level interpretab...

---

## 42. Estimating Flow Velocity and Vehicle Angle-of-Attack from Non-invasive Piezoelectric Structural Measurements Using Deep Learning

**Authors**: Chandler B. Smith, S. Hales Swift, Andrew Steyer, Ihab El-Kady  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.23496  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.23496v1.pdf

**Abstract**:
> arXiv:2603.23496v1 Announce Type: new 
Abstract: Accurate estimation of aerodynamic state variables such as freestream velocity and angle of attack (AoA) is important for aerodynamic load prediction, flight control, and model validation. This work presents a non-intrusive method for estimating vehicle velocity and AoA from structural vibration measurements rather than direct flow instrumentation such as pitot tubes. A dense array of piezoelectric sensors mounted on the interior skin of an aeroshell capture vibrations induced by turbulent boundary layer pressure fluctuations, and a convolutional neural network (CNN) is trained to invert these structural responses to recover velocity and AoA.
  Proof-of-concept is demonstrated through controlled experiments in Sandia's hypersonic wind tunnel...

---

## 43. Demystifying Low-Rank Knowledge Distillation in Large Language Models: Convergence, Generalization, and Information-Theoretic Guarantees

**Authors**: Alberlucia Rafael Soarez, Daniel Kim, Mariana Costa, Alejandro Torre  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22355  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22355v1.pdf

**Abstract**:
> arXiv:2603.22355v1 Announce Type: cross 
Abstract: Knowledge distillation has emerged as a powerful technique for compressing large language models (LLMs) into efficient, deployable architectures while preserving their advanced capabilities. Recent advances in low-rank knowledge distillation, particularly methods like Low-Rank Clone (LRC), have demonstrated remarkable empirical success, achieving comparable performance to full-parameter distillation with significantly reduced training data and computational overhead. However, the theoretical foundations underlying these methods remain poorly understood. In this paper, we establish a rigorous theoretical framework for low-rank knowledge distillation in language models. We prove that under mild assumptions, low-rank projection preserves the ...

---

## 44. Q-AGNN: Quantum-Enhanced Attentive Graph Neural Network for Intrusion Detection

**Authors**: Devashish Chaudhary, Sutharshan Rajasegarar, Shiva Raj Pokhrel  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22365  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22365v1.pdf

**Abstract**:
> arXiv:2603.22365v1 Announce Type: cross 
Abstract: With the rapid growth of interconnected devices, accurately detecting malicious activities in network traffic has become increasingly challenging. Most existing deep learning-based intrusion detection systems treat network flows as independent instances, thereby failing to exploit the relational dependencies inherent in network communications. To address this limitation, we propose Q-AGNN, a Quantum-Enhanced Attentive Graph Neural Network for intrusion detection, where network flows are modeled as nodes and edges represent similarity relationships. Q-AGNN leverages parameterized quantum circuits (PQCs) to encode multi-hop neighborhood information into a high-dimensional latent space, inducing a bounded quantum feature map that implements a...

---

## 45. Modeling Quantum Federated Autoencoder for Anomaly Detection in IoT Networks

**Authors**: Devashish Chaudhary, Sutharshan Rajasegarar, Shiva Raj Pokhrel  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22366  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22366v1.pdf

**Abstract**:
> arXiv:2603.22366v1 Announce Type: cross 
Abstract: We propose a Quantum Federated Autoencoder for Anomaly Detection, a framework that leverages quantum federated learning for efficient, secure, and distributed processing in IoT networks. By harnessing quantum autoencoders for high-dimensional feature representation and federated learning for decentralized model training, the approach transforms localized learning on edge devices without requiring transmission of raw data, thereby preserving privacy and minimizing communication overhead. The model leverages quantum advantage in pattern recognition to enhance detection sensitivity, particularly in complex and dynamic IoT network traffic. Experiments on a real-world IoT dataset show that the proposed method delivers anomaly detection accuracy...

---

## 46. SynLeaF: A Dual-Stage Multimodal Fusion Framework for Synthetic Lethality Prediction Across Pan- and Single-Cancer Contexts

**Authors**: Zheming Xing, Siyuan Zhou, Ruinan Wang, Rui Han, Shiming Zhang, Shiqu Chen, Yurui Huang, Jiahao Ma, ...  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22369  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22369v1.pdf

**Abstract**:
> arXiv:2603.22369v1 Announce Type: cross 
Abstract: Accurate prediction of synthetic lethality (SL) is important for guiding the development of cancer drugs and therapies. SL prediction faces significant challenges in the effective fusion of heterogeneous multi-source data. Existing multimodal methods often suffer from "modality laziness" due to disparate convergence speeds, which hinders the exploitation of complementary information. This is also one reason why most existing SL prediction models cannot perform well on both pan-cancer and single-cancer SL pair prediction. In this study, we propose SynLeaF, a dual-stage multimodal fusion framework for SL prediction across pan- and single-cancer contexts. The framework employs a VAE-based cross-encoder with a product of experts mechanism to f...

---

## 47. Improving LLM Predictions via Inter-Layer Structural Encoders

**Authors**: Tom Ulanovski (Tel Aviv University), Eyal Blyachman (Tel Aviv University), Maya Bechler-Speicher (Me...  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22665  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22665v1.pdf

**Abstract**:
> arXiv:2603.22665v1 Announce Type: cross 
Abstract: The standard practice in Large Language Models (LLMs) is to base predictions on the final-layer token representations. Recent studies, however, show that intermediate layers encode substantial information, which may contain more task-relevant features than the final-layer representations alone. Importantly, it was shown that for different tasks, different layers may be optimal. In this work we introduce Inter-Layer Structural Encoders (ILSE), a powerful structural approach to learn one effective representation from the LLM's internal layer representations all together. Central to ILSE is Cayley-Encoder, a mathematically grounded geometric encoder that leverages expander Cayley graphs for efficient inter-layer information propagation. We ev...

---

## 48. Reconstruction-Guided Slot Curriculum: Addressing Object Over-Fragmentation in Video Object-Centric Learning

**Authors**: WonJun Moon, Hyun Seok Seong, Jae-Pil Heo  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22758  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22758v1.pdf

**Abstract**:
> arXiv:2603.22758v1 Announce Type: cross 
Abstract: Video Object-Centric Learning seeks to decompose raw videos into a small set of object slots, but existing slot-attention models often suffer from severe over-fragmentation. This is because the model is implicitly encouraged to occupy all slots to minimize the reconstruction objective, thereby representing a single object with multiple redundant slots. We tackle this limitation with a reconstruction-guided slot curriculum (SlotCurri). Training starts with only a few coarse slots and progressively allocates new slots where reconstruction error remains high, thus expanding capacity only where it is needed and preventing fragmentation from the outset. Yet, during slot expansion, meaningful sub-parts can emerge only if coarse-level semantics a...

---

## 49. Dynamical Systems Theory Behind a Hierarchical Reasoning Model

**Authors**: Vasiliy A. Es'kin, Mikhail E. Smorkalov  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22871  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22871v1.pdf

**Abstract**:
> arXiv:2603.22871v1 Announce Type: cross 
Abstract: Current large language models (LLMs) primarily rely on linear sequence generation and massive parameter counts, yet they severely struggle with complex algorithmic reasoning. While recent reasoning architectures, such as the Hierarchical Reasoning Model (HRM) and Tiny Recursive Model (TRM), demonstrate that compact recursive networks can tackle these tasks, their training dynamics often lack rigorous mathematical guarantees, leading to instability and representational collapse. We propose the Contraction Mapping Model (CMM), a novel architecture that reformulates discrete recursive reasoning into continuous Neural Ordinary and Stochastic Differential Equations (NODEs/NSDEs). By explicitly enforcing the convergence of the latent phase point...

---

## 50. Dual-Teacher Distillation with Subnetwork Rectification for Black-Box Domain Adaptation

**Authors**: Zhe Zhang, Jing Li, Wanli Xue, Xu Cheng, Jianhua Zhang, Qinghua Hu, Shengyong Chen  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22908  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22908v1.pdf

**Abstract**:
> arXiv:2603.22908v1 Announce Type: cross 
Abstract: Assuming that neither source data nor the source model is accessible, black box domain adaptation represents a highly practical yet extremely challenging setting, as transferable information is restricted to the predictions of the black box source model, which can only be queried using target samples. Existing approaches attempt to extract transferable knowledge through pseudo label refinement or by leveraging external vision language models (ViLs), but they often suffer from noisy supervision or insufficient utilization of the semantic priors provided by ViLs, which ultimately hinder adaptation performance. To overcome these limitations, we propose a dual teacher distillation with subnetwork rectification (DDSR) model that jointly exploit...

---

## 51. FixationFormer: Direct Utilization of Expert Gaze Trajectories for Chest X-Ray Classification

**Authors**: Daniel Beckmann, Benjamin Risse  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22939  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22939v1.pdf

**Abstract**:
> arXiv:2603.22939v1 Announce Type: cross 
Abstract: Expert eye movements provide a rich, passive source of domain knowledge in radiology, offering a powerful cue for integrating diagnostic reasoning into computer-aided analysis. However, direct integration into CNN-based systems, which historically have dominated the medical image analysis domain, is challenging: gaze recordings are sequential, temporally dense yet spatially sparse, noisy, and variable across experts. As a consequence, most existing image-based models utilize reduced representations such as heatmaps. In contrast, gaze naturally aligns with transformer architectures, as both are sequential in nature and rely on attention to highlight relevant input regions. In this work, we introduce FixationFormer, a transformer-based archi...

---

## 52. Privacy-Preserving EHR Data Transformation via Geometric Operators: A Human-AI Co-Design Technical Report

**Authors**: Maolin Wang, Beining Bao, Gan Yuan, Hongyu Chen, Bingkun Zhao, Baoshuo Kan, Jiming Xu, Qi Shi, Yingg...  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22954  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22954v1.pdf

**Abstract**:
> arXiv:2603.22954v1 Announce Type: cross 
Abstract: Electronic health records (EHRs) and other real-world clinical data are essential for clinical research, medical artificial intelligence, and life science, but their sharing is severely limited by privacy, governance, and interoperability constraints. These barriers create persistent data silos that hinder multi-center studies, large-scale model development, and broader biomedical discovery. Existing privacy-preserving approaches, including multi-party computation and related cryptographic techniques, provide strong protection but often introduce substantial computational overhead, reducing the efficiency of large-scale machine learning and foundation-model training. In addition, many such methods make data usable for restricted computatio...

---

## 53. High-Resolution Tensor-Network Fourier Methods for Exponentially Compressed Non-Gaussian Aggregate Distributions

**Authors**: Juan Jos\'e Rodr\'iguez-Aldavero, Juan Jos\'e Garc\'ia-Ripoll  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.23106  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.23106v1.pdf

**Abstract**:
> arXiv:2603.23106v1 Announce Type: cross 
Abstract: Characteristic functions of weighted sums of independent random variables exhibit low-rank structure in the quantized tensor train (QTT) representation, also known as matrix product states (MPS), enabling up to exponential compression of their fully non-Gaussian probability distributions. Under variable independence, the global characteristic function factorizes into local terms. Its low-rank QTT structure arises from intrinsic spectral smoothness in continuous models, or from spectral energy concentration as the number of components $D$ grows in discrete models. We demonstrate this on weighted sums of Bernoulli and lognormal random variables. In the former, despite an adversarial, incompressible small-$D$ regime, the characteristic functi...

---

## 54. Conformal Cross-Modal Active Learning

**Authors**: Huy Hoang Nguyen, C\'edric Jung, Shirin Salehi, Tobias Gl\"uck, Anke Schmeink, Andreas Kugi  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.23159  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.23159v1.pdf

**Abstract**:
> arXiv:2603.23159v1 Announce Type: cross 
Abstract: Foundation models for vision have transformed visual recognition with powerful pretrained representations and strong zero-shot capabilities, yet their potential for data-efficient learning remains largely untapped. Active Learning (AL) aims to minimize annotation costs by strategically selecting the most informative samples for labeling, but existing methods largely overlook the rich multimodal knowledge embedded in modern vision-language models (VLMs). We introduce Conformal Cross-Modal Acquisition (CCMA), a novel AL framework that bridges vision and language modalities through a teacher-student architecture. CCMA employs a pretrained VLM as a teacher to provide semantically grounded uncertainty estimates, conformally calibrated to guide ...

---

## 55. PhysSkin: Real-Time and Generalizable Physics-Based Animation via Self-Supervised Neural Skinning

**Authors**: Yuanhang Lei, Tao Cheng, Xingxuan Li, Boming Zhao, Siyuan Huang, Ruizhen Hu, Peter Yichen Chen, Huju...  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.23194  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.23194v1.pdf

**Abstract**:
> arXiv:2603.23194v1 Announce Type: cross 
Abstract: Achieving real-time physics-based animation that generalizes across diverse 3D shapes and discretizations remains a fundamental challenge. We introduce PhysSkin, a physics-informed framework that addresses this challenge. In the spirit of Linear Blend Skinning, we learn continuous skinning fields as basis functions lifting motion subspace coordinates to full-space deformation, with subspace defined by handle transformations. To generate mesh-free, discretization-agnostic, and physically consistent skinning fields that generalize well across diverse 3D shapes, PhysSkin employs a new neural skinning fields autoencoder which consists of a transformer-based encoder and a cross-attention decoder. Furthermore, we also develop a novel physics-inf...

---

## 56. Not All Tokens Are Created Equal: Query-Efficient Jailbreak Fuzzing for LLMs

**Authors**: Wenyu Chen, Xiangtao Meng, Chuanchao Zang, Li Wang, Xinyu Gao, Jianing Wang, Peng Zhan, Zheng Li, Sh...  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.23269  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.23269v1.pdf

**Abstract**:
> arXiv:2603.23269v1 Announce Type: cross 
Abstract: Large Language Models(LLMs) are widely deployed, yet are vulnerable to jailbreak prompts that elicit policy-violating outputs. Although prior studies have uncovered these risks, they typically treat all tokens as equally important during prompt mutation, overlooking the varying contributions of individual tokens to triggering model refusals. Consequently, these attacks introduce substantial redundant searching under query-constrained scenarios, reducing attack efficiency and hindering comprehensive vulnerability assessment. In this work, we conduct a token-level analysis of refusal behavior and observe that token contributions are highly skewed rather than uniform. Moreover, we find strong cross-model consistency in refusal tendencies, ena...

---

## 57. ARGENT: Adaptive Hierarchical Image-Text Representations

**Authors**: Chuong Huynh, Hossein Souri, Abhinav Kumar, Vitali Petsiuk, Deen Dayal Mohan, Suren Kumar  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.23311  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.23311v1.pdf

**Abstract**:
> arXiv:2603.23311v1 Announce Type: cross 
Abstract: Large-scale Vision-Language Models (VLMs) such as CLIP learn powerful semantic representations but operate in Euclidean space, which fails to capture the inherent hierarchical structure of visual and linguistic concepts. Hyperbolic geometry, with its exponential volume growth, offers a principled alternative for embedding such hierarchies with low distortion. However, existing hyperbolic VLMs use entailment losses that are unstable: as parent embeddings contract toward the origin, their entailment cones widen toward a half-space, causing catastrophic cone collapse that destroys the intended hierarchy. Additionally, hierarchical evaluation of these models remains unreliable, being largely retrieval-based and correlation-based metrics and pr...

---

## 58. Contrastive Metric Learning for Point Cloud Segmentation in Highly Granular Detectors

**Authors**: Max Marriott-Clarke, Lazar Novakovic, Elizabeth Ratzer, Robert J. Bainbridge, Loukas Gouskos, Benedi...  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.23356  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.23356v1.pdf

**Abstract**:
> arXiv:2603.23356v1 Announce Type: cross 
Abstract: We propose a novel clustering approach for point-cloud segmentation based on supervised contrastive metric learning (CML). Rather than predicting cluster assignments or object-centric variables, the method learns a latent representation in which points belonging to the same object are embedded nearby while unrelated points are separated. Clusters are then reconstructed using a density-based readout in the learned metric space, decoupling representation learning from cluster formation and enabling flexible inference. The approach is evaluated on simulated data from a highly granular calorimeter, where the task is to separate highly overlapping particle showers represented as sets of calorimeter hits. A direct comparison with object condensa...

---

## 59. CSTS: A Canonical Security Telemetry Substrate for AI-Native Cyber Detection

**Authors**: Abdul Rahman  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.23459  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.23459v1.pdf

**Abstract**:
> arXiv:2603.23459v1 Announce Type: cross 
Abstract: AI-driven cybersecurity systems often fail under cross-environment deployment due to fragmented, event-centric telemetry representations. We introduce the Canonical Security Telemetry Substrate (CSTS), an entity-relational abstraction that enforces identity persistence, typed relationships, and temporal state invariants. Across heterogeneous environments, CSTS improves cross-topology transfer for identity-centric detection and prevents collapse under schema perturbation. For zero-day detection, CSTS isolates semantic orientation instability as a modeling, not schema, phenomenon, clarifying layered portability requirements.

---

## 60. VTAM: Video-Tactile-Action Models for Complex Physical Interaction Beyond VLAs

**Authors**: Haoran Yuan, Weigang Yi, Zhenyu Zhang, Wendi Chen, Yuchen Mo, Jiashi Yin, Xinzhuo Li, Xiangyu Zeng, ...  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.23481  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.23481v1.pdf

**Abstract**:
> arXiv:2603.23481v1 Announce Type: cross 
Abstract: Video-Action Models (VAMs) have emerged as a promising framework for embodied intelligence, learning implicit world dynamics from raw video streams to produce temporally consistent action predictions. Although such models demonstrate strong performance on long-horizon tasks through visual reasoning, they remain limited in contact-rich scenarios where critical interaction states are only partially observable from vision alone. In particular, fine-grained force modulation and contact transitions are not reliably encoded in visual tokens, leading to unstable or imprecise behaviors. To bridge this gap, we introduce the Video-Tactile Action Model (VTAM), a multimodal world modeling framework that incorporates tactile perception as a complementa...

---

## 61. VISion On Request: Enhanced VLLM efficiency with sparse, dynamically selected, vision-language interactions

**Authors**: Adrian Bulat, Alberto Baldrati, Ioannis Maniadis Metaxas, Yassine Ouali, Georgios Tzimiropoulos  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.23495  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.23495v1.pdf

**Abstract**:
> arXiv:2603.23495v1 Announce Type: cross 
Abstract: Existing approaches for improving the efficiency of Large Vision-Language Models (LVLMs) are largely based on the concept of visual token reduction. This approach, however, creates an information bottleneck that impairs performance, especially on challenging tasks that require fine-grained understanding and reasoning. In this work, we challenge this paradigm by introducing VISion On Request (VISOR), a method that reduces inference cost without discarding visual information. Instead of compressing the image, VISOR improves efficiency by sparsifying the interaction between image and text tokens. Specifically, the language model attends to the full set of high-resolution visual tokens through a small, strategically placed set of attention lay...

---

## 62. Knee or ROC

**Authors**: Veronica Wendt, Jacob Steiner, Byunggu Yu, Caleb Kelly, Justin Kim  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2401.07390  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2401.07390v3.pdf

**Abstract**:
> arXiv:2401.07390v3 Announce Type: replace 
Abstract: Self-attention transformers have demonstrated accuracy for image classification with smaller data sets. However, a limitation is that tests to-date are based upon single class image detection with known representation of image populations. For instances where the input image classes may be greater than one and test sets that lack full information on representation of image populations, accuracy calculations must adapt. The Receiver Operating Characteristic (ROC) accuracy threshold can address the instances of multiclass input images. However, this approach is unsuitable in instances where image population representation is unknown. We then consider calculating accuracy using the knee method to determine threshold values on an ad-hoc basi...

---

## 63. Addressing Large Action Spaces in 3D Floorplanning via Spatial Generalization

**Authors**: Fin Amin, Nirjhor Rouf, Tse-Han Pan, Sounak Dutta, Md Kamal Ibn Shafi, Paul D. Franzon  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2406.10538  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2406.10538v3.pdf

**Abstract**:
> arXiv:2406.10538v3 Announce Type: replace 
Abstract: Many recent machine learning approaches to floorplanning represent placement decisions using discrete canvas coordinates, which creates scalability bottlenecks as the action space grows. In this work, we study the effect of learning a continuous action representation for 3D floorplanning. By reasoning in a continuous placement space and discretizing only at inference time, our method decouples the output structure from the canvas resolution, which makes learning and inference more tractable in large design spaces. A central idea in our approach is \textit{$L$-action similarity}: actions that are close in the placement space often produce similar returns. This smoothness induces a useful structural bias that allows the model to generalize...

---

## 64. DART-Eval: A Comprehensive DNA Language Model Evaluation Benchmark on Regulatory DNA

**Authors**: Aman Patel, Arpita Singhal, Austin Wang, Anusri Pampari, Maya Kasowski, Anshul Kundaje  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2412.05430  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2412.05430v3.pdf

**Abstract**:
> arXiv:2412.05430v3 Announce Type: replace 
Abstract: Recent advances in self-supervised models for natural language, vision, and protein sequences have inspired the development of large genomic DNA language models (DNALMs). These models aim to learn generalizable representations of diverse DNA elements, potentially enabling various genomic prediction, interpretation and design tasks. Despite their potential, existing benchmarks do not adequately assess the capabilities of DNALMs on key downstream applications involving an important class of non-coding DNA elements critical for regulating gene activity. In this study, we introduce DART-Eval, a suite of representative benchmarks specifically focused on regulatory DNA to evaluate model performance across zero-shot, probed, and fine-tuned scen...

---

## 65. Paired Wasserstein Autoencoders for Conditional Sampling

**Authors**: Moritz Piening, Matthias Chung  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2412.07586  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2412.07586v2.pdf

**Abstract**:
> arXiv:2412.07586v2 Announce Type: replace 
Abstract: Generative autoencoders learn compact latent representations of data distributions through jointly optimized encoder--decoder pairs. In particular, Wasserstein autoencoders (WAEs) minimize a relaxed optimal transport (OT) objective, where similarity between distributions is measured through a cost-minimizing joint distribution (OT coupling). Beyond distribution matching, neural OT methods aim to learn mappings between two data distributions induced by an OT coupling. Building on the formulation of the WAE loss, we derive a novel loss that enables sampling from OT-type couplings via two paired WAEs with shared latent space. The resulting fully parametrized joint distribution yields (i) learned cost-optimal transport maps between the two d...

---

## 66. GAIA: A Foundation Model for Operational Atmospheric Dynamics

**Authors**: Ata Akbari Asanjan, Olivia Alexander, Tom Berg, Stephen Peng, Jad Makki, Clara Zhang, Matt Yang, Dis...  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2505.18179  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2505.18179v3.pdf

**Abstract**:
> arXiv:2505.18179v3 Announce Type: replace 
Abstract: We introduce GAIA (Geospatial Artificial Intelligence for Atmospheres), a hybrid self-supervised geospatial foundation model that fuses Masked Autoencoders (MAE) with self-distillation with no labels (DINO) to generate semantically rich representations from global geostationary satellite imagery. Pre-trained on 15 years of globally-merged infrared observations (2001-2015), GAIA learns disentangled representations that capture atmospheric dynamics rather than trivial diurnal patterns, as evidenced by distributed principal component structure and temporal coherence analysis. We demonstrate robust reconstruction capabilities across varying data availability (30-95% masking), achieving superior gap-filling performance on real missing data pa...

---

## 67. Learning The Minimum Action Distance

**Authors**: Lorenzo Steccanella, Joshua B. Evans, \"Ozg\"ur \c{S}im\c{s}ek, Anders Jonsson  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2506.09276  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2506.09276v3.pdf

**Abstract**:
> arXiv:2506.09276v3 Announce Type: replace 
Abstract: This paper presents a state representation framework for Markov decision processes (MDPs) that can be learned solely from state trajectories, requiring neither reward signals nor the actions executed by the agent. We propose learning the minimum action distance (MAD), defined as the minimum number of actions required to transition between states, as a fundamental metric that captures the underlying structure of an environment. MAD naturally enables critical downstream tasks such as goal-conditioned reinforcement learning and reward shaping by providing a dense, geometrically meaningful measure of progress. Our self-supervised learning approach constructs an embedding space where the distances between embedded state pairs correspond to th...

---

## 68. UniCA: Unified Covariate Adaptation for Time Series Foundation Model

**Authors**: Lu Han, Yu Liu, Lan Li, Qiwen Deng, Jian Jiang, Yinbo Sun, Zhe Yu, Binfeng Wang, Xingyu Lu, Lintao M...  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2506.22039  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2506.22039v2.pdf

**Abstract**:
> arXiv:2506.22039v2 Announce Type: replace 
Abstract: Time Series Foundation Models (TSFMs) have achieved remarkable success through large-scale pretraining. However, their design primarily targets real-valued series, limiting their ability to handle general forecasting tasks involving diverse and often heterogeneous covariates -- such as categorical variables and multimodal data (e.g., images, text) -- which are typically task-specific and difficult to leverage during pretraining. To address this gap, we propose Unified Covariate Adaptation (UniCA), a framework to bridge TSFMs with general covariate-aware forecasting. UniCA first performs covariate homogenization to transform heterogeneous covariates into high-level homogeneous series representations and then fuses them via a unified atten...

---

## 69. FEDONet : Fourier-Embedded DeepONet for Spectrally Accurate Operator Learning

**Authors**: Arth Sojitra, Mrigank Dhingra, Omer San  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2509.12344  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2509.12344v4.pdf

**Abstract**:
> arXiv:2509.12344v4 Announce Type: replace 
Abstract: Deep Operator Networks (DeepONets) have recently emerged as powerful data-driven frameworks for learning nonlinear operators, particularly suited for approximating solutions to partial differential equations. Despite their promising capabilities, the standard implementation of DeepONets, which typically employs fully connected linear layers in the trunk network, can encounter limitations in capturing complex spatial structures inherent to various PDEs. To address this limitation, we use Fourier-Embedded trunk networks within the DeepONet architecture, leveraging random Fourier features to enrich spatial representation capabilities. The Fourier-Embedded DeepONet (FEDONet) demonstrates superior performance compared to the traditional DeepO...

---

## 70. Counterfactual Identifiability via Dynamic Optimal Transport

**Authors**: Fabio De Sousa Ribeiro, Ainkaran Santhirasekaram, Ben Glocker  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.08294  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.08294v2.pdf

**Abstract**:
> arXiv:2510.08294v2 Announce Type: replace 
Abstract: We address the open question of counterfactual identification for high-dimensional multivariate outcomes from observational data. Pearl (2000) argues that counterfactuals must be identifiable (i.e., recoverable from the observed data distribution) to justify causal claims. A recent line of work on counterfactual inference shows promising results but lacks identification, undermining the causal validity of its estimates. To address this, we establish a foundation for multivariate counterfactual identification using continuous-time flows, including non-Markovian settings under standard criteria. We characterise the conditions under which flow matching yields a unique, monotone, and rank-preserving counterfactual transport map with tools fr...

---

## 71. CSI-4CAST: A Hybrid Deep Learning Model for CSI Prediction with Comprehensive Robustness and Generalization Testing

**Authors**: Sikai Cheng, Reza Zandehshahvar, Haoruo Zhao, Daniel A. Garcia-Ulloa, Alejandro Villena-Rodriguez, C...  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.12996  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.12996v2.pdf

**Abstract**:
> arXiv:2510.12996v2 Announce Type: replace 
Abstract: Channel state information (CSI) prediction is a promising strategy for ensuring reliable and efficient operation of massive multiple-input multiple-output (mMIMO) systems by providing timely downlink (DL) CSI. While deep learning-based methods have advanced beyond conventional model-driven and statistical approaches, they remain limited in robustness to practical non-Gaussian noise, generalization across diverse channel conditions, and computational efficiency. This paper introduces CSI-4CAST, a hybrid deep learning architecture that integrates 4 key components, i.e., Convolutional neural network residuals, Adaptive correction layers, ShuffleNet blocks, and Transformers, to efficiently capture both local and long-range dependencies in CS...

---

## 72. GUIrilla: A Scalable Framework for Automated Desktop UI Exploration

**Authors**: Sofiya Garkot, Maksym Shamrai, Ivan Synytsia, Mariya Hirna  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.16051  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.16051v2.pdf

**Abstract**:
> arXiv:2510.16051v2 Announce Type: replace 
Abstract: The performance and generalization of foundation models for interactive systems critically depend on the availability of large-scale, realistic training data. While recent advances in large language models (LLMs) have improved GUI understanding, progress in desktop automation remains constrained by the scarcity of high-quality, publicly available desktop interaction data, particularly for macOS. We introduce GUIRILLA, a scalable data crawling framework for automated exploration of desktop GUIs. GUIRILLA is not an autonomous agent; instead, it systematically collects realistic interaction traces and accessibility metadata intended to support the training, evaluation, and stabilization of downstream foundation models and GUI agents. The fr...

---

## 73. Parameter-Free Clustering via Self-Supervised Consensus Maximization (Extended Version)

**Authors**: Lijun Zhang, Suyuan Liu, Siwei Wang, Shengju Yu, Xueling Zhu, Miaomiao Li, Xinwang Liu  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2511.09211  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2511.09211v3.pdf

**Abstract**:
> arXiv:2511.09211v3 Announce Type: replace 
Abstract: Clustering is a fundamental task in unsupervised learning, but most existing methods heavily rely on hyperparameters such as the number of clusters or other sensitive settings, limiting their applicability in real-world scenarios. To address this long-standing challenge, we propose a novel and fully parameter-free clustering framework via Self-supervised Consensus Maximization, named SCMax. Our framework performs hierarchical agglomerative clustering and cluster evaluation in a single, integrated process. At each step of agglomeration, it creates a new, structure-aware data representation through a self-supervised learning task guided by the current clustering structure. We then introduce a nearest neighbor consensus score, which measure...

---

## 74. Data-Efficient and Robust Trajectory Generation through Pathlet Dictionary Learning

**Authors**: Yuanbo Tang, Yan Tang, Zixuan Zhang, Zihui Zhao, Yang Li  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2511.16105  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2511.16105v2.pdf

**Abstract**:
> arXiv:2511.16105v2 Announce Type: replace 
Abstract: Trajectory generation has recently drawn growing interest in privacy-preserving urban mobility studies and location-based service applications. Although many studies have used deep learning or generative AI methods to model trajectories and have achieved promising results, the robustness and interpretability of such models are largely unexplored. This limits the application of trajectory generation algorithms on noisy real-world data and their trustworthiness in downstream tasks. To address this issue, we exploit the regular structure in urban trajectories and propose a deep generative model based on the pathlet representation, which encode trajectories with binary vectors associated with a learned dictionary of trajectory segments. Spec...

---

## 75. Latent Diffusion Inversion Requires Understanding the Latent Space

**Authors**: Mingxing Rao, Bowen Qu, Daniel Moyer  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2511.20592  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2511.20592v2.pdf

**Abstract**:
> arXiv:2511.20592v2 Announce Type: replace 
Abstract: The recovery of training data from generative models ("model inversion") has been extensively studied for diffusion models in the data domain as a memorization/overfitting phenomenon. Latent diffusion models (LDMs), which operate on the latent codes from encoder/decoder pairs, have been robust to prior inversion methods. In this work we describe two key findings: (1) the diffusion model exhibits non-uniform memorization across latent codes, tending to overfit samples located in high-distortion regions of the decoder pullback metric; (2) even within a single latent code, memorization contributions are unequal across representation dimensions. Our proposed method to ranks latent dimensions by their contribution to the decoder pullback metr...

---

## 76. Representational Homomorphism Predicts and Improves Compositional Generalization In Transformer Language Model

**Authors**: Zhiyu An, Wan Du  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2601.18858  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2601.18858v2.pdf

**Abstract**:
> arXiv:2601.18858v2 Announce Type: replace 
Abstract: Compositional generalization-the ability to interpret novel combinations of familiar components-remains a persistent challenge for neural networks. Behavioral evaluations reveal \emph{when} models fail but offer limited insight into \emph{why} failures arise at the representational level. We introduce \textit{Homomorphism Error} (HE), a structural metric that measures the inconsistency between a set of established rules for which words combine to form new meaning (linguistic syntax) and model's learned rules for which hidden states combine to form new states (semantic syntax). We formulate this inconsistency as deviations from approximate homomorphisms between the linguistic expression algebra and a model's hidden-state space. We designe...

---

## 77. FlyPrompt: Brain-Inspired Random-Expanded Routing with Temporal-Ensemble Experts for General Continual Learning

**Authors**: Hongwei Yan, Guanglong Sun, Kanglei Zhou, Qian Li, Liyuan Wang, Yi Zhong  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.01976  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.01976v3.pdf

**Abstract**:
> arXiv:2602.01976v3 Announce Type: replace 
Abstract: General continual learning (GCL) challenges intelligent systems to learn from single-pass, non-stationary data streams without clear task boundaries. While recent advances in continual parameter-efficient tuning (PET) of pretrained models show promise, they typically rely on multiple training epochs and explicit task cues, limiting their effectiveness in GCL scenarios. Moreover, existing methods often lack targeted design and fail to address two fundamental challenges in continual PET: how to allocate expert parameters to evolving data distributions, and how to improve their representational capacity under limited supervision. Inspired by the fruit fly's hierarchical memory system characterized by sparse expansion and modular ensembles, ...

---

## 78. Refine Now, Query Fast: A Decoupled Refinement Paradigm for Implicit Neural Fields

**Authors**: Tianyu Xiong, Skylar Wurster, Han-Wei Shen  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.15155  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.15155v3.pdf

**Abstract**:
> arXiv:2602.15155v3 Announce Type: replace 
Abstract: Implicit Neural Representations (INRs) have emerged as promising surrogates for large 3D scientific simulations due to their ability to continuously model spatial and conditional fields, yet they face a critical fidelity-speed dilemma: deep MLPs suffer from high inference cost, while efficient embedding-based models lack sufficient expressiveness. To resolve this, we propose the Decoupled Representation Refinement (DRR) architectural paradigm. DRR leverages a deep refiner network, alongside non-parametric transformations, in a one-time offline process to encode rich representations into a compact and efficient embedding structure. This approach decouples slow neural networks with high representational capacity from the fast inference pat...

---

## 79. When Sensors Fail: Temporal Sequence Models for Robust PPO under Sensor Drift

**Authors**: Kevin Vogt-Lowell, Theodoros Tsiligkaridis, Rodney Lafuente-Mercado, Surabhi Ghatti, Shanghua Gao, M...  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.04648  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.04648v2.pdf

**Abstract**:
> arXiv:2603.04648v2 Announce Type: replace 
Abstract: Real-world reinforcement learning systems must operate under distributional drift in their observation streams, yet most policy architectures implicitly assume fully observed and noise-free states. We study robustness of Proximal Policy Optimization (PPO) under temporally persistent sensor failures that induce partial observability and representation shift. To respond to this drift, we augment PPO with temporal sequence models, including Transformers and State Space Models (SSMs), to enable policies to infer missing information from history and maintain performance. Under a stochastic sensor failure process, we prove a high-probability bound on infinite-horizon reward degradation that quantifies how robustness depends on policy smoothnes...

---

## 80. Multi-Station WiFi CSI Sensing Framework Robust to Station-wise Feature Missingness and Limited Labeled Data

**Authors**: Keita Kayano, Takayuki Nishio, Daiki Yoda, Yuta Hirai, Tomoko Adachi  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11858  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11858v2.pdf

**Abstract**:
> arXiv:2603.11858v2 Announce Type: replace 
Abstract: We propose a WiFi Channel State Information (CSI) sensing framework for multi-station deployments that addresses two fundamental challenges in practical CSI sensing: station-wise feature missingness and limited labeled data. Feature missingness is commonly handled by resampling unevenly spaced CSI measurements or by reconstructing missing samples, while label scarcity is mitigated by data augmentation or self-supervised representation learning. However, these techniques are typically developed in isolation and do not jointly address long-term, structured station unavailability together with label scarcity. To bridge this gap, we explicitly incorporate station unavailability into both representation learning and downstream model training....

---

## 81. PRISM: Demystifying Retention and Interaction in Mid-Training

**Authors**: Bharat Runwal, Ashish Agrawal, Anurag Roy, Rameswar Panda  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.17074  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.17074v3.pdf

**Abstract**:
> arXiv:2603.17074v3 Announce Type: replace 
Abstract: We present PRISM, a comprehensive empirical study of mid-training design choices for large language models. Through controlled experiments across seven base models spanning four families (Granite, LLaMA, Mistral, Nemotron-H), two architecture types (dense Transformer and attention-Mamba hybrid), and scales from 3B to 24B parameters, we show that mid-training on approximately 27B high-quality tokens yields consistent gains of +15 to +40 points on math, +5 to +12 points on code, and +6 to +13 points on science benchmarks while preserving general performance. The full PRISM to RL pipeline improves macro-average across six reasoning benchmarks from under 12 to 29-42 (a 3-4x improvement), whereas RL applied directly to most of the base models...

---

## 82. MKA: Memory-Keyed Attention for Efficient Long-Context Reasoning

**Authors**: Dong Liu, Yanxuan Yu, Ben Lengerich, Ying Nian Wu  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20586  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20586v2.pdf

**Abstract**:
> arXiv:2603.20586v2 Announce Type: replace 
Abstract: As long-context language modeling becomes increasingly important, the cost of maintaining and attending to large Key/Value (KV) caches grows rapidly, becoming a major bottleneck in both training and inference. While prior works such as Multi-Query Attention (MQA) and Multi-Latent Attention (MLA) reduce memory by sharing or compressing KV features, they often trade off representation quality or incur runtime overhead. We propose Memory-Keyed Attention (MKA), a hierarchical attention mechanism that integrates multi-level KV caches (local, session, and long-term) and learns to route attention across them dynamically. We further introduce Route-Fused MKA (FastMKA), a broadcast-routed variant that fuses memory sources before attention computa...

---

## 83. An Accurate and Interpretable Framework for Trustworthy Process Monitoring

**Authors**: Hao Wang, Zhiyu Wang, Yunlong Niu, Zhaoran Liu, Haozhe Li, Yilin Liao, Yuxin Huang, Xinggao Liu  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2302.10426  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2302.10426v3.pdf

**Abstract**:
> arXiv:2302.10426v3 Announce Type: replace-cross 
Abstract: Trustworthy process monitoring seeks to build an accurate and interpretable monitoring framework, which is critical for ensuring the safety of energy conversion plant (ECP) that operates under extreme working conditions such as high pressure and temperature. Contemporary self-attentive models, however, fall short in this domain for two main reasons. First, they rely on step-wise correlations that fail to involve physically meaningful semantics in ECP logs, resulting in suboptimal accuracy and interpretability. Second, attention matrices are frequently cluttered with spurious correlations that obscure physically meaningful ones, further impeding effective interpretation. To overcome these issues, we propose AttentionMixer, a framewo...

---

## 84. HD-Bind: Encoding of Molecular Structure with Low Precision, Hyperdimensional Binary Representations

**Authors**: Derek Jones, Jonathan E. Allen, Xiaohua Zhang, Behnam Khaleghi, Jaeyoung Kang, Weihong Xu, Niema Mos...  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2303.15604  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2303.15604v2.pdf

**Abstract**:
> arXiv:2303.15604v2 Announce Type: replace-cross 
Abstract: Publicly available collections of drug-like molecules have grown to comprise 10s of billions of possibilities in recent history due to advances in chemical synthesis. Traditional methods for identifying "hit" molecules from a large collection of potential drug-like candidates have relied on biophysical theory to compute approximations to the Gibbs free energy of the binding interaction between the drug to its protein target. A major drawback of the approaches is that they require exceptional computing capabilities to consider for even relatively small collections of molecules. Hyperdimensional Computing (HDC) is a recently proposed learning paradigm that is able to leverage low-precision binary vector arithmetic to build efficient ...

---

## 85. Learning dynamically inspired bases for Koopman and transfer operator approximation

**Authors**: Gary Froyland, Kevin K\"uhl  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2505.05085  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2505.05085v3.pdf

**Abstract**:
> arXiv:2505.05085v3 Announce Type: replace-cross 
Abstract: Transfer and Koopman operator methods offer a framework for representing complex, nonlinear dynamical systems via linear transformations, enabling a deeper understanding of the underlying dynamics. The spectra of these operators provide important insights into system predictability and emergent behaviour, although efficiently estimating them from data can be challenging. We approach this issue through the lens of general operator and representational learning, in which we approximate these linear operators using efficient finite-dimensional representations. Specifically, we machine-learn orthonormal basis functions that are dynamically tailored to the system. This learned basis provides a particularly accurate approximation of the ...

---

## 86. PRISM: Video Dataset Condensation with Progressive Refinement and Insertion for Sparse Motion

**Authors**: Jaehyun Choi, Jiwan Hur, Gyojin Han, Jaemyung Yu, Junmo Kim  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2505.22564  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2505.22564v2.pdf

**Abstract**:
> arXiv:2505.22564v2 Announce Type: replace-cross 
Abstract: Video dataset condensation aims to reduce the immense computational cost of video processing. However, it faces a fundamental challenge regarding the inseparable interdependence between spatial appearance and temporal dynamics. Prior work follows a static/dynamic disentanglement paradigm where videos are decomposed into static content and auxiliary motion signals. This multi-stage approach often misrepresents the intrinsic coupling of real-world actions. We introduce Progressive Refinement and Insertion for Sparse Motion (PRISM), a holistic approach that treats the video as a unified and fully coupled spatiotemporal structure from the outset. To maximize representational efficiency, PRISM addresses the inherent temporal redundancy ...

---

## 87. Towards a general-purpose foundation model for fMRI analysis

**Authors**: Cheng Wang, Yu Jiang, Zhihao Peng, Chenxin Li, Changbae Bang, Lin Zhao, Wanyi Fu, Jinglei Lv, Jorge ...  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2506.11167  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2506.11167v2.pdf

**Abstract**:
> arXiv:2506.11167v2 Announce Type: replace-cross 
Abstract: Functional MRI (fMRI) is crucial for studying brain function and diagnosing neurological disorders. However, existing analysis methods suffer from reproducibility and transferability challenges due to complex preprocessing pipelines and task-specific model designs. In this work, we introduce NeuroSTORM (Neuroimaging Foundation Model with Spatial-Temporal Optimized Representation Modeling) that learns generalizable representations directly from 4D fMRI volumes and enables efficient transfer to diverse downstream applications. Specifically, NeuroSTORM is pre-trained on 28.65 million fMRI frames from over 50,000 subjects, spanning multiple centers and ages 5 to 100. It combines an efficient spatiotemporal modeling design and lightweig...

---

## 88. MoEGCL: Mixture of Ego-Graphs Contrastive Representation Learning for Multi-View Clustering

**Authors**: Jian Zhu, Xin Zou, Jun Sun, Cheng Luo, Lei Liu, Lingfang Zeng, Ning Zhang, Bian Wu, Chang Tang, Liro...  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2511.05876  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2511.05876v5.pdf

**Abstract**:
> arXiv:2511.05876v5 Announce Type: replace-cross 
Abstract: In recent years, the advancement of Graph Neural Networks (GNNs) has significantly propelled progress in Multi-View Clustering (MVC). However, existing methods face the problem of coarse-grained graph fusion. Specifically, current approaches typically generate a separate graph structure for each view and then perform weighted fusion of graph structures at the view level, which is a relatively rough strategy. To address this limitation, we present a novel Mixture of Ego-Graphs Contrastive Representation Learning (MoEGCL). It mainly consists of two modules. In particular, we propose an innovative Mixture of Ego-Graphs Fusion (MoEGF), which constructs ego graphs and utilizes a Mixture-of-Experts network to implement fine-grained fusio...

---

## 89. MOON2.0: Dynamic Modality-balanced Multimodal Representation Learning for E-commerce Product Understanding

**Authors**: Zhanheng Nie, Chenghan Fu, Daoze Zhang, Junxian Wu, Wanxian Guan, Pengjie Wang, Jian Xu, Bo Zheng  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2511.12449  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2511.12449v2.pdf

**Abstract**:
> arXiv:2511.12449v2 Announce Type: replace-cross 
Abstract: Recent Multimodal Large Language Models (MLLMs) have significantly advanced e-commerce product understanding. However, they still face three challenges: (i) the modality imbalance induced by modality mixed training; (ii) underutilization of the intrinsic alignment relationships among visual and textual information within a product; and (iii) limited handling of noise in e-commerce multimodal data. To address these, we propose MOON2.0, a dynamic modality-balanced MultimOdal representation learning framework for e-commerce prOduct uNderstanding. It comprises: (1) a Modality-driven Mixture-of-Experts (MoE) that adaptively processes input samples by their modality composition, enabling Multimodal Joint Learning to mitigate the modality...

---

## 90. Cross-Sensory Brain Passage Retrieval: Scaling Beyond Visual to Audio

**Authors**: Niall McGuire, Yashar Moshfeghi  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2601.14001  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2601.14001v2.pdf

**Abstract**:
> arXiv:2601.14001v2 Announce Type: replace-cross 
Abstract: Query formulation from internal information needs remains fundamentally challenging across all Information Retrieval paradigms due to cognitive complexity and physical impairments. Brain Passage Retrieval (BPR) addresses this by directly mapping EEG signals to passage representations without intermediate text translation. However, existing BPR research exclusively uses visual stimuli, leaving critical questions unanswered: Can auditory EEG enable effective retrieval for voice-based interfaces and visually impaired users? Can training on combined EEG datasets from different sensory modalities improve performance despite severe data scarcity? We present the first systematic investigation of auditory EEG for BPR and evaluate cross-sen...

---

## 91. 1S-DAug: One-Shot Data Augmentation for Robust Few-Shot Generalization

**Authors**: Yunwei Bai, Ying Kiat Tan, Yao Shu, Tsuhan Chen  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.00114  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.00114v3.pdf

**Abstract**:
> arXiv:2602.00114v3 Announce Type: replace-cross 
Abstract: Few-shot learning (FSL) challenges model generalization to novel classes based on just a few shots of labeled examples, a testbed where traditional test-time augmentations fail to be effective. We introduce 1S-DAug, a one-shot generative augmentation operator that synthesizes diverse yet faithful variants from just one example image at test time. 1S-DAug couples traditional geometric perturbations with controlled noise injection and a denoising diffusion process conditioned on the original image. The generated images are then encoded and aggregated, alongside the original image, into a combined representation for more robust FSL predictions. Integrated as a training-free model-agnostic plugin, 1S-DAug consistently improves FSL acro...

---

## 92. Catalogue Grounded Multimodal Attribution for Museum Video under Resource and Regulatory Constraints

**Authors**: Minsak Nanang, Adrian Hilton, Armin Mustafa  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11147  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11147v2.pdf

**Abstract**:
> arXiv:2603.11147v2 Announce Type: replace-cross 
Abstract: Audiovisual (AV) archives in museums and galleries are growing rapidly, but much of this material remains effectively locked away because it lacks consistent, searchable metadata. Existing method for archiving requires extensive manual effort. We address this by automating the most labour intensive part of the workflow: catalogue style metadata curation for in gallery video, grounded in an existing collection database. Concretely, we propose catalogue-grounded multimodal attribution for museum AV content using an open, locally deployable video language model. We design a multi pass pipeline that (i) summarises artworks in a video, (ii) generates catalogue style descriptions and genre labels, and (iii) attempts to attribute title an...

---

## 93. Foundation-Model Surrogates Enable Data-Efficient Active Learning for Materials Discovery

**Authors**: Jeffrey Hu, Rongzhi Dong, Ying Feng, Ming Hu, Jianjun Hu  
**Categories**: cs.LG  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12567  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12567v3.pdf

**Abstract**:
> arXiv:2603.12567v3 Announce Type: replace-cross 
Abstract: Active learning (AL) has emerged as a powerful paradigm for accelerating materials discovery by iteratively steering experiments toward promising candidates, reducing the number of costly synthesis-and-characterization cycles needed to identify optimal materials. However, current AL relies predominantly on Gaussian Process (GP) and Random Forest (RF) surrogates, which suffer from complementary limitations: GP underfits complex composition-property landscapes due to rigid kernel assumptions, while RF produces unreliable heuristic uncertainty estimates in small-data regimes. This small-data challenge is pervasive in materials science, making reliable surrogate modeling extremely difficult with models trained from scratch on each new ...

---

## 94. Memory Bear AI Memory Science Engine for Multimodal Affective Intelligence: A Technical Report

**Authors**: Deliang Wen, Ke Sun, Yu Wang  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22306  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22306v1.pdf

**Abstract**:
> arXiv:2603.22306v1 Announce Type: new 
Abstract: Affective judgment in real interaction is rarely a purely local prediction problem. Emotional meaning often depends on prior trajectory, accumulated context, and multimodal evidence that may be weak, noisy, or incomplete at the current moment. Although multimodal emotion recognition (MER) has improved the integration of text, speech, and visual signals, many existing systems remain optimized for short-range inference and provide limited support for persistent affective memory, long-horizon dependency modeling, and robust interpretation under imperfect input.
  This technical report presents the Memory Bear AI Memory Science Engine, a memory-centered framework for multimodal affective intelligence. Instead of treating emotion as a transient o...

---

## 95. Dynamic Fusion-Aware Graph Convolutional Neural Network for Multimodal Emotion Recognition in Conversations

**Authors**: Tao Meng, Weilun Tang, Yuntao Shou, Yilong Tan, Jun Zhou, Wei Ai, Keqin Li  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22345  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22345v1.pdf

**Abstract**:
> arXiv:2603.22345v1 Announce Type: new 
Abstract: Multimodal emotion recognition in conversations (MERC) aims to identify and understand the emotions expressed by speakers during utterance interaction from multiple modalities (e.g., text, audio, images, etc.). Existing studies have shown that GCN can improve the performance of MERC by modeling dependencies between speakers. However, existing methods usually use fixed parameters to process multimodal features for different emotion types, ignoring the dynamics of fusion between different modalities, which forces the model to balance performance between multiple emotion categories, thus limiting the model's performance on some specific emotions. To this end, we propose a dynamic fusion-aware graph convolutional neural network (DF-GCN) for robu...

---

## 96. Session Risk Memory (SRM): Temporal Authorization for Deterministic Pre-Execution Safety Gates

**Authors**: Florin Adrian Chitan  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22350  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22350v1.pdf

**Abstract**:
> arXiv:2603.22350v1 Announce Type: new 
Abstract: Deterministic pre-execution safety gates evaluate whether individual agent actions are compatible with their assigned roles. While effective at per-action authorization, these systems are structurally blind to distributed attacks that decompose harmful intent across multiple individually-compliant steps. This paper introduces Session Risk Memory (SRM), a lightweight deterministic module that extends stateless execution gates with trajectory-level authorization. SRM maintains a compact semantic centroid representing the evolving behavioral profile of an agent session and accumulates a risk signal through exponential moving average over baseline-subtracted gate outputs. It operates on the same semantic vector representation as the underlying g...

---

## 97. HyFI: Hyperbolic Feature Interpolation for Brain-Vision Alignment

**Authors**: Sangmin Jo, Wootaek Jeong, Da-Woon Heo, Yoohwan Hwang, Heung-Il Suk  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22721  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22721v1.pdf

**Abstract**:
> arXiv:2603.22721v1 Announce Type: new 
Abstract: Recent progress in artificial intelligence has encouraged numerous attempts to understand and decode human visual system from brain signals. These prior works typically align neural activity independently with semantic and perceptual features extracted from images using pre-trained vision models. However, they fail to account for two key challenges: (1) the modality gap arising from the natural difference in the information level of representation between brain signals and images, and (2) the fact that semantic and perceptual features are highly entangled within neural activity. To address these issues, we utilize hyperbolic space, which is well-suited for considering differences in the amount of information and has the geometric property th...

---

## 98. CLiGNet: Clinical Label-Interaction Graph Network for Medical Specialty Classification from Clinical Transcriptions

**Authors**: Pronob Kumar Barman, Pronoy Kumar Barman  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22752  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22752v1.pdf

**Abstract**:
> arXiv:2603.22752v1 Announce Type: new 
Abstract: Automated classification of clinical transcriptions into medical specialties is essential for routing, coding, and clinical decision support, yet prior work on the widely used MTSamples benchmark suffers from severe data leakage caused by applying SMOTE oversampling before train test splitting. We first document this methodological flaw and establish a leakage free benchmark across 40 medical specialties (4966 records), revealing that the true task difficulty is substantially higher than previously reported.
  We then introduce CLiGNet (Clinical Label Interaction Graph Network), a neural architecture that combines a Bio ClinicalBERT text encoder with a two layer Graph Convolutional Network operating on a specialty label graph constructed fro...

---

## 99. AgriPestDatabase-v1.0: A Structured Insect Dataset for Training Agricultural Large Language Model

**Authors**: Yagizhan Bilal Durak, Ahsan Ul Islam, Shahidul Islam, Ashley Morgan-Olvera, Iftekhar Ibne Basith, Sy...  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22777  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22777v1.pdf

**Abstract**:
> arXiv:2603.22777v1 Announce Type: new 
Abstract: Agricultural pest management increasingly relies on timely and accurate access to expert knowledge, yet high quality labeled data and continuous expert support remain limited, particularly for farmers operating in rural regions with unstable/no internet connectivity. At the same time, the rapid growth of AI and LLMs has created new opportunities to deliver practical decision support tools directly to end users in agriculture through compact and deployable systems. This work addresses (i) generating a structured insect information dataset, and (ii) adapting a lightweight LLM model ($\leq$ 7B) by fine tuning it for edge device uses in agricultural pest management. The textual data collection was done by reviewing and collecting information fro...

---

## 100. Reliable Classroom AI via Neuro-Symbolic Multimodal Reasoning

**Authors**: Sina Bagheri Nezhad  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22793  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22793v1.pdf

**Abstract**:
> arXiv:2603.22793v1 Announce Type: new 
Abstract: Classroom AI is rapidly expanding from low-level perception toward higher-level judgments about engagement, confusion, collaboration, and instructional quality. Yet classrooms are among the hardest real-world settings for multimodal vision: they are multi-party, noisy, privacy-sensitive, pedagogically diverse, and often multilingual. In this paper, we argue that classroom AI should be treated as a critical domain, where raw predictive accuracy is insufficient unless predictions are accompanied by verifiable evidence, calibrated uncertainty, and explicit deployment guardrails. We introduce NSCR, a neuro-symbolic framework that decomposes classroom analytics into four layers: perceptual grounding, symbolic abstraction, executable reasoning, an...

---

## 101. Continuous Optimization for Satisfiability Modulo Theories on Linear Real Arithmetic

**Authors**: Yunuo Cen, Daniel Ebler, Xuanyao Fong  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22877  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22877v1.pdf

**Abstract**:
> arXiv:2603.22877v1 Announce Type: new 
Abstract: Efficient solutions for satisfiability modulo theories (SMT) are integral in industrial applications such as hardware verification and design automation. Existing approaches are predominantly based on conflict-driven clause learning, which is structurally difficult to parallelize and therefore scales poorly. In this work, we introduce FourierSMT as a scalable and highly parallelizable continuous-variable optimization framework for SMT. We generalize the Walsh-Fourier expansion (WFE), called extended WFE (xWFE), from the Boolean domain to a mixed Boolean-real domain, which allows the use of gradient methods for SMT. This addresses the challenge of finding satisfying variable assignments to high-arity constraints by local updates of discrete v...

---

## 102. Separating Diagnosis from Control: Auditable Policy Adaptation in Agent-Based Simulations with LLM-Based Diagnostics

**Authors**: Shaoxin Zhong, Yuchen Su, Michael Witbrock  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22904  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22904v1.pdf

**Abstract**:
> arXiv:2603.22904v1 Announce Type: new 
Abstract: Mitigating elderly loneliness requires policy interventions that achieve both adaptability and auditability. Existing methods struggle to reconcile these objectives: traditional agent-based models suffer from static rigidity, while direct large language model (LLM) controllers lack essential traceability. This work proposes a three-layer framework that separates diagnosis from control to achieve both properties simultaneously. LLMs operate strictly as diagnostic instruments that assess population state and generate structured risk evaluations, while deterministic formulas with explicit bounds translate these assessments into traceable parameter updates. This separation ensures that every policy decision can be attributed to inspectable rules...

---

## 103. ProGRank: Probe-Gradient Reranking to Defend Dense-Retriever RAG from Corpus Poisoning

**Authors**: Xiangyu Yin, Yi Qi, Chih-hong Cheng  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22934  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22934v1.pdf

**Abstract**:
> arXiv:2603.22934v1 Announce Type: new 
Abstract: Retrieval-Augmented Generation (RAG) improves the reliability of large language model applications by grounding generation in retrieved evidence, but it also introduces a new attack surface: corpus poisoning. In this setting, an adversary injects or edits passages so that they are ranked into the Top-$K$ results for target queries and then affect downstream generation. Existing defences against corpus poisoning often rely on content filtering, auxiliary models, or generator-side reasoning, which can make deployment more difficult. We propose ProGRank, a post hoc, training-free retriever-side defence for dense-retriever RAG. ProGRank stress-tests each query--passage pair under mild randomized perturbations and extracts probe gradients from a ...

---

## 104. PersonalQ: Select, Quantize, and Serve Personalized Diffusion Models for Efficient Inference

**Authors**: Qirui Wang, Qi Guo, Yiding Sun, Junkai Yang, Dongxu Zhang, Shanmin Pang, Qing Guo  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22943  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22943v1.pdf

**Abstract**:
> arXiv:2603.22943v1 Announce Type: new 
Abstract: Personalized text-to-image generation lets users fine-tune diffusion models into repositories of concept-specific checkpoints, but serving these repositories efficiently is difficult for two reasons: natural-language requests are often ambiguous and can be misrouted to visually similar checkpoints, and standard post-training quantization can distort the fragile representations that encode personalized concepts. We present PersonalQ, a unified framework that connects checkpoint selection and quantization through a shared signal -- the checkpoint's trigger token. Check-in performs intent-aligned selection by combining intent-aware hybrid retrieval with LLM-based reranking over checkpoint context and asks a brief clarification question only whe...

---

## 105. JFTA-Bench: Evaluate LLM's Ability of Tracking and Analyzing Malfunctions Using Fault Trees

**Authors**: Yuhui Wang, Zhixiong Yang, Ming Zhang, Shihan Dou, Zhiheng Xi, Enyu Zhou, Senjie Jin, Yujiong Shen, ...  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22978  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22978v1.pdf

**Abstract**:
> arXiv:2603.22978v1 Announce Type: new 
Abstract: In the maintenance of complex systems, fault trees are used to locate problems and provide targeted solutions. To enable fault trees stored as images to be directly processed by large language models, which can assist in tracking and analyzing malfunctions, we propose a novel textual representation of fault trees. Building on it, we construct a benchmark for multi-turn dialogue systems that emphasizes robust interaction in complex environments, evaluating a model's ability to assist in malfunction localization, which contains $3130$ entries and $40.75$ turns per entry on average. We train an end-to-end model to generate vague information to reflect user behavior and introduce long-range rollback and recovery procedures to simulate user error...

---

## 106. SAiW: Source-Attributable Invisible Watermarking for Proactive Deepfake Defense

**Authors**: Bibek Das, Chandranath Adak, Soumi Chattopadhyay, Zahid Akhtar, Soumya Dutta  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.23178  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.23178v1.pdf

**Abstract**:
> arXiv:2603.23178v1 Announce Type: new 
Abstract: Deepfakes generated by modern generative models pose a serious threat to information integrity, digital identity, and public trust. Existing detection methods are largely reactive, attempting to identify manipulations after they occur and often failing to generalize across evolving generation techniques. This motivates the need for proactive mechanisms that secure media authenticity at the time of creation. In this work, we introduce SAiW, a Source-Attributed Invisible watermarking Framework for proactive deepfake defense and media provenance verification. Unlike conventional watermarking methods that treat watermark payloads as generic signals, SAiW formulates watermark embedding as a source-conditioned representation learning problem, wher...

---

## 107. PERMA: Benchmarking Personalized Memory Agents via Event-Driven Preference and Realistic Task Environments

**Authors**: Shuochen Liu, Junyi Zhu, Long Shu, Junda Lin, Yuhao Chen, Haotian Zhang, Chao Zhang, Derong Xu, Jia ...  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.23231  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.23231v1.pdf

**Abstract**:
> arXiv:2603.23231v1 Announce Type: new 
Abstract: Empowering large language models with long-term memory is crucial for building agents that adapt to users' evolving needs. However, prior evaluations typically interleave preference-related dialogues with irrelevant conversations, reducing the task to needle-in-a-haystack retrieval while ignoring relationships between events that drive the evolution of user preferences. Such settings overlook a fundamental characteristic of real-world personalization: preferences emerge gradually and accumulate across interactions within noisy contexts. To bridge this gap, we introduce PERMA, a benchmark designed to evaluate persona consistency over time beyond static preference recall. Additionally, we incorporate (1) text variability and (2) linguistic ali...

---

## 108. RelayS2S: A Dual-Path Speculative Generation for Real-Time Dialogue

**Authors**: Long Mai  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.23346  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.23346v1.pdf

**Abstract**:
> arXiv:2603.23346v1 Announce Type: new 
Abstract: Real-time spoken dialogue systems face a fundamental tension between latency and response quality. End-to-end speech-to-speech (S2S) models respond immediately and naturally handle turn-taking, backchanneling, and interruption, but produce semantically weaker outputs. Cascaded pipelines (ASR -> LLM) deliver stronger responses at the cost of latency that grows with model size. We present RelayS2S, a hybrid architecture that runs two paths in parallel upon turn detection. The fast path -- a duplex S2S model -- speculatively drafts a short response prefix that is streamed immediately to TTS for low-latency audio onset, while continuing to monitor live audio events. The slow path -- a cascaded ASR -> LLM pipeline -- generates a higher-quality co...

---

## 109. Whether, Not Which: Mechanistic Interpretability Reveals Dissociable Affect Reception and Emotion Categorization in LLMs

**Authors**: Michael Keeman  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22295  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22295v1.pdf

**Abstract**:
> arXiv:2603.22295v1 Announce Type: cross 
Abstract: Large language models appear to develop internal representations of emotion -- "emotion circuits," "emotion neurons," and structured emotional manifolds have been reported across multiple model families. But every study making these claims uses stimuli signalled by explicit emotion keywords, leaving a fundamental question unanswered: do these circuits detect genuine emotional meaning, or do they detect the word "devastated"? We present the first clinical validity test of emotion circuit claims using mechanistic interpretability methods grounded in clinical psychology -- clinical vignettes that evoke emotions through situational and behavioural cues alone, emotion keywords removed. Across six models (Llama-3.2-1B, Llama-3-8B, Gemma-2-9B; ba...

---

## 110. Bridging neuroscience and AI: adaptive, culturally sensitive technologies transforming aphasia rehabilitation

**Authors**: Andreea I. Niculescu, Jochen Ehnes, Minghui Dong  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22357  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22357v1.pdf

**Abstract**:
> arXiv:2603.22357v1 Announce Type: cross 
Abstract: Aphasia, a language impairment primarily resulting from stroke or brain injury, profoundly disrupts communication and everyday functioning. Despite advances in speech therapy, barriers such as limited therapist availability and the scarcity of personalized, culturally relevant tools continue to hinder optimal rehabilitation outcomes. This paper reviews recent developments in neurocognitive research and language technologies that contribute to the diagnosis and therapy of aphasia. Drawing on findings from our ethnographic field study, we introduce two digital therapy prototypes designed to reflect local linguistic diversity and enhance patient engagement. We also show how insights from neuroscience and the local context guided the design of...

---

## 111. Early Discoveries of Algorithmist I: Promise of Provable Algorithm Synthesis at Scale

**Authors**: Janardhan Kulkarni  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22363  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22363v1.pdf

**Abstract**:
> arXiv:2603.22363v1 Announce Type: cross 
Abstract: Designing algorithms with provable guarantees that also work well in practice remains difficult, requiring both mathematical reasoning and careful implementation. Existing approaches that bridge worst-case theory and empirical performance, such as beyond-worst-case analysis and data-driven algorithm selection, typically assume prior distributional knowledge or restrict attention to a fixed pool of algorithms. Recent progress in LLMs suggests a new possibility: provable algorithm synthesis on the fly. To study this, we built Algorithmist, an autonomous researcher agent on top of GitHub Copilot that runs a multi-agent research-and-review loop, with separate stages for idea generation, algorithm and proof development, proof-guided implementat...

---

## 112. When Visuals Aren't the Problem: Evaluating Vision-Language Models on Misleading Data Visualizations

**Authors**: Harsh Nishant Lalai, Raj Sanjay Shah, Hanspeter Pfister, Sashank Varma, Grace Guo  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22368  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22368v1.pdf

**Abstract**:
> arXiv:2603.22368v1 Announce Type: cross 
Abstract: Visualizations help communicate data insights, but deceptive data representations can distort their interpretation and propagate misinformation. While recent Vision Language Models (VLMs) perform well on many chart understanding tasks, their ability to detect misleading visualizations, especially when deception arises from subtle reasoning errors in captions, remains poorly understood. Here, we evaluate VLMs on misleading visualization-caption pairs grounded in a fine-grained taxonomy of reasoning errors (e.g., Cherry-picking, Causal inference) and visualization design errors (e.g., Truncated axis, Dual axis, inappropriate encodings). To this end, we develop a benchmark that combines real-world visualization with human-authored, curated mi...

---

## 113. Tiny Inference-Time Scaling with Latent Verifiers

**Authors**: Davide Bucciarelli, Evelyn Turri, Lorenzo Baraldi, Marcella Cornia, Lorenzo Baraldi, Rita Cucchiara  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22492  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22492v1.pdf

**Abstract**:
> arXiv:2603.22492v1 Announce Type: cross 
Abstract: Inference-time scaling has emerged as an effective way to improve generative models at test time by using a verifier to score and select candidate outputs. A common choice is to employ Multimodal Large Language Models (MLLMs) as verifiers, which can improve performance but introduce substantial inference-time cost. Indeed, diffusion pipelines operate in an autoencoder latent space to reduce computation, yet MLLM verifiers still require decoding candidates to pixel space and re-encoding them into the visual embedding space, leading to redundant and costly operations. In this work, we propose Verifier on Hidden States (VHS), a verifier that operates directly on intermediate hidden representations of Diffusion Transformer (DiT) single-step ge...

---

## 114. GraphRAG for Engineering Diagrams: ChatP&ID Enables LLM Interaction with P&IDs

**Authors**: Achmad Anggawirya Alimin, Artur M. Schweidtmann  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22528  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22528v1.pdf

**Abstract**:
> arXiv:2603.22528v1 Announce Type: cross 
Abstract: Large Language Models (LLMs) combined with Retrieval-Augmented Generation (RAG) and knowledge graphs offer new opportunities for interacting with engineering diagrams such as Piping and Instrumentation Diagrams (P&amp;IDs). However, directly processing raw images or smart P&amp;ID files with LLMs is often costly, inefficient, and prone to hallucinations. This work introduces ChatP&amp;ID, an agentic framework that enables grounded and cost-effective natural-language interaction with P&amp;IDs using Graph Retrieval-Augmented Generation (GraphRAG), a paradigm we refer to as GraphRAG for engineering diagrams. Smart P&amp;IDs encoded in the DEXPI standard are transformed into structured knowledge graphs, which serve as the basis for graph-base...

---

## 115. LGSE: Lexically Grounded Subword Embedding Initialization for Low-Resource Language Adaptation

**Authors**: Hailay Teklehaymanot, Dren Fazlija, Wolfgang Nejdl  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22629  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22629v1.pdf

**Abstract**:
> arXiv:2603.22629v1 Announce Type: cross 
Abstract: Adapting pretrained language models to low-resource, morphologically rich languages remains a significant challenge. Existing vocabulary expansion methods typically rely on arbitrarily segmented subword units, resulting in fragmented lexical representations and loss of critical morphological information. To address this limitation, we propose the Lexically Grounded Subword Embedding Initialization (LGSE) framework, which introduces morphologically informed segmentation for initializing embeddings of novel tokens. Instead of using random vectors or arbitrary subwords, LGSE decomposes words into their constituent morphemes and constructs semantically coherent embeddings by averaging pretrained subword or FastText-based morpheme representatio...

---

## 116. AwesomeLit: Towards Hypothesis Generation with Agent-Supported Literature Research

**Authors**: Zefei Xie, Yuhan Guo, Kai Xu  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22648  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22648v1.pdf

**Abstract**:
> arXiv:2603.22648v1 Announce Type: cross 
Abstract: There are different goals for literature research, from understanding an unfamiliar topic to generate hypothesis for the next research project. The nature of literature research also varies according to user's familiarity level of the topic. For inexperienced researchers, identifying gaps in the existing literature and generating feasible hypothesis are crucial but challenging. While general ``deep research'' tools can be used, they are not designed for such use case, thus often not effective. In addition, the ``black box" nature and hallucination of Large Language Models (LLMs) often lead to distrust. In this paper, we introduce a human-agent collaborative visualization system AwesomeLit to address this need. It has several novel features...

---

## 117. UAV-DETR: DETR for Anti-Drone Target Detection

**Authors**: Jun Yang, Dong Wang, Hongxu Yin, Hongpeng Li, Jianxiong Yu  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22841  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22841v1.pdf

**Abstract**:
> arXiv:2603.22841v1 Announce Type: cross 
Abstract: Drone detection is pivotal in numerous security and counter-UAV applications. However, existing deep learning-based methods typically struggle to balance robust feature representation with computational efficiency. This challenge is particularly acute when detecting miniature drones against complex backgrounds under severe environmental interference. To address these issues, we introduce UAV-DETR, a novel framework that integrates a small-target-friendly architecture with real-time detection capabilities. Specifically, UAV-DETR features a WTConv-enhanced backbone and a Sliding Window Self-Attention (SWSA-IFI) encoder, capturing the high-frequency structural details of tiny targets while drastically reducing parameter overhead. Furthermore,...

---

## 118. ForestPrune: High-ratio Visual Token Compression for Video Multimodal Large Language Models via Spatial-Temporal Forest Modeling

**Authors**: Shaobo Ju, Baiyang Song, Tao Chen, Jiapeng Zhang, Qiong Wu, Chao Chang, HuaiXi Wang, Yiyi Zhou, Rong...  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.22911  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.22911v1.pdf

**Abstract**:
> arXiv:2603.22911v1 Announce Type: cross 
Abstract: Due to the great saving of computation and memory overhead, token compression has become a research hot-spot for MLLMs and achieved remarkable progress in image-language tasks. However, for the video, existing methods still fall short of high-ratio token compression. We attribute this shortcoming to the insufficient modeling of temporal and continual video content, and propose a novel and training-free token pruning method for video MLLMs, termed ForestPrune, which achieves effective and high-ratio pruning via Spatial-temporal Forest Modeling. In practice, ForestPrune construct token forests across video frames based on the semantic, spatial and temporal constraints, making an overall comprehension of videos. Afterwards, ForestPrune evalua...

---

## 119. AgentRAE: Remote Action Execution through Notification-based Visual Backdoors against Screenshots-based Mobile GUI Agents

**Authors**: Yutao Luo, Haotian Zhu, Shuchao Pang, Zhigang Lu, Tian Dong, Yongbin Zhou, Minhui Xue  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.23007  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.23007v1.pdf

**Abstract**:
> arXiv:2603.23007v1 Announce Type: cross 
Abstract: The rapid adoption of mobile graphical user interface (GUI) agents, which autonomously control applications and operating systems (OS), exposes new system-level attack surfaces. Existing backdoors against web GUI agents and general GenAI models rely on environmental injection or deceptive pop-ups to mislead the agent operation. However, these techniques do not work on screenshots-based mobile GUI agents due to the challenges of restricted trigger design spaces, OS background interference, and conflicts in multiple trigger-action mappings. We propose AgentRAE, a novel backdoor attack capable of inducing Remote Action Execution in mobile GUI agents using visually natural triggers (e.g., benign app icons in notifications). To address the unde...

---

## 120. Why AI-Generated Text Detection Fails: Evidence from Explainable AI Beyond Benchmark Accuracy

**Authors**: Shushanta Pudasaini, Luis Miralles-Pechu\'an, David Lillis, Marisa Llorens Salvador  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.23146  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.23146v1.pdf

**Abstract**:
> arXiv:2603.23146v1 Announce Type: cross 
Abstract: The widespread adoption of Large Language Models (LLMs) has made the detection of AI-Generated text a pressing and complex challenge. Although many detection systems report high benchmark accuracy, their reliability in real-world settings remains uncertain, and their interpretability is often unexplored. In this work, we investigate whether contemporary detectors genuinely identify machine authorship or merely exploit dataset-specific artefacts. We propose an interpretable detection framework that integrates linguistic feature engineering, machine learning, and explainable AI techniques. When evaluated on two prominent benchmark corpora, namely PAN CLEF 2025 and COLING 2025, our model trained on 30 linguistic features achieves leaderboard-...

---

## 121. Reasoning over Semantic IDs Enhances Generative Recommendation

**Authors**: Yingzhi He, Yan Sun, Junfei Tan, Yuxin Chen, Xiaoyu Kong, Chunxu Shen, Xiang Wang, An Zhang, Tat-Sen...  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.23183  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.23183v1.pdf

**Abstract**:
> arXiv:2603.23183v1 Announce Type: cross 
Abstract: Recent advances in generative recommendation have leveraged pretrained LLMs by formulating sequential recommendation as autoregressive generation over a unified token space comprising language tokens and itemic identifiers, where each item is represented by a compact sequence of discrete tokens, namely Semantic IDs (SIDs). This SID-based formulation enables efficient decoding over large-scale item corpora and provides a natural interface for LLM-based recommenders to leverage rich world knowledge. Meanwhile, breakthroughs in LLM reasoning motivate reasoning-enhanced recommendation, yet effective reasoning over SIDs remains underexplored and challenging. Itemic tokens are not natively meaningful to LLMs; moreover, recommendation-oriented SI...

---

## 122. A Multimodal Framework for Human-Multi-Agent Interaction

**Authors**: Shaid Hasan, Breenice Lee, Sujan Sarker, Tariq Iqbal  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.23271  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.23271v1.pdf

**Abstract**:
> arXiv:2603.23271v1 Announce Type: cross 
Abstract: Human-robot interaction is increasingly moving toward multi-robot, socially grounded environments. Existing systems struggle to integrate multimodal perception, embodied expression, and coordinated decision-making in a unified framework. This limits natural and scalable interaction in shared physical spaces. We address this gap by introducing a multimodal framework for human-multi-agent interaction in which each robot operates as an autonomous cognitive agent with integrated multimodal perception and Large Language Model (LLM)-driven planning grounded in embodiment. At the team level, a centralized coordination mechanism regulates turn-taking and agent participation to prevent overlapping speech and conflicting actions. Implemented on two ...

---

## 123. Curriculum-Driven 3D CT Report Generation via Language-Free Visual Grafting and Zone-Constrained Compression

**Authors**: V. K. Cody Bumgardner, Mitchell A. Klusty, Mahmut S. Gokmen, Evan W. Damron  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.23308  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.23308v1.pdf

**Abstract**:
> arXiv:2603.23308v1 Announce Type: cross 
Abstract: Automated radiology report generation from 3D computed tomography (CT) volumes is challenging due to extreme sequence lengths, severe class imbalance, and the tendency of large language models (LLMs) to ignore visual tokens in favor of linguistic priors. We present Ker-VLJEPA-3B, a four-phase curriculum learning framework for free-text report generation from thoracic CT volumes. A phased training curriculum progressively adapts a Llama 3.2 3B decoder to ground its output in visual features from a frozen, self-supervised encoder. Our visual backbone (LeJEPA ViT-Large) is trained via self-supervised joint-embedding prediction on unlabeled CTs, without text supervision. Unlike contrastive models (CLIP, BiomedCLIP), this language-free backbone...

---

## 124. Leveraging LLMs and Social Media to Understand User Perception of Smartphone-Based Earthquake Early Warnings

**Authors**: Hanjing Wang, S. Mostafa Mousavi, Patrick Robertson, Richard M. Allen, Alexie Barski, Robert Bosch, ...  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.23322  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.23322v1.pdf

**Abstract**:
> arXiv:2603.23322v1 Announce Type: cross 
Abstract: Android's Earthquake Alert (AEA) system provided timely early warnings to millions during the Mw 6.2 Marmara Ereglisi, T\"urkiye earthquake on April 23, 2025. This event, the largest in the region in 25 years, served as a critical real-world test for smartphone-based Earthquake Early Warning (EEW) systems. The AEA system successfully delivered alerts to users with high precision, offering over a minute of warning before the strongest shaking reached urban areas. This study leveraged Large Language Models (LLMs) to analyze more than 500 public social media posts from the X platform, extracting 42 distinct attributes related to user experience and behavior. Statistical analyses revealed significant relationships, notably a strong correlation...

---

## 125. Obscure but Effective: Classical Chinese Jailbreak Prompt Optimization via Bio-Inspired Search

**Authors**: Xun Huang, Simeng Qin, Xiaoshuang Jia, Ranjie Duan, Huanqian Yan, Zhitao Zeng, Fei Yang, Yang Liu, X...  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.22983  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.22983v3.pdf

**Abstract**:
> arXiv:2602.22983v3 Announce Type: replace 
Abstract: As Large Language Models (LLMs) are increasingly used, their security risks have drawn increasing attention. Existing research reveals that LLMs are highly susceptible to jailbreak attacks, with effectiveness varying across language contexts. This paper investigates the role of classical Chinese in jailbreak attacks. Owing to its conciseness and obscurity, classical Chinese can partially bypass existing safety constraints, exposing notable vulnerabilities in LLMs. Based on this observation, this paper proposes a framework, CC-BOS, for the automatic generation of classical Chinese adversarial prompts based on multi-dimensional fruit fly optimization, facilitating efficient and automated jailbreak attacks in black-box settings. Prompts are...

---

## 126. Agentic AI-based Coverage Closure for Formal Verification

**Authors**: Sivaram Pothireddypalli, Ashish Raman, Deepak Narayan Gadde, Aman Kumar  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.03147  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.03147v2.pdf

**Abstract**:
> arXiv:2603.03147v2 Announce Type: replace 
Abstract: Coverage closure is a critical requirement in Integrated Chip (IC) development process and key metric for verification sign-off. However, traditional exhaustive approaches often fail to achieve full coverage within project timelines. This study presents an agentic AI-driven workflow that utilizes Large Language Model (LLM)-enabled Generative AI (GenAI) to automate coverage analysis for formal verification, identify coverage gaps, and generate the required formal properties. The framework accelerates verification efficiency by systematically addressing coverage holes. Benchmarking open-source and internal designs reveals a measurable increase in coverage metrics, with improvements correlated to the complexity of the design. Comparative an...

---

## 127. Retrieval-Augmented Generation with Covariate Time Series

**Authors**: Kenny Ye Liang, Zhongyi Pei, Huan Zhang, Yuhui Liu, Shaoxu Song, Jianmin Wang  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.04951  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.04951v2.pdf

**Abstract**:
> arXiv:2603.04951v2 Announce Type: replace 
Abstract: While RAG has greatly enhanced LLMs, extending this paradigm to Time-Series Foundation Models (TSFMs) remains a challenge. This is exemplified in the Predictive Maintenance of the Pressure Regulating and Shut-Off Valve (PRSOV), a high-stakes industrial scenario characterized by (1) data scarcity, (2) short transient sequences, and (3) covariate coupled dynamics. Unfortunately, existing time-series RAG approaches predominantly rely on generated static vector embeddings and learnable context augmenters, which may fail to distinguish similar regimes in such scarce, transient, and covariate coupled scenarios. To address these limitations, we propose RAG4CTS, a regime-aware, training-free RAG framework for Covariate Time-Series. Specifically,...

---

## 128. Towards Intelligent Geospatial Data Discovery: a knowledge graph-driven multi-agent framework powered by large language models

**Authors**: Ruixiang Liu, Zhenlong Li, Ali Khosravi Kazazi  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20670  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20670v2.pdf

**Abstract**:
> arXiv:2603.20670v2 Announce Type: replace 
Abstract: The rapid growth in the volume, variety, and velocity of geospatial data has created data ecosystems that are highly distributed, heterogeneous, and semantically inconsistent. Existing data catalogs, portals, and infrastructures still rely largely on keyword-based search with limited semantic support, which often fails to capture user intent and leads to weak retrieval performance. To address these challenges, this study proposes a knowledge graph-driven multi-agent framework for intelligent geospatial data discovery, powered by large language models. The framework introduces a unified geospatial metadata ontology as a semantic mediation layer to align heterogeneous metadata standards across platforms and constructs a geospatial metadata...

---

## 129. Cerebra: A Multidisciplinary AI Board for Multimodal Dementia Characterization and Risk Assessment

**Authors**: Sheng Liu, Long Chen, Zeyun Zhao, Qinglin Gou, Qingyue Wei, Arjun Masurkar, Kevin M. Spiegler, Phili...  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21597  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21597v2.pdf

**Abstract**:
> arXiv:2603.21597v2 Announce Type: replace 
Abstract: Modern clinical practice increasingly depends on reasoning over heterogeneous, evolving, and incomplete patient data. Although recent advances in multimodal foundation models have improved performance on various clinical tasks, most existing models remain static, opaque, and poorly aligned with real-world clinical workflows. We present Cerebra, an interactive multi-agent AI team that coordinates specialized agents for EHR, clinical notes, and medical imaging analysis. These outputs are synthesized into a clinician-facing dashboard that combines visual analytics with a conversational interface, enabling clinicians to interrogate predictions and contextualize risk at the point of care. Cerebra supports privacy-preserving deployment by oper...

---

## 130. MS-DGCNN++: Multi-Scale Dynamic Graph Convolution with Scale-Dependent Normalization for Robust LiDAR Tree Species Classification

**Authors**: Said Ohamouddou, Hanaa El Afia, Mohamed Hamza Boulaich, Abdellatif El Afia, Raddouane Chiheb  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2507.12602  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2507.12602v2.pdf

**Abstract**:
> arXiv:2507.12602v2 Announce Type: replace-cross 
Abstract: Graph-based deep learning on LiDAR point clouds encodes geometry through edge features, yet standard implementations use the same encoding at every scale. In tree species classification, where point density varies by orders of magnitude between trunk and canopy, this is particularly limiting. We prove it is suboptimal: normalized directional features have mean squared error decaying as $\mathcal{O}(1/s^2)$ with inter-point distance~$s$, while raw displacement error is constant, implying each encoding suits a different signal-to-noise ratio (SNR) regime. We propose MS-DGCNN++, a multi-scale dynamic graph convolutional network with \emph{scale-dependent edge encoding}: raw vectors at the local scale (low SNR) and hybrid raw-plus-norm...

---

## 131. From Product Hilbert Spaces to the Generalized Koopman Operator and the Nonlinear Fundamental Lemma

**Authors**: Mircea Lazar  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2508.07494  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2508.07494v2.pdf

**Abstract**:
> arXiv:2508.07494v2 Announce Type: replace-cross 
Abstract: The generalization of the Koopman operator to systems with control input and the derivation of a nonlinear fundamental lemma are two open problems that play a key role in the development of data-driven control methods for nonlinear systems. In this paper we derive a novel solution to these problems based on basis functions expansion in a product Hilbert space constructed as the tensor product between the Hilbert spaces of the state and input observable functions, respectively. We identify relaxed invariance conditions that guarantee existence of a bounded linear operator, i.e., the generalized Koopman operator, from the constructed product Hilbert space to the Hilbert space corresponding to the lifted state propagated forward in ti...

---

## 132. From Context to Intent: Reasoning-Guided Function-Level Code Completion

**Authors**: Yanzhou Li, Tianlin Li, Yiran Zhang, Shangqing Liu, Aishan Liu, Xianglong Liu, Yang Liu  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2508.09537  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2508.09537v2.pdf

**Abstract**:
> arXiv:2508.09537v2 Announce Type: replace-cross 
Abstract: The growing capabilities of Large Language Models (LLMs) have led to their widespread adoption for function completion within code repositories. Recent studies on such tasks show promising results when explicit instructions, often in the form of docstrings, are available to guide the completion. However, in real-world scenarios, clear docstrings are frequently absent. Under such conditions, LLMs typically fail to produce accurate completions. To enable more automated and accurate function completion in such settings, we aim to enable LLMs to accurately infer the developer's intent prior to code completion. Our key insight is that the preceding code, namely the code context before the function to be completed, often contains valuabl...

---

## 133. VL-KnG: Persistent Spatiotemporal Knowledge Graphs from Egocentric Video for Embodied Scene Understanding

**Authors**: Mohamad Al Mdfaa, Svetlana Lukina, Timur Akhtyamov, Arthur Nigmatzyanov, Dmitrii Nalberskii, Sergey ...  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.01483  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.01483v2.pdf

**Abstract**:
> arXiv:2510.01483v2 Announce Type: replace-cross 
Abstract: Vision-language models (VLMs) demonstrate strong image-level scene understanding but often lack persistent memory, explicit spatial representations, and computational efficiency when reasoning over long video sequences. We present VL-KnG, a training-free framework that constructs spatiotemporal knowledge graphs from monocular video, bridging fine-grained scene graphs and global topological graphs without 3D reconstruction. VL-KnG processes video in chunks, maintains persistent object identity via LLM-based Spatiotemporal Object Association (STOA), and answers queries via Graph-Enhanced Retrieval (GER), a hybrid of GraphRAG subgraph retrieval and SigLIP2 visual grounding. Once built, the knowledge graph eliminates the need to re-pro...

---

## 134. Happiness is Sharing a Vocabulary: A Study of Transliteration Methods

**Authors**: Haeji Jung, Jinju Kim, Kyungjin Kim, Youjeong Roh, David R. Mortensen  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.10827  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.10827v2.pdf

**Abstract**:
> arXiv:2510.10827v2 Announce Type: replace-cross 
Abstract: Transliteration has emerged as a promising means to bridge the gap between various languages in multilingual NLP, showing promising results especially for languages using non-Latin scripts. We investigate the degree to which shared script, overlapping token vocabularies, and shared phonology contribute to performance of multilingual models. To this end, we conduct controlled experiments using three kinds of transliteration (romanization, phonemic transcription, and substitution ciphers) as well as orthography. We evaluate each model on three downstream tasks -- named entity recognition (NER), part-of-speech tagging (POS) and natural language inference (NLI) -- and find that romanization significantly outperforms other input types i...

---

## 135. Do Vision-Language Models Measure Up? Benchmarking Visual Measurement Reading with MeasureBench

**Authors**: Fenfen Lin, Yesheng Liu, Haiyu Xu, Chen Yue, Zheqi He, Mingxuan Zhao, Miguel Hu Chen, Jiakang Liu, J...  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.26865  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.26865v2.pdf

**Abstract**:
> arXiv:2510.26865v2 Announce Type: replace-cross 
Abstract: Reading measurement instruments is effortless for humans and requires relatively little domain expertise, yet it remains surprisingly challenging for current vision-language models (VLMs) as we find in preliminary evaluation. In this work, we introduce MeasureBench, a benchmark on visual measurement reading covering both real-world and synthesized images of various types of measurements, along with an extensible pipeline for data synthesis. Our pipeline procedurally generates a specified type of gauge with controllable visual appearance, enabling scalable variation in key details such as pointers, scales, fonts, lighting, and clutter. Evaluation on popular proprietary and open-weight VLMs shows that even the strongest frontier VLMs...

---

## 136. VLM-CAD: VLM-Optimized Collaborative Agent Design Workflow for Analog Circuit Sizing

**Authors**: Guanyuan Pan, Shuai Wang, Yugui Lin, Tiansheng Zhou, Pietro Li\`o, Zhenxin Zhao, Yaqi Wang  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2601.07315  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2601.07315v4.pdf

**Abstract**:
> arXiv:2601.07315v4 Announce Type: replace-cross 
Abstract: Vision Language Models (VLMs) have demonstrated remarkable potential in multimodal reasoning, yet they inherently suffer from spatial blindness and logical hallucinations when interpreting densely structured engineering content, such as analog circuit schematics. To address these challenges, we propose a Vision Language Model-Optimized Collaborative Agent Design Workflow for Analog Circuit Sizing (VLM-CAD) designed for robust, step-by-step reasoning over multimodal evidence. VLM-CAD bridges the modality gap by integrating a neuro-symbolic structural parsing module, Image2Net, which transforms raw pixels into explicit topological graphs and structured JSON representations to anchor VLM interpretation in deterministic facts. To ensur...

---

## 137. Hierarchical Long Video Understanding with Audiovisual Entity Cohesion and Agentic Search

**Authors**: Xinlei Yin, Xiulian Peng, Xiao Li, Zhiwei Xiong, Yan Lu  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2601.13719  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2601.13719v2.pdf

**Abstract**:
> arXiv:2601.13719v2 Announce Type: replace-cross 
Abstract: Long video understanding presents significant challenges for vision-language models due to extremely long context windows. Existing solutions relying on naive chunking strategies with retrieval-augmented generation, typically suffer from information fragmentation and a loss of global coherence. We present HAVEN, a unified framework for long-video understanding that enables coherent and comprehensive reasoning by integrating audiovisual entity cohesion and hierarchical video indexing with agentic search. First, we preserve semantic consistency by integrating entity-level representations across visual and auditory streams, while organizing content into a structured hierarchy spanning global summary, scene, segment, and entity levels....

---

## 138. Energy-Aware Reinforcement Learning for Robotic Manipulation of Articulated Components in Infrastructure Operation and Maintenance

**Authors**: Xiaowen Tao, Yinuo Wang, Haitao Ding, Yuanyang Qi, Ziyu Song  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.12288  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.12288v3.pdf

**Abstract**:
> arXiv:2602.12288v3 Announce Type: replace-cross 
Abstract: With the growth of intelligent civil infrastructure and smart cities, operation and maintenance (O&amp;M) increasingly requires safe, efficient, and energy-conscious robotic manipulation of articulated components, including access doors, service drawers, and pipeline valves. However, existing robotic approaches either focus primarily on grasping or target object-specific articulated manipulation, and they rarely incorporate explicit actuation energy into multi-objective optimisation, which limits their scalability and suitability for long-term deployment in real O&amp;M settings. Therefore, this paper proposes an articulation-agnostic and energy-aware reinforcement learning framework for robotic manipulation in intelligent infrastr...

---

## 139. CRoCoDiL: Continuous and Robust Conditioned Diffusion for Language

**Authors**: Roy Uziel, Omer Belhasin, Itay Levi, Akhiad Bercovich, Ran El-Yaniv, Ran Zilberstein, Michael Elad  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.20210  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.20210v2.pdf

**Abstract**:
> arXiv:2603.20210v2 Announce Type: replace-cross 
Abstract: Masked Diffusion Models (MDMs) provide an efficient non-causal alternative to autoregressive generation but often struggle with token dependencies and semantic incoherence due to their reliance on discrete marginal distributions. We address these limitations by shifting the diffusion process into a continuous sentence-level semantic space. We propose CRoCoDiL (Continuous and Robust Conditioned Diffusion for Language), a unified fine-tuning approach that jointly trains an encoder-demasker architecture, grounding the MDM demasking in continuous latent representations. This leads to the formation of a novel autoencoder in which decoding is obtained by an MDM algorithm. Relying on the same framework, we introduce two unconditional text...

---

## 140. DeepXplain: XAI-Guided Autonomous Defense Against Multi-Stage APT Campaigns

**Authors**: Trung V. Phan, Thomas Bauschert  
**Categories**: cs.AI  
**Published**: Wed, 25 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.21296  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.21296v2.pdf

**Abstract**:
> arXiv:2603.21296v2 Announce Type: replace-cross 
Abstract: Advanced Persistent Threats (APTs) are stealthy, multi-stage attacks that require adaptive and timely defense. While deep reinforcement learning (DRL) enables autonomous cyber defense, its decisions are often opaque and difficult to trust in operational environments. This paper presents DeepXplain, an explainable DRL framework for stage-aware APT defense. Building on our prior DeepStage model, DeepXplain integrates provenance-based graph learning, temporal stage estimation, and a unified XAI pipeline that provides structural, temporal, and policy-level explanations. Unlike post-hoc methods, explanation signals are incorporated directly into policy optimization through evidence alignment and confidence-aware reward shaping. To the b...

---

