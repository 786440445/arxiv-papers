# arXiv Papers - 2026-03-10

**来源**: arXiv (cs.SD, eess.AS, cs.LG, cs.AI)  
**关键词**: speech, audio, music, voice, sound, Mel, representation, self-supervised  
**今日新论文**: 6 篇

---

## 1. Multi-View Based Audio Visual Target Speaker Extraction

**Authors**: Peijun Yang, Zhan Jin, Juan Liu, Ming Li  
**Categories**: eess.AS  
**Published**: Tue, 10 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.07696  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.07696v1.pdf

**Abstract**:
> arXiv:2603.07696v1 Announce Type: new 
Abstract: Audio-Visual Target Speaker Extraction (AVTSE) aims to separate a target speaker's voice from a mixed audio signal using the corresponding visual cues. While most existing AVTSE methods rely exclusively on frontal-view videos, this limitation restricts their robustness in real-world scenarios where non-frontal views are prevalent. Such visual perspectives often contain complementary articulatory information that could enhance speech extraction. In this work, we propose Multi-View Tensor Fusion (MVTF), a novel framework that transforms multi-view learning into single-view performance gains. During the training stage, we leverage synchronized multi-perspective lip videos to learn cross-view correlations through MVTF, where pairwise outer produ...

---

## 2. Quantifying Cross-Lingual Transfer in Paralinguistic Speech Tasks

**Authors**: Pol Buitrago, Oriol Pareras, Federico Costa, Javier Hernando  
**Categories**: eess.AS  
**Published**: Tue, 10 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.08231  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.08231v1.pdf

**Abstract**:
> arXiv:2603.08231v1 Announce Type: new 
Abstract: Paralinguistic speech tasks are often considered relatively language-agnostic, as they rely on extralinguistic acoustic cues rather than lexical content. However, prior studies report performance degradation under cross-lingual conditions, indicating non-negligible language dependence. Still, these studies typically focus on isolated language pairs or task-specific settings, limiting comparability and preventing a systematic assessment of task-level language dependence.
  We introduce the Cross-Lingual Transfer Matrix (CLTM), a systematic method to quantify cross-lingual interactions between pairs of languages within a given task. We apply the CLTM to two paralinguistic tasks, gender identification and speaker verification, using a multiling...

---

## 3. Scaling Self-Supervised Speech Models Uncovers Deep Linguistic Relationships: Evidence from the Pacific Cluster

**Authors**: Minu Kim, Hoirin Kim, David R. Mortensen  
**Categories**: eess.AS  
**Published**: Tue, 10 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2603.07238  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2603.07238v1.pdf

**Abstract**:
> arXiv:2603.07238v1 Announce Type: cross 
Abstract: Similarities between language representations derived from Self-Supervised Speech Models (S3Ms) have been observed to primarily reflect geographic proximity or surface typological similarities driven by recent expansion or contact, potentially missing deeper genealogical signals. We investigate how scaling linguistic coverage of an S3M-based language identification system from 126 to 4,017 languages influences this topology. Our results reveal a non-linear effect: while phylogenetic recovery remains stagnant up to the 1K scale, the 4K model displays a dramatic qualitative shift, resolving both clear lineages and complex, long-term linguistic contact. Notably, our analysis reveals the emergence of a robust macro-cluster in the Pacific (comp...

---

## 4. Measuring Audio's Impact on Correctness: Audio-Contribution-Aware Post-Training of Large Audio Language Models

**Authors**: Haolin He, Xingjian Du, Renhe Sun, Zheqi Dai, Yujia Xiao, Mingru Yang, Jiayi Zhou, Xiquan Li, Zhengx...  
**Categories**: eess.AS  
**Published**: Tue, 10 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2509.21060  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2509.21060v4.pdf

**Abstract**:
> arXiv:2509.21060v4 Announce Type: replace 
Abstract: Large Audio Language Models (LALMs) represent an important frontier in multimodal AI, addressing diverse audio tasks. Recently, post-training of LALMs has received increasing attention due to significant performance improvements over foundation models. While single-stage post-training such as reinforcement learning (RL) has demonstrated promising results, multi-stage approaches such as supervised fine-tuning (SFT) followed by RL remain suboptimal. The allocation of data across multiple training stages to maximize LALM capabilities has not been fully explored, and large-scale, high-quality datasets for such research are also lacking. To address these problems, we firstly present AudioMCQ, a comprehensive audio multiple-choice question dat...

---

## 5. Spatially-Augmented Sequence-to-Sequence Neural Diarization for Meetings

**Authors**: Li Li, Ming Cheng, Juan Liu, Ming Li  
**Categories**: eess.AS  
**Published**: Tue, 10 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2510.09505  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2510.09505v2.pdf

**Abstract**:
> arXiv:2510.09505v2 Announce Type: replace 
Abstract: This paper proposes a Spatially-Augmented Sequence-to-Sequence Neural Diarization (SA-S2SND) framework, which integrates direction-of-arrival (DOA) cues estimated by SRP-DNN into the S2SND backbone. A two-stage training strategy is adopted: the model is first trained with single-channel audio and DOA features, and then further optimized with multi-channel inputs under DOA guidance. In addition, a simulated DOA generation scheme is introduced to alleviate dependence on matched multi-channel corpora. On the AliMeeting dataset, SA-S2SND consistently outperform the S2SND baseline, achieving a 7.4% relative DER reduction in the offline mode and over 19% improvement when combined with channel attention. These results demonstrate that spatial c...

---

## 6. Flow2GAN: Hybrid Flow Matching and GAN with Multi-Resolution Network for Few-step High-Fidelity Audio Generation

**Authors**: Zengwei Yao, Wei Kang, Han Zhu, Liyong Guo, Lingxuan Ye, Fangjun Kuang, Weiji Zhuang, Zhaoqing Li, Z...  
**Categories**: eess.AS  
**Published**: Tue, 10 Mar 2026 00:00:00 -0400  
**Link**: https://arxiv.org/abs/2512.23278  
**PDF**: https://arxiv.org/pdf/oai:arXiv.org:2512.23278v2.pdf

**Abstract**:
> arXiv:2512.23278v2 Announce Type: replace 
Abstract: Existing dominant methods for audio generation include Generative Adversarial Networks (GANs) and diffusion-based methods like Flow Matching. GANs suffer from slow convergence during training, while diffusion methods require multi-step inference that introduces considerable computational overhead. In this work, we introduce Flow2GAN, a two-stage framework that combines Flow Matching training for learning generative capabilities with GAN fine-tuning for efficient few-step inference. Specifically, given audio's unique properties, we first improve Flow Matching for audio modeling through: 1) reformulating the objective as endpoint estimation, avoiding velocity estimation difficulties when involving empty regions; 2) applying spectral energy...

---

