# arXiv Papers - 2026-02-07

**论文数量**: 16

## 1. LCLA: Language-Conditioned Latent Alignment for Vision-Language Navigation

**Authors**: Soumik Sarkar...
**Categories**: cs.RO
**Published**: 2026-02-07T17:20:43Z
**Link**: https://arxiv.org/abs/2602.07629v2
**PDF**: https://arxiv.org/pdf/2602.07629v2.pdf

**Abstract**:
> We propose LCLA (Language-Conditioned Latent Alignment), a framework for vision-language navigation that learns modular perception-action interfaces by aligning sensory observations to a latent representation of an expert policy. The expert is first trained with privileged state information, inducing a latent space sufficient for control, after which its latent interface and action head are frozen. A lightweight adapter is then trained to map raw visual-language observations, via a frozen vision-language model, into the expert's latent space, reducing the problem of visuomotor learning to supervised latent alignment rather than end-to-end policy optimization. This decoupling enforces a stable contract between perception and control, enabling expert behavior to be reused across sensing moda...

---

## 2. SciClaimEval: Cross-modal Claim Verification in Scientific Papers

**Authors**: Akiko Aizawa...
**Categories**: cs.CL
**Published**: 2026-02-07T16:58:55Z
**Link**: https://arxiv.org/abs/2602.07621v2
**PDF**: https://arxiv.org/pdf/2602.07621v2.pdf

**Abstract**:
> We present SciClaimEval, a new scientific dataset for the claim verification task. Unlike existing resources, SciClaimEval features authentic claims, including refuted ones, directly extracted from published papers. To create refuted claims, we introduce a novel approach that modifies the supporting evidence (figures and tables), rather than altering the claims or relying on large language models (LLMs) to fabricate contradictions. The dataset provides cross-modal evidence with diverse representations: figures are available as images, while tables are provided in multiple formats, including images, LaTeX source, HTML, and JSON. SciClaimEval contains 1,664 annotated samples from 180 papers across three domains, machine learning, natural language processing, and medicine, validated through e...

---

## 3. Quantifying resilience for distribution system customers with SALEDI

**Authors**: Ian Dobson...
**Categories**: eess.SY, stat.AP
**Published**: 2026-02-07T20:10:43Z
**Link**: https://arxiv.org/abs/2602.07684v1
**PDF**: https://arxiv.org/pdf/2602.07684v1.pdf

**Abstract**:
> The impact of routine smaller outages on distribution system customers in terms of customer minutes interrupted can be tracked using conventional reliability indices. However, the customer minutes interrupted in large blackout events are extremely variable, and this makes it difficult to quantify the customer impact of these extreme events with resilience metrics. We solve this problem with the System Average Large Event Duration Index SALEDI that logarithmically transforms the customer minutes interrupted. We explain how this new resilience metric works, compare it with alternatives, quantify its statistical accuracy, and illustrate its practical use with standard outage data from five utilities.

---

## 4. HistoMet: A Pan-Cancer Deep Learning Framework for Prognostic Prediction of Metastatic Progression and Site Tropism from Primary Tumor Histopathology

**Authors**: M. Khalid Khan Niazi...
**Categories**: cs.CV
**Published**: 2026-02-07T16:25:02Z
**Link**: https://arxiv.org/abs/2602.07608v1
**PDF**: https://arxiv.org/pdf/2602.07608v1.pdf

**Abstract**:
> Metastatic Progression remains the leading cause of cancer-related mortality, yet predicting whether a primary tumor will metastasize and where it will disseminate directly from histopathology remains a fundamental challenge. Although whole-slide images (WSIs) provide rich morphological information, prior computational pathology approaches typically address metastatic status or site prediction as isolated tasks, and do not explicitly model the clinically sequential decision process of metastatic risk assessment followed by downstream site-specific evaluation. To address this research gap, we present a decision-aware, concept-aligned MIL framework, HistoMet, for prognostic metastatic outcome prediction from primary tumor WSIs. Our proposed framework adopts a two-module prediction pipeline i...

---

## 5. Object-Oriented Transition Modeling with Inductive Logic Programming

**Authors**: Dmitri Loguinov...
**Categories**: cs.LG
**Published**: 2026-02-07T16:11:53Z
**Link**: https://arxiv.org/abs/2602.07602v1
**PDF**: https://arxiv.org/pdf/2602.07602v1.pdf

**Abstract**:
> Building models of the world from observation, i.e., induction, is one of the major challenges in machine learning. In order to be useful, models need to maintain accuracy when used in novel situations, i.e., generalize. In addition, they should be easy to interpret and efficient to train. Prior work has investigated these concepts in the context of object-oriented representations inspired by human cognition. In this paper, we develop a novel learning algorithm that is substantially more powerful than these previous methods. Our thorough experiments, including ablation tests and comparison with neural baselines, demonstrate a significant improvement over the state-of-the-art.

---

## 6. MSN: A Memory-based Sparse Activation Scaling Framework for Large-scale Industrial Recommendation

**Authors**: Jingjian Lin...
**Categories**: cs.IR
**Published**: 2026-02-07T12:43:51Z
**Link**: https://arxiv.org/abs/2602.07526v1
**PDF**: https://arxiv.org/pdf/2602.07526v1.pdf

**Abstract**:
> Scaling deep learning recommendation models is an effective way to improve model expressiveness. Existing approaches often incur substantial computational overhead, making them difficult to deploy in large-scale industrial systems under strict latency constraints. Recent sparse activation scaling methods, such as Sparse Mixture-of-Experts, reduce computation by activating only a subset of parameters, but still suffer from high memory access costs and limited personalization capacity due to the large size and small number of experts. To address these challenges, we propose MSN, a memory-based sparse activation scaling framework for recommendation models. MSN dynamically retrieves personalized representations from a large parameterized memory and integrates them into downstream feature inter...

---

## 7. Aegis: Towards Governance, Integrity, and Security of AI Voice Agents

**Authors**: Wenqi Wei...
**Categories**: cs.CR, cs.MA
**Published**: 2026-02-07T05:51:36Z
**Link**: https://arxiv.org/abs/2602.07379v1
**PDF**: https://arxiv.org/pdf/2602.07379v1.pdf

**Abstract**:
> With the rapid advancement and adoption of Audio Large Language Models (ALLMs), voice agents are now being deployed in high-stakes domains such as banking, customer service, and IT support. However, their vulnerabilities to adversarial misuse still remain unexplored. While prior work has examined aspects of trustworthiness in ALLMs, such as harmful content generation and hallucination, systematic security evaluations of voice agents are still lacking. To address this gap, we propose Aegis, a red-teaming framework for the governance, integrity, and security of voice agents. Aegis models the realistic deployment pipeline of voice agents and designs structured adversarial scenarios of critical risks, including privacy leakage, privilege escalation, resource abuse, etc. We evaluate the framewo...

---

## 8. Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation

**Authors**: Gaofeng Meng...
**Categories**: cs.CL, cs.AI
**Published**: 2026-02-07T03:41:04Z
**Link**: https://arxiv.org/abs/2602.07338v1
**PDF**: https://arxiv.org/pdf/2602.07338v1.pdf

**Abstract**:
> Multi-turn conversation has emerged as a predominant interaction paradigm for Large Language Models (LLMs). Users often employ follow-up questions to refine their intent, expecting LLMs to adapt dynamically. However, recent research reveals that LLMs suffer a substantial performance drop in multi-turn settings compared to single-turn interactions with fully specified instructions, a phenomenon termed ``Lost in Conversation'' (LiC). While this prior work attributes LiC to model unreliability, we argue that the root cause lies in an intent alignment gap rather than intrinsic capability deficits. In this paper, we first demonstrate that LiC is not a failure of model capability but rather a breakdown in interaction between users and LLMs. We theoretically show that scaling model size or improv...

---

## 9. Substrate-Voltage-Controlled Temporal Nonlinearity in Ferroelectric FET-based Reservoir Computing

**Authors**: Shinichi Takagi...
**Categories**: physics.app-ph
**Published**: 2026-02-07T03:29:12Z
**Link**: https://arxiv.org/abs/2602.07334v1
**PDF**: https://arxiv.org/pdf/2602.07334v1.pdf

**Abstract**:
> Physical reservoir computing exploits inherent nonlinearity and short-term memory of physical dynamics to achieve efficient processing of time-series data with extremely-low training cost. In this study, we demonstrate a ferroelectric field-effect transistor (FeFET)-based reservoir computing system with augmented temporal and spatial nonlinearity by utilizing both gate and substrate terminals as inputs. The ferroelectric polarization state in the next time step can additionally be controlled by modifying the electric field distribution in the gate stack of FeFET through a substrate input, enabling more diverse internal states compared with the case where inputs are applied only to the gate. To introduce a nonlinearity in the time domain, we introduce a delay between a gate input and a subs...

---

## 10. The Fisher score on the closed simplex

**Authors**: Eva Riccomagno...
**Categories**: math.ST
**Published**: 2026-02-07T19:20:53Z
**Link**: https://arxiv.org/abs/2602.07665v1
**PDF**: https://arxiv.org/pdf/2602.07665v1.pdf

**Abstract**:
> We extend classical analytic tools for finite-state statistical models to allow zero probabilities. Using methods from algebraic statistics and information geometry, we develop a framework in which a smooth statistical model could hit the boundary of the simplex, for example, in contingency tables with non-structural zeros. The central object of our approach is the vector bundle whose fibres are the $p$-contrasts associated to each probability distribution $p$. In this framework, Fisher score and other key statistical concepts, such as entropy for one-dimensional statistical models, admit an algebraic representation also on the boundary of the simplex.

---

## 11. Spectral Gating Networks

**Authors**: Keze Wang...
**Categories**: cs.LG, cs.AI
**Published**: 2026-02-07T20:00:49Z
**Link**: https://arxiv.org/abs/2602.07679v1
**PDF**: https://arxiv.org/pdf/2602.07679v1.pdf

**Abstract**:
> Gating mechanisms are ubiquitous, yet a complementary question in feed-forward networks remains under-explored: how to introduce frequency-rich expressivity without sacrificing stability and scalability? This tension is exposed by spline-based Kolmogorov-Arnold Network (KAN) parameterizations, where grid refinement can induce parameter growth and brittle optimization in high dimensions. To propose a stability-preserving way to inject spectral capacity into existing MLP/FFN layers under fixed parameter and training budgets, we introduce Spectral Gating Networks (SGN), a drop-in spectral reparameterization. SGN augments a standard activation pathway with a compact spectral pathway and learnable gates that allow the model to start from a stable base behavior and progressively allocate capacit...

---

## 12. An Efficient and Robust Projection Enhanced Interpolation Based Tensor Train Decomposition

**Authors**: Tianyi Shi...
**Categories**: math.NA
**Published**: 2026-02-07T18:30:29Z
**Link**: https://arxiv.org/abs/2602.07653v1
**PDF**: https://arxiv.org/pdf/2602.07653v1.pdf

**Abstract**:
> The tensor-train (TT) format is a data-sparse tensor representation commonly used in high dimensional data approximations. In order to represent data with interpretability in data science, researchers develop data-centric skeletonized low rank approximations. However, these methods might still suffer from accuracy degeneracy, nonrobustness, and high computation costs. In this paper, given existing skeletonized TT approximations, we propose a family of projection enhanced interpolation based algorithms to further improve approximation accuracy while keeping low computational complexity. We do this as a postprocessing step to existing interpolative decompositions, via oversampling data not in skeletons to include more information and selecting subsets of pivots for faster projections. We ill...

---

## 13. Cosmology with one galaxy: An analytic formula relating $Ω_{\rm m}$ with galaxy properties

**Authors**: Natalí S. M. de Santi...
**Categories**: astro-ph.CO, astro-ph.GA
**Published**: 2026-02-07T18:23:07Z
**Link**: https://arxiv.org/abs/2602.07651v1
**PDF**: https://arxiv.org/pdf/2602.07651v1.pdf

**Abstract**:
> Standard cosmological analyses typically treat galaxy formation and cosmological parameter inference as decoupled problems, relying on population-level statistics such as clustering, lensing, or halo abundances. However, classical studies of baryon fractions in massive galaxy clusters have long suggested that gravitationally bound systems may retain cosmological information through their baryonic content. Building on this insight, we present the first analytic and physically interpretable cosmological tracer that links the matter density parameter, $Ω_m$, directly to intrinsic galaxy-scale observables, demonstrating that cosmological information can be extracted from individual galaxies. Using symbolic regression applied to state-of-the-art hydrodynamical simulations from the CAMELS projec...

---

## 14. Encoding Matters: Benchmarking Binary and D-ary Representations for Quantum Combinatorial Optimization

**Authors**: Udaya Parampalli...
**Categories**: quant-ph
**Published**: 2026-02-07T04:37:32Z
**Link**: https://arxiv.org/abs/2602.07357v1
**PDF**: https://arxiv.org/pdf/2602.07357v1.pdf

**Abstract**:
> Combinatorial optimization problems are typically formulated using Quadratic Unconstrained Binary Optimization (QUBO), where constraints are enforced through penalty terms that introduce auxiliary variables and rapidly increase Hamiltonian complexity, limiting scalability on near term quantum devices. In this work, we systematically study Quadratic Unconstrained D-ary Optimization (QUDO) as an alternative formulation in which decision variables are encoded directly in higher dimensional Hilbert spaces. We demonstrate that QUDO naturally captures structural constraints across a range of problem classes, including the Traveling Salesman Problem, two variants of the Vehicle Routing Problem, graph coloring, job scheduling, and Max-K-Cut, without the need for extensive penalty constructions. Us...

---

## 15. Knowledge Graph and Hypergraph Transformers with Repository-Attention and Journey-Based Role Transport

**Authors**: Mahesh Godavarti...
**Categories**: cs.LG, cs.AI
**Published**: 2026-02-07T22:44:37Z
**Link**: https://arxiv.org/abs/2603.03304v1
**PDF**: https://arxiv.org/pdf/2603.03304v1.pdf

**Abstract**:
> We present a concise architecture for joint training on sentences and structured data while keeping knowledge and language representations separable. The model treats knowledge graphs and hypergraphs as structured instances with role slots and encodes them into a key-value repository that a language transformer can attend over. Attention is conditioned by journey-based role transport, which unifies edge-labeled KG traversal, hyperedge traversal, and sentence structure. We outline a dual-stream architecture, hierarchical layer groups with instance-local, neighborhood, and global mixing attention, retrieval over a separate repository, and multi-task objectives spanning masked language modeling, link prediction, and role-consistency denoising. The result is an explicit, inspectable separation...

---

## 16. Efficient Table Retrieval and Understanding with Multimodal Large Language Models

**Authors**: Shuai Zhang...
**Categories**: cs.AI, cs.LG
**Published**: 2026-02-07T17:50:33Z
**Link**: https://arxiv.org/abs/2602.07642v1
**PDF**: https://arxiv.org/pdf/2602.07642v1.pdf

**Abstract**:
> Tabular data is frequently captured in image form across a wide range of real-world scenarios such as financial reports, handwritten records, and document scans. These visual representations pose unique challenges for machine understanding, as they combine both structural and visual complexities. While recent advances in Multimodal Large Language Models (MLLMs) show promising results in table understanding, they typically assume the relevant table is readily available. However, a more practical scenario involves identifying and reasoning over relevant tables from large-scale collections to answer user queries. To address this gap, we propose TabRAG, a framework that enables MLLMs to answer queries over large collections of table images. Our approach first retrieves candidate tables using j...

---

