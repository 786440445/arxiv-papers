# arXiv Papers - 2026-02-11

**论文数量**: 13

## 1. C^2ROPE: Causal Continuous Rotary Positional Encoding for 3D Large Multimodal-Models Reasoning

**Authors**: Ka-Veng Yuen...
**Categories**: cs.CV, cs.AI
**Published**: 2026-02-11T05:50:17Z
**Link**: https://arxiv.org/abs/2602.10551v2
**PDF**: https://arxiv.org/pdf/2602.10551v2.pdf

**Abstract**:
> Recent advances in 3D Large Multimodal Models (LMMs) built on Large Language Models (LLMs) have established the alignment of 3D visual features with LLM representations as the dominant paradigm. However, the inherited Rotary Position Embedding (RoPE) introduces limitations for multimodal processing. Specifically, applying 1D temporal positional indices disrupts the continuity of visual features along the column dimension, resulting in spatial locality loss. Moreover, RoPE follows the prior that temporally closer image tokens are more causally related, leading to long-term decay in attention allocation and causing the model to progressively neglect earlier visual tokens as the sequence length increases. To address these issues, we propose C^2RoPE, an improved RoPE that explicitly models loc...

---

## 2. How Many Features Can a Language Model Store Under the Linear Representation Hypothesis?

**Authors**: Kenny Peng...
**Categories**: cs.LG, cs.AI, cs.CL, cs.IT, math.CO
**Published**: 2026-02-11T17:49:32Z
**Link**: https://arxiv.org/abs/2602.11246v1
**PDF**: https://arxiv.org/pdf/2602.11246v1.pdf

**Abstract**:
> We introduce a mathematical framework for the linear representation hypothesis (LRH), which asserts that intermediate layers of language models store features linearly. We separate the hypothesis into two claims: linear representation (features are linearly embedded in neuron activations) and linear accessibility (features can be linearly decoded). We then ask: How many neurons $d$ suffice to both linearly represent and linearly access $m$ features? Classical results in compressed sensing imply that for $k$-sparse inputs, $d = O(k\log (m/k))$ suffices if we allow non-linear decoding algorithms (Candes and Tao, 2006; Candes et al., 2006; Donoho, 2006). However, the additional requirement of linear decoding takes the problem out of the classical compressed sensing, into linear compressed sen...

---

## 3. Beyond Musical Descriptors: Extracting Preference-Bearing Intent in Music Queries

**Authors**: Elena V. Epure...
**Categories**: cs.SD, cs.CL, cs.IR, cs.LG, eess.AS
**Published**: 2026-02-11T10:52:38Z
**Link**: https://arxiv.org/abs/2602.12301v1
**PDF**: https://arxiv.org/pdf/2602.12301v1.pdf

**Abstract**:
> Although annotated music descriptor datasets for user queries are increasingly common, few consider the user's intent behind these descriptors, which is essential for effectively meeting their needs. We introduce MusicRecoIntent, a manually annotated corpus of 2,291 Reddit music requests, labeling musical descriptors across seven categories with positive, negative, or referential preference-bearing roles. We then investigate how reliably large language models (LLMs) can extract these music descriptors, finding that they do capture explicit descriptors but struggle with context-dependent ones. This work can further serve as a benchmark for fine-grained modeling of user intent and for gaining insights into improving LLM-based music understanding systems.

---

## 4. HiFloat4 Format for Language Model Inference

**Authors**: Heng Liao...
**Categories**: cs.LG, cs.AI, cs.AR
**Published**: 2026-02-11T19:07:36Z
**Link**: https://arxiv.org/abs/2602.11287v2
**PDF**: https://arxiv.org/pdf/2602.11287v2.pdf

**Abstract**:
> This paper introduces HiFloat4 (HiF4), a block floating-point data format tailored for deep learning. Each HiF4 unit packs 64 4-bit elements with 32 bits of shared scaling metadata, averaging 4.5 bits per value. The metadata specifies a three-level scaling hierarchy, capturing inter- and intra-group dynamic range while improving the utilization of the representational space. In addition, the large 64-element group size enables matrix multiplications to be executed in a highly fixed-point manner, significantly reducing hardware area and power consumption. To evaluate the proposed format, we conducted inference experiments on several language models, including LLaMA, Qwen, Mistral, DeepSeek-V3.1 and LongCat. Results show that HiF4 achieves higher average accuracy than the state-of-the-art NV...

---

## 5. Eliminating Delocalization Error through Localized Orbital Scaling Correction with Orbital Relaxation from Linear Response

**Authors**: Weitao Yang...
**Categories**: physics.chem-ph
**Published**: 2026-02-11T16:24:34Z
**Link**: https://arxiv.org/abs/2602.11003v1
**PDF**: https://arxiv.org/pdf/2602.11003v1.pdf

**Abstract**:
> Despite the great success Kohn-Sham density functional theory (KS-DFT) has achieved, the delocalization error remains a major challenge for commonly used density functional approximations (DFAs), resulting in systematic errors in ionization energies, electron affinities, band structures, and charge distributions. A recently developed localized orbital scaling correction (LOSC) method, namely linear response LOSC (lrLOSC), addresses these challenges by incorporating a functional correction that includes the screening effect and orbital localization within the LOSC framework. The method has been shown to provide accurate descriptions of bulk systems and core-level binding energies in small molecular systems. In this work, we extend the applicability of lrLOSC to a broader range of molecular ...

---

## 6. RiemannGL: Riemannian Geometry Changes Graph Deep Learning

**Authors**: Philip S. Yu...
**Categories**: cs.LG, cs.AI
**Published**: 2026-02-11T16:10:53Z
**Link**: https://arxiv.org/abs/2602.10982v1
**PDF**: https://arxiv.org/pdf/2602.10982v1.pdf

**Abstract**:
> Graphs are ubiquitous, and learning on graphs has become a cornerstone in artificial intelligence and data mining communities. Unlike pixel grids in images or sequential structures in language, graphs exhibit a typical non-Euclidean structure with complex interactions among the objects. This paper argues that Riemannian geometry provides a principled and necessary foundation for graph representation learning, and that Riemannian graph learning should be viewed as a unifying paradigm rather than a collection of isolated techniques. While recent studies have explored the integration of graph learning and Riemannian geometry, most existing approaches are limited to a narrow class of manifolds, particularly hyperbolic spaces, and often adopt extrinsic manifold formulations. We contend that the...

---

## 7. VFGS-Net: Frequency-Guided State-Space Learning for Topology-Preserving Retinal Vessel Segmentation

**Authors**: Nan Mu...
**Categories**: cs.CV
**Published**: 2026-02-11T16:07:29Z
**Link**: https://arxiv.org/abs/2602.10978v1
**PDF**: https://arxiv.org/pdf/2602.10978v1.pdf

**Abstract**:
> Accurate retinal vessel segmentation is a critical prerequisite for quantitative analysis of retinal images and computer-aided diagnosis of vascular diseases such as diabetic retinopathy. However, the elongated morphology, wide scale variation, and low contrast of retinal vessels pose significant challenges for existing methods, making it difficult to simultaneously preserve fine capillaries and maintain global topological continuity. To address these challenges, we propose the Vessel-aware Frequency-domain and Global Spatial modeling Network (VFGS-Net), an end-to-end segmentation framework that seamlessly integrates frequency-aware feature enhancement, dual-path convolutional representation learning, and bidirectional asymmetric spatial state-space modeling within a unified architecture. ...

---

## 8. Can LLMs Cook Jamaican Couscous? A Study of Cultural Novelty in Recipe Generation

**Authors**: G. Farnadi...
**Categories**: cs.AI
**Published**: 2026-02-11T15:55:22Z
**Link**: https://arxiv.org/abs/2602.10964v1
**PDF**: https://arxiv.org/pdf/2602.10964v1.pdf

**Abstract**:
> Large Language Models (LLMs) are increasingly used to generate and shape cultural content, ranging from narrative writing to artistic production. While these models demonstrate impressive fluency and generative capacity, prior work has shown that they also exhibit systematic cultural biases, raising concerns about stereotyping, homogenization, and the erasure of culturally specific forms of expression. Understanding whether LLMs can meaningfully align with diverse cultures beyond the dominant ones remains a critical challenge. In this paper, we study cultural adaptation in LLMs through the lens of cooking recipes, a domain in which culture, tradition, and creativity are tightly intertwined. We build on the \textit{GlobalFusion} dataset, which pairs human recipes from different countries ac...

---

## 9. Towards Learning a Generalizable 3D Scene Representation from 2D Observations

**Authors**: Stefan Wermter...
**Categories**: cs.CV, cs.RO
**Published**: 2026-02-11T15:22:41Z
**Link**: https://arxiv.org/abs/2602.10943v1
**PDF**: https://arxiv.org/pdf/2602.10943v1.pdf

**Abstract**:
> We introduce a Generalizable Neural Radiance Field approach for predicting 3D workspace occupancy from egocentric robot observations. Unlike prior methods operating in camera-centric coordinates, our model constructs occupancy representations in a global workspace frame, making it directly applicable to robotic manipulation. The model integrates flexible source views and generalizes to unseen object arrangements without scene-specific finetuning. We demonstrate the approach on a humanoid robot and evaluate predicted geometry against 3D sensor ground truth. Trained on 40 real scenes, our model achieves 26mm reconstruction error, including occluded regions, validating its ability to infer complete 3D occupancy beyond traditional stereo vision methods.

---

## 10. Reference Output Tracking in Boolean Control Networks

**Authors**: Maria Elena Valcher...
**Categories**: eess.SY
**Published**: 2026-02-11T13:21:32Z
**Link**: https://arxiv.org/abs/2602.10835v1
**PDF**: https://arxiv.org/pdf/2602.10835v1.pdf

**Abstract**:
> In this paper, the problem of tracking a given reference output trajectory is investigated for the class of Boolean control networks, by resorting to their algebraic representation. First, the case of a finite-length reference trajectory is addressed, and the analysis and algorithm first proposed in [17] are extended to be able to deal with arbitrary initial conditions and to identify all possible solutions. The approach developed for the finite-length case is then adjusted to cope with periodic reference output trajectories. The results of the paper are illustrated through an example.

---

## 11. DMP-3DAD: Cross-Category 3D Anomaly Detection via Realistic Depth Map Projection with Few Normal Samples

**Authors**: Jun Yu...
**Categories**: cs.CV
**Published**: 2026-02-11T12:47:38Z
**Link**: https://arxiv.org/abs/2602.10806v1
**PDF**: https://arxiv.org/pdf/2602.10806v1.pdf

**Abstract**:
> Cross-category anomaly detection for 3D point clouds aims to determine whether an unseen object belongs to a target category using only a few normal examples. Most existing methods rely on category-specific training, which limits their flexibility in few-shot scenarios. In this paper, we propose DMP-3DAD, a training-free framework for cross-category 3D anomaly detection based on multi-view realistic depth map projection. Specifically, by converting point clouds into a fixed set of realistic depth images, our method leverages a frozen CLIP visual encoder to extract multi-view representations and performs anomaly detection via weighted feature similarity, which does not require any fine-tuning or category-dependent adaptation. Extensive experiments on the ShapeNetPart dataset demonstrate tha...

---

## 12. Compute Only Once: UG-Separation for Efficient Large Recommendation Models

**Authors**: Yuchao Zheng...
**Categories**: cs.IR, cs.LG
**Published**: 2026-02-11T02:53:59Z
**Link**: https://arxiv.org/abs/2602.10455v1
**PDF**: https://arxiv.org/pdf/2602.10455v1.pdf

**Abstract**:
> Driven by scaling laws, recommender systems increasingly rely on large-scale models to capture complex feature interactions and user behaviors, but this trend also leads to prohibitive training and inference costs. While long-sequence models(e.g., LONGER) can reuse user-side computation through KV caching, such reuse is difficult in dense feature interaction architectures(e.g., RankMixer), where user and group (candidate item) features are deeply entangled across layers. In this work, we propose User-Group Separation (UG-Sep), a novel framework that enables reusable user-side computation in dense interaction models for the first time. UG-Sep introduces a masking mechanism that explicitly disentangles user-side and item-side information flows within token-mixing layers, ensuring that a subs...

---

## 13. Navigating heterogeneous protein landscapes through geometry-aware smoothing

**Authors**: Dianbo Liu...
**Categories**: cs.CE
**Published**: 2026-02-11T02:07:08Z
**Link**: https://arxiv.org/abs/2602.10422v1
**PDF**: https://arxiv.org/pdf/2602.10422v1.pdf

**Abstract**:
> The evolutionary fitness landscape of biological molecules is extremely sparse and heterogeneous, with functional sequences forming isolated dense ``islands'' within a vast combinatorial space of largely non-functional variants. Protein sequences, in particular, exemplify this structure, yet most generative artificial intelligence models implicitly assume a homogeneous data distribution. We show that this assumption fundamentally breaks down in heterogeneous biological sequence spaces: fixed global noise levels impose a destructive trade-off, either oversmoothing dense functional clusters or fragmenting sparse regions and producing non-functional hallucinations. To address this limitation, we introduce \emph{Density-Dependent Smoothing} (DDS), a geometry-aware generative framework that ada...

---

