# arXiv Papers - 2026-03-20

**来源**: arXiv (cs.SD, eess.AS, cs.LG, cs.AI)  
**关键词**: speech, audio, music, voice, sound, Mel, representation, self-supervised  
**今日新论文**: 131 篇

---

## 1. MOSS-TTS Technical Report

**Authors**: Yitian Gong, Botian Jiang, Yiwei Zhao, Yucheng Yuan, Kuangwei Chen, Yaozhou Jiang, Cheng Chang, Dong...  
**Categories**: cs.SD  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18090  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18090v1.pdf

**Abstract**:
> arXiv:2603.18090v1 Announce Type: new 
Abstract: This technical report presents MOSS-TTS, a speech generation foundation model built on a scalable recipe: discrete audio tokens, autoregressive modeling, and large-scale pretraining. Built on MOSS-Audio-Tokenizer, a causal Transformer tokenizer that compresses 24 kHz audio to 12.5 fps with variable-bitrate RVQ and unified semantic-acoustic representations, we release two complementary generators: MOSS-TTS, which emphasizes structural simplicity, scalability, and long-context/control-oriented deployment, and MOSS-TTS-Local-Transformer, which introduces a frame-local autoregressive module for higher modeling efficiency, stronger speaker preservation, and a shorter time to first audio. Across multilingual and open-domain settings, MOSS-TTS supp...

---

## 2. Towards Interpretable Framework for Neural Audio Codecs via Sparse Autoencoders: A Case Study on Accent Information

**Authors**: Shih-Heng Wang, Tiantian Feng, Aditya Kommineni, Thanathai Lertpetchpun, Bowen Yi, Xuan Shi, Shrikan...  
**Categories**: cs.SD  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18359  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18359v1.pdf

**Abstract**:
> arXiv:2603.18359v1 Announce Type: new 
Abstract: Neural Audio Codecs (NACs) are widely adopted in modern speech systems, yet how they encode linguistic and paralinguistic information remains unclear. Improving the interpretability of NAC representations is critical for understanding and deploying them in sensitive applications. Hence, we employ Sparse Autoencoders (SAEs) to decompose dense NAC representations into sparse, interpretable activations. In this work, we focus on a challenging paralinguistic attribute-accent-and propose a framework to quantify NAC interpretability. We evaluate four NAC models under 16 SAE configurations using a relative performance index. Our results show that DAC and SpeechTokenizer achieve the highest interpretability. We further reveal that acoustic-oriented ...

---

## 3. Words at Play: Benchmarking Audio Pun Understanding in Large Audio-Language Models

**Authors**: Yuchen Su, Shaoxin Zhong, Yonghua Zhu, Ruofan Wang, Zijian Huang, Qiqi Wang, Na Zhao, Diana Benavide...  
**Categories**: cs.SD  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18678  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18678v1.pdf

**Abstract**:
> arXiv:2603.18678v1 Announce Type: new 
Abstract: Puns represent a typical linguistic phenomenon that exploits polysemy and phonetic ambiguity to generate humour, posing unique challenges for natural language understanding. Within pun research, audio plays a central role in human communication except text and images, while datasets and systematic resources for spoken puns remain scarce, leaving this crucial modality largely underexplored. In this paper, we present APUN-Bench, the first benchmark dedicated to evaluating large audio language models (LALMs) on audio pun understanding. Our benchmark contains 4,434 audio samples annotated across three stages: pun recognition, pun word location and pun meaning inference. We conduct a deep analysis of APUN-Bench by systematically evaluating 10 sta...

---

## 4. Few-shot Acoustic Synthesis with Multimodal Flow Matching

**Authors**: Amandine Brunetto  
**Categories**: cs.SD  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.19176  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.19176v1.pdf

**Abstract**:
> arXiv:2603.19176v1 Announce Type: new 
Abstract: Generating audio that is acoustically consistent with a scene is essential for immersive virtual environments. Recent neural acoustic field methods enable spatially continuous sound rendering but remain scene-specific, requiring dense audio measurements and costly training for each environment. Few-shot approaches improve scalability across rooms but still rely on multiple recordings and, being deterministic, fail to capture the inherent uncertainty of scene acoustics under sparse context. We introduce flow-matching acoustic generation (FLAC), a probabilistic method for few-shot acoustic synthesis that models the distribution of plausible room impulse responses (RIRs) given minimal scene context. FLAC leverages a diffusion transformer traine...

---

## 5. ProKWS: Personalized Keyword Spotting via Collaborative Learning of Phonemes and Prosody

**Authors**: Jianan Pan, Yuanming Zhang, Kejie Huang  
**Categories**: cs.SD  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18024  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18024v1.pdf

**Abstract**:
> arXiv:2603.18024v1 Announce Type: cross 
Abstract: Current keyword spotting systems primarily use phoneme-level matching to distinguish confusable words but ignore user-specific pronunciation traits like prosody (intonation, stress, rhythm). This paper presents ProKWS, a novel framework integrating fine-grained phoneme learning with personalized prosody modeling. We design a dual-stream encoder where one stream derives robust phonemic representations through contrastive learning, while the other extracts speaker-specific prosodic patterns. A collaborative fusion module dynamically combines phonemic and prosodic information, enhancing adaptability across acoustic environments. Experiments show ProKWS delivers highly competitive performance, comparable to state-of-the-art models on standard ...

---

## 6. DEAF: A Benchmark for Diagnostic Evaluation of Acoustic Faithfulness in Audio Language Models

**Authors**: Jiaqi Xiong, Yunjia Qi, Qi Cao, Yu Zheng, Weisheng Xu, Ziteng Wang, Ruofan Liao, Yutong Zhang, Siche...  
**Categories**: cs.SD  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18048  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18048v1.pdf

**Abstract**:
> arXiv:2603.18048v1 Announce Type: cross 
Abstract: Recent Audio Multimodal Large Language Models (Audio MLLMs) demonstrate impressive performance on speech benchmarks, yet it remains unclear whether these models genuinely process acoustic signals or rely on text-based semantic inference. To systematically study this question, we introduce DEAF (Diagnostic Evaluation of Acoustic Faithfulness), a benchmark of over 2,700 conflict stimuli spanning three acoustic dimensions: emotional prosody, background sounds, and speaker identity. Then, we design a controlled multi-level evaluation framework that progressively increases textual influence, ranging from semantic conflicts in the content to misleading prompts and their combination, allowing us to disentangle content-driven bias from prompt-indu...

---

## 7. EgoAdapt: Enhancing Robustness in Egocentric Interactive Speaker Detection Under Missing Modalities

**Authors**: Xinyuan Qian, Xinjia Zhu, Alessio Brutti, Dong Liang  
**Categories**: cs.SD  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18082  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18082v1.pdf

**Abstract**:
> arXiv:2603.18082v1 Announce Type: cross 
Abstract: TTM (Talking to Me) task is a pivotal component in understanding human social interactions, aiming to determine who is engaged in conversation with the camera-wearer. Traditional models often face challenges in real-world scenarios due to missing visual data, neglecting the role of head orientation, and background noise. This study addresses these limitations by introducing EgoAdapt, an adaptive framework designed for robust egocentric "Talking to Me" speaker detection under missing modalities. Specifically, EgoAdapt incorporates three key modules: (1) a Visual Speaker Target Recognition (VSTR) module that captures head orientation as a non-verbal cue and lip movement as a verbal cue, allowing a comprehensive interpretation of both verbal ...

---

## 8. STEP: Detecting Audio Backdoor Attacks via Stability-based Trigger Exposure Profiling

**Authors**: Kun Wang, Meng Chen, Junhao Wang, Yuli Wu, Li Lu, Chong Zhang, Peng Cheng, Jiaheng Zhang, Kui Ren  
**Categories**: cs.SD  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18103  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18103v1.pdf

**Abstract**:
> arXiv:2603.18103v1 Announce Type: cross 
Abstract: With the widespread deployment of deep-learning-based speech models in security-critical applications, backdoor attacks have emerged as a serious threat: an adversary who poisons a small fraction of training data can implant a hidden trigger that controls the model's output while preserving normal behavior on clean inputs. Existing inference-time defenses are not well suited to the audio domain, as they either rely on trigger over-robustness assumptions that fail on transformation-based and semantic triggers, or depend on properties specific to image or text modalities. In this paper, we propose STEP (Stability-based Trigger Exposure Profiling), a black-box, retraining-free backdoor detector that operates under hard-label-only access. Its ...

---

## 9. ALIGN: Adversarial Learning for Generalizable Speech Neuroprosthesis

**Authors**: Zhanqi Zhang, Shun Li, Bernardo L. Sabatini, Mikio Aoi, Gal Mishne  
**Categories**: cs.SD  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18299  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18299v1.pdf

**Abstract**:
> arXiv:2603.18299v1 Announce Type: cross 
Abstract: Intracortical brain-computer interfaces (BCIs) can decode speech from neural activity with high accuracy when trained on data pooled across recording sessions. In realistic deployment, however, models must generalize to new sessions without labeled data, and performance often degrades due to cross-session nonstationarities (e.g., electrode shifts, neural turnover, and changes in user strategy). In this paper, we propose ALIGN, a session-invariant learning framework based on multi-domain adversarial neural networks for semi-supervised cross-session adaptation. ALIGN trains a feature encoder jointly with a phoneme classifier and a domain classifier operating on the latent representation. Through adversarial optimization, the encoder is encou...

---

## 10. DiscoPhon: Benchmarking the Unsupervised Discovery of Phoneme Inventories With Discrete Speech Units

**Authors**: Maxime Poli, Manel Khentout, Angelo Ortiz Tandazo, Ewan Dunbar, Emmanuel Chemla, Emmanuel Dupoux  
**Categories**: cs.SD  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18612  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18612v1.pdf

**Abstract**:
> arXiv:2603.18612v1 Announce Type: cross 
Abstract: We introduce DiscoPhon, a multilingual benchmark for evaluating unsupervised phoneme discovery from discrete speech units. DiscoPhon covers 6 dev and 6 test languages, chosen to span a wide range of phonemic contrasts. Given only 10 hours of speech in a previously unseen language, systems must produce discrete units that are mapped to a predefined phoneme inventory, through either a many-to-one or a one-to-one assignment. The resulting sequences are evaluated for unit quality, recognition and segmentation. We provide four pretrained multilingual HuBERT and SpidR baselines, and show that phonemic information is available enough in current models for derived units to correlate well with phonemes, though with variations across languages.

---

## 11. How Auditory Knowledge in LLM Backbones Shapes Audio Language Models: A Holistic Evaluation

**Authors**: Ke-Han Lu, Szu-Wei Fu, Chao-Han Huck Yang, Zhehuai Chen, Sung-Feng Huang, Chih-Kai Yang, Yi-Cheng Li...  
**Categories**: cs.SD  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.19195  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.19195v1.pdf

**Abstract**:
> arXiv:2603.19195v1 Announce Type: cross 
Abstract: Large language models (LLMs) have been widely used as knowledge backbones of Large Audio Language Models (LALMs), yet how much auditory knowledge they encode through text-only pre-training and how this affects downstream performance remains unclear. We study this gap by comparing different LLMs under two text-only and one audio-grounded setting: (1) direct probing on AKB-2000, a curated benchmark testing the breadth and depth of auditory knowledge; (2) cascade evaluation, where LLMs reason over text descriptions from an audio captioner; and (3) audio-grounded evaluation, where each LLM is fine-tuned into a Large Audio Language Model (LALM) with an audio encoder. Our findings reveal that auditory knowledge varies substantially across famili...

---

## 12. Evaluating Hallucinations in Audio-Visual Multimodal LLMs with Spoken Queries under Diverse Acoustic Conditions

**Authors**: Hansol Park, Hoseong Ahn, Junwon Moon, Yejin Lee, Kyuhong Shim  
**Categories**: cs.SD  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.08581  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.08581v2.pdf

**Abstract**:
> arXiv:2510.08581v2 Announce Type: replace 
Abstract: Hallucinations in multimodal models have been extensively studied using benchmarks that probe reliability in image-text query settings. However, the effect of spoken queries on multimodal hallucinations remains largely unexplored, despite the growing role of voice interfaces. In this paper, we introduce a systematic pipeline that converts existing multimodal hallucination benchmarks into spoken-query versions while preserving the original tasks and labels. We instantiate this pipeline on RePOPE and release RePOPE-Spk, where all queries are provided as spoken audio under diverse input conditions. Experimental results show that hallucinations escalate when queries are spoken rather than written: error rates increase by 3-6% with clean spee...

---

## 13. Fair-Gate: Fairness-Aware Interpretable Risk Gating for Sex-Fair Voice Biometrics

**Authors**: Yangyang Qu, Todisco Massimiliano, Galdi Chiara, Evans Nicholas  
**Categories**: cs.SD  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11360  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11360v2.pdf

**Abstract**:
> arXiv:2603.11360v2 Announce Type: replace 
Abstract: Voice biometric systems can exhibit sex-related performance gaps even when overall verification accuracy is strong. We attribute these gaps to two practical mechanisms: (i) demographic shortcut learning, where speaker classification training exploits spurious correlations between sex and speaker identity, and (ii) feature entanglement, where sex-linked acoustic variation overlaps with identity cues and cannot be removed without degrading speaker discrimination. We propose Fair-Gate, a fairness-aware and interpretable risk-gating framework that addresses both mechanisms in a single pipeline. Fair-Gate applies risk extrapolation to reduce variation in speaker-classification risk across proxy sex groups, and introduces a local complementary...

---

## 14. DeSTA2.5-Audio: Toward General-Purpose Large Audio Language Model with Self-Generated Cross-Modal Alignment

**Authors**: Ke-Han Lu, Zhehuai Chen, Szu-Wei Fu, Chao-Han Huck Yang, Sung-Feng Huang, Chih-Kai Yang, Chee-En Yu,...  
**Categories**: cs.SD  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2507.02768  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2507.02768v2.pdf

**Abstract**:
> arXiv:2507.02768v2 Announce Type: replace-cross 
Abstract: We introduce DeSTA2.5-Audio, a general-purpose Large Audio Language Model (LALM) designed for robust auditory perception and instruction-following. Recent LALMs augment Large Language Models (LLMs) with auditory capabilities by training on large-scale audio-instruction datasets. However, existing LALMs have often suffered from the catastrophic forgetting of the LLM's original abilities. Therefore, balancing knowledge retention and audio perception has become a critical challenge. To address this, we revisit the data construction pipeline and propose a self-generated cross-modal alignment strategy in which the backbone LLM generates its own training targets, named DeSTA. This approach aims at preserving the LLM's native language pro...

---

## 15. MPDR Beamforming for Almost-Cyclostationary Processes

**Authors**: Giovanni Bologni, Martin Bo M{\o}ller, Richard Heusdens, Richard C. Hendriks  
**Categories**: cs.SD  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.18391  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.18391v2.pdf

**Abstract**:
> arXiv:2510.18391v2 Announce Type: replace-cross 
Abstract: Conventional acoustic beamformers typically assume short-time stationarity and process frequency bins independently, ignoring inter-frequency correlations. This is suboptimal for almost-periodic noise sources such as engines, fans, and musical instruments: these signals are better modeled as (almost) cyclostationary (ACS) processes with statistically correlated spectral components. This paper introduces the cyclic minimum power distortionless response (cMPDR) beamformer, which extends the conventional MPDR to jointly exploit spatial and spectral correlations. Building on frequency-shifted (FRESH) filtering, it suppresses noise components that are coherent across harmonically related frequencies, reducing residual noise beyond what ...

---

## 16. Affect Decoding in Phonated and Silent Speech Production from Surface EMG

**Authors**: Simon Pistrosch, Kleanthis Avramidis, Zhao Ren, Tiantian Feng, Jihwan Lee, Monica Gonzalez-Machorro,...  
**Categories**: cs.SD  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11715  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11715v2.pdf

**Abstract**:
> arXiv:2603.11715v2 Announce Type: replace-cross 
Abstract: The expression of affect is integral to spoken communication, yet, its link to underlying articulatory execution remains unclear. Measures of articulatory muscle activity such as EMG could reveal how speech production is modulated by emotion alongside acoustic speech analyses. We investigate affect decoding from facial and neck surface electromyography (sEMG) during phonated and silent speech production. For this purpose, we introduce a dataset comprising 2,780 utterances from 12 participants across 3 tasks, on which we evaluate both intra- and inter-subject decoding using a range of features and model embeddings. Our results reveal that EMG representations reliably discriminate frustration with up to 0.845 AUC, and generalize well...

---

## 17. ARTT: Augmented Reverberant-Target Training for Unsupervised Monaural Speech Dereverberation

**Authors**: Siqi Song, Fulin Wu, Zhong-Qiu Wang  
**Categories**: eess.AS  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18485  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18485v1.pdf

**Abstract**:
> arXiv:2603.18485v1 Announce Type: new 
Abstract: Due to the absence of clean reference signals and spatial cues, monaural unsupervised speech dereverberation is a challenging ill-posed inverse problem. To realize it, we propose augmented reverberant-target training (ARTT), which consists of two stages. In the first stage, reverberant-target training (RTT) is proposed to first further reverberate the observed reverberant mixture signal, and then train a deep neural network (DNN) to recover the observed reverberant mixture via discriminative training. Although the target signal to fit is reverberant, we find that the resulting DNN can effectively reduce reverberation. In the second stage, an online self-distillation mechanism based on the mean-teacher algorithm is proposed to further improve...

---

## 18. Modeling Overlapped Speech with Shuffles

**Authors**: Matthew Wiesner, Samuele Cornell, Alexander Polok, Lucas Ondel Yang, Luk\'a\v{s} Burget, Sanjeev Khu...  
**Categories**: eess.AS  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.17769  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.17769v1.pdf

**Abstract**:
> arXiv:2603.17769v1 Announce Type: cross 
Abstract: We propose to model parallel streams of data, such as overlapped speech, using shuffles. Specifically, this paper shows how the shuffle product and partial order finite-state automata (FSAs) can be used for alignment and speaker-attributed transcription of overlapped speech. We train using the total score on these FSAs as a loss function, marginalizing over all possible serializations of overlapping sequences at subword, word, and phrase levels. To reduce graph size, we impose temporal constraints by constructing partial order FSAs. We address speaker attribution by modeling (token, speaker) tuples directly. Viterbi alignment through the shuffle product FSA directly enables one-pass alignment. We evaluate performance on synthetic LibriSpee...

---

## 19. Investigating Faithfulness in Large Audio Language Models

**Authors**: Pooneh Mousavi, Lovenya Jain, Mirco Ravanelli, Cem Subakan  
**Categories**: eess.AS  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2509.22363  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2509.22363v3.pdf

**Abstract**:
> arXiv:2509.22363v3 Announce Type: replace-cross 
Abstract: Large Audio Language Models (LALMs) integrate audio encoders with pretrained Large Language Models to perform complex multimodal reasoning tasks. While these models can generate Chain-of-Thought (CoT) explanations, the faithfulness of these reasoning chains remains unclear. In this work, we propose a systematic framework to evaluate CoT faithfulness in LALMs with respect to both the input audio and the final model prediction. We define three criteria for audio faithfulness: hallucination-free, holistic, and attentive listening. We also introduce a benchmark based on both audio and CoT interventions to assess faithfulness. Experiments on Audio Flamingo 3 and Qwen2.5-Omni suggest a potential multimodal disconnect: reasoning often ali...

---

## 20. Engineering Verifiable Modularity in Transformers via Per-Layer Supervision

**Authors**: J. Clayton Kerce  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18029  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18029v1.pdf

**Abstract**:
> arXiv:2603.18029v1 Announce Type: new 
Abstract: Transformers resist surgical control. Ablating an attention head identified as critical for capitalization produces minimal behavioral change because distributed redundancy compensates for damage. This Hydra effect renders interpretability illusory: we may identify components through correlation, but cannot predict or control their causal role. We demonstrate that architectural interventions can expose hidden modularity. Our approach combines dual-stream processing separating token and contextual representations, per-layer supervision providing independent gradient signal at each depth, and gated attention regularizing toward discrete activation patterns. When trained with per-layer supervision, models produce ablation effects 5 to 23 times ...

---

## 21. Taming Epilepsy: Mean Field Control of Whole-Brain Dynamics

**Authors**: Ming Li, Ting Gao, Jingqiao Dua  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18035  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18035v1.pdf

**Abstract**:
> arXiv:2603.18035v1 Announce Type: new 
Abstract: Controlling the high-dimensional neural dynamics during epileptic seizures remains a significant challenge due to the nonlinear characteristics and complex connectivity of the brain. In this paper, we propose a novel framework, namely Graph-Regularized Koopman Mean-Field Game (GK-MFG), which integrates Reservoir Computing (RC) for Koopman operator approximation with Alternating Population and Agent Control Network (APAC-Net) for solving distributional control problems. By embedding Electroencephalogram (EEG) dynamics into a linear latent space and imposing graph Laplacian constraints derived from the Phase Locking Value (PLV), our method achieves robust seizure suppression while respecting the functional topological structure of the brain.

---

## 22. Quotient Geometry and Persistence-Stable Metrics for Swarm Configurations

**Authors**: Mark M. Bailey  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18041  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18041v1.pdf

**Abstract**:
> arXiv:2603.18041v1 Announce Type: new 
Abstract: Swarm and constellation reconfiguration can be viewed as motion of an unordered point configuration in an ambient space. Here, we provide persistence-stable, symmetry-invariant geometric representations for comparing and monitoring multi-agent configuration data. We introduce a quotient formation space $\mathcal{S}_n(M,G)=M^n/(G\times S_n)$ and a formation matching metric $d_{M,G}$ obtained by optimizing a worst-case assignment error over ambient symmetries $g\in G$ and relabelings $\sigma\in S_n$. This metric is a structured, physically interpretable relaxation of Gromov--Hausdorff distance: the induced inter-agent metric spaces satisfy $d_{\mathrm{GH}}(X_x,X_y)\le d_{M,G}([x],[y])$. Composing this bound with stability of Vietoris--Rips per...

---

## 23. NANOZK: Layerwise Zero-Knowledge Proofs for Verifiable Large Language Model Inference

**Authors**: Zhaohui Geoffrey Wang  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18046  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18046v1.pdf

**Abstract**:
> arXiv:2603.18046v1 Announce Type: new 
Abstract: When users query proprietary LLM APIs, they receive outputs with no cryptographic assurance that the claimed model was actually used. Service providers could substitute cheaper models, apply aggressive quantization, or return cached responses - all undetectable by users paying premium prices for frontier capabilities. We present METHOD, a zero-knowledge proof system that makes LLM inference verifiable: users can cryptographically confirm that outputs correspond to the computation of a specific model.
  Our approach exploits the fact that transformer inference naturally decomposes into independent layer computations, enabling a layerwise proof framework where each layer generates a constant-size proof regardless of model width. This decomposi...

---

## 24. Fundamental Limits of Neural Network Sparsification: Evidence from Catastrophic Interpretability Collapse

**Authors**: Dip Roy, Rajiv Misra, Sanjay Kumar Singh  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18056  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18056v1.pdf

**Abstract**:
> arXiv:2603.18056v1 Announce Type: new 
Abstract: Extreme neural network sparsification (90% activation reduction) presents a critical challenge for mechanistic interpretability: understanding whether interpretable features survive aggressive compression. This work investigates feature survival under severe capacity constraints in hybrid Variational Autoencoder--Sparse Autoencoder (VAE-SAE) architectures. We introduce an adaptive sparsity scheduling framework that progressively reduces active neurons from 500 to 50 over 50 training epochs, and provide empirical evidence for fundamental limits of the sparsification-interpretability relationship. Testing across two benchmark datasets -- dSprites and Shapes3D -- with both Top-k and L1 sparsification methods, our key finding reveals a pervasive...

---

## 25. ARTEMIS: A Neuro Symbolic Framework for Economically Constrained Market Dynamics

**Authors**: Rahul D Ray  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18107  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18107v1.pdf

**Abstract**:
> arXiv:2603.18107v1 Announce Type: new 
Abstract: Deep learning models in quantitative finance often operate as black boxes, lacking interpretability and failing to incorporate fundamental economic principles such as no-arbitrage constraints. This paper introduces ARTEMIS (Arbitrage-free Representation Through Economic Models and Interpretable Symbolics), a novel neuro-symbolic framework combining a continuous-time Laplace Neural Operator encoder, a neural stochastic differential equation regularised by physics-informed losses, and a differentiable symbolic bottleneck that distils interpretable trading rules. The model enforces economic plausibility via two novel regularisation terms: a Feynman-Kac PDE residual penalising local no-arbitrage violations, and a market price of risk penalty bou...

---

## 26. BoundAD: Boundary-Aware Negative Generation for Time Series Anomaly Detection

**Authors**: Xiancheng Wang, Lin Wang, Zhibo Zhang, Rui Wang, Minghang Zhao  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18111  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18111v1.pdf

**Abstract**:
> arXiv:2603.18111v1 Announce Type: new 
Abstract: Contrastive learning methods for time series anomaly detection (TSAD) heavily depend on the quality of negative sample construction. However, existing strategies based on random perturbations or pseudo-anomaly injection often struggle to simultaneously preserve temporal semantic consistency and provide effective decision-boundary supervision. Most existing methods rely on prior anomaly injection, while overlooking the potential of generating hard negatives near the data manifold boundary directly from normal samples themselves. To address this issue, we propose a reconstruction-driven boundary negative generation framework that automatically constructs hard negatives through the reconstruction process of normal samples. Specifically, the met...

---

## 27. R2-Dreamer: Redundancy-Reduced World Models without Decoders or Augmentation

**Authors**: Naoki Morihira (Honda R and D Co. Ltd, The University of Tokyo), Amal Nahar (Honda R and D Co. Ltd),...  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18202  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18202v1.pdf

**Abstract**:
> arXiv:2603.18202v1 Announce Type: new 
Abstract: A central challenge in image-based Model-Based Reinforcement Learning (MBRL) is to learn representations that distill essential information from irrelevant visual details. While promising, reconstruction-based methods often waste capacity on large task-irrelevant regions. Decoder-free methods instead learn robust representations by leveraging Data Augmentation (DA), but reliance on such external regularizers limits versatility. We propose R2-Dreamer, a decoder-free MBRL framework with a self-supervised objective that serves as an internal regularizer, preventing representation collapse without resorting to DA. The core of our method is a redundancy-reduction objective inspired by Barlow Twins, which can be easily integrated into existing fra...

---

## 28. Approximate Subgraph Matching with Neural Graph Representations and Reinforcement Learning

**Authors**: Kaiyang Li, Shihao Ji, Zhipeng Cai, Wei Li  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18314  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18314v1.pdf

**Abstract**:
> arXiv:2603.18314v1 Announce Type: new 
Abstract: Approximate subgraph matching (ASM) is a task that determines the approximate presence of a given query graph in a large target graph. Being an NP-hard problem, ASM is critical in graph analysis with a myriad of applications ranging from database systems and network science to biochemistry and privacy. Existing techniques often employ heuristic search strategies, which cannot fully utilize the graph information, leading to sub-optimal solutions. This paper proposes a Reinforcement Learning based Approximate Subgraph Matching (RL-ASM) algorithm that exploits graph transformers to effectively extract graph representations and RL-based policies for ASM. Our model is built upon the branch-and-bound algorithm that selects one pair of nodes from t...

---

## 29. Learning to Reason with Curriculum I: Provable Benefits of Autocurriculum

**Authors**: Nived Rajaraman, Audrey Huang, Miro Dudik, Robert Schapire, Dylan J. Foster, Akshay Krishnamurthy  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18325  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18325v1.pdf

**Abstract**:
> arXiv:2603.18325v1 Announce Type: new 
Abstract: Chain-of-thought reasoning, where language models expend additional computation by producing thinking tokens prior to final responses, has driven significant advances in model capabilities. However, training these reasoning models is extremely costly in terms of both data and compute, as it involves collecting long traces of reasoning behavior from humans or synthetic generators and further post-training the model via reinforcement learning. Are these costs fundamental, or can they be reduced through better algorithmic design? We show that autocurriculum, where the model uses its own performance to decide which problems to focus training on, provably improves upon standard training recipes for both supervised fine-tuning (SFT) and reinforcem...

---

## 30. MLOW: Interpretable Low-Rank Frequency Magnitude Decomposition of Multiple Effects for Time Series Forecasting

**Authors**: Runze Yang, Longbing Cao, Xiaoming Wu, Xin You, Kun Fang, Jianxun Li, Jie Yang  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18432  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18432v1.pdf

**Abstract**:
> arXiv:2603.18432v1 Announce Type: new 
Abstract: Separating multiple effects in time series is fundamental yet challenging for time-series forecasting (TSF). However, existing TSF models cannot effectively learn interpretable multi-effect decomposition by their smoothing-based temporal techniques. Here, a new interpretable frequency-based decomposition pipeline MLOW captures the insight: a time series can be represented as a magnitude spectrum multiplied by the corresponding phase-aware basis functions, and the magnitude spectrum distribution of a time series always exhibits observable patterns for different effects. MLOW learns a low-rank representation of the magnitude spectrum to capture dominant trending and seasonal effects. We explore low-rank methods, including PCA, NMF, and Semi-NM...

---

## 31. SINDy-KANs: Sparse identification of non-linear dynamics through Kolmogorov-Arnold networks

**Authors**: Amanda A. Howard, Nicholas Zolman, Bruno Jacob, Steven L. Brunton, Panos Stinis  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18548  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18548v1.pdf

**Abstract**:
> arXiv:2603.18548v1 Announce Type: new 
Abstract: Kolmogorov-Arnold networks (KANs) have arisen as a potential way to enhance the interpretability of machine learning. However, solutions learned by KANs are not necessarily interpretable, in the sense of being sparse or parsimonious. Sparse identification of nonlinear dynamics (SINDy) is a complementary approach that allows for learning sparse equations for dynamical systems from data; however, learned equations are limited by the library. In this work, we present SINDy-KANs, which simultaneously train a KAN and a SINDy-like representation to increase interpretability of KAN representations with SINDy applied at the level of each activation function, while maintaining the function compositions possible through deep KANs. We apply our method ...

---

## 32. STEP: Scientific Time-Series Encoder Pretraining via Cross-Domain Distillation

**Authors**: Chen Zhang, Liwei Liu, Jun Tao, Xiaoyu Yang, Xuenan Xu, Kai Chen, Bowen Zhou, Wen Wu, Chao Zhang  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18688  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18688v1.pdf

**Abstract**:
> arXiv:2603.18688v1 Announce Type: new 
Abstract: Scientific time series are central to scientific AI but are typically sparse, highly heterogeneous, and limited in scale, making unified representation learning particularly challenging. Meanwhile, foundation models pretrained on relevant time series domains such as audio, general time series, and brain signals contain rich knowledge, but their applicability to scientific signals remains underexplored. In this paper, we investigate the transferability and complementarity of foundation models from relevant time series domains, and study how to effectively leverage them to build a unified encoder for scientific time series. We first systematically evaluate relevant foundation models, showing the effectiveness of knowledge transfer to scientifi...

---

## 33. OCP: Orthogonal Constrained Projection for Sparse Scaling in Industrial Commodity Recommendation

**Authors**: Chen Sun, Beilin Xu, Boheng Tan, Jiacheng Wang, Yuefeng Sun, Rite Bo, Ying He, Yaqiang Zang, Pinghua...  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18697  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18697v1.pdf

**Abstract**:
> arXiv:2603.18697v1 Announce Type: new 
Abstract: In industrial commodity recommendation systems, the representation quality of Item-Id vocabularies directly impacts the scalability and generalization ability of recommendation models. A key challenge is that traditional Item-Id vocabularies, when subjected to sparse scaling, suffer from low-frequency information interference, which restricts their expressive power for massive item sets and leads to representation collapse. To address this issue, we propose an Orthogonal Constrained Projection method to optimize embedding representation. By enforcing orthogonality, the projection constrains the backpropagation manifold, aligning the singular value spectrum of the learned embeddings with the orthogonal basis. This alignment ensures high singu...

---

## 34. Signals of Success and Struggle: Early Prediction and Physiological Signatures of Human Performance across Task Complexity

**Authors**: Yufei Cao, Penny Sweetser, Ziyu Chen, Xuanying Zhu  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18798  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18798v1.pdf

**Abstract**:
> arXiv:2603.18798v1 Announce Type: new 
Abstract: User performance is crucial in interactive systems, capturing how effectively users engage with task execution. Prospectively predicting performance enables the timely identification of users struggling with task demands. While ocular and cardiac signals are widely used to characterise performance-relevant visual behaviour and physiological activation, their potential for early prediction and for revealing the physiological mechanisms underlying performance differences remains underexplored. We conducted a within-subject experiment in a game environment with naturally unfolding complexity, using early ocular and cardiac signals to predict later performance and to examine physiological and self-reported group differences. Results show that th...

---

## 35. Authority-Level Priors: An Under-Specified Constraint in Hierarchical Predictive Processing

**Authors**: Marcela Palejova  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18888  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18888v1.pdf

**Abstract**:
> arXiv:2603.18888v1 Announce Type: new 
Abstract: Hierarchical predictive processing explains adaptive behaviour through precision-weighted inference. Explicit belief revision often fails to produce corresponding changes in stress reactivity or autonomic regulation. This asymmetry suggests the framework leaves under-specified a governance-level constraint concerning which identity-level hypotheses regulate autonomic and behavioural control under uncertainty. We introduce Authority-Level Priors (ALPs) as meta-structural constraints defining a regulatory-admissible subset (Hauth, a subset of H) of identity-level hypotheses. ALPs are not additional representational states nor hyperpriors over precision; they constrain which hypotheses are admissible for regulatory control. Precision determines...

---

## 36. Communication-Efficient and Robust Multi-Modal Federated Learning via Latent-Space Consensus

**Authors**: Mohamed Badi, Chaouki Ben Issaid, Mehdi Bennis  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.19067  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.19067v1.pdf

**Abstract**:
> arXiv:2603.19067v1 Announce Type: new 
Abstract: Federated learning (FL) enables collaborative model training across distributed devices without sharing raw data, but applying FL to multi-modal settings introduces significant challenges. Clients typically possess heterogeneous modalities and model architectures, making it difficult to align feature spaces efficiently while preserving privacy and minimizing communication costs. To address this, we introduce CoMFed, a Communication-Efficient Multi-Modal Federated Learning framework that uses learnable projection matrices to generate compressed latent representations. A latent-space regularizer aligns these representations across clients, improving cross-modal consistency and robustness to outliers. Experiments on human activity recognition b...

---

## 37. On Optimizing Multimodal Jailbreaks for Spoken Language Models

**Authors**: Aravind Krishnan, Karolina Sta\'nczak, Dietrich Klakow  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.19127  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.19127v1.pdf

**Abstract**:
> arXiv:2603.19127v1 Announce Type: new 
Abstract: As Spoken Language Models (SLMs) integrate speech and text modalities, they inherit the safety vulnerabilities of their LLM backbone and an expanded attack surface. SLMs have been previously shown to be susceptible to jailbreaking, where adversarial prompts induce harmful responses. Yet existing attacks largely remain unimodal, optimizing either text or audio in isolation. We explore gradient-based multimodal jailbreaks by introducing JAMA (Joint Audio-text Multimodal Attack), a joint multimodal optimization framework combining Greedy Coordinate Gradient (GCG) for text and Projected Gradient Descent (PGD) for audio, to simultaneously perturb both modalities. Evaluations across four state-of-the-art SLMs and four audio types demonstrate that ...

---

## 38. Hierarchical Latent Structure Learning through Online Inference

**Authors**: Ines Aitsahalia, Kiyohito Iigaya  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.19139  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.19139v1.pdf

**Abstract**:
> arXiv:2603.19139v1 Announce Type: new 
Abstract: Learning systems must balance generalization across experiences with discrimination of task-relevant details. Effective learning therefore requires representations that support both. Online latent-cause models support incremental inference but assume flat partitions, whereas hierarchical Bayesian models capture multilevel structure but typically require offline inference. We introduce the Hierarchical Online Learning of Multiscale Experience Structure (HOLMES) model, a computational framework for hierarchical latent structure learning through online inference. HOLMES combines a variation on the nested Chinese Restaurant Process prior with sequential Monte Carlo inference to perform tractable trial-by-trial inference over hierarchical latent ...

---

## 39. Enhancing Pretrained Model-based Continual Representation Learning via Guided Random Projection

**Authors**: Ruilin Li, Heming Zou, Xiufeng Yan, Zheming Liang, Jie Yang, Chenliang Li, Xue Yang  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.19145  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.19145v1.pdf

**Abstract**:
> arXiv:2603.19145v1 Announce Type: new 
Abstract: Recent paradigms in Random Projection Layer (RPL)-based continual representation learning have demonstrated superior performance when building upon a pre-trained model (PTM). These methods insert a randomly initialized RPL after a PTM to enhance feature representation in the initial stage. Subsequently, a linear classification head is used for analytic updates in the continual learning stage. However, under severe domain gaps between pre-trained representations and target domains, a randomly initialized RPL exhibits limited expressivity under large domain shifts. While largely scaling up the RPL dimension can improve expressivity, it also induces an ill-conditioned feature matrix, thereby destabilizing the recursive analytic updates of the l...

---

## 40. Rigorous Error Certification for Neural PDE Solvers: From Empirical Residuals to Solution Guarantees

**Authors**: Amartya Mukherjee, Maxwell Fitzsimmons, David C. Del Rey Fern\'andez, Jun Liu  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.19165  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.19165v1.pdf

**Abstract**:
> arXiv:2603.19165v1 Announce Type: new 
Abstract: Uncertainty quantification for partial differential equations is traditionally grounded in discretization theory, where solution error is controlled via mesh/grid refinement. Physics-informed neural networks fundamentally depart from this paradigm: they approximate solutions by minimizing residual losses at collocation points, introducing new sources of error arising from optimization, sampling, representation, and overfitting. As a result, the generalization error in the solution space remains an open problem.
  Our main theoretical contribution establishes generalization bounds that connect residual control to solution-space error. We prove that when neural approximations lie in a compact subset of the solution space, vanishing residual er...

---

## 41. SOL-ExecBench: Speed-of-Light Benchmarking for Real-World GPU Kernels Against Hardware Limits

**Authors**: Edward Lin, Sahil Modi, Siva Kumar Sastry Hari, Qijing Huang, Zhifan Ye, Nestor Qin, Fengzhe Zhou, Y...  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.19173  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.19173v1.pdf

**Abstract**:
> arXiv:2603.19173v1 Announce Type: new 
Abstract: As agentic AI systems become increasingly capable of generating and optimizing GPU kernels, progress is constrained by benchmarks that reward speedup over software baselines rather than proximity to hardware-efficient execution. We present SOL-ExecBench, a benchmark of 235 CUDA kernel optimization problems extracted from 124 production and emerging AI models spanning language, diffusion, vision, audio, video, and hybrid architectures, targeting NVIDIA Blackwell GPUs. The benchmark covers forward and backward workloads across BF16, FP8, and NVFP4, including kernels whose best performance is expected to rely on Blackwell-specific capabilities. Unlike prior benchmarks that evaluate kernels primarily relative to software implementations, SOL-Exe...

---

## 42. Improving RCT-Based Treatment Effect Estimation Under Covariate Mismatch via Calibrated Alignment

**Authors**: Amir Asiaee, Samhita Pal  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.19186  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.19186v1.pdf

**Abstract**:
> arXiv:2603.19186v1 Announce Type: new 
Abstract: Randomized controlled trials (RCTs) are the gold standard for estimating heterogeneous treatment effects, yet they are often underpowered for detecting effect heterogeneity. Large observational studies (OS) can supplement RCTs for conditional average treatment effect (CATE) estimation, but a key barrier is covariate mismatch: the two sources measure different, only partially overlapping, covariates. We propose CALM (Calibrated ALignment under covariate Mismatch), which bypasses imputation by learning embeddings that map each source's features into a common representation space. OS outcome models are transferred to the RCT embedding space and calibrated using trial data, preserving causal identification from randomization. Finite-sample risk ...

---

## 43. Robustness, Cost, and Attack-Surface Concentration in Phishing Detection

**Authors**: Julian Allagan, Mohamed Elbakary, Zohreh Safari, Weizheng Gao, Gabrielle Morgan, Essence Morgan, Vla...  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.19204  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.19204v1.pdf

**Abstract**:
> arXiv:2603.19204v1 Announce Type: new 
Abstract: Phishing detectors built on engineered website features attain near-perfect accuracy under i.i.d.\ evaluation, yet deployment security depends on robustness to post-deployment feature manipulation. We study this gap through a cost-aware evasion framework that models discrete, monotone feature edits under explicit attacker budgets. Three diagnostics are introduced: minimal evasion cost (MEC), the evasion survival rate $S(B)$, and the robustness concentration index (RCI).
  On the UCI Phishing Websites benchmark (11\,055 instances, 30 ternary features), Logistic Regression, Random Forests, Gradient Boosted Trees, and XGBoost all achieve $\mathrm{AUC}\ge 0.979$ under static evaluation. Under budgeted sanitization-style evasion, robustness conve...

---

## 44. Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems

**Authors**: Scott Thornton  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18034  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18034v1.pdf

**Abstract**:
> arXiv:2603.18034v1 Announce Type: cross 
Abstract: Retrieval-Augmented Generation (RAG) systems extend large language models (LLMs) with external knowledge sources but introduce new attack surfaces through the retrieval pipeline. In particular, adversaries can poison retrieval corpora so that malicious documents are preferentially retrieved at inference time, enabling targeted manipulation of model outputs. We study gradient-guided corpus poisoning attacks against modern RAG pipelines and evaluate retrieval-layer defenses that require no modification to the underlying LLM.
  We implement dual-document poisoning attacks consisting of a sleeper document and a trigger document optimized using Greedy Coordinate Gradient (GCG). In a large-scale evaluation on the Security Stack Exchange corpus (...

---

## 45. A Novel Framework using Intuitionistic Fuzzy Logic with U-Net and U-Net++ Architecture: A case Study of MRI Bain Image Segmentation

**Authors**: Hanuman Verma, Kiho Im, Akshansh Gupta, M. Tanveer  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18042  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18042v1.pdf

**Abstract**:
> arXiv:2603.18042v1 Announce Type: cross 
Abstract: Accurate segmentation of brain images from magnetic resonance imaging (MRI) scans plays a pivotal role in brain image analysis and the diagnosis of neurological disorders. Deep learning algorithms, particularly U-Net and U-Net++, are widely used for image segmentation. However, it finds difficult to deal with uncertainty in images. To address this challenge, this work integrates intuitionistic fuzzy logic into U-Net and U-Net++, propose a novel framework, named as IFS U-Net and IFS U-Net++. These models accept input data in an intuitionistic fuzzy representation to manage uncertainty arising from vague ness and imprecise data. This approach effectively handles tissue ambiguity caused by the partial volume effect and boundary uncertainties....

---

## 46. CytoSyn: a Foundation Diffusion Model for Histopathology -- Tech Report

**Authors**: Thomas Duboudin, Xavier Fontaine, Etienne Andrier, Lionel Guillou, Alexandre Filiot, Thalyssa Baiocc...  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18089  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18089v1.pdf

**Abstract**:
> arXiv:2603.18089v1 Announce Type: cross 
Abstract: Computational pathology has made significant progress in recent years, fueling advances in both fundamental disease understanding and clinically ready tools. This evolution is driven by the availability of large amounts of digitized slides and specialized deep learning methods and models. Multiple self-supervised foundation feature extractors have been developed, enabling downstream predictive applications from cell segmentation to tumor sub-typing and survival analysis. In contrast, generative foundation models designed specifically for histopathology remain scarce. Such models could address tasks that are beyond the capabilities of feature extractors, such as virtual staining. In this paper, we introduce CytoSyn, a state-of-the-art found...

---

## 47. MAED: Mathematical Activation Error Detection for Mitigating Physical Fault Attacks in DNN Inference

**Authors**: Kasra Ahmadi, Saeed Aghapour, Mehran Mozaffari Kermani, Reza Azarderakhsh  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18120  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18120v1.pdf

**Abstract**:
> arXiv:2603.18120v1 Announce Type: cross 
Abstract: The inference phase of deep neural networks (DNNs) in embedded systems is increasingly vulnerable to fault attacks and failures, which can result in incorrect predictions. These vulnerabilities can potentially lead to catastrophic consequences, making the development of effective mitigation techniques essential. In this paper, we introduce MAED (Mathematical Activation Error Detection), an algorithm-level error detection framework that exploits mathematical identities to continuously validate the correctness of non-linear activation function computations at runtime. To the best of our knowledge, this work is the first to integrate algorithm-level error detection techniques to defend against both malicious fault injection attacks and natura...

---

## 48. HRI-SA: A Multimodal Dataset for Online Assessment of Human Situational Awareness during Remote Human-Robot Teaming

**Authors**: Hashini Senaratne, Richard Attfield, Samith Widhanapathirana, David Howard, Cecile Paris, Dana Kulic...  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18344  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18344v1.pdf

**Abstract**:
> arXiv:2603.18344v1 Announce Type: cross 
Abstract: Maintaining situational awareness (SA) is critical in human-robot teams. Yet, under high workload and dynamic conditions, operators often experience SA gaps. Automated detection of SA gaps could provide timely assistance for operators. However, conventional SA measures either disrupt task flow or cannot capture real-time fluctuations, limiting their operational utility. To the best of our knowledge, no publicly available dataset currently supports the systematic evaluation of online human SA assessment in human-robot teaming. To advance the development of online SA assessment tools, we introduce HRI-SA, a multimodal dataset from 30 participants in a realistic search-and-rescue human-robot teaming context, incorporating eye movements, pupil...

---

## 49. Multi-Domain Causal Empirical Bayes Under Linear Mixing

**Authors**: Bohan Wu, Julius von K\"ugelgen, David M. Blei  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18404  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18404v1.pdf

**Abstract**:
> arXiv:2603.18404v1 Announce Type: cross 
Abstract: Causal representation learning (CRL) aims to learn low-dimensional causal latent variables from high-dimensional observations. While identifiability has been extensively studied for CRL, estimation has been less explored. In this paper, we explore the use of empirical Bayes (EB) to estimate causal representations. In particular, we consider the problem of learning from data from multiple domains, where differences between domains are modeled by interventions in a shared underlying causal model. Multi-domain CRL naturally poses a simultaneous inference problem that EB is designed to tackle. Here, we propose an EB $f$-modeling algorithm that improves the quality of learned causal variables by exploiting invariant structure within and across ...

---

## 50. Learning Decision-Sufficient Representations for Linear Optimization

**Authors**: Yuhan Ye, Saurabh Amin, Asuman Ozdauglar  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18551  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18551v1.pdf

**Abstract**:
> arXiv:2603.18551v1 Announce Type: cross 
Abstract: We study how to construct compressed datasets that suffice to recover optimal decisions in linear programs with an unknown cost vector $c$ lying in a prior set $\mathcal{C}$. Recent work by Bennouna et al. provides an exact geometric characterization of sufficient decision datasets (SDDs) via an intrinsic decision-relevant dimension $d^\star$. However, their algorithm for constructing minimum-size SDDs requires solving mixed-integer programs. In this paper, we establish hardness results showing that computing $d^\star$ is NP-hard and deciding whether a dataset is globally sufficient is coNP-hard, thereby resolving a recent open problem posed by Bennouna et al. To address this worst-case intractability, we introduce pointwise sufficiency, a...

---

## 51. CausalVAD: De-confounding End-to-End Autonomous Driving via Causal Intervention

**Authors**: Jiacheng Tang, Zhiyuan Zhou, Zhuolin He, Jia Zhang, Kai Zhang, Jian Pu  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18561  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18561v1.pdf

**Abstract**:
> arXiv:2603.18561v1 Announce Type: cross 
Abstract: Planning-oriented end-to-end driving models show great promise, yet they fundamentally learn statistical correlations instead of true causal relationships. This vulnerability leads to causal confusion, where models exploit dataset biases as shortcuts, critically harming their reliability and safety in complex scenarios. To address this, we introduce CausalVAD, a de-confounding training framework that leverages causal intervention. At its core, we design the sparse causal intervention scheme (SCIS), a lightweight, plug-and-play module to instantiate the backdoor adjustment theory in neural networks. SCIS constructs a dictionary of prototypes representing latent driving contexts. It then uses this dictionary to intervene on the model's spars...

---

## 52. SwiftGS: Episodic Priors for Immediate Satellite Surface Recovery

**Authors**: Rong Fu, Jiekai Wu, Haiyun Wei, Xiaowen Ma, Shiyin Lin, Kangan Qian, Chuang Liu, Jianyuan Ni, Simon ...  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18634  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18634v1.pdf

**Abstract**:
> arXiv:2603.18634v1 Announce Type: cross 
Abstract: Rapid, large-scale 3D reconstruction from multi-date satellite imagery is vital for environmental monitoring, urban planning, and disaster response, yet remains difficult due to illumination changes, sensor heterogeneity, and the cost of per-scene optimization. We introduce SwiftGS, a meta-learned system that reconstructs 3D surfaces in a single forward pass by predicting geometry-radiation-decoupled Gaussian primitives together with a lightweight SDF, replacing expensive per-scene fitting with episodic training that captures transferable priors. The model couples a differentiable physics graph for projection, illumination, and sensor response with spatial gating that blends sparse Gaussian detail and global SDF structure, and incorporates...

---

## 53. Towards Interpretable Foundation Models for Retinal Fundus Images

**Authors**: Samuel Ofosu Mensah, Maria Camila Roa Carvajal, Kerol Djoumessi, Philipp Berens  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18846  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18846v1.pdf

**Abstract**:
> arXiv:2603.18846v1 Announce Type: cross 
Abstract: Foundation models are used to extract transferable representations from large amounts of unlabeled data, typically via self-supervised learning (SSL). However, many of these models rely on architectures that offer limited interpretability, which is a critical issue in high-stakes domains such as medical imaging. We propose Dual-IFM, a foundation model that is interpretable-by-design in two ways: First, it provides local interpretability for individual images through class evidence maps that are faithful to the decision-making process. Second, it provides global interpretability for entire datasets through a 2D projection layer that allows for direct visualization of the model's representation space. We trained our model on over 800,000 col...

---

## 54. CRAFT: Aligning Diffusion Models with Fine-Tuning Is Easier Than You Think

**Authors**: Zening Sun, Zhengpeng Xie, Lichen Bai, Shitong Shao, Shuo Yang, Zeke Xie  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18991  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18991v1.pdf

**Abstract**:
> arXiv:2603.18991v1 Announce Type: cross 
Abstract: Aligning Diffusion models has achieved remarkable breakthroughs in generating high-quality, human preference-aligned images. Existing techniques, such as supervised fine-tuning (SFT) and DPO-style preference optimization, have become principled tools for fine-tuning diffusion models. However, SFT relies on high-quality images that are costly to obtain, while DPO-style methods depend on large-scale preference datasets, which are often inconsistent in quality. Beyond data dependency, these methods are further constrained by computational inefficiency. To address these two challenges, we propose Composite Reward Assisted Fine-Tuning (CRAFT), a lightweight yet powerful fine-tuning paradigm that requires significantly reduced training data whil...

---

## 55. Towards Verifiable AI with Lightweight Cryptographic Proofs of Inference

**Authors**: Pranay Anchuri, Matteo Campanelli, Paul Cesaretti, Rosario Gennaro, Tushar M. Jois, Hasan S. Kayman,...  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.19025  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.19025v1.pdf

**Abstract**:
> arXiv:2603.19025v1 Announce Type: cross 
Abstract: When large AI models are deployed as cloud-based services, clients have no guarantee that responses are correct or were produced by the intended model. Rerunning inference locally is infeasible for large models, and existing cryptographic proof systems -- while providing strong correctness guarantees -- introduce prohibitive prover overhead (e.g., hundreds of seconds per query for billion-parameter models). We present a verification framework and protocol that replaces full cryptographic proofs with a lightweight, sampling-based approach grounded in statistical properties of neural networks. We formalize the conditions under which trace separation between functionally dissimilar models can be leveraged to argue the security of verifiable i...

---

## 56. SEM: Sparse Embedding Modulation for Post-Hoc Debiasing of Vision-Language Models

**Authors**: Quentin Guimard, Federico Bartsch, Simone Caldarella, Rahaf Aljundi, Elisa Ricci, Massimiliano Manci...  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.19028  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.19028v1.pdf

**Abstract**:
> arXiv:2603.19028v1 Announce Type: cross 
Abstract: Models that bridge vision and language, such as CLIP, are key components of multimodal AI, yet their large-scale, uncurated training data introduce severe social and spurious biases. Existing post-hoc debiasing methods often operate directly in the dense CLIP embedding space, where bias and task-relevant information are highly entangled. This entanglement limits their ability to remove bias without degrading semantic fidelity. In this work, we propose Sparse Embedding Modulation (SEM), a post-hoc, zero-shot debiasing framework that operates in a Sparse Autoencoder (SAE) latent space. By decomposing CLIP text embeddings into disentangled features, SEM identifies and modulates bias-relevant neurons while preserving query-relevant ones. This ...

---

## 57. Meanings and Measurements: Multi-Agent Probabilistic Grounding for Vision-Language Navigation

**Authors**: Swagat Padhan, Lakshya Jain, Bhavya Minesh Shah, Omkar Patil, Thao Nguyen, Nakul Gopalan  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.19166  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.19166v1.pdf

**Abstract**:
> arXiv:2603.19166v1 Announce Type: cross 
Abstract: Robots collaborating with humans must convert natural language goals into actionable, physically grounded decisions. For example, executing a command such as "go two meters to the right of the fridge" requires grounding semantic references, spatial relations, and metric constraints within a 3D scene. While recent vision language models (VLMs) demonstrate strong semantic grounding capabilities, they are not explicitly designed to reason about metric constraints in physically defined spaces. In this work, we empirically demonstrate that state-of-the-art VLM-based grounding approaches struggle with complex metric-semantic language queries. To address this limitation, we propose MAPG (Multi-Agent Probabilistic Grounding), an agentic framework ...

---

## 58. The Exponentially Weighted Signature

**Authors**: Alexandre Bloch, Samuel N. Cohen, Terry Lyons, Jo\"el Mouterde, Benjamin Walker  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.19198  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.19198v1.pdf

**Abstract**:
> arXiv:2603.19198v1 Announce Type: cross 
Abstract: The signature is a canonical representation of a multidimensional path over an interval. However, it treats all historical information uniformly, offering no intrinsic mechanism for contextualising the relevance of the past. To address this, we introduce the Exponentially Weighted Signature (EWS), generalising the Exponentially Fading Memory (EFM) signature from diagonal to general bounded linear operators. These operators enable cross-channel coupling at the level of temporal weighting together with richer memory dynamics including oscillatory, growth, and regime-dependent behaviour, while preserving the algebraic strengths of the classical signature. We show that the EWS is the unique solution to a linear controlled differential equation...

---

## 59. Inverse classification with logistic and softmax classifiers: efficient optimization

**Authors**: Miguel \'A. Carreira-Perpi\~n\'an, Suryabhan Singh Hada  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2309.08945  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2309.08945v2.pdf

**Abstract**:
> arXiv:2309.08945v2 Announce Type: replace 
Abstract: In recent years, a certain type of problems have become of interest where one wants to query a trained classifier. Specifically, one wants to find the closest instance to a given input instance such that the classifier's predicted label is changed in a desired way. Examples of these "inverse classification" problems are counterfactual explanations, adversarial examples and model inversion. All of them are fundamentally optimization problems over the input instance vector involving a fixed classifier, and it is of interest to achieve a fast solution for interactive or real-time applications. We focus on solving this problem efficiently with the squared Euclidean distance for two of the most widely used classifiers: logistic regression and...

---

## 60. On Minimal Depth in Neural Networks

**Authors**: Juan L. Valerdi  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2402.15315  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2402.15315v5.pdf

**Abstract**:
> arXiv:2402.15315v5 Announce Type: replace 
Abstract: Understanding the relationship between the depth of a neural network and its representational capacity is a central problem in deep learning theory. In this work, we develop a geometric framework to analyze the expressivity of ReLU networks with the notion of depth complexity for convex polytopes. The depth of a polytope recursively quantifies the number of alternating convex hull and Minkowski sum operations required to construct it. This geometric perspective serves as a rigorous tool for deriving depth lower bounds and understanding the structural limits of deep neural architectures.
  We establish lower and upper bounds on the depth of polytopes, as well as tight bounds for classical families. These results yield two main consequence...

---

## 61. Modality Equilibrium Matters: Minor-Modality-Aware Adaptive Alternating for Cross-Modal Memory Enhancement

**Authors**: Xiang Shi, Rui Zhang, Jiawei Liu, Yinpeng Liu, Qikai Cheng, Wei Lu  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2506.00030  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2506.00030v2.pdf

**Abstract**:
> arXiv:2506.00030v2 Announce Type: replace 
Abstract: Multimodal fusion is susceptible to modality imbalance, where dominant modalities overshadow weak ones, easily leading to biased learning and suboptimal fusion, especially for incomplete modality conditions. To address this problem, we propose a Shapley-guided alternating training framework that adaptively prioritizes minor modalities to balance and thus enhance the fusion. Our method leverages Shapley Value-based scheduling to improve the training sequence adaptively, ensuring that under-optimized modalities receive sufficient learning. Additionally, we introduce the memory module to refine and inherit modality-specific representations with a cross-modal mapping mechanism to align features at both the feature and sample levels. To furth...

---

## 62. Activation Quantization of Vision Encoders Needs Prefixing Registers

**Authors**: Seunghyeon Kim, Taesun Yeom, Jinho Kim, Wonpyo Park, Kyuyeun Kim, Jaeho Lee  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.04547  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.04547v4.pdf

**Abstract**:
> arXiv:2510.04547v4 Announce Type: replace 
Abstract: Large pretrained vision encoders are central to multimodal intelligence, powering applications from on-device vision processing to vision-language models. Since these applications often demand real-time processing of massive visual data, reducing the inference cost of vision encoders is critical. Quantization offers a practical path, but it remains challenging even at 8-bit precision due to so-called outliers. In this work, we propose $\textit{RegCache}$, a training-free algorithm that mitigates outliers in large-scale pretrained vision encoders and serves as a plug-in module that can be applied on top of other quantization methods. RegCache introduces outlier-prone yet semantically meaningless prefix tokens to the vision encoder, which ...

---

## 63. Heads collapse, features stay: Why Replay needs big buffers

**Authors**: Giulia Lanzillotta, Damiano Meier, Thomas Hofmann  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2512.07400  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2512.07400v2.pdf

**Abstract**:
> arXiv:2512.07400v2 Announce Type: replace 
Abstract: A persistent paradox in continual learning (CL) is that neural networks often retain linearly separable representations of past tasks even when their output predictions fail. We formalize this distinction as the gap between deep (feature-space) and shallow (classifier-level) forgetting. We reveal a critical asymmetry in Experience Replay: while minimal buffers successfully anchor feature geometry and prevent deep forgetting, mitigating shallow forgetting typically requires substantially larger buffer capacities. To explain this, we extend the Neural Collapse framework to the sequential setting. We characterize deep forgetting as a geometric drift toward out-of-distribution subspaces and prove that any non-zero replay fraction asymptotica...

---

## 64. Weights to Code: Extracting Interpretable Algorithms from the Discrete Transformer

**Authors**: Yifan Zhang, Wei Bi, Kechi Zhang, Dongming Jin, Jie Fu, Zhi Jin  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2601.05770  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2601.05770v2.pdf

**Abstract**:
> arXiv:2601.05770v2 Announce Type: replace 
Abstract: Algorithm extraction aims to synthesize executable programs directly from models trained on algorithmic tasks, enabling de novo algorithm discovery without relying on human-written code. However, applying this paradigm to Transformer is hindered by representation entanglement (e.g., superposition), where entangled features encoded in overlapping directions obstruct the recovery of symbolic expressions. We propose the Discrete Transformer, an architecture explicitly designed to bridge the gap between continuous representations and discrete symbolic logic. By injecting discreteness through temperature-annealed sampling, our framework effectively leverages hypothesis testing and symbolic regression to extract human-readable programs. Empiri...

---

## 65. DeeperBrain: A Neuro-Grounded EEG Foundation Model Towards Universal BCI

**Authors**: Jiquan Wang, Sha Zhao, Yangxuan Zhou, Yiming Kang, Shijian Li, Gang Pan  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2601.06134  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2601.06134v2.pdf

**Abstract**:
> arXiv:2601.06134v2 Announce Type: replace 
Abstract: Electroencephalography (EEG) foundation models hold significant promise for universal Brain-Computer Interfaces (BCIs). However, existing approaches often rely on end-to-end fine-tuning and exhibit limited efficacy under frozen-probing protocols, lacking the intrinsic universality required for broad generalization. This limitation stems from adapting general-purpose sequence architectures that overlook the biophysical and dynamical principles of neural activity. To bridge this gap, we propose DeeperBrain, a neuro-grounded foundation model integrating domain-specific inductive biases into its model design and learning objectives. Architecturally, DeeperBrain incorporates a volume conduction-aware channel encoding to model spatial mixing v...

---

## 66. Multimodal Machine Learning for Soft High-k Elastomers under Data Scarcity

**Authors**: Brijesh FNU, Viet Thanh Duy Nguyen, Ashima Sharma, Md Harun Rashid Molla, Chengyi Xu, Truong-Son Hy  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2601.18032  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2601.18032v2.pdf

**Abstract**:
> arXiv:2601.18032v2 Announce Type: replace 
Abstract: Dielectric materials are critical building blocks for modern electronics such as sensors, actuators, and transistors. With rapid advances in soft and stretchable electronics for emerging human- and robot-interfacing applications, there is a growing need for high-performance dielectric elastomers. However, developing soft elastomers that simultaneously exhibit high dielectric constants (k) and low Young's moduli (E) remains a major challenge. Although individual elastomer designs have been reported, structured datasets that systematically integrate molecular sequence, dielectric, and mechanical properties are largely unavailable. To address this gap, we curate a compact, high-quality dataset of acrylate-based dielectric elastomers by aggr...

---

## 67. Krause Synchronization Transformers

**Authors**: Jingkun Liu, Yisong Yue, Max Welling, Yue Song  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.11534  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.11534v2.pdf

**Abstract**:
> arXiv:2602.11534v2 Announce Type: replace 
Abstract: Self-attention in Transformers relies on globally normalized softmax weights, causing all tokens to compete for influence at every layer. When composed across depth, this interaction pattern induces strong synchronization dynamics that favor convergence toward a dominant mode, a behavior associated with representation collapse and attention sink phenomena. We introduce Krause Attention, a principled attention mechanism inspired by bounded-confidence consensus dynamics. Krause Attention replaces similarity-based global aggregation with distance-based, localized, and selectively sparse interactions, promoting structured local synchronization instead of global mixing. We relate this behavior to recent theory modeling Transformer dynamics as...

---

## 68. Causality is Key for Interpretability Claims to Generalise

**Authors**: Shruti Joshi, Aaron Mueller, David Klindt, Wieland Brendel, Patrik Reizinger, Dhanya Sridhar  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.16698  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.16698v2.pdf

**Abstract**:
> arXiv:2602.16698v2 Announce Type: replace 
Abstract: Interpretability research on large language models (LLMs) has yielded important insights into model behaviour, yet recurring pitfalls persist: findings that do not generalise, and causal interpretations that outrun the evidence. Our position is that causal inference specifies what constitutes a valid mapping from model activations to invariant high-level structures, the data or assumptions needed to achieve it, and the inferences it can support. Specifically, Pearl's causal hierarchy clarifies what an interpretability study can justify. Observations establish associations between model behaviour and internal components. Interventions (e.g., ablations or activation patching) support claims how these edits affect a behavioural metric (e.g....

---

## 69. Stable Deep Reinforcement Learning via Isotropic Gaussian Representations

**Authors**: Ali Saheb Pasand, Johan Obando-Ceron, Aaron Courville, Pouya Bashivan, Pablo Samuel Castro  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.19373  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.19373v2.pdf

**Abstract**:
> arXiv:2602.19373v2 Announce Type: replace 
Abstract: Deep reinforcement learning systems often suffer from unstable training dynamics due to non-stationarity, where learning objectives and data distributions evolve over time. We show that under non-stationary targets, isotropic Gaussian embeddings are provably advantageous. In particular, they induce stable tracking of time-varying targets for linear readouts, achieve maximal entropy under a fixed variance budget, and encourage a balanced use of all representational dimensions--all of which enable agents to be more adaptive and stable. Building on this insight, we propose the use of Sketched Isotropic Gaussian Regularization for shaping representations toward an isotropic Gaussian distribution during training. We demonstrate empirically, o...

---

## 70. Improving Spatial Allocation for Energy System Coupling with Graph Neural Networks

**Authors**: Xuanhao Mu, Jakob Geiges, Nan Liu, Thorsten Schlachter, Veit Hagenmeyer  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.22249  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.22249v2.pdf

**Abstract**:
> arXiv:2602.22249v2 Announce Type: replace 
Abstract: In energy system analysis, coupling models with mismatched spatial resolutions is a significant challenge. A common solution is assigning weights to high-resolution geographic units for aggregation, but traditional models are limited by using only a single geospatial attribute. This paper presents an innovative method employing a self-supervised Heterogeneous Graph Neural Network to address this issue. This method models high-resolution geographic units as graph nodes, integrating various geographical features to generate physically meaningful weights for each grid point. These weights enhance the conventional Voronoi-based allocation method, allowing it to go beyond simply geographic proximity by incorporating essential geographic infor...

---

## 71. Nonparametric Variational Differential Privacy via Embedding Parameter Clipping

**Authors**: Dina El Zein, Shashi Kumar, James Henderson  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.09583  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.09583v2.pdf

**Abstract**:
> arXiv:2603.09583v2 Announce Type: replace 
Abstract: The nonparametric variational information bottleneck (NVIB) provides the foundation for nonparametric variational differential privacy (NVDP), a framework for building privacy-preserving language models. However, the learned latent representations can drift into regions with high information content, leading to poor privacy guarantees, but also low utility due to numerical instability during training. In this work, we introduce a principled parameter clipping strategy to directly address this issue. Our method is mathematically derived from the objective of minimizing the R\'enyi Divergence (RD) upper bound, yielding specific, theoretically grounded constraints on the posterior mean, variance, and mixture weight parameters. We apply our ...

---

## 72. Representation Finetuning for Continual Learning

**Authors**: Haihua Luo, Xuming Ran, Tommi K\"arkk\"ainen, Huiyan Xue, Zhonghua Chen, Qi Xu, Fengyu Cong  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11201  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11201v2.pdf

**Abstract**:
> arXiv:2603.11201v2 Announce Type: replace 
Abstract: The world is inherently dynamic, and continual learning aims to enable models to adapt to ever-evolving data streams. While pre-trained models have shown powerful performance in continual learning, they still require finetuning to adapt effectively to downstream tasks. However, prevailing Parameter-Efficient Fine-Tuning (PEFT) methods operate through empirical, black-box optimization at the weight level. These approaches lack explicit control over representation drift, leading to sensitivity to domain shifts and catastrophic forgetting in continual learning scenarios. In this work, we introduce Continual Representation Learning (CoRe), a novel framework that for the first time shifts the finetuning paradigm from weight space to represent...

---

## 73. PREBA: Surgical Duration Prediction via PCA-Weighted Retrieval-Augmented LLMs and Bayesian Averaging Aggregation

**Authors**: Wanyin Wu, Kanxue Li, Baosheng Yu, Haoyun Zhao, Yibing Zhan, Dapeng Tao, Hua Jin  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.13275  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.13275v2.pdf

**Abstract**:
> arXiv:2603.13275v2 Announce Type: replace 
Abstract: Accurate prediction of surgical duration is pivotal for hospital resource management. Although recent supervised learning approaches-from machine learning (ML) to fine-tuned large language models (LLMs)-have shown strong performance, they remain constrained by the need for high-quality labeled data and computationally intensive training. In contrast, zero-shot LLM inference offers a promising training-free alternative but it lacks grounding in institution-specific clinical context (e.g., local demographics and case-mix distributions), making its predictions clinically misaligned and prone to instability. To address these limitations, we present PREBA, a retrieval-augmented framework that integrates PCA-weighted retrieval and Bayesian ave...

---

## 74. Exploring AI in Fashion: A Review of Aesthetics, Personalization, Virtual Try-On, and Forecasting

**Authors**: Laila Khalid, Wei Gong  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2101.08301  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2101.08301v2.pdf

**Abstract**:
> arXiv:2101.08301v2 Announce Type: replace-cross 
Abstract: Fashion-focused artificial intelligence has rapidly advanced in recent years, driven by deep learning and its deployment in recommender systems, detection, retrieval, and analytics. Yet several consumer-facing domains remain comparatively under-surveyed despite their practical impact. This work provides a comprehensive review of methods, datasets, and evaluation metrics across four such domains: aesthetics, personalization, virtual try-on, and forecasting. We synthesize technical approaches spanning representation learning, preference modeling, image transformation, and time-series analysis; relate them to downstream recommender systems and user experience; and highlight cross-domain dependencies (e.g., aesthetics-informed personal...

---

## 75. Soft-Di[M]O: Improving One-Step Discrete Image Generation with Soft Embeddings

**Authors**: Yuanzhi Zhu, Xi Wang, St\'ephane Lathuili\`ere, Vicky Kalogeiton  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2509.22925  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2509.22925v2.pdf

**Abstract**:
> arXiv:2509.22925v2 Announce Type: replace-cross 
Abstract: One-step generators distilled from Masked Diffusion Models (MDMs) compress multiple sampling steps into a single forward pass, enabling efficient text and image synthesis. However, they suffer two key limitations: they inherit modeling bias from the teacher, and their discrete token outputs block gradient flow, preventing post-distillation refinements such as adversarial training, reward-based fine-tuning, and Test-Time Embedding Optimization (TTEO). In this work, we introduce soft embeddings, a simple relaxation that replaces discrete tokens with the expected embeddings under the generator's output distribution. Soft embeddings preserve representation fidelity for one-step discrete generator while providing a fully differentiable ...

---

## 76. Towards more holistic interpretability: A lightweight disentangled Concept Bottleneck Model

**Authors**: Gaoxiang Huang, Songning Lai, Yutao Yue  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.15770  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.15770v2.pdf

**Abstract**:
> arXiv:2510.15770v2 Announce Type: replace-cross 
Abstract: Concept Bottleneck Models (CBMs) enhance interpretability by predicting human-understandable concepts as intermediate representations. However, existing CBMs often suffer from input-to-concept mapping bias and limited controllability, which restricts their practical utility and undermines the reliability of concept-based strategies. To address these challenges, we propose a Lightweight Disentangled Concept Bottleneck Model (LDCBM) that automatically groups visual features into semantically meaningful components without the need for region annotations. By introducing a filter grouping loss and joint concept supervision, our method improves the alignment between visual patterns and concepts, enabling more transparent and robust decis...

---

## 77. A Structured Nonparametric Framework for Nonlinear Accelerated Failure Time Models (KAN-AFT)

**Authors**: Mebin Jose, Jisha Francis, Sudheesh Kumar Kattumannil  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2512.20305  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2512.20305v2.pdf

**Abstract**:
> arXiv:2512.20305v2 Announce Type: replace-cross 
Abstract: Accelerated failure time (AFT) models provide a direct and interpretable time-scale description of covariate effects in lifetime data analysis, but classical formulations rely on linear predictors and are therefore limited in their ability to represent nonlinear relationships. Moreover, in heterogeneous clinical settings with complex covariate structures and varying censoring mechanisms, standard survival models such as the Cox proportional hazards model or AFT formulations may be inadequate due to restrictive structural assumptions.
  We propose a structured nonparametric extension of the AFT framework in which the regression function governing log-survival time is an unknown smooth function represented through Kolmogorov--Arnold ...

---

## 78. Multi-Preconditioned LBFGS for Training Finite-Basis PINNs

**Authors**: Marc Salvad\'o-Benasco, Aymane Kssim, Alexander Heinlein, Rolf Krause, Serge Gratton, Alena Kopani\v...  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2601.08709  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2601.08709v2.pdf

**Abstract**:
> arXiv:2601.08709v2 Announce Type: replace-cross 
Abstract: A multi-preconditioned LBFGS (MP-LBFGS) algorithm is introduced for training finite-basis physics-informed neural networks (FBPINNs). The algorithm is motivated by the nonlinear additive Schwarz method and exploits the domain-decomposition-inspired additive architecture of FBPINNs, in which local neural networks are defined on subdomains, thereby localizing the network representation. Parallel, subdomain-local quasi-Newton corrections are then constructed on the corresponding local parts of the architecture. A key feature is a novel nonlinear multi-preconditioning mechanism, in which subdomain corrections are optimally combined through the solution of a low-dimensional subspace minimization problem. Numerical experiments indicate t...

---

## 79. Is Hierarchical Quantization Essential for Optimal Reconstruction?

**Authors**: Shirin Reyhanian, Laurenz Wiskott  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2601.22244  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2601.22244v2.pdf

**Abstract**:
> arXiv:2601.22244v2 Announce Type: replace-cross 
Abstract: Vector-quantized variational autoencoders (VQ-VAEs) are central to models that rely on high reconstruction fidelity, from neural compression to generative pipelines. Hierarchical extensions, such as VQ-VAE2, are often credited with superior reconstruction performance because they split global and local features across multiple levels. However, since higher levels derive all their information from lower levels, they should not carry additional reconstructive content beyond what the lower-level already encodes. Combined with recent advances in training objectives and quantization mechanisms, this leads us to ask whether a single-level VQ-VAE, with matched representational budget and no codebook collapse, can equal the reconstruction ...

---

## 80. 1S-DAug: One-Shot Data Augmentation for Robust Few-Shot Generalization

**Authors**: Yunwei Bai, Ying Kiat Tan, Yao Shu, Tsuhan Chen  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.00114  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.00114v2.pdf

**Abstract**:
> arXiv:2602.00114v2 Announce Type: replace-cross 
Abstract: Few-shot learning (FSL) challenges model generalization to novel classes based on just a few shots of labeled examples, a testbed where traditional test-time augmentations fail to be effective. We introduce 1S-DAug, a one-shot generative augmentation operator that synthesizes diverse yet faithful variants from just one example image at test time. 1S-DAug couples traditional geometric perturbations with controlled noise injection and a denoising diffusion process conditioned on the original image. The generated images are then encoded and aggregated, alongside the original image, into a combined representation for more robust FSL predictions. Integrated as a training-free model-agnostic plugin, 1S-DAug consistently improves FSL acro...

---

## 81. Optimal rates for density and mode estimation with expand-and-sparsify representations

**Authors**: Kaushik Sinha, Christopher Tosh  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.06175  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.06175v2.pdf

**Abstract**:
> arXiv:2602.06175v2 Announce Type: replace-cross 
Abstract: Expand-and-sparsify representations are a class of theoretical models that capture sparse representation phenomena observed in the sensory systems of many animals. At a high level, these representations map an input $x \in \mathbb{R}^d$ to a much higher dimension $m \gg d$ via random linear projections before zeroing out all but the $k \ll m$ largest entries. The result is a $k$-sparse vector in $\{0,1\}^m$. We study the suitability of this representation for two fundamental statistical problems: density estimation and mode estimation. For density estimation, we show that a simple linear function of the expand-and-sparsify representation produces an estimator with minimax-optimal $\ell_{\infty}$ convergence rates. In mode estimatio...

---

## 82. Theory and interpretability of Quantum Extreme Learning Machines: a Pauli-transfer matrix approach

**Authors**: Markus Gross, Hans-Martin Rieser  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.18377  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.18377v2.pdf

**Abstract**:
> arXiv:2602.18377v2 Announce Type: replace-cross 
Abstract: Quantum reservoir computers (QRCs) have emerged as a promising approach to quantum machine learning, since they utilize the natural dynamics of quantum systems for data processing and are simple to train. Here, we consider $n$-qubit quantum extreme learning machines (QELMs) with initial-state encoding and continuous-time reservoir dynamics. QELMs are memoryless QRCs capable of various ML tasks, such as image classification and time series forecasting. We apply the Pauli transfer matrix (PTM) formalism to theoretically analyze the influence of encoding, reservoir dynamics, and measurement operations (including temporal multiplexing) on the QELM performance. This formalism makes explicit that the encoding determines the complete set ...

---

## 83. Bridging the Simulation-to-Reality Gap in Electron Microscope Calibration via VAE-EM Estimation

**Authors**: Jilles S. van Hulst, W. P. M. H. Heemels, Duarte J. Antunes  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16549  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16549v2.pdf

**Abstract**:
> arXiv:2603.16549v2 Announce Type: replace-cross 
Abstract: Electron microscopy has enabled many scientific breakthroughs across multiple fields. A key challenge is the tuning of microscope parameters based on images to overcome optical aberrations that deteriorate image quality. This calibration problem is challenging due to the high-dimensional and noisy nature of the diagnostic images, and the fact that optimal parameters cannot be identified from a single image. We tackle the calibration problem for Scanning Transmission Electron Microscopes (STEM) by employing variational autoencoders (VAEs), trained on simulated data, to learn low-dimensional representations of images, whereas most existing methods extract only scalar values. We then simultaneously estimate the model that maps calibra...

---

## 84. Probing Cultural Signals in Large Language Models through Author Profiling

**Authors**: Valentin Lafargue, Ariel Guerra-Adames, Emmanuelle Claeys, Elouan Vuichard, Jean-Michel Loubes  
**Categories**: cs.LG  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.16749  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.16749v2.pdf

**Abstract**:
> arXiv:2603.16749v2 Announce Type: replace-cross 
Abstract: Large language models (LLMs) are increasingly deployed in applications with societal impact, raising concerns about the cultural biases they encode. We probe these representations by evaluating whether LLMs can perform author profiling from song lyrics in a zero-shot setting, inferring singers' gender and ethnicity without task-specific fine-tuning. Across several open-source models evaluated on more than 10,000 lyrics, we find that LLMs achieve non-trivial profiling performance but demonstrate systematic cultural alignment: most models default toward North American ethnicity, while DeepSeek-1.5B aligns more strongly with Asian ethnicity. This finding emerges from both the models' prediction distributions and an analysis of their g...

---

## 85. Continually self-improving AI

**Authors**: Zitong Yang  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18073  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18073v1.pdf

**Abstract**:
> arXiv:2603.18073v1 Announce Type: new 
Abstract: Modern language model-based AI systems are remarkably powerful, yet their capabilities remain fundamentally capped by their human creators in three key ways. First, although a model's weights can be updated via fine-tuning, acquiring new knowledge from small, specialized corpora after pretraining remains highly data-inefficient. Second, the training of these systems relies heavily on finite, human-generated data from across history. Third, the pipelines used to train AI models are confined by the algorithms that human researchers can discover and explore. This thesis takes a small step toward overcoming these inherent limitations, presenting three chapters aimed at breaking these dependencies to create continually self-improving AI. First, t...

---

## 86. TeachingCoach: A Fine-Tuned Scaffolding Chatbot for Instructional Guidance to Instructors

**Authors**: Isabel Molnar, Peiyu Li, Si Chen, Sugana Chawla, James Lang, Ronald Metoyer, Ting Hua, Nitesh V. Cha...  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18189  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18189v1.pdf

**Abstract**:
> arXiv:2603.18189v1 Announce Type: new 
Abstract: Higher education instructors often lack timely and pedagogically grounded support, as scalable instructional guidance remains limited and existing tools rely on generic chatbot advice or non-scalable teaching center human-human consultations. We present TeachingCoach, a pedagogically grounded chatbot designed to support instructor professional development through real-time, conversational guidance. TeachingCoach is built on a data-centric pipeline that extracts pedagogical rules from educational resources and uses synthetic dialogue generation to fine-tune a specialized language model that guides instructors through problem identification, diagnosis, and strategy development. Expert evaluations show TeachingCoach produces clearer, more refle...

---

## 87. The Validity Gap in Health AI Evaluation: A Cross-Sectional Analysis of Benchmark Composition

**Authors**: Alvin Rajkomar, Pavan Sudarshan, Angela Lai, Lily Peng  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18294  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18294v1.pdf

**Abstract**:
> arXiv:2603.18294v1 Announce Type: new 
Abstract: Background: Clinical trials rely on transparent inclusion criteria to ensure generalizability. In contrast, benchmarks validating health-related large language models (LLMs) rarely characterize the "patient" or "query" populations they contain. Without defined composition, aggregate performance metrics may misrepresent model readiness for clinical use.
  Methods: We analyzed 18,707 consumer health queries across six public benchmarks using LLMs as automated coding instruments to apply a standardized 16-field taxonomy profiling context, topic, and intent.
  Results: We identified a structural "validity gap." While benchmarks have evolved from static retrieval to interactive dialogue, clinical composition remains misaligned with real-world nee...

---

## 88. Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations

**Authors**: Sanjay Basu, Sadiq Y. Patel, Parth Sheth, Bhairavi Muralidharan, Namrata Elamaran, Aakriti Kinra, Jo...  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18353  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18353v1.pdf

**Abstract**:
> arXiv:2603.18353v1 Announce Type: new 
Abstract: Language models encode task-relevant knowledge in internal representations that far exceeds their output performance, but whether mechanistic interpretability methods can bridge this knowledge-action gap has not been systematically tested. We compared four mechanistic interpretability methods -- concept bottleneck steering (Steerling-8B), sparse autoencoder feature steering, logit lens with activation patching, and linear probing with truthfulness separator vector steering (Qwen 2.5 7B Instruct) -- for correcting false-negative triage errors using 400 physician-adjudicated clinical vignettes (144 hazards, 256 benign). Linear probes discriminated hazardous from benign cases with 98.2% AUROC, yet the model's output sensitivity was only 45.1%, ...

---

## 89. CAPSUL: A Comprehensive Human Protein Benchmark for Subcellular Localization

**Authors**: Yicheng Hu, Xinyu Lin, Shulin Li, Wenjie Wang, Fengbin Zhu, Fuli Feng  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18571  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18571v1.pdf

**Abstract**:
> arXiv:2603.18571v1 Announce Type: new 
Abstract: Subcellular localization is a crucial biological task for drug target identification and function annotation. Although it has been biologically realized that subcellular localization is closely associated with protein structure, no existing dataset offers comprehensive 3D structural information with detailed subcellular localization annotations, thus severely hindering the application of promising structure-based models on this task. To address this gap, we introduce a new benchmark called $\mathbf{CAPSUL}$, a $\mathbf{C}$omprehensive hum$\mathbf{A}$n $\mathbf{P}$rotein benchmark for $\mathbf{SU}$bcellular $\mathbf{L}$ocalization. It features a dataset that integrates diverse 3D structural representations with fine-grained subcellular locali...

---

## 90. MANAR: Memory-augmented Attention with Navigational Abstract Conceptual Representation

**Authors**: Zuher Jahshan, Ben Ben Ishay, Leonid Yavits  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18676  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18676v1.pdf

**Abstract**:
> arXiv:2603.18676v1 Announce Type: new 
Abstract: MANAR (Memory-augmented Attention with Navigational Abstract Conceptual Representation), contextualization layer generalizes standard multi-head attention (MHA) by instantiating the principles of Global Workspace Theory (GWT). While MHA enables unconstrained all-to-all communication, it lacks the functional bottleneck and global integration mechanisms hypothesized in cognitive models of consciousness. MANAR addresses this by implementing a central workspace through a trainable memory of abstract concepts and an Abstract Conceptual Representation (ACR). The architecture follows a two-stage logic that maps directly to GWT mechanics: (i) an integration phase, where retrieved memory concepts converge to form a collective "mental image" (the ACR)...

---

## 91. Accurate and Efficient Multi-Channel Time Series Forecasting via Sparse Attention Mechanism

**Authors**: Lei Gao, Hengda Bao, Jingfei Fang, Guangzheng Wu, Weihua Zhou, Yun Zhou  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18712  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18712v1.pdf

**Abstract**:
> arXiv:2603.18712v1 Announce Type: new 
Abstract: The task of multi-channel time series forecasting is ubiquitous in numerous fields such as finance, supply chain management, and energy planning. It is critical to effectively capture complex dynamic dependencies within and between channels for accurate predictions. However, traditional method paid few attentions on learning the interaction among channels. This paper proposes Linear-Network (Li-Net), a novel architecture designed for multi-channel time series forecasting that captures the linear and non-linear dependencies among channels. Li-Net dynamically compresses representations across sequence and channel dimensions, processes the information through a configurable non-linear module and subsequently reconstructs the forecasts. Moreover...

---

## 92. A Concept is More Than a Word: Diversified Unlearning in Text-to-Image Diffusion Models

**Authors**: Duc Hao Pham, Van Duy Truong, Duy Khanh Dinh, Tien Cuong Nguyen, Dien Hy Ngo, Tuan Anh Bui  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18767  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18767v1.pdf

**Abstract**:
> arXiv:2603.18767v1 Announce Type: new 
Abstract: Concept unlearning has emerged as a promising direction for reducing the risks of harmful content generation in text-to-image diffusion models by selectively erasing undesirable concepts from a model's parameters. Existing approaches typically rely on keywords to identify the target concept to be unlearned. However, we show that this keyword-based formulation is inherently limited: a visual concept is multi-dimensional, can be expressed in diverse textual forms, and often overlap with related concepts in the latent space, making keyword-only unlearning, which imprecisely indicate the target concept is brittle and prone to over-forgetting. This occurs because a single keyword represents only a narrow point estimate of the concept, failing to ...

---

## 93. Quantitative Introspection in Language Models: Tracking Internal States Across Conversation

**Authors**: Nicolas Martorell  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18893  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18893v1.pdf

**Abstract**:
> arXiv:2603.18893v1 Announce Type: new 
Abstract: Tracking the internal states of large language models across conversations is important for safety, interpretability, and model welfare, yet current methods are limited. Linear probes and other white-box methods compress high-dimensional representations imperfectly and are harder to apply with increasing model size. Taking inspiration from human psychology, where numeric self-report is a widely used tool for tracking internal states, we ask whether LLMs' own numeric self-reports can track probe-defined emotive states over time. We study four concept pairs (wellbeing, interest, focus, and impulsivity) in 40 ten-turn conversations, operationalizing introspection as the causal informational coupling between a model's self-report and a concept-m...

---

## 94. Secure Linear Alignment of Large Language Models

**Authors**: Matt Gorbett, Suman Jana  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18908  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18908v1.pdf

**Abstract**:
> arXiv:2603.18908v1 Announce Type: new 
Abstract: Language models increasingly appear to learn similar representations, despite differences in training objectives, architectures, and data modalities. This emerging compatibility between independently trained models introduces new opportunities for cross-model alignment to downstream objectives. Moreover, it unlocks new potential application domains, such as settings where security, privacy, or competitive constraints prohibit direct data or model sharing. In this work, we propose a privacy-preserving framework that exploits representational convergence to enable cross-silo inference between independent language models. The framework learns an affine transformation over a shared public dataset and applies homomorphic encryption to protect cli...

---

## 95. Evaluating 5W3H Structured Prompting for Intent Alignment in Human-AI Interaction

**Authors**: Peng Gang  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18976  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18976v1.pdf

**Abstract**:
> arXiv:2603.18976v1 Announce Type: new 
Abstract: Natural language prompts often suffer from intent transmission loss: the gap between what users actually need and what they communicate to AI systems. We evaluate PPS (Prompt Protocol Specification), a 5W3H-based framework for structured intent representation in human-AI interaction. In a controlled three-condition study across 60 tasks in three domains (business, technical, and travel), three large language models (DeepSeek-V3, Qwen-Max, and Kimi), and three prompt conditions - (A) simple prompts, (B) raw PPS JSON, and (C) natural-language-rendered PPS - we collect 540 AI-generated outputs evaluated by an LLM judge. We introduce goal_alignment, a user-intent-centered evaluation dimension, and find that rendered PPS outperforms both simple p...

---

## 96. Man and machine: artificial intelligence and judicial decision making

**Authors**: Arthur Dyevre, Ahmad Shahvaroughi  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.19042  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.19042v1.pdf

**Abstract**:
> arXiv:2603.19042v1 Announce Type: new 
Abstract: The integration of artificial intelligence (AI) technologies into judicial decision-making - particularly in pretrial, sentencing, and parole contexts - has generated substantial concerns about transparency, reliability, and accountability. At the same time, these developments have brought the limitations of human judgment into sharper relief and underscored the importance of understanding how judges interact with AI-based decision aids. Using criminal justice risk assessment as a focal case, we conduct a synthetic review connecting three intertwined aspects of AI's role in judicial decision-making: the performance and fairness of AI tools, the strengths and biases of human judges, and the nature of AI+human interactions. Across the fields o...

---

## 97. LuMamba: Latent Unified Mamba for Electrode Topology-Invariant and Efficient EEG Modeling

**Authors**: Dana\'e Broustail, Anna Tegon, Thorir Mar Ingolfsson, Yawei Li, Luca Benini  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.19100  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.19100v1.pdf

**Abstract**:
> arXiv:2603.19100v1 Announce Type: new 
Abstract: Electroencephalography (EEG) enables non-invasive monitoring of brain activity across clinical and neurotechnology applications, yet building foundation models for EEG remains challenging due to \emph{differing electrode topologies} and \emph{computational scalability}, as Transformer architectures incur quadratic sequence complexity. As a joint solution, we propose \textbf{LuMamba} (\textbf{L}atent \textbf{U}nified \textbf{Mamba}), a self-supervised framework combining topology-invariant encodings with linear-complexity state-space modeling, using LUNA's learned-query cross-attention mechanism for channel unification~\cite{luna}, and FEMBA's bidirectional Mamba blocks for efficient temporal modeling~\cite{femba}. Within this architecture, w...

---

## 98. Using Optimal Transport as Alignment Objective for fine-tuning Multilingual Contextualized Embeddings

**Authors**: Sawsan Alqahtani, Garima Lalwani, Yi Zhang, Salvatore Romeo, Saab Mansour  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2110.02887  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2110.02887v1.pdf

**Abstract**:
> arXiv:2110.02887v1 Announce Type: cross 
Abstract: Recent studies have proposed different methods to improve multilingual word representations in contextualized settings including techniques that align between source and target embedding spaces. For contextualized embeddings, alignment becomes more complex as we additionally take context into consideration. In this work, we propose using Optimal Transport (OT) as an alignment objective during fine-tuning to further improve multilingual contextualized representations for downstream cross-lingual transfer. This approach does not require word-alignment pairs prior to fine-tuning that may lead to sub-optimal matching and instead learns the word alignments within context in an unsupervised manner. It also allows different types of mappings due ...

---

## 99. Do Large Language Models Possess a Theory of Mind? A Comparative Evaluation Using the Strange Stories Paradigm

**Authors**: Anna Babarczy, Andras Lukacs, Peter Vedres, Zeteny Bujka  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18007  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18007v1.pdf

**Abstract**:
> arXiv:2603.18007v1 Announce Type: cross 
Abstract: The study explores whether current Large Language Models (LLMs) exhibit Theory of Mind (ToM) capabilities -- specifically, the ability to infer others' beliefs, intentions, and emotions from text. Given that LLMs are trained on language data without social embodiment or access to other manifestations of mental representations, their apparent social-cognitive reasoning raises key questions about the nature of their understanding. Are they capable of robust mental-state attribution indistinguishable from human ability in its output, or do their outputs merely reflect superficial pattern completion? To address this question, we tested five LLMs and compared their performance to that of human controls using an adapted version of a text-based t...

---

## 100. Agentic Framework for Political Biography Extraction

**Authors**: Yifei Zhu, Songpo Yang, Jiangnan Zhu, Junyan Jiang  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18010  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18010v1.pdf

**Abstract**:
> arXiv:2603.18010v1 Announce Type: cross 
Abstract: The production of large-scale political datasets typically demands extracting structured facts from vast piles of unstructured documents or web sources, a task that traditionally relies on expensive human experts and remains prohibitively difficult to automate at scale. In this paper, we leverage Large Language Models (LLMs) to automate the extraction of multi-dimensional elite biographies, addressing a long-standing bottleneck in political science research. We propose a two-stage ``Synthesis-Coding'' framework for complex extraction task: an upstream synthesis stage that uses recursive agentic LLMs to search, filter, and curate biography from heterogeneous web sources, followed by a downstream coding stage that maps curated biography into...

---

## 101. Clinically Meaningful Explainability for NeuroAI: An ethical, technical, and clinical perspective

**Authors**: Laura Schopp, Ambra DImperio, Jalal Etesami, Marcello Ienca  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18028  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18028v1.pdf

**Abstract**:
> arXiv:2603.18028v1 Announce Type: cross 
Abstract: While explainable AI (XAI) is often heralded as a means to enhance transparency and trustworthiness in closed-loop neurotechnology for psychiatric and neurological conditions, its real-world prevalence remains low. Moreover, empirical evidence suggests that the type of explanations provided by current XAI methods often fails to align with clinicians' end-user needs. In this viewpoint, we argue that clinically meaningful explainability (CME) is essential for AI-enabled closed-loop medical neurotechnology and must be addressed from an ethical, technical, and clinical perspective. Instead of exhaustive technical detail, clinicians prioritize clinically relevant, actionable explanations, such as clear representations of input-output relationsh...

---

## 102. Uncovering Latent Phase Structures and Branching Logic in Locomotion Policies: A Case Study on HalfCheetah

**Authors**: Daisuke Yasui, Toshitaka Matsuki, Hiroshi Sato  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18084  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18084v1.pdf

**Abstract**:
> arXiv:2603.18084v1 Announce Type: cross 
Abstract: In locomotion control tasks, Deep Reinforcement Learning (DRL) has demonstrated high performance; however, the decision-making process of the learned policy remains a black box, making it difficult for humans to understand. On the other hand, in periodic motions such as walking, it is well known that implicit motion phases exist, such as the stance phase and the swing phase. Focusing on this point, this study hypothesizes that a policy trained for locomotion control may also represent a phase structure that is interpretable by humans. To examine this hypothesis in a controlled setting, we consider a locomotion task that is amenable to observing whether a policy autonomously acquires temporally structured phases through interaction with the...

---

## 103. A Trace-Based Assurance Framework for Agentic AI Orchestration: Contracts, Testing, and Governance

**Authors**: Ciprian Paduraru, Petru-Liviu Bouruc, Alin Stefanescu  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18096  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18096v1.pdf

**Abstract**:
> arXiv:2603.18096v1 Announce Type: cross 
Abstract: In Agentic AI, Large Language Models (LLMs) are increasingly used in the orchestration layer to coordinate multiple agents and to interact with external services, retrieval components, and shared memory. In this setting, failures are not limited to incorrect final outputs. They also arise from long-horizon interaction, stochastic decisions, and external side effects (such as API calls, database writes, and message sends). Common failures include non-termination, role drift, propagation of unsupported claims, and attacks via untrusted context or external channels.
  This paper presents an assurance framework for such Agentic AI systems. Executions are instrumented as Message-Action Traces (MAT) with explicit step and trace contracts. Contra...

---

## 104. Understanding Task Aggregation for Generalizable Ultrasound Foundation Models

**Authors**: Fangyijie Wang, Tanya Akumu, Vien Ngoc Dang, Amelia Jim\'nez-S\'anchez, Jieyun Bai, Gu\'enol\'e Silv...  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18123  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18123v1.pdf

**Abstract**:
> arXiv:2603.18123v1 Announce Type: cross 
Abstract: Foundation models promise to unify multiple clinical tasks within a single framework, but recent ultrasound studies report that unified models can underperform task-specific baselines. We hypothesize that this degradation arises not from model capacity limitations, but from task aggregation strategies that ignore interactions between task heterogeneity and available training data scale. In this work, we systematically analyze when heterogeneous ultrasound tasks can be jointly learned without performance loss, establishing practical criteria for task aggregation in unified clinical imaging models. We introduce M2DINO, a multi-organ, multi-task framework built on DINOv3 with task-conditioned Mixture-of-Experts blocks for adaptive capacity al...

---

## 105. How LLMs Distort Our Written Language

**Authors**: Marwa Abdulhai, Isadora White, Yanming Wan, Ibrahim Qureshi, Joel Leibo, Max Kleiman-Weiner, Natasha...  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18161  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18161v1.pdf

**Abstract**:
> arXiv:2603.18161v1 Announce Type: cross 
Abstract: Large language models (LLMs) are used by over a billion people globally, most often to assist with writing. In this work, we demonstrate that LLMs not only alter the voice and tone of human writing, but also consistently alter the intended meaning. First, we conduct a human user study to understand how people actually interact with LLMs when using them for writing. Our findings reveal that extensive LLM use led to a nearly 70% increase in essays that remained neutral in answering the topic question. Significantly more heavy LLM users reported that the writing was less creative and not in their voice. Next, using a dataset of human-written essays that was collected in 2021 before the widespread release of LLMs, we study how asking an LLM to...

---

## 106. LRConv-NeRV: Low Rank Convolution for Efficient Neural Video Compression

**Authors**: Tamer Shanableh  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18261  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18261v1.pdf

**Abstract**:
> arXiv:2603.18261v1 Announce Type: cross 
Abstract: Neural Representations for Videos (NeRV) encode entire video sequences within neural network parameters, offering an alternative paradigm to conventional video codecs. However, the convolutional decoder of NeRV remains computationally expensive and memory intensive, limiting its deployment in resource-constrained environments. This paper proposes LRConv-NeRV, an efficient NeRV variant that replaces selected dense 3x3 convolutional layers with structured low-rank separable convolutions, trained end-to-end within the decoder architecture. By progressively applying low-rank factorization from the largest to earlier decoder stages, LRConv-NeRV enables controllable trade-offs between reconstruction quality and efficiency. Extensive experiments ...

---

## 107. Sparse3DTrack: Monocular 3D Object Tracking Using Sparse Supervision

**Authors**: Nikhil Gosala, B. Ravi Kiran, Senthil Yogamani, Abhinav Valada  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18298  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18298v1.pdf

**Abstract**:
> arXiv:2603.18298v1 Announce Type: cross 
Abstract: Monocular 3D object tracking aims to estimate temporally consistent 3D object poses across video frames, enabling autonomous agents to reason about scene dynamics. However, existing state-of-the-art approaches are fully supervised and rely on dense 3D annotations over long video sequences, which are expensive to obtain and difficult to scale. In this work, we address this fundamental limitation by proposing the first sparsely supervised framework for monocular 3D object tracking. Our approach decomposes the task into two sequential sub-problems: 2D query matching and 3D geometry estimation. Both components leverage the spatio-temporal consistency of image sequences to augment a sparse set of labeled samples and learn rich 2D and 3D represe...

---

## 108. HypeMed: Enhancing Medication Recommendations with Hypergraph-Based Patient Relationships

**Authors**: Xiangxu Zhang, Xiao Zhou, Hongteng Xu, Jianxun Lian  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18459  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18459v1.pdf

**Abstract**:
> arXiv:2603.18459v1 Announce Type: cross 
Abstract: Medication recommendations aim to generate safe and effective medication sets from health records. However, accurately recommending medications hinges on inferring a patient's latent clinical condition from sparse and noisy observations, which requires both (i) preserving the visit-level combinatorial semantics of co-occurring entities and (ii) leveraging informative historical references through effective, visit-conditioned retrieval. Most existing methods fall short in one of both aspects: graph-based modeling often fragments higher-order intra-visit patterns into pairwise relations, while inter-visit augmentation methods commonly exhibit an imbalance between learning a globally stable representation space and performing dynamic retrieva...

---

## 109. Foundations and Architectures of Artificial Intelligence for Motor Insurance

**Authors**: Teerapong Panboonyuen  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18508  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18508v1.pdf

**Abstract**:
> arXiv:2603.18508v1 Announce Type: cross 
Abstract: This handbook presents a systematic treatment of the foundations and architectures of artificial intelligence for motor insurance, grounded in large-scale real-world deployment. It formalizes a vertically integrated AI paradigm that unifies perception, multimodal reasoning, and production infrastructure into a cohesive intelligence stack for automotive risk assessment and claims processing. At its core, the handbook develops domain-adapted transformer architectures for structured visual understanding, relational vehicle representation learning, and multimodal document intelligence, enabling end-to-end automation of vehicle damage analysis, claims evaluation, and underwriting workflows. These components are composed into a scalable pipeline...

---

## 110. SCISSR: Scribble-Conditioned Interactive Surgical Segmentation and Refinement

**Authors**: Haonan Ping, Jian Jiang, Cheng Yuan, Qizhen Sun, Lv Wu, Yutong Ban  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18544  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18544v1.pdf

**Abstract**:
> arXiv:2603.18544v1 Announce Type: cross 
Abstract: Accurate segmentation of tissues and instruments in surgical scenes is annotation-intensive due to irregular shapes, thin structures, specularities, and frequent occlusions. While SAM models support point, box, and mask prompts, points are often too sparse and boxes too coarse to localize such challenging targets. We present SCISSR, a scribble-promptable framework for interactive surgical scene segmentation. It introduces a lightweight Scribble Encoder that converts freehand scribbles into dense prompt embeddings compatible with the mask decoder, enabling iterative refinement for a target object by drawing corrective strokes on error regions. Because all added modules (the Scribble Encoder, Spatial Gated Fusion, and LoRA adapters) interact...

---

## 111. HiMu: Hierarchical Multimodal Frame Selection for Long Video Question Answering

**Authors**: Dan Ben-Ami, Gabriele Serussi, Kobi Cohen, Chaim Baskin  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18558  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18558v1.pdf

**Abstract**:
> arXiv:2603.18558v1 Announce Type: cross 
Abstract: Long-form video question answering requires reasoning over extended temporal contexts, making frame selection critical for large vision-language models (LVLMs) bound by finite context windows. Existing methods face a sharp trade-off: similarity-based selectors are fast but collapse compositional queries into a single dense vector, losing sub-event ordering and cross-modal bindings; agent-based methods recover this structure through iterative LVLM inference, but at prohibitive cost. We introduce HiMu, a training-free framework that bridges this gap. A single text-only LLM call decomposes the query into a hierarchical logic tree whose leaves are atomic predicates, each routed to a lightweight expert spanning vision (CLIP, open-vocabulary det...

---

## 112. Multiscale Switch for Semi-Supervised and Contrastive Learning in Medical Ultrasound Image Segmentation

**Authors**: Jingguo Qu, Xinyang Han, Yao Pu, Man-Lik Chui, Simon Takadiyi Gunda, Ziman Chen, Jing Qin, Ann Dorot...  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18655  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18655v1.pdf

**Abstract**:
> arXiv:2603.18655v1 Announce Type: cross 
Abstract: Medical ultrasound image segmentation faces significant challenges due to limited labeled data and characteristic imaging artifacts including speckle noise and low-contrast boundaries. While semi-supervised learning (SSL) approaches have emerged to address data scarcity, existing methods suffer from suboptimal unlabeled data utilization and lack robust feature representation mechanisms. In this paper, we propose Switch, a novel SSL framework with two key innovations: (1) Multiscale Switch (MSS) strategy that employs hierarchical patch mixing to achieve uniform spatial coverage; (2) Frequency Domain Switch (FDS) with contrastive learning that performs amplitude switching in Fourier space for robust feature representations. Our framework int...

---

## 113. Functional Subspace Watermarking for Large Language Models

**Authors**: Zikang Ding, Junhao Li, Suling Wu, Junchi Yao, Hongbo Liu, Lijie Hu  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18793  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18793v1.pdf

**Abstract**:
> arXiv:2603.18793v1 Announce Type: cross 
Abstract: Model watermarking utilizes internal representations to protect the ownership of large language models (LLMs). However, these features inevitably undergo complex distortions during realistic model modifications such as fine-tuning, quantization, or knowledge distillation, making reliable extraction extremely challenging. Despite extensive research on model-side watermarking, existing methods still lack sufficient robustness against parameter-level perturbations. To address this gap, we propose \texttt{\textbf{Functional Subspace Watermarking (FSW)}}, a framework that anchors ownership signals into a low-dimensional functional backbone. Specifically, we first solve a generalized eigenvalue problem to extract a stable functional subspace for...

---

## 114. PRIOR: Perceptive Learning for Humanoid Locomotion with Reference Gait Priors

**Authors**: Chenxi Han, Shilu He, Yi Cheng, Linqi Ye, Houde Liu  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.18979  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.18979v1.pdf

**Abstract**:
> arXiv:2603.18979v1 Announce Type: cross 
Abstract: Training perceptive humanoid locomotion policies that traverse complex terrains with natural gaits remains an open challenge, typically demanding multi-stage training pipelines, adversarial objectives, or extensive real-world calibration. We present PRIOR, an efficient and reproducible framework built on Isaac Lab that achieves robust terrain traversal with human-like gaits through a simple yet effective design: (i) a parametric gait generator that supplies stable reference trajectories derived from motion capture without adversarial training, (ii) a GRU-based state estimator that infers terrain geometry directly from egocentric depth images via self-supervised heightmap reconstruction, and (iii) terrain-adaptive footstep rewards that guid...

---

## 115. What Really Controls Temporal Reasoning in Large Language Models: Tokenisation or Representation of Time?

**Authors**: Gagan Bhatia, Ahmad Muhammad Isa, Maxime Peyrard, Wei Zhao  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.19017  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.19017v1.pdf

**Abstract**:
> arXiv:2603.19017v1 Announce Type: cross 
Abstract: We present MultiTempBench, a multilingual temporal reasoning benchmark spanning three tasks, date arithmetic, time zone conversion, and temporal relation extraction across five languages (English, German, Chinese, Arabic, and Hausa) and multiple calendar conventions (Gregorian, Hijri, and Chinese Lunar). MultiTempBench contains $15,000$ examples built by translating $750$ curated English questions and expanding each into controlled date-format variants. We evaluate 20 LLMs and introduce the multilingual Date Fragmentation Ratio (mDFR), calibrated with human severity ratings, together with geometric-probing analyses of internal temporal representations. We find tokenisation quality of temporal artefacts is a resource-dependent bottleneck: i...

---

## 116. CAMO: A Conditional Neural Solver for the Multi-objective Multiple Traveling Salesman Problem

**Authors**: Fengxiaoxiao Li, Xiao Mao, Mingfeng Fan, Yifeng Zhang, Yi Li, Tanishq Duhan, Guillaume Sartoretti  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.19074  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.19074v1.pdf

**Abstract**:
> arXiv:2603.19074v1 Announce Type: cross 
Abstract: Robotic systems often require a team of robots to collectively visit multiple targets while optimizing competing objectives, such as total travel cost and makespan. This setting can be formulated as the Multi-Objective Multiple Traveling Salesman Problem (MOMTSP). Although learning-based methods have shown strong performance on the single-agent TSP and multi-objective TSP variants, they rarely address the combined challenges of multi-agent coordination and multi-objective trade-offs, which introduce dual sources of complexity. To bridge this gap, we propose CAMO, a conditional neural solver for MOMTSP that generalizes across varying numbers of targets, agents, and preference vectors, and yields high-quality approximations to the Pareto fro...

---

## 117. UGID: Unified Graph Isomorphism for Debiasing Large Language Models

**Authors**: Zikang Ding, Junchi Yao, Junhao Li, Yi Zhang, Wenbo Jiang, Hongbo Liu, Lijie Hu  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.19144  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.19144v1.pdf

**Abstract**:
> arXiv:2603.19144v1 Announce Type: cross 
Abstract: Large language models (LLMs) exhibit pronounced social biases. Output-level or data-optimization--based debiasing methods cannot fully resolve these biases, and many prior works have shown that biases are embedded in internal representations. We propose \underline{U}nified \underline{G}raph \underline{I}somorphism for \underline{D}ebiasing large language models (\textit{\textbf{UGID}}), an internal-representation--level debiasing framework for large language models that models the Transformer as a structured computational graph, where attention mechanisms define the routing edges of the graph and hidden states define the graph nodes. Specifically, debiasing is formulated as enforcing invariance of the graph structure across counterfactual ...

---

## 118. $R$-equivalence on Cubic Surfaces I: Existing Cases with Non-Trivial Universal Equivalence

**Authors**: Dimitri Kanevsky, Julian Salazar, Matt Harvey  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.19215  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.19215v1.pdf

**Abstract**:
> arXiv:2603.19215v1 Announce Type: cross 
Abstract: Let $V$ be a smooth cubic surface over a $p$-adic field $k$ with good reduction. Swinnerton-Dyer (1981) proved that $R$-equivalence is trivial on $V(k)$ except perhaps if $V$ is one of three special types--those whose $R$-equivalence he could not bound by proving the universal (admissible) equivalence is trivial. We consider all surfaces $V$ currently known to have non-trivial universal equivalence. Beyond being intractable to Swinnerton-Dyer's approach, we observe that if these surfaces also had non-trivial $R$-equivalence, they would contradict Colliot-Th\'el\`ene and Sansuc's conjecture regarding the $k$-rationality of universal torsors for geometrically rational surfaces.
  By devising new methods to study $R$-equivalence, we prove tha...

---

## 119. Multimodal Fused Learning for Solving the Generalized Traveling Salesman Problem in Robotic Task Planning

**Authors**: Jiaqi Chen, Mingfeng Fan, Xuefeng Zhang, Jingsong Liang, Yuhong Cao, Guohua Wu, Guillaume Adrien Sar...  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2506.16931  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2506.16931v2.pdf

**Abstract**:
> arXiv:2506.16931v2 Announce Type: replace 
Abstract: Effective and efficient task planning is essential for mobile robots, especially in applications like warehouse retrieval and environmental monitoring. These tasks often involve selecting one location from each of several target clusters, forming a Generalized Traveling Salesman Problem (GTSP) that remains challenging to solve both accurately and efficiently. To address this, we propose a Multimodal Fused Learning (MMFL) framework that leverages both graph and image-based representations to capture complementary aspects of the problem, and learns a policy capable of generating high-quality task planning schemes in real time. Specifically, we first introduce a coordinate-based image builder that transforms GTSP instances into spatially in...

---

## 120. From Logs to Language: Learning Optimal Verbalization for LLM-Based Recommendation at Industry Scale

**Authors**: Yucheng Shi, Ying Li, Yu Wang, Yesu Feng, Arjun Rao, Rein Houthooft, Shradha Sehgal, Jin Wang, Hao Z...  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.20558  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.20558v2.pdf

**Abstract**:
> arXiv:2602.20558v2 Announce Type: replace 
Abstract: Large language models (LLMs) are promising backbones for generative recommender systems, yet a key challenge remains underexplored: verbalization, i.e., converting structured user interaction logs into effective natural language inputs. Existing methods rely on rigid templates that simply concatenate fields, yielding suboptimal representations for recommendation. We propose a data-centric framework that learns verbalization for LLM-based recommendation. Using reinforcement learning, a verbalization agent transforms raw interaction histories into optimized textual contexts, with recommendation accuracy as the training signal. This agent learns to filter noise, incorporate relevant metadata, and reorganize information to improve downstream...

---

## 121. Is Contrastive Distillation Enough for Learning Comprehensive 3D Representations?

**Authors**: Yifan Zhang, Junhui Hou  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2412.08973  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2412.08973v4.pdf

**Abstract**:
> arXiv:2412.08973v4 Announce Type: replace-cross 
Abstract: Cross-modal contrastive distillation has recently been explored for learning effective 3D representations. However, existing methods focus primarily on modality-shared features, neglecting the modality-specific features during the pre-training process, which leads to suboptimal representations. In this paper, we theoretically analyze the limitations of current contrastive methods for 3D representation learning and propose a new framework, namely CMCR (Cross-Modal Comprehensive Representation Learning), to address these shortcomings. Our approach improves upon traditional methods by better integrating both modality-shared and modality-specific features. Specifically, we introduce masked image modeling and occupancy estimation tasks ...

---

## 122. A New Tractable Description Logic under Categorical Semantics

**Authors**: Chan Le Duc, Ludovic Brieulle  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2505.08916  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2505.08916v2.pdf

**Abstract**:
> arXiv:2505.08916v2 Announce Type: replace-cross 
Abstract: Biomedical ontologies contain numerous concept or role names involving negative knowledge such as lacks_part, absence_of. Such a representation with labels rather than logical constructors would not allow a reasoner to interpret lacks_part as a kind of negation of has_part. It is known that adding negation to the tractable Description Logic (DL) EL allowing for conjunction, existential restriction and concept inclusion makes it intractable since the obtained logic includes implicitly disjunction and universal restriction which interact with other constructors. In this paper, we propose a new extension of EL with a weakened negation allowing to represent negative knowledge while retaining tractability. To this end, we introduce cate...

---

## 123. Look Before You Fuse: 2D-Guided Cross-Modal Alignment for Robust 3D Detection

**Authors**: Xiang Li, Zhangchi Hu, Xiao Xu, Bin Kong  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2507.16861  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2507.16861v4.pdf

**Abstract**:
> arXiv:2507.16861v4 Announce Type: replace-cross 
Abstract: Integrating LiDAR and camera inputs into a unified Bird's-Eye-View (BEV) representation is crucial for enhancing 3D perception capabilities of autonomous vehicles. However, existing methods suffer from spatial misalignment between LiDAR and camera features, which causes inaccurate depth supervision in camera branch and erroneous fusion during cross-modal feature aggregation. The root cause of this misalignment lies in projection errors, stemming from calibration inaccuracies and rolling shutter effect. The key insight of this work is that locations of these projection errors are not random but highly predictable, as they are concentrated at object-background boundaries which 2D detectors can reliably identify. Based on this, our ma...

---

## 124. Blind to Position, Biased in Language: Probing Mid-Layer Representational Bias in Vision-Language Encoders for Zero-Shot Language-Grounded Spatial Understanding

**Authors**: Na Min An, Inha Kang, Minhyun Lee, Hyunjung Shim  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2509.23098  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2509.23098v2.pdf

**Abstract**:
> arXiv:2509.23098v2 Announce Type: replace-cross 
Abstract: Vision-Language Encoders (VLEs) are widely adopted as the backbone of zero-shot referring image segmentation (RIS), enabling text-guided localization without task-specific training. However, prior works underexplored the underlying biases within mid-layer representations that preserve positional and language-specific information. Through layer-wise investigation, we reveal that the conventionally used final-layer multimodal embeddings prioritize global semantic alignment, leading to two coupled consequences. First, vision embeddings exhibit weak sensitivity to positional cues. Second, multilingual text embeddings form language-dependent geometric shifts within the shared space. Motivated by these findings, we identify an underexplo...

---

## 125. From Binary to Bilingual: How the National Weather Service is Using Artificial Intelligence to Develop a Comprehensive Translation Program

**Authors**: Joseph E. Trujillo-Falcon, Monica L. Bozeman, Liam E. Llewellyn, Samuel T. Halvorson, Meryl Mizell, ...  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.14369  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.14369v2.pdf

**Abstract**:
> arXiv:2510.14369v2 Announce Type: replace-cross 
Abstract: To advance a Weather-Ready Nation, the National Weather Service (NWS) is developing a systematic translation program to better serve the 68.8 million people in the U.S. who do not speak English at home. This article outlines the foundation of an automated translation tool for NWS products, powered by artificial intelligence. The NWS has partnered with LILT, whose patented training process enables large language models (LLMs) to adapt neural machine translation (NMT) tools for weather terminology and messaging. Designed for scalability across Weather Forecast Offices (WFOs) and National Centers, the system is currently being developed in Spanish, Simplified Chinese, Vietnamese, and other widely spoken non-English languages. Rooted i...

---

## 126. Manual2Skill++: Connector-Aware General Robotic Assembly from Instruction Manuals via Vision-Language Models

**Authors**: Chenrui Tie, Shengxiang Sun, Yudi Lin, Yanbo Wang, Zhongrui Li, Zhouhan Zhong, Jinxuan Zhu, Yiman Pa...  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.16344  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.16344v2.pdf

**Abstract**:
> arXiv:2510.16344v2 Announce Type: replace-cross 
Abstract: Assembly hinges on reliably forming connections between parts; yet most robotic approaches plan assembly sequences and part poses while treating connectors as an afterthought. Connections represent the foundational physical constraints of assembly execution; while task planning sequences operations, the precise establishment of these constraints ultimately determines assembly success. In this paper, we treat connections as explicit, primary entities in assembly representation, directly encoding connector types, specifications, and locations for every assembly step. Drawing inspiration from how humans learn assembly tasks through step-by-step instruction manuals, we present Manual2Skill++, a vision-language framework that automatica...

---

## 127. A Multicenter Benchmark of Multiple Instance Learning Models for Lymphoma Subtyping from HE-stained Whole Slide Images

**Authors**: Rao Muhammad Umer, Daniel Sens, Jonathan Noll, Sohom Dey, Christian Matek, Lukas Wolfseher, Rainer S...  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2512.14640  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2512.14640v3.pdf

**Abstract**:
> arXiv:2512.14640v3 Announce Type: replace-cross 
Abstract: Timely and accurate lymphoma diagnosis is essential for guiding cancer treatment. Standard diagnostic practice combines hematoxylin and eosin (HE)-stained whole slide images with immunohistochemistry, flow cytometry, and molecular genetic tests to determine lymphoma subtypes, a process requiring costly equipment, and skilled personnel, causing treatment delays. Deep learning methods could assist pathologists by extracting diagnostic information from routinely available HE-stained slides directly, yet comprehensive benchmarks for lymphoma subtyping on multicenter data are lacking. In this work, we present the first multicenter lymphoma benchmark, covering four common lymphoma subtypes and healthy control tissue. We systematically ev...

---

## 128. Neuron-Guided Interpretation of Code LLMs: Where, Why, and How?

**Authors**: Zhe Yin, Xiaodong Gu, Beijun Shen  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2512.19980  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2512.19980v2.pdf

**Abstract**:
> arXiv:2512.19980v2 Announce Type: replace-cross 
Abstract: Code language models excel on code intelligence tasks, yet their internal interpretability is underexplored. Existing neuron interpretability techniques from NLP are suboptimal for source code due to programming languages formal, hierarchical, and executable nature. We empirically investigate code LLMs at the neuron level, localizing language-specific neurons (selectively responsive to one language) and concept layers (feed-forward layers encoding language-agnostic code representations). We analyze Llama-3.1-8B and Qwen2.5-Coder-32B on multilingual inputs in C++, Java, Python, Go, and JavaScript, measuring neuron selectivity and layerwise contributions during generation. We find (1) neurons specialized for individual languages alon...

---

## 129. Farther the Shift, Sparser the Representation: Analyzing OOD Mechanisms in LLMs

**Authors**: Mingyu Jin, Yutong Yin, Jingcheng Niu, Qingcheng Zeng, Wujiang Xu, Mengnan Du, Wei Cheng, Zhaoran Wa...  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.03415  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.03415v2.pdf

**Abstract**:
> arXiv:2603.03415v2 Announce Type: replace-cross 
Abstract: In this work, we investigate how Large Language Models (LLMs) adapt their internal representations when encountering inputs of increasing difficulty, quantified as the degree of out-of-distribution (OOD) shift. We reveal a consistent and quantifiable phenomenon: as task difficulty increases, whether through harder reasoning questions, longer contexts, or adding answer choices, the last hidden states of LLMs become substantially sparser. In short, \textbf{\textit{the farther the shift, the sparser the representations}}. This sparsity--difficulty relation is observable across diverse models and domains, suggesting that language models respond to unfamiliar or complex inputs by concentrating computation into specialized subspaces in t...

---

## 130. Deep Expert Injection for Anchoring Retinal VLMs with Domain-Specific Knowledge

**Authors**: Shuai Lu, Meng Wang, Jia Guo, Jiawei Du, Bo Liu, Shengzhu Yang, Weihang Zhang, Huazhu Fu, Huiqi Li  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.07131  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.07131v3.pdf

**Abstract**:
> arXiv:2603.07131v3 Announce Type: replace-cross 
Abstract: Large Vision Language Models (LVLMs) show immense potential for automated ophthalmic diagnosis. However, their clinical deployment is severely hindered by lacking domain-specific knowledge. In this work, we identify two structural deficiencies hindering reliable medical reasoning: 1) the Perception Gap, where general-purpose visual encoders fail to resolve fine-grained pathological cues (e.g., microaneurysms); and 2) the Reasoning Gap, where sparse visual evidence is progressively overridden by massive language priors in deeper transformer layers, leading to ungrounded hallucinations. To bridge these gaps, we propose EyExIn, a data-efficient framework designed to anchor retinal VLMs with expert knowledge via a Deep Expert Injection...

---

## 131. WORKSWORLD: A Domain for Integrated Numeric Planning and Scheduling of Distributed Pipelined Workflows

**Authors**: Taylor Paul, William Regli  
**Categories**: cs.AI  
**Published**: Fri, 20 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.12214  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.12214v2.pdf

**Abstract**:
> arXiv:2603.12214v2 Announce Type: replace-cross 
Abstract: This work pursues automated planning and scheduling of distributed data pipelines, or workflows. We develop a general workflow and resource graph representation that includes both data processing and sharing components with corresponding network interfaces for scheduling. Leveraging these graphs, we introduce WORKSWORLD, a new domain for numeric domain-independent planners designed for permanently scheduled workflows, like ingest pipelines. Our framework permits users to define data sources, available workflow components, and desired data destinations and formats without explicitly declaring the entire workflow graph as a goal. The planner solves a joint planning and scheduling problem, producing a plan that both builds the workflo...

---

