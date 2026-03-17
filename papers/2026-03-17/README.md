# arXiv Papers - 2026-03-17

**来源**: arXiv (cs.SD, eess.AS, cs.LG, cs.AI)  
**关键词**: speech, audio, music, voice, sound, Mel, representation, self-supervised  
**今日新论文**: 103 篇

---

## 1. Mask2Flow-TSE: Two-Stage Target Speaker Extraction with Masking and Flow Matching

**Authors**: Junwon Moon, Hyunjin Choi, Hansol Park, Heeseung Kim, Kyuhong Shim  
**Categories**: cs.SD  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12837  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12837v1.pdf

**Abstract**:
> arXiv:2603.12837v1 Announce Type: new 
Abstract: Target speaker extraction (TSE) extracts the target speaker's voice from overlapping speech mixtures given a reference utterance. Existing approaches typically fall into two categories: discriminative and generative. Discriminative methods apply time-frequency masking for fast inference but often over-suppress the target signal, while generative methods synthesize high-quality speech at the cost of numerous iterative steps. We propose Mask2Flow-TSE, a two-stage framework combining the strengths of both paradigms. The first stage applies discriminative masking for coarse separation, and the second stage employs flow matching to refine the output toward target speech. Unlike generative approaches that synthesize speech from Gaussian noise, our...

---

## 2. DAST: A Dual-Stream Voice Anonymization Attacker with Staged Training

**Authors**: Ridwan Arefeen, Xiaoxiao Miao, Rong Tong, Aik Beng Ng, Simon See, Timothy Liu  
**Categories**: cs.SD  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12840  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12840v1.pdf

**Abstract**:
> arXiv:2603.12840v1 Announce Type: new 
Abstract: Voice anonymization masks vocal traits while preserving linguistic content, which may still leak speaker-specific patterns. To assess and strengthen privacy evaluation, we propose a dual-stream attacker that fuses spectral and self-supervised learning features via parallel encoders with a three-stage training strategy. Stage I establishes foundational speaker-discriminative representations. Stage II leverages the shared identity-transformation characteristics of voice conversion and anonymization, exposing the model to diverse converted speech to build cross-system robustness. Stage III provides lightweight adaptation to target anonymized data. Results on the VoicePrivacy Attacker Challenge (VPAC) dataset demonstrate that Stage II is the pri...

---

## 3. Perpetual Dialogues: A Computational Analysis of Voice-Guitar Interaction in Carlos Paredes's Discography

**Authors**: Gilberto Bernardes, N\'adia Moura, Ant\'onio S\'a Pinto  
**Categories**: cs.SD  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12854  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12854v1.pdf

**Abstract**:
> arXiv:2603.12854v1 Announce Type: new 
Abstract: Computational musicology enables systematic analysis of performative and structural traits in recorded music, yet existing approaches remain largely tailored to notated, score-based repertoires. This study advances a methodology for analyzing voice-guitar interaction in Carlos Paredes's vocal collaborations - an oral-tradition context where compositional and performative layers co-emerge. Using source-separated stems, physics-informed harmonic modelling, and beat-level audio descriptors, we examine melodic, harmonic, and rhythmic relationships across eight recordings with four singers. Our commonality-diversity framework, combining multi-scale correlation analysis with residual-based detection of structural deviations, reveals that expressiv...

---

## 4. TASTE-Streaming: Towards Streamable Text-Aligned Speech Tokenization and Embedding for Spoken Language Modeling

**Authors**: Liang-Hsuan Tseng, Hung-yi Lee  
**Categories**: cs.SD  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12350  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12350v1.pdf

**Abstract**:
> arXiv:2603.12350v1 Announce Type: cross 
Abstract: Text-speech joint spoken language modeling (SLM) aims at natural and intelligent speech-based interactions, but developing such a system may suffer from modality mismatch: speech unit sequences are much longer than text tokens. Prior work reduces this gap with text-aligned tokenization and embedding (TASTE), producing speech tokens that align in lengths with their textual counterparts. However, the dependence on an external ASR system and the use of a non-causal decoder limits streaming use. To address this limitation, we propose TASTE-S, a streamable extension of TASTE suitable for real-time usage. TASTE-S integrates a CTC-based ASR module into the encoder for instant dual-modality encoding. We also redesign the unit decoder to enable on-...

---

## 5. RadEar: A Self-Supervised RF Backscatter System for Voice Eavesdropping and Separation

**Authors**: Qijun Wang, Peihao Yan, Chunqi Qian, Huacheng Zeng  
**Categories**: cs.SD  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12446  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12446v1.pdf

**Abstract**:
> arXiv:2603.12446v1 Announce Type: cross 
Abstract: Eavesdropping on voice conversations presents a growing threat to personal privacy and information security. In this paper, we present RadEar, a novel RF backscatter-based system designed to enable covert voice eavesdropping through walls. RadEar consists of two key components: (i) a batteryless RF backscatter tag covertly deployed inside the target space, and (ii) an RF reader located outside the room that performs signal demodulation, voice separation, and denoising. The tag features a compact, dual-resonator design that achieves energy-efficient frequency modulation for continuous voice eavesdropping while mitigating self-interference by separating excitation and reflection frequencies. To overcome the challenges of weak signal receptio...

---

## 6. Self-Supervised Speech Models Encode Phonetic Context via Position-dependent Orthogonal Subspaces

**Authors**: Kwanghee Choi, Eunjung Yeo, Cheol Jun Cho, David R. Mortensen, David Harwath  
**Categories**: cs.SD  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12642  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12642v1.pdf

**Abstract**:
> arXiv:2603.12642v1 Announce Type: cross 
Abstract: Transformer-based self-supervised speech models (S3Ms) are often described as contextualized, yet what this entails remains unclear. Here, we focus on how a single frame-level S3M representation can encode phones and their surrounding context. Prior work has shown that S3Ms represent phones compositionally; for example, phonological vectors such as voicing, bilabiality, and nasality vectors are superposed in the S3M representation of [m]. We extend this view by proposing that phonological information from a sequence of neighboring phones is also compositionally encoded in a single frame, such that vectors corresponding to previous, current, and next phones are superposed within a single frame-level representation. We show that this structu...

---

## 7. Mitigating Latent Mismatch in cVAE-Based Singing Voice Synthesis via Flow Matching

**Authors**: Minhyeok Yun, Yong-Hoon Choi  
**Categories**: cs.SD  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2601.00217  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2601.00217v2.pdf

**Abstract**:
> arXiv:2601.00217v2 Announce Type: replace 
Abstract: Singing voice synthesis (SVS) aims to generate natural and expressive singing waveforms from symbolic musical scores. In cVAE-based SVS, however, a mismatch arises because the decoder is trained with latent representations inferred from target singing signals, while inference relies on latent representations predicted only from conditioning inputs. This discrepancy can weaken fine expressive acoustic details in the synthesized output. To mitigate this issue, we propose FM-Singer, a flow-matching-based latent refinement framework for cVAE-based singing voice synthesis. Rather than redesigning the acoustic decoder, the proposed method learns a continuous vector field that transports inference-time latent samples toward posterior-like laten...

---

## 8. nlm: Real-Time Non-linear Modal Synthesis in Max

**Authors**: Rodrigo Diaz, Rodrigo Constanzo, Mark Sandler  
**Categories**: cs.SD  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10240  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10240v2.pdf

**Abstract**:
> arXiv:2603.10240v2 Announce Type: replace 
Abstract: We present nlm, a set of Max externals that enable efficient real-time non-linear modal synthesis for strings, membranes, and plates. The externals, implemented in C++, offer interactive control of physical parameters, allow the loading of custom modal data, and provide multichannel output. By integrating interactive physical-modelling capabilities into a familiar environment, nlm lowers the barrier for composers, performers, and sound designers to explore the expressive potential of non-linear modal synthesis. The externals are available as open-source software at https://github.com/rodrigodzf/nlm.

---

## 9. MAGE: A Coarse-to-Fine Speech Enhancer with Masked Generative Model

**Authors**: The Hieu Pham, Tan Dat Nguyen, Phuong Thanh Tran, Joon Son Chung, Duc Dung Nguyen  
**Categories**: cs.SD  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2509.19881  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2509.19881v3.pdf

**Abstract**:
> arXiv:2509.19881v3 Announce Type: replace-cross 
Abstract: Speech enhancement remains challenging due to the trade-off between efficiency and perceptual quality. In this paper, we introduce MAGE, a Masked Audio Generative Enhancer that advances generative speech enhancement through a compact and robust design. Unlike prior masked generative models with random masking, MAGE employs a scarcity-aware coarse-to-fine masking strategy that prioritizes frequent tokens in early steps and rare tokens in later refinements, improving efficiency and generalization. We also propose a lightweight corrector module that further stabilizes inference by detecting low-confidence predictions and re-masking them for refinement. Built on BigCodec and finetuned from Qwen2.5-0.5B, MAGE is reduced to 200M paramete...

---

## 10. OmniForcing: Unleashing Real-time Joint Audio-Visual Generation

**Authors**: Yaofeng Su, Yuming Li, Zeyue Xue, Jie Huang, Siming Fu, Haoran Li, Ying Li, Zezhong Qian, Haoyang Hu...  
**Categories**: cs.SD  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11647  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11647v2.pdf

**Abstract**:
> arXiv:2603.11647v2 Announce Type: replace-cross 
Abstract: Recent joint audio-visual diffusion models achieve remarkable generation quality but suffer from high latency due to their bidirectional attention dependencies, hindering real-time applications. We propose OmniForcing, the first framework to distill an offline, dual-stream bidirectional diffusion model into a high-fidelity streaming autoregressive generator. However, naively applying causal distillation to such dual-stream architectures triggers severe training instability, due to the extreme temporal asymmetry between modalities and the resulting token sparsity. We address the inherent information density gap by introducing an Asymmetric Block-Causal Alignment with a zero-truncation Global Prefix that prevents multi-modal synchron...

---

## 11. Room Impulse Response Completion Using Signal-Prediction Diffusion Models Conditioned on Simulated Early Reflections

**Authors**: Zeyu Xu, Andreas Brendel, Albert G. Prinn, Emanu\"el A. P. Habets  
**Categories**: eess.AS  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12442  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12442v1.pdf

**Abstract**:
> arXiv:2603.12442v1 Announce Type: new 
Abstract: Room impulse responses (RIRs) are fundamental to audio data augmentation, acoustic signal processing, and immersive audio rendering. While geometric simulators such as the image source method (ISM) can efficiently generate early reflections, they lack the realism of measured RIRs due to missing acoustic wave effects. We propose a diffusion-based RIR completion method using signal-prediction conditioned on ISM-simulated direct-path and early reflections. Unlike state-of-the-art methods, our approach imposes no fixed duration constraint on the input early reflections. We further incorporate classifier-free guidance to steer generation toward a target distribution learned from physically realistic RIRs simulated with the Treble SDK. Objective e...

---

## 12. Lightweight speech enhancement guided target speech extraction in noisy multi-speaker scenarios

**Authors**: Ziling Huang, Junnan Wu, Lichun Fan, Zhenbo Luo, Jian Luan, Haixin Guan, Yanhua Long  
**Categories**: eess.AS  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2508.19583  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2508.19583v2.pdf

**Abstract**:
> arXiv:2508.19583v2 Announce Type: replace 
Abstract: Target speech extraction (TSE) has achieved strong performance in relatively simple conditions such as one-speaker-plus-noise and two-speaker mixtures, but its performance remains unsatisfactory in noisy multi-speaker scenarios. To address this issue, we introduce a lightweight speech enhancement model, GTCRN, to better guide TSE in noisy environments. Building on our competitive previous speaker embedding/encoder-free framework SEF-PNet, we propose two extensions: LGTSE and D-LGTSE. LGTSE incorporates noise-agnostic enrollment guidance by denoising the input noisy speech before context interaction with enrollment speech, thereby reducing noise interference. D-LGTSE further improves system robustness against speech distortion by leveragi...

---

## 13. On Deepfake Voice Detection -- It's All in the Presentation

**Authors**: H\'ector Delgado, Giorgio Ramondetti, Emanuele Dalmasso, Gennady Karvitsky, Daniele Colibro, Haydar ...  
**Categories**: eess.AS  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2509.26471  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2509.26471v2.pdf

**Abstract**:
> arXiv:2509.26471v2 Announce Type: replace 
Abstract: While the technologies empowering malicious audio deepfakes have dramatically evolved in recent years due to generative AI advances, the same cannot be said of global research into spoofing (deepfake) countermeasures. This paper highlights how current deepfake datasets and research methodologies led to systems that failed to generalize to real world application. The main reason is due to the difference between raw deepfake audio, and deepfake audio that has been presented through a communication channel, e.g. by phone. We propose a new framework for data creation and research methodology, allowing for the development of spoofing countermeasures that would be more effective in real-world scenarios. By following the guidelines outlined her...

---

## 14. Dynamically Slimmable Speech Enhancement Network with Metric-Guided Training

**Authors**: Haixin Zhao, Kaixuan Yang, Nilesh Madhu  
**Categories**: eess.AS  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.11395  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.11395v3.pdf

**Abstract**:
> arXiv:2510.11395v3 Announce Type: replace 
Abstract: To further reduce the complexity of lightweight speech enhancement models, we introduce a gating-based Dynamically Slimmable Network (DSN). The DSN comprises static and dynamic components. For architecture-independent applicability, we introduce distinct dynamic structures targeting the commonly used components, namely, grouped recurrent neural network units, multi-head attention, convolutional, and fully connected layers. A policy module adaptively governs the use of dynamic parts at a frame-wise resolution according to the input signal quality, controlling computational load. We further propose Metric-Guided Training (MGT) to explicitly guide the policy module in assessing input speech quality. Experimental results demonstrate that the...

---

## 15. TripleC Learning and Lightweight Speech Enhancement for Multi-Condition Target Speech Extraction

**Authors**: Ziling Huang  
**Categories**: eess.AS  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2512.04945  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2512.04945v2.pdf

**Abstract**:
> arXiv:2512.04945v2 Announce Type: replace 
Abstract: In our recent work, we proposed Lightweight Speech Enhancement Guided Target Speech Extraction (LGTSE) and demonstrated its effectiveness in multi-speaker-plus-noise scenarios. However, real-world applications often involve more diverse and complex conditions, such as one-speaker-plus-noise or two-speaker-without-noise. To address this challenge, we extend LGTSE with a Cross-Condition Consistency learning strategy, termed TripleC Learning. This strategy is first validated under multi-speaker-plus-noise condition and then evaluated for its generalization across diverse scenarios. Moreover, building upon the lightweight front-end denoiser in LGTSE, which can flexibly process both noisy and clean mixtures and shows strong generalization to ...

---

## 16. Multi-objective Genetic Programming with Multi-view Multi-level Feature for Enhanced Protein Secondary Structure Prediction

**Authors**: Yining Qian, Lijie Su, Meiling Xu, Xianpeng Wang  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12293  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12293v1.pdf

**Abstract**:
> arXiv:2603.12293v1 Announce Type: new 
Abstract: Predicting protein secondary structure is essential for understanding protein function and advancing drug discovery. However, the intricate sequence-structure relationship poses significant challenges for accurate modeling. To address these, we propose MOGP-MMF, a multi-objective genetic programming framework that reformulates PSSP as an automated optimization task focused on feature selection and fusion. Specifically, MOGP-MMF introduces a multi-view multi-level representation strategy that integrates evolutionary, semantic, and newly introduced structural views to capture the comprehensive protein folding logic. Leveraging an enriched operator set, the framework evolves both linear and nonlinear fusion functions, effectively capturing high...

---

## 17. Global Evolutionary Steering: Refining Activation Steering Control via Cross-Layer Consistency

**Authors**: Xinyan Jiang, Wenjing Yu, Di Wang, Lijie Hu  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12298  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12298v1.pdf

**Abstract**:
> arXiv:2603.12298v1 Announce Type: new 
Abstract: Activation engineering enables precise control over Large Language Models (LLMs) without the computational cost of fine-tuning. However, existing methods deriving vectors from static activation differences are susceptible to high-dimensional noise and layer-wise semantic drift, often capturing spurious correlations rather than the target intent. To address this, we propose Global Evolutionary Refined Steering (GER-steer), a training-free framework that grounded in the geometric stability of the network's representation evolution. GER-steer exploits this global signal to rectify raw steering vectors, effectively decoupling robust semantic intent from orthogonal artifacts. Extensive evaluations confirm that GER-steer consistently outperforms b...

---

## 18. A Geometrically-Grounded Drive for MDL-Based Optimization in Deep Learning

**Authors**: Ming Lei, Shufan Wu, Christophe Baehr  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12304  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12304v1.pdf

**Abstract**:
> arXiv:2603.12304v1 Announce Type: new 
Abstract: This paper introduces a novel optimization framework that fundamentally integrates the Minimum Description Length (MDL) principle into the training dynamics of deep neural networks. Moving beyond its conventional role as a model selection criterion, we reformulate MDL as an active, adaptive driving force within the optimization process itself. The core of our method is a geometrically-grounded cognitive manifold whose evolution is governed by a \textit{coupled Ricci flow}, enriched with a novel \textit{MDL Drive} term derived from first principles. This drive, modulated by the task-loss gradient, creates a seamless harmony between data fidelity and model simplification, actively compressing the internal representation during training. We est...

---

## 19. HCP-DCNet: A Hierarchical Causal Primitive Dynamic Composition Network for Self-Improving Causal Understanding

**Authors**: Ming Lei, Shufan Wu, Christophe Baehr  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12305  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12305v1.pdf

**Abstract**:
> arXiv:2603.12305v1 Announce Type: new 
Abstract: The ability to understand and reason about cause and effect -- encompassing interventions, counterfactuals, and underlying mechanisms -- is a cornerstone of robust artificial intelligence. While deep learning excels at pattern recognition, it fundamentally lacks a model of causality, making systems brittle under distribution shifts and unable to answer ``what-if'' questions. This paper introduces the \emph{Hierarchical Causal Primitive Dynamic Composition Network (HCP-DCNet)}, a unified framework that bridges continuous physical dynamics with discrete symbolic causal inference. Departing from monolithic representations, HCP-DCNet decomposes causal scenes into reusable, typed \emph{causal primitives} organized into four abstraction layers: ph...

---

## 20. Thermodynamics of Reinforcement Learning Curricula

**Authors**: Jacob Adamczyk, Juan Sebastian Rojas, Rahul V. Kulkarni  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12324  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12324v1.pdf

**Abstract**:
> arXiv:2603.12324v1 Announce Type: new 
Abstract: Connections between statistical mechanics and machine learning have repeatedly proven fruitful, providing insight into optimization, generalization, and representation learning. In this work, we follow this tradition by leveraging results from non-equilibrium thermodynamics to formalize curriculum learning in reinforcement learning (RL). In particular, we propose a geometric framework for RL by interpreting reward parameters as coordinates on a task manifold. We show that, by minimizing the excess thermodynamic work, optimal curricula correspond to geodesics in this task space. As an application of this framework, we provide an algorithm, "MEW" (Minimum Excess Work), to derive a principled schedule for temperature annealing in maximum-entrop...

---

## 21. Budget-Sensitive Discovery Scoring: A Formally Verified Framework for Evaluating AI-Guided Scientific Selection

**Authors**: Abhinaba Basu, Pavan Chakraborty  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12349  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12349v1.pdf

**Abstract**:
> arXiv:2603.12349v1 Announce Type: new 
Abstract: Scientific discovery increasingly relies on AI systems to select candidates for expensive experimental validation, yet no principled, budget-aware evaluation framework exists for comparing selection strategies -- a gap intensified by large language models (LLMs), which generate plausible scientific proposals without reliable downstream evaluation. We introduce the Budget-Sensitive Discovery Score (BSDS), a formally verified metric -- 20 theorems machine-checked by the Lean 4 proof assistant -- that jointly penalizes false discoveries (lambda-weighted FDR) and excessive abstention (gamma-weighted coverage gap) at each budget level. Its budget-averaged form, the Discovery Quality Score (DQS), provides a single summary statistic that no propose...

---

## 22. Bases of Steerable Kernels for Equivariant CNNs: From 2D Rotations to the Lorentz Group

**Authors**: Alan Garbarz  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12459  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12459v1.pdf

**Abstract**:
> arXiv:2603.12459v1 Announce Type: new 
Abstract: We present an alternative way of solving the steerable kernel constraint that appears in the design of steerable equivariant convolutional neural networks. We find explicit real and complex bases which are ready to use, for different symmetry groups and for feature maps of arbitrary tensor type. A major advantage of this method is that it bypasses the need to numerically or analytically compute Clebsch-Gordan coefficients and works directly with the representations of the input and output feature maps. The strategy is to find a basis of kernels that respect a simpler invariance condition at some point $x_0$, and then \textit{steer} it with the defining equation of steerability to move to some arbitrary point $x=g\cdot x_0$. This idea has alr...

---

## 23. As Language Models Scale, Low-order Linear Depth Dynamics Emerge

**Authors**: Buddhika Nettasinghe, Geethu Joseph  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12541  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12541v1.pdf

**Abstract**:
> arXiv:2603.12541v1 Announce Type: new 
Abstract: Large language models are often viewed as high-dimensional nonlinear systems and treated as black boxes. Here, we show that transformer depth dynamics admit accurate low-order linear surrogates within context. Across tasks including toxicity, irony, hate speech and sentiment, a 32-dimensional linear surrogate reproduces the layerwise sensitivity profile of GPT-2-large with near-perfect agreement, capturing how the final output shifts under additive injections at each layer. We then uncover a surprising scaling principle: for a fixed-order linear surrogate, agreement with the full model improves monotonically with model size across the GPT-2 family. This linear surrogate also enables principled multi-layer interventions that require less ener...

---

## 24. Deep Distance Measurement Method for Unsupervised Multivariate Time Series Similarity Retrieval

**Authors**: Susumu Naito, Kouta Nakata, Yasunori Taguchi  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12544  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12544v1.pdf

**Abstract**:
> arXiv:2603.12544v1 Announce Type: new 
Abstract: We propose the Deep Distance Measurement Method (DDMM) to improve retrieval accuracy in unsupervised multivariate time series similarity retrieval. DDMM enables learning of minute differences within states in the entire time series and thereby recognition of minute differences between states, which are of interest to users in industrial plants. To achieve this, DDMM uses a learning algorithm that assigns a weight to each pair of an anchor and a positive sample, arbitrarily sampled from the entire time series, based on the Euclidean distance within the pair and learns the differences within the pairs weighted by the weights. This algorithm allows both learning minute differences within states and sampling pairs from the entire time series. Ou...

---

## 25. Asymptotic and Finite-Time Guarantees for Langevin-Based Temperature Annealing in InfoNCE

**Authors**: Faris Chaudhry  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12552  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12552v1.pdf

**Abstract**:
> arXiv:2603.12552v1 Announce Type: new 
Abstract: The InfoNCE loss in contrastive learning depends critically on a temperature parameter, yet its dynamics under fixed versus annealed schedules remain poorly understood. We provide a theoretical analysis by modeling embedding evolution under Langevin dynamics on a compact Riemannian manifold. Under mild smoothness and energy-barrier assumptions, we show that classical simulated annealing guarantees extend to this setting: slow logarithmic inverse-temperature schedules ensure convergence in probability to a set of globally optimal representations, while faster schedules risk becoming trapped in suboptimal minima. Our results establish a link between contrastive learning and simulated annealing, providing a principled basis for understanding an...

---

## 26. Lyapunov Stable Graph Neural Flow

**Authors**: Haoyu Chu, Xiaotong Chen, Wei Zhou, Wenjun Cui, Kai Zhao, Shikui Wei, Qiyu Kang  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12557  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12557v1.pdf

**Abstract**:
> arXiv:2603.12557v1 Announce Type: new 
Abstract: Graph Neural Networks (GNNs) are highly vulnerable to adversarial perturbations in both topology and features, making the learning of robust representations a critical challenge. In this work, we bridge GNNs with control theory to introduce a novel defense framework grounded in integer- and fractional-order Lyapunov stability. Unlike conventional strategies that rely on resource-heavy adversarial training or data purification, our approach fundamentally constrains the underlying feature-update dynamics of the GNN. We propose an adaptive, learnable Lyapunov function paired with a novel projection mechanism that maps the network's state into a stable space, thereby offering theoretically provable stability guarantees. Notably, this mechanism i...

---

## 27. A Spectral Revisit of the Distributional Bellman Operator under the Cram\'er Metric

**Authors**: Keru Wang, Yixin Deng, Yao Lyu, Stephen Redmond, Shengbo Eben Li  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12576  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12576v1.pdf

**Abstract**:
> arXiv:2603.12576v1 Announce Type: new 
Abstract: Distributional reinforcement learning (DRL) studies the evolution of full return distributions under Bellman updates rather than focusing on expected values. A classical result is that the distributional Bellman operator is contractive under the Cram\'er metric, which corresponds to an $L^2$ geometry on differences of cumulative distribution functions (CDFs). While this contraction ensures stability of policy evaluation, existing analyses remain largely metric, focusing on contraction properties without elucidating the structural action of the Bellman update on distributions. In this work, we analyse distributional Bellman dynamics directly at the level of CDFs, treating the Cram\'er geometry as the intrinsic analytical setting. At this leve...

---

## 28. Maximizing Incremental Information Entropy for Contrastive Learning

**Authors**: Jiansong Zhang, Zhuoqin Yang, Xu Wu, Xiaoling Luo, Peizhong Liu, Linlin Shen  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12594  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12594v1.pdf

**Abstract**:
> arXiv:2603.12594v1 Announce Type: new 
Abstract: Contrastive learning has achieved remarkable success in self-supervised representation learning, often guided by information-theoretic objectives such as mutual information maximization. Motivated by the limitations of static augmentations and rigid invariance constraints, we propose IE-CL (Incremental-Entropy Contrastive Learning), a framework that explicitly optimizes the entropy gain between augmented views while preserving semantic consistency. Our theoretical framework reframes the challenge by identifying the encoder as an information bottleneck and proposes a joint optimization of two components: a learnable transformation for entropy generation and an encoder regularizer for its preservation. Experiments on CIFAR-10/100, STL-10, and ...

---

## 29. Federated Hierarchical Clustering with Automatic Selection of Optimal Cluster Numbers

**Authors**: Yue Zhang, Chuanlong Qiu, Xinfa Liao, Yiqun Zhang  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12684  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12684v1.pdf

**Abstract**:
> arXiv:2603.12684v1 Announce Type: new 
Abstract: Federated Clustering (FC) is an emerging and promising solution in exploring data distribution patterns from distributed and privacy-protected data in an unsupervised manner. Existing FC methods implicitly rely on the assumption that clients are with a known number of uniformly sized clusters. However, the true number of clusters is typically unknown, and cluster sizes are naturally imbalanced in real scenarios. Furthermore, the privacy-preserving transmission constraints in federated learning inevitably reduce usable information, making the development of robust and accurate FC extremely challenging. Accordingly, we propose a novel FC framework named Fed-$k^*$-HC, which can automatically determine an optimal number of clusters $k^*$ based o...

---

## 30. Residual SODAP: Residual Self-Organizing Domain-Adaptive Prompting with Structural Knowledge Preservation for Continual Learning

**Authors**: Gyutae Oh, Jungwoo Bae, Jitae Shin  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12816  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12816v1.pdf

**Abstract**:
> arXiv:2603.12816v1 Announce Type: new 
Abstract: Continual learning (CL) suffers from catastrophic forgetting, which is exacerbated in domain-incremental learning (DIL) where task identifiers are unavailable and storing past data is infeasible. While prompt-based CL (PCL) adapts representations with a frozen backbone, we observe that prompt-only improvements are often insufficient due to suboptimal prompt selection and classifier-level instability under domain shifts. We propose Residual SODAP, which jointly performs prompt-based representation adaptation and classifier-level knowledge preservation. Our framework combines $\alpha$-entmax sparse prompt selection with residual aggregation, data-free distillation with pseudo-feature replay, prompt-usage--based drift detection, and uncertainty...

---

## 31. SCOPE: Semantic Coreset with Orthogonal Projection Embeddings for Federated learning

**Authors**: Md Anwar Hossen, Nathan R. Tallent, Luanzheng Guo, Ali Jannesary  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12976  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12976v1.pdf

**Abstract**:
> arXiv:2603.12976v1 Announce Type: new 
Abstract: Scientific discovery increasingly requires learning on federated datasets, fed by streams from high-resolution instruments, that have extreme class imbalance. Current ML approaches either require impractical data aggregation or fail due to class imbalance. Existing coreset selection methods rely on local heuristics, making them unaware of the global data landscape and prone to sub-optimal and non-representative pruning. To overcome these challenges, we introduce SCOPE (Semantic Coreset using Orthogonal Projection Embeddings for Federated learning), a coreset framework for federated data that filters anomalies and adaptively prunes redundant data to mitigate long-tail skew. By analyzing the latent space distribution, we score each data point ...

---

## 32. 3DTCR: A Physics-Based Generative Framework for Vortex-Following 3D Reconstruction to Improve Tropical Cyclone Intensity Forecasting

**Authors**: Jun Liu, Xiaohui Zhong, Kai Zheng, Jiarui Li, Yifei Li, Tao Zhou, Wenxu Qian, Shun Dai, Ruian Tie, Y...  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13049  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13049v1.pdf

**Abstract**:
> arXiv:2603.13049v1 Announce Type: new 
Abstract: Tropical cyclone (TC) intensity forecasting remains challenging as current numerical and AI-based weather models fail to satisfactorily represent extreme TC structure and intensity. Although intensity time-series forecasting has achieved significant advances, it outputs intensity sequences rather than the three-dimensional inner-core fine-scale structure and physical mechanisms governing TC evolution. High-resolution numerical simulations can capture these features but remain computationally expensive and inefficient for large-scale operational applications. Here we present 3DTCR, a physics-based generative framework combining physical constraints with generative AI efficiency for 3D TC structure reconstruction. Trained on a six-year, 3-km-r...

---

## 33. Competition-Aware CPC Forecasting with Near-Market Coverage

**Authors**: Sebastian Frey, Edoardo Beccari, Maximilian Kranz, Nicol\`o Alberto Pellizzari, Ali Mete Karaman, Qi...  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13059  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13059v1.pdf

**Abstract**:
> arXiv:2603.13059v1 Announce Type: new 
Abstract: Cost-per-click (CPC) in paid search is a volatile auction outcome generated by a competitive landscape that is only partially observable from any single advertiser's history. Using Google Ads auction logs from a concentrated car-rental market (2021--2023), we forecast weekly CPC for 1,811 keyword series and approximate latent competition through complementary signals derived from keyword text, CPC trajectories, and geographic market structure. We construct (i) semantic neighborhoods and a semantic keyword graph from pretrained transformer-based representations of keyword text, (ii) behavioral neighborhoods via Dynamic Time Warping (DTW) alignment of CPC trajectories, and (iii) geographic-intent covariates capturing localized demand and marke...

---

## 34. GeoChemAD: Benchmarking Unsupervised Geochemical Anomaly Detection for Mineral Exploration

**Authors**: Yihao Ding, Yiran Zhang, Chris Gonzalez, Eun-Jung Holden, Wei Liu  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13068  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13068v1.pdf

**Abstract**:
> arXiv:2603.13068v1 Announce Type: new 
Abstract: Geochemical anomaly detection plays a critical role in mineral exploration as deviations from regional geochemical baselines may indicate mineralization. Existing studies suffer from two key limitations: (1) single region scenarios which limit model generalizability; (2) proprietary datasets, which makes result reproduction unattainable. In this work, we introduce \textbf{GeoChemAD}, an open-source benchmark dataset compiled from government-led geological surveys, covering multiple regions, sampling sources, and target elements. The dataset comprises eight subsets representing diverse spatial scales and sampling conditions. To establish strong baselines, we reproduce and benchmark a range of unsupervised anomaly detection methods, including ...

---

## 35. Representation Learning for Spatiotemporal Physical Systems

**Authors**: Helen Qu, Rudy Morel, Michael McCabe, Alberto Bietti, Fran\c{c}ois Lanusse, Shirley Ho, Yann LeCun  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13227  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13227v1.pdf

**Abstract**:
> arXiv:2603.13227v1 Announce Type: new 
Abstract: Machine learning approaches to spatiotemporal physical systems have primarily focused on next-frame prediction, with the goal of learning an accurate emulator for the system's evolution in time. However, these emulators are computationally expensive to train and are subject to performance pitfalls, such as compounding errors during autoregressive rollout. In this work, we take a different perspective and look at scientific tasks further downstream of predicting the next frame, such as estimation of a system's governing physical parameters. Accuracy on these tasks offers a uniquely quantifiable glimpse into the physical relevance of the representations of these models. We evaluate the effectiveness of general-purpose self-supervised methods i...

---

## 36. Predictive Analytics for Foot Ulcers Using Time-Series Temperature and Pressure Data

**Authors**: Md Tanvir Hasan Turja  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12278  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12278v1.pdf

**Abstract**:
> arXiv:2603.12278v1 Announce Type: cross 
Abstract: Diabetic foot ulcers (DFUs) are a severe complication of diabetes, often resulting in significant morbidity. This paper presents a predictive analytics framework utilizing time-series data captured by wearable foot sensors -- specifically NTC thin-film thermocouples for temperature measurement and FlexiForce pressure sensors for plantar load monitoring. Data was collected from healthy subjects walking on an instrumented pathway. Unsupervised machine learning algorithms, Isolation Forest and K-Nearest Neighbors (KNN), were applied to detect anomalies that may indicate early ulcer risk. Through rigorous data preprocessing and targeted feature engineering, physiologic patterns were extracted to identify subtle changes in foot temperature and ...

---

## 37. Beyond Motion Imitation: Is Human Motion Data Alone Sufficient to Explain Gait Control and Biomechanics?

**Authors**: Xinyi Liu, Jangwhan Ahn, Edgar Lobaton, Jennie Si, He Huang  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12408  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12408v1.pdf

**Abstract**:
> arXiv:2603.12408v1 Announce Type: cross 
Abstract: With the growing interest in motion imitation learning (IL) for human biomechanics and wearable robotics, this study investigates how additional foot-ground interaction measures, used as reward terms, affect human gait kinematics and kinetics estimation within a reinforcement learning-based IL framework. Results indicate that accurate reproduction of forward kinematics alone does not ensure biomechanically plausible joint kinetics. Adding foot-ground contacts and contact forces to the IL reward terms enables the prediction of joint moments in forward walking simulation, which are significantly closer to those computed by inverse dynamics. This finding highlights a fundamental limitation of motion-only IL approaches, which may prioritize ki...

---

## 38. Revisiting Model Stitching In the Foundation Model Era

**Authors**: Zheda Mai, Ke Zhang, Fu-En Wang, Zixiao Ken Wang, Albert Y. C. Chen, Lu Xia, Min Sun, Wei-Lun Chao, ...  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12433  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12433v1.pdf

**Abstract**:
> arXiv:2603.12433v1 Announce Type: cross 
Abstract: Model stitching, connecting early layers of one model (source) to later layers of another (target) via a light stitch layer, has served as a probe of representational compatibility. Prior work finds that models trained on the same dataset remain stitchable (negligible accuracy drop) despite different initializations or objectives. We revisit stitching for Vision Foundation Models (VFMs) that vary in objectives, data, and modality mix (e.g., CLIP, DINOv2, SigLIP 2) and ask: Are heterogeneous VFMs stitchable? We introduce a systematic protocol spanning the stitch points, stitch layer families, training losses, and downstream tasks. Three findings emerge. (1) Stitch layer training matters: conventional approaches that match the intermediate f...

---

## 39. Unmasking Biases and Reliability Concerns in Convolutional Neural Networks Analysis of Cancer Pathology Images

**Authors**: Michael Okonoda, Eder Martinez, Abhilekha Dalal, Lior Shamir  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12445  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12445v1.pdf

**Abstract**:
> arXiv:2603.12445v1 Announce Type: cross 
Abstract: Convolutional Neural Networks have shown promising effectiveness in identifying different types of cancer from radiographs. However, the opaque nature of CNNs makes it difficult to fully understand the way they operate, limiting their assessment to empirical evaluation. Here we study the soundness of the standard practices by which CNNs are evaluated for the purpose of cancer pathology. Thirteen highly used cancer benchmark datasets were analyzed, using four common CNN architectures and different types of cancer, such as melanoma, carcinoma, colorectal cancer, and lung cancer. We compared the accuracy of each model with that of datasets made of cropped segments from the background of the original images that do not contain clinically relev...

---

## 40. FloeNet: A mass-conserving global sea ice emulator that generalizes across climates

**Authors**: William Gregory, Mitchell Bushuk, James Duncan, Elynn Wu, Adam Subel, Spencer K. Clark, Bill Hurlin,...  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12449  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12449v1.pdf

**Abstract**:
> arXiv:2603.12449v1 Announce Type: cross 
Abstract: We introduce FloeNet, a machine-learning emulator trained on the Geophysical Fluid Dynamics Laboratory global sea ice model, SIS2. FloeNet is a mass-conserving model, emulating 6-hour mass and area budget tendencies related to sea ice and snow-on-sea-ice growth, melt, and advection. We train FloeNet using simulated data from a reanalysis-forced ice-ocean simulation and test its ability to generalize to pre-industrial control and 1% CO2 climates. FloeNet outperforms a non-conservative model at reproducing sea ice and snow-on-sea-ice mean state, trends, and inter-annual variability, with volume anomaly correlations above 0.96 in the Antarctic and 0.76 in the Arctic, across all forcings. FloeNet also produces the correct thermodynamic vs dyna...

---

## 41. Addressing Data Scarcity in 3D Trauma Detection through Self-Supervised and Semi-Supervised Learning with Vertex Relative Position Encoding

**Authors**: Shivam Chaudhary, Sheethal Bhat, Andreas Maier  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12514  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12514v1.pdf

**Abstract**:
> arXiv:2603.12514v1 Announce Type: cross 
Abstract: Accurate detection and localization of traumatic injuries in abdominal CT scans remains a critical challenge in emergency radiology, primarily due to severe scarcity of annotated medical data. This paper presents a label-efficient approach combining self-supervised pre-training with semi-supervised detection for 3D medical image analysis. We employ patch-based Masked Image Modeling (MIM) to pre-train a 3D U-Net encoder on 1,206 CT volumes without annotations, learning robust anatomical representations. The pretrained encoder enables two downstream clinical tasks: 3D injury detection using VDETR with Vertex Relative Position Encoding, and multi-label injury classification. For detection, semi-supervised learning with 2,000 unlabeled volumes...

---

## 42. Deferred is Better: A Framework for Multi-Granularity Deferred Interaction of Heterogeneous Features

**Authors**: Yi Xu, Moyu Zhang, Chaofan Fan, Jinxin Hu, Yu Zhang, Xiaoyi Zeng  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12586  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12586v1.pdf

**Abstract**:
> arXiv:2603.12586v1 Announce Type: cross 
Abstract: Click-through rate (CTR) prediction models estimates the probability of a user-item click by modeling interactions across a vast feature space. A fundamental yet often overlooked challenge is the inherent heterogeneity of these features: their sparsity and information content vary dramatically. For instance, categorical features like item IDs are extremely sparse, whereas numerical features like item price are relatively dense. Prevailing CTR models have largely ignored this heterogeneity, employing a uniform feature interaction strategy that inputs all features into the interaction layers simultaneously. This approach is suboptimal, as the premature introduction of low-information features can inject significant noise and mask the signals...

---

## 43. Anchored Alignment: Preventing Positional Collapse in Multimodal Recommender Systems

**Authors**: Yonghun Jeong, David Yoon Suk Kang, Yeon-Chang Lee  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12726  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12726v1.pdf

**Abstract**:
> arXiv:2603.12726v1 Announce Type: cross 
Abstract: Multimodal recommender systems (MMRS) leverage images, text, and interaction signals to enrich item representations. However, recent alignment based MMRSs that enforce a unified embedding space often blur modality specific structures and exacerbate ID dominance. Therefore, we propose AnchorRec, a multimodal recommendation framework that performs indirect, anchor based alignment in a lightweight projection domain. By decoupling alignment from representation learning, AnchorRec preserves each modality's native structure while maintaining cross modal consistency and avoiding positional collapse. Experiments on four Amazon datasets show that AnchorRec achieves competitive top N recommendation accuracy, while qualitative analyses demonstrate im...

---

## 44. VecMol: Vector-Field Representations for 3D Molecule Generation

**Authors**: Yuchen Hua, Xingang Peng, Jianzhu Ma, Muhan Zhang  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12734  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12734v1.pdf

**Abstract**:
> arXiv:2603.12734v1 Announce Type: cross 
Abstract: Generative modeling of three-dimensional (3D) molecules is a fundamental yet challenging problem in drug discovery and materials science. Existing approaches typically represent molecules as 3D graphs and co-generate discrete atom types with continuous atomic coordinates, leading to intrinsic learning difficulties such as heterogeneous modality entanglement and geometry-chemistry coherence constraints. We propose VecMol, a paradigm-shifting framework that reimagines molecular representation by modeling 3D molecules as continuous vector fields over Euclidean space, where vectors point toward nearby atoms and implicitly encode molecular structure. The vector field is parameterized by a neural field and generated using a latent diffusion mode...

---

## 45. Show, Don't Tell: Detecting Novel Objects by Watching Human Videos

**Authors**: James Akl, Jose Nicolas Avendano Arbelaez, James Barabas, Jennifer L. Barry, Kalie Ching, Noam Eshed...  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12751  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12751v1.pdf

**Abstract**:
> arXiv:2603.12751v1 Announce Type: cross 
Abstract: How can a robot quickly identify and recognize new objects shown to it during a human demonstration? Existing closed-set object detectors frequently fail at this because the objects are out-of-distribution. While open-set detectors (e.g., VLMs) sometimes succeed, they often require expensive and tedious human-in-the-loop prompt engineering to uniquely recognize novel object instances. In this paper, we present a self-supervised system that eliminates the need for tedious language descriptions and expensive prompt engineering by training a bespoke object detector on an automatically created dataset, supervised by the human demonstration itself. In our approach, "Show, Don't Tell," we show the detector the specific objects of interest during...

---

## 46. TerraFlow: Multimodal, Multitemporal Representation Learning for Earth Observation

**Authors**: Nazar Puriy, Johannes Jakubik, Benedikt Blumenstiel, Konrad Schindler  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12762  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12762v1.pdf

**Abstract**:
> arXiv:2603.12762v1 Announce Type: cross 
Abstract: We propose TerraFlow, a novel approach to multimodal, multitemporal learning for Earth observation. TerraFlow builds on temporal training objectives that enable sequence-aware learning across space, time, and modality, while remaining robust to the variable-length inputs commonly encountered in real-world Earth observation data. Our experiments demonstrate superiority of TerraFlow over state-of-the-art foundation models for Earth observation across all temporal tasks of the GEO-Bench-2 benchmark. We additionally demonstrate that TerraFlow is able to make initial steps towards deep-learning based risk map prediction for natural disasters -- a task on which other state-of-the-art foundation models frequently collapse. TerraFlow outperforms s...

---

## 47. PVI: Plug-in Visual Injection for Vision-Language-Action Models

**Authors**: Zezhou Zhang, Songxin Zhang, Xiao Xiong, Junjie Zhang, Zejian Xie, Jingyi Xi, Zunyao Mao, Zan Mao, Z...  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12772  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12772v1.pdf

**Abstract**:
> arXiv:2603.12772v1 Announce Type: cross 
Abstract: VLA architectures that pair a pretrained VLM with a flow-matching action expert have emerged as a strong paradigm for language-conditioned manipulation. Yet the VLM, optimized for semantic abstraction and typically conditioned on static visual observations, tends to attenuate fine-grained geometric cues and often lacks explicit temporal evidence for the action expert. Prior work mitigates this by injecting auxiliary visual features, but existing approaches either focus on static spatial representations or require substantial architectural modifications to accommodate temporal inputs, leaving temporal information underexplored. We propose Plug-in Visual Injection (PVI), a lightweight, encoder-agnostic module that attaches to a pretrained ac...

---

## 48. Towards Faithful Multimodal Concept Bottleneck Models

**Authors**: Pierre Moreau, Emeline Pineau Ferrand, Yann Choho, Benjamin Wong, Annabelle Blangero, Milan Bhan  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13163  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13163v1.pdf

**Abstract**:
> arXiv:2603.13163v1 Announce Type: cross 
Abstract: Concept Bottleneck Models (CBMs) are interpretable models that route predictions through a layer of human-interpretable concepts. While widely studied in vision and, more recently, in NLP, CBMs remain largely unexplored in multimodal settings. For their explanations to be faithful, CBMs must satisfy two conditions: concepts must be properly detected, and concept representations must encode only their intended semantics, without smuggling extraneous task-relevant or inter-concept information into final predictions, a phenomenon known as leakage. Existing approaches treat concept detection and leakage mitigation as separate problems, and typically improve one at the expense of predictive accuracy. In this work, we introduce f-CBM, a faithful...

---

## 49. Sampling and Uniqueness Sets in Graphon Signal Processing

**Authors**: Alejandro Parada-Mayorga, Alejandro Ribeiro  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2401.06279  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2401.06279v3.pdf

**Abstract**:
> arXiv:2401.06279v3 Announce Type: replace 
Abstract: In this work, we study the properties of sampling sets on families of large graphs by leveraging the theory of graphons and graph limits. To this end, we extend to graphon signals the notion of removable and uniqueness sets, which was developed originally for the analysis of signals on graphs. We state the formal definition of a $\Lambda-$removable set and conditions under which a bandlimited graphon signal can be represented in a unique way when its samples are obtained from the complement of a given $\Lambda-$removable set in the graphon. By leveraging such results we show that graphon representations of graphs and graph signals can be used as a common framework to compare sampling sets between graphs with different numbers of nodes an...

---

## 50. Causality Is Key to Understand and Balance Multiple Goals in Trustworthy ML and Foundation Models

**Authors**: Ruta Binkyte, Ivaxi Sheth, Zhijing Jin, Mohammad Havaei, Bernhard Sch\"olkopf, Mario Fritz  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2502.21123  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2502.21123v5.pdf

**Abstract**:
> arXiv:2502.21123v5 Announce Type: replace 
Abstract: Ensuring trustworthiness in machine learning (ML) systems is crucial as they become increasingly embedded in high-stakes domains. This paper advocates for integrating causal methods into machine learning to navigate the trade-offs among key principles of trustworthy ML, including fairness, privacy, robustness, accuracy, and explainability. While these objectives should ideally be satisfied simultaneously, they are often addressed in isolation, leading to conflicts and suboptimal solutions. Drawing on existing applications of causality in ML that successfully align goals such as fairness and accuracy or privacy and robustness, this paper argues that a causal approach is essential for balancing multiple competing objectives in both trustwo...

---

## 51. Unsupervised anomaly detection in MeV ultrafast electron diffraction

**Authors**: Mariana A. Fazio, Manel Martinez-Ramon, Salvador Sosa G\"uitron, Marcus Babzien, Mikhail Fedurin, Ju...  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2505.13702  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2505.13702v2.pdf

**Abstract**:
> arXiv:2505.13702v2 Announce Type: replace 
Abstract: MeV ultrafast electron diffraction (MUED) is a pump-probe technique used to study the dynamic structural evolution of materials. An ultrashort laser pulse triggers structural changes, which are then probed by an ultrashort relativistic electron beam. To overcome low signal-to-noise ratios, diffraction patterns are averaged over thousands of shots. However, shot-to-shot instabilities in the electron beam can distort individual patterns, introducing uncertainty. Improving MUED accuracy requires detecting and removing these anomalous patterns from large datasets. In this work, we developed a fully unsupervised methodology for the detection of anomalous diffraction patterns. Using a convolutional autoencoder, we calculate the reconstruction ...

---

## 52. Backward Oversmoothing: why is it hard to train deep Graph Neural Networks?

**Authors**: Nicolas Keriven  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2505.16736  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2505.16736v2.pdf

**Abstract**:
> arXiv:2505.16736v2 Announce Type: replace 
Abstract: Oversmoothing has long been identified as a major limitation of Graph Neural Networks (GNNs): input node features are smoothed at each layer and converge to a non-informative representation, if the weights of the GNN are sufficiently bounded. This assumption is crucial: if, on the contrary, the weights are sufficiently large, then oversmoothing may not happen. Theoretically, GNN could thus learn to not oversmooth. However it does not really happen in practice, which prompts us to examine oversmoothing from an optimization point of view. In this paper, we analyze backward oversmoothing, that is, the notion that backpropagated errors used to compute gradients are also subject to oversmoothing from output to input. With non-linear activatio...

---

## 53. Accelerating Diffusion Model Training under Minimal Budgets: A Condensation-Based Perspective

**Authors**: Rui Huang, Shitong Shao, Zikai Zhou, Pukun Zhao, Hangyu Guo, Tian Ye, Lichen Bai, Shuo Yang, Zeke Xi...  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2507.05914  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2507.05914v3.pdf

**Abstract**:
> arXiv:2507.05914v3 Announce Type: replace 
Abstract: Diffusion models have achieved remarkable performance on a wide range of generative tasks, yet training them from scratch is notoriously resource-intensive, typically requiring millions of training images and many GPU days. Motivated by a data-centric view of this bottleneck, we adopt a condensation-based perspective: given a large training set, the goal is to construct a much smaller condensed dataset that still supports training strong diffusion models under minimal data and compute budgets. To operationalize this perspective, we introduce Diffusion Dataset Condensation (D2C), a two-phase framework comprising Select and Attach. In the Select phase, a diffusion difficulty score combined with interval sampling is used to identify a compa...

---

## 54. Invariant Graph Transformer for Out-of-Distribution Generalization

**Authors**: Tianyin Liao, Ziwei Zhang, Yufei Sun, Chunyu Hu, Jianxin Li  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2508.00304  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2508.00304v2.pdf

**Abstract**:
> arXiv:2508.00304v2 Announce Type: replace 
Abstract: Graph Transformers (GTs) have demonstrated great effectiveness across various graph analytical tasks. However, the existing GTs focus on training and testing graph data originated from the same distribution, but fail to generalize under distribution shifts. Graph invariant learning, aiming to capture generalizable graph structural patterns with labels under distribution shifts, is potentially a promising solution, but how to design attention mechanisms and positional and structural encodings (PSEs) based on graph invariant learning principles remains challenging. To solve these challenges, we introduce Graph Out-Of-Distribution generalized Transformer (GOODFormer), aiming to learn generalized graph representations by capturing invariant ...

---

## 55. ASTGI: Adaptive Spatio-Temporal Graph Interactions for Irregular Multivariate Time Series Forecasting

**Authors**: Xvyuan Liu, Xiangfei Qiu, Hanyin Cheng, Xingjian Wu, Chenjuan Guo, Bin Yang, Jilin Hu  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2509.23313  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2509.23313v3.pdf

**Abstract**:
> arXiv:2509.23313v3 Announce Type: replace 
Abstract: Irregular multivariate time series (IMTS) are prevalent in critical domains like healthcare and finance, where accurate forecasting is vital for proactive decision-making. However, the asynchronous sampling and irregular intervals inherent to IMTS pose two core challenges for existing methods: (1) how to accurately represent the raw information of irregular time series without introducing data distortion, and (2) how to effectively capture the complex dynamic dependencies between observation points. To address these challenges, we propose the Adaptive Spatio-Temporal Graph Interaction (ASTGI) framework. Specifically, the framework first employs a Spatio-Temporal Point Representation module to encode each discrete observation as a point w...

---

## 56. Language Models are Injective and Hence Invertible

**Authors**: Giorgos Nikolaou, Tommaso Mencattini, Donato Crisostomi, Andrea Santilli, Yannis Panagakis, Emanuele...  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.15511  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.15511v4.pdf

**Abstract**:
> arXiv:2510.15511v4 Announce Type: replace 
Abstract: Transformer components such as non-linear activations and normalization are inherently non-injective, suggesting that different inputs could map to the same output and prevent exact recovery of the input from a model's representations. In this paper, we challenge this view. First, we prove mathematically that transformer language models mapping discrete input sequences to their corresponding sequence of continuous representations are injective and therefore lossless, a property established at initialization and preserved during training. Second, we confirm this result empirically through billions of collision tests on six state-of-the-art language models, and observe no collisions. Third, we operationalize injectivity: we introduce SipIt...

---

## 57. NeuCo-Bench: A Novel Benchmark Framework for Neural Embeddings in Earth Observation

**Authors**: Rikard Vinge, Isabelle Wittmann, Jannik Schneider, Michael Marszalek, Luis Gilch, Thomas Brunschwile...  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.17914  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.17914v2.pdf

**Abstract**:
> arXiv:2510.17914v2 Announce Type: replace 
Abstract: We introduce NeuCo-Bench, a novel benchmark framework for evaluating (lossy) neural compression and representation learning in the context of Earth Observation (EO). Our approach builds on fixed-size embeddings that act as compact, task-agnostic representations applicable to a broad range of downstream tasks. NeuCo-Bench comprises three components: (i) an evaluation pipeline built around embeddings, (ii) a challenge mode with a hidden-task leaderboard designed to mitigate pretraining bias, and (iii) a scoring system that balances accuracy and stability. To support reproducibility, we release SSL4EO-S12-downstream, a curated multispectral, multitemporal EO dataset. We present results from a public challenge at the 2025 CVPR EARTHVISION wo...

---

## 58. LLM Unlearning with LLM Beliefs

**Authors**: Kemou Li, Qizhou Wang, Yue Wang, Fengpeng Li, Jun Liu, Bo Han, Jiantao Zhou  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.19422  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.19422v2.pdf

**Abstract**:
> arXiv:2510.19422v2 Announce Type: replace 
Abstract: Large language models trained on vast corpora inherently risk memorizing sensitive or harmful content, which may later resurface in their outputs. Prevailing unlearning methods generally rely on gradient ascent and its variants to lower the probability of specific target responses. However, we find that this strategy induces a critical side effect: probability mass is redistributed into high-likelihood regions, often corresponding to semantically related rephrasings of the targets. We refer to this as the squeezing effect, which explains why many methods yield merely spurious unlearning, a problem further obscured by automated metrics (e.g., ROUGE, truth ratio) that misreport actual success. To address this, we propose a bootstrapping (B...

---

## 59. Structural Incompatibility of Differentiable Sorting and Within-Vector Rank Normalization

**Authors**: Taeyun Kim  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2512.22587  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2512.22587v2.pdf

**Abstract**:
> arXiv:2512.22587v2 Announce Type: replace 
Abstract: We show that differentiable sorting and ranking operators are structurally incompatible with within-vector rank normalization. We formalize admissibility through monotone invariance (C1), batch independence (C2), and a rank-space stability condition (C3). Gap-sensitive relaxations such as SoftSort violate (C1) by a quantitative margin that depends on the temperature and input scale. Batchwise rank relaxations such as SinkhornSort violate (C2): the same sample can be assigned outputs arbitrarily close to 0 or 1 depending solely on batch context. Condition (C3) implies (C1) under the rank representation used here and should not be read as a third independent failure mode. We also characterize the admissible class: any admissible operator m...

---

## 60. From Activation to Initialization: Scaling Insights for Optimizing Neural Fields

**Authors**: Hemanth Saratchandran, Sameera Ramasinghe, Simon Lucey  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2403.19205  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2403.19205v2.pdf

**Abstract**:
> arXiv:2403.19205v2 Announce Type: replace-cross 
Abstract: In the realm of computer vision, Neural Fields have gained prominence as a contemporary tool harnessing neural networks for signal representation. Despite the remarkable progress in adapting these networks to solve a variety of problems, the field still lacks a comprehensive theoretical framework. This article aims to address this gap by delving into the intricate interplay between initialization and activation, providing a foundational basis for the robust optimization of Neural Fields. Our theoretical insights reveal a deep-seated connection among network initialization, architectural choices, and the optimization process, emphasizing the need for a holistic approach when designing cutting-edge Neural Fields.

---

## 61. Latent diffusion models for parameterization and data assimilation of facies-based geomodels

**Authors**: Guido Di Federico, Louis J. Durlofsky  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2406.14815  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2406.14815v5.pdf

**Abstract**:
> arXiv:2406.14815v5 Announce Type: replace-cross 
Abstract: Geological parameterization entails the representation of a geomodel using a small set of latent variables and a mapping from these variables to grid-block properties such as porosity and permeability. Parameterization is useful for data assimilation (history matching), as it maintains geological realism while reducing the number of variables to be determined. Diffusion models are a new class of generative deep-learning procedures that have been shown to outperform previous methods, such as generative adversarial networks, for image generation tasks. Diffusion models are trained to "denoise", which enables them to generate new geological realizations from input fields characterized by random noise. Latent diffusion models, which ar...

---

## 62. Token Distillation: Attention-aware Input Embeddings For New Tokens

**Authors**: Konstantin Dobler, Desmond Elliott, Gerard de Melo  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2505.20133  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2505.20133v3.pdf

**Abstract**:
> arXiv:2505.20133v3 Announce Type: replace-cross 
Abstract: Current language models rely on static vocabularies determined at pretraining time, which can lead to decreased performance and increased computational cost for domains underrepresented in the original vocabulary. New tokens can be added to solve this problem, when coupled with a good initialization for their new embeddings. However, existing embedding initialization methods require expensive further training or pretraining of additional modules. In this paper, we propose Token Distillation and show that by distilling representations obtained using the original tokenization, we can quickly learn high-quality input embeddings for new tokens. Experimental results with a wide range of open-weight models show that Token Distillation ou...

---

## 63. From Video to EEG: Adapting Joint Embedding Predictive Architecture to Uncover Saptiotemporal Dynamics in Brain Signal Analysis

**Authors**: Amirabbas Hojjati, Lu Li, Ibrahim Hameed, Anis Yazidi, Pedro G. Lind, Rabindra Khadka  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2507.03633  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2507.03633v5.pdf

**Abstract**:
> arXiv:2507.03633v5 Announce Type: replace-cross 
Abstract: EEG signals capture brain activity with high temporal and low spatial resolution, supporting applications such as neurological diagnosis, cognitive monitoring, and brain-computer interfaces. However, effective analysis is hindered by limited labeled data, high dimensionality, and the absence of scalable models that fully capture spatiotemporal dependencies. Existing self-supervised learning (SSL) methods often focus on either spatial or temporal features, leading to suboptimal representations. To this end, we propose EEG-VJEPA, a novel adaptation of the Video Joint Embedding Predictive Architecture (V-JEPA) for EEG classification. By treating EEG as video-like sequences, EEG-VJEPA learns semantically meaningful spatiotemporal repre...

---

## 64. Quantum-Informed Machine Learning for Predicting Spatiotemporal Chaos with Practical Quantum Advantage

**Authors**: Maida Wang, Xiao Xue, Mingyang Gao, Peter V. Coveney  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2507.19861  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2507.19861v5.pdf

**Abstract**:
> arXiv:2507.19861v5 Announce Type: replace-cross 
Abstract: We introduce a quantum-informed machine learning (QIML) framework for modelling the long-term behaviour of high-dimensional chaotic systems. QIML combines a one-time, offline-trained quantum generative model with a classical autoregressive predictor for spatiotemporal field generation. The quantum model learns a quantum prior (Q-Prior) that guides the representation of small-scale interactions and improves the modelling of fine-scale dynamics. We evaluate QIML on the Kuramoto-Sivashinsky equation, two-dimensional Kolmogorov flow, and the three-dimensional turbulent channel flow used as a realistic inflow condition. Across these systems, QIML improves predictive distribution accuracy by up to 17.25% and full-spectrum fidelity by up ...

---

## 65. SegDAC: Visual Generalization in Reinforcement Learning via Dynamic Object Tokens

**Authors**: Alexandre Brown, Glen Berseth  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2508.09325  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2508.09325v4.pdf

**Abstract**:
> arXiv:2508.09325v4 Announce Type: replace-cross 
Abstract: Visual reinforcement learning policies trained on pixel observations often struggle to generalize when visual conditions change at test time. Object-centric representations are a promising alternative, but most approaches use fixed-size slot representations, require image reconstruction, or need auxiliary losses to learn object decompositions. As a result, it remains unclear how to learn RL policies directly from object-level inputs without these constraints. We propose SegDAC, a Segmentation-Driven Actor-Critic that operates on a variable-length set of object token embeddings. At each timestep, text-grounded segmentation produces object masks from which spatially aware token embeddings are extracted. A transformer-based actor-crit...

---

## 66. The causal structure of galactic astrophysics

**Authors**: Harry Desmond, Joseph Ramsey  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.01112  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.01112v3.pdf

**Abstract**:
> arXiv:2510.01112v3 Announce Type: replace-cross 
Abstract: Data-driven astrophysics currently relies on the detection and characterisation of correlations between objects' properties, which are then used to test physical theories that make predictions for them. This process fails to utilise information in the data that forms a crucial part of the theories' predictions, namely which variables are directly correlated (as opposed to accidentally correlated through others), the directions of these determinations, and the presence or absence of confounders that correlate variables in the dataset but are themselves absent from it. We propose to recover this information through causal discovery, a well-developed methodology for inferring the causal structure of datasets that is however almost ent...

---

## 67. LatentChem: From Textual CoT to Latent Thinking in Chemical Reasoning

**Authors**: Xinwu Ye, Yicheng Mao, Jia Zhang, Yimeng Liu, Li Hao, Fang Wu, Zhiwei Li, Yuxuan Liao, Zehong Wang, ...  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.07075  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.07075v4.pdf

**Abstract**:
> arXiv:2602.07075v4 Announce Type: replace-cross 
Abstract: Chemical large language models (LLMs) predominantly rely on explicit Chain-of-Thought (CoT) in natural language to perform complex reasoning. However, chemical reasoning is inherently continuous and structural, and forcing it into discrete linguistic tokens introduces a fundamental representation mismatch that constrains both efficiency and performance. We introduce LatentChem, a latent reasoning interface that decouples chemical computation from textual generation, enabling models to perform multi-step reasoning directly in continuous latent space while emitting language only for final outputs. Remarkably, we observe a consistent emergent behavior: when optimized solely for task success, models spontaneously internalize reasoning,...

---

## 68. One Supervisor, Many Modalities: Adaptive Tool Orchestration for Autonomous Queries

**Authors**: Mayank Saini, Arit Kumar Bishwas  
**Categories**: cs.LG  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11545  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11545v2.pdf

**Abstract**:
> arXiv:2603.11545v2 Announce Type: replace-cross 
Abstract: We present an agentic AI framework for autonomous multimodal query processing that coordinates specialized tools across text, image, audio, video, and document modalities. A central Supervisor dynamically decomposes user queries, delegates subtasks to modality-appropriate tools (e.g., object detection, OCR, speech transcription), and synthesizes results through adaptive routing strategies rather than predetermined decision trees. For text-only queries, the framework uses learned routing via RouteLLM, while non-text paths use SLM-assisted modality decomposition. Evaluated on 2,847 queries across 15 task categories, our framework achieves 72% reduction in time-to-accurate-answer, 85% reduction in conversational rework, and 67% cost r...

---

## 69. Context-Enriched Natural Language Descriptions of Vessel Trajectories

**Authors**: Kostas Patroumpas, Alexandros Troupiotis-Kapeliaris, Giannis Spiliopoulos, Panagiotis Betchavas, Dim...  
**Categories**: cs.AI  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12287  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12287v1.pdf

**Abstract**:
> arXiv:2603.12287v1 Announce Type: new 
Abstract: We address the problem of transforming raw vessel trajectory data collected from AIS into structured and semantically enriched representations interpretable by humans and directly usable by machine reasoning systems. We propose a context-aware trajectory abstraction framework that segments noisy AIS sequences into distinct trips each consisting of clean, mobility-annotated episodes. Each episode is further enriched with multi-source contextual information, such as nearby geographic entities, offshore navigation features, and weather conditions. Crucially, such representations can support generation of controlled natural language descriptions using LLMs. We empirically examine the quality of such descriptions generated using several LLMs over...

---

## 70. Task-Specific Knowledge Distillation via Intermediate Probes

**Authors**: Ryan Brown, Chris Russell  
**Categories**: cs.AI  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12270  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12270v1.pdf

**Abstract**:
> arXiv:2603.12270v1 Announce Type: cross 
Abstract: Knowledge distillation from large language models (LLMs) assumes that the teacher's output distribution is a high-quality training signal. On reasoning tasks, this assumption is frequently violated. A model's intermediate representations may encode the correct answer, yet this information is lost or distorted through the vocabulary projection, where prompt formatting and answer-token choices creates brittle, noisy outputs.
  We introduce \method{}, a distillation framework that bypasses this bottleneck by training lightweight probes on frozen teacher hidden states and using the probe's predictions, rather than output logits, as supervision for student training. This simple change yields consistent improvements across four reasoning benchma...

---

## 71. The DIME Architecture: A Unified Operational Algorithm for Neural Representation, Dynamics, Control and Integration

**Authors**: Ionel Cristian Vladu, Nicu Bizdoaca, Ionica Pirici, Tudor-Adrian Balseanu, Eduard Nicusor Bondoc  
**Categories**: cs.AI  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12286  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12286v1.pdf

**Abstract**:
> arXiv:2603.12286v1 Announce Type: cross 
Abstract: Modern neuroscience has accumulated extensive evidence on perception, memory, prediction, valuation, and consciousness, yet still lacks an explicit operational architecture capable of integrating these phenomena within a unified computational framework. Existing theories address specific aspects of neural function: predictive coding and active inference emphasize hierarchical inference and prediction error minimization; engram theories explain memory through distributed cell assemblies; neuromodulatory accounts focus on value-dependent regulation of plasticity and behaviour; and global workspace or large-scale network models investigate mechanisms underlying conscious access. Despite their explanatory power, these approaches remain only pa...

---

## 72. Optimizing Task Completion Time Updates Using POMDPs

**Authors**: Duncan Eddy, Esen Yel, Emma Passmore, Niles Egan, Grayson Armour, Dylan M. Asmar, Mykel J. Kochender...  
**Categories**: cs.AI  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12340  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12340v1.pdf

**Abstract**:
> arXiv:2603.12340v1 Announce Type: cross 
Abstract: Managing announced task completion times is a fundamental control problem in project management. While extensive research exists on estimating task durations and task scheduling, the problem of when and how to update completion times communicated to stakeholders remains understudied. Organizations must balance announcement accuracy against the costs of frequent timeline updates, which can erode stakeholder trust and trigger costly replanning. Despite the prevalence of this problem, current approaches rely on static predictions or ad-hoc policies that fail to account for the sequential nature of announcement management. In this paper, we formulate the task announcement problem as a Partially Observable Markov Decision Process (POMDP) where ...

---

## 73. Spatio-Semantic Expert Routing Architecture with Mixture-of-Experts for Referring Image Segmentation

**Authors**: Alaa Dalaq, Muzammil Behzad  
**Categories**: cs.AI  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12538  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12538v1.pdf

**Abstract**:
> arXiv:2603.12538v1 Announce Type: cross 
Abstract: Referring image segmentation aims to produce a pixel-level mask for the image region described by a natural-language expression. Although pretrained vision-language models have improved semantic grounding, many existing methods still rely on uniform refinement strategies that do not fully match the diverse reasoning requirements of referring expressions. Because of this mismatch, predictions often contain fragmented regions, inaccurate boundaries, or even the wrong object, especially when pretrained backbones are frozen for computational efficiency. To address these limitations, we propose SERA, a Spatio-Semantic Expert Routing Architecture for referring image segmentation. SERA introduces lightweight, expression-aware expert refinement at...

---

## 74. Multiscale Structure-Guided Latent Diffusion for Multimodal MRI Translation

**Authors**: Jianqiang Lin (Northeastern University, Shenyang, China, Key Laboratory of Intelligent Computing in ...  
**Categories**: cs.AI  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12581  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12581v1.pdf

**Abstract**:
> arXiv:2603.12581v1 Announce Type: cross 
Abstract: Although diffusion models have achieved remarkable progress in multi-modal magnetic resonance imaging (MRI) translation tasks, existing methods still tend to suffer from anatomical inconsistencies or degraded texture details when handling arbitrary missing-modality scenarios. To address these issues, we propose a latent diffusion-based multi-modal MRI translation framework, termed MSG-LDM. By leveraging the available modalities, the proposed method infers complete structural information, which preserves reliable boundary details. Specifically, we introduce a style--structure disentanglement mechanism in the latent space, which explicitly separates modality-specific style features from shared structural representations, and jointly models l...

---

## 75. Mastering Negation: Boosting Grounding Models via Grouped Opposition-Based Learning

**Authors**: Zesheng Yang, Xi Jiang, Bingzhang Hu, Weili Guan, Runmin Cong, Guo-Jun Qi, Feng Zheng  
**Categories**: cs.AI  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12606  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12606v1.pdf

**Abstract**:
> arXiv:2603.12606v1 Announce Type: cross 
Abstract: Current vision-language detection and grounding models predominantly focus on prompts with positive semantics and often struggle to accurately interpret and ground complex expressions containing negative semantics. A key reason for this limitation is the lack of high-quality training data that explicitly captures discriminative negative samples and negation-aware language descriptions.
  To address this challenge, we introduce D-Negation, a new dataset that provides objects annotated with both positive and negative semantic descriptions. Building upon the observation that negation reasoning frequently appears in natural language, we further propose a grouped opposition-based learning framework that learns negation-aware representations fro...

---

## 76. Literary Narrative as Moral Probe : A Cross-System Framework for Evaluating AI Ethical Reasoning and Refusal Behavior

**Authors**: David C. Flynn  
**Categories**: cs.AI  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12615  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12615v1.pdf

**Abstract**:
> arXiv:2603.12615v1 Announce Type: cross 
Abstract: Existing AI moral evaluation frameworks test for the production of correct-sounding ethical responses rather than the presence of genuine moral reasoning capacity. This paper introduces a novel probe methodology using literary narrative - specifically, unresolvable moral scenarios drawn from a published science fiction series - as stimulus material structurally resistant to surface performance. We present results from a 24-condition cross-system study spanning 13 distinct systems across two series: Series 1 (frontier commercial systems, blind; n=7) and Series 2 (local and API open-source systems, blind and declared; n=6). Four Series 2 systems were re-administered under declared conditions (13 blind + 4 declared + 7 ceiling probe = 24 tota...

---

## 77. VLM4Rec: Multimodal Semantic Representation for Recommendation with Large Vision-Language Models

**Authors**: Ty Valencia, Burak Barlas, Varun Singhal, Ruchir Bhatia, Wei Yang  
**Categories**: cs.AI  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12625  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12625v1.pdf

**Abstract**:
> arXiv:2603.12625v1 Announce Type: cross 
Abstract: Multimodal recommendation is commonly framed as a feature fusion problem, where textual and visual signals are combined to better model user preference. However, the effectiveness of multimodal recommendation may depend not only on how modalities are fused, but also on whether item content is represented in a semantic space aligned with preference matching. This issue is particularly important because raw visual features often preserve appearance similarity, while user decisions are typically driven by higher-level semantic factors such as style, material, and usage context. Motivated by this observation, we propose LVLM-grounded Multimodal Semantic Representation for Recommendation (VLM4Rec), a lightweight framework that organizes multimo...

---

## 78. Towards unified brain-to-text decoding across speech production and perception

**Authors**: Zhizhang Yuan, Yang Yang, Gaorui Zhang, Baowen Cheng, Zehan Wu, Yuhao Xu, Xiaoying Liu, Liang Chen, ...  
**Categories**: cs.AI  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12628  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12628v1.pdf

**Abstract**:
> arXiv:2603.12628v1 Announce Type: cross 
Abstract: Speech production and perception are the main ways humans communicate daily. Prior brain-to-text decoding studies have largely focused on a single modality and alphabetic languages. Here, we present a unified brain-to-sentence decoding framework for both speech production and perception in Mandarin Chinese. The framework exhibits strong generalization ability, enabling sentence-level decoding when trained only on single-character data and supporting characters and syllables unseen during training. In addition, it allows direct and controlled comparison of neural dynamics across modalities. Mandarin speech is decoded by first classifying syllable components in Hanyu Pinyin, namely initials and finals, from neural signals, followed by a post...

---

## 79. LR-SGS: Robust LiDAR-Reflectance-Guided Salient Gaussian Splatting for Self-Driving Scene Reconstruction

**Authors**: Ziyu Chen, Fan Zhu, Hui Zhu, Deyi Kong, Xinkai Kuang, Yujia Zhang, Chunmao Jiang  
**Categories**: cs.AI  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12647  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12647v1.pdf

**Abstract**:
> arXiv:2603.12647v1 Announce Type: cross 
Abstract: Recent 3D Gaussian Splatting (3DGS) methods have demonstrated the feasibility of self-driving scene reconstruction and novel view synthesis. However, most existing methods either rely solely on cameras or use LiDAR only for Gaussian initialization or depth supervision, while the rich scene information contained in point clouds, such as reflectance, and the complementarity between LiDAR and RGB have not been fully exploited, leading to degradation in challenging self-driving scenes, such as those with high ego-motion and complex lighting. To address these issues, we propose a robust and efficient LiDAR-reflectance-guided Salient Gaussian Splatting method (LR-SGS) for self-driving scenes, which introduces a structure-aware Salient Gaussian r...

---

## 80. CMHANet: A Cross-Modal Hybrid Attention Network for Point Cloud Registration

**Authors**: Dongxu Zhang, Yingsen Wang, Yiding Sun, Haoran Xu, Peilin Fan, Jihua Zhu  
**Categories**: cs.AI  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12721  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12721v1.pdf

**Abstract**:
> arXiv:2603.12721v1 Announce Type: cross 
Abstract: Robust point cloud registration is a fundamental task in 3D computer vision and geometric deep learning, essential for applications such as large-scale 3D reconstruction, augmented reality, and scene understanding. However, the performance of established learning-based methods often degrades in complex, real world scenarios characterized by incomplete data, sensor noise, and low overlap regions. To address these limitations, we propose CMHANet, a novel Cross-Modal Hybrid Attention Network. Our method integrates the fusion of rich contextual information from 2D images with the geometric detail of 3D point clouds, yielding a comprehensive and resilient feature representation. Furthermore, we introduce an innovative optimization function base...

---

## 81. CognitionCapturerPro: Towards High-Fidelity Visual Decoding from EEG/MEG via Multi-modal Information and Asymmetric Alignment

**Authors**: Kaifan Zhang, Lihuo He, Junjie Ke, Yuqi Ji, Lukun Wu, Lizi Wang, Xinbo Gao  
**Categories**: cs.AI  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12722  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12722v1.pdf

**Abstract**:
> arXiv:2603.12722v1 Announce Type: cross 
Abstract: Visual stimuli reconstruction from EEG remains challenging due to fidelity loss and representation shift. We propose CognitionCapturerPro, an enhanced framework that integrates EEG with multi-modal priors (images, text, depth, and edges) via collaborative training. Our core contributions include an uncertainty-weighted similarity scoring mechanism to quantify modality-specific fidelity and a fusion encoder for integrating shared representations. By employing a simplified alignment module and a pre-trained diffusion model, our method significantly outperforms the original CognitionCapturer on the THINGS-EEG dataset, improving Top-1 and Top-5 retrieval accuracy by 25.9% and 10.6%, respectively. Code is available at: https://github.com/XiaoZh...

---

## 82. MoKus: Leveraging Cross-Modal Knowledge Transfer for Knowledge-Aware Concept Customization

**Authors**: Chenyang Zhu, Hongxiang Li, Xiu Li, Long Chen  
**Categories**: cs.AI  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12743  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12743v1.pdf

**Abstract**:
> arXiv:2603.12743v1 Announce Type: cross 
Abstract: Concept customization typically binds rare tokens to a target concept. Unfortunately, these approaches often suffer from unstable performance as the pretraining data seldom contains these rare tokens. Meanwhile, these rare tokens fail to convey the inherent knowledge of the target concept. Consequently, we introduce Knowledge-aware Concept Customization, a novel task aiming at binding diverse textual knowledge to target visual concepts. This task requires the model to identify the knowledge within the text prompt to perform high-fidelity customized generation. Meanwhile, the model should efficiently bind all the textual knowledge to the target concept. Therefore, we propose MoKus, a novel framework for knowledge-aware concept customization...

---

## 83. Cheers: Decoupling Patch Details from Semantic Representations Enables Unified Multimodal Comprehension and Generation

**Authors**: Yichen Zhang, Da Peng, Zonghao Guo, Zijian Zhang, Xuesong Yang, Tong Sun, Shichu Sun, Yidan Zhang, Y...  
**Categories**: cs.AI  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12793  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12793v1.pdf

**Abstract**:
> arXiv:2603.12793v1 Announce Type: cross 
Abstract: A recent cutting-edge topic in multimodal modeling is to unify visual comprehension and generation within a single model. However, the two tasks demand mismatched decoding regimes and visual representations, making it non-trivial to jointly optimize within a shared feature space. In this work, we present Cheers, a unified multimodal model that decouples patch-level details from semantic representations, thereby stabilizing semantics for multimodal understanding and improving fidelity for image generation via gated detail residuals. Cheers includes three key components: (i) a unified vision tokenizer that encodes and compresses image latent states into semantic tokens for efficient LLM conditioning, (ii) an LLM-based Transformer that unifie...

---

## 84. Team LEYA in 10th ABAW Competition: Multimodal Ambivalence/Hesitancy Recognition Approach

**Authors**: Elena Ryumina (St. Petersburg Federal Research Center of the Russian Academy of Sciences, St. Peters...  
**Categories**: cs.AI  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12848  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12848v1.pdf

**Abstract**:
> arXiv:2603.12848v1 Announce Type: cross 
Abstract: Ambivalence/hesitancy recognition in unconstrained videos is a challenging problem due to the subtle, multimodal, and context-dependent nature of this behavioral state. In this paper, a multimodal approach for video-level ambivalence/hesitancy recognition is presented for the 10th ABAW Competition. The proposed approach integrates four complementary modalities: scene, face, audio, and text. Scene dynamics are captured with a VideoMAE-based model, facial information is encoded through emotional frame-level embeddings aggregated by statistical pooling, acoustic representations are extracted with EmotionWav2Vec2.0 and processed by a Mamba-based temporal encoder, and linguistic cues are modeled using fine-tuned transformer-based text models. T...

---

## 85. Learning from Child-Directed Speech in Two-Language Scenarios: A French-English Case Study

**Authors**: Liel Binyamin, Elior Sulem  
**Categories**: cs.AI  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12906  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12906v1.pdf

**Abstract**:
> arXiv:2603.12906v1 Announce Type: cross 
Abstract: Research on developmentally plausible language models has largely focused on English, leaving open questions about multilingual settings. We present a systematic study of compact language models by extending BabyBERTa to English-French scenarios under strictly size-matched data conditions, covering monolingual, bilingual, and cross-lingual settings. Our design contrasts two types of training corpora: (i) child-directed speech (about 2.5M tokens), following BabyBERTa and related work, and (ii) multi-domain corpora (about 10M tokens), extending the BabyLM framework to French. To enable fair evaluation, we also introduce new resources, including French versions of QAMR and QASRL, as well as English and French multi-domain corpora.
  We evalua...

---

## 86. FedBPrompt: Federated Domain Generalization Person Re-Identification via Body Distribution Aware Visual Prompts

**Authors**: Xin Xu, Weilong Li, Wei Liu, Wenke Huang, Zhixi Yu, Bin Yang, Xiaoying Liao, Kui Jiang  
**Categories**: cs.AI  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12912  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12912v1.pdf

**Abstract**:
> arXiv:2603.12912v1 Announce Type: cross 
Abstract: Federated Domain Generalization for Person Re-Identification (FedDG-ReID) learns domain-invariant representations from decentralized data. While Vision Transformer (ViT) is widely adopted, its global attention often fails to distinguish pedestrians from high similarity backgrounds or diverse viewpoints -- a challenge amplified by cross-client distribution shifts in FedDG-ReID. To address this, we propose Federated Body Distribution Aware Visual Prompt (FedBPrompt), introducing learnable visual prompts to guide Transformer attention toward pedestrian-centric regions. FedBPrompt employs a Body Distribution Aware Visual Prompts Mechanism (BAPM) comprising: Holistic Full Body Prompts to suppress cross-client background noise, and Body Part Ali...

---

## 87. Delta1 with LLM: symbolic and neural integration for credible and explainable reasoning

**Authors**: Yang Xu, Jun Liu, Shuwei Chen, Chris Nugent, Hailing Guo  
**Categories**: cs.AI  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12953  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12953v1.pdf

**Abstract**:
> arXiv:2603.12953v1 Announce Type: cross 
Abstract: Neuro-symbolic reasoning increasingly demands frameworks that unite the formal rigor of logic with the interpretability of large language models (LLMs). We introduce an end to end explainability by construction pipeline integrating the Automated Theorem Generator Delta1 based on the full triangular standard contradiction (FTSC) with LLMs. Delta1 deterministically constructs minimal unsatisfiable clause sets and complete theorems in polynomial time, ensuring both soundness and minimality by construction. The LLM layer verbalizes each theorem and proof trace into coherent natural language explanations and actionable insights. Empirical studies across health care, compliance, and regulatory domains show that Delta1 and LLM enables interpretab...

---

## 88. Fair Lung Disease Diagnosis from Chest CT via Gender-Adversarial Attention Multiple Instance Learning

**Authors**: Aditya Parikh, Aasa Feragen  
**Categories**: cs.AI  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12988  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12988v1.pdf

**Abstract**:
> arXiv:2603.12988v1 Announce Type: cross 
Abstract: We present a fairness-aware framework for multi-class lung disease diagnosis from chest CT volumes, developed for the Fair Disease Diagnosis Challenge at the PHAROS-AIF-MIH Workshop (CVPR 2026). The challenge requires classifying CT scans into four categories -- Healthy, COVID-19, Adenocarcinoma, and Squamous Cell Carcinoma -- with performance measured as the average of per-gender macro F1 scores, explicitly penalizing gender-inequitable predictions. Our approach addresses two core difficulties: the sparse pathological signal across hundreds of slices, and a severe demographic imbalance compounded across disease class and gender. We propose an attention-based Multiple Instance Learning (MIL) model on a ConvNeXt backbone that learns to iden...

---

## 89. Team RAS in 10th ABAW Competition: Multimodal Valence and Arousal Estimation Approach

**Authors**: Elena Ryumina (St. Petersburg Federal Research Center of the Russian Academy of Sciences, St. Peters...  
**Categories**: cs.AI  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13056  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13056v1.pdf

**Abstract**:
> arXiv:2603.13056v1 Announce Type: cross 
Abstract: Continuous emotion recognition in terms of valence and arousal under in-the-wild (ITW) conditions remains a challenging problem due to large variations in appearance, head pose, illumination, occlusions, and subject-specific patterns of affective expression. We present a multimodal method for valence-arousal estimation ITW. Our method combines three complementary modalities: face, behavior, and audio. The face modality relies on GRADA-based frame-level embeddings and Transformer-based temporal regression. We use Qwen3-VL-4B-Instruct to extract behavior-relevant information from video segments, while Mamba is used to model temporal dynamics across segments. The audio modality relies on WavLM-Large with attention-statistics pooling and inclu...

---

## 90. Human-in-the-Loop LLM Grading for Handwritten Mathematics Assessments

**Authors**: Arne Vanhoyweghen, Vincent Holst, Melika Mobini, Lukas Van de Voorde, Tibo Vanleke, Bert Verbruggen,...  
**Categories**: cs.AI  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13083  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13083v1.pdf

**Abstract**:
> arXiv:2603.13083v1 Announce Type: cross 
Abstract: Providing timely and individualised feedback on handwritten student work is highly beneficial for learning but difficult to achieve at scale. This challenge has become more pressing as generative AI undermines the reliability of take-home assessments, shifting emphasis toward supervised, in-class evaluation. We present a scalable, end-to-end workflow for LLM-assisted grading of short, pen-and-paper assessments. The workflow spans (1) constructing solution keys, (2) developing detailed rubric-style grading keys used to guide the LLM, and (3) a grading procedure that combines automated scanning and anonymisation, multi-pass LLM scoring, automated consistency checks, and mandatory human verification. We deploy the system in two undergraduate ...

---

## 91. Visual-ERM: Reward Modeling for Visual Equivalence

**Authors**: Ziyu Liu, Shengyuan Ding, Xinyu Fang, Xuanlang Dai, Penghui Yang, Jianze Liang, Jiaqi Wang, Kai Chen...  
**Categories**: cs.AI  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13224  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13224v1.pdf

**Abstract**:
> arXiv:2603.13224v1 Announce Type: cross 
Abstract: Vision-to-code tasks require models to reconstruct structured visual inputs, such as charts, tables, and SVGs, into executable or structured representations with high visual fidelity. While recent Large Vision Language Models (LVLMs) achieve strong results via supervised fine-tuning, reinforcement learning remains challenging due to misaligned reward signals. Existing rewards either rely on textual rules or coarse visual embedding similarity, both of which fail to capture fine-grained visual discrepancies and are vulnerable to reward hacking. We propose Visual Equivalence Reward Model (Visual-ERM), a multimodal generative reward model that provides fine-grained, interpretable, and task-agnostic feedback to evaluate vision-to-code quality d...

---

## 92. Tiny Recursive Reasoning with Mamba-2 Attention Hybrid

**Authors**: Wenlong Wang, Fergal Reid  
**Categories**: cs.AI  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.12078  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.12078v2.pdf

**Abstract**:
> arXiv:2602.12078v2 Announce Type: replace 
Abstract: Recent work on recursive reasoning models like TRM demonstrates that tiny networks (7M parameters) can achieve strong performance on abstract reasoning tasks through latent recursion -- iterative refinement in hidden representation space without emitting intermediate tokens. This raises a natural question about operator choice: Mamba-2's state space recurrence is itself a form of iterative refinement, making it a natural candidate for recursive reasoning -- but does introducing Mamba-2 into the recursive scaffold preserve reasoning capability? We investigate this by replacing the Transformer blocks in TRM with Mamba-2 hybrid operators while maintaining parameter parity (6.83M vs 6.86M parameters). On ARC-AGI-1, we find that the hybrid im...

---

## 93. Partially Recentralization Softmax Loss for Vision-Language Models Robustness

**Authors**: Hao Wang, Jinzhe Jiang, Xin Zhang, Chen Li  
**Categories**: cs.AI  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2402.03627  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2402.03627v4.pdf

**Abstract**:
> arXiv:2402.03627v4 Announce Type: replace-cross 
Abstract: As Large Language Models make a breakthrough in natural language processing tasks (NLP), multimodal technique becomes extremely popular. However, it has been shown that multimodal NLP are vulnerable to adversarial attacks, where the outputs of a model can be dramatically changed by a perturbation to the input. While several defense techniques have been proposed both in computer vision and NLP models, the multimodal robustness of models have not been fully explored. In this paper, we study the adversarial robustness provided by modifying loss function of pre-trained multimodal models, by restricting top K softmax outputs. Based on the evaluation and scoring, our experiments show that after a fine-tuning, adversarial robustness of pr...

---

## 94. Computational lexical analysis of Flamenco genres

**Authors**: Pablo Rosillo-Rodes, Maxi San Miguel, David Sanchez  
**Categories**: cs.AI  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2405.05723  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2405.05723v2.pdf

**Abstract**:
> arXiv:2405.05723v2 Announce Type: replace-cross 
Abstract: Flamenco, recognized by UNESCO as part of the Intangible Cultural Heritage of Humanity, is a profound expression of cultural identity rooted in Andalusia, Spain. However, there is a lack of quantitative studies that help identify characteristic patterns in this long-lived music tradition. In this work, we present a computational analysis of Flamenco lyrics, employing natural language processing and machine learning to categorize over 2000 lyrics into their respective Flamenco genres, termed as $\textit{palos}$. Using a Multinomial Naive Bayes classifier, we find that lexical variation across styles enables to accurately identify distinct $\textit{palos}$. More importantly, from an automatic method of word usage, we obtain the seman...

---

## 95. Motion Dreamer: Boundary Conditional Motion Reasoning for Physically Coherent Video Generation

**Authors**: Tianshuo Xu, Zhifei Chen, Leyi Wu, Hao Lu, Yuying Chen, Lihui Jiang, Bingbing Liu, Yingcong Chen  
**Categories**: cs.AI  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2412.00547  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2412.00547v4.pdf

**Abstract**:
> arXiv:2412.00547v4 Announce Type: replace-cross 
Abstract: Recent advances in video generation have shown promise for generating future scenarios, critical for planning and control in autonomous driving and embodied intelligence. However, real-world applications demand more than visually plausible predictions; they require reasoning about object motions based on explicitly defined boundary conditions, such as initial scene image and partial object motion. We term this capability Boundary Conditional Motion Reasoning. Current approaches either neglect explicit user-defined motion constraints, producing physically inconsistent motions, or conversely demand complete motion inputs, which are rarely available in practice. Here we introduce Motion Dreamer, a two-stage framework that explicitly s...

---

## 96. Think with 3D: Geometric Imagination Grounded Spatial Reasoning from Limited Views

**Authors**: Zhangquan Chen, Manyuan Zhang, Xinlei Yu, Xufang Luo, Mingze Sun, Zihao Pan, Xiang An, Yan Feng, Pen...  
**Categories**: cs.AI  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.18632  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.18632v4.pdf

**Abstract**:
> arXiv:2510.18632v4 Announce Type: replace-cross 
Abstract: Though recent advances in vision-language models (VLMs) have achieved remarkable progress across a wide range of multimodal tasks, understanding 3D spatial relationships from limited views remains a significant challenge. Previous reasoning methods typically rely on pure text (e.g., topological cognitive maps) or on 2D visual cues. However, their limited representational capacity hinders performance in specific tasks that require 3D spatial imagination. To address this limitation, we propose 3DThinker, a framework that can effectively exploits the rich geometric information embedded within images while reasoning, like humans do. Our framework is the first to enable 3D mentaling during reasoning without any 3D prior input, and it do...

---

## 97. Multimodal Continual Learning with MLLMs from Multi-scenario Perspectives

**Authors**: Kai Jiang, Siqi Huang, Xiangyu Chen, Jiawei Shao, Hongyuan Zhang, Ping Luo, Xuelong Li  
**Categories**: cs.AI  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2511.18507  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2511.18507v3.pdf

**Abstract**:
> arXiv:2511.18507v3 Announce Type: replace-cross 
Abstract: Multimodal large language models (MLLMs) deployed on devices must adapt to continuously changing visual scenarios such as variations in background and perspective, to effectively perform complex visual tasks. To investigate catastrophic forgetting under real-world scenario shifts, we construct a multimodal visual understanding dataset (MSVQA), covering four distinct scenarios and perspectives: high-altitude, underwater, low-altitude, and indoor environments. Furthermore, we propose UNIFIER (mUltimodal coNtInual learning with MLLMs From multi-scenarIo pERspectives), a continual learning (CL) framework designed to address visual discrepancies while learning different scenarios. Compared to existing CL methods, UNIFIER enables knowled...

---

## 98. Towards Contextual Sensitive Data Detection

**Authors**: Liang Telkamp, Madelon Hulsebos  
**Categories**: cs.AI  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2512.04120  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2512.04120v2.pdf

**Abstract**:
> arXiv:2512.04120v2 Announce Type: replace-cross 
Abstract: The emergence of open data portals necessitates more attention to protecting sensitive data before datasets get published and exchanged. To do so effectively, we observe the need to refine and broaden our definitions of sensitive data, and argue that the sensitivity of data depends on its context. Following this definition, we introduce a contextual data sensitivity framework building on two core concepts: 1) type contextualization, which considers the type of the data values at hand within the overall context of the dataset or document to assess their true sensitivity, and 2) domain contextualization, which assesses the sensitivity of data values informed by domain-specific information external to the dataset, such as geographic o...

---

## 99. OpenVision 3: A Family of Unified Visual Encoder for Both Understanding and Generation

**Authors**: Letian Zhang, Sucheng Ren, Yanqing Liu, Xianhang Li, Zeyu Wang, Yuyin Zhou, Huaxiu Yao, Zeyu Zheng, ...  
**Categories**: cs.AI  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2601.15369  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2601.15369v2.pdf

**Abstract**:
> arXiv:2601.15369v2 Announce Type: replace-cross 
Abstract: This paper presents a family of advanced vision encoder, named OpenVision 3, that learns a single, unified visual representation that can serve both image understanding and image generation. Our core architecture is simple: we feed VAE-compressed image latents to a ViT encoder and train its output to support two complementary roles. First, the encoder output is passed to the ViT-VAE decoder to reconstruct the original image, encouraging the representation to capture generative structure. Second, the same representation is optimized with contrastive learning and image-captioning objectives, strengthening semantic features. By jointly optimizing reconstruction- and semantics-driven signals in a shared latent space, the encoder learns...

---

## 100. BitDance: Scaling Autoregressive Generative Models with Binary Tokens

**Authors**: Yuang Ai, Jiaming Han, Shaobin Zhuang, Weijia Mao, Xuefeng Hu, Ziyan Yang, Zhenheng Yang, Yali Wang,...  
**Categories**: cs.AI  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.14041  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.14041v2.pdf

**Abstract**:
> arXiv:2602.14041v2 Announce Type: replace-cross 
Abstract: We present BitDance, a scalable autoregressive (AR) image generator that predicts binary visual tokens instead of codebook indices. With high-entropy binary latents, BitDance lets each token represent up to $2^{256}$ states, yielding a compact yet highly expressive discrete representation. Sampling from such a huge token space is difficult with standard classification. To resolve this, BitDance uses a binary diffusion head: instead of predicting an index with softmax, it employs continuous-space diffusion to generate the binary tokens. Furthermore, we propose next-patch diffusion, a new decoding method that predicts multiple tokens in parallel with high accuracy, greatly speeding up inference. On ImageNet 256x256, BitDance achieves...

---

## 101. Beyond Static Instruction: A Multi-agent AI Framework for Adaptive Augmented Reality Robot Training

**Authors**: Nicolas Leins, Jana Gonnermann-M\"uller, Malte Teichmann, Sebastian Pokutta  
**Categories**: cs.AI  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.00016  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.00016v2.pdf

**Abstract**:
> arXiv:2603.00016v2 Announce Type: replace-cross 
Abstract: Augmented Reality (AR) offers powerful visualization capabilities for industrial robot training, yet current interfaces remain predominantly static, failing to account for learners' diverse cognitive profiles. In this paper, we present an AR application for robot training and propose a multi-agent AI framework for future integration that bridges the gap between static visualization and pedagogical intelligence. We report on the evaluation of the baseline AR interface with 36 participants performing a robotic pick-and-place task. While overall usability was high, notable disparities in task duration and learner characteristics highlighted the necessity for dynamic adaptation. To address this, we propose a multi-agent framework that ...

---

## 102. Ref-DGS: Reflective Dual Gaussian Splatting

**Authors**: Ningjing Fan, Yiqun Wang, Dongming Yan, Peter Wonka  
**Categories**: cs.AI  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.07664  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.07664v2.pdf

**Abstract**:
> arXiv:2603.07664v2 Announce Type: replace-cross 
Abstract: Reflective appearance, especially strong and typically near-field specular reflections, poses a fundamental challenge for accurate surface reconstruction and novel view synthesis. Existing Gaussian splatting methods either fail to model near-field specular reflections or rely on explicit ray tracing at substantial computational cost. We present Ref-DGS, a reflective dual Gaussian splatting framework that addresses this trade-off by decoupling surface reconstruction from specular reflection within an efficient rasterization-based pipeline. Ref-DGS introduces a dual Gaussian scene representation consisting of geometry Gaussians and complementary local reflection Gaussians that capture near-field specular interactions without explicit...

---

## 103. Beyond Convolution: A Taxonomy of Structured Operators for Learning-Based Image Processing

**Authors**: Simone Cammarasana  
**Categories**: cs.AI  
**Published**: Mon, 16 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12067  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12067v2.pdf

**Abstract**:
> arXiv:2603.12067v2 Announce Type: replace-cross 
Abstract: The convolution operator is the fundamental building block of modern convolutional neural networks (CNNs), owing to its simplicity, translational equivariance, and efficient implementation. However, its structure as a fixed, linear, locally-averaging operator limits its ability to capture structured signal properties such as low-rank decompositions, adaptive basis representations, and non-uniform spatial dependencies. This paper presents a systematic taxonomy of operators that extend or replace the standard convolution in learning-based image processing pipelines. We organise the landscape of alternative operators into five families: (i) decomposition-based operators, which separate structural and noise components through singular ...

---

