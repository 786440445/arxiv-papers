# arXiv Papers - 2026-03-13

**来源**: arXiv (cs.SD, eess.AS, cs.LG, cs.AI)  
**关键词**: speech, audio, music, voice, sound, Mel, representation, self-supervised  
**今日新论文**: 113 篇

---

## 1. nlm: Real-Time Non-linear Modal Synthesis in Max

**Authors**: Rodrigo Diaz, Rodrigo Constanzo, Mark Sandler  
**Categories**: cs.SD  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10240  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10240v1.pdf

**Abstract**:
> arXiv:2603.10240v1 Announce Type: new 
Abstract: We present \texttt{nlm}, a set of Max externals that enable efficient real-time non-linear modal synthesis for strings, membranes, and plates. The externals, implemented in C++, offer interactive control of physical parameters, allow the loading of custom modal data, and provide multichannel output. By integrating interactive physical-modelling capabilities into a familiar environment, \texttt{nlm} lowers the barrier for composers, performers, and sound designers to explore the expressive potential of non-linear modal synthesis. The externals are available as open-source software at https://github.com/rodrigodzf/nlm.

---

## 2. ID-LoRA: Identity-Driven Audio-Video Personalization with In-Context LoRA

**Authors**: Aviad Dahan, Moran Yanuka, Noa Kraicer, Lior Wolf, Raja Giryes  
**Categories**: cs.SD  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10256  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10256v1.pdf

**Abstract**:
> arXiv:2603.10256v1 Announce Type: new 
Abstract: Existing video personalization methods preserve visual likeness but treat video and audio separately. Without access to the visual scene, audio models cannot synchronize sounds with on-screen actions; and because classical voice-cloning models condition only on a reference recording, a text prompt cannot redirect speaking style or acoustic environment. We propose ID-LoRA (Identity-Driven In-Context LoRA), which jointly generates a subject's appearance and voice in a single model, letting a text prompt, a reference image, and a short audio clip govern both modalities together. ID-LoRA adapts the LTX-2 joint audio-video diffusion backbone via parameter-efficient In-Context LoRA and, to our knowledge, is the first method to personalize visual a...

---

## 3. MoXaRt: Audio-Visual Object-Guided Sound Interaction for XR

**Authors**: Tianyu Xu, Sieun Kim, Qianhui Zheng, Ruoyu Xu, Tejasvi Ravi, Anuva Kulkarni, Katrina Passarella-Ward...  
**Categories**: cs.SD  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10465  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10465v1.pdf

**Abstract**:
> arXiv:2603.10465v1 Announce Type: new 
Abstract: In Extended Reality (XR), complex acoustic environments often overwhelm users, compromising both scene awareness and social engagement due to entangled sound sources. We introduce MoXaRt, a real-time XR system that uses audio-visual cues to separate these sources and enable fine-grained sound interaction. MoXaRt's core is a cascaded architecture that performs coarse, audio-only separation in parallel with visual detection of sources (e.g., faces, instruments). These visual anchors then guide refinement networks to isolate individual sources, separating complex mixes of up to 5 concurrent sources (e.g., 2 voices + 3 instruments) with ~2 second processing latency. We validate MoXaRt through a technical evaluation on a new dataset of 30 one-min...

---

## 4. Towards Robust Speech Deepfake Detection via Human-Inspired Reasoning

**Authors**: Artem Dvirniak, Evgeny Kushnir, Dmitrii Tarasov, Artem Iudin, Oleg Kiriukhin, Mikhail Pautov, Dmitri...  
**Categories**: cs.SD  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10725  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10725v1.pdf

**Abstract**:
> arXiv:2603.10725v1 Announce Type: new 
Abstract: The modern generative audio models can be used by an adversary in an unlawful manner, specifically, to impersonate other people to gain access to private information. To mitigate this issue, speech deepfake detection (SDD) methods started to evolve. Unfortunately, current SDD methods generally suffer from the lack of generalization to new audio domains and generators. More than that, they lack interpretability, especially human-like reasoning that would naturally explain the attribution of a given audio to the bona fide or spoof class and provide human-perceptible cues. In this paper, we propose HIR-SDD, a novel SDD framework that combines the strengths of Large Audio Language Models (LALMs) with the chain-of-thought reasoning derived from t...

---

## 5. Speaker Verification with Speech-Aware LLMs: Evaluation and Augmentation

**Authors**: Thomas Thebaud, Yuzhe Wang, Laureano Moro-Velazquez, Jesus Villalba-Lopez, Najim Dehak  
**Categories**: cs.SD  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10827  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10827v1.pdf

**Abstract**:
> arXiv:2603.10827v1 Announce Type: new 
Abstract: Speech-aware large language models (LLMs) can accept speech inputs, yet their training objectives largely emphasize linguistic content or specific fields such as emotions or the speaker's gender, leaving it unclear whether they encode speaker identity. First, we propose a model-agnostic scoring protocol that produces continuous verification scores for both API-only and open-weight models, using confidence scores or log-likelihood ratios from the Yes/No token probabilities. Using this protocol, we benchmark recent speech-aware LLMs and observe weak speaker discrimination (EERs above 20% on VoxCeleb1). Second, we introduce a lightweight augmentation that equips an LLM with ASV capability by injecting frozen ECAPA-TDNN speaker embeddings throug...

---

## 6. OSUM-Pangu: An Open-Source Multidimension Speech Understanding Foundation Model Built upon OpenPangu on Ascend NPUs

**Authors**: Yujie Liao, Xuelong Geng, Hongfei Xue, Shuiyuan Wang, Lei Xie  
**Categories**: cs.SD  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10862  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10862v1.pdf

**Abstract**:
> arXiv:2603.10862v1 Announce Type: new 
Abstract: Recent advancements in Speech Large Language Models have significantly enhanced multi-dimensional speech understanding. However, the majority of high-performance frameworks are predominantly optimized for GPU centric ecosystems and proprietary backbones, creating a significant gap for deployment on non-CUDA computing infrastructures. In this paper, we present OSUM-Pangu, a fully open-source speech understanding foundation model developed on a completely non-CUDA software and hardware stack. By integrating an audio encoder with the openPangu-7B LLM backbone, we successfully implement the entire training and inference pipeline on the Ascend NPU platform. To facilitate efficient task alignment under non-CUDA resource constraints, we adopt a pra...

---

## 7. VoxCare: Studying Natural Communication Behaviors of Hospital Caregivers through Wearable Sensing of Egocentric Audio

**Authors**: Tiantian Feng, Kleanthis Avramidis, Anfeng Xu, Deqi Wang, Brandon M Booth, Shrikanth Narayanan  
**Categories**: cs.SD  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10888  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10888v1.pdf

**Abstract**:
> arXiv:2603.10888v1 Announce Type: new 
Abstract: Healthcare professionals work in complex, high-stakes environments where effective communication is critical for care delivery, team coordination, and individual well-being. However, communication activity in everyday clinical settings remains challenging to measure and largely unexplored in human behavioral research. We present VoxCare, a scalable egocentric wearable audio sensing and computing system that captures natural communication behaviors of hospital professionals in real-world settings without storing raw audio. VoxCare performs real-time, on-device acoustic feature extraction and applies a speech foundation model-guided teacher-student framework to identify foreground speech activity. From these features, VoxCare derives interpret...

---

## 8. Training-Free Multi-Step Inference for Target Speaker Extraction

**Authors**: Zhenghai You, Ying Shi, Lantian Li, Dong Wang  
**Categories**: cs.SD  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10921  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10921v1.pdf

**Abstract**:
> arXiv:2603.10921v1 Announce Type: new 
Abstract: Target speaker extraction (TSE) aims to recover a target speaker's speech from a mixture using a reference utterance as a cue. Most TSE systems adopt conditional auto-encoder architectures with one-step inference. Inspired by test-time scaling, we propose a training-free multi-step inference method that enables iterative refinement with a frozen pretrained model. At each step, new candidates are generated by interpolating the original mixture and the previous estimate, and the best candidate is selected for further refinement until convergence. Experiments show that, when ground-truth target speech is available, optimizing an intrusive metric (SI-SDRi) yields consistent gains across multiple evaluation metrics. Without ground truth, optimizi...

---

## 9. AMB-DSGDN: Adaptive Modality-Balanced Dynamic Semantic Graph Differential Network for Multimodal Emotion Recognition

**Authors**: Yunsheng Wang, Yuntao Shou, Yilong Tan, Wei Ai, Tao Meng, Keqin Li  
**Categories**: cs.SD  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10043  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10043v1.pdf

**Abstract**:
> arXiv:2603.10043v1 Announce Type: cross 
Abstract: Multimodal dialogue emotion recognition captures emotional cues by fusing text, visual, and audio modalities. However, existing approaches still suffer from notable limitations in modeling emotional dependencies and learning multimodal representations. On the one hand, they are unable to effectively filter out redundant or noisy signals within multimodal features, which hinders the accurate capture of the dynamic evolution of emotional states across and within speakers. On the other hand, during multimodal feature learning, dominant modalities tend to overwhelm the fusion process, thereby suppressing the complementary contributions of non-dominant modalities such as speech and vision, ultimately constraining the overall recognition perform...

---

## 10. PRoADS: Provably Secure and Robust Audio Diffusion Steganography with latent optimization and backward Euler Inversion

**Authors**: YongPeng Yan, Yanan Li, Qiyang Xiao, Yanzhen Ren  
**Categories**: cs.SD  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10314  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10314v1.pdf

**Abstract**:
> arXiv:2603.10314v1 Announce Type: cross 
Abstract: This paper proposes PRoADS, a provably secure and robust audio steganographic framework based on audio diffusion models. As a generative steganography scheme, PRoADS embeds secret messages into the initial noise of diffusion models via orthogonal matrix projection. To address the reconstruction errors in diffusion inversion that cause high bit error rates (BER), we introduce Latent Optimization and Backward Euler Inversion to minimize the latent reconstruction and diffusion inversion errors. Comprehensive experiments demonstrate that our scheme sustains a remarkably low BER of 0.15\% under 64 kbps MP3 compression, significantly outperforming existing methods and exhibiting strong robustness.

---

## 11. NasoVoce: A Nose-Mounted Low-Audibility Speech Interface for Always-Available Speech Interaction

**Authors**: Jun Rekimoto, Yu Nishimura, Bojian Yang  
**Categories**: cs.SD  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10324  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10324v1.pdf

**Abstract**:
> arXiv:2603.10324v1 Announce Type: cross 
Abstract: Silent and whispered speech offer promise for always-available voice interaction with AI, yet existing methods struggle to balance vocabulary size, wearability, silence, and noise robustness. We present NasoVoce, a nose-bridge-mounted interface that integrates a microphone and a vibration sensor. Positioned at the nasal pads of smart glasses, it unobtrusively captures both acoustic and vibration signals. The nasal bridge, close to the mouth, allows access to bone- and skin-conducted speech and enables reliable capture of low-volume utterances such as whispered speech. While the microphone captures high-quality audio, it is highly sensitive to environmental noise. Conversely, the vibration sensor is robust to noise but yields lower signal q...

---

## 12. G-STAR: End-to-End Global Speaker-Tracking Attributed Recognition

**Authors**: Jing Peng, Ziyi Chen, Haoyu Li, Yucheng Wang, Duo Ma, Mengtian Li, Yunfan Du, Dezhu Xu, Kai Yu, Shua...  
**Categories**: cs.SD  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10468  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10468v1.pdf

**Abstract**:
> arXiv:2603.10468v1 Announce Type: cross 
Abstract: We study timestamped speaker-attributed ASR for long-form, multi-party speech with overlap, where chunk-wise inference must preserve meeting-level speaker identity consistency while producing time-stamped, speaker-labeled transcripts. Previous Speech-LLM systems tend to prioritize either local diarization or global labeling, but often lack the ability to capture fine-grained temporal boundaries or robust cross-chunk identity linking. We propose G-STAR, an end-to-end system that couples a time-aware speaker-tracking module with a Speech-LLM transcription backbone. The tracker provides structured speaker cues with temporal grounding, and the LLM generates attributed text conditioned on these cues. G-STAR supports both component-wise optimiza...

---

## 13. Geo-ATBench: A Benchmark for Geospatial Audio Tagging with Geospatial Semantic Context

**Authors**: Yuanbo Hou, Yanru Wu, Qiaoqiao Ren, Shengchen Li, Stephen Roberts, Dick Botteldooren  
**Categories**: cs.SD  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10623  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10623v1.pdf

**Abstract**:
> arXiv:2603.10623v1 Announce Type: cross 
Abstract: Environmental sound understanding in computational auditory scene analysis (CASA) is often formulated as an audio-only recognition problem. This formulation leaves a persistent drawback in multi-label audio tagging (AT): acoustic similarity can make certain events difficult to separate from waveforms alone. In such cases, disambiguating cues often lie outside the waveform. Geospatial semantic context (GSC), derived from geographic information system data, e.g., points of interest (POI), provides location-tied environmental priors that can help reduce this ambiguity. A systematic study of this direction is enabled through the proposed geospatial audio tagging (Geo-AT) task, which conditions multi-label sound event tagging on GSC alongside a...

---

## 14. V2M-Zero: Zero-Pair Time-Aligned Video-to-Music Generation

**Authors**: Yan-Bo Lin, Jonah Casebeer, Long Mai, Aniruddha Mahapatra, Gedas Bertasius, Nicholas J. Bryan  
**Categories**: cs.SD  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11042  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11042v1.pdf

**Abstract**:
> arXiv:2603.11042v1 Announce Type: cross 
Abstract: Generating music that temporally aligns with video events is challenging for existing text-to-music models, which lack fine-grained temporal control. We introduce V2M-Zero, a zero-pair video-to-music generation approach that outputs time-aligned music for video. Our method is motivated by a key observation: temporal synchronization requires matching when and how much change occurs, not what changes. While musical and visual events differ semantically, they exhibit shared temporal structure that can be captured independently within each modality. We capture this structure through event curves computed from intra-modal similarity using pretrained music and video encoders. By measuring temporal change within each modality independently, these...

---

## 15. Are Deep Speech Denoising Models Robust to Adversarial Noise?

**Authors**: Will Schwarzer, Neel Chaudhari, Philip S. Thomas, Andrea Fanelli, Xiaoyu Liu  
**Categories**: cs.SD  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2503.11627  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2503.11627v2.pdf

**Abstract**:
> arXiv:2503.11627v2 Announce Type: replace 
Abstract: Deep noise suppression (DNS) models enjoy widespread use throughout a variety of high-stakes speech applications. However, we show that four recent DNS models can each be reduced to outputting unintelligible gibberish through the addition of psychoacoustically hidden adversarial noise, even in low-background-noise and simulated over-the-air settings. For three of the models, a small transcription study with audio and multimedia experts confirms unintelligibility of the attacked audio; simultaneously, an ABX study shows that the adversarial noise is generally imperceptible, with some variance between participants and samples. While we also establish several negative results around targeted attacks and model transfer, our results neverthel...

---

## 16. Efficient Audio-Visual Speech Separation with Discrete Lip Semantics and Multi-Scale Global-Local Attention

**Authors**: Kai Li, Kejun Gao, Xiaolin Hu  
**Categories**: cs.SD  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2509.23610  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2509.23610v2.pdf

**Abstract**:
> arXiv:2509.23610v2 Announce Type: replace 
Abstract: Audio-visual speech separation (AVSS) methods leverage visual cues to extract target speech and have demonstrated strong separation quality in noisy acoustic environments. However, these methods usually involve a large number of parameters and require high computational cost, which is unacceptable in many applications where speech separation serves as only a preprocessing step for further speech processing. To address this issue, we propose an efficient AVSS method, named Dolphin. For visual feature extraction, we develop DP-LipCoder, a dual-path lightweight video encoder that transforms lip-motion into discrete audio-aligned semantic tokens. For audio separation, we construct a lightweight encoder-decoder separator, in which each layer ...

---

## 17. Modeling strategies for speech enhancement in the latent space of a neural audio codec

**Authors**: Sofiene Kammoun, Xavier Alameda-Pineda, Simon Leglaive  
**Categories**: cs.SD  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.26299  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.26299v3.pdf

**Abstract**:
> arXiv:2510.26299v3 Announce Type: replace 
Abstract: Neural audio codecs (NACs) provide compact latent speech representations in the form of sequences of continuous vectors or discrete tokens. In this work, we investigate how these two types of speech representations compare when used as training targets for supervised speech enhancement. We consider both autoregressive and non-autoregressive speech enhancement models based on the Conformer architecture, as well as a simple baseline where the NAC encoder is simply fine-tuned for speech enhancement. Our experiments reveal three key findings: predicting continuous latent representations consistently outperforms discrete token prediction; autoregressive models achieve higher quality but at the expense of intelligibility and efficiency, making...

---

## 18. Evaluation of Audio Compression Codecs

**Authors**: Thien T. Duong, Jan P. Springer  
**Categories**: cs.SD  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2511.11527  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2511.11527v2.pdf

**Abstract**:
> arXiv:2511.11527v2 Announce Type: replace 
Abstract: Perceptual quality of audio is the combination of aural accuracy and listener-perceived sound fidelity. It is how humans respond to the accuracy, intelligibility, and fidelity of aural media. Today this fidelity is also heavily influenced by the use of audio compression codecs for storing aural media in digital form. We argue that, when choosing an audio compression codec, users should not only look at compression efficiency but also consider the sonic perceptual quality properties of available audio compression codecs.
  We evaluate several commonly used audio compression codecs in terms of compression performance as well as their sonic perceptual quality via codec performance measurements, visualizations, and PEAQ scores. We demonstrat...

---

## 19. Robust Audio-Visual Target Speaker Extraction with Emotion-Aware Multiple Enrollment Fusion

**Authors**: Zhan Jin, Bang Zeng, Peijun Yang, Jiarong Du, Wei Ju, Yao Tian, Juan Liu, Ming Li  
**Categories**: cs.SD  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2509.12583  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2509.12583v3.pdf

**Abstract**:
> arXiv:2509.12583v3 Announce Type: replace-cross 
Abstract: Audio-Visual Target Speaker Extraction (AVTSE) is crucial for cocktail party scenarios. Leveraging multiple cues --such as utterance-level speaker embeddings or steady face images, and frame-level lip motion or facial expression features --can significantly improve performance. However, real-world applications often suffer from intermittent signal loss, especially for frame-level cues. This paper systematically investigates the robustness of multi-enrollment fusion under varying degrees of modality missing. Results show that while full multimodal fusion excels under ideal conditions, its performance degrades sharply when encountering unseen modalities missing during the testing. Crucially, training with a high missing rate dramatic...

---

## 20. Trade-offs between structural richness and communication efficiency in music network representations

**Authors**: Lluc Bono Rossell\'o, Robert Jankowski, Hugues Bersini, Mari\'an Bogu\~n\'a, M. \'Angeles Serrano  
**Categories**: cs.SD  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2509.14053  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2509.14053v3.pdf

**Abstract**:
> arXiv:2509.14053v3 Announce Type: replace-cross 
Abstract: Music is a structured and perceptually rich sequence of sounds in time, whose perception is shaped by the interplay of expectation and uncertainty about what comes next. Yet the uncertainty we infer from music depends on how the musical piece is encoded as an event sequence. In this work, we use network representations, in which event types are nodes and observed transitions are directed edges, to compare how different feature encodings shape the transition structure we recover and what this implies for both the descriptive uncertainty expectation under imperfect memory and noise. We systematically analyse eight encodings of piano music, from single-feature vocabularies to richer multi-feature combinations. These representational c...

---

## 21. HyWA: Hypernetwork Weight Adapting Personalized Voice Activity Detection

**Authors**: Mahsa Ghazvini Nejad, Hamed Jafarzadeh Asl, Amin Edraki, Mohammadreza Sadeghi, Masoud Asgharian, Yua...  
**Categories**: cs.SD  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.12947  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.12947v2.pdf

**Abstract**:
> arXiv:2510.12947v2 Announce Type: replace-cross 
Abstract: Personalized Voice Activity Detection (PVAD) systems activate only in response to a specific target speaker. Speaker-conditioning methods are employed to inject information about the target speaker into a VAD pipeline, to achieve personalization. Existing speaker-conditioning methods typically modify the inputs or activations of a VAD model. We propose an alternative perspective to speaker conditioning. Our approach, HyWA, employs a hypernetwork to generate personalized weights for a few selected layers of a standard VAD model. We evaluate HyWA against multiple baseline speaker-conditioning techniques using a fixed backbone VAD. Our comparison shows consistent improvements in PVAD performance. This new approach improves the current...

---

## 22. Calibration-Reasoning Framework for Descriptive Speech Quality Assessment

**Authors**: Elizaveta Kostenok, Mathieu Salzmann, Milos Cernak  
**Categories**: eess.AS  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10175  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10175v1.pdf

**Abstract**:
> arXiv:2603.10175v1 Announce Type: new 
Abstract: Explainable speech quality assessment requires moving beyond Mean Opinion Scores (MOS) to analyze underlying perceptual dimensions. To address this, we introduce a novel post-training method that tailors the foundational Audio Large Language Model for multidimensional reasoning, detection and classification of audio artifacts. First, a calibration stage aligns the model to predict predefined perceptual dimensions. Second, a reinforcement learning stage leverages Group Relative Policy Optimization (GRPO) with dimension-specific rewards to heavily enhance accuracy of descriptions and temporal localization of quality issues. With this approach we reach state-of-the-art results of 0.71 mean PCC score on the multidimensional QualiSpeech benchmark...

---

## 23. Speech Codec Probing from Semantic and Phonetic Perspectives

**Authors**: Xuan Shi, Chang Zeng, Tiantian Feng, Shih-Heng Wang, Jianbo Ma, Shrikanth Narayanan  
**Categories**: eess.AS  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10371  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10371v1.pdf

**Abstract**:
> arXiv:2603.10371v1 Announce Type: new 
Abstract: Speech tokenizers are essential for connecting speech to large language models (LLMs) in multimodal systems. These tokenizers are expected to preserve both semantic and acoustic information for downstream understanding and generation. However, emerging evidence suggests that what is termed "semantic" in speech representations does not align with text-derived semantics: a mismatch that can degrade multimodal LLM performance. In this paper, we systematically analyze the information encoded by several widely used speech tokenizers, disentangling their semantic and phonetic content through word-level probing tasks, layerwise representation analysis, and cross-modal alignment metrics such as CKA. Our results show that current tokenizers primarily...

---

## 24. MOS-Bias: From Hidden Gender Bias to Gender-Aware Speech Quality Assessment

**Authors**: Wenze Ren, Yi-Cheng Lin, Wen-Chin Huang, Erica Cooper, Ryandhimas E. Zezario, Hsin-Min Wang, Hung-yi...  
**Categories**: eess.AS  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10723  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10723v1.pdf

**Abstract**:
> arXiv:2603.10723v1 Announce Type: new 
Abstract: The Mean Opinion Score (MOS) serves as the standard metric for speech quality assessment, yet biases in human annotations remain underexplored. We conduct the first systematic analysis of gender bias in MOS, revealing that male listeners consistently assign higher scores than female listeners--a gap that is most pronounced in low-quality speech and gradually diminishes as quality improves. This quality-dependent structure proves difficult to eliminate through simple calibration. We further demonstrate that automated MOS models trained on aggregated labels exhibit predictions skewed toward male standards of perception. To address this, we propose a gender-aware model that learns gender-specific scoring patterns through abstracting binary grou...

---

## 25. Multi-View Based Audio Visual Target Speaker Extraction

**Authors**: Peijun Yang, Zhan Jin, Juan Liu, Ming Li  
**Categories**: eess.AS  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.07696  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.07696v2.pdf

**Abstract**:
> arXiv:2603.07696v2 Announce Type: replace 
Abstract: Audio-Visual Target Speaker Extraction (AVTSE) aims to separate a target speaker's voice from a mixed audio signal using the corresponding visual cues. While most existing AVTSE methods rely exclusively on frontal-view videos, this limitation restricts their robustness in real-world scenarios where non-frontal views are prevalent. Such visual perspectives often contain complementary articulatory information that could enhance speech extraction. In this work, we propose Multi-View Tensor Fusion (MVTF), a novel framework that transforms multi-view learning into single-view performance gains. During the training stage, we leverage synchronized multi-perspective lip videos to learn cross-view correlations through MVTF, where pairwise outer p...

---

## 26. Computational modeling of early language learning from acoustic speech and audiovisual input without linguistic priors

**Authors**: Okko R\"as\"anen  
**Categories**: eess.AS  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.08359  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.08359v2.pdf

**Abstract**:
> arXiv:2603.08359v2 Announce Type: replace-cross 
Abstract: Learning to understand speech appears almost effortless for typically developing infants, yet from an information-processing perspective, acquiring a language from acoustic speech is an enormous challenge. This chapter reviews recent developments in using computational models to understand early language acquisition from speech and audiovisual input. The focus is on self-supervised and visually grounded models of perceptual learning. We show how these models are becoming increasingly powerful in learning various aspects of speech without strong linguistic priors, and how many features of early language development can be explained through a shared set of learning principles-principles broadly compatible with multiple theories of la...

---

## 27. LWM-Temporal: Sparse Spatio-Temporal Attention for Wireless Channel Representation Learning

**Authors**: Sadjad Alikhani, Akshay Malhotra, Shahab Hamidi-Rad, Ahmed Alkhateeb  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10024  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10024v1.pdf

**Abstract**:
> arXiv:2603.10024v1 Announce Type: new 
Abstract: LWM-Temporal is a new member of the Large Wireless Models (LWM) family that targets the spatiotemporal nature of wireless channels. Designed as a task-agnostic foundation model, LWM-Temporal learns universal channel embeddings that capture mobility-induced evolution and are reusable across various downstream tasks. To achieve this objective, LWM-Temporal operates in the angle-delay-time domain and introduces Sparse Spatio-Temporal Attention (SSTA), a propagation-aligned attention mechanism that restricts interactions to physically plausible neighborhoods, reducing attention complexity by an order of magnitude while preserving geometry-consistent dependencies. LWM-Temporal is pretrained in a self-supervised manner using a physics-informed mas...

---

## 28. Gated Adaptation for Continual Learning in Human Activity Recognition

**Authors**: Reza Rahimi Azghan, Gautham Krishna Gudur, Mohit Malu, Edison Thomaz, Giulia Pedrielli, Pavan Turaga...  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10046  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10046v1.pdf

**Abstract**:
> arXiv:2603.10046v1 Announce Type: new 
Abstract: Wearable sensors in Internet of Things (IoT) ecosystems increasingly support applications such as remote health monitoring, elderly care, and smart home automation, all of which rely on robust human activity recognition (HAR). Continual learning systems must balance plasticity (learning new tasks) with stability (retaining prior knowledge), yet AI models often exhibit catastrophic forgetting, where learning new tasks degrades performance on earlier ones. This challenge is especially acute in domain-incremental HAR, where on-device models must adapt to new subjects with distinct movement patterns while maintaining accuracy on prior subjects without transmitting sensitive data to the cloud. We propose a parameter-efficient continual learning f...

---

## 29. Training Language Models via Neural Cellular Automata

**Authors**: Dan Lee, Seungwook Han, Akarsh Kumar, Pulkit Agrawal  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10055  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10055v1.pdf

**Abstract**:
> arXiv:2603.10055v1 Announce Type: new 
Abstract: Pre-training is crucial for large language models (LLMs), as it is when most representations and capabilities are acquired. However, natural language pre-training has problems: high-quality text is finite, it contains human biases, and it entangles knowledge with reasoning. This raises a fundamental question: is natural language the only path to intelligence? We propose using neural cellular automata (NCA) to generate synthetic, non-linguistic data for pre-pre-training LLMs--training on synthetic-then-natural language. NCA data exhibits rich spatiotemporal structure and statistics resembling natural language while being controllable and cheap to generate at scale. We find that pre-pre-training on only 164M NCA tokens improves downstream lang...

---

## 30. Dissecting Chronos: Sparse Autoencoders Reveal Causal Feature Hierarchies in Time Series Foundation Models

**Authors**: Anurag Mishra  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10071  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10071v1.pdf

**Abstract**:
> arXiv:2603.10071v1 Announce Type: new 
Abstract: Time series foundation models (TSFMs) are increasingly deployed in high-stakes domains, yet their internal representations remain opaque. We present the first application of sparse autoencoders (SAEs) to a TSFM, training TopK SAEs on activations of Chronos-T5-Large (710M parameters) across six layers. Through 392 single-feature ablation experiments, we establish that every ablated feature produces a positive CRPS degradation, confirming causal relevance. Our analysis reveals a depth-dependent hierarchy: early encoder layers encode low-level frequency features, the mid-encoder concentrates causally critical change-detection features, and the final encoder compresses a rich but less causally important taxonomy of temporal concepts. The most cr...

---

## 31. ES-dLLM: Efficient Inference for Diffusion Large Language Models by Early-Skipping

**Authors**: Zijian Zhu, Fei Ren, Zhanhong Tan, Kaisheng Ma  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10088  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10088v1.pdf

**Abstract**:
> arXiv:2603.10088v1 Announce Type: new 
Abstract: Diffusion large language models (dLLMs) are emerging as a promising alternative to autoregressive models (ARMs) due to their ability to capture bidirectional context and the potential for parallel generation. Despite the advantages, dLLM inference remains computationally expensive as the full input context is processed at every iteration. In this work, we analyze the generation dynamics of dLLMs and find that intermediate representations, including key, value, and hidden states, change only subtly across successive iterations. Leveraging this insight, we propose \textbf{ES-dLLM}, a training-free inference acceleration framework for dLLM that reduces computation by skipping tokens in early layers based on the estimated importance. Token impor...

---

## 32. A Survey of Weight Space Learning: Understanding, Representation, and Generation

**Authors**: Xiaolong Han, Zehong Wang, Bo Zhao, Binchi Zhang, Jundong Li, Damian Borth, Rose Yu, Haggai Maron, Y...  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10090  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10090v1.pdf

**Abstract**:
> arXiv:2603.10090v1 Announce Type: new 
Abstract: Neural network weights are typically viewed as the end product of training, while most deep learning research focuses on data, features, and architectures. However, recent advances show that the set of all possible weight values (weight space) itself contains rich structure: pretrained models form organized distributions, exhibit symmetries, and can be embedded, compared, or even generated. Understanding such structures has tremendous impact on how neural networks are analyzed and compared, and on how knowledge is transferred across models, beyond individual training instances. This emerging research direction, which we refer to as Weight Space Learning (WSL), treats neural weights as a meaningful domain for analysis and modeling. This surve...

---

## 33. ReMix: Reinforcement routing for mixtures of LoRAs in LLM finetuning

**Authors**: Ruizhong Qiu, Hanqing Zeng, Yinglong Xia, Yiwen Meng, Ren Chen, Jiarui Feng, Dongqi Fu, Qifan Wang, ...  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10160  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10160v1.pdf

**Abstract**:
> arXiv:2603.10160v1 Announce Type: new 
Abstract: Low-rank adapters (LoRAs) are a parameter-efficient finetuning technique that injects trainable low-rank matrices into pretrained models to adapt them to new tasks. Mixture-of-LoRAs models expand neural networks efficiently by routing each layer input to a small subset of specialized LoRAs of the layer. Existing Mixture-of-LoRAs routers assign a learned routing weight to each LoRA to enable end-to-end training of the router. Despite their empirical promise, we observe that the routing weights are typically extremely imbalanced across LoRAs in practice, where only one or two LoRAs often dominate the routing weights. This essentially limits the number of effective LoRAs and thus severely hinders the expressive power of existing Mixture-of-LoRA...

---

## 34. DT-BEHRT: Disease Trajectory-aware Transformer for Interpretable Patient Representation Learning

**Authors**: Deyi Li, Zijun Yao, Qi Xu, Muxuan Liang, Lingyao Li, Zijian Xu, Mei Liu  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10180  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10180v1.pdf

**Abstract**:
> arXiv:2603.10180v1 Announce Type: new 
Abstract: The growing adoption of electronic health record (EHR) systems has provided unprecedented opportunities for predictive modeling to guide clinical decision making. Structured EHRs contain longitudinal observations of patients across hospital visits, where each visit is represented by a set of medical codes. While sequence-based, graph-based, and graph-enhanced sequence approaches have been developed to capture rich code interactions over time or within the same visits, they often overlook the inherent heterogeneous roles of medical codes arising from distinct clinical characteristics and contexts. To this end, in this study we propose the Disease Trajectory-aware Transformer for EHR (DT-BEHRT), a graph-enhanced sequential architecture that di...

---

## 35. Rethinking the Harmonic Loss via Non-Euclidean Distance Layers

**Authors**: Maxwell Miller-Golub, Kamil Faber, Marcin Pietron, Panpan Zheng, Pasquale Minervini, Roberto Corizzo  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10225  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10225v1.pdf

**Abstract**:
> arXiv:2603.10225v1 Announce Type: new 
Abstract: Cross-entropy loss has long been the standard choice for training deep neural networks, yet it suffers from interpretability limitations, unbounded weight growth, and inefficiencies that can contribute to costly training dynamics. The harmonic loss is a distance-based alternative grounded in Euclidean geometry that improves interpretability and mitigates phenomena such as grokking, or delayed generalization on the test set. However, the study of harmonic loss remains narrow: only Euclidean distance is explored, and no systematic evaluation of computational efficiency or sustainability was conducted. We extend harmonic loss by systematically investigating a broad spectrum of distance metrics as replacements for the Euclidean distance. We comp...

---

## 36. GaLoRA: Parameter-Efficient Graph-Aware LLMs for Node Classification

**Authors**: Mayur Choudhary, Saptarshi Sengupta, Katerina Potika  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10298  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10298v1.pdf

**Abstract**:
> arXiv:2603.10298v1 Announce Type: new 
Abstract: The rapid rise of large language models (LLMs) and their ability to capture semantic relationships has led to their adoption in a wide range of applications. Text-attributed graphs (TAGs) are a notable example where LLMs can be combined with Graph Neural Networks to improve the performance of node classification. In TAGs, each node is associated with textual content and such graphs are commonly seen in various domains such as social networks, citation graphs, recommendation systems, etc. Effectively learning from TAGs would enable better representations of both structural and textual representations of the graph and improve decision-making in relevant domains. We present GaLoRA, a parameter-efficient framework that integrates structural info...

---

## 37. Domain-Adaptive Health Indicator Learning with Degradation-Stage Synchronized Sampling and Cross-Domain Autoencoder

**Authors**: Jungho Choo, Hanbyeol Park, Gawon Lee, Yunkyung Park, Hyerim Bae  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10430  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10430v1.pdf

**Abstract**:
> arXiv:2603.10430v1 Announce Type: new 
Abstract: The construction of high quality health indicators (HIs) is crucial for effective prognostics and health management. Although deep learning has significantly advanced HI modeling, existing approaches often struggle with distribution mismatches resulting from varying operating conditions. Although domain adaptation is typically employed to mitigate these shifts, two critical challenges remain: (1) the misalignment of degradation stages during random mini-batch sampling, resulting in misleading discrepancy losses, and (2) the structural limitations of small-kernel 1D-CNNs in capturing long-range temporal dependencies within complex vibration signals. To address these issues, we propose a domain-adaptive framework comprising degradation stage s...

---

## 38. The Curse and Blessing of Mean Bias in FP4-Quantized LLM Training

**Authors**: Hengjie Cao, Zhendong Huang, Mengyi Chen, Yifeng Yang, Fanqi Yu, Ruijun Huang, Fang Dong, Xin Zhang,...  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10444  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10444v1.pdf

**Abstract**:
> arXiv:2603.10444v1 Announce Type: new 
Abstract: Large language models trained on natural language exhibit pronounced anisotropy: a small number of directions concentrate disproportionate energy, while the remaining dimensions form a broad semantic tail. In low-bit training regimes, this geometry becomes numerically unstable. Because blockwise quantization scales are determined by extreme elementwise magnitudes, dominant directions stretch the dynamic range, compressing long-tail semantic variation into narrow numerical bins. We show that this instability is primarily driven by a coherent rank-one mean bias, which constitutes the dominant component of spectral anisotropy in LLM representations. This mean component emerges systematically across layers and training stages and accounts for th...

---

## 39. A Universal Nearest-Neighbor Estimator for Intrinsic Dimensionality

**Authors**: Eng-Jon Ong, Omer Bobrowski, Gesine Reinert, Primoz Skraba  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10493  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10493v1.pdf

**Abstract**:
> arXiv:2603.10493v1 Announce Type: new 
Abstract: Estimating the intrinsic dimensionality (ID) of data is a fundamental problem in machine learning and computer vision, providing insight into the true degrees of freedom underlying high-dimensional observations. Existing methods often rely on geometric or distributional assumptions and can significantly fail when these assumptions are violated. In this paper, we introduce a novel ID estimator based on nearest-neighbor distance ratios that involves simple calculations and achieves state-of-the-art results. Most importantly, we provide a theoretical analysis proving that our estimator is \emph{universal}, namely, it converges to the true ID independently of the distribution generating the data. We present experimental results on benchmark mani...

---

## 40. Surrogate models for nuclear fusion with parametric Shallow Recurrent Decoder Networks: applications to magnetohydrodynamics

**Authors**: M. Lo Verso, C. Introini, E. Cervi, L. Savoldi, J. N. Kutz, A. Cammi  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10678  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10678v1.pdf

**Abstract**:
> arXiv:2603.10678v1 Announce Type: new 
Abstract: Magnetohydrodynamic (MHD) effects play a key role in the design and operation of nuclear fusion systems, where electrically conducting fluids (such as liquid metals or molten salts in reactor blankets) interact with magnetic fields of varying intensity and orientation, which affect the resulting flow. The numerical resolution of MHD models involves highly nonlinear multiphysics systems of equations and can become computationally expensive, particularly in multi-query, parametric, or real-time contexts. This work investigates a fully data-driven framework for MHD state reconstruction that combines dimensionality reduction via Singular Value Decomposition (SVD) with the SHallow REcurrent Decoder (SHRED), a neural network architecture designed ...

---

## 41. Riemannian MeanFlow for One-Step Generation on Manifolds

**Authors**: Zichen Zhong, Haoliang Sun, Yukun Zhao, Yongshun Gong, Yilong Yin  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10718  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10718v1.pdf

**Abstract**:
> arXiv:2603.10718v1 Announce Type: new 
Abstract: Flow Matching enables simulation-free training of generative models on Riemannian manifolds, yet sampling typically still relies on numerically integrating a probability-flow ODE. We propose Riemannian MeanFlow (RMF), extending MeanFlow to manifold-valued generation where velocities lie in location-dependent tangent spaces. RMF defines an average-velocity field via parallel transport and derives a Riemannian MeanFlow identity that links average and instantaneous velocities for intrinsic supervision. We make this identity practical in a log-map tangent representation, avoiding trajectory simulation and heavy geometric computations. For stable optimization, we decompose the RMF objective into two terms and apply conflict-aware multi-task learn...

---

## 42. $V_{0.5}$: Generalist Value Model as a Prior for Sparse RL Rollouts

**Authors**: Yi-Kai Zhang, Yueqing Sun, Hongyan Hao, Qi Gu, Xunliang Cai, De-Chuan Zhan, Han-Jia Ye  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10848  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10848v1.pdf

**Abstract**:
> arXiv:2603.10848v1 Announce Type: new 
Abstract: In Reinforcement Learning with Verifiable Rewards (RLVR), constructing a robust advantage baseline is critical for policy gradients, effectively guiding the policy model to reinforce desired behaviors. Recent research has introduced Generalist Value Models (such as $V_0$), which achieve pre-trained value estimation by explicitly encoding model capabilities in-context, eliminating the need to synchronously update the value model alongside the policy model. In this paper, we propose $V_{0.5}$, which adaptively fuses the baseline predicted by such value model (acting as a prior) with the empirical mean derived from sparse rollouts. This constructs a robust baseline that balances computational efficiency with extremely low variance. Specifically...

---

## 43. SNPgen: Phenotype-Supervised Genotype Representation and Synthetic Data Generation via Latent Diffusion

**Authors**: Andrea Lampis, Michela Carlotta Massi, Nicola Pirastu, Francesca Ieva, Matteo Matteucci, Emanuele Di...  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10873  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10873v1.pdf

**Abstract**:
> arXiv:2603.10873v1 Announce Type: new 
Abstract: Polygenic risk scores and other genomic analyses require large individual-level genotype datasets, yet strict data access restrictions impede sharing. Synthetic genotype generation offers a privacy-preserving alternative, but most existing methods operate unconditionally, producing samples without phenotype alignment, or rely on unsupervised compression, creating a gap between statistical fidelity and downstream task utility. We present SNPgen, a two-stage conditional latent diffusion framework for generating phenotype-supervised synthetic genotypes. SNPgen combines GWAS-guided variant selection (1,024-2,048 trait-associated SNPs) with a variational autoencoder for genotype compression and a latent diffusion model conditioned on binary disea...

---

## 44. Historical Consensus: Preventing Posterior Collapse via Iterative Selection of Gaussian Mixture Priors

**Authors**: Zegu Zhang, Jian Zhang  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10935  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10935v1.pdf

**Abstract**:
> arXiv:2603.10935v1 Announce Type: new 
Abstract: Variational autoencoders (VAEs) frequently suffer from posterior collapse, where latent variables become uninformative and the approximate posterior degenerates to the prior. Recent work has characterized this phenomenon as a phase transition governed by the spectral properties of the data covariance matrix. In this paper, we propose a fundamentally different approach: instead of avoiding collapse through architectural constraints or hyperparameter tuning, we eliminate the possibility of collapse altogether by leveraging the multiplicity of Gaussian mixture model (GMM) clusterings. We introduce Historical Consensus Training, an iterative selection procedure that progressively refines a set of candidate GMM priors through alternating optimiza...

---

## 45. Bio-Inspired Self-Supervised Learning for Wrist-worn IMU Signals

**Authors**: Prithviraj Tarale, Kiet Chu, Abhishek Varghese, Kai-Chun Liu, Maxwell A Xu, Mohit Iyyer, Sunghoon I....  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10961  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10961v1.pdf

**Abstract**:
> arXiv:2603.10961v1 Announce Type: new 
Abstract: Wearable accelerometers have enabled large-scale health and wellness monitoring, yet learning robust human-activity representations has been constrained by the scarcity of labeled data. While self-supervised learning offers a potential remedy, existing approaches treat sensor streams as unstructured time series, overlooking the underlying biological structure of human movement, a factor we argue is critical for effective Human Activity Recognition (HAR). We introduce a novel tokenization strategy grounded in the submovement theory of motor control, which posits that continuous wrist motion is composed of superposed elementary basis functions called submovements. We define our token as the movement segment, a unit of motion composed of a fini...

---

## 46. Cross-Species Transfer Learning for Electrophysiology-to-Transcriptomics Mapping in Cortical GABAergic Interneurons

**Authors**: Theo Schwider, Ramin Ramezani  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11000  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11000v1.pdf

**Abstract**:
> arXiv:2603.11000v1 Announce Type: new 
Abstract: Single-cell electrophysiological recordings provide a powerful window into neuronal functional diversity and offer an interpretable route for linking intrinsic physiology to transcriptomic identity. Here, we replicate and extend the electrophysiology-to-transcriptomics framework introduced by Gouwens et al. (2020) using publicly available Allen Institute Patch-seq datasets from both mouse and human cortex. We focus on GABAergic inhibitory interneurons to target a subclass structure (Lamp5, Pvalb, Sst, Vip) that is comparable and conserved across species. After quality control, we analyzed 3,699 mouse visual cortex neurons and 506 human neocortical neurons from neurosurgical resections. Using standardized electrophysiological features and spa...

---

## 47. Leech Lattice Vector Quantization for Efficient LLM Compression

**Authors**: Tycho F. A. van der Ouderaa, Mart van Baalen, Paul Whatmough, Markus Nagel  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11021  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11021v1.pdf

**Abstract**:
> arXiv:2603.11021v1 Announce Type: new 
Abstract: Scalar quantization of large language models (LLMs) is fundamentally limited by information-theoretic bounds. While vector quantization (VQ) overcomes these limits by encoding blocks of parameters jointly, practical implementations must avoid the need for expensive lookup mechanisms or other explicit codebook storage. Lattice approaches address this through highly structured and dense packing. This paper explores the Leech lattice, which, with its optimal sphere packing and kissing configurations at 24 dimensions, is the highest dimensional lattice known with such optimal properties. To make the Leech lattice usable for LLM quantization, we extend an existing search algorithm based on the extended Golay code construction, to i) support index...

---

## 48. Probing the Limits of the Lie Detector Approach to LLM Deception

**Authors**: Tom-Felix Berger  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10003  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10003v1.pdf

**Abstract**:
> arXiv:2603.10003v1 Announce Type: cross 
Abstract: Mechanistic approaches to deception in large language models (LLMs) often rely on "lie detectors", that is, truth probes trained to identify internal representations of model outputs as false. The lie detector approach to LLM deception implicitly assumes that deception is coextensive with lying. This paper challenges that assumption. It experimentally investigates whether LLMs can deceive without producing false statements and whether truth probes fail to detect such behavior. Across three open-source LLMs, it is shown that some models reliably deceive by producing misleading non-falsities, particularly when guided by few-shot prompting. It is further demonstrated that truth probes trained on standard true-false datasets are significantly ...

---

## 49. GATech at AbjadGenEval Shared Task: Multilingual Embeddings for Arabic Machine-Generated Text Classification

**Authors**: Ahmed Khaled Khamis  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10007  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10007v1.pdf

**Abstract**:
> arXiv:2603.10007v1 Announce Type: cross 
Abstract: We present our approach to the AbjadGenEval shared task on detecting AI-generated Arabic text. We fine-tuned the multilingual E5-large encoder for binary classification, and we explored several pooling strategies to pool token representations, including weighted layer pooling, multi-head attention pooling, and gated fusion. Interestingly, none of these outperformed simple mean pooling, which achieved an F1 of 0.75 on the test set. We believe this is because complex pooling methods introduce additional parameters that need more data to train properly, whereas mean pooling offers a stable baseline that generalizes well even with limited examples. We also observe a clear pattern in the data: human-written texts tend to be significantly longer...

---

## 50. GATech at AbjadMed: Bidirectional Encoders vs. Causal Decoders: Insights from 82-Class Arabic Medical Classification

**Authors**: Ahmed Khaled Khamis  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10008  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10008v1.pdf

**Abstract**:
> arXiv:2603.10008v1 Announce Type: cross 
Abstract: This paper presents system description for Arabic medical text classification across 82 distinct categories. Our primary architecture utilizes a fine-tuned AraBERTv2 encoder enhanced with a hybrid pooling strategies, combining attention and mean representations, and multi-sample dropout for robust regularization. We systematically benchmark this approach against a suite of multilingual and Arabic-specific encoders, as well as several large-scale causal decoders, including zero-shot re-ranking via Llama 3.3 70B and feature extraction from Qwen 3B hidden states. Our findings demonstrate that specialized bidirectional encoders significantly outperform causal decoders in capturing the precise semantic boundaries required for fine-grained medic...

---

## 51. Tureis: Transformer-based Unified Resilience for IoT Devices in Smart Homes

**Authors**: Alireza Borhani, Vafa Andalibi, Bahar Asgari  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10038  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10038v1.pdf

**Abstract**:
> arXiv:2603.10038v1 Announce Type: cross 
Abstract: Smart-home IoT systems rely on heterogeneous sensor networks whose correctness shapes application behavior and the physical environment. However, these low-cost, resource-constrained sensors are highly prone to failure under real-world stressors. Prior methods often assume single-failure, single-resident settings, offer only failure detection rather than sensor-level localization, cover limited fault types and sensor modalities, require labels and human intervention, or impose overheads hindering edge deployment. To overcome these limitations, we propose Tureis, a self-supervised, context-aware method for failure detection and faulty-sensor localization in smart homes, designed for multi-failure, multi-resident edge settings. Tureis encode...

---

## 52. Where Do Flow Semantics Reside? A Protocol-Native Tabular Pretraining Paradigm for Encrypted Traffic Classification

**Authors**: Sizhe Huang, Shujie Yang  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10051  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10051v1.pdf

**Abstract**:
> arXiv:2603.10051v1 Announce Type: cross 
Abstract: Self-supervised masked modeling shows promise for encrypted traffic classification by masking and reconstructing raw bytes. Yet recent work reveals these methods fail to reduce reliance on labeled data despite costly pretraining: under frozen encoder evaluation, accuracy drops from greater than 0.9 to less than 0.47. We argue the root cause is inductive bias mismatch: flattening traffic into byte sequences destroys protocol-defined semantics. We identify three specific issues: 1) field unpredictability, random fields like ip.id are unlearnable yet treated as reconstruction targets; 2) embedding confusion, semantically distinct fields collapse into a unified embedding space; 3) metadata loss, capture-time metadata essential for temporal ana...

---

## 53. Unbalanced Optimal Transport Dictionary Learning for Unsupervised Hyperspectral Image Clustering

**Authors**: Joshua Lentz, Nicholas Karris, Alex Cloninger, James M. Murphy  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10132  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10132v1.pdf

**Abstract**:
> arXiv:2603.10132v1 Announce Type: cross 
Abstract: Hyperspectral images capture vast amounts of high-dimensional spectral information about a scene, making labeling an intensive task that is resistant to out-of-the-box statistical methods. Unsupervised learning of clusters allows for automated segmentation of the scene, enabling a more rapid understanding of the image. Partitioning the spectral information contained within the data via dictionary learning in Wasserstein space has proven an effective method for unsupervised clustering. However, this approach requires balancing the spectral profiles of the data, blurring the classes, and sacrificing robustness to outliers and noise. In this paper, we suggest improving this approach by utilizing unbalanced Wasserstein barycenters to learn a l...

---

## 54. ARCHE: Autoregressive Residual Compression with Hyperprior and Excitation

**Authors**: Sofia Iliopoulou, Dimitris Ampeliotis, Athanassios Skodras  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10188  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10188v1.pdf

**Abstract**:
> arXiv:2603.10188v1 Announce Type: cross 
Abstract: Recent progress in learning-based image compression has demonstrated that end-to-end optimization can substantially outperform traditional codecs by jointly learning compact latent representations and probabilistic entropy models. However, many existing approaches achieve high rate-distortion efficiency at the expense of increased computational cost and limited parallelism. This paper presents ARCHE - Autoregressive Residual Compression with Hyperprior and Excitation, an end-to-end learned image compression framework that balances modeling accuracy and computational efficiency. The proposed architecture unifies hierarchical, spatial, and channel-based priors within a single probabilistic framework, capturing both global and local dependenc...

---

## 55. One Adapter for All: Towards Unified Representation in Step-Imbalanced Class-Incremental Learning

**Authors**: Xiaoyan Zhang, Jiangpeng He  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10237  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10237v1.pdf

**Abstract**:
> arXiv:2603.10237v1 Announce Type: cross 
Abstract: Class-incremental learning (CIL) aims to acquire new classes over time while retaining prior knowledge, yet most setups and methods assume balanced task streams. In practice, the number of classes per task often varies significantly. We refer to this as step imbalance, where large tasks that contain more classes dominate learning and small tasks inject unstable updates. Existing CIL methods assume balanced tasks and therefore treat all tasks uniformly, producing imbalanced updates that degrade overall learning performance. To address this challenge, we propose One-A, a unified and imbalance-aware framework that incrementally merges task updates into a single adapter, maintaining constant inference cost. One-A performs asymmetric subspace a...

---

## 56. Quantum entanglement provides a competitive advantage in adversarial games

**Authors**: Peiyong Wang, Kieran Hymas, James Quach  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10289  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10289v1.pdf

**Abstract**:
> arXiv:2603.10289v1 Announce Type: cross 
Abstract: Whether uniquely quantum resources confer advantages in fully classical, competitive environments remains an open question. Competitive zero-sum reinforcement learning is particularly challenging, as success requires modelling dynamic interactions between opposing agents rather than static state-action mappings. Here, we conduct a controlled study isolating the role of quantum entanglement in a quantum-classical hybrid agent trained on Pong, a competitive Markov game. An 8-qubit parameterised quantum circuit serves as a feature extractor within a proximal policy optimisation framework, allowing direct comparison between separable circuits and architectures incorporating fixed (CZ) or trainable (IsingZZ) entangling gates. Entangled circuits...

---

## 57. Dual Space Preconditioning for Gradient Descent in the Overparameterized Regime

**Authors**: Reza Ghane, Danil Akhtiamov, Babak Hassibi  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10485  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10485v1.pdf

**Abstract**:
> arXiv:2603.10485v1 Announce Type: cross 
Abstract: In this work we study the convergence properties of the Dual Space Preconditioned Gradient Descent, encompassing optimizers such as Normalized Gradient Descent, Gradient Clipping and Adam. We consider preconditioners of the form $\nabla K$, where $K: \mathbb{R}^p \to \mathbb{R}$ is convex and assume that the latter is applied to train an over-parameterized linear model with loss of the form $\ell({X} {W} - {Y})$, for weights ${W} \in \mathbb{R}^{d \times k}$, labels ${Y} \in \mathbb{R}^{n \times k}$ and data ${X} \in \mathbb{R}^{n \times d}$. Under the aforementioned assumptions, we prove that the iterates of the preconditioned gradient descent always converge to a point ${W}_{\infty} \in \mathbb{R}^{d \times k}$ satisfying ${X}{W}_{\infty...

---

## 58. A New Tensor Network: Tubal Tensor Train and Its Applications

**Authors**: Salman Ahmadi-Asl, Valentin Leplat, Anh-Huy Phan, Andrzej Cichocki  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10503  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10503v1.pdf

**Abstract**:
> arXiv:2603.10503v1 Announce Type: cross 
Abstract: We introduce the tubal tensor train (TTT) decomposition, a tensor-network model that combines the t-product algebra of the tensor singular value decomposition (T-SVD) with the low-order core structure of the tensor train (TT) format. For an order-$(N+1)$ tensor with a distinguished tube mode, the proposed representation consists of two third-order boundary cores and $N-2$ fourth-order interior cores linked through the t-product. As a result, for bounded tubal ranks, the storage scales linearly with the number of modes, in contrast to direct high-order extensions of T-SVD. We present two computational strategies: a sequential fixed-rank construction, called TTT-SVD, and a Fourier-slice alternating scheme based on the alternating two-cores u...

---

## 59. Detecting and Eliminating Neural Network Backdoors Through Active Paths with Application to Intrusion Detection

**Authors**: Eirik H{\o}yheim, Magnus Wiik Eckhoff, Gudmund Grov, Robert Flood, David Aspinall  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10641  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10641v1.pdf

**Abstract**:
> arXiv:2603.10641v1 Announce Type: cross 
Abstract: Machine learning backdoors have the property that the machine learning model should work as expected on normal inputs, but when the input contains a specific $\textit{trigger}$, it behaves as the attacker desires. Detecting such triggers has been proven to be extremely difficult. In this paper, we present a novel and explainable approach to detect and eliminate such backdoor triggers based on active paths found in neural networks. We present promising experimental evidence of our approach, which involves injecting backdoors into a machine learning model used for intrusion detection.

---

## 60. Pointy - A Lightweight Transformer for Point Cloud Foundation Models

**Authors**: Konrad Szafer, Marek Kraft, Dominik Belter  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10963  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10963v1.pdf

**Abstract**:
> arXiv:2603.10963v1 Announce Type: cross 
Abstract: Foundation models for point cloud data have recently grown in capability, often leveraging extensive representation learning from language or vision. In this work, we take a more controlled approach by introducing a lightweight transformer-based point cloud architecture. In contrast to the heavy reliance on cross-modal supervision, our model is trained only on 39k point clouds - yet it outperforms several larger foundation models trained on over 200k training samples. Interestingly, our method approaches state-of-the-art results from models that have seen over a million point clouds, images, and text samples, demonstrating the value of a carefully curated training setup and architecture. To ensure rigorous evaluation, we conduct a comprehe...

---

## 61. Large Language Models for Travel Behavior Prediction

**Authors**: Baichuan Mo, Hanyong Xu, Ruoyun Ma, Jung-Hoon Cho, Dingyi Zhuang, Xiaotong Guo, Jinhua Zhao  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2312.00819  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2312.00819v2.pdf

**Abstract**:
> arXiv:2312.00819v2 Announce Type: replace 
Abstract: Travel behavior prediction is a core problem in transportation demand management and is traditionally addressed using numerical models calibrated on observed data. With recent advances in large language models (LLMs), new opportunities have emerged to model human decision-making through natural language reasoning. This study explores the use of LLMs for travel behavior prediction through two complementary frameworks. The first framework employs a zero-shot prompting strategy, where the prediction task, traveler attributes, and relevant domain knowledge are described in text, enabling the LLM to directly generate predictions without task-specific training data. The second framework uses LLM-generated text embeddings as high-level represen...

---

## 62. Mamba Neural Operator: Who Wins? Transformers vs. State-Space Models for PDEs

**Authors**: Chun-Wun Cheng, Jiahao Huang, Yi Zhang, Guang Yang, Carola-Bibiane Sch\"onlieb, Angelica I. Aviles-R...  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2410.02113  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2410.02113v3.pdf

**Abstract**:
> arXiv:2410.02113v3 Announce Type: replace 
Abstract: Partial differential equations (PDEs) are widely used to model complex physical systems, but solving them efficiently remains a significant challenge. Recently, Transformers have emerged as the preferred architecture for PDEs due to their ability to capture intricate dependencies. However, they struggle with representing continuous dynamics and long-range interactions. To overcome these limitations, we introduce the Mamba Neural Operator (MNO), a novel framework that enhances neural operator-based techniques for solving PDEs. MNO establishes a formal theoretical connection between structured state-space models (SSMs) and neural operators, offering a unified structure that can adapt to diverse architectures, including Transformer-based mo...

---

## 63. CARTGen-IR: Synthetic Tabular Data Generation for Imbalanced Regression

**Authors**: Ant\'onio Pedro Pinheiro, Rita P. Ribeiro  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2506.02811  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2506.02811v2.pdf

**Abstract**:
> arXiv:2506.02811v2 Announce Type: replace 
Abstract: Handling imbalanced target distributions in regression poses a persistent challenge, as the underrepresentation of relevant target values can significantly hinder model performance. Existing data-level solutions often adapt classification-oriented techniques, introducing arbitrary thresholds over the continuous target and leading to artificial and potentially misleading problem formulations. Deep generative models offer flexible sample synthesis but are computationally intensive and difficult to interpret. We propose a CART-based synthetic sampling method specifically designed for imbalanced regression on tabular data. The method integrates relevance- and density-guided sampling to address sparse target regions without thresholding, and ...

---

## 64. Silhouette-Driven Instance-Weighted $k$-means

**Authors**: Aggelos Semoglou, Aristidis Likas, John Pavlopoulos  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2506.12878  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2506.12878v2.pdf

**Abstract**:
> arXiv:2506.12878v2 Announce Type: replace 
Abstract: Clustering is a fundamental unsupervised learning task with applications across a wide range of domains. Popular algorithms such as $k$-means are efficient and widely used, but can be sensitive to outliers, ambiguous boundary points, and heterogeneous cluster geometry, which may distort centroid estimates and yield suboptimal partitions. We introduce K-Sil, a silhouette-driven $k$-means variant that, at each iteration, weights points using a centroid-margin proxy for the silhouette score, emphasizing confidently assigned instances while down-weighting borderline or noisy regions. Centroid updates take the form of a softmax-weighted mean, and an adaptive temperature automatically calibrates the sharpness of the weight distribution using a...

---

## 65. Global Minimizers of Sigmoid Contrastive Loss

**Authors**: Kiril Bangachev, Guy Bresler, Iliyas Noman, Yury Polyanskiy  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2509.18552  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2509.18552v2.pdf

**Abstract**:
> arXiv:2509.18552v2 Announce Type: replace 
Abstract: The meta-task of obtaining and aligning representations through contrastive pretraining is steadily gaining importance since its introduction in CLIP and ALIGN. In this paper we theoretically explain the advantages of synchronizing with trainable inverse temperature and bias under the sigmoid loss, as implemented in the recent SigLIP and SigLIP2 models of Google DeepMind. Temperature and bias can drive the loss function to zero for a rich class of configurations that we call $(\mathsf{m}, \mathsf{b}_{\mathsf{rel}})$-Constellations. $(\mathsf{m}, \mathsf{b}_{\mathsf{rel}})$-Constellations are a novel combinatorial object related to spherical codes and are parametrized by a margin $\mathsf{m}$ and relative bias $\mathsf{b}_{\mathsf{rel}}$....

---

## 66. One-Prompt Strikes Back: Sparse Mixture of Experts for Prompt-based Continual Learning

**Authors**: Minh Le, Bao-Ngoc Dao, Huy Nguyen, Quyen Tran, Anh Nguyen, Nhat Ho  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2509.24483  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2509.24483v3.pdf

**Abstract**:
> arXiv:2509.24483v3 Announce Type: replace 
Abstract: Prompt-based methods have recently gained prominence in Continual Learning (CL) due to their strong performance and memory efficiency. A prevalent strategy in this paradigm assigns a dedicated subset of prompts to each task, which, while effective, incurs substantial computational overhead and causes memory requirements to scale linearly with the number of tasks. Conversely, approaches employing a single shared prompt across tasks offer greater efficiency but often suffer from degraded performance due to knowledge interference. To reconcile this trade-off, we propose SMoPE, a novel framework that integrates the benefits of both task-specific and shared prompt strategies. Inspired by recent findings on the relationship between Prefix Tuni...

---

## 67. Pretrained battery transformer (PBT): A foundation model for universal battery life prediction

**Authors**: Ruifeng Tan, Weixiang Hong, Jia Li, Jiaqiang Huang, Tong-Yi Zhang  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2512.16334  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2512.16334v5.pdf

**Abstract**:
> arXiv:2512.16334v5 Announce Type: replace 
Abstract: Early prediction of battery cycle life is essential for improving battery design, manufacturing, and deployment. However, despite encouraging results with machine learning, progress remains constrained by scarce data and data heterogeneity across battery chemistries, specifications, formation protocols, and operating conditions. Although transfer learning has been widely explored to alleviate these challenges, its effectiveness is constrained by the lack of a foundation model that can capture broadly transferable knowledge from diverse battery life data. This gap persists because integration of heterogeneous battery datasets under data scarcity is inherently challenging. Here we introduce the pretrained battery transformer (PBT), a found...

---

## 68. Geometric Scaling of Bayesian Inference in LLMs

**Authors**: Naman Agarwal, Siddhartha R. Dalal, Vishal Misra  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2512.23752  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2512.23752v4.pdf

**Abstract**:
> arXiv:2512.23752v4 Announce Type: replace 
Abstract: Recent work has shown that small transformers trained in controlled "wind-tunnel'' settings can implement exact Bayesian inference, and that their training dynamics produce a geometric substrate -- low-dimensional value manifolds and progressively orthogonal keys -- that encodes posterior structure. We investigate whether this geometric signature persists in production-grade language models. Across Pythia, Phi-2, Llama-3, and Mistral families, we find that last-layer value representations organize along a single dominant axis whose position strongly correlates with predictive entropy, and that domain-restricted prompts collapse this structure into the same low-dimensional manifolds observed in synthetic settings.
  To probe the role of t...

---

## 69. Inferring Clinically Relevant Molecular Subtypes of Pancreatic Cancer from Routine Histopathology Using Deep Learning

**Authors**: Abdul Rehman Akbar, Alejandro Levya, Ashwini Esnakula, Elshad Hasanov, Anne Noonan, Lingbin Meng, Su...  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2601.03410  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2601.03410v2.pdf

**Abstract**:
> arXiv:2601.03410v2 Announce Type: replace 
Abstract: Molecular subtyping of PDAC into basal-like and classical has established prognostic and predictive value. However, its use in clinical practice is limited by cost, turnaround time, and tissue requirements, thereby restricting its application in the management of PDAC. We introduce PanSubNet, an interpretable deep learning framework that predicts therapy-relevant molecular subtypes directly from standard H&amp;E-stained WSIs. PanSubNet was developed using data from 1,055 patients across two multi-institutional cohorts (PANCAN, n=846; TCGA, n=209) with paired histology and RNA-seq data. Ground-truth labels were derived using the validated Moffitt 50-gene signature refined by GATA6 expression. The model employs dual-scale architecture that...

---

## 70. BD-Merging: Bias-Aware Dynamic Model Merging with Evidence-Guided Contrastive Learning

**Authors**: Yuhan Xie, Chen Lyu  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.03920  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.03920v2.pdf

**Abstract**:
> arXiv:2603.03920v2 Announce Type: replace 
Abstract: Model Merging (MM) has emerged as a scalable paradigm for multi-task learning (MTL), enabling multiple task-specific models to be integrated without revisiting the original training data. Despite recent progress, the reliability of MM under test-time distribution shift remains insufficiently understood. Most existing MM methods typically assume that test data are clean and distributionally aligned with both the training and auxiliary sources. However, this assumption rarely holds in practice, often resulting in biased predictions with degraded generalization. To address this issue, we present BD-Merging, a bias-aware unsupervised model merging framework that explicitly models uncertainty to achieve adaptive reliability under distribution...

---

## 71. Task Aware Modulation Using Representation Learning for Upsaling of Terrestrial Carbon Fluxes

**Authors**: Aleksei Rozanov, Arvind Renganathan, Vipin Kumar  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.09974  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.09974v2.pdf

**Abstract**:
> arXiv:2603.09974v2 Announce Type: replace 
Abstract: Accurately upscaling terrestrial carbon fluxes is central to estimating the global carbon budget, yet remains challenging due to the sparse and regionally biased distribution of ground measurements. Existing data-driven upscaling products often fail to generalize beyond observed domains, leading to systematic regional biases and high predictive uncertainty. We introduce Task-Aware Modulation with Representation Learning (TAM-RL), a framework that couples spatio-temporal representation learning with knowledge-guided encoder-decoder architecture and loss function derived from the carbon balance equation. Across 150+ flux tower sites representing diverse biomes and climate regimes, TAM-RL improves predictive performance relative to existing...

---

## 72. Consistency-based Abductive Reasoning over Perceptual Errors of Multiple Pre-trained Models in Novel Environments

**Authors**: Mario Leiva, Noel Ngu, Joshua Shay Kricheli, Aditya Taparia, Ransalu Senanayake, Paulo Shakarian, Na...  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2505.19361  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2505.19361v5.pdf

**Abstract**:
> arXiv:2505.19361v5 Announce Type: replace-cross 
Abstract: The deployment of pre-trained perception models in novel environments often leads to performance degradation due to distributional shifts. Although recent artificial intelligence approaches for metacognition use logical rules to characterize and filter model errors, improving precision often comes at the cost of reduced recall. This paper addresses the hypothesis that leveraging multiple pre-trained models can mitigate this recall reduction. We formulate the challenge of identifying and managing conflicting predictions from various models as a consistency-based abduction problem, building on the idea of abductive learning (ABL) but applying it to test-time instead of training. The input predictions and the learned error detection r...

---

## 73. The Yokai Learning Environment: Tracking Beliefs Over Space and Time

**Authors**: Constantin Ruhdorfer, Matteo Bortoletto, Johannes Forkel, Jakob Foerster, Andreas Bulling  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2508.12480  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2508.12480v2.pdf

**Abstract**:
> arXiv:2508.12480v2 Announce Type: replace-cross 
Abstract: The ability to cooperate with unknown partners is a central challenge in cooperative AI and widely studied in the form of zero-shot coordination (ZSC), which evaluates an algorithm by measuring the performance of independently trained agents when paired. The Hanabi Learning Environment (HLE) has become the dominant benchmark for ZSC, but recent work has achieved near-perfect inter-seed cross-play performance, limiting its ability to track algorithmic progress. We introduce the Yokai Learning Environment (YLE) - an open-source multi-agent RL benchmark in which effective collaboration requires building common ground by tracking and updating beliefs over moving cards, reasoning under ambiguous hints, and deciding when to terminate the...

---

## 74. Uncovering Semantic Selectivity of Latent Groups in Higher Visual Cortex with Mutual Information-Guided Diffusion

**Authors**: Yule Wang, Joseph Yu, Chengrui Li, Weihan Li, Anqi Wu  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.02182  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.02182v2.pdf

**Abstract**:
> arXiv:2510.02182v2 Announce Type: replace-cross 
Abstract: Understanding how neural populations in higher visual areas encode object-centered visual information remains a central challenge in computational neuroscience. Prior works have investigated representational alignment between artificial neural networks and the visual cortex. Nevertheless, these findings are indirect and offer limited insights to the structure of neural populations themselves. Similarly, decoding-based methods have quantified semantic features from neural populations but have not uncovered their underlying organizations. This leaves open a scientific question: "how feature-specific visual information is distributed across neural populations in higher visual areas, and whether it is organized into structured, semanti...

---

## 75. A Systematic Evaluation of Self-Supervised Learning for Label-Efficient Sleep Staging with Wearable EEG

**Authors**: Emilio Estevan, Mar\'ia Sierra-Torralba, Eduardo L\'opez-Larraz, Luis Montesano  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.07960  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.07960v3.pdf

**Abstract**:
> arXiv:2510.07960v3 Announce Type: replace-cross 
Abstract: Wearable EEG devices have emerged as a promising alternative to polysomnography (PSG). As affordable and scalable solutions, their widespread adoption results in the collection of massive volumes of unlabeled data that cannot be analyzed by clinicians at scale. Meanwhile, the recent success of deep learning for sleep scoring has relied on large annotated datasets. Self-supervised learning (SSL) offers an opportunity to bridge this gap, leveraging unlabeled signals to address label scarcity and reduce annotation effort. In this paper, we present the first systematic evaluation of SSL for sleep staging using wearable EEG. We introduce a structured benchmarking framework encompassing a range of SSL paradigms and propose a specialized ...

---

## 76. PvP: Data-Efficient Humanoid Robot Learning with Proprioceptive-Privileged Contrastive Representations

**Authors**: Mingqi Yuan, Tao Yu, Haolin Song, Bo Li, Xin Jin, Hua Chen, Wenjun Zeng  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2512.13093  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2512.13093v2.pdf

**Abstract**:
> arXiv:2512.13093v2 Announce Type: replace-cross 
Abstract: Achieving efficient and robust whole-body control (WBC) is essential for enabling humanoid robots to perform complex tasks in dynamic environments. Despite the success of reinforcement learning (RL) in this domain, its sample inefficiency remains a significant challenge due to the intricate dynamics and partial observability of humanoid robots. To address this limitation, we propose PvP, a Proprioceptive-Privileged contrastive learning framework that leverages the intrinsic complementarity between proprioceptive and privileged states. PvP learns compact and task-relevant latent representations without requiring hand-crafted data augmentations, enabling faster and more stable policy learning. To support systematic evaluation, we dev...

---

## 77. NMIRacle: Multi-modal Generative Molecular Elucidation from IR and NMR Spectra

**Authors**: Federico Ottomano, Yingzhen Li, Alex M. Ganose  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2512.19733  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2512.19733v2.pdf

**Abstract**:
> arXiv:2512.19733v2 Announce Type: replace-cross 
Abstract: Molecular structure elucidation from spectroscopic data is a long-standing challenge in Chemistry, traditionally requiring expert interpretation. We introduce NMIRacle, a two-stage generative framework that builds upon recent paradigms in AI-driven spectroscopy with minimal assumptions. In the first stage, NMIRacle learns to reconstruct molecular structures from count-aware fragment representations, capturing both fragment identities and their occurrences. In the second stage, a spectral encoder maps input spectra (IR, 1H-NMR, 13C-NMR) into a latent embedding used to condition the pre-trained generator, which is fine-tuned for direct spectra-to-molecule generation. This formulation bridges fragment-level chemical modeling with spec...

---

## 78. Many AI Analysts, One Dataset: Navigating the Agentic Data Science Multiverse

**Authors**: Martin Bertran, Riccardo Fogliato, Zhiwei Steven Wu  
**Categories**: cs.LG  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.18710  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.18710v2.pdf

**Abstract**:
> arXiv:2602.18710v2 Announce Type: replace-cross 
Abstract: Empirical conclusions depend not only on data but on analytic decisions made throughout the research process. Many-analyst studies have quantified this dependence: independent teams testing the same hypothesis on the same dataset regularly reach conflicting conclusions. But such studies require costly human coordination and are rarely conducted. We show that fully autonomous AI analysts built on large language models (LLMs) can, cheaply and at scale, replicate the structured analytic diversity observed in human multi-analyst studies. In our framework, each AI analyst independently executes a complete analysis pipeline on a fixed dataset and hypothesis; a separate AI auditor screens every run for methodological validity. Across thre...

---

## 79. The System Hallucination Scale (SHS): A Minimal yet Effective Human-Centered Instrument for Evaluating Hallucination-Related Behavior in Large Language Models

**Authors**: Heimo M\"uller, Dominik Steiger, Markus Plass, Andreas Holzinger  
**Categories**: cs.AI  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.09989  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.09989v1.pdf

**Abstract**:
> arXiv:2603.09989v1 Announce Type: cross 
Abstract: We introduce the System Hallucination Scale (SHS), a lightweight and human-centered measurement instrument for assessing hallucination-related behavior in large language models (LLMs). Inspired by established psychometric tools such as the System Usability Scale (SUS) and the System Causability Scale (SCS), SHS enables rapid, interpretable, and domain-agnostic evaluation of factual unreliability, incoherence, misleading presentation, and responsiveness to user guidance in model-generated text. SHS is explicitly not an automatic hallucination detector or benchmark metric; instead, it captures how hallucination phenomena manifest from a user perspective under realistic interaction conditions. A real-world evaluation with 210 participants dem...

---

## 80. PoultryLeX-Net: Domain-Adaptive Dual-Stream Transformer Architecture for Large-Scale Poultry Stakeholder Modeling

**Authors**: Stephen Afrifa, Biswash Khatiwada, Kapalik Khanal, Sanjay Shah, Lingjuan Wang-Li, Ramesh Bahadur Bis...  
**Categories**: cs.AI  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.09991  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.09991v1.pdf

**Abstract**:
> arXiv:2603.09991v1 Announce Type: cross 
Abstract: The rapid growth of the global poultry industry, driven by rising demand for affordable animal protein, has intensified public discourse surrounding production practices, housing, management, animal welfare, and supply-chain transparency. Social media platforms such as X (formerly Twitter) generate large volumes of unstructured textual data that capture stakeholder sentiment across the poultry industry. Extracting accurate sentiment signals from this domain-specific discourse remains challenging due to contextual ambiguity, linguistic variability, and limited domain awareness in general-purpose language models. This study presents PoultryLeX-Net, a lexicon-enhanced, domain-adaptive dual-stream transformer framework for fine-grained sentime...

---

## 81. Evaluating Adjective-Noun Compositionality in LLMs: Functional vs Representational Perspectives

**Authors**: Ruchira Dhar, Qiwei Peng, Anders S{\o}gaard  
**Categories**: cs.AI  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.09994  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.09994v1.pdf

**Abstract**:
> arXiv:2603.09994v1 Announce Type: cross 
Abstract: Compositionality is considered central to language abilities. As performant language systems, how do large language models (LLMs) do on compositional tasks? We evaluate adjective-noun compositionality in LLMs using two complementary setups: prompt-based functional assessment and a representational analysis of internal model states. Our results reveal a striking divergence between task performance and internal states. While LLMs reliably develop compositional representations, they fail to translate consistently into functional task success across model variants. Consequently, we highlight the importance of contrastive evaluation for obtaining a more complete understanding of model capabilities.

---

## 82. Evaluating Progress in Graph Foundation Models: A Comprehensive Benchmark and New Insights

**Authors**: Xingtong Yu, Shenghua Ye, Ruijuan Liang, Chang Zhou, Hong Cheng, Xinming Zhang, Yuan Fang  
**Categories**: cs.AI  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10033  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10033v1.pdf

**Abstract**:
> arXiv:2603.10033v1 Announce Type: cross 
Abstract: Graph foundation models (GFM) aim to acquire transferable knowledge by pre-training on diverse graphs, which can be adapted to various downstream tasks. However, domain shift in graphs is inherently two-dimensional: graphs differ not only in what they describe (topic domains) but also in how they are represented (format domains). Most existing GFM benchmarks vary only topic domains, thereby obscuring how knowledge transfers across both dimensions. We present a new benchmark that jointly evaluates topic and format gaps across the full GFM pipeline, including multi-domain self-supervised pre-training and few-shot downstream adaptation, and provides a timely evaluation of recent GFMs in the rapidly evolving landscape. Our protocol enables con...

---

## 83. Social Knowledge for Cross-Domain User Preference Modeling

**Authors**: Nir Lotan, Adir Solomon, Ido Guy, Einat Minkov  
**Categories**: cs.AI  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10148  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10148v1.pdf

**Abstract**:
> arXiv:2603.10148v1 Announce Type: cross 
Abstract: We demonstrate that user preferences can be represented and predicted across topical domains using large-scale social modeling. Given information about popular entities favored by a user, we project the user into a social embedding space learned from a large-scale sample of the Twitter (now X) network. By representing both users and popular entities in a joint social space, we can assess the relevance of candidate entities (e.g., music artists) using cosine similarity within this embedding space. A comprehensive evaluation using link prediction experiments shows that this method achieves effective personalization in zero-shot setting, when no user feedback is available for entities in the target domain, yielding substantial improvements ov...

---

## 84. Compatibility at a Cost: Systematic Discovery and Exploitation of MCP Clause-Compliance Vulnerabilities

**Authors**: Nanzi Yang, Weiheng Bai, Kangjie Lu  
**Categories**: cs.AI  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10163  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10163v1.pdf

**Abstract**:
> arXiv:2603.10163v1 Announce Type: cross 
Abstract: The Model Context Protocol (MCP) is a recently proposed interoperability standard that unifies how AI agents connect with external tools and data sources. By defining a set of common client-server message exchange clauses, MCP replaces fragmented integrations with a standardized, plug-and-play framework. However, to be compatible with diverse AI agents, the MCP specification relaxes many behavioral constraints into optional clauses, leading to misuse-prone SDK implementation. We identify it as a new attack surface that allows adversaries to achieve multiple attacks (e.g, silent prompt injection, DoS, etc.), named as \emph{compatibility-abusing attacks}.
  In this work, we present the first systematic framework for analyzing this new attack...

---

## 85. Delta-K: Boosting Multi-Instance Generation via Cross-Attention Augmentation

**Authors**: Zitong Wang, Zijun Shen, Haohao Xu, Zhengjie Luo, Weibin Wu  
**Categories**: cs.AI  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10210  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10210v1.pdf

**Abstract**:
> arXiv:2603.10210v1 Announce Type: cross 
Abstract: While Diffusion Models excel in text-to-image synthesis, they often suffer from concept omission when synthesizing complex multi-instance scenes. Existing training-free methods attempt to resolve this by rescaling attention maps, which merely exacerbates unstructured noise without establishing coherent semantic representations. To address this, we propose Delta-K, a backbone-agnostic and plug-and-play inference framework that tackles omission by operating directly in the shared cross-attention Key space. Specifically, with Vision-language model, we extract a differential key $\Delta K$ that encodes the semantic signature of missing concepts. This signal is then injected during the early semantic planning stage of the diffusion process. Gov...

---

## 86. Robotic Ultrasound Makes CBCT Alive

**Authors**: Feng Li, Ziyuan Li, Zhongliang Jiang, Nassir Navab, Yuan Bi  
**Categories**: cs.AI  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10220  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10220v1.pdf

**Abstract**:
> arXiv:2603.10220v1 Announce Type: cross 
Abstract: Intraoperative Cone Beam Computed Tomography (CBCT) provides a reliable 3D anatomical context essential for interventional planning. However, its static nature fails to provide continuous monitoring of soft-tissue deformations induced by respiration, probe pressure, and surgical manipulation, leading to navigation discrepancies. We propose a deformation-aware CBCT updating framework that leverages robotic ultrasound as a dynamic proxy to infer tissue motion and update static CBCT slices in real time. Starting from calibration-initialized alignment with linear correlation of linear combination (LC2)-based rigid refinement, our method establishes accurate multimodal correspondence. To capture intraoperative dynamics, we introduce the ultraso...

---

## 87. Joint Imaging-ROI Representation Learning via Cross-View Contrastive Alignment for Brain Disorder Classification

**Authors**: Wei Liang, Lifang He  
**Categories**: cs.AI  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10253  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10253v1.pdf

**Abstract**:
> arXiv:2603.10253v1 Announce Type: cross 
Abstract: Brain imaging classification is commonly approached from two perspectives: modeling the full image volume to capture global anatomical context, or constructing ROI-based graphs to encode localized and topological interactions. Although both representations have demonstrated independent efficacy, their relative contributions and potential complementarity remain insufficiently understood. Existing fusion approaches are typically task-specific and do not enable controlled evaluation of each representation under consistent training settings. To address this gap, we propose a unified cross-view contrastive framework for joint imaging-ROI representation learning. Our method learns subject-level global (imaging) and local (ROI-graph) embeddings a...

---

## 88. Mitigating Translationese Bias in Multilingual LLM-as-a-Judge via Disentangled Information Bottleneck

**Authors**: Hongbin Zhang, Kehai Chen, Xuefen Bai, Youcheng Pan, Yang Xiang, Jinpeng Wang, Min Zhang  
**Categories**: cs.AI  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10351  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10351v1.pdf

**Abstract**:
> arXiv:2603.10351v1 Announce Type: cross 
Abstract: Large language models (LLMs) have become a standard for multilingual evaluation, yet they exhibit a severe systematic translationese bias. In this paper, translationese bias is characterized as LLMs systematically favoring machine-translated text over human-authored references, particularly in low-resource languages. We attribute this bias to spurious correlations with (i) latent manifold alignment with English and (ii) cross-lingual predictability. To mitigate this bias, we propose DIBJudge, a robust fine-tuning framework that learns a minimally sufficient, judgment-critical representation via variational information compression, while explicitly isolating spurious factors into the dedicated bias branch. Furthermore, we incorporate a cros...

---

## 89. Utility Function is All You Need: LLM-based Congestion Control

**Authors**: Neta Rozen-Schiff, Liron Schiff, Stefan Schmid  
**Categories**: cs.AI  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10357  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10357v1.pdf

**Abstract**:
> arXiv:2603.10357v1 Announce Type: cross 
Abstract: Congestion is a critical and challenging problem in communication networks. Congestion control protocols allow network applications to tune their sending rate in a way that optimizes their performance and the network utilization. In the common distributed setting, the applications cannot collaborate with each other directly but instead obtain similar estimations about the state of the network using latency and loss measurements. These measurements can be fed into analytical functions, referred to by utility functions, whose gradients help each and all distributed senders to converge to a desired state.
  The above process becomes extremely complicated when each application has different optimization goals and requirements. Crafting these u...

---

## 90. Beyond Interleaving: Causal Attention Reformulations for Generative Recommender Systems

**Authors**: Hailing Cheng  
**Categories**: cs.AI  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10369  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10369v1.pdf

**Abstract**:
> arXiv:2603.10369v1 Announce Type: cross 
Abstract: Generative Recommender Systems (GR) increasingly model user behavior as a sequence generation task by interleaving item and action tokens. While effective, this formulation introduces significant structural and computational inefficiencies: it doubles sequence length, incurs quadratic overhead, and relies on implicit attention to recover the causal relationship between an item and its associated action. Furthermore, interleaving heterogeneous tokens forces the Transformer to disentangle semantically incompatible signals, leading to increased attention noise and reduced representation efficiency.In this work, we propose a principled reformulation of generative recommendation that aligns sequence modeling with underlying causal structures an...

---

## 91. Enhancing Network Intrusion Detection Systems: A Multi-Layer Ensemble Approach to Mitigate Adversarial Attacks

**Authors**: Nasim Soltani, Shayan Nejadshamsi, Zakaria Abou El Houda, Raphael Khoury, Kelton A. P. Costa, Tiago ...  
**Categories**: cs.AI  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10413  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10413v1.pdf

**Abstract**:
> arXiv:2603.10413v1 Announce Type: cross 
Abstract: Adversarial examples can represent a serious threat to machine learning (ML) algorithms. If used to manipulate the behaviour of ML-based Network Intrusion Detection Systems (NIDS), they can jeopardize network security. In this work, we aim to mitigate such risks by increasing the robustness of NIDS towards adversarial attacks. To that end, we explore two adversarial methods for generating malicious network traffic. The first method is based on Generative Adversarial Networks (GAN) and the second one is the Fast Gradient Sign Method (FGSM). The adversarial examples generated by these methods are then used to evaluate a novel multilayer defense mechanism, specifically designed to mitigate the vulnerability of ML-based NIDS. Our solution cons...

---

## 92. Towards Cognitive Defect Analysis in Active Infrared Thermography with Vision-Text Cues

**Authors**: Mohammed Salah, Eman Ouda, Giuseppe Dell'Avvocato, Fabrizio Sarasini, Ester D'Accardi, Jorge Dias, D...  
**Categories**: cs.AI  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10549  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10549v1.pdf

**Abstract**:
> arXiv:2603.10549v1 Announce Type: cross 
Abstract: Active infrared thermography (AIRT) is currently witnessing a surge of artificial intelligence (AI) methodologies being deployed for automated subsurface defect analysis of high performance carbon fiber-reinforced polymers (CFRP). Deploying AI-based AIRT methodologies for inspecting CFRPs requires the creation of time consuming and expensive datasets of CFRP inspection sequences to train neural networks. To address this challenge, this work introduces a novel language-guided framework for cognitive defect analysis in CFRPs using AIRT and vision-language models (VLMs). Unlike conventional learning-based approaches, the proposed framework does not require developing training datasets for extensive training of defect detectors, instead it rel...

---

## 93. Recover to Predict: Progressive Retrospective Learning for Variable-Length Trajectory Prediction

**Authors**: Hao Zhou, Lu Qi, Jason Li, Jie Zhang, Yi Liu, Xu Yang, Mingyu Fan, Fei Luo  
**Categories**: cs.AI  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10597  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10597v1.pdf

**Abstract**:
> arXiv:2603.10597v1 Announce Type: cross 
Abstract: Trajectory prediction is critical for autonomous driving, enabling safe and efficient planning in dense, dynamic traffic. Most existing methods optimize prediction accuracy under fixed-length observations. However, real-world driving often yields variable-length, incomplete observations, posing a challenge to these methods. A common strategy is to directly map features from incomplete observations to those from complete ones. This one-shot mapping, however, struggles to learn accurate representations for short trajectories due to significant information gaps. To address this issue, we propose a Progressive Retrospective Framework (PRF), which gradually aligns features from incomplete observations with those from complete ones via a cascade...

---

## 94. A Platform-Agnostic Multimodal Digital Human Modelling Framework: Neurophysiological Sensing in Game-Based Interaction

**Authors**: Daniel J. Buxton, Mufti Mahmud, Jordan J. Bird, Thomas Hughes-Roberts, David J. Brown  
**Categories**: cs.AI  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10680  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10680v1.pdf

**Abstract**:
> arXiv:2603.10680v1 Announce Type: cross 
Abstract: Digital Human Modelling (DHM) is increasingly shaped by advances in AI, wearable biosensing, and interactive digital environments, particularly in research addressing accessibility and inclusion. However, many AI-enabled DHM approaches remain tightly coupled to specific platforms, tasks, or interpretative pipelines, limiting reproducibility, scalability, and ethical reuse. This paper presents a platform-agnostic DHM framework designed to support AI-ready multimodal interaction research by explicitly separating sensing, interaction modelling, and inference readiness. The framework integrates the OpenBCI Galea headset as a unified multimodal sensing layer, providing concurrent EEG, EMG, EOG, PPG, and inertial data streams, alongside a reprod...

---

## 95. RandMark: On Random Watermarking of Visual Foundation Models

**Authors**: Anna Chistyakova, Mikhail Pautov  
**Categories**: cs.AI  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10695  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10695v1.pdf

**Abstract**:
> arXiv:2603.10695v1 Announce Type: cross 
Abstract: Being trained on large and diverse datasets, visual foundation models (VFMs) can be fine-tuned to achieve remarkable performance and efficiency in various downstream computer vision tasks. The high computational cost of data collection and training makes these models valuable assets, which motivates some VFM owners to distribute them alongside a license to protect their intellectual property rights. In this paper, we propose an approach to ownership verification of visual foundation models that leverages a small encoder-decoder network to embed digital watermarks into an internal representation of a hold-out set of input images. The method is based on random watermark embedding, which makes the watermark statistics detectable in functional...

---

## 96. Structured Linked Data as a Memory Layer for Agent-Orchestrated Retrieval

**Authors**: Andrea Volpini, Elie Raad, Beatrice Gamba, David Riccitelli  
**Categories**: cs.AI  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10700  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10700v1.pdf

**Abstract**:
> arXiv:2603.10700v1 Announce Type: cross 
Abstract: Retrieval-Augmented Generation (RAG) systems typically treat documents as flat text, ignoring the structured metadata and linked relationships that knowledge graphs provide. In this paper, we investigate whether structured linked data, specifically Schema.org markup and dereferenceable entity pages served by a Linked Data Platform, can improve retrieval accuracy and answer quality in both standard and agentic RAG systems. We conduct a controlled experiment across four domains (editorial, legal, travel, e-commerce) using Vertex AI Vector Search 2.0 for retrieval and the Google Agent Development Kit (ADK) for agentic reasoning. Our experimental design tests seven conditions: three document representations (plain HTML, HTML with JSON-LD, and ...

---

## 97. UAV traffic scene understanding: A cross-spectral guided approach and a unified benchmark

**Authors**: Yu Zhang, Zhicheng Zhao, Ze Luo, Chenglong Li, Jin Tang  
**Categories**: cs.AI  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10722  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10722v1.pdf

**Abstract**:
> arXiv:2603.10722v1 Announce Type: cross 
Abstract: Traffic scene understanding from unmanned aerial vehicle (UAV) platforms is crucial for intelligent transportation systems due to its flexible deployment and wide-area monitoring capabilities. However, existing methods face significant challenges in real-world surveillance, as their heavy reliance on optical imagery leads to severe performance degradation under adverse illumination conditions like nighttime and fog. Furthermore, current Visual Question Answering (VQA) models are restricted to elementary perception tasks, lacking the domain-specific regulatory knowledge required to assess complex traffic behaviors. To address these limitations, we propose a novel Cross-spectral Traffic Cognition Network (CTCNet) for robust UAV traffic scene...

---

## 98. GRACE: A Unified 2D Multi-Robot Path Planning Simulator & Benchmark for Grid, Roadmap, And Continuous Environments

**Authors**: Chuanlong Zang, Anna Mannucci, Isabelle Barz, Philipp Schillinger, Florian Lier, Wolfgang H\"onig  
**Categories**: cs.AI  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10858  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10858v1.pdf

**Abstract**:
> arXiv:2603.10858v1 Announce Type: cross 
Abstract: Advancing Multi-Agent Pathfinding (MAPF) and Multi-Robot Motion Planning (MRMP) requires platforms that enable transparent, reproducible comparisons across modeling choices. Existing tools either scale under simplifying assumptions (grids, homogeneous agents) or offer higher fidelity with less comparable instrumentation. We present GRACE, a unified 2D simulator+benchmark that instantiates the same task at multiple abstraction levels (grid, roadmap, continuous) via explicit, reproducible operators and a common evaluation protocol. Our empirical results on public maps and representative planners enable commensurate comparisons on a shared instance set. Furthermore, we quantify the expected representation-fidelity trade-offs (MRMP solves inst...

---

## 99. Contact Coverage-Guided Exploration for General-Purpose Dexterous Manipulation

**Authors**: Zixuan Liu, Ruoyi Qiao, Chenrui Tie, Xuanwei Liu, Yunfan Lou, Chongkai Gao, Zhixuan Xu, Lin Shao  
**Categories**: cs.AI  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.10971  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.10971v1.pdf

**Abstract**:
> arXiv:2603.10971v1 Announce Type: cross 
Abstract: Deep Reinforcement learning (DRL) has achieved remarkable success in domains with well-defined reward structures, such as Atari games and locomotion. In contrast, dexterous manipulation lacks general-purpose reward formulations and typically depends on task-specific, handcrafted priors to guide hand-object interactions. We propose Contact Coverage-Guided Exploration (CCGE), a general exploration method designed for general-purpose dexterous manipulation tasks. CCGE represents contact state as the intersection between object surface points and predefined hand keypoints, encouraging dexterous hands to discover diverse and novel contact patterns, namely which fingers contact which object regions. It maintains a contact counter conditioned on ...

---

## 100. Instruction set for the representation of graphs

**Authors**: Ezequiel Lopez-Rubio, Mario Pascual-Gonzalez  
**Categories**: cs.AI  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11039  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11039v1.pdf

**Abstract**:
> arXiv:2603.11039v1 Announce Type: cross 
Abstract: We present IsalGraph, a method for representing the structure of any finite, simple graph as a compact string over a nine-character instruction alphabet. The encoding is executed by a small virtual machine comprising a sparse graph, a circular doubly-linked list (CDLL) of graph-node references, and two traversal pointers. Instructions either move a pointer through the CDLL or insert a node or edge into the graph. A key design property is that every string over the alphabet decodes to a valid graph, with no invalid states reachable. A greedy \emph{GraphToString} algorithm encodes any connected graph into a string in time polynomial in the number of nodes; an exhaustive-backtracking variant produces a canonical string by selecting the lexico...

---

## 101. LiTo: Surface Light Field Tokenization

**Authors**: Jen-Hao Rick Chang, Xiaoming Zhao, Dorian Chan, Oncel Tuzel  
**Categories**: cs.AI  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.11047  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.11047v1.pdf

**Abstract**:
> arXiv:2603.11047v1 Announce Type: cross 
Abstract: We propose a 3D latent representation that jointly models object geometry and view-dependent appearance. Most prior works focus on either reconstructing 3D geometry or predicting view-independent diffuse appearance, and thus struggle to capture realistic view-dependent effects. Our approach leverages that RGB-depth images provide samples of a surface light field. By encoding random subsamples of this surface light field into a compact set of latent vectors, our model learns to represent both geometry and appearance within a unified 3D latent space. This representation reproduces view-dependent effects such as specular highlights and Fresnel reflections under complex lighting. We further train a latent flow matching model on this representa...

---

## 102. What We Don't C: Manifold Disentanglement for Structured Discovery

**Authors**: Brian Rogers, Micah Bowles, Chris J. Lintott, Steve Croft, Oliver N. F. King, James Kostas Ray  
**Categories**: cs.AI  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2511.09433  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2511.09433v2.pdf

**Abstract**:
> arXiv:2511.09433v2 Announce Type: replace 
Abstract: Accessing information in learned representations is critical for annotation, discovery, and data filtering in disciplines where high-dimensional datasets are common. We introduce What We Don't C, a novel approach based on latent flow matching that disentangles latent subspaces by explicitly removing information included in conditional guidance, resulting in meaningful residual representations. This allows factors of variation which have not already been captured in conditioning to become more readily available. We show how guidance in the flow path necessarily represses the information from the guiding, conditioning variables. Our results highlight this approach as a simple yet powerful mechanism for analyzing, controlling, and repurposi...

---

## 103. Curveball Steering: The Right Direction To Steer Isn't Always Linear

**Authors**: Shivam Raval, Hae Jin Song, Linlin Wu, Abir Harrasse, Jeff M. Phillips, Amirali Abdullah  
**Categories**: cs.AI  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.09313  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.09313v2.pdf

**Abstract**:
> arXiv:2603.09313v2 Announce Type: replace 
Abstract: Activation steering is a widely used approach for controlling large language model (LLM) behavior by intervening on internal representations. Existing methods largely rely on the Linear Representation Hypothesis, assuming behavioral attributes can be manipulated using global linear directions. In practice, however, such linear interventions often behave inconsistently. We question this assumption by analyzing the intrinsic geometry of LLM activation spaces. Measuring geometric distortion via the ratio of geodesic to Euclidean distances, we observe substantial and concept-dependent distortions, indicating that activation spaces are not well-approximated by a globally linear geometry. Motivated by this, we propose "Curveball steering", a n...

---

## 104. Explainability of Text Processing and Retrieval Methods: A Survey

**Authors**: Sourav Saha, Debapriyo Majumdar, Mandar Mitra  
**Categories**: cs.AI  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2212.07126  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2212.07126v3.pdf

**Abstract**:
> arXiv:2212.07126v3 Announce Type: replace-cross 
Abstract: Deep Learning and Machine Learning based models have become extremely popular in text processing and information retrieval. However, the non-linear structures present inside the networks make these models largely inscrutable. A significant body of research has focused on increasing the transparency of these models. This article provides a broad overview of research on the explainability and interpretability of natural language processing and information retrieval methods. More specifically, we survey approaches that have been applied to explain word embeddings, sequence modeling, attention modules, transformers, BERT, and document ranking. The concluding section suggests some possible directions for future research on this topic.

---

## 105. Large Language Model Psychometrics: A Systematic Review of Evaluation, Validation, and Enhancement

**Authors**: Haoran Ye, Jing Jin, Yuhang Xie, Xin Zhang, Guojie Song  
**Categories**: cs.AI  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2505.08245  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2505.08245v3.pdf

**Abstract**:
> arXiv:2505.08245v3 Announce Type: replace-cross 
Abstract: The advancement of large language models (LLMs) has outpaced traditional evaluation methodologies. This progress presents novel challenges, such as measuring human-like psychological constructs, moving beyond static and task-specific benchmarks, and establishing human-centered evaluation. These challenges intersect with psychometrics, the science of quantifying the intangible aspects of human psychology, such as personality, values, and intelligence. This review paper introduces and synthesizes the emerging interdisciplinary field of LLM Psychometrics, which leverages psychometric instruments, theories, and principles to evaluate, understand, and enhance LLMs. The reviewed literature systematically shapes benchmarking principles, b...

---

## 106. Training with Pseudo-Code for Instruction Following

**Authors**: Prince Kumar, Rudra Murthy, Riyaz Bhat, Danish Contractor  
**Categories**: cs.AI  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2505.18011  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2505.18011v2.pdf

**Abstract**:
> arXiv:2505.18011v2 Announce Type: replace-cross 
Abstract: Despite rapid advances in the capabilities of Large Language Models (LLMs), they continue to struggle with following relatively simple and unambiguous instructions, particularly when compositional structure is involved. Recent work suggests that models may follow instructions more effectively when they are expressed in pseudo-code rather than natural language. However, writing pseudo-code programs can be tedious, and relying on few-shot demonstrations or inference-time code prompting is often unnatural for non-expert users of LLMs. To overcome these limitations, we propose a training time approach that fine-tunes LLMs using instruction-tuning data augmented with pseudo-code representations of natural language instructions paired wi...

---

## 107. What Makes Code Generation Ethically Sourced?

**Authors**: Zhuolin Xu, Chenglin Li, Qiushi Li, Shin Hwei Tan  
**Categories**: cs.AI  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2507.19743  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2507.19743v2.pdf

**Abstract**:
> arXiv:2507.19743v2 Announce Type: replace-cross 
Abstract: Several code generation models have been proposed to help reduce time and effort in solving software-related tasks. To ensure responsible AI, there are growing interests over various ethical issues (e.g., unclear licensing, privacy, fairness, and environment impact). These studies have the overarching goal of ensuring ethically sourced generation, which has gained growing attentions in speech synthesis and image generation. In this paper, we introduce the novel notion of Ethically Sourced Code Generation (ES-CodeGen) to refer to managing all processes involved in code generation model development from data collection to post-deployment via ethical and sustainable practices. To build a taxonomy of ES-CodeGen, we perform a two-phase ...

---

## 108. MVCustom: Multi-View Customized Diffusion via Geometric Latent Rendering and Completion

**Authors**: Minjung Shin, Hyunin Cho, Sooyeon Go, Jin-Hwa Kim, Youngjung Uh  
**Categories**: cs.AI  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.13702  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.13702v2.pdf

**Abstract**:
> arXiv:2510.13702v2 Announce Type: replace-cross 
Abstract: Multi-view generation with camera pose control and prompt-based customization are both essential elements for achieving controllable generative models. However, existing multi-view generation models do not support customization with geometric consistency, whereas customization models lack explicit viewpoint control, making them challenging to unify. Motivated by these gaps, we introduce a novel task, multi-view customization, which aims to jointly achieve multi-view camera pose control and customization. Due to the scarcity of training data in customization, existing multi-view generation models, which inherently rely on large-scale datasets, struggle to generalize to diverse prompts. To address this, we propose MVCustom, a novel d...

---

## 109. D-GAP: Improving Out-of-Domain Robustness via Dataset-Agnostic and Gradient-Guided Augmentation in Frequency and Pixel Spaces

**Authors**: Ruoqi Wang, Haitao Wang, Shaojie Guo, Qiong Luo  
**Categories**: cs.AI  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2511.11286  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2511.11286v2.pdf

**Abstract**:
> arXiv:2511.11286v2 Announce Type: replace-cross 
Abstract: Out-of-domain (OOD) robustness is challenging to achieve in real-world computer vision applications, where shifts in image background, style, and acquisition instruments always degrade model performance. Generic augmentations show inconsistent gains under such shifts, whereas dataset-specific augmentations require expert knowledge and prior analysis. Moreover, prior studies show that neural networks adapt poorly to domain shifts because they exhibit a learning bias to domain-specific frequency components. Perturbing frequency values can mitigate such bias but overlooks pixel-level details, leading to suboptimal performance. To address these problems, we propose D-GAP, a Dataset-agnostic and Gradient-guided augmentation method for t...

---

## 110. Enhancing Tree Species Classification: Insights from YOLOv8 and Explainable AI Applied to TLS Point Cloud Projections

**Authors**: Adrian Straker, Paul Magdon, Marco Zullich, Maximilian Freudenberg, Christoph Kleinn, Johannes Breid...  
**Categories**: cs.AI  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2512.16950  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2512.16950v2.pdf

**Abstract**:
> arXiv:2512.16950v2 Announce Type: replace-cross 
Abstract: Aiming to advance research in the field of interpretability of deep learning models for tree species classification using TLS 3D point clouds we present insights in the classification abilities of YOLOv8 through a new framework which enables systematic analysis of saliency maps derived from CAM (Class Activation Mapping). To investigate the contribution of structural tree features to the classification decisions of the models, we link regions with high saliency derived from the application of Finer-CAM to segments of 2D side-view images that correspond to structural tree features. Using TLS 3D point clouds from 2445 trees across seven European tree species, we trained five YOLOv8 models with cross-validation, reaching a mean accura...

---

## 111. UniWeTok: An Unified Binary Tokenizer with Codebook Size $\mathit{2^{128}}$ for Unified Multimodal Large Language Model

**Authors**: Shaobin Zhuang, Yuang Ai, Jiaming Han, Weijia Mao, Xiaohui Li, Fangyikang Wang, Xiao Wang, Yan Li, S...  
**Categories**: cs.AI  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2602.14178  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2602.14178v3.pdf

**Abstract**:
> arXiv:2602.14178v3 Announce Type: replace-cross 
Abstract: Unified Multimodal Large Language Models (MLLMs) require a visual representation that simultaneously supports high-fidelity reconstruction, complex semantic extraction, and generative suitability. However, existing visual tokenizers typically struggle to satisfy these conflicting objectives within a single framework. In this paper, we introduce UniWeTok, a unified discrete tokenizer designed to bridge this gap using a massive binary codebook ($\mathit{2^{128}}$). For training framework, we introduce Pre-Post Distillation and a Generative-Aware Prior to enhance the semantic extraction and generative prior of the discrete tokens. In terms of model architecture, we propose a convolution-attention hybrid architecture with the SigLu act...

---

## 112. SeDa: A Unified System for Dataset Discovery and Multi-Entity Augmented Semantic Exploration

**Authors**: Kan Ling, Zhen Qin, Yichi Zhu, Hengrun Zhang, Huiqun Yu, Guisheng Fan  
**Categories**: cs.AI  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.07502  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.07502v2.pdf

**Abstract**:
> arXiv:2603.07502v2 Announce Type: replace-cross 
Abstract: The continuous expansion of open data platforms and research repositories has led to a fragmented dataset ecosystem, posing significant challenges for cross-source data discovery and interpretation. To address these challenges, we introduce SeDa--a unified framework for dataset discovery, semantic annotation, and multi-entity augmented navigation. SeDa integrates more than 7.6 million datasets from over 200 platforms, spanning governmental, academic, and industrial domains. The framework first performs semantic extraction and standardization to harmonize heterogeneous metadata representations. On this basis, a topic-tagging mechanism constructs an extensible tag graph that supports thematic retrieval and cross-domain association, w...

---

## 113. AutoViVQA: A Large-Scale Automatically Constructed Dataset for Vietnamese Visual Question Answering

**Authors**: Nguyen Anh Tuong, Phan Ba Duc, Nguyen Trung Quoc, Tran Dac Thinh, Dang Duy Lan, Nguyen Quoc Thinh, T...  
**Categories**: cs.AI  
**Published**: Thu, 12 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.09689  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.09689v2.pdf

**Abstract**:
> arXiv:2603.09689v2 Announce Type: replace-cross 
Abstract: Visual Question Answering (VQA) is a fundamental multimodal task that requires models to jointly understand visual and textual information. Early VQA systems relied heavily on language biases, motivating subsequent work to emphasize visual grounding and balanced datasets. With the success of large-scale pre-trained transformers for both text and vision domains -- such as PhoBERT for Vietnamese language understanding and Vision Transformers (ViT) for image representation learning -- multimodal fusion has achieved remarkable progress.
  For Vietnamese VQA, several datasets have been introduced to promote research in low-resource multimodal learning, including ViVQA, OpenViVQA, and the recently proposed ViTextVQA. These resources enab...

---

