# arXiv Papers - 2026-02-02

**论文数量**: 12

## 1. Fat-Cat: Document-Driven Metacognitive Multi-Agent System for Complex Reasoning

**Authors**: Aming Wu...
**Categories**: cs.LG
**Published**: 2026-02-02T15:12:13Z
**Link**: https://arxiv.org/abs/2602.02206v2
**PDF**: https://arxiv.org/pdf/2602.02206v2.pdf

**Abstract**:
> The effectiveness of LLM-based agents is often limited not by model capacity alone, but by how efficiently contextual information is utilized at runtime. Existing agent frameworks rely on rigid, syntax-heavy state representations such as nested JSON, which require models to devote a substantial portion of their limited attention to syntactic processing rather than semantic reasoning. In this paper, we propose Fat-Cat, a document-driven agent architecture that improves the signal-to-noise ratio of state management. By integrating three key components: (1) a Semantic File System that represents agent state as Markdown documents aligned with common pre-training corpora, (2) a Textual Strategy Evolution module that accumulates task-solving knowledge without parameter updates, and (3) a Closed-...

---

## 2. Notes on the Reward Representation of Posterior Updates

**Authors**: Pedro A. Ortega...
**Categories**: cs.LG, cs.AI, stat.ML
**Published**: 2026-02-02T23:37:39Z
**Link**: https://arxiv.org/abs/2602.02912v1
**PDF**: https://arxiv.org/pdf/2602.02912v1.pdf

**Abstract**:
> Many ideas in modern control and reinforcement learning treat decision-making as inference: start from a baseline distribution and update it when a signal arrives. We ask when this can be made literal rather than metaphorical. We study the special case where a KL-regularized soft update is exactly a Bayesian posterior inside a single fixed probabilistic model, so the update variable is a genuine channel through which information is transmitted. In this regime, behavioral change is driven only by evidence carried by that channel: the update must be explainable as an evidence reweighing of the baseline. This yields a sharp identification result: posterior updates determine the relative, context-dependent incentive signal that shifts behavior, but they do not uniquely determine absolute rewar...

---

## 3. HALT: Hallucination Assessment via Log-probs as Time series

**Authors**: Ashok Goel...
**Categories**: cs.CL, cs.AI
**Published**: 2026-02-02T22:46:23Z
**Link**: https://arxiv.org/abs/2602.02888v1
**PDF**: https://arxiv.org/pdf/2602.02888v1.pdf

**Abstract**:
> Hallucinations remain a major obstacle for large language models (LLMs), especially in safety-critical domains. We present HALT (Hallucination Assessment via Log-probs as Time series), a lightweight hallucination detector that leverages only the top-20 token log-probabilities from LLM generations as a time series. HALT uses a gated recurrent unit model combined with entropy-based features to learn model calibration bias, providing an extremely efficient alternative to large encoders. Unlike white-box approaches, HALT does not require access to hidden states or attention maps, relying only on output log-probabilities. Unlike black-box approaches, it operates on log-probs rather than surface-form text, which enables stronger domain generalization and compatibility with proprietary LLMs witho...

---

## 4. Chain of Simulation: A Dual-Mode Reasoning Framework for Large Language Models with Dynamic Problem Routing

**Authors**: Saeid Sheikhi...
**Categories**: cs.AI, cs.CL, cs.LG
**Published**: 2026-02-02T21:44:01Z
**Link**: https://arxiv.org/abs/2602.02842v1
**PDF**: https://arxiv.org/pdf/2602.02842v1.pdf

**Abstract**:
> We present Chain of Simulation (CoS), a novel dual-mode reasoning framework that dynamically routes problems to specialized reasoning strategies in Large Language Models (LLMs). Unlike existing uniform prompting approaches, CoS employs three distinct reasoning modes: (1) computational flow with self-consistency for mathematical problems, (2) symbolic state tracking with JSON representations for spatial reasoning, and (3) hybrid fact-extraction for multi-hop inference. Through comprehensive evaluation on GSM8K, StrategyQA, and bAbI benchmarks using four state-of-the-art models (Gemma-3 27B, LLaMA-3.1 8B, Mistral 7B, and Qwen-2.5 14B), we demonstrate that CoS achieves 71.5% accuracy on GSM8K (1.0% absolute improvement), 90.0% on StrategyQA (2.5% improvement), and 19.0% on bAbI (65.2% relativ...

---

## 5. Beyond Content: Behavioral Policies Reveal Actors in Information Operations

**Authors**: Marian-Andrei Rizoiu...
**Categories**: cs.SI, cs.LG
**Published**: 2026-02-02T21:39:21Z
**Link**: https://arxiv.org/abs/2602.02838v1
**PDF**: https://arxiv.org/pdf/2602.02838v1.pdf

**Abstract**:
> The detection of online influence operations -- coordinated campaigns by malicious actors to spread narratives -- has traditionally depended on content analysis or network features. These approaches are increasingly brittle as generative models produce convincing text, platforms restrict access to behavioral data, and actors migrate to less-regulated spaces. We introduce a platform-agnostic framework that identifies malicious actors from their behavioral policies by modeling user activity as sequential decision processes. We apply this approach to 12,064 Reddit users, including 99 accounts linked to the Russian Internet Research Agency in Reddit's 2017 transparency report, analyzing over 38 million activity steps from 2015-2018. Activity-based representations, which model how users act rat...

---

## 6. Simulating Human Audiovisual Search Behavior

**Authors**: Antti Oulasvirta...
**Categories**: cs.HC, cs.AI, cs.RO
**Published**: 2026-02-02T20:47:05Z
**Link**: https://arxiv.org/abs/2602.02790v1
**PDF**: https://arxiv.org/pdf/2602.02790v1.pdf

**Abstract**:
> Locating a target based on auditory and visual cues$\unicode{x2013}$such as finding a car in a crowded parking lot or identifying a speaker in a virtual meeting$\unicode{x2013}$requires balancing effort, time, and accuracy under uncertainty. Existing models of audiovisual search often treat perception and action in isolation, overlooking how people adaptively coordinate movement and sensory strategies. We present Sensonaut, a computational model of embodied audiovisual search. The core assumption is that people deploy their body and sensory systems in ways they believe will most efficiently improve their chances of locating a target, trading off time and effort under perceptual constraints. Our model formulates this as a resource-rational decision-making problem under partial observability...

---

## 7. Smell with Genji: Rediscovering Human Perception through an Olfactory Game with AI

**Authors**: Hiroshi Ishii...
**Categories**: cs.HC
**Published**: 2026-02-02T20:40:48Z
**Link**: https://arxiv.org/abs/2602.02785v1
**PDF**: https://arxiv.org/pdf/2602.02785v1.pdf

**Abstract**:
> Olfaction plays an important role in human perception, yet its subjective and ephemeral nature makes it difficult to articulate, compare, and share across individuals. Traditional practices like the Japanese incense game Genji-ko offer one way to structure olfactory experience through shared interpretation. In this work, we present Smell with Genji, an AI-mediated olfactory interaction system that reinterprets Genji-ko as a collaborative human-AI sensory experience. By integrating a game setup, a mobile application, and an LLM-powered co-smelling partner equipped with olfactory sensing and LLM-based conversation, the system invites participants to compare scents and construct Genji-mon patterns, fostering reflection through a dialogue that highlights the alignment and discrepancies between...

---

## 8. Markov Random Fields: Structural Properties, Phase Transition, and Response Function Analysis

**Authors**: Catherine A. Calder...
**Categories**: stat.ME
**Published**: 2026-02-02T20:26:56Z
**Link**: https://arxiv.org/abs/2602.02771v1
**PDF**: https://arxiv.org/pdf/2602.02771v1.pdf

**Abstract**:
> This paper presents a focused review of Markov random fields (MRFs)--commonly used probabilistic representations of spatial dependence in discrete spatial domains--for categorical data, with an emphasis on models for binary-valued observations or latent variables. We examine core structural properties of these models, including clique factorization, conditional independence, and the role of neighborhood structures. We also discuss the phenomenon of phase transition and its implications for statistical model specification and inference. A central contribution of this review is the use of response functions, a unifying tool we introduce for prior analysis that provides insight into how different formulations of MRFs influence implied marginal and joint distributions. We illustrate these conc...

---

## 9. Visualizing the Matrix Product as a Transformation: A Task Design Using GeoGebra in Secondary Mathematics Education

**Authors**: Felix De La Cruz Serrano...
**Categories**: math.HO
**Published**: 2026-02-02T20:02:17Z
**Link**: https://arxiv.org/abs/2602.02747v1
**PDF**: https://arxiv.org/pdf/2602.02747v1.pdf

**Abstract**:
> The teaching of matrix multiplication in secondary education is often limited to the mechanical application of the row-by-column algorithm, leaving aside its interpretation as a geometric transformation. This study analyzes the impact of a GeoGebra-mediated instructional sequence, grounded in the Mathematical Working Space (MWS) framework, on students learning of the matrix product. Ten fifth-year secondary students from a school in Lima (Peru) participated in the study. The intervention was carried out over four sessions, combining manual activities with digital exploration using GeoGebra. The results show notable progress in students semiotic genesis, reflected in the coordination of algebraic, graphical, and numerical representations; in instrumental genesis, through the increasingly me...

---

## 10. hSNMF: Hybrid Spatially Regularized NMF for Image-Derived Spatial Transcriptomics

**Authors**: Tania Banerjee...
**Categories**: cs.LG, q-bio.QM
**Published**: 2026-02-02T18:40:08Z
**Link**: https://arxiv.org/abs/2602.02638v1
**PDF**: https://arxiv.org/pdf/2602.02638v1.pdf

**Abstract**:
> High-resolution spatial transcriptomics platforms, such as Xenium, generate single-cell images that capture both molecular and spatial context, but their extremely high dimensionality poses major challenges for representation learning and clustering. In this study, we analyze data from the Xenium platform, which captures high-resolution images of tumor microarray (TMA) tissues and converts them into cell-by-gene matrices suitable for computational analysis. We benchmark and extend nonnegative matrix factorization (NMF) for spatial transcriptomics by introducing two spatially regularized variants. First, we propose Spatial NMF (SNMF), a lightweight baseline that enforces local spatial smoothness by diffusing each cell's NMF factor vector over its spatial neighborhood. Second, we introduce H...

---

## 11. FiLoRA: Focus-and-Ignore LoRA for Controllable Feature Reliance

**Authors**: Kyungreem Han...
**Categories**: cs.LG, cs.AI
**Published**: 2026-02-02T13:00:57Z
**Link**: https://arxiv.org/abs/2602.02060v1
**PDF**: https://arxiv.org/pdf/2602.02060v1.pdf

**Abstract**:
> Multimodal foundation models integrate heterogeneous signals across modalities, yet it remains poorly understood how their predictions depend on specific internal feature groups and whether such reliance can be deliberately controlled. Existing studies of shortcut and spurious behavior largely rely on post hoc analyses or feature removal, offering limited insight into whether reliance can be modulated without altering task semantics. We introduce FiLoRA (Focus-and-Ignore LoRA), an instruction-conditioned, parameter-efficient adaptation framework that enables explicit control over internal feature reliance while keeping the predictive objective fixed. FiLoRA decomposes adaptation into feature group-aligned LoRA modules and applies instruction-conditioned gating, allowing natural language in...

---

## 12. Robust Domain Generalization under Divergent Marginal and Conditional Distributions

**Authors**: Taesup Kim...
**Categories**: cs.LG
**Published**: 2026-02-02T12:13:41Z
**Link**: https://arxiv.org/abs/2602.02015v1
**PDF**: https://arxiv.org/pdf/2602.02015v1.pdf

**Abstract**:
> Domain generalization (DG) aims to learn predictive models that can generalize to unseen domains. Most existing DG approaches focus on learning domain-invariant representations under the assumption of conditional distribution shift (i.e., primarily addressing changes in $P(X\mid Y)$ while assuming $P(Y)$ remains stable). However, real-world scenarios with multiple domains often involve compound distribution shifts where both the marginal label distribution $P(Y)$ and the conditional distribution $P(X\mid Y)$ vary simultaneously. To address this, we propose a unified framework for robust domain generalization under divergent marginal and conditional distributions. We derive a novel risk bound for unseen domains by explicitly decomposing the joint distribution into marginal and conditional c...

---

