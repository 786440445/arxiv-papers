# arXiv Papers - 2026-03-13

**论文数量**: 470

## 1. Distilling 大语言模型 Semantic Priors into Encoder-Only Multi-Talker 语音识别 with Talker-Count Routing

**原标题**: Distilling LLM Semantic Priors into Encoder-Only Multi-Talker ASR with Talker-Count Routing

**作者**: Hao Shi, Yusuke Fujita, Roman Koshkin, Mengjie Zhao, Yuan Gao, Lianbo Liu, Yui Sudo
**分类**: cs.SD
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10587v1

**中文摘要**:
> arXiv:2603.10587v1 Announce Type: new 
摘要: Large language models (LLMs) provide strong semantic priors that can improve multi-talker automatic 语音 识别 (机器翻译-语音识别), but using an 大语言模型 as an autoregressive decoder is computationally expensive and remains fragile under heavy overlap. In this 论文, we propose an encoder-only 机器翻译-语音识别 框架 that adapts an 大语言模型 to multi-talker conditioning and distills its semantic guidance into the encoder during 训练, while retaining fast CTC-style decoding at 推理. Our 模型 employs a post-encoder separator with serialized CTC to produce talker-ordered transcripts, and leverages an adapted 大语言模型-based SOT objective as a multi-talker-aware teacher signal to explicitly regularize mixed-语音 representations. To further support variable numbers of talkers, we introduce a Talke...

**Original Abstract**:
> arXiv:2603.10587v1 Announce Type: new 
Abstract: Large language models (LLMs) provide strong semantic priors that can improve multi-talker automatic speech recognition (MT-ASR), but using an LLM as an autoregressive decoder is computationally expensive and remains fragile under heavy overlap. In this paper, we propose an encoder-only MT-ASR framework that adapts an LLM to multi-talker conditioning and distills its semantic guidance into the encoder during training, while retaining fast CTC-style decoding at inference. Our model employs a post-encoder separator with serialized CTC to produce talker-ordered transcripts, and leverages an adapted LLM-based SOT objective as a multi-talker-aware teacher signal to explicitly regularize mixed-speech representations. To further support variable num...

---

## 2. AlphaFlowTSE: One-Step 生成式 目标 说话人 Extraction via Conditional AlphaFlow

**原标题**: AlphaFlowTSE: One-Step Generative Target Speaker Extraction via Conditional AlphaFlow

**作者**: Duojia Li, Shuhan Zhang, Zihan Qian, Wenxuan Wu, Shuai Wang, Qingyang Hong, Lin Li, Haizhou Li
**分类**: cs.SD
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10701v1

**中文摘要**:
> arXiv:2603.10701v1 Announce Type: new 
摘要: In 目标 说话人 extraction (TSE), we aim to recover 目标 语音 from a multi-talker mixture using a short enrollment utterance as reference. Recent studies on diffusion and flow-matching generators have improved 目标-语音 fidelity. However, multi-step 采样 increases 延迟, and one-step solutions often rely on a mixture-dependent time coordinate that can be unreliable for real-world conversations. We present AlphaFlowTSE, a one-step conditional 生成式 模型 trained with a Jacobian-向量 product (JVP)-free AlphaFlow objective. AlphaFlowTSE learns mean-velocity transport along a mixture-to-目标 轨迹 starting from the observed mixture, eliminating auxiliary mixing-ratio prediction, and stabilizes 训练 by combining flow matching with an interval-consistency teacher-student 目标. Experiment...

**Original Abstract**:
> arXiv:2603.10701v1 Announce Type: new 
Abstract: In target speaker extraction (TSE), we aim to recover target speech from a multi-talker mixture using a short enrollment utterance as reference. Recent studies on diffusion and flow-matching generators have improved target-speech fidelity. However, multi-step sampling increases latency, and one-step solutions often rely on a mixture-dependent time coordinate that can be unreliable for real-world conversations. We present AlphaFlowTSE, a one-step conditional generative model trained with a Jacobian-vector product (JVP)-free AlphaFlow objective. AlphaFlowTSE learns mean-velocity transport along a mixture-to-target trajectory starting from the observed mixture, eliminating auxiliary mixing-ratio prediction, and stabilizes training by combining ...

---

## 3. 概率 Verification of 声纹 Anti-Spoofing Models

**原标题**: Probabilistic Verification of Voice Anti-Spoofing Models

**作者**: Evgeny Kushnir, Alexandr Kozodaev, Dmitrii Korzh, Mikhail Pautov, Oleg Kiriukhin, Oleg Y. Rogov
**分类**: cs.SD
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10713v1

**中文摘要**:
> arXiv:2603.10713v1 Announce Type: new 
摘要: Recent advances in 生成式 models have amplified the risk of malicious misuse of 语音 合成 technologies, enabling adversaries to impersonate 目标 speakers and access sensitive resources. Although 语音 deepfake 检测 has progressed rapidly, most existing countermeasures lack formal 鲁棒性 guarantees or fail to generalize to unseen 生成 techniques. We propose PV-VASM, a 概率 框架 for verifying the 鲁棒性 of 声纹 anti-spoofing models (VASMs). PV-VASM estimates the probability of misclassification under text-to-语音 (文本转语音), 声纹 cloning (语音转换), and parametric signal transformations. The 方案 is 模型-agnostic and enables 鲁棒性 verification against unseen 语音 合成 techniques and input perturbations. We derive a theoretical upper bound on the error probability and validate the 方法 across diverse...

**Original Abstract**:
> arXiv:2603.10713v1 Announce Type: new 
Abstract: Recent advances in generative models have amplified the risk of malicious misuse of speech synthesis technologies, enabling adversaries to impersonate target speakers and access sensitive resources. Although speech deepfake detection has progressed rapidly, most existing countermeasures lack formal robustness guarantees or fail to generalize to unseen generation techniques. We propose PV-VASM, a probabilistic framework for verifying the robustness of voice anti-spoofing models (VASMs). PV-VASM estimates the probability of misclassification under text-to-speech (TTS), voice cloning (VC), and parametric signal transformations. The approach is model-agnostic and enables robustness verification against unseen speech synthesis techniques and inpu...

---

## 4. When Fine-Tuning Fails and when it Generalises: 角色 of Data Diversity and Mixed 训练 in 大语言模型-based 文本转语音

**原标题**: When Fine-Tuning Fails and when it Generalises: Role of Data Diversity and Mixed Training in LLM-based TTS

**作者**: Anupam Purwar, Aditya Choudhary
**分类**: cs.SD
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10904v1

**中文摘要**:
> arXiv:2603.10904v1 Announce Type: new 
摘要: Large language models are increasingly adopted as semantic backbones for 神经 text-to-语音 systems. However, frozen 大语言模型 representations are insufficient for modeling 说话人 specific acoustic and perceptual characteristics. Our experiments involving fine tuning of the Language 模型 backbone of 文本转语音 show promise in improving the 声纹 consistency and Signal to Noise ratio SNR in 声纹 cloning task. Across multiple speakers LoRA finetuning consistently outperforms the non-finetuned base 通义千问-0.5B 模型 across three complementary dimensions of 语音 quality. First, perceptual quality improves significantly with DNS-MOS gains of up to 0.42 points for speakers whose 训练 data exhibits sufficient acoustic variability. Second, 说话人 fidelity improves for all evaluated speakers...

**Original Abstract**:
> arXiv:2603.10904v1 Announce Type: new 
Abstract: Large language models are increasingly adopted as semantic backbones for neural text-to-speech systems. However, frozen LLM representations are insufficient for modeling speaker specific acoustic and perceptual characteristics. Our experiments involving fine tuning of the Language Model backbone of TTS show promise in improving the voice consistency and Signal to Noise ratio SNR in voice cloning task. Across multiple speakers LoRA finetuning consistently outperforms the non-finetuned base Qwen-0.5B model across three complementary dimensions of speech quality. First, perceptual quality improves significantly with DNS-MOS gains of up to 0.42 points for speakers whose training data exhibits sufficient acoustic variability. Second, speaker fide...

---

## 5. FireRedASR2S: A 状态-of-the-Art Industrial-Grade All-in-One Automatic 语音 识别 系统

**原标题**: FireRedASR2S: A State-of-the-Art Industrial-Grade All-in-One Automatic Speech Recognition System

**作者**: Kaituo Xu, Yan Jia, Kai Huang, Junjie Chen, Wenpeng Li, Kun Liu, Feng-Long Xie, Xu Tang, Yao Hu
**分类**: cs.SD
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10420v1

**中文摘要**:
> arXiv:2603.10420v1 Announce Type: cross 
摘要: We present FireRedASR2S, a 状态-of-the-art industrial-grade all-in-one automatic 语音 识别 (语音识别) 系统. It integrates four modules in a unified pipeline: 语音识别, 声纹 Activity 检测 (VAD), Spoken Language Identification (LID), and Punctuation Prediction (Punc). All modules achieve SOTA 性能 on the evaluated benchmarks: FireRedASR2: An 语音识别 module with two variants, FireRedASR2-大语言模型 (8B+ parameters) and FireRedASR2-AED (1B+ parameters), supporting 语音 and singing transcription for Mandarin, Chinese dialects and accents, English, and 代码-switching. Compared to FireRedASR, FireRedASR2 delivers improved 识别 accuracy and broader dialect and accent coverage. FireRedASR2-大语言模型 achieves 2.89% average CER on 4 public Mandarin benchmarks and 11.55% on 19 public Chinese dial...

**Original Abstract**:
> arXiv:2603.10420v1 Announce Type: cross 
Abstract: We present FireRedASR2S, a state-of-the-art industrial-grade all-in-one automatic speech recognition (ASR) system. It integrates four modules in a unified pipeline: ASR, Voice Activity Detection (VAD), Spoken Language Identification (LID), and Punctuation Prediction (Punc). All modules achieve SOTA performance on the evaluated benchmarks: FireRedASR2: An ASR module with two variants, FireRedASR2-LLM (8B+ parameters) and FireRedASR2-AED (1B+ parameters), supporting speech and singing transcription for Mandarin, Chinese dialects and accents, English, and code-switching. Compared to FireRedASR, FireRedASR2 delivers improved recognition accuracy and broader dialect and accent coverage. FireRedASR2-LLM achieves 2.89% average CER on 4 public Man...

---

## 6. Fish 音频 S2 技术报告

**原标题**: Fish Audio S2 Technical Report

**作者**: Shijia Liao, Yuxuan Wang, Songting Liu, Yifan Cheng, Ruoyi Zhang, Tianyu Li, Shidong Li, Yisheng Zheng, Xingwei Liu, Qingzheng Wang, Zhizhuo Zhou, Jiahua Liu, Xin Chen, Dawei Han
**分类**: cs.SD
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.08823v2

**中文摘要**:
> arXiv:2603.08823v2 Announce Type: replace 
摘要: We introduce Fish 音频 S2, an open-sourced text-to-语音 系统 featuring multi-说话人, multi-turn 生成, and, most importantly, instruction-following 控制 via natural-language descriptions. To scale 训练, we develop a multi-stage 训练 recipe together with a staged data pipeline covering 视频 captioning and 语音 captioning, 声纹-quality assessment, and 奖励 modeling. To push the frontier of open-source 文本转语音, we release our 模型 weights, fine-tuning 代码, and an SGLang-based 推理 engine. The 推理 engine is production-ready for 流式, achieving an RTF of 0.195 and a time-to-first-音频 below 100 ms.Our 代码 and weights are available on GitHub (https://GitHub.com/fishaudio/fish-语音) and Hugging Face (https://huggingface.co/fishaudio/s2-pro). We highly encourage readers to visit https://fish...

**Original Abstract**:
> arXiv:2603.08823v2 Announce Type: replace 
Abstract: We introduce Fish Audio S2, an open-sourced text-to-speech system featuring multi-speaker, multi-turn generation, and, most importantly, instruction-following control via natural-language descriptions. To scale training, we develop a multi-stage training recipe together with a staged data pipeline covering video captioning and speech captioning, voice-quality assessment, and reward modeling. To push the frontier of open-source TTS, we release our model weights, fine-tuning code, and an SGLang-based inference engine. The inference engine is production-ready for streaming, achieving an RTF of 0.195 and a time-to-first-audio below 100 ms.Our code and weights are available on GitHub (https://github.com/fishaudio/fish-speech) and Hugging Face...

---

## 7. FireRedASR2S: A 状态-of-the-Art Industrial-Grade All-in-One Automatic 语音 识别 系统

**原标题**: FireRedASR2S: A State-of-the-Art Industrial-Grade All-in-One Automatic Speech Recognition System

**作者**: Kaituo Xu, Yan Jia, Kai Huang, Junjie Chen, Wenpeng Li, Kun Liu, Feng-Long Xie, Xu Tang, Yao Hu
**分类**: eess.AS
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10420v1

**中文摘要**:
> arXiv:2603.10420v1 Announce Type: new 
摘要: We present FireRedASR2S, a 状态-of-the-art industrial-grade all-in-one automatic 语音 识别 (语音识别) 系统. It integrates four modules in a unified pipeline: 语音识别, 声纹 Activity 检测 (VAD), Spoken Language Identification (LID), and Punctuation Prediction (Punc). All modules achieve SOTA 性能 on the evaluated benchmarks: FireRedASR2: An 语音识别 module with two variants, FireRedASR2-大语言模型 (8B+ parameters) and FireRedASR2-AED (1B+ parameters), supporting 语音 and singing transcription for Mandarin, Chinese dialects and accents, English, and 代码-switching. Compared to FireRedASR, FireRedASR2 delivers improved 识别 accuracy and broader dialect and accent coverage. FireRedASR2-大语言模型 achieves 2.89% average CER on 4 public Mandarin benchmarks and 11.55% on 19 public Chinese dialec...

**Original Abstract**:
> arXiv:2603.10420v1 Announce Type: new 
Abstract: We present FireRedASR2S, a state-of-the-art industrial-grade all-in-one automatic speech recognition (ASR) system. It integrates four modules in a unified pipeline: ASR, Voice Activity Detection (VAD), Spoken Language Identification (LID), and Punctuation Prediction (Punc). All modules achieve SOTA performance on the evaluated benchmarks: FireRedASR2: An ASR module with two variants, FireRedASR2-LLM (8B+ parameters) and FireRedASR2-AED (1B+ parameters), supporting speech and singing transcription for Mandarin, Chinese dialects and accents, English, and code-switching. Compared to FireRedASR, FireRedASR2 delivers improved recognition accuracy and broader dialect and accent coverage. FireRedASR2-LLM achieves 2.89% average CER on 4 public Manda...

---

## 8. 可解释 大语言模型 Unlearning Through 推理

**原标题**: Explainable LLM Unlearning Through Reasoning

**作者**: Junfeng Liao, Qizhou Wang, Shanshan Ye, Xin Yu, Ling Chen, Zhen Fang
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.09980v1

**中文摘要**:
> arXiv:2603.09980v1 Announce Type: new 
摘要: 大语言模型 unlearning is essential for mitigating safety, copyright, and 隐私 concerns in pre-trained large language models (LLMs). Compared to preference alignment, it offers a more explicit way by removing undesirable knowledge characterized by specific unlearning datasets. In previous works, 梯度 上升 (GA) and its variants have shown promise for implementing unlearning, yet their untargeted nature results in unintended degradation of general capabilities, incomplete removal of knowledge, and the 生成 of incoherent responses, among many others. We argue that these issues stem from the absence of explicit guidance on what and how models should unlearn. To fill this gap, we introduce a novel unlearning 目标, 推理-based unlearning 目标, which satisfies both the speci...

**Original Abstract**:
> arXiv:2603.09980v1 Announce Type: new 
Abstract: LLM unlearning is essential for mitigating safety, copyright, and privacy concerns in pre-trained large language models (LLMs). Compared to preference alignment, it offers a more explicit way by removing undesirable knowledge characterized by specific unlearning datasets. In previous works, gradient ascent (GA) and its variants have shown promise for implementing unlearning, yet their untargeted nature results in unintended degradation of general capabilities, incomplete removal of knowledge, and the generation of incoherent responses, among many others. We argue that these issues stem from the absence of explicit guidance on what and how models should unlearn. To fill this gap, we introduce a novel unlearning target, reasoning-based unlearn...

---

## 9. MoE-SpAc: 高效 MoE 推理 Based on Speculative Activation Utility in Heterogeneous Edge Scenarios

**原标题**: MoE-SpAc: Efficient MoE Inference Based on Speculative Activation Utility in Heterogeneous Edge Scenarios

**作者**: Shuhuai Li, Jianghao Lin, Dongdong Ge, Yinyu Ye
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.09983v1

**中文摘要**:
> arXiv:2603.09983v1 Announce Type: new 
摘要: Mixture-of-Experts (MoE) models enable 可扩展 性能 but face severe 内存 constraints on edge devices. Existing offloading strategies struggle with I/O bottlenecks due to the 动态, low-information nature of autoregressive expert activation. In this 论文, we propose to repurpose Speculative Decoding (SD) not merely as a compute加速器, but as an informative lookahead sensor for 内存 management, supported by our theoretical and empirical analyses. Hence, we introduce MoE-SpAc, an MoE 推理 框架 that integrates a Speculative Utility Estimator to track expert demand, a Heterogeneous Workload Balancer to dynamically partition computation via 在线 integer 优化, and an Asynchronous Execution Engine to unify the prefetching and eviction in the same utility space. Extensive experimen...

**Original Abstract**:
> arXiv:2603.09983v1 Announce Type: new 
Abstract: Mixture-of-Experts (MoE) models enable scalable performance but face severe memory constraints on edge devices. Existing offloading strategies struggle with I/O bottlenecks due to the dynamic, low-information nature of autoregressive expert activation. In this paper, we propose to repurpose Speculative Decoding (SD) not merely as a compute accelerator, but as an informative lookahead sensor for memory management, supported by our theoretical and empirical analyses. Hence, we introduce MoE-SpAc, an MoE inference framework that integrates a Speculative Utility Estimator to track expert demand, a Heterogeneous Workload Balancer to dynamically partition computation via online integer optimization, and an Asynchronous Execution Engine to unify th...

---

## 10. Personalized Group Relative 策略 优化 for Heterogenous Preference Alignment

**原标题**: Personalized Group Relative Policy Optimization for Heterogenous Preference Alignment

**作者**: Jialu Wang, Heinrich Peters, Asad A. Butt, Navid Hashemi, Alireza Hashemi, Pouya M. Ghari, Joseph Hoover, James Rae, Morteza Dehghani
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10009v1

**中文摘要**:
> arXiv:2603.10009v1 Announce Type: new 
摘要: Despite their sophisticated general-purpose capabilities, Large Language Models (LLMs) often fail to align with diverse individual preferences because standard post-训练 methods, like 强化 学习 with Human Feedback (RLHF), optimize for a single, global objective. While Group Relative 策略 优化 (GRPO) is a widely adopted on-策略 强化 学习 框架, its group-based 归一化 implicitly assumes that all samples are exchangeable, inheriting this limitation in personalized settings. This assumption conflates distinct user 奖励 distributions and systematically biases 学习 toward dominant preferences while suppressing minority signals. To address this, we introduce Personalized GRPO (P-GRPO), a novel alignment 框架 that decouples 优势 estimation from immediate 批次 statistics. By normalizing ...

**Original Abstract**:
> arXiv:2603.10009v1 Announce Type: new 
Abstract: Despite their sophisticated general-purpose capabilities, Large Language Models (LLMs) often fail to align with diverse individual preferences because standard post-training methods, like Reinforcement Learning with Human Feedback (RLHF), optimize for a single, global objective. While Group Relative Policy Optimization (GRPO) is a widely adopted on-policy reinforcement learning framework, its group-based normalization implicitly assumes that all samples are exchangeable, inheriting this limitation in personalized settings. This assumption conflates distinct user reward distributions and systematically biases learning toward dominant preferences while suppressing minority signals. To address this, we introduce Personalized GRPO (P-GRPO), a no...

---

## 11. Revisiting Sharpness-Aware Minimization: A More Faithful and Effective 实现

**原标题**: Revisiting Sharpness-Aware Minimization: A More Faithful and Effective Implementation

**作者**: Jianlong Chen, Zhiming Zhou
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10048v1

**中文摘要**:
> arXiv:2603.10048v1 Announce Type: new 
摘要: Sharpness-Aware Minimization (SAM) enhances 泛化 by minimizing the maximum 训练 损失 within a predefined neighborhood around the parameters. However, its practical 实现 approximates this as 梯度 上升(s) followed by applying the 梯度 at the 上升 point to update the current parameters. This practice can be justified as approximately optimizing the objective by neglecting the (full) derivative of the 上升 point with respect to the current parameters. Nevertheless, a direct and intuitive understanding of why using the 梯度 at the 上升 point to update the current parameters works superiorly is still lacking. Our work bridges this gap by proposing a novel and intuitive interpretation. We show that the 梯度 at the single-step 上升 point, \uline{when applied to the current paramet...

**Original Abstract**:
> arXiv:2603.10048v1 Announce Type: new 
Abstract: Sharpness-Aware Minimization (SAM) enhances generalization by minimizing the maximum training loss within a predefined neighborhood around the parameters. However, its practical implementation approximates this as gradient ascent(s) followed by applying the gradient at the ascent point to update the current parameters. This practice can be justified as approximately optimizing the objective by neglecting the (full) derivative of the ascent point with respect to the current parameters. Nevertheless, a direct and intuitive understanding of why using the gradient at the ascent point to update the current parameters works superiorly is still lacking. Our work bridges this gap by proposing a novel and intuitive interpretation. We show that the gr...

---

## 12. InFusionLayer: a CFA-based ensemble tool to generate new classifiers for 学习 and modeling

**原标题**: InFusionLayer: a CFA-based ensemble tool to generate new classifiers for learning and modeling

**作者**: Eric Roginek, Jingyan Xu, D. Frank. Hsu
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10049v1

**中文摘要**:
> arXiv:2603.10049v1 Announce Type: new 
摘要: Ensemble 学习 is a well established body of methods for machine 学习 to enhance predictive 性能 by combining multiple algorithms/models. Combinatorial Fusion Analysis (CFA) has provided 方法 and practice for combining multiple scoring systems, using rank-score characteristic (RSC) function and cognitive diversity (CD), including ensemble 方法 and 模型 fusion. However, there is no general-purpose Python tool available that incorporate these techniques. In this 论文 we introduce \texttt{InFusionLayer}, a machine 学习 架构 inspired by CFA at the 系统 fusion level that uses a moderate set of base models to optimize 无监督 and 有监督 学习 multiclassification problems. We demonstrate \texttt{InFusionLayer}'s ease of use for PyTorch, TensorFlow, and Scikit-learn workflows by valida...

**Original Abstract**:
> arXiv:2603.10049v1 Announce Type: new 
Abstract: Ensemble learning is a well established body of methods for machine learning to enhance predictive performance by combining multiple algorithms/models. Combinatorial Fusion Analysis (CFA) has provided method and practice for combining multiple scoring systems, using rank-score characteristic (RSC) function and cognitive diversity (CD), including ensemble method and model fusion. However, there is no general-purpose Python tool available that incorporate these techniques. In this paper we introduce \texttt{InFusionLayer}, a machine learning architecture inspired by CFA at the system fusion level that uses a moderate set of base models to optimize unsupervised and supervised learning multiclassification problems. We demonstrate \texttt{InFusio...

---

## 13. 集群-Aware 注意力-Based 深度 强化 学习 for Pickup and Delivery Problems

**原标题**: Cluster-Aware Attention-Based Deep Reinforcement Learning for Pickup and Delivery Problems

**作者**: Wentao Wang, Lifeng Han, Guangyu Zou
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10053v1

**中文摘要**:
> arXiv:2603.10053v1 Announce Type: new 
摘要: The Pickup and Delivery Problem (PDP) is a fundamental and challenging variant of the Vehicle Routing Problem, characterized by tightly coupled pickup--delivery pairs, precedence constraints, and spatial layouts that often exhibit clustering. Existing 深度 强化 学习 (DRL) approaches either 模型 all nodes on a flat graph, relying on implicit 学习 to enforce constraints, or achieve strong 性能 through 推理-time collaborative 搜索 at the cost of substantial 延迟. In this 论文, we propose \emph{CAADRL} (集群-Aware 注意力-based 深度 强化 学习), a DRL 框架 that explicitly exploits the multi-scale structure of PDP instances via 集群-aware encoding and hierarchical decoding. The encoder builds on a Transformer and combines global self-注意力 with intra-集群 注意力 over depot, pickup, and delivery ...

**Original Abstract**:
> arXiv:2603.10053v1 Announce Type: new 
Abstract: The Pickup and Delivery Problem (PDP) is a fundamental and challenging variant of the Vehicle Routing Problem, characterized by tightly coupled pickup--delivery pairs, precedence constraints, and spatial layouts that often exhibit clustering. Existing deep reinforcement learning (DRL) approaches either model all nodes on a flat graph, relying on implicit learning to enforce constraints, or achieve strong performance through inference-time collaborative search at the cost of substantial latency. In this paper, we propose \emph{CAADRL} (Cluster-Aware Attention-based Deep Reinforcement Learning), a DRL framework that explicitly exploits the multi-scale structure of PDP instances via cluster-aware encoding and hierarchical decoding. The encoder ...

---

## 14. HTMuon: Improving Muon via Heavy-Tailed Spectral Correction

**原标题**: HTMuon: Improving Muon via Heavy-Tailed Spectral Correction

**作者**: Tianyu Pang, Yujie Fang, Zihang Liu, Shenyang Deng, Lei Hsiung, Shuhua Yu, Yaoqing Yang
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10067v1

**中文摘要**:
> arXiv:2603.10067v1 Announce Type: new 
摘要: Muon has recently shown promising results in 大语言模型 训练. In this work, we study how to further improve Muon. We argue that Muon's orthogonalized update rule suppresses the emergence of heavy-tailed weight spectra and over-emphasizes the 训练 along noise-dominated directions. Motivated by the Heavy-Tailed Self-正则化 (HT-SR) theory, we propose HTMuon. HTMuon preserves Muon's ability to capture parameter interdependencies while producing heavier-tailed updates and inducing heavier-tailed weight spectra. Experiments on 大语言模型 pretraining and 图像 分类 show that HTMuon consistently improves 性能 over 状态-of-the-art baselines and can also serve as a plug-in on top of existing Muon variants. For example, on LLaMA pretraining on the C4 数据集, HTMuon reduces perplexity by...

**Original Abstract**:
> arXiv:2603.10067v1 Announce Type: new 
Abstract: Muon has recently shown promising results in LLM training. In this work, we study how to further improve Muon. We argue that Muon's orthogonalized update rule suppresses the emergence of heavy-tailed weight spectra and over-emphasizes the training along noise-dominated directions. Motivated by the Heavy-Tailed Self-Regularization (HT-SR) theory, we propose HTMuon. HTMuon preserves Muon's ability to capture parameter interdependencies while producing heavier-tailed updates and inducing heavier-tailed weight spectra. Experiments on LLM pretraining and image classification show that HTMuon consistently improves performance over state-of-the-art baselines and can also serve as a plug-in on top of existing Muon variants. For example, on LLaMA pre...

---

## 15. Improving 搜索 智能体 with One Line of 代码

**原标题**: Improving Search Agent with One Line of Code

**作者**: Jian Li, Dongsheng Chen, Zhenhua Xu, Yizhang Jin, Jiafu Wu, Chengjie Wang, Xiaotong Yuan, Yabiao Wang
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10069v1

**中文摘要**:
> arXiv:2603.10069v1 Announce Type: new 
摘要: Tool-based Agentic 强化 学习 (TARL) has emerged as a promising paradigm for 训练 搜索 agents to interact with external tools for a multi-turn information-seeking process autonomously. However, we identify a critical 训练 instability that leads to catastrophic 模型 collapse: Importance 采样 Distribution Drift(ISDD). In Group Relative 策略 优化(GRPO), a widely adopted TARL 算法, ISDD manifests as a precipitous decline in the importance 采样 ratios, which nullifies 梯度 updates and triggers irreversible 训练 failure. To address this, we propose \textbf{S}earch \textbf{A}gent \textbf{P}olicy \textbf{O}ptimization (\textbf{SAPO}), which stabilizes 训练 via a conditional token-level KL constraint. Unlike hard clipping, which ignores distributional divergence, SAPO selectively pena...

**Original Abstract**:
> arXiv:2603.10069v1 Announce Type: new 
Abstract: Tool-based Agentic Reinforcement Learning (TARL) has emerged as a promising paradigm for training search agents to interact with external tools for a multi-turn information-seeking process autonomously. However, we identify a critical training instability that leads to catastrophic model collapse: Importance Sampling Distribution Drift(ISDD). In Group Relative Policy Optimization(GRPO), a widely adopted TARL algorithm, ISDD manifests as a precipitous decline in the importance sampling ratios, which nullifies gradient updates and triggers irreversible training failure. To address this, we propose \textbf{S}earch \textbf{A}gent \textbf{P}olicy \textbf{O}ptimization (\textbf{SAPO}), which stabilizes training via a conditional token-level KL con...

---

## 16. Marginals Before Conditionals

**原标题**: Marginals Before Conditionals

**作者**: Mihir Sahasrabudhe
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10074v1

**中文摘要**:
> arXiv:2603.10074v1 Announce Type: new 
摘要: We construct a minimal task that isolates conditional 学习 in 神经 networks: a surjective map with K-fold ambiguity, resolved by a selector token z, so H(A | B) = log K while H(A | B, z) = 0. The 模型 learns the marginal P(A | B) first, producing a plateau at exactly log K, before acquiring the full conditional in a sharp, collective 转移. The plateau has a clean decomposition: height = log K (set by ambiguity), duration = f(D) (set by 数据集 size D, not K). 梯度 noise stabilizes the marginal solution: higher 学习 rates monotonically slow the 转移 (3.6* across a 7* {\eta} range at fixed 吞吐量), and 批次-size reduction delays escape, consistent with an entropic force opposing departure from the low-梯度 marginal. Internally, a selector-routing head assembles during the p...

**Original Abstract**:
> arXiv:2603.10074v1 Announce Type: new 
Abstract: We construct a minimal task that isolates conditional learning in neural networks: a surjective map with K-fold ambiguity, resolved by a selector token z, so H(A | B) = log K while H(A | B, z) = 0. The model learns the marginal P(A | B) first, producing a plateau at exactly log K, before acquiring the full conditional in a sharp, collective transition. The plateau has a clean decomposition: height = log K (set by ambiguity), duration = f(D) (set by dataset size D, not K). Gradient noise stabilizes the marginal solution: higher learning rates monotonically slow the transition (3.6* across a 7* {\eta} range at fixed throughput), and batch-size reduction delays escape, consistent with an entropic force opposing departure from the low-gradient m...

---

## 17. Stochastic Port-Hamiltonian 神经 Networks: Universal Approximation with Passivity Guarantees

**原标题**: Stochastic Port-Hamiltonian Neural Networks: Universal Approximation with Passivity Guarantees

**作者**: Luca Di Persio, Matthias Ehrhardt, Youness Outaleb
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10078v1

**中文摘要**:
> arXiv:2603.10078v1 Announce Type: new 
摘要: Stochastic port-Hamiltonian systems represent open dynamical systems with dissipation, inputs, and stochastic forcing in an energy based form. We introduce stochastic port-Hamiltonian 神经 networks, SPH-NNs, which parameterize the Hamiltonian with a feedforward 网络 and enforce skew symmetry of the interconnection matrix and positive semidefiniteness of the dissipation matrix. For It\^o dynamics we establish a weak passivity inequality in expectation under an explicit generator condition, stated for a stopped process on a compact set. We also prove a universal approximation 结果 showing that, on any compact set and finite 视野, SPH-NNs approximate the coefficients of a 目标 stochastic port-Hamiltonian 系统 with $C^2$ accuracy of the Hamiltonian and yield coup...

**Original Abstract**:
> arXiv:2603.10078v1 Announce Type: new 
Abstract: Stochastic port-Hamiltonian systems represent open dynamical systems with dissipation, inputs, and stochastic forcing in an energy based form. We introduce stochastic port-Hamiltonian neural networks, SPH-NNs, which parameterize the Hamiltonian with a feedforward network and enforce skew symmetry of the interconnection matrix and positive semidefiniteness of the dissipation matrix. For It\^o dynamics we establish a weak passivity inequality in expectation under an explicit generator condition, stated for a stopped process on a compact set. We also prove a universal approximation result showing that, on any compact set and finite horizon, SPH-NNs approximate the coefficients of a target stochastic port-Hamiltonian system with $C^2$ accuracy o...

---

## 18. Large Spikes in Stochastic 梯度 Descent: A Large-Deviations View

**原标题**: Large Spikes in Stochastic Gradient Descent: A Large-Deviations View

**作者**: Benjamin Gess, Daniel Heydecker
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10079v1

**中文摘要**:
> arXiv:2603.10079v1 Announce Type: new 
摘要: We analyse SGD 训练 of a shallow, fully connected 网络 in the NTK scaling and provide a quantitative theory of the catapult phase. We identify an explicit criterion separating two behaviours: When an explicit function $G$, depending only on the kernel, 学习 rate $\eta$ and data, is positive, SGD produces large NTK-flattening spikes with high probability; when $G<0$, their probability decays like $(n/\eta)^{-\vartheta/2}$, for an explicitly characterised $\vartheta\in (0,\infty)$. This yields a concrete parameter-dependent explanation for why such spikes may still be observed at practical widths.

**Original Abstract**:
> arXiv:2603.10079v1 Announce Type: new 
Abstract: We analyse SGD training of a shallow, fully connected network in the NTK scaling and provide a quantitative theory of the catapult phase. We identify an explicit criterion separating two behaviours: When an explicit function $G$, depending only on the kernel, learning rate $\eta$ and data, is positive, SGD produces large NTK-flattening spikes with high probability; when $G<0$, their probability decays like $(n/\eta)^{-\vartheta/2}$, for an explicitly characterised $\vartheta\in (0,\infty)$. This yields a concrete parameter-dependent explanation for why such spikes may still be observed at practical widths.

---

## 19. Digging Deeper: 学习 Multi-Level Concept Hierarchies

**原标题**: Digging Deeper: Learning Multi-Level Concept Hierarchies

**作者**: Oscar Hill, Mateo Espinosa Zarlenga, Mateja Jamnik
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10084v1

**中文摘要**:
> arXiv:2603.10084v1 Announce Type: new 
摘要: Although concept-based models promise interpretability by explaining predictions with human-understandable concepts, they typically rely on exhaustive annotations and treat concepts as flat and independent. To circumvent this, recent work has introduced Hierarchical Concept 嵌入 Models (HiCEMs) to explicitly 模型 concept relationships, and Concept Splitting to discover sub-concepts using only coarse annotations. However, both HiCEMs and Concept Splitting are restricted to shallow hierarchies. We overcome this limitation with Multi-Level Concept Splitting (MLCS), which discovers multi-level concept hierarchies from only top-level supervision, and 深度-HiCEMs, an 架构 that represents these discovered hierarchies and enables interventions at multiple levels ...

**Original Abstract**:
> arXiv:2603.10084v1 Announce Type: new 
Abstract: Although concept-based models promise interpretability by explaining predictions with human-understandable concepts, they typically rely on exhaustive annotations and treat concepts as flat and independent. To circumvent this, recent work has introduced Hierarchical Concept Embedding Models (HiCEMs) to explicitly model concept relationships, and Concept Splitting to discover sub-concepts using only coarse annotations. However, both HiCEMs and Concept Splitting are restricted to shallow hierarchies. We overcome this limitation with Multi-Level Concept Splitting (MLCS), which discovers multi-level concept hierarchies from only top-level supervision, and Deep-HiCEMs, an architecture that represents these discovered hierarchies and enables inter...

---

## 20. KernelSkill: A Multi-智能体 框架 for GPU Kernel 优化

**原标题**: KernelSkill: A Multi-Agent Framework for GPU Kernel Optimization

**作者**: Qitong Sun, Jun Han, Tianlin Li, Zhe Tang, Sheng Chen, Fei Yang, Aishan Liu, Xianglong Liu, Yang Liu
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10085v1

**中文摘要**:
> arXiv:2603.10085v1 Announce Type: new 
摘要: Improving GPU kernel efficiency is crucial for advancing AI systems. Recent work has explored leveraging large language models (LLMs) for GPU kernel 生成 and 优化. However, existing 大语言模型-based kernel 优化 pipelines typically rely on opaque, implicitly learned heuristics within the LLMs to determine 优化 strategies. This leads to inefficient trial-and-error and weakly 可解释 optimizations. Our key insight is to replace implicit heuristics with expert 优化 skills that are knowledge-driven and aware of task trajectories. Specifically, we present KernelSkill, a multi-智能体 框架 with a dual-level 内存 架构. KernelSkill operates by coordinating agents with long-term 内存 of reusable expert skills and short-term 内存 to prevent repetitive backtracking. On KernelBench Levels 1-3...

**Original Abstract**:
> arXiv:2603.10085v1 Announce Type: new 
Abstract: Improving GPU kernel efficiency is crucial for advancing AI systems. Recent work has explored leveraging large language models (LLMs) for GPU kernel generation and optimization. However, existing LLM-based kernel optimization pipelines typically rely on opaque, implicitly learned heuristics within the LLMs to determine optimization strategies. This leads to inefficient trial-and-error and weakly interpretable optimizations. Our key insight is to replace implicit heuristics with expert optimization skills that are knowledge-driven and aware of task trajectories. Specifically, we present KernelSkill, a multi-agent framework with a dual-level memory architecture. KernelSkill operates by coordinating agents with long-term memory of reusable expe...

---

## 21. Equivariant Asynchronous Diffusion: An Adaptive Denoising Schedule for Accelerated Molecular Conformation 生成

**原标题**: Equivariant Asynchronous Diffusion: An Adaptive Denoising Schedule for Accelerated Molecular Conformation Generation

**作者**: Junyi An, Chao Qu, Yun-Fei Shi, Zhijian Zhou, Fenglei Cao, Yuan Qi
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10093v1

**中文摘要**:
> arXiv:2603.10093v1 Announce Type: new 
摘要: Recent 3D molecular 生成 methods primarily use asynchronous auto-regressive or synchronous diffusion models. While auto-regressive models build molecules sequentially, they're limited by a short 视野 and a discrepancy between 训练 and 推理. Conversely, synchronous diffusion models denoise all atoms at once, offering a molecule-level 视野 but failing to capture the 因果 relationships inherent in hierarchical molecular structures. We introduce Equivariant Asynchronous Diffusion (EAD) to overcome these limitations. EAD is a novel diffusion 模型 that combines the strengths of both approaches: it uses an asynchronous denoising schedule to better capture molecular hierarchy while maintaining a molecule-level 视野. Since these relationships are often complex, we propose...

**Original Abstract**:
> arXiv:2603.10093v1 Announce Type: new 
Abstract: Recent 3D molecular generation methods primarily use asynchronous auto-regressive or synchronous diffusion models. While auto-regressive models build molecules sequentially, they're limited by a short horizon and a discrepancy between training and inference. Conversely, synchronous diffusion models denoise all atoms at once, offering a molecule-level horizon but failing to capture the causal relationships inherent in hierarchical molecular structures. We introduce Equivariant Asynchronous Diffusion (EAD) to overcome these limitations. EAD is a novel diffusion model that combines the strengths of both approaches: it uses an asynchronous denoising schedule to better capture molecular hierarchy while maintaining a molecule-level horizon. Since ...

---

## 22. Rethinking Adam for Time Series Forecasting: A Simple Heuristic to Improve 优化 under Distribution Shifts

**原标题**: Rethinking Adam for Time Series Forecasting: A Simple Heuristic to Improve Optimization under Distribution Shifts

**作者**: Yuze Dong, Jinsong Wu
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10095v1

**中文摘要**:
> arXiv:2603.10095v1 Announce Type: new 
摘要: Time-series forecasting often faces challenges from non-stationarity, particularly distributional drift, where the data distribution evolves over time. This 动态 behavior can undermine the effectiveness of adaptive optimizers, such as Adam, which are typically designed for stationary objectives. In this 论文, we revisit Adam in the context of non-stationary forecasting and identify that its second-order 偏见 correction limits responsiveness to shifting 损失 landscapes. To address this, we propose TS_Adam, a lightweight variant that removes the second-order correction from the 学习 rate computation. This simple modification improves adaptability to distributional drift while preserving the 优化器 core structure and requiring no additional hyperparameters. TS_Ad...

**Original Abstract**:
> arXiv:2603.10095v1 Announce Type: new 
Abstract: Time-series forecasting often faces challenges from non-stationarity, particularly distributional drift, where the data distribution evolves over time. This dynamic behavior can undermine the effectiveness of adaptive optimizers, such as Adam, which are typically designed for stationary objectives. In this paper, we revisit Adam in the context of non-stationary forecasting and identify that its second-order bias correction limits responsiveness to shifting loss landscapes. To address this, we propose TS_Adam, a lightweight variant that removes the second-order correction from the learning rate computation. This simple modification improves adaptability to distributional drift while preserving the optimizer core structure and requiring no add...

---

## 23. Denoising the US Census: Succinct Block Hierarchical Regression

**原标题**: Denoising the US Census: Succinct Block Hierarchical Regression

**作者**: Badih Ghazi, Pritish Kamath, Ravi Kumar, Pasin Manurangsi, Adam Sealfon
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10099v1

**中文摘要**:
> arXiv:2603.10099v1 Announce Type: new 
摘要: The US Census Bureau Disclosure Avoidance 系统 (DAS) balances confidentiality and utility requirements for the decennial US Census (Abowd et al., 2022). The DAS was used in the 2020 Census to produce demographic datasets critically used for legislative apportionment and redistricting, federal and 状态 funding allocation, municipal and infrastructure 规划, and scientific research. At the heart of DAS is TopDown, a heuristic post-processing 方法 that combines billions of private noisy measurements across six geographic levels in order to produce new estimates that are consistent, more 准确, and satisfy certain structural constraints on the data.
  In this work, we introduce BlueDown, a new post-processing 方法 that produces more 准确, consistent estimates while s...

**Original Abstract**:
> arXiv:2603.10099v1 Announce Type: new 
Abstract: The US Census Bureau Disclosure Avoidance System (DAS) balances confidentiality and utility requirements for the decennial US Census (Abowd et al., 2022). The DAS was used in the 2020 Census to produce demographic datasets critically used for legislative apportionment and redistricting, federal and state funding allocation, municipal and infrastructure planning, and scientific research. At the heart of DAS is TopDown, a heuristic post-processing method that combines billions of private noisy measurements across six geographic levels in order to produce new estimates that are consistent, more accurate, and satisfy certain structural constraints on the data.
  In this work, we introduce BlueDown, a new post-processing method that produces more...

---

## 24. Hardware 高效 Approximate 卷积 with Tunable Error Tolerance for CNNs

**原标题**: Hardware Efficient Approximate Convolution with Tunable Error Tolerance for CNNs

**作者**: Vishal Shashidhar, Anupam Kumari, Roy P Paily
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10100v1

**中文摘要**:
> arXiv:2603.10100v1 Announce Type: new 
摘要: Modern CNNs' high computational demands hinder edge 部署, as traditional ``hard'' sparsity (skipping mathematical zeros) loses effectiveness in 深度 layers or with smooth activations like Tanh. We propose a ``soft sparsity'' paradigm using a hardware 高效 Most Significant Bit (MSB) 代理 to skip negligible non-zero multiplications. Integrated as a custom RISC-V instruction and evaluated on LeNet-5 (MNIST), this 方法 reduces ReLU MACs by 88.42% and Tanh MACs by 74.87% with zero accuracy 损失--outperforming zero-skipping by 5x. By clock-gating inactive multipliers, we estimate power savings of 35.2\% for ReLU and 29.96\% for Tanh. While 内存 access makes power reduction sub-linear to operation savings, this 方案 significantly optimizes resource-constrained 推理.

**Original Abstract**:
> arXiv:2603.10100v1 Announce Type: new 
Abstract: Modern CNNs' high computational demands hinder edge deployment, as traditional ``hard'' sparsity (skipping mathematical zeros) loses effectiveness in deep layers or with smooth activations like Tanh. We propose a ``soft sparsity'' paradigm using a hardware efficient Most Significant Bit (MSB) proxy to skip negligible non-zero multiplications. Integrated as a custom RISC-V instruction and evaluated on LeNet-5 (MNIST), this method reduces ReLU MACs by 88.42% and Tanh MACs by 74.87% with zero accuracy loss--outperforming zero-skipping by 5x. By clock-gating inactive multipliers, we estimate power savings of 35.2\% for ReLU and 29.96\% for Tanh. While memory access makes power reduction sub-linear to operation savings, this approach significantl...

---

## 25. CLIPO: 对比 学习 in 策略 优化 Generalizes RLVR

**原标题**: CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR

**作者**: Sijia Cui, Pengyu Cheng, Jiajun Song, Yongbo Gai, Guojun Zhang, Zhechao Yu, Jianhe Lin, Xiaoxi Jiang, Guanjun Jiang
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10101v1

**中文摘要**:
> arXiv:2603.10101v1 Announce Type: new 
摘要: 强化 学习 with Verifiable Rewards (RLVR) has significantly advanced the 推理 capacity of Large Language Models (LLMs). However, RLVR solely relies on final answers as outcome rewards, neglecting the correctness of intermediate 推理 steps. 训练 on these process-wrong but outcome-correct rollouts can lead to hallucination and answer-copying, severely undermining the 模型's 泛化 and 鲁棒性. To address this, we incorporate a 对比 学习 mechanism into the 策略 优化 (CLIPO) to generalize the RLVR process. By optimizing a 对比 损失 over successful rollouts, CLIPO steers the 大语言模型 to capture the invariant structure shared across correct 推理 paths. This provides a more 鲁棒 cross-轨迹 正则化 than the original single-path supervision in RLVR, effectively mitigating step-level 推理 inconsistencies...

**Original Abstract**:
> arXiv:2603.10101v1 Announce Type: new 
Abstract: Reinforcement Learning with Verifiable Rewards (RLVR) has significantly advanced the reasoning capacity of Large Language Models (LLMs). However, RLVR solely relies on final answers as outcome rewards, neglecting the correctness of intermediate reasoning steps. Training on these process-wrong but outcome-correct rollouts can lead to hallucination and answer-copying, severely undermining the model's generalization and robustness. To address this, we incorporate a Contrastive Learning mechanism into the Policy Optimization (CLIPO) to generalize the RLVR process. By optimizing a contrastive loss over successful rollouts, CLIPO steers the LLM to capture the invariant structure shared across correct reasoning paths. This provides a more robust cr...

---

## 26. Lost in the Middle at Birth: An Exact Theory of Transformer Position 偏见

**原标题**: Lost in the Middle at Birth: An Exact Theory of Transformer Position Bias

**作者**: Borun D Chowdhury
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10123v1

**中文摘要**:
> arXiv:2603.10123v1 Announce Type: new 
摘要: The ``Lost in the Middle'' phenomenon -- a U-shaped 性能 curve where LLMs retrieve well from the beginning and end of a context but fail in the middle -- is widely attributed to learned Softmax artifacts or the distance-decay of positional encodings like RoPE. This 论文 makes a single, precise claim: \emph{the U-shape is already present at initialization, before any 训练 or positional encoding takes effect.} It is an inherent geometric property of the 因果 decoder with residual connections.
  We 模型 multi-layer 因果 注意力 as iterated powers of the Ces\`{a}ro matrix and derive the exact closed-form influence density in the continuous limit. 因果 masking forces a logarithmic divergence of 梯度 influence at the start of the prompt (the Primacy Tail), while residual c...

**Original Abstract**:
> arXiv:2603.10123v1 Announce Type: new 
Abstract: The ``Lost in the Middle'' phenomenon -- a U-shaped performance curve where LLMs retrieve well from the beginning and end of a context but fail in the middle -- is widely attributed to learned Softmax artifacts or the distance-decay of positional encodings like RoPE. This paper makes a single, precise claim: \emph{the U-shape is already present at initialization, before any training or positional encoding takes effect.} It is an inherent geometric property of the causal decoder with residual connections.
  We model multi-layer causal attention as iterated powers of the Ces\`{a}ro matrix and derive the exact closed-form influence density in the continuous limit. Causal masking forces a logarithmic divergence of gradient influence at the start...

---

## 27. A 神经 operator for predicting vibration frequency response curves from limited data

**原标题**: A neural operator for predicting vibration frequency response curves from limited data

**作者**: D. Bluedorn, A. Badawy, B. E. Saunders, D. Roettgen, A. Abdelkefi
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10149v1

**中文摘要**:
> arXiv:2603.10149v1 Announce Type: new 
摘要: In the design of engineered components, rigorous vibration testing is essential for 性能 validation and identification of resonant frequencies and amplitudes encountered during operation. Performing this 评估 numerically via machine 学习 has great potential to accelerate design 迭代 and make testing workflows more 高效. However, dynamical systems are conventionally difficult to solve via machine 学习 methods without using physics-based regularizing 损失 functions. To properly perform this forecasting task, a structure that has an inspectable physical obedience can be devised without the use of regularizing terms from first principles. The 方法 employed in this work is a 神经 operator integrated with an implicit numerical scheme. This 架构 enables operators to learn o...

**Original Abstract**:
> arXiv:2603.10149v1 Announce Type: new 
Abstract: In the design of engineered components, rigorous vibration testing is essential for performance validation and identification of resonant frequencies and amplitudes encountered during operation. Performing this evaluation numerically via machine learning has great potential to accelerate design iteration and make testing workflows more efficient. However, dynamical systems are conventionally difficult to solve via machine learning methods without using physics-based regularizing loss functions. To properly perform this forecasting task, a structure that has an inspectable physical obedience can be devised without the use of regularizing terms from first principles. The method employed in this work is a neural operator integrated with an impl...

---

## 28. Mashup 学习: Faster Finetuning by Remixing Past Checkpoints

**原标题**: Mashup Learning: Faster Finetuning by Remixing Past Checkpoints

**作者**: Sofia Maria Lo Cicero Vaina, Artem Chumachenko, Max Ryabinin
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10156v1

**中文摘要**:
> arXiv:2603.10156v1 Announce Type: new 
摘要: Finetuning on domain-specific data is a well-established 方法 for enhancing 大语言模型 性能 on downstream tasks. 训练 on each 数据集 produces a new set of 模型 weights, resulting in a multitude of checkpoints saved in-house or on open-source platforms. However, these 训练 artifacts are rarely reused for subsequent experiments despite containing improved 模型 abilities for potentially similar tasks. In this 论文, we propose Mashup 学习, a simple 方法 to leverage the outputs of prior 训练 runs to enhance 模型 adaptation to new tasks. Our procedure identifies the most relevant historical checkpoints for a 目标 数据集, aggregates them with 模型 merging, and uses the 结果 as an improved initialization for 训练. Across 8 standard 大语言模型 benchmarks, four models, and two collections of source che...

**Original Abstract**:
> arXiv:2603.10156v1 Announce Type: new 
Abstract: Finetuning on domain-specific data is a well-established method for enhancing LLM performance on downstream tasks. Training on each dataset produces a new set of model weights, resulting in a multitude of checkpoints saved in-house or on open-source platforms. However, these training artifacts are rarely reused for subsequent experiments despite containing improved model abilities for potentially similar tasks. In this paper, we propose Mashup Learning, a simple method to leverage the outputs of prior training runs to enhance model adaptation to new tasks. Our procedure identifies the most relevant historical checkpoints for a target dataset, aggregates them with model merging, and uses the result as an improved initialization for training. ...

---

## 29. 演员-Accelerated 策略 Dual Averaging for 强化 学习 in Continuous 动作 Spaces

**原标题**: Actor-Accelerated Policy Dual Averaging for Reinforcement Learning in Continuous Action Spaces

**作者**: Ji Gao, Caleb Ju, Guanghui Lan, Zhaohui Tong
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10199v1

**中文摘要**:
> arXiv:2603.10199v1 Announce Type: new 
摘要: 策略 Dual Averaging (PDA) offers a principled 策略 Mirror Descent (PMD) 框架 that more naturally admits 价值 function approximation than standard PMD, enabling the use of approximate 优势 (or Q-) functions while retaining strong convergence guarantees. However, applying PDA in continuous 状态 and 动作 spaces remains computationally challenging, since 动作 选择 involves solving an 优化 sub-problem at each 决策 step. In this 论文, we propose \textit{演员-accelerated PDA}, which uses a learned 策略 网络 to approximate the solution of the 优化 sub-problems, yielding faster runtimes while maintaining convergence guarantees. We provide a theoretical analysis that quantifies how 演员 approximation error impacts the convergence of PDA under suitable assumptions. We then evaluate its 性能 on...

**Original Abstract**:
> arXiv:2603.10199v1 Announce Type: new 
Abstract: Policy Dual Averaging (PDA) offers a principled Policy Mirror Descent (PMD) framework that more naturally admits value function approximation than standard PMD, enabling the use of approximate advantage (or Q-) functions while retaining strong convergence guarantees. However, applying PDA in continuous state and action spaces remains computationally challenging, since action selection involves solving an optimization sub-problem at each decision step. In this paper, we propose \textit{actor-accelerated PDA}, which uses a learned policy network to approximate the solution of the optimization sub-problems, yielding faster runtimes while maintaining convergence guarantees. We provide a theoretical analysis that quantifies how actor approximatio...

---

## 30. SiMPO: Measure Matching for 在线 Diffusion 强化 学习

**原标题**: SiMPO: Measure Matching for Online Diffusion Reinforcement Learning

**作者**: Haitong Ma, Chenxiao Gao, Tianyi Chen, Na Li, Bo Dai
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10250v1

**中文摘要**:
> arXiv:2603.10250v1 Announce Type: new 
摘要: A commonly used family of RL algorithms for diffusion policies conducts softmax reweighting over the behavior 策略, which usually induces an over-greedy 策略 and fails to leverage feedback from negative samples. In this work, we introduce Signed Measure 策略 优化 (SiMPO), a simple and unified 框架 that generalizes reweighting scheme in diffusion RL with general monotonic functions. SiMPO revisits diffusion RL via a two-stage measure matching lens. First, we construct a virtual 目标 策略 by $f$-divergence regularized 策略 优化, where we can relax the non-negativity constraint to allow for a signed 目标 measure. Second, we use this signed measure to guide diffusion or flow models through reweighted matching. This formulation offers two key advantages: a) it generalizes...

**Original Abstract**:
> arXiv:2603.10250v1 Announce Type: new 
Abstract: A commonly used family of RL algorithms for diffusion policies conducts softmax reweighting over the behavior policy, which usually induces an over-greedy policy and fails to leverage feedback from negative samples. In this work, we introduce Signed Measure Policy Optimization (SiMPO), a simple and unified framework that generalizes reweighting scheme in diffusion RL with general monotonic functions. SiMPO revisits diffusion RL via a two-stage measure matching lens. First, we construct a virtual target policy by $f$-divergence regularized policy optimization, where we can relax the non-negativity constraint to allow for a signed target measure. Second, we use this signed measure to guide diffusion or flow models through reweighted matching. ...

---

## 31. Improving TabPFN's Synthetic Data 生成 by Integrating 因果 Structure

**原标题**: Improving TabPFN's Synthetic Data Generation by Integrating Causal Structure

**作者**: Davide Tugnoli, Andrea De Lorenzo, Marco Virgolin, Giovanni Cin\`a
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10254v1

**中文摘要**:
> arXiv:2603.10254v1 Announce Type: new 
摘要: Synthetic tabular data 生成 addresses data scarcity and 隐私 constraints in a variety of domains. Tabular Prior-Data Fitted 网络 (TabPFN), a recent foundation 模型 for tabular data, has been shown capable of generating high-quality synthetic tabular data. However, TabPFN is autoregressive: features are generated sequentially by conditioning on the previous ones, depending on the order in which they appear in the input data. We demonstrate that when the 特征 order conflicts with 因果 structure, the 模型 produces spurious correlations that impair its ability to generate synthetic data and preserve 因果 effects. We address this limitation by integrating 因果 structure into TabPFN's 生成 process through two complementary approaches: Directed Acyclic Graph (DAG)-aware con...

**Original Abstract**:
> arXiv:2603.10254v1 Announce Type: new 
Abstract: Synthetic tabular data generation addresses data scarcity and privacy constraints in a variety of domains. Tabular Prior-Data Fitted Network (TabPFN), a recent foundation model for tabular data, has been shown capable of generating high-quality synthetic tabular data. However, TabPFN is autoregressive: features are generated sequentially by conditioning on the previous ones, depending on the order in which they appear in the input data. We demonstrate that when the feature order conflicts with causal structure, the model produces spurious correlations that impair its ability to generate synthetic data and preserve causal effects. We address this limitation by integrating causal structure into TabPFN's generation process through two complemen...

---

## 32. Discovery of a Hematopoietic Manifold in scGPT Yields a 方法 for Extracting Performant Algorithms from Biological Foundation 模型 Internals

**原标题**: Discovery of a Hematopoietic Manifold in scGPT Yields a Method for Extracting Performant Algorithms from Biological Foundation Model Internals

**作者**: Ihor Kendiukhov
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10261v1

**中文摘要**:
> arXiv:2603.10261v1 Announce Type: new 
摘要: We report the discovery and extraction of a compact hematopoietic 算法 from the single-cell foundation 模型 scGPT, to our knowledge the first biologically useful, competitive 算法 extracted from a foundation 模型 via mechanistic interpretability. We show that scGPT internally encodes a compact hematopoietic manifold with significant developmental branch structure, validated on a strict non-overlap Tabula Sapiens external panel and confirmed via frozen-head 零样本 transfer to an independent multi-donor immune panel. To isolate this geometry, we introduce a general three-stage extraction 方法 consisting of direct operator export from frozen 注意力 weights, a lightweight learned adaptor, and a task-specific readout, producing a standalone 算法 without 目标-数据集 retrainin...

**Original Abstract**:
> arXiv:2603.10261v1 Announce Type: new 
Abstract: We report the discovery and extraction of a compact hematopoietic algorithm from the single-cell foundation model scGPT, to our knowledge the first biologically useful, competitive algorithm extracted from a foundation model via mechanistic interpretability. We show that scGPT internally encodes a compact hematopoietic manifold with significant developmental branch structure, validated on a strict non-overlap Tabula Sapiens external panel and confirmed via frozen-head zero-shot transfer to an independent multi-donor immune panel. To isolate this geometry, we introduce a general three-stage extraction method consisting of direct operator export from frozen attention weights, a lightweight learned adaptor, and a task-specific readout, producin...

---

## 33. Estimating condition number with Graph 神经 Networks

**原标题**: Estimating condition number with Graph Neural Networks

**作者**: Erin Carson, Xinye Chen
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10277v1

**中文摘要**:
> arXiv:2603.10277v1 Announce Type: new 
摘要: In this 论文, we propose a fast 方法 for estimating the condition number of sparse matrices using graph 神经 networks (GNNs). To enable 高效 训练 and 推理 of GNNs, our proposed 特征 engineering for GNNs achieves $\mathrm{O}(\mathrm{nnz} + n)$, where $\mathrm{nnz}$ is the number of non-zero elements in the matrix and $n$ denotes the matrix dimension. We propose two prediction schemes for estimating the matrix condition number using GNNs. The extensive experiments for the two schemes are conducted for 1-norm and 2-norm condition number estimation, which show that our 方法 achieves a significant speedup over the Hager-Higham and Lanczos methods.

**Original Abstract**:
> arXiv:2603.10277v1 Announce Type: new 
Abstract: In this paper, we propose a fast method for estimating the condition number of sparse matrices using graph neural networks (GNNs). To enable efficient training and inference of GNNs, our proposed feature engineering for GNNs achieves $\mathrm{O}(\mathrm{nnz} + n)$, where $\mathrm{nnz}$ is the number of non-zero elements in the matrix and $n$ denotes the matrix dimension. We propose two prediction schemes for estimating the matrix condition number using GNNs. The extensive experiments for the two schemes are conducted for 1-norm and 2-norm condition number estimation, which show that our method achieves a significant speedup over the Hager-Higham and Lanczos methods.

---

## 34. 鲁棒 Post-训练 for 生成式 Recommenders: Why Exponential 奖励-Weighted SFT Outperforms RLHF

**原标题**: Robust Post-Training for Generative Recommenders: Why Exponential Reward-Weighted SFT Outperforms RLHF

**作者**: Keertana Chidambaram, Sanath Kumar Krishnamurthy, Qiuling Xu, Ko-Jen Hsiao, Moumita Bhattacharya
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10279v1

**中文摘要**:
> arXiv:2603.10279v1 Announce Type: new 
摘要: Aligning 生成式 recommender systems to user preferences via post-训练 is critical for closing the gap between next-item prediction and actual 推荐 quality. Existing post-训练 methods are ill-suited for production-scale systems: RLHF methods 奖励 hack due to noisy user feedback and unreliable 奖励 models, 离线 RL alternatives require propensity scores that are unavailable, and 在线 interaction is infeasible. We identify exponential 奖励-weighted SFT with weights $w = \exp(r/\lambda)$ as uniquely suited to this setting, and provide the theoretical and empirical foundations that explain why. By optimizing directly on observed rewards without querying a learned 奖励 模型, the 方法 is immune to 奖励 hacking, requires no propensity scores, and is fully 离线. We prove the first 策略 i...

**Original Abstract**:
> arXiv:2603.10279v1 Announce Type: new 
Abstract: Aligning generative recommender systems to user preferences via post-training is critical for closing the gap between next-item prediction and actual recommendation quality. Existing post-training methods are ill-suited for production-scale systems: RLHF methods reward hack due to noisy user feedback and unreliable reward models, offline RL alternatives require propensity scores that are unavailable, and online interaction is infeasible. We identify exponential reward-weighted SFT with weights $w = \exp(r/\lambda)$ as uniquely suited to this setting, and provide the theoretical and empirical foundations that explain why. By optimizing directly on observed rewards without querying a learned reward model, the method is immune to reward hacking...

---

## 35. Taming Score-Based Denoisers in ADMM: A Convergent Plug-and-Play 框架

**原标题**: Taming Score-Based Denoisers in ADMM: A Convergent Plug-and-Play Framework

**作者**: Rajesh Shrestha, Xiao Fu
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10281v1

**中文摘要**:
> arXiv:2603.10281v1 Announce Type: new 
摘要: While score-based 生成式 models have emerged as powerful priors for solving inverse problems, directly integrating them into 优化 algorithms such as ADMM remains nontrivial. Two central challenges arise: i) the mismatch between the noisy data manifolds used to train the score functions and the geometry of ADMM iterates, especially due to the influence of dual variables, and ii) the lack of convergence understanding when ADMM is equipped with score-based denoisers. To address the manifold mismatch issue, we propose ADMM plug-and-play (ADMM-PnP) with the AC-DC denoiser, a new 框架 that embeds a three-stage denoiser into ADMM: (1) auto-correction (AC) via additive Gaussian noise, (2) directional correction (DC) using conditional Langevin dynamics, and (3) s...

**Original Abstract**:
> arXiv:2603.10281v1 Announce Type: new 
Abstract: While score-based generative models have emerged as powerful priors for solving inverse problems, directly integrating them into optimization algorithms such as ADMM remains nontrivial. Two central challenges arise: i) the mismatch between the noisy data manifolds used to train the score functions and the geometry of ADMM iterates, especially due to the influence of dual variables, and ii) the lack of convergence understanding when ADMM is equipped with score-based denoisers. To address the manifold mismatch issue, we propose ADMM plug-and-play (ADMM-PnP) with the AC-DC denoiser, a new framework that embeds a three-stage denoiser into ADMM: (1) auto-correction (AC) via additive Gaussian noise, (2) directional correction (DC) using conditiona...

---

## 36. GSVD for Geometry-Grounded 数据集 Comparison: An Alignment Angle Is All You Need

**原标题**: GSVD for Geometry-Grounded Dataset Comparison: An Alignment Angle Is All You Need

**作者**: Eduarda de Souza Marques, Arthur Sobrinho Ferreira da Rocha, Joao Paixao, Heudson Mirandola, Daniel Sadoc Menasche
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10283v1

**中文摘要**:
> arXiv:2603.10283v1 Announce Type: new 
摘要: Geometry-grounded 学习 asks models to respect structure in the problem domain rather than treating observations as arbitrary vectors. Motivated by this view, we revisit a classical but underused primitive for comparing datasets: linear relations between two data matrices, expressed via the co-span constraint $Ax = By = z$ in a shared ambient space. To operationalize this comparison, we use the generalized singular 价值 decomposition (GSVD) as a joint coordinate 系统 for two subspaces. In particular, we exploit the GSVD form $A = HCU$, $B = HSV$ with $C^{\top}C + S^{\top}S = I$, which separates shared versus 数据集-specific directions through the diagonal structure of $(C, S)$. From these factors we derive an 可解释 *angle score* $\theta(z) \in [0, \pi/2]$ for...

**Original Abstract**:
> arXiv:2603.10283v1 Announce Type: new 
Abstract: Geometry-grounded learning asks models to respect structure in the problem domain rather than treating observations as arbitrary vectors. Motivated by this view, we revisit a classical but underused primitive for comparing datasets: linear relations between two data matrices, expressed via the co-span constraint $Ax = By = z$ in a shared ambient space. To operationalize this comparison, we use the generalized singular value decomposition (GSVD) as a joint coordinate system for two subspaces. In particular, we exploit the GSVD form $A = HCU$, $B = HSV$ with $C^{\top}C + S^{\top}S = I$, which separates shared versus dataset-specific directions through the diagonal structure of $(C, S)$. From these factors we derive an interpretable *angle scor...

---

## 37. Copula-ResLogit: A 深度-Copula 框架 for Unobserved Confounding Effects

**原标题**: Copula-ResLogit: A Deep-Copula Framework for Unobserved Confounding Effects

**作者**: Kimia Kamal, Bilal Farooq
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10284v1

**中文摘要**:
> arXiv:2603.10284v1 Announce Type: new 
摘要: A key challenge in travel demand analysis is the presence of unobserved factors that may generate non-因果 dependencies, obscuring the true 因果 effects. To address the issue, the study introduces a novel 深度 学习 based fully 可解释 joint modelling 框架, Copula-ResLogit, which integrates the flexibility of Residual 神经 网络 (ResNet) architectures with the dependence capturing capabilities of copula models. This hybrid structure enables us to first detect unobserved confounding through traditional copula function based joint modelling and then mitigate these hidden associations by incorporating 深度 学习 components. The study applies this 框架 to two case studies, including the relationship between stress levels and wait time of pedestrians when crossing mid block in V...

**Original Abstract**:
> arXiv:2603.10284v1 Announce Type: new 
Abstract: A key challenge in travel demand analysis is the presence of unobserved factors that may generate non-causal dependencies, obscuring the true causal effects. To address the issue, the study introduces a novel deep learning based fully interpretable joint modelling framework, Copula-ResLogit, which integrates the flexibility of Residual Neural Network (ResNet) architectures with the dependence capturing capabilities of copula models. This hybrid structure enables us to first detect unobserved confounding through traditional copula function based joint modelling and then mitigate these hidden associations by incorporating deep learning components. The study applies this framework to two case studies, including the relationship between stress l...

---

## 38. Regime-aware financial volatility forecasting via in-context 学习

**原标题**: Regime-aware financial volatility forecasting via in-context learning

**作者**: Saba Asaad, Shayan Mohajer Hamidi, Ali Bereyhi
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10299v1

**中文摘要**:
> arXiv:2603.10299v1 Announce Type: new 
摘要: This work introduces a regime-aware in-context 学习 框架 that leverages large language models (LLMs) for financial volatility forecasting under nonstationary market conditions. The proposed 方案 deploys pretrained LLMs to reason over historical volatility patterns and adjust their predictions without parameter fine-tuning. We develop an oracle-guided refinement procedure that constructs regime-aware demonstrations from 训练 data. An 大语言模型 is then deployed as an in-context learner that predicts the next-step volatility from the input sequence using demonstrations sampled conditional to the estimated market label. This conditional 采样 strategy enables the 大语言模型 to adapt its predictions to regime-dependent volatility dynamics through contextual 推理 alone. Expe...

**Original Abstract**:
> arXiv:2603.10299v1 Announce Type: new 
Abstract: This work introduces a regime-aware in-context learning framework that leverages large language models (LLMs) for financial volatility forecasting under nonstationary market conditions. The proposed approach deploys pretrained LLMs to reason over historical volatility patterns and adjust their predictions without parameter fine-tuning. We develop an oracle-guided refinement procedure that constructs regime-aware demonstrations from training data. An LLM is then deployed as an in-context learner that predicts the next-step volatility from the input sequence using demonstrations sampled conditional to the estimated market label. This conditional sampling strategy enables the LLM to adapt its predictions to regime-dependent volatility dynamics ...

---

## 39. What do near-optimal 学习 rate schedules look like?

**原标题**: What do near-optimal learning rate schedules look like?

**作者**: Hiroki Naganuma, Atish Agarwala, Priya Kasimbeg, George E. Dahl
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10301v1

**中文摘要**:
> arXiv:2603.10301v1 Announce Type: new 
摘要: A basic unanswered question in 神经 网络 训练 is: what is the best 学习 rate schedule shape for a given workload? The choice of 学习 rate schedule is a key factor in the success or failure of the 训练 process, but beyond having some kind of warmup and decay, there is no consensus on what makes a good schedule shape. To answer this question, we designed a 搜索 procedure to find the best shapes within a parameterized schedule family. Our 方案 factors out the schedule shape from the base 学习 rate, which otherwise would dominate cross-schedule comparisons. We applied our 搜索 procedure to a variety of schedule families on three workloads: linear regression, 图像 分类 on CIFAR-10, and small-scale language modeling on Wikitext103. We showed that our 搜索 procedure indeed genera...

**Original Abstract**:
> arXiv:2603.10301v1 Announce Type: new 
Abstract: A basic unanswered question in neural network training is: what is the best learning rate schedule shape for a given workload? The choice of learning rate schedule is a key factor in the success or failure of the training process, but beyond having some kind of warmup and decay, there is no consensus on what makes a good schedule shape. To answer this question, we designed a search procedure to find the best shapes within a parameterized schedule family. Our approach factors out the schedule shape from the base learning rate, which otherwise would dominate cross-schedule comparisons. We applied our search procedure to a variety of schedule families on three workloads: linear regression, image classification on CIFAR-10, and small-scale langu...

---

## 40. How to make the most of your masked language 模型 for protein engineering

**原标题**: How to make the most of your masked language model for protein engineering

**作者**: Calvin McCarter, Nick Bhattacharya, Sebastian W. Ober, Hunter Elliott
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10302v1

**中文摘要**:
> arXiv:2603.10302v1 Announce Type: new 
摘要: A plethora of protein language models have been released in recent years. Yet comparatively little work has addressed how to best sample from them to optimize desired biological properties. We fill this gap by proposing a flexible, effective 采样 方法 for masked language models (MLMs), and by systematically evaluating models and methods both in silico and in vitro on actual antibody therapeutics campaigns. Firstly, we propose 采样 with stochastic beam 搜索, exploiting the fact that MLMs are remarkably 高效 at evaluating the pseudo-perplexity of the entire 1-edit neighborhood of a sequence. Reframing 生成 in terms of entire-sequence 评估 enables flexible guidance with multiple 优化 objectives. Secondly, we report results from our extensive in vitro head-to-head 评估...

**Original Abstract**:
> arXiv:2603.10302v1 Announce Type: new 
Abstract: A plethora of protein language models have been released in recent years. Yet comparatively little work has addressed how to best sample from them to optimize desired biological properties. We fill this gap by proposing a flexible, effective sampling method for masked language models (MLMs), and by systematically evaluating models and methods both in silico and in vitro on actual antibody therapeutics campaigns. Firstly, we propose sampling with stochastic beam search, exploiting the fact that MLMs are remarkably efficient at evaluating the pseudo-perplexity of the entire 1-edit neighborhood of a sequence. Reframing generation in terms of entire-sequence evaluation enables flexible guidance with multiple optimization objectives. Secondly, we...

---

## 41. Data-Driven Integration Kernels for 可解释 Nonlocal Operator 学习

**原标题**: Data-Driven Integration Kernels for Interpretable Nonlocal Operator Learning

**作者**: Savannah L. Ferretti, Jerry Lin, Sara Shamekh, Jane W. Baldwin, Michael S. Pritchard, Tom Beucler
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10305v1

**中文摘要**:
> arXiv:2603.10305v1 Announce Type: new 
摘要: Machine 学习 models can represent climate processes that are nonlocal in horizontal space, height, and time, often by combining information across these dimensions in highly nonlinear ways. While this can improve predictive skill, it makes learned relationships difficult to interpret and prone to overfitting as the extent of nonlocal information grows. We address this challenge by introducing data-driven integration kernels, a 框架 that adds structure to nonlocal operator 学习 by explicitly separating nonlocal information aggregation from local nonlinear prediction. Each spatiotemporal predictor field is first integrated using learnable kernels (defined as continuous weighting functions over horizontal space, height, and/or time), after which a local no...

**Original Abstract**:
> arXiv:2603.10305v1 Announce Type: new 
Abstract: Machine learning models can represent climate processes that are nonlocal in horizontal space, height, and time, often by combining information across these dimensions in highly nonlinear ways. While this can improve predictive skill, it makes learned relationships difficult to interpret and prone to overfitting as the extent of nonlocal information grows. We address this challenge by introducing data-driven integration kernels, a framework that adds structure to nonlocal operator learning by explicitly separating nonlocal information aggregation from local nonlinear prediction. Each spatiotemporal predictor field is first integrated using learnable kernels (defined as continuous weighting functions over horizontal space, height, and/or time...

---

## 42. Federated Active 学习 Under Extreme Non-IID and Global Class Imbalance

**原标题**: Federated Active Learning Under Extreme Non-IID and Global Class Imbalance

**作者**: Chen-Chen Zong, Sheng-Jun Huang
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10341v1

**中文摘要**:
> arXiv:2603.10341v1 Announce Type: new 
摘要: Federated active 学习 (FAL) seeks to reduce annotation cost under 隐私 constraints, yet its effectiveness degrades in realistic settings with severe global class imbalance and highly heterogeneous clients. We conduct a systematic study of query-模型 选择 in FAL and uncover a central insight: the 模型 that achieves more class-balanced 采样, especially for minority classes, consistently leads to better final 性能. Moreover, global-模型 querying is beneficial only when the global distribution is highly imbalanced and 客户端 data are relatively homogeneous; otherwise, the local 模型 is preferable. Based on these findings, we propose FairFAL, an adaptive class-fair FAL 框架. FairFAL (1) infers global imbalance and local-global divergence via lightweight prediction discrepanc...

**Original Abstract**:
> arXiv:2603.10341v1 Announce Type: new 
Abstract: Federated active learning (FAL) seeks to reduce annotation cost under privacy constraints, yet its effectiveness degrades in realistic settings with severe global class imbalance and highly heterogeneous clients. We conduct a systematic study of query-model selection in FAL and uncover a central insight: the model that achieves more class-balanced sampling, especially for minority classes, consistently leads to better final performance. Moreover, global-model querying is beneficial only when the global distribution is highly imbalanced and client data are relatively homogeneous; otherwise, the local model is preferable. Based on these findings, we propose FairFAL, an adaptive class-fair FAL framework. FairFAL (1) infers global imbalance and ...

---

## 43. 因果 Concept Graphs in 大语言模型 隐变量 Space for Stepwise 推理

**原标题**: Causal Concept Graphs in LLM Latent Space for Stepwise Reasoning

**作者**: Md Muntaqim Meherab, Noor Islam S. Mohammad, Faiza Feroz
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10377v1

**中文摘要**:
> arXiv:2603.10377v1 Announce Type: new 
摘要: Sparse autoencoders can localize where concepts live in language models, but not how they interact during multi-step 推理. We propose 因果 Concept Graphs (CCG): a directed acyclic graph over sparse, 可解释 隐变量 features, where edges capture learned 因果 dependencies between concepts. We combine task-conditioned sparse autoencoders for concept discovery with DAGMA-style differentiable structure 学习 for graph recovery and introduce the 因果 Fidelity Score (CFS) to evaluate whether graph-guided interventions induce larger downstream effects than random ones. On ARC-Challenge, StrategyQA, and LogiQA with GPT-2 Medium, across five seeds ($n{=}15$ paired runs), CCG achieves $\CFS=5.654\pm0.625$, outperforming ROME-style tracing ($3.382\pm0.233$), SAE-only ranking ($...

**Original Abstract**:
> arXiv:2603.10377v1 Announce Type: new 
Abstract: Sparse autoencoders can localize where concepts live in language models, but not how they interact during multi-step reasoning. We propose Causal Concept Graphs (CCG): a directed acyclic graph over sparse, interpretable latent features, where edges capture learned causal dependencies between concepts. We combine task-conditioned sparse autoencoders for concept discovery with DAGMA-style differentiable structure learning for graph recovery and introduce the Causal Fidelity Score (CFS) to evaluate whether graph-guided interventions induce larger downstream effects than random ones. On ARC-Challenge, StrategyQA, and LogiQA with GPT-2 Medium, across five seeds ($n{=}15$ paired runs), CCG achieves $\CFS=5.654\pm0.625$, outperforming ROME-style tr...

---

## 44. Optimal Expert-注意力 Allocation in Mixture-of-Experts: A 可扩展 Law for 动态 模型 Design

**原标题**: Optimal Expert-Attention Allocation in Mixture-of-Experts: A Scalable Law for Dynamic Model Design

**作者**: Junzhuo Li, Peijie Jiang, Changxin Tian, Jia Liu, Zhiqiang Zhang, Xuming Hu
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10379v1

**中文摘要**:
> arXiv:2603.10379v1 Announce Type: new 
摘要: This 论文 presents a novel extension of 神经 scaling laws to Mixture-of-Experts (MoE) models, focusing on the optimal allocation of compute between expert and 注意力 sub-layers. As MoE architectures have emerged as an 高效 方法 for scaling 模型 capacity without proportionally increasing computation, determining the optimal expert-注意力 compute ratio becomes critical. We define the ratio $r$ as the fraction of total FLOPs per token dedicated to the expert layers versus the 注意力 layers, and explore how this ratio interacts with the overall compute budget and 模型 sparsity. Through extensive experiments with GPT-style MoE Transformers, we empirically find that the optimal ratio $r^*$ follows a power-law relationship with total compute and varies with sparsity. Our ana...

**Original Abstract**:
> arXiv:2603.10379v1 Announce Type: new 
Abstract: This paper presents a novel extension of neural scaling laws to Mixture-of-Experts (MoE) models, focusing on the optimal allocation of compute between expert and attention sub-layers. As MoE architectures have emerged as an efficient method for scaling model capacity without proportionally increasing computation, determining the optimal expert-attention compute ratio becomes critical. We define the ratio $r$ as the fraction of total FLOPs per token dedicated to the expert layers versus the attention layers, and explore how this ratio interacts with the overall compute budget and model sparsity. Through extensive experiments with GPT-style MoE Transformers, we empirically find that the optimal ratio $r^*$ follows a power-law relationship with...

---

## 45. Variance-Aware Adaptive Weighting for Diffusion 模型 训练

**原标题**: Variance-Aware Adaptive Weighting for Diffusion Model Training

**作者**: Nanlong Sun, Lei Shi
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10391v1

**中文摘要**:
> arXiv:2603.10391v1 Announce Type: new 
摘要: Diffusion models have recently achieved remarkable success in 生成式 modeling, yet their 训练 dynamics across different noise levels remain highly imbalanced, which can lead to inefficient 优化 and unstable 学习 behavior. In this work, we investigate this imbalance from the perspective of 损失 variance across log-SNR levels and propose a variance-aware adaptive weighting strategy to address it. The proposed 方案 dynamically adjusts 训练 weights based on the observed variance distribution, encouraging a more balanced 优化 process across noise levels. Extensive experiments on CIFAR-10 and CIFAR-100 demonstrate that the proposed 方法 consistently improves 生成式 性能 over standard 训练 schemes, achieving lower Fr\'echet Inception Distance (FID) while also reducing 性能 variance...

**Original Abstract**:
> arXiv:2603.10391v1 Announce Type: new 
Abstract: Diffusion models have recently achieved remarkable success in generative modeling, yet their training dynamics across different noise levels remain highly imbalanced, which can lead to inefficient optimization and unstable learning behavior. In this work, we investigate this imbalance from the perspective of loss variance across log-SNR levels and propose a variance-aware adaptive weighting strategy to address it. The proposed approach dynamically adjusts training weights based on the observed variance distribution, encouraging a more balanced optimization process across noise levels. Extensive experiments on CIFAR-10 and CIFAR-100 demonstrate that the proposed method consistently improves generative performance over standard training scheme...

---

## 46. Graph-GRPO: 训练 Graph Flow Models with 强化 学习

**原标题**: Graph-GRPO: Training Graph Flow Models with Reinforcement Learning

**作者**: Baoheng Zhu, Deyu Bo, Delvin Ce Zhang, Xiao Wang
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10395v1

**中文摘要**:
> arXiv:2603.10395v1 Announce Type: new 
摘要: Graph 生成 is a fundamental task with broad applications, such as drug discovery. Recently, discrete flow matching-based graph 生成, \aka, graph flow 模型 (GFM), has emerged due to its superior 性能 and flexible 采样. However, effectively aligning GFMs with complex human preferences or task-specific objectives remains a significant challenge. In this 论文, we propose Graph-GRPO, an 在线 强化 学习 (RL) 框架 for 训练 GFMs under verifiable rewards. Our 方法 makes two key contributions: (1) We derive an analytical expression for the 转移 probability of GFMs, replacing the Monte Carlo 采样 and enabling fully differentiable rollouts for RL 训练; (2) We propose a refinement strategy that randomly perturbs specific nodes and edges in a graph, and regenerates them, allowing for localiz...

**Original Abstract**:
> arXiv:2603.10395v1 Announce Type: new 
Abstract: Graph generation is a fundamental task with broad applications, such as drug discovery. Recently, discrete flow matching-based graph generation, \aka, graph flow model (GFM), has emerged due to its superior performance and flexible sampling. However, effectively aligning GFMs with complex human preferences or task-specific objectives remains a significant challenge. In this paper, we propose Graph-GRPO, an online reinforcement learning (RL) framework for training GFMs under verifiable rewards. Our method makes two key contributions: (1) We derive an analytical expression for the transition probability of GFMs, replacing the Monte Carlo sampling and enabling fully differentiable rollouts for RL training; (2) We propose a refinement strategy t...

---

## 47. On the 学习 Dynamics of Two-layer Linear Networks with Label Noise SGD

**原标题**: On the Learning Dynamics of Two-layer Linear Networks with Label Noise SGD

**作者**: Tongcheng Zhang, Zhanpeng Zhou, Mingze Wang, Andi Han, Wei Huang, Taiji Suzuki, Junchi Yan
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10397v1

**中文摘要**:
> arXiv:2603.10397v1 Announce Type: new 
摘要: One crucial factor behind the success of 深度 学习 lies in the implicit 偏见 induced by noise inherent in 梯度-based 训练 algorithms. Motivated by empirical observations that 训练 with noisy labels improves 模型 泛化, we delve into the underlying mechanisms behind stochastic 梯度 descent (SGD) with label noise. Focusing on a two-layer over-parameterized linear 网络, we analyze the 学习 dynamics of label noise SGD, unveiling a two-phase 学习 behavior. In \emph{Phase I}, the magnitudes of 模型 weights progressively diminish, and the 模型 escapes the lazy regime; enters the rich regime. In \emph{Phase II}, the alignment between 模型 weights and the ground-truth interpolator increases, and the 模型 eventually converges. Our analysis highlights the critical 角色 of label noise in drivi...

**Original Abstract**:
> arXiv:2603.10397v1 Announce Type: new 
Abstract: One crucial factor behind the success of deep learning lies in the implicit bias induced by noise inherent in gradient-based training algorithms. Motivated by empirical observations that training with noisy labels improves model generalization, we delve into the underlying mechanisms behind stochastic gradient descent (SGD) with label noise. Focusing on a two-layer over-parameterized linear network, we analyze the learning dynamics of label noise SGD, unveiling a two-phase learning behavior. In \emph{Phase I}, the magnitudes of model weights progressively diminish, and the model escapes the lazy regime; enters the rich regime. In \emph{Phase II}, the alignment between model weights and the ground-truth interpolator increases, and the model e...

---

## 48. Designing Service Systems from Textual Evidence

**原标题**: Designing Service Systems from Textual Evidence

**作者**: Ruicheng Ao, Hongyu Chen, Siyang Gao, Hanwei Li, David Simchi-Levi
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10400v1

**中文摘要**:
> arXiv:2603.10400v1 Announce Type: new 
摘要: Designing service systems requires selecting among alternative configurations -- choosing the best chatbot variant, the optimal routing 策略, or the most effective quality 控制 procedure. In many service systems, the primary evidence of 性能 quality is textual -- customer support transcripts, complaint narratives, compliance 审稿 reports -- rather than the scalar measurements assumed by classical 优化 methods. Large language models (LLMs) can read such textual evidence and produce standardized quality scores, but these automated judges exhibit systematic biases that vary across alternatives and 评估 instances. Human expert 审稿 remains 准确 but costly. We study how to identify the best service configuration with high confidence while minimizing expensive human au...

**Original Abstract**:
> arXiv:2603.10400v1 Announce Type: new 
Abstract: Designing service systems requires selecting among alternative configurations -- choosing the best chatbot variant, the optimal routing policy, or the most effective quality control procedure. In many service systems, the primary evidence of performance quality is textual -- customer support transcripts, complaint narratives, compliance review reports -- rather than the scalar measurements assumed by classical optimization methods. Large language models (LLMs) can read such textual evidence and produce standardized quality scores, but these automated judges exhibit systematic biases that vary across alternatives and evaluation instances. Human expert review remains accurate but costly. We study how to identify the best service configuration ...

---

## 49. Effective 数据集 Distillation for Spatio-Temporal Forecasting with Bi-dimensional Compression

**原标题**: Effective Dataset Distillation for Spatio-Temporal Forecasting with Bi-dimensional Compression

**作者**: Taehyung Kwon, Yeonje Choi, Yeongho Kim, Kijung Shin
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10410v1

**中文摘要**:
> arXiv:2603.10410v1 Announce Type: new 
摘要: Spatio-temporal time series are widely used in real-world applications, including traffic prediction and weather forecasting. They are sequences of observations over extensive periods and multiple locations, naturally represented as multidimensional data. Forecasting is a central task in spatio-temporal analysis, and numerous 深度 学习 methods have been developed to address it. However, as 数据集 sizes and 模型 complexities continue to grow in practice, 训练 深度 学习 models has become increasingly time- and resource-intensive. A promising solution to this challenge is 数据集 distillation, which synthesizes compact datasets that can effectively replace the original data for 模型 训练. Although successful in various domains, including time series analysis, existing 数据集 ...

**Original Abstract**:
> arXiv:2603.10410v1 Announce Type: new 
Abstract: Spatio-temporal time series are widely used in real-world applications, including traffic prediction and weather forecasting. They are sequences of observations over extensive periods and multiple locations, naturally represented as multidimensional data. Forecasting is a central task in spatio-temporal analysis, and numerous deep learning methods have been developed to address it. However, as dataset sizes and model complexities continue to grow in practice, training deep learning models has become increasingly time- and resource-intensive. A promising solution to this challenge is dataset distillation, which synthesizes compact datasets that can effectively replace the original data for model training. Although successful in various domain...

---

## 50. GGMPs: Generalized Gaussian Mixture Processes

**原标题**: GGMPs: Generalized Gaussian Mixture Processes

**作者**: Vardaan Tekriwal, Mark D. Risser, Hengrui Luo, Marcus M. Noack
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10442v1

**中文摘要**:
> arXiv:2603.10442v1 Announce Type: new 
摘要: Conditional density estimation is complicated by multimodality, heteroscedasticity, and strong non-Gaussianity. Gaussian processes (GPs) provide a principled nonparametric 框架 with calibrated uncertainty, but standard GP regression is limited by its unimodal Gaussian predictive form. We introduce the Generalized Gaussian Mixture Process (GGMP), a GP-based 方法 for multimodal conditional density estimation in settings where each input may be associated with a complex output distribution rather than a single scalar response. GGMP combines local Gaussian mixture fitting, cross-input component alignment and per-component heteroscedastic GP 训练 to produce a closed-form Gaussian mixture predictive density. The 方法 is tractable, compatible with standard GP so...

**Original Abstract**:
> arXiv:2603.10442v1 Announce Type: new 
Abstract: Conditional density estimation is complicated by multimodality, heteroscedasticity, and strong non-Gaussianity. Gaussian processes (GPs) provide a principled nonparametric framework with calibrated uncertainty, but standard GP regression is limited by its unimodal Gaussian predictive form. We introduce the Generalized Gaussian Mixture Process (GGMP), a GP-based method for multimodal conditional density estimation in settings where each input may be associated with a complex output distribution rather than a single scalar response. GGMP combines local Gaussian mixture fitting, cross-input component alignment and per-component heteroscedastic GP training to produce a closed-form Gaussian mixture predictive density. The method is tractable, com...

---

## 51. Unlearning the Unpromptable: Prompt-free Instance Unlearning in Diffusion Models

**原标题**: Unlearning the Unpromptable: Prompt-free Instance Unlearning in Diffusion Models

**作者**: Kyungryeol Lee, Kyeonghyun Lee, Seongmin Hong, Byung Hyun Lee, Se Young Chun
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10445v1

**中文摘要**:
> arXiv:2603.10445v1 Announce Type: new 
摘要: Machine unlearning aims to remove specific outputs from trained models, often at the concept level, such as forgetting all occurrences of a particular celebrity or filtering content via text prompts. However, many undesired outputs, such as an individual's face or generations culturally or factually misinterpreted, cannot often be specified by text prompts. We address this underexplored setting of instance unlearning for outputs that are undesired but unpromptable, where the goal is to forget 目标 outputs selectively while preserving the REST. To this end, we introduce an effective surrogate-based unlearning 方法 that leverages 图像 editing, timestep-aware weighting, and 梯度 surgery to guide trained diffusion models toward forgetting specific outputs. Ex...

**Original Abstract**:
> arXiv:2603.10445v1 Announce Type: new 
Abstract: Machine unlearning aims to remove specific outputs from trained models, often at the concept level, such as forgetting all occurrences of a particular celebrity or filtering content via text prompts. However, many undesired outputs, such as an individual's face or generations culturally or factually misinterpreted, cannot often be specified by text prompts. We address this underexplored setting of instance unlearning for outputs that are undesired but unpromptable, where the goal is to forget target outputs selectively while preserving the rest. To this end, we introduce an effective surrogate-based unlearning method that leverages image editing, timestep-aware weighting, and gradient surgery to guide trained diffusion models toward forgetti...

---

## 52. Spatio-Temporal Forecasting of Retaining Wall Deformation: Mitigating Error Accumulation via Multi-Resolution ConvLSTM Stacking Ensemble

**原标题**: Spatio-Temporal Forecasting of Retaining Wall Deformation: Mitigating Error Accumulation via Multi-Resolution ConvLSTM Stacking Ensemble

**作者**: Jihoon Kim (Department of Civil,Environmental Engineering, Hongik University, Seoul, Republic of Korea), Heejung Youn (Department of Civil,Environmental Engineering, Hongik University, Seoul, Republic of Korea)
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10453v1

**中文摘要**:
> arXiv:2603.10453v1 Announce Type: new 
摘要: This study proposes a multi-resolution Convolutional Long Short-Term 内存 (ConvLSTM) ensemble 框架 that leverages diverse temporal input resolutions to mitigate error accumulation and improve long-视野 forecasting of retaining-structure behavior during staged excavation. An extensive database of lateral wall displacement responses was generated through PLAXIS2D simulations incorporating five-layered soil stratigraphy, two excavation depths (14 and 20 m), and stochastically varied geotechnical and structural parameters, yielding 2,000 time-series deflection profiles. Three ConvLSTM models trained at different input resolutions were integrated using a fully connected 神经 网络 meta-learner to construct the ensemble 模型. Validation using both numerical results ...

**Original Abstract**:
> arXiv:2603.10453v1 Announce Type: new 
Abstract: This study proposes a multi-resolution Convolutional Long Short-Term Memory (ConvLSTM) ensemble framework that leverages diverse temporal input resolutions to mitigate error accumulation and improve long-horizon forecasting of retaining-structure behavior during staged excavation. An extensive database of lateral wall displacement responses was generated through PLAXIS2D simulations incorporating five-layered soil stratigraphy, two excavation depths (14 and 20 m), and stochastically varied geotechnical and structural parameters, yielding 2,000 time-series deflection profiles. Three ConvLSTM models trained at different input resolutions were integrated using a fully connected neural network meta-learner to construct the ensemble model. Valida...

---

## 53. Muscle Synergy Priors Enhance Biomechanical Fidelity in Predictive Musculoskeletal Locomotion Simulation

**原标题**: Muscle Synergy Priors Enhance Biomechanical Fidelity in Predictive Musculoskeletal Locomotion Simulation

**作者**: Ilseung Park (Carnegie Mellon University), Eunsik Choi (Seoul National University), Jangwhan Ahn (UNC-Chapel Hill and NC State University), Jooeun Ahn (Seoul National University)
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10474v1

**中文摘要**:
> arXiv:2603.10474v1 Announce Type: new 
摘要: Human locomotion emerges from high-dimensional neuromuscular 控制, making predictive musculoskeletal simulation challenging. We present a physiology-informed 强化-学习 框架 that constrains 控制 using muscle synergies. We extracted a low-dimensional synergy basis from inverse musculoskeletal analyses of a small set of overground walking trials and used it as the 动作 space for a muscle-driven three-dimensional 模型 trained across variable speeds, slopes and uneven terrain. The resulting controller generated stable gait from 0.7-1.8 m/s and on $\pm$ 6$^{\circ}$ grades and reproduced condition-dependent modulation of joint angles, joint moments and ground reaction forces. Compared with an unconstrained controller, synergy-constrained 控制 reduced non-physiological k...

**Original Abstract**:
> arXiv:2603.10474v1 Announce Type: new 
Abstract: Human locomotion emerges from high-dimensional neuromuscular control, making predictive musculoskeletal simulation challenging. We present a physiology-informed reinforcement-learning framework that constrains control using muscle synergies. We extracted a low-dimensional synergy basis from inverse musculoskeletal analyses of a small set of overground walking trials and used it as the action space for a muscle-driven three-dimensional model trained across variable speeds, slopes and uneven terrain. The resulting controller generated stable gait from 0.7-1.8 m/s and on $\pm$ 6$^{\circ}$ grades and reproduced condition-dependent modulation of joint angles, joint moments and ground reaction forces. Compared with an unconstrained controller, syn...

---

## 54. World 模型 for Battery Degradation Prediction Under Non-Stationary Aging

**原标题**: World Model for Battery Degradation Prediction Under Non-Stationary Aging

**作者**: Kai Chin Lim, Khay Wai See
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10527v1

**中文摘要**:
> arXiv:2603.10527v1 Announce Type: new 
摘要: Degradation prognosis for lithium-ion cells requires forecasting the 状态-of-health (SOH) 轨迹 over future cycles. Existing data-driven approaches can produce 轨迹 outputs through direct regression, but lack a mechanism to propagate degradation dynamics 前向 in time. This 论文 formulates battery degradation prognosis as a world 模型 problem, encoding raw voltage, current, and temperature time-series from each cycle into a 隐变量 状态 and propagating it 前向 via a learned dynamics 转移 to produce a future 轨迹 spanning 80 cycles. To investigate whether electrochemical knowledge improves the learned dynamics, a Single Particle 模型 (SPM) constraint is incorporated into the 训练 损失. Three configurations are evaluated on the Severson LiFePO4 (LFP) 数据集 of 138 cells. Iterative ro...

**Original Abstract**:
> arXiv:2603.10527v1 Announce Type: new 
Abstract: Degradation prognosis for lithium-ion cells requires forecasting the state-of-health (SOH) trajectory over future cycles. Existing data-driven approaches can produce trajectory outputs through direct regression, but lack a mechanism to propagate degradation dynamics forward in time. This paper formulates battery degradation prognosis as a world model problem, encoding raw voltage, current, and temperature time-series from each cycle into a latent state and propagating it forward via a learned dynamics transition to produce a future trajectory spanning 80 cycles. To investigate whether electrochemical knowledge improves the learned dynamics, a Single Particle Model (SPM) constraint is incorporated into the training loss. Three configurations ...

---

## 55. UAV-MARL: Multi-智能体 强化 学习 for Time-Critical and 动态 Medical Supply Delivery

**原标题**: UAV-MARL: Multi-Agent Reinforcement Learning for Time-Critical and Dynamic Medical Supply Delivery

**作者**: Islam Guven, Mehmet Parlak
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10528v1

**中文摘要**:
> arXiv:2603.10528v1 Announce Type: new 
摘要: Unmanned aerial vehicles (UAVs) are increasingly used to support time-critical medical supply delivery, providing rapid and flexible logistics during emergencies and resource shortages. However, effective 部署 of UAV fleets requires coordination mechanisms capable of prioritizing medical requests, allocating limited aerial resources, and adapting delivery schedules under uncertain operational conditions. This 论文 presents a multi-智能体 强化 学习 (MARL) 框架 for coordinating UAV fleets in stochastic medical delivery scenarios where requests vary in urgency, location, and delivery deadlines. The problem is formulated as a partially observable Markov 决策 process (POMDP) in which UAV agents maintain awareness of medical delivery demands while having limited visib...

**Original Abstract**:
> arXiv:2603.10528v1 Announce Type: new 
Abstract: Unmanned aerial vehicles (UAVs) are increasingly used to support time-critical medical supply delivery, providing rapid and flexible logistics during emergencies and resource shortages. However, effective deployment of UAV fleets requires coordination mechanisms capable of prioritizing medical requests, allocating limited aerial resources, and adapting delivery schedules under uncertain operational conditions. This paper presents a multi-agent reinforcement learning (MARL) framework for coordinating UAV fleets in stochastic medical delivery scenarios where requests vary in urgency, location, and delivery deadlines. The problem is formulated as a partially observable Markov decision process (POMDP) in which UAV agents maintain awareness of me...

---

## 56. Tackling Length Inflation Without Trade-offs: Group Relative 奖励 Rescaling for 强化 学习

**原标题**: Tackling Length Inflation Without Trade-offs: Group Relative Reward Rescaling for Reinforcement Learning

**作者**: Zichao Li, Jie Lou, Fangchen Dong, Zhiyuan Fan, Mengjie Ren, Hongyu Lin, Xianpei Han, Debing Zhang, Le Sun, Yaojie Lu, Xing Yu
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10535v1

**中文摘要**:
> arXiv:2603.10535v1 Announce Type: new 
摘要: 强化 学习 significantly enhances 大语言模型 capabilities but suffers from a critical issue: length inflation, where models adopt verbosity or inefficient 推理 to maximize rewards. Prior approaches struggle to address this challenge in a general and lossless manner, primarily because additive penalties introduce a compensatory effect that creates 优化 shortcuts, while heuristic gating strategies lack generality beyond binary feedback. To bridge this gap, we present Group Relative 奖励 Rescaling (GR$^3$), which reframes length 控制 as a multiplicative rescaling paradigm, effectively establishing a generalized, continuous, and 奖励-dependent gating mechanism. To further ensure lossless 优化, we incorporate group-relative 正则化 and 优势-aware calibration, which dynamically ad...

**Original Abstract**:
> arXiv:2603.10535v1 Announce Type: new 
Abstract: Reinforcement learning significantly enhances LLM capabilities but suffers from a critical issue: length inflation, where models adopt verbosity or inefficient reasoning to maximize rewards. Prior approaches struggle to address this challenge in a general and lossless manner, primarily because additive penalties introduce a compensatory effect that creates optimization shortcuts, while heuristic gating strategies lack generality beyond binary feedback. To bridge this gap, we present Group Relative Reward Rescaling (GR$^3$), which reframes length control as a multiplicative rescaling paradigm, effectively establishing a generalized, continuous, and reward-dependent gating mechanism. To further ensure lossless optimization, we incorporate grou...

---

## 57. SCORE: Replacing Layer Stacking with Contractive 循环 Depth

**原标题**: SCORE: Replacing Layer Stacking with Contractive Recurrent Depth

**作者**: Guillaume Godin
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10544v1

**中文摘要**:
> arXiv:2603.10544v1 Announce Type: new 
摘要: Residual connections are central to modern 深度 神经 networks, enabling stable 优化 and 高效 information flow across depth. In this work, we propose SCORE (Skip-Connection ODE 循环 嵌入), a discrete 循环 alternative to classical layer stacking. Instead of composing multiple independent layers, SCORE iteratively applies a single shared 神经 block using an ODE (Ordinary Differential Equation)-inspired contractive update: ht+1 = (1 - dt) * ht + dt * F(ht) This formulation can be interpreted as a depth-by-迭代 refinement process, where the step size dt explicitly controls stability and update magnitude. Unlike continuous 神经 ODE approaches, SCORE uses a fixed number of discrete iterations and standard 反向传播 without requiring ODE solvers or adjoint methods. We evaluate SC...

**Original Abstract**:
> arXiv:2603.10544v1 Announce Type: new 
Abstract: Residual connections are central to modern deep neural networks, enabling stable optimization and efficient information flow across depth. In this work, we propose SCORE (Skip-Connection ODE Recurrent Embedding), a discrete recurrent alternative to classical layer stacking. Instead of composing multiple independent layers, SCORE iteratively applies a single shared neural block using an ODE (Ordinary Differential Equation)-inspired contractive update: ht+1 = (1 - dt) * ht + dt * F(ht) This formulation can be interpreted as a depth-by-iteration refinement process, where the step size dt explicitly controls stability and update magnitude. Unlike continuous Neural ODE approaches, SCORE uses a fixed number of discrete iterations and standard back...

---

## 58. 学习 to Score: Tuning 集群 Schedulers through 强化 学习

**原标题**: Learning to Score: Tuning Cluster Schedulers through Reinforcement Learning

**作者**: Martin Asenov, Qiwen Deng, Gingfung Yeung, Adam Barker
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10545v1

**中文摘要**:
> arXiv:2603.10545v1 Announce Type: new 
摘要: Efficiently allocating incoming jobs to nodes in large-scale clusters can lead to substantial improvements in both 集群 utilization and job 性能. In order to allocate incoming jobs, 集群 schedulers usually rely on a set of scoring functions to rank feasible nodes. Results from individual scoring functions are usually weighted equally, which could lead to sub-optimal deployments as the one-size-fits-all solution does not take into account the characteristics of each workload. Tuning the weights of scoring functions, however, requires expert knowledge and is computationally expensive.
  This 论文 proposes a 强化 学习 方案 for 学习 the weights in 调度器 scoring algorithms with the overall objective of improving the end-to-end 性能 of jobs for a given 集群. Our 方案 is based ...

**Original Abstract**:
> arXiv:2603.10545v1 Announce Type: new 
Abstract: Efficiently allocating incoming jobs to nodes in large-scale clusters can lead to substantial improvements in both cluster utilization and job performance. In order to allocate incoming jobs, cluster schedulers usually rely on a set of scoring functions to rank feasible nodes. Results from individual scoring functions are usually weighted equally, which could lead to sub-optimal deployments as the one-size-fits-all solution does not take into account the characteristics of each workload. Tuning the weights of scoring functions, however, requires expert knowledge and is computationally expensive.
  This paper proposes a reinforcement learning approach for learning the weights in scheduler scoring algorithms with the overall objective of impro...

---

## 59. A Bipartite Graph 方案 to U.S.-China Cross-Market 回报 Forecasting

**原标题**: A Bipartite Graph Approach to U.S.-China Cross-Market Return Forecasting

**作者**: Jing Liu, Maria Grith, Xiaowen Dong, Mihai Cucuringu
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10559v1

**中文摘要**:
> arXiv:2603.10559v1 Announce Type: new 
摘要: This 论文 studies cross-market 回报 predictability through a machine 学习 框架 that preserves economic structure. Exploiting the non-overlapping trading hours of the U.S. and Chinese equity markets, we construct a directed bipartite graph that captures time-ordered predictive linkages between stocks across markets. Edges are selected via rolling-window hypothesis testing, and the resulting graph serves as a sparse, economically 可解释 特征-选择 layer for downstream machine 学习 models. We apply a range of regularized and ensemble methods to forecast open-to-close returns using lagged foreign-market information. Our results reveal a pronounced directional asymmetry: U.S. previous-close-to-close returns contain substantial predictive information for Chinese intraday...

**Original Abstract**:
> arXiv:2603.10559v1 Announce Type: new 
Abstract: This paper studies cross-market return predictability through a machine learning framework that preserves economic structure. Exploiting the non-overlapping trading hours of the U.S. and Chinese equity markets, we construct a directed bipartite graph that captures time-ordered predictive linkages between stocks across markets. Edges are selected via rolling-window hypothesis testing, and the resulting graph serves as a sparse, economically interpretable feature-selection layer for downstream machine learning models. We apply a range of regularized and ensemble methods to forecast open-to-close returns using lagged foreign-market information. Our results reveal a pronounced directional asymmetry: U.S. previous-close-to-close returns contain s...

---

## 60. Riemannian Geometry-Preserving Variational Autoencoder for MI-BCI Data Augmentation

**原标题**: Riemannian Geometry-Preserving Variational Autoencoder for MI-BCI Data Augmentation

**作者**: Viktorija Po\c{l}aka, Ivo Pascal de Jong, Andreea Ioana Sburlea
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10563v1

**中文摘要**:
> arXiv:2603.10563v1 Announce Type: new 
摘要: This 论文 addresses the challenge of generating synthetic electroencephalogram (EEG) covariance matrices for motor imagery brain-computer interface (MI-BCI) applications. Objective: We aim to develop a 生成式 模型 capable of producing high-fidelity synthetic covariance matrices while preserving their symmetric positive-definite nature. 方案: We propose a Riemannian geometry-preserving variational autoencoder (RGP-VAE) integrating geometric mappings with a composite 损失 function combining Riemannian distance, tangent space reconstruction accuracy and 生成式 diversity. Results: The 模型 generates valid, representative EEG covariance matrices, while 学习 a subject-invariant 隐变量 space. Synthetic data proves practically useful for MI-BCI, with its impact depending on t...

**Original Abstract**:
> arXiv:2603.10563v1 Announce Type: new 
Abstract: This paper addresses the challenge of generating synthetic electroencephalogram (EEG) covariance matrices for motor imagery brain-computer interface (MI-BCI) applications. Objective: We aim to develop a generative model capable of producing high-fidelity synthetic covariance matrices while preserving their symmetric positive-definite nature. Approach: We propose a Riemannian geometry-preserving variational autoencoder (RGP-VAE) integrating geometric mappings with a composite loss function combining Riemannian distance, tangent space reconstruction accuracy and generative diversity. Results: The model generates valid, representative EEG covariance matrices, while learning a subject-invariant latent space. Synthetic data proves practically use...

---

## 61. Implicit Statistical 推理 in Transformers: Approximating Likelihood-Ratio Tests In-Context

**原标题**: Implicit Statistical Inference in Transformers: Approximating Likelihood-Ratio Tests In-Context

**作者**: Faris Chaudhry, Siddhant Gadkari
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10573v1

**中文摘要**:
> arXiv:2603.10573v1 Announce Type: new 
摘要: In-context 学习 (ICL) allows Transformers to adapt to novel tasks without weight updates, yet the underlying algorithms remain poorly understood. We adopt a statistical 决策-theoretic perspective by investigating simple binary hypothesis testing, where the optimal 策略 is determined by the likelihood-ratio test. Notably, this setup provides a mathematically rigorous setting for mechanistic interpretability where the 目标 algorithmic ground truth is known. By 训练 Transformers on tasks requiring distinct geometries (linear shifted means vs. nonlinear variance estimation), we demonstrate that the models approximate the Bayes-optimal sufficient statistics from context up to some monotonic transformation, matching the 性能 of an ideal oracle estimator in nonlinea...

**Original Abstract**:
> arXiv:2603.10573v1 Announce Type: new 
Abstract: In-context learning (ICL) allows Transformers to adapt to novel tasks without weight updates, yet the underlying algorithms remain poorly understood. We adopt a statistical decision-theoretic perspective by investigating simple binary hypothesis testing, where the optimal policy is determined by the likelihood-ratio test. Notably, this setup provides a mathematically rigorous setting for mechanistic interpretability where the target algorithmic ground truth is known. By training Transformers on tasks requiring distinct geometries (linear shifted means vs. nonlinear variance estimation), we demonstrate that the models approximate the Bayes-optimal sufficient statistics from context up to some monotonic transformation, matching the performance...

---

## 62. HAPEns: Hardware-Aware Post-Hoc Ensembling for Tabular Data

**原标题**: HAPEns: Hardware-Aware Post-Hoc Ensembling for Tabular Data

**作者**: Jannis Maier, Lennart Purucker
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10582v1

**中文摘要**:
> arXiv:2603.10582v1 Announce Type: new 
摘要: Ensembling is commonly used in machine 学习 on tabular data to boost predictive 性能 and 鲁棒性, but larger ensembles often lead to increased hardware demand. We introduce HAPEns, a post-hoc ensembling 方法 that explicitly balances accuracy against hardware efficiency. Inspired by multi-objective and quality diversity 优化, HAPEns constructs a diverse set of ensembles along the Pareto front of predictive 性能 and resource usage. Existing hardware-aware post-hoc ensembling baselines are not available, highlighting the novelty of our 方案. Experiments on 83 tabular 分类 datasets show that HAPEns significantly outperforms baselines, finding superior trade-offs for ensemble 性能 and 部署 cost. Ablation studies also reveal that 内存 usage is a particularly effective objectiv...

**Original Abstract**:
> arXiv:2603.10582v1 Announce Type: new 
Abstract: Ensembling is commonly used in machine learning on tabular data to boost predictive performance and robustness, but larger ensembles often lead to increased hardware demand. We introduce HAPEns, a post-hoc ensembling method that explicitly balances accuracy against hardware efficiency. Inspired by multi-objective and quality diversity optimization, HAPEns constructs a diverse set of ensembles along the Pareto front of predictive performance and resource usage. Existing hardware-aware post-hoc ensembling baselines are not available, highlighting the novelty of our approach. Experiments on 83 tabular classification datasets show that HAPEns significantly outperforms baselines, finding superior trade-offs for ensemble performance and deployment...

---

## 63. 梯度 Flow Drifting: 生成式 Modeling via Wasserstein 梯度 Flows of KDE-Approximated Divergences

**原标题**: Gradient Flow Drifting: Generative Modeling via Wasserstein Gradient Flows of KDE-Approximated Divergences

**作者**: Jiarui Cao, Zixuan Wei, Yuxin Liu
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10592v1

**中文摘要**:
> arXiv:2603.10592v1 Announce Type: new 
摘要: We reveal a precise mathematical 框架 about a new family of 生成式 models which we call 梯度 Flow Drifting. With this 框架, we prove an equivalence between the recently proposed Drifting 模型 and the Wasserstein 梯度 flow of the 前向 KL divergence under kernel density estimation (KDE) approximation. Specifically, we prove that the drifting field of drifting 模型 (arXiv:2602.04770) equals, up to a 带宽-squared scaling factor, the difference of KDE log-density gradients $\nabla \log p_{\mathrm{kde}} - \nabla \log q_{\mathrm{kde}}$, which is exactly the particle velocity field of the Wasserstein-2 梯度 flow of $KL(q\|p)$ with KDE-approximated densities. Besides that, this broad family of 生成式 models can also include MMD-based generators, which arises as special cases of W...

**Original Abstract**:
> arXiv:2603.10592v1 Announce Type: new 
Abstract: We reveal a precise mathematical framework about a new family of generative models which we call Gradient Flow Drifting. With this framework, we prove an equivalence between the recently proposed Drifting Model and the Wasserstein gradient flow of the forward KL divergence under kernel density estimation (KDE) approximation. Specifically, we prove that the drifting field of drifting model (arXiv:2602.04770) equals, up to a bandwidth-squared scaling factor, the difference of KDE log-density gradients $\nabla \log p_{\mathrm{kde}} - \nabla \log q_{\mathrm{kde}}$, which is exactly the particle velocity field of the Wasserstein-2 gradient flow of $KL(q\|p)$ with KDE-approximated densities. Besides that, this broad family of generative models can...

---

## 64. 强化 学习 with Conditional Expectation 奖励

**原标题**: Reinforcement Learning with Conditional Expectation Reward

**作者**: Changyi Xiao, Caijun Xu, Yixin Cao
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10624v1

**中文摘要**:
> arXiv:2603.10624v1 Announce Type: new 
摘要: 强化 学习 with Verifiable Rewards (RLVR) has proven effective in enhancing the 推理 capabilities of large language models, particularly in domains such as mathematics where reliable rule-based verifiers can be constructed. However, the reliance on handcrafted, domain-specific verification rules substantially limits the applicability of RLVR to general 推理 domains with free-form answers, where valid answers often exhibit significant variability, making it difficult to establish complete and 准确 rules. To address this limitation, we propose Conditional Expectation 奖励 (CER), which leverages the large language 模型 itself as an implicit verifier, and is therefore applicable to general domains and eliminates the need for external verifiers or auxiliary models. C...

**Original Abstract**:
> arXiv:2603.10624v1 Announce Type: new 
Abstract: Reinforcement Learning with Verifiable Rewards (RLVR) has proven effective in enhancing the reasoning capabilities of large language models, particularly in domains such as mathematics where reliable rule-based verifiers can be constructed. However, the reliance on handcrafted, domain-specific verification rules substantially limits the applicability of RLVR to general reasoning domains with free-form answers, where valid answers often exhibit significant variability, making it difficult to establish complete and accurate rules. To address this limitation, we propose Conditional Expectation Reward (CER), which leverages the large language model itself as an implicit verifier, and is therefore applicable to general domains and eliminates the ...

---

## 65. Spatio-Temporal 注意力 Graph 神经 网络: Explaining Causalities With 注意力

**原标题**: Spatio-Temporal Attention Graph Neural Network: Explaining Causalities With Attention

**作者**: Kosti Koistinen, Kirsi Hellsten, Joni Herttuainen, Kimmo K. Kaski
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10676v1

**中文摘要**:
> arXiv:2603.10676v1 Announce Type: new 
摘要: Industrial 控制 Systems (ICS) underpin critical infrastructure and face growing cyber-physical threats due to the convergence of operational technology and networked environments. While machine 学习-based anomaly 检测 approaches in ICS shows strong theoretical 性能, 部署 is often limited by poor explainability, high false-positive rates, and sensitivity to evolving 系统 behavior, i.e., baseline drifting. We propose a Spatio-Temporal 注意力 Graph 神经 网络 (STA-GNN) for 无监督 and 可解释 anomaly 检测 in ICS that models both temporal dynamics and relational structure of the 系统. Sensors, controllers, and 网络 entities are represented as nodes in a dynamically learned graph, enabling the 模型 to capture inter-dependencies across physical processes and communication patterns. 注意力 me...

**Original Abstract**:
> arXiv:2603.10676v1 Announce Type: new 
Abstract: Industrial Control Systems (ICS) underpin critical infrastructure and face growing cyber-physical threats due to the convergence of operational technology and networked environments. While machine learning-based anomaly detection approaches in ICS shows strong theoretical performance, deployment is often limited by poor explainability, high false-positive rates, and sensitivity to evolving system behavior, i.e., baseline drifting. We propose a Spatio-Temporal Attention Graph Neural Network (STA-GNN) for unsupervised and explainable anomaly detection in ICS that models both temporal dynamics and relational structure of the system. Sensors, controllers, and network entities are represented as nodes in a dynamically learned graph, enabling the ...

---

## 66. Contract And Conquer: How to Provably Compute 对抗 Examples for a Black-Box 模型?

**原标题**: Contract And Conquer: How to Provably Compute Adversarial Examples for a Black-Box Model?

**作者**: Anna Chistyakova, Mikhail Pautov
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10689v1

**中文摘要**:
> arXiv:2603.10689v1 Announce Type: new 
摘要: Black-box 对抗 attacks are widely used as tools to test the 鲁棒性 of 深度 神经 networks against malicious perturbations of input data aimed at a specific change in the output of the 模型. Such methods, although they remain empirically effective, usually do not guarantee that an 对抗 example can be found for a particular 模型. In this 论文, we propose Contract And Conquer (CAC), an 方案 to provably compute 对抗 examples for 神经 networks in a black-box manner. The 方法 is based on knowledge distillation of a black-box 模型 on an expanding distillation 数据集 and precise contraction of the 对抗 example 搜索 space. CAC is supported by the transferability guarantee: we prove that the 方法 yields an 对抗 example for the black-box 模型 within a fixed number of 算法 iterations. Experimentally, ...

**Original Abstract**:
> arXiv:2603.10689v1 Announce Type: new 
Abstract: Black-box adversarial attacks are widely used as tools to test the robustness of deep neural networks against malicious perturbations of input data aimed at a specific change in the output of the model. Such methods, although they remain empirically effective, usually do not guarantee that an adversarial example can be found for a particular model. In this paper, we propose Contract And Conquer (CAC), an approach to provably compute adversarial examples for neural networks in a black-box manner. The method is based on knowledge distillation of a black-box model on an expanding distillation dataset and precise contraction of the adversarial example search space. CAC is supported by the transferability guarantee: we prove that the method yield...

---

## 67. Beyond Accuracy: Reliability and Uncertainty Estimation in Convolutional 神经 Networks

**原标题**: Beyond Accuracy: Reliability and Uncertainty Estimation in Convolutional Neural Networks

**作者**: Sanne Ruijs, Alina Kosiakova, Farrukh Javed
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10731v1

**中文摘要**:
> arXiv:2603.10731v1 Announce Type: new 
摘要: 深度 神经 networks (DNNs) have become integral to a wide range of scientific and practical applications due to their flexibility and strong predictive 性能. Despite their accuracy, however, DNNs frequently exhibit poor calibration, often assigning overly confident probabilities to incorrect predictions. This limitation underscores the growing need for integrated mechanisms that provide reliable uncertainty estimation. In this article, we compare two prominent approaches for uncertainty quantification: a 贝叶斯 approximation via Monte Carlo Dropout and the nonparametric Conformal Prediction 框架. Both methods are assessed using two convolutional 神经 网络 architectures; H-CNN VGG16 and GoogLeNet, trained on the Fashion-MNIST 数据集. The empirical results show that a...

**Original Abstract**:
> arXiv:2603.10731v1 Announce Type: new 
Abstract: Deep neural networks (DNNs) have become integral to a wide range of scientific and practical applications due to their flexibility and strong predictive performance. Despite their accuracy, however, DNNs frequently exhibit poor calibration, often assigning overly confident probabilities to incorrect predictions. This limitation underscores the growing need for integrated mechanisms that provide reliable uncertainty estimation. In this article, we compare two prominent approaches for uncertainty quantification: a Bayesian approximation via Monte Carlo Dropout and the nonparametric Conformal Prediction framework. Both methods are assessed using two convolutional neural network architectures; H-CNN VGG16 and GoogLeNet, trained on the Fashion-MN...

---

## 68. A Grammar of Machine 学习 Workflows

**原标题**: A Grammar of Machine Learning Workflows

**作者**: Simon Roth
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10742v1

**中文摘要**:
> arXiv:2603.10742v1 Announce Type: new 
摘要: Data leakage affected 294 发布日期 papers across 17 scientific fields (Kapoor & Narayanan, 2023). The dominant response has been documentation: checklists, linters, best-practice guides. Documentation does not prevent these failures. This 论文 proposes a structural remedy: a grammar that decomposes the 有监督 学习 lifecycle into 7 kernel primitives connected by a typed directed acyclic graph (DAG), with four hard constraints that 拒绝 the two most damaging leakage classes at call time. The grammar's core contribution is the terminal assess constraint: a runtime-enforced evaluate/assess boundary where repeated test-set assessment is rejected by a guard on a nominally distinct Evidence type. A companion study across 2,047 experimental instances quantifies why th...

**Original Abstract**:
> arXiv:2603.10742v1 Announce Type: new 
Abstract: Data leakage affected 294 published papers across 17 scientific fields (Kapoor & Narayanan, 2023). The dominant response has been documentation: checklists, linters, best-practice guides. Documentation does not prevent these failures. This paper proposes a structural remedy: a grammar that decomposes the supervised learning lifecycle into 7 kernel primitives connected by a typed directed acyclic graph (DAG), with four hard constraints that reject the two most damaging leakage classes at call time. The grammar's core contribution is the terminal assess constraint: a runtime-enforced evaluate/assess boundary where repeated test-set assessment is rejected by a guard on a nominally distinct Evidence type. A companion study across 2,047 experimen...

---

## 69. CUPID: A Plug-in 框架 for Joint Aleatoric and Epistemic Uncertainty Estimation with a Single 模型

**原标题**: CUPID: A Plug-in Framework for Joint Aleatoric and Epistemic Uncertainty Estimation with a Single Model

**作者**: Xinran Xu, Xiuyi Fan
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10745v1

**中文摘要**:
> arXiv:2603.10745v1 Announce Type: new 
摘要: 准确 estimation of uncertainty in 深度 学习 is critical for deploying models in high-stakes domains such as medical diagnosis and 自主 决策-making, where overconfident predictions can lead to harmful outcomes. In practice, understanding the reason behind a 模型's uncertainty and the type of uncertainty it represents can support risk-aware decisions, enhance user trust, and guide additional data collection. However, many existing methods only address a single type of uncertainty or require modifications and retraining of the base 模型, making them difficult to adopt in real-world systems. We introduce CUPID (Comprehensive Uncertainty Plug-in estImation 模型), a general-purpose module that jointly estimates aleatoric and epistemic uncertainty without modifying or r...

**Original Abstract**:
> arXiv:2603.10745v1 Announce Type: new 
Abstract: Accurate estimation of uncertainty in deep learning is critical for deploying models in high-stakes domains such as medical diagnosis and autonomous decision-making, where overconfident predictions can lead to harmful outcomes. In practice, understanding the reason behind a model's uncertainty and the type of uncertainty it represents can support risk-aware decisions, enhance user trust, and guide additional data collection. However, many existing methods only address a single type of uncertainty or require modifications and retraining of the base model, making them difficult to adopt in real-world systems. We introduce CUPID (Comprehensive Uncertainty Plug-in estImation moDel), a general-purpose module that jointly estimates aleatoric and e...

---

## 70. Prioritizing 梯度 Sign Over Modulus: An Importance-Aware 框架 for Wireless Federated 学习

**原标题**: Prioritizing Gradient Sign Over Modulus: An Importance-Aware Framework for Wireless Federated Learning

**作者**: Yiyang Yue, Jiacheng Yao, Wei Xu, Zhaohui Yang, George K. Karagiannidis, Dusit Niyato
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10763v1

**中文摘要**:
> arXiv:2603.10763v1 Announce Type: new 
摘要: Wireless federated 学习 (FL) facilitates collaborative 训练 of artificial intelligence (AI) models to support ubiquitous intelligent applications at the wireless edge. However, the inherent constraints of limited wireless resources inevitably lead to unreliable communication, which poses a significant challenge to wireless FL. To overcome this challenge, we propose Sign-优先 FL (SP-FL), a novel 框架 that improves wireless FL by prioritizing the transmission of important 梯度 information through uneven resource allocation. Specifically, recognizing the importance of descent direction in 模型 updating, we transmit 梯度 signs in individual packets and allow their reuse for 梯度 descent if the remaining 梯度 modulus cannot be correctly recovered. To further improve the...

**Original Abstract**:
> arXiv:2603.10763v1 Announce Type: new 
Abstract: Wireless federated learning (FL) facilitates collaborative training of artificial intelligence (AI) models to support ubiquitous intelligent applications at the wireless edge. However, the inherent constraints of limited wireless resources inevitably lead to unreliable communication, which poses a significant challenge to wireless FL. To overcome this challenge, we propose Sign-Prioritized FL (SP-FL), a novel framework that improves wireless FL by prioritizing the transmission of important gradient information through uneven resource allocation. Specifically, recognizing the importance of descent direction in model updating, we transmit gradient signs in individual packets and allow their reuse for gradient descent if the remaining gradient ...

---

## 71. Dynamics-Informed 深度 学习 for Predicting Extreme Events

**原标题**: Dynamics-Informed Deep Learning for Predicting Extreme Events

**作者**: Eirini Katsidoniotaki, Themistoklis P. Sapsis
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10777v1

**中文摘要**:
> arXiv:2603.10777v1 Announce Type: new 
摘要: Predicting extreme events in high-dimensional chaotic dynamical systems remains a fundamental challenge, as such events are rare, intermittent, and arise from transient dynamical mechanisms that are difficult to infer from limited observations. Accordingly, 实时 forecasting calls for precursors that 编码 the mechanisms driving extremes, rather than relying solely on statistical associations. We propose a fully data-driven 框架 for long-lead prediction of extreme events that constructs 可解释, mechanism-aware precursors by explicitly tracking transient instabilities preceding event onset. The 方案 leverages a reduced-order formulation to compute finite-time Lyapunov exponent (FTLE)-like precursors directly from 状态 snapshots, without requiring knowledge of the...

**Original Abstract**:
> arXiv:2603.10777v1 Announce Type: new 
Abstract: Predicting extreme events in high-dimensional chaotic dynamical systems remains a fundamental challenge, as such events are rare, intermittent, and arise from transient dynamical mechanisms that are difficult to infer from limited observations. Accordingly, real-time forecasting calls for precursors that encode the mechanisms driving extremes, rather than relying solely on statistical associations. We propose a fully data-driven framework for long-lead prediction of extreme events that constructs interpretable, mechanism-aware precursors by explicitly tracking transient instabilities preceding event onset. The approach leverages a reduced-order formulation to compute finite-time Lyapunov exponent (FTLE)-like precursors directly from state sn...

---

## 72. AI-Enhanced Spatial Cellular Traffic Demand Prediction with Contextual Clustering and Error Correction for 5G/6G 规划

**原标题**: AI-Enhanced Spatial Cellular Traffic Demand Prediction with Contextual Clustering and Error Correction for 5G/6G Planning

**作者**: Mohamad Alkadamani, Colin Brown, Halim Yanikomeroglu
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10800v1

**中文摘要**:
> arXiv:2603.10800v1 Announce Type: new 
摘要: 准确 spatial prediction of cellular traffic demand is essential for 5G NR capacity 规划, 网络 densification, and data-driven 6G 规划. Although machine 学习 can fuse heterogeneous geospatial and socio-economic layers to estimate fine-grained demand maps, spatial autocorrelation can cause neighborhood leakage under naive train/test splits, inflating accuracy and weakening 规划 reliability. This 论文 presents an AI-driven 框架 that reduces leakage and improves spatial 泛化 via a context-aware two-stage splitting strategy with residual spatial error correction. Experiments using crowdsourced usage indicators across five major Canadian cities show consistent mean absolute error (MAE) reductions relative to location-only clustering, supporting more reliable 带宽 provisioni...

**Original Abstract**:
> arXiv:2603.10800v1 Announce Type: new 
Abstract: Accurate spatial prediction of cellular traffic demand is essential for 5G NR capacity planning, network densification, and data-driven 6G planning. Although machine learning can fuse heterogeneous geospatial and socio-economic layers to estimate fine-grained demand maps, spatial autocorrelation can cause neighborhood leakage under naive train/test splits, inflating accuracy and weakening planning reliability. This paper presents an AI-driven framework that reduces leakage and improves spatial generalization via a context-aware two-stage splitting strategy with residual spatial error correction. Experiments using crowdsourced usage indicators across five major Canadian cities show consistent mean absolute error (MAE) reductions relative to l...

---

## 73. Protein Counterfactuals via Diffusion-Guided 隐变量 优化

**原标题**: Protein Counterfactuals via Diffusion-Guided Latent Optimization

**作者**: Weronika K{\l}os, Sidney Bender, Lukas Kades
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10811v1

**中文摘要**:
> arXiv:2603.10811v1 Announce Type: new 
摘要: 深度 学习 models can predict protein properties with unprecedented accuracy but rarely offer mechanistic insight or actionable guidance for engineering improved variants. When a 模型 flags an antibody as unstable, the protein engineer is left without recourse: which mutations would rescue stability while preserving function? We introduce Manifold-Constrained Counterfactual 优化 for Proteins (MCCOP), a 框架 that computes minimal, biologically plausible sequence edits that flip a 模型's prediction to a desired 目标 状态. MCCOP operates in a continuous joint sequence-structure 隐变量 space and employs a pretrained diffusion 模型 as a manifold prior, balancing three objectives: validity (achieving the 目标 property), proximity (minimizing mutations), and plausibility (produ...

**Original Abstract**:
> arXiv:2603.10811v1 Announce Type: new 
Abstract: Deep learning models can predict protein properties with unprecedented accuracy but rarely offer mechanistic insight or actionable guidance for engineering improved variants. When a model flags an antibody as unstable, the protein engineer is left without recourse: which mutations would rescue stability while preserving function? We introduce Manifold-Constrained Counterfactual Optimization for Proteins (MCCOP), a framework that computes minimal, biologically plausible sequence edits that flip a model's prediction to a desired target state. MCCOP operates in a continuous joint sequence-structure latent space and employs a pretrained diffusion model as a manifold prior, balancing three objectives: validity (achieving the target property), pro...

---

## 74. Evaluating randomized smoothing as a defense against 对抗 attacks in 轨迹 prediction

**原标题**: Evaluating randomized smoothing as a defense against adversarial attacks in trajectory prediction

**作者**: Julian F. Schumann, Eduardo Figueiredo, Frederik Baymler Mathiesen, Luca Laurenti, Jens Kober, Arkady Zgonnikov
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10821v1

**中文摘要**:
> arXiv:2603.10821v1 Announce Type: new 
摘要: 准确 and 鲁棒 轨迹 prediction is essential for safe and 高效 自主 driving, yet recent work has shown that even 状态-of-the-art prediction models are highly vulnerable to inputs being mildly perturbed by 对抗 attacks. Although 模型 vulnerabilities to such attacks have been studied, work on effective countermeasures remains limited. In this work, we develop and evaluate a new defense mechanism for 轨迹 prediction models based on randomized smoothing -- an 方案 previously applied successfully in other domains. We evaluate its ability to improve 模型 鲁棒性 through a series of experiments that test different strategies of randomized smoothing. We show that our 方案 can consistently improve prediction 鲁棒性 of multiple base 轨迹 prediction models in various datasets without compromi...

**Original Abstract**:
> arXiv:2603.10821v1 Announce Type: new 
Abstract: Accurate and robust trajectory prediction is essential for safe and efficient autonomous driving, yet recent work has shown that even state-of-the-art prediction models are highly vulnerable to inputs being mildly perturbed by adversarial attacks. Although model vulnerabilities to such attacks have been studied, work on effective countermeasures remains limited. In this work, we develop and evaluate a new defense mechanism for trajectory prediction models based on randomized smoothing -- an approach previously applied successfully in other domains. We evaluate its ability to improve model robustness through a series of experiments that test different strategies of randomized smoothing. We show that our approach can consistently improve predi...

---

## 75. Towards Cold-Start Drafting and Continual Refining: A 价值-Driven 内存 方案 with Application to NPU Kernel 合成

**原标题**: Towards Cold-Start Drafting and Continual Refining: A Value-Driven Memory Approach with Application to NPU Kernel Synthesis

**作者**: Yujie Zheng, Zhuo Li, Shengtao Zhang, Hanjing Wang, Junjie Sheng, Jiaqian Wang, Junchi Yan, Weinan Zhang, Ying Wen, Bo Tang, Muning Wen
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10846v1

**中文摘要**:
> arXiv:2603.10846v1 Announce Type: new 
摘要: Deploying Large Language Models to data-scarce programming domains poses significant challenges, particularly for kernel 合成 on emerging Domain-Specific Architectures where a "Data Wall" limits available 训练 data. While models excel on data-rich platforms like CUDA, they suffer catastrophic 性能 drops on data-scarce ecosystems such as NPU programming. To overcome this cold-start barrier without expensive fine-tuning, we introduce EvoKernel, a self-evolving agentic 框架 that automates the lifecycle of kernel 合成 from initial drafting to continual refining. EvoKernel addresses this by formulating the 合成 process as a 内存-based 强化 学习 task. Through a novel 价值-driven 检索 mechanism, it learns stage-specific Q-values that prioritize experiences based on their cont...

**Original Abstract**:
> arXiv:2603.10846v1 Announce Type: new 
Abstract: Deploying Large Language Models to data-scarce programming domains poses significant challenges, particularly for kernel synthesis on emerging Domain-Specific Architectures where a "Data Wall" limits available training data. While models excel on data-rich platforms like CUDA, they suffer catastrophic performance drops on data-scarce ecosystems such as NPU programming. To overcome this cold-start barrier without expensive fine-tuning, we introduce EvoKernel, a self-evolving agentic framework that automates the lifecycle of kernel synthesis from initial drafting to continual refining. EvoKernel addresses this by formulating the synthesis process as a memory-based reinforcement learning task. Through a novel value-driven retrieval mechanism, i...

---

## 76. 6ABOS: An Open-Source Atmospheric Correction 框架 for the EnMAP Hyperspectral Mission Based on 6S

**原标题**: 6ABOS: An Open-Source Atmospheric Correction Framework for the EnMAP Hyperspectral Mission Based on 6S

**作者**: Gabriel Caballero Ca\~nas, B\'arbara Alvado Arranz, Xavier S\`oria-Perpiny\`a, Antonio Ruiz-Verd\'u, Jes\'us Delegido, Jos\'e Moreno
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10856v1

**中文摘要**:
> arXiv:2603.10856v1 Announce Type: new 
摘要: The Environmental Mapping and Analysis Program (EnMAP) mission has opened new frontiers in the monitoring of optically complex environments. However, the 准确 检索 of surface reflectance over water bodies remains a significant challenge, as the water-leaving signal typically accounts for only a small fraction of the total radiance, being easily obscured by atmospheric scattering and surface reflection effects. This 论文 introduces 6ABOS (6S-based Atmospheric Background Offset Subtraction), a novel open-source Python 框架 designed to automate the atmospheric correction (AC) of EnMAP hyperspectral imagery. By leveraging the Second Simulation of the Satellite Signal in the Solar Spectrum (6S) radiative transfer 模型, 6ABOS implements a physically-based inversi...

**Original Abstract**:
> arXiv:2603.10856v1 Announce Type: new 
Abstract: The Environmental Mapping and Analysis Program (EnMAP) mission has opened new frontiers in the monitoring of optically complex environments. However, the accurate retrieval of surface reflectance over water bodies remains a significant challenge, as the water-leaving signal typically accounts for only a small fraction of the total radiance, being easily obscured by atmospheric scattering and surface reflection effects. This paper introduces 6ABOS (6S-based Atmospheric Background Offset Subtraction), a novel open-source Python framework designed to automate the atmospheric correction (AC) of EnMAP hyperspectral imagery. By leveraging the Second Simulation of the Satellite Signal in the Solar Spectrum (6S) radiative transfer model, 6ABOS imple...

---

## 77. LAtte: Hyperbolic Lorentz 注意力 for Cross-Subject EEG 分类

**原标题**: LAtte: Hyperbolic Lorentz Attention for Cross-Subject EEG Classification

**作者**: Johannes Burchert, Ahmad Bdeir, Tom Hanika, Lars Schmidt-Thieme, Niels Landwehr
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10881v1

**中文摘要**:
> arXiv:2603.10881v1 Announce Type: new 
摘要: Electroencephalogram (EEG) 分类 is critical for applications ranging from medical diagnostics to brain-computer interfaces, yet it remains challenging due to the inherently low signal-to-noise ratio (SNR) and high inter-subject variability. To address these issues, we propose LAtte, a novel 框架 that integrates a Lorentz 注意力 Module with an InceptionTime-based encoder to enable 鲁棒 and generalizable EEG 分类. Unlike prior work, which evaluates primarily on single-subject 性能, LAtte focuses on cross-subject 训练. First, we learn a shared baseline signal across all subjects using pretraining tasks to capture common underlying patterns. Then, we utilize novel Lorentz low-rank adapters to learn subject-specific embeddings that 模型 individual differences. This all...

**Original Abstract**:
> arXiv:2603.10881v1 Announce Type: new 
Abstract: Electroencephalogram (EEG) classification is critical for applications ranging from medical diagnostics to brain-computer interfaces, yet it remains challenging due to the inherently low signal-to-noise ratio (SNR) and high inter-subject variability. To address these issues, we propose LAtte, a novel framework that integrates a Lorentz Attention Module with an InceptionTime-based encoder to enable robust and generalizable EEG classification. Unlike prior work, which evaluates primarily on single-subject performance, LAtte focuses on cross-subject training. First, we learn a shared baseline signal across all subjects using pretraining tasks to capture common underlying patterns. Then, we utilize novel Lorentz low-rank adapters to learn subjec...

---

## 78. Continuous Diffusion Transformers for Designing Synthetic Regulatory Elements

**原标题**: Continuous Diffusion Transformers for Designing Synthetic Regulatory Elements

**作者**: Jonathan Liu, Kia Ghods
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10885v1

**中文摘要**:
> arXiv:2603.10885v1 Announce Type: new 
摘要: We present a parameter-高效 Diffusion Transformer (DiT) for generating 200bp cell-type-specific regulatory DNA sequences. By replacing the U-Net backbone of DNA-Diffusion with a Transformer denoiser equipped with a 2D CNN input encoder, our 模型 matches the U-Net's best validation 损失 in 13 epochs (60$\times$ fewer) and converges 39% lower, while reducing memorization from 5.3% to 1.7% of generated sequences aligning to 训练 data via BLAT. Ablations show the CNN encoder is essential: without it, validation 损失 increases 70% regardless of positional 嵌入 choice. We further apply DDPO finetuning using Enformer as a 奖励 模型, achieving a 38$\times$ improvement in predicted regulatory activity. Cross-validation against DRAKES on an independent prediction task conf...

**Original Abstract**:
> arXiv:2603.10885v1 Announce Type: new 
Abstract: We present a parameter-efficient Diffusion Transformer (DiT) for generating 200bp cell-type-specific regulatory DNA sequences. By replacing the U-Net backbone of DNA-Diffusion with a transformer denoiser equipped with a 2D CNN input encoder, our model matches the U-Net's best validation loss in 13 epochs (60$\times$ fewer) and converges 39% lower, while reducing memorization from 5.3% to 1.7% of generated sequences aligning to training data via BLAT. Ablations show the CNN encoder is essential: without it, validation loss increases 70% regardless of positional embedding choice. We further apply DDPO finetuning using Enformer as a reward model, achieving a 38$\times$ improvement in predicted regulatory activity. Cross-validation against DRAKE...

---

## 79. Dynamics-Predictive 采样 for Active RL Finetuning of Large 推理 Models

**原标题**: Dynamics-Predictive Sampling for Active RL Finetuning of Large Reasoning Models

**作者**: Yixiu Mao, Yun Qu, Qi Wang, Heming Zou, Xiangyang Ji
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10887v1

**中文摘要**:
> arXiv:2603.10887v1 Announce Type: new 
摘要: 强化 学习 (RL) finetuning has become a key 技术 for enhancing the 推理 abilities of large language models (LLMs). However, its effectiveness critically depends on the 选择 of 训练 data. Recent advances underscore the importance of 在线 prompt 选择 methods, which typically concentrate 训练 on partially solved or moderately challenging examples under the current 策略, thereby yielding more effective 模型 updates. While significantly accelerating RL finetuning in terms of 训练 steps, they also incur substantial computational overhead by requiring extensive 大语言模型 rollouts over large candidate batches to identify informative samples, an expense that can outweigh the finetuning process itself. To address this challenge, this work proposes Dynamics-Predictive 采样 (DPS), which 在线...

**Original Abstract**:
> arXiv:2603.10887v1 Announce Type: new 
Abstract: Reinforcement learning (RL) finetuning has become a key technique for enhancing the reasoning abilities of large language models (LLMs). However, its effectiveness critically depends on the selection of training data. Recent advances underscore the importance of online prompt selection methods, which typically concentrate training on partially solved or moderately challenging examples under the current policy, thereby yielding more effective model updates. While significantly accelerating RL finetuning in terms of training steps, they also incur substantial computational overhead by requiring extensive LLM rollouts over large candidate batches to identify informative samples, an expense that can outweigh the finetuning process itself. To add...

---

## 80. Ergodicity in 强化 学习

**原标题**: Ergodicity in reinforcement learning

**作者**: Dominik Baumann, Erfaun Noorani, Arsenii Mustafin, Xinyi Sheng, Bert Verbruggen, Arne Vanhoyweghen, Vincent Ginis, Thomas B. Sch\"on
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10895v1

**中文摘要**:
> arXiv:2603.10895v1 Announce Type: new 
摘要: In 强化 学习, we typically aim to optimize the expected 价值 of the sum of rewards an 智能体 collects over a 轨迹. However, if the process generating these rewards is non-ergodic, the expected 价值, i.e., the average over infinitely many trajectories with a given 策略, is uninformative for the average over a single, but infinitely long 轨迹. Thus, if we care about how the individual 智能体 performs during 部署, the expected 价值 is not a good 优化 objective. In this 论文, we discuss the impact of non-ergodic 奖励 processes on 强化 学习 agents through an instructive example, relate the notion of ergodic 奖励 processes to more widely used notions of ergodic Markov chains, and present existing solutions that optimize long-term 性能 of individual trajectories under non-ergodic 奖励 dynamics...

**Original Abstract**:
> arXiv:2603.10895v1 Announce Type: new 
Abstract: In reinforcement learning, we typically aim to optimize the expected value of the sum of rewards an agent collects over a trajectory. However, if the process generating these rewards is non-ergodic, the expected value, i.e., the average over infinitely many trajectories with a given policy, is uninformative for the average over a single, but infinitely long trajectory. Thus, if we care about how the individual agent performs during deployment, the expected value is not a good optimization objective. In this paper, we discuss the impact of non-ergodic reward processes on reinforcement learning agents through an instructive example, relate the notion of ergodic reward processes to more widely used notions of ergodic Markov chains, and present ...

---

## 81. LookaheadKV: Fast and 准确 KV Cache Eviction by Glimpsing into the Future without 生成

**原标题**: LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation

**作者**: Jinwoo Ahn, Ingyu Seong, Akhil Kedia, Junhan Kim, Hyemi Jang, Kangwook Lee, Yongkweon Jeon
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10899v1

**中文摘要**:
> arXiv:2603.10899v1 Announce Type: new 
摘要: Transformer-based large language models (LLMs) rely on key-价值 (KV) caching to avoid redundant computation during autoregressive 推理. While this mechanism greatly improves efficiency, the cache size grows linearly with the input sequence length, quickly becoming a bottleneck for long-context tasks. Existing solutions mitigate this problem by evicting prompt KV that are deemed unimportant, guided by estimated importance scores. Notably, a recent line of work proposes to improve eviction quality by "glimpsing into the future", in which a draft generator produces a surrogate future response approximating the 目标 模型's true response, and this surrogate is subsequently used to estimate the importance of cached KV more accurately. However, these approaches ...

**Original Abstract**:
> arXiv:2603.10899v1 Announce Type: new 
Abstract: Transformer-based large language models (LLMs) rely on key-value (KV) caching to avoid redundant computation during autoregressive inference. While this mechanism greatly improves efficiency, the cache size grows linearly with the input sequence length, quickly becoming a bottleneck for long-context tasks. Existing solutions mitigate this problem by evicting prompt KV that are deemed unimportant, guided by estimated importance scores. Notably, a recent line of work proposes to improve eviction quality by "glimpsing into the future", in which a draft generator produces a surrogate future response approximating the target model's true response, and this surrogate is subsequently used to estimate the importance of cached KV more accurately. How...

---

## 82. NCAA Bracket Prediction Using Machine 学习 and Combinatorial Fusion Analysis

**原标题**: NCAA Bracket Prediction Using Machine Learning and Combinatorial Fusion Analysis

**作者**: Yuanhong Wu, Isaiah Smith, Tushar Marwah, Michael Schroeter, Mohamed Rahouti, D. Frank Hsu
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10916v1

**中文摘要**:
> arXiv:2603.10916v1 Announce Type: new 
摘要: Machine 学习 models have demonstrated remarkable success in sports prediction in the past years, often treating sports prediction as a 分类 task within the field. This 论文 introduces new perspectives for analyzing sports data to predict outcomes more accurately. We leverage rankings to generate team rankings for the 2024 数据集 using Combinatorial Fusion Analysis (CFA), a new paradigm for combining multiple scoring systems through the rank-score characteristic (RSC) function and cognitive diversity (CD). Our 结果 based on rank combination with respect to team ranking has an accuracy rate of $74.60\%$, which is higher than the best of the ten popular public ranking systems ($73.02\%$). This exhibits the efficacy of CFA in enhancing the precision of sports pr...

**Original Abstract**:
> arXiv:2603.10916v1 Announce Type: new 
Abstract: Machine learning models have demonstrated remarkable success in sports prediction in the past years, often treating sports prediction as a classification task within the field. This paper introduces new perspectives for analyzing sports data to predict outcomes more accurately. We leverage rankings to generate team rankings for the 2024 dataset using Combinatorial Fusion Analysis (CFA), a new paradigm for combining multiple scoring systems through the rank-score characteristic (RSC) function and cognitive diversity (CD). Our result based on rank combination with respect to team ranking has an accuracy rate of $74.60\%$, which is higher than the best of the ten popular public ranking systems ($73.02\%$). This exhibits the efficacy of CFA in e...

---

## 83. ECoLAD: 部署-Oriented 评估 for Automotive Time-Series Anomaly 检测

**原标题**: ECoLAD: Deployment-Oriented Evaluation for Automotive Time-Series Anomaly Detection

**作者**: Kadir-Kaan \"Ozer, Ren\'e Ebeling, Markus Enzweiler
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10926v1

**中文摘要**:
> arXiv:2603.10926v1 Announce Type: new 
摘要: Time-series anomaly detectors are commonly compared on workstation-class hardware under unconstrained execution. In-vehicle monitoring, however, requires predictable 延迟 and stable behavior under limited CPU 并行. Accuracy-only leaderboards can therefore misrepresent which methods remain feasible under 部署-relevant constraints.
  We present ECoLAD (Efficiency Compute Ladder for Anomaly 检测), a 部署-oriented 评估 protocol instantiated as an empirical study on proprietary automotive telemetry (anomaly rate ${\approx}$0.022) and complementary public benchmarks. ECoLAD applies a monotone compute-reduction ladder across heterogeneous detector families using mechanically determined, integer-only scaling rules and explicit CPU thread caps, while logging every app...

**Original Abstract**:
> arXiv:2603.10926v1 Announce Type: new 
Abstract: Time-series anomaly detectors are commonly compared on workstation-class hardware under unconstrained execution. In-vehicle monitoring, however, requires predictable latency and stable behavior under limited CPU parallelism. Accuracy-only leaderboards can therefore misrepresent which methods remain feasible under deployment-relevant constraints.
  We present ECoLAD (Efficiency Compute Ladder for Anomaly Detection), a deployment-oriented evaluation protocol instantiated as an empirical study on proprietary automotive telemetry (anomaly rate ${\approx}$0.022) and complementary public benchmarks. ECoLAD applies a monotone compute-reduction ladder across heterogeneous detector families using mechanically determined, integer-only scaling rules an...

---

## 84. Quantifying Membership Disclosure Risk for Tabular Synthetic Data Using Kernel Density Estimators

**原标题**: Quantifying Membership Disclosure Risk for Tabular Synthetic Data Using Kernel Density Estimators

**作者**: Rajdeep Pathak, Sayantee Jana
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10937v1

**中文摘要**:
> arXiv:2603.10937v1 Announce Type: new 
摘要: The use of synthetic data has become increasingly popular as a 隐私-preserving alternative to sharing real datasets, especially in sensitive domains such as healthcare, finance, and demography. However, the 隐私 assurances of synthetic data are not absolute, and remain susceptible to membership 推理 attacks (MIAs), where adversaries aim to determine whether a specific individual was present in the 数据集 used to train the generator. In this work, we propose a practical and effective 方法 to quantify membership disclosure risk in tabular synthetic datasets using kernel density estimators (KDEs). Our KDE-based 方案 models the distribution of nearest-neighbour distances between synthetic data and the 训练 records, allowing 概率 推理 of membership and enabling 鲁棒 评估 via...

**Original Abstract**:
> arXiv:2603.10937v1 Announce Type: new 
Abstract: The use of synthetic data has become increasingly popular as a privacy-preserving alternative to sharing real datasets, especially in sensitive domains such as healthcare, finance, and demography. However, the privacy assurances of synthetic data are not absolute, and remain susceptible to membership inference attacks (MIAs), where adversaries aim to determine whether a specific individual was present in the dataset used to train the generator. In this work, we propose a practical and effective method to quantify membership disclosure risk in tabular synthetic datasets using kernel density estimators (KDEs). Our KDE-based approach models the distribution of nearest-neighbour distances between synthetic data and the training records, allowing...

---

## 85. Safe RLHF Beyond Expectation: Stochastic Dominance for Universal Spectral Risk 控制

**原标题**: Safe RLHF Beyond Expectation: Stochastic Dominance for Universal Spectral Risk Control

**作者**: Yaswanth Chittepu, Ativ Joshi, Rajarshi Bhattacharjee, Scott Niekum
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10938v1

**中文摘要**:
> arXiv:2603.10938v1 Announce Type: new 
摘要: Safe 强化 学习 from Human Feedback (RLHF) typically enforces safety through expected cost constraints, but the expectation captures only a single statistic of the cost distribution and fails to account for distributional uncertainty, particularly under heavy tails or rare catastrophic events. This limitation is problematic when 鲁棒性 and risk sensitivity are critical. Stochastic dominance offers a principled alternative by comparing entire cost distributions rather than just their averages, enabling direct 控制 over tail risks and potential 分布外 failures that expectation-based constraints may overlook. In this work, we propose Risk-sensitive Alignment via Dominance (RAD), a novel alignment 框架 that replaces scalar expected cost constraints with First-Order ...

**Original Abstract**:
> arXiv:2603.10938v1 Announce Type: new 
Abstract: Safe Reinforcement Learning from Human Feedback (RLHF) typically enforces safety through expected cost constraints, but the expectation captures only a single statistic of the cost distribution and fails to account for distributional uncertainty, particularly under heavy tails or rare catastrophic events. This limitation is problematic when robustness and risk sensitivity are critical. Stochastic dominance offers a principled alternative by comparing entire cost distributions rather than just their averages, enabling direct control over tail risks and potential out-of-distribution failures that expectation-based constraints may overlook. In this work, we propose Risk-sensitive Alignment via Dominance (RAD), a novel alignment framework that r...

---

## 86. When should we trust the annotation? Selective prediction for molecular structure 检索 from mass spectra

**原标题**: When should we trust the annotation? Selective prediction for molecular structure retrieval from mass spectra

**作者**: Mira J\"urgens, Gaetan De Waele, Morteza Rakhshaninejad, Willem Waegeman
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10950v1

**中文摘要**:
> arXiv:2603.10950v1 Announce Type: new 
摘要: Machine 学习 methods for identifying molecular structures from tandem mass spectra (MS/MS) have advanced rapidly, yet current approaches still exhibit significant error rates. In high-stakes applications such as clinical metabolomics and environmental screening, incorrect annotations can have serious consequences, making it essential to determine when a prediction can be trusted. We introduce a selective prediction 框架 for molecular structure 检索 from MS/MS spectra, enabling models to abstain from predictions when uncertainty is too high. We formulate the problem within the risk-coverage tradeoff 框架 and comprehensively evaluate uncertainty quantification strategies at two levels of granularity: fingerprint-level uncertainty over predicted molecular fi...

**Original Abstract**:
> arXiv:2603.10950v1 Announce Type: new 
Abstract: Machine learning methods for identifying molecular structures from tandem mass spectra (MS/MS) have advanced rapidly, yet current approaches still exhibit significant error rates. In high-stakes applications such as clinical metabolomics and environmental screening, incorrect annotations can have serious consequences, making it essential to determine when a prediction can be trusted. We introduce a selective prediction framework for molecular structure retrieval from MS/MS spectra, enabling models to abstain from predictions when uncertainty is too high. We formulate the problem within the risk-coverage tradeoff framework and comprehensively evaluate uncertainty quantification strategies at two levels of granularity: fingerprint-level uncert...

---

## 87. Ranking 推理 LLMs under Test-Time Scaling

**原标题**: Ranking Reasoning LLMs under Test-Time Scaling

**作者**: Mohsen Hariri, Michael Hinczewski, Jing Ma, Vipin Chaudhary
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10960v1

**中文摘要**:
> arXiv:2603.10960v1 Announce Type: new 
摘要: Test-time scaling evaluates 推理 LLMs by 采样 multiple outputs per prompt, but ranking models in this regime remains underexplored. We formalize dense 基准 ranking under test-time scaling and introduce Scorio, a library that implements statistical ranking methods such as paired-comparison models, item response theory (IRT) models, voting rules, and graph- and spectral-based methods. Across $20$ 推理 models on four Olympiad-style math benchmarks (AIME'24, AIME'25, HMMT'25, and BrUMO'25; up to $N=80$ trials), most full-trial rankings agree closely with the 贝叶斯 gold standard $\mathrm{Bayes}_{\mathcal{U}}@80$ (mean Kendall's $\tau_b = 0.93$--$0.95$), and $19$--$34$ methods recover exactly the same ordering. In the single-trial regime, the best methods reach $...

**Original Abstract**:
> arXiv:2603.10960v1 Announce Type: new 
Abstract: Test-time scaling evaluates reasoning LLMs by sampling multiple outputs per prompt, but ranking models in this regime remains underexplored. We formalize dense benchmark ranking under test-time scaling and introduce Scorio, a library that implements statistical ranking methods such as paired-comparison models, item response theory (IRT) models, voting rules, and graph- and spectral-based methods. Across $20$ reasoning models on four Olympiad-style math benchmarks (AIME'24, AIME'25, HMMT'25, and BrUMO'25; up to $N=80$ trials), most full-trial rankings agree closely with the Bayesian gold standard $\mathrm{Bayes}_{\mathcal{U}}@80$ (mean Kendall's $\tau_b = 0.93$--$0.95$), and $19$--$34$ methods recover exactly the same ordering. In the single-...

---

## 88. TOSSS: a CVE-based Software Security 基准 for Large Language Models

**原标题**: TOSSS: a CVE-based Software Security Benchmark for Large Language Models

**作者**: Marc Damie, Murat Bilgehan Ertan, Domenico Essoussi, Angela Makhanu, Ga\"etan Peter, Roos Wensveen
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10969v1

**中文摘要**:
> arXiv:2603.10969v1 Announce Type: new 
摘要: With their increasing capabilities, Large Language Models (LLMs) are now used across many industries. They have become useful tools for software engineers and support a wide range of development tasks. As LLMs are increasingly used in software development workflows, a critical question arises: are LLMs good at software security? At the same time, organizations worldwide invest heavily in cybersecurity to reduce exposure to disruptive attacks. The integration of LLMs into software engineering workflows may introduce new vulnerabilities and weaken existing security efforts.
  We introduce TOSSS (Two-Option 安全 Snippet 选择), a 基准 that measures the ability of LLMs to choose between 安全 and vulnerable 代码 snippets. Existing security benchmarks for LLMs cov...

**Original Abstract**:
> arXiv:2603.10969v1 Announce Type: new 
Abstract: With their increasing capabilities, Large Language Models (LLMs) are now used across many industries. They have become useful tools for software engineers and support a wide range of development tasks. As LLMs are increasingly used in software development workflows, a critical question arises: are LLMs good at software security? At the same time, organizations worldwide invest heavily in cybersecurity to reduce exposure to disruptive attacks. The integration of LLMs into software engineering workflows may introduce new vulnerabilities and weaken existing security efforts.
  We introduce TOSSS (Two-Option Secure Snippet Selection), a benchmark that measures the ability of LLMs to choose between secure and vulnerable code snippets. Existing se...

---

## 89. FRIEND: Federated 学习 for Joint 优化 of multi-RIS Configuration and Eavesdropper Intelligent 检测 in B5G Networks

**原标题**: FRIEND: Federated Learning for Joint Optimization of multi-RIS Configuration and Eavesdropper Intelligent Detection in B5G Networks

**作者**: Maria Lamprini A. Bartsioka, Ioannis A. Bartsiokas, Anastasios K. Papazafeiropoulos, Maria A. Seimeni, Dimitra I. Kaklamani, Iakovos S. Venieris
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10977v1

**中文摘要**:
> arXiv:2603.10977v1 Announce Type: new 
摘要: As wireless systems evolve toward Beyond 5G (B5G), the adoption of cell-free (CF) millimeter-wave (mmWave) architectures combined with Reconfigurable Intelligent Surfaces (RIS) is emerging as a key enabler for ultra-reliable, high-capacity, 可扩展, and 安全 Industrial Internet of Things (IIoT) communications. However, safeguarding these complex and 分布式 environments against eavesdropping remains a critical challenge, particularly when conventional security mechanisms struggle to overcome scalability, and 延迟 constraints. In this 论文, a novel 框架 for detecting malicious users in RIS-enhanced cell-free mmWave networks using Federated 学习 (FL) is presented. The envisioned setup features multiple access points (APs) operating without traditional cell boundaries...

**Original Abstract**:
> arXiv:2603.10977v1 Announce Type: new 
Abstract: As wireless systems evolve toward Beyond 5G (B5G), the adoption of cell-free (CF) millimeter-wave (mmWave) architectures combined with Reconfigurable Intelligent Surfaces (RIS) is emerging as a key enabler for ultra-reliable, high-capacity, scalable, and secure Industrial Internet of Things (IIoT) communications. However, safeguarding these complex and distributed environments against eavesdropping remains a critical challenge, particularly when conventional security mechanisms struggle to overcome scalability, and latency constraints. In this paper, a novel framework for detecting malicious users in RIS-enhanced cell-free mmWave networks using Federated Learning (FL) is presented. The envisioned setup features multiple access points (APs) o...

---

## 90. Federated 学习-driven Beam Management in LEO 6G Non-Terrestrial Networks

**原标题**: Federated Learning-driven Beam Management in LEO 6G Non-Terrestrial Networks

**作者**: Maria Lamprini Bartsioka, Ioannis A. Bartsiokas, Athanasios D. Panagopoulos, Dimitra I. Kaklamani, Iakovos S. Venieris
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10983v1

**中文摘要**:
> arXiv:2603.10983v1 Announce Type: new 
摘要: Low Earth Orbit (LEO) Non-Terrestrial Networks (NTNs) require 高效 beam management under 动态 propagation conditions. This work investigates Federated 学习 (FL)-based beam 选择 in LEO satellite constellations, where orbital planes operate as 分布式 learners through the utilization of High-Altitude Platform Stations (HAPS). Two models, a Multi-Layer Perceptron (MLP) and a Graph 神经 网络 (GNN), are evaluated using realistic channel and beamforming data. Results demonstrate that GNN surpasses MLP in beam prediction accuracy and stability, particularly at low elevation angles, enabling lightweight and intelligent beam management for future NTN deployments.

**Original Abstract**:
> arXiv:2603.10983v1 Announce Type: new 
Abstract: Low Earth Orbit (LEO) Non-Terrestrial Networks (NTNs) require efficient beam management under dynamic propagation conditions. This work investigates Federated Learning (FL)-based beam selection in LEO satellite constellations, where orbital planes operate as distributed learners through the utilization of High-Altitude Platform Stations (HAPS). Two models, a Multi-Layer Perceptron (MLP) and a Graph Neural Network (GNN), are evaluated using realistic channel and beamforming data. Results demonstrate that GNN surpasses MLP in beam prediction accuracy and stability, particularly at low elevation angles, enabling lightweight and intelligent beam management for future NTN deployments.

---

## 91. The Discrete Charm of the MLP: Binary Routing of Continuous Signals in Transformer Feed-前向 Layers

**原标题**: The Discrete Charm of the MLP: Binary Routing of Continuous Signals in Transformer Feed-Forward Layers

**作者**: Peter Balogh
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10985v1

**中文摘要**:
> arXiv:2603.10985v1 Announce Type: new 
摘要: We show that MLP layers in Transformer language models perform binary routing of continuous signals: the 决策 of whether a token needs nonlinear processing is well-captured by binary neuron activations, even though the signals being routed are continuous. In GPT-2 Small (124M parameters), we find that specific neurons implement a consensus 架构 -- seven "default-ON" neurons and one exception handler (N2123 in Layer 11) that are 93-98% mutually exclusive -- creating a binary routing switch. A cross-layer analysis reveals a developmental arc: early layers (L1-3) use single gateway neurons to route exceptions without consensus quorums; middle layers (L4-6) show diffuse processing with neither gateway nor consensus; and late layers (L7-11) crystallize ful...

**Original Abstract**:
> arXiv:2603.10985v1 Announce Type: new 
Abstract: We show that MLP layers in transformer language models perform binary routing of continuous signals: the decision of whether a token needs nonlinear processing is well-captured by binary neuron activations, even though the signals being routed are continuous. In GPT-2 Small (124M parameters), we find that specific neurons implement a consensus architecture -- seven "default-ON" neurons and one exception handler (N2123 in Layer 11) that are 93-98% mutually exclusive -- creating a binary routing switch. A cross-layer analysis reveals a developmental arc: early layers (L1-3) use single gateway neurons to route exceptions without consensus quorums; middle layers (L4-6) show diffuse processing with neither gateway nor consensus; and late layers (...

---

## 92. MCMC Informed 神经 Emulators for Uncertainty Quantification in Dynamical Systems

**原标题**: MCMC Informed Neural Emulators for Uncertainty Quantification in Dynamical Systems

**作者**: Heikki Haario, Zhi-Song Liu, Martin Simon, Hendrik Weichel
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10987v1

**中文摘要**:
> arXiv:2603.10987v1 Announce Type: new 
摘要: 神经 networks are a commonly used 方案 to replace physical models with computationally cheap surrogates. Parametric uncertainty quantification can be included in 训练, assuming that an 准确 prior distribution of the 模型 parameters is available. Here we study the common opposite situation, where direct screening or random 采样 of 模型 parameters leads to exhaustive 训练 times and evaluations at unphysical parameter values. Our solution is to decouple uncertainty quantification from 网络 架构. Instead of 采样 网络 weights, we introduce the 模型-parameter distribution as an input to 网络 训练 via Markov chain Monte Carlo (MCMC). In this way, the surrogate achieves the same uncertainty quantification as the underlying physical 模型, but with substantially reduced computation time. ...

**Original Abstract**:
> arXiv:2603.10987v1 Announce Type: new 
Abstract: Neural networks are a commonly used approach to replace physical models with computationally cheap surrogates. Parametric uncertainty quantification can be included in training, assuming that an accurate prior distribution of the model parameters is available. Here we study the common opposite situation, where direct screening or random sampling of model parameters leads to exhaustive training times and evaluations at unphysical parameter values. Our solution is to decouple uncertainty quantification from network architecture. Instead of sampling network weights, we introduce the model-parameter distribution as an input to network training via Markov chain Monte Carlo (MCMC). In this way, the surrogate achieves the same uncertainty quantific...

---

## 93. Factorized 神经 Implicit DMD for Parametric Dynamics

**原标题**: Factorized Neural Implicit DMD for Parametric Dynamics

**作者**: Siyuan Chen, Zhecheng Wang, Yixin Chen, Yue Chang, Peter Yichen Chen, Eitan Grinspun, Jonathan Panuelos
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10995v1

**中文摘要**:
> arXiv:2603.10995v1 Announce Type: new 
摘要: A data-driven, 模型-free 方案 to modeling the temporal 进化 of physical systems mitigates the need for explicit knowledge of the governing equations. Even when physical priors such as partial differential equations are available, such systems often reside in high-dimensional 状态 spaces and exhibit nonlinear dynamics, making traditional numerical solvers computationally expensive and ill-suited for 实时 analysis and 控制. Consider the problem of 学习 a parametric flow of a dynamical 系统: with an initial field and a set of physical parameters, we aim to predict the 系统's 进化 over time in a way that supports long-视野 rollouts, 泛化 to unseen parameters, and spectral analysis.
  We propose a physics-coded 神经 field parameterization of the Koopman operator's spectral deco...

**Original Abstract**:
> arXiv:2603.10995v1 Announce Type: new 
Abstract: A data-driven, model-free approach to modeling the temporal evolution of physical systems mitigates the need for explicit knowledge of the governing equations. Even when physical priors such as partial differential equations are available, such systems often reside in high-dimensional state spaces and exhibit nonlinear dynamics, making traditional numerical solvers computationally expensive and ill-suited for real-time analysis and control. Consider the problem of learning a parametric flow of a dynamical system: with an initial field and a set of physical parameters, we aim to predict the system's evolution over time in a way that supports long-horizon rollouts, generalization to unseen parameters, and spectral analysis.
  We propose a phys...

---

## 94. 神经 Field Thermal Tomography: A Differentiable Physics 框架 for Non-Destructive 评估

**原标题**: Neural Field Thermal Tomography: A Differentiable Physics Framework for Non-Destructive Evaluation

**作者**: Tao Zhong, Yixun Hu, Dongzhe Zheng, Aditya Sood, Christine Allen-Blanchette
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.11045v1

**中文摘要**:
> arXiv:2603.11045v1 Announce Type: new 
摘要: We propose 神经 Field Thermal Tomography (NeFTY), a differentiable physics 框架 for the quantitative 3D reconstruction of material properties from transient surface temperature measurements. While traditional thermography relies on pixel-wise 1D approximations that neglect lateral diffusion, and soft-constrained Physics-Informed 神经 Networks (PINNs) often fail in transient diffusion scenarios due to 梯度 stiffness, NeFTY parameterizes the 3D diffusivity field as a continuous 神经 field optimized through a rigorous numerical solver. By leveraging a differentiable physics solver, our 方案 enforces thermodynamic laws as hard constraints while maintaining the 内存 efficiency required for high-resolution 3D tomography. Our discretize-then-optimize paradigm effectiv...

**Original Abstract**:
> arXiv:2603.11045v1 Announce Type: new 
Abstract: We propose Neural Field Thermal Tomography (NeFTY), a differentiable physics framework for the quantitative 3D reconstruction of material properties from transient surface temperature measurements. While traditional thermography relies on pixel-wise 1D approximations that neglect lateral diffusion, and soft-constrained Physics-Informed Neural Networks (PINNs) often fail in transient diffusion scenarios due to gradient stiffness, NeFTY parameterizes the 3D diffusivity field as a continuous neural field optimized through a rigorous numerical solver. By leveraging a differentiable physics solver, our approach enforces thermodynamic laws as hard constraints while maintaining the memory efficiency required for high-resolution 3D tomography. Our d...

---

## 95. Breaking the Stochasticity Barrier: An Adaptive Variance-Reduced 方法 for Variational Inequalities

**原标题**: Breaking the Stochasticity Barrier: An Adaptive Variance-Reduced Method for Variational Inequalities

**作者**: Yungi Jeong, Takumi Otsuka
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2601.23034v1

**中文摘要**:
> arXiv:2601.23034v1 Announce Type: cross 
摘要: Stochastic non-convex non-concave 优化, formally characterized as Stochastic Variational Inequalities (SVIs), presents unique challenges due to rotational dynamics and the absence of a global merit function. While adaptive step-size methods (like Armijo line-搜索) have revolutionized convex minimization, their application to this setting is hindered by the Stochasticity Barrier: the noise in 梯度 estimation masks the true operator curvature, triggering erroneously large steps that destabilize convergence. In this work, we propose VR-SDA-A (Variance-Reduced Stochastic Descent-上升 with Armijo), a novel 算法 that integrates recursive 动量 (STORM) with a rigorous Same-批次 Curvature Verification mechanism. We introduce a theoretical 框架 based on a Lyapunov potent...

**Original Abstract**:
> arXiv:2601.23034v1 Announce Type: cross 
Abstract: Stochastic non-convex non-concave optimization, formally characterized as Stochastic Variational Inequalities (SVIs), presents unique challenges due to rotational dynamics and the absence of a global merit function. While adaptive step-size methods (like Armijo line-search) have revolutionized convex minimization, their application to this setting is hindered by the Stochasticity Barrier: the noise in gradient estimation masks the true operator curvature, triggering erroneously large steps that destabilize convergence. In this work, we propose VR-SDA-A (Variance-Reduced Stochastic Descent-Ascent with Armijo), a novel algorithm that integrates recursive momentum (STORM) with a rigorous Same-Batch Curvature Verification mechanism. We introdu...

---

## 96. ConFu: Contemplate the Future for Better Speculative 采样

**原标题**: ConFu: Contemplate the Future for Better Speculative Sampling

**作者**: Zongyue Qin, Raghavv Goel, Mukul Gagrani, Risheek Garrepalli, Mingu Lee, Yizhou Sun
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.08899v1

**中文摘要**:
> arXiv:2603.08899v1 Announce Type: cross 
摘要: Speculative decoding has emerged as a powerful 方案 to accelerate large language 模型 (大语言模型) 推理 by employing lightweight draft models to propose candidate tokens that are subsequently verified by the 目标 模型. The effectiveness of this paradigm critically depends on the quality of the draft 模型. While recent advances such as the EAGLE series achieve 状态-of-the-art speedup, existing draft models remain limited by error accumulation: they condition only on the current prefix, causing their predictions to drift from the 目标 模型 over steps. In this work, we propose \textbf{ConFu} (Contemplate the Future), a novel speculative decoding 框架 that enables draft models to anticipate the future direction of 生成. ConFu introduces (i) contemplate tokens and soft prompts...

**Original Abstract**:
> arXiv:2603.08899v1 Announce Type: cross 
Abstract: Speculative decoding has emerged as a powerful approach to accelerate large language model (LLM) inference by employing lightweight draft models to propose candidate tokens that are subsequently verified by the target model. The effectiveness of this paradigm critically depends on the quality of the draft model. While recent advances such as the EAGLE series achieve state-of-the-art speedup, existing draft models remain limited by error accumulation: they condition only on the current prefix, causing their predictions to drift from the target model over steps. In this work, we propose \textbf{ConFu} (Contemplate the Future), a novel speculative decoding framework that enables draft models to anticipate the future direction of generation. C...

---

## 97. MITRA: An AI Assistant for Knowledge 检索 in Physics Collaborations

**原标题**: MITRA: An AI Assistant for Knowledge Retrieval in Physics Collaborations

**作者**: Abhishikth Mallampalli, Sridhara Dasu
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.09800v1

**中文摘要**:
> arXiv:2603.09800v1 Announce Type: cross 
摘要: Large-scale scientific collaborations, such as the Compact Muon Solenoid (CMS) at CERN, produce a vast and ever-growing 语料库 of internal documentation. Navigating this complex information landscape presents a significant challenge for both new and experienced researchers, hindering knowledge sharing and slowing down the pace of scientific discovery. To address this, we present a prototype of MITRA, a 检索-Augmented 生成 (RAG) based 系统, designed to answer specific, context-aware questions about physics analyses. MITRA employs a novel, automated pipeline using Selenium for document 检索 from internal databases and Optical Character 识别 (OCR) with layout parsing for high-fidelity text extraction. Crucially, MITRA's entire 框架, from the 嵌入 模型 to the Large La...

**Original Abstract**:
> arXiv:2603.09800v1 Announce Type: cross 
Abstract: Large-scale scientific collaborations, such as the Compact Muon Solenoid (CMS) at CERN, produce a vast and ever-growing corpus of internal documentation. Navigating this complex information landscape presents a significant challenge for both new and experienced researchers, hindering knowledge sharing and slowing down the pace of scientific discovery. To address this, we present a prototype of MITRA, a Retrieval-Augmented Generation (RAG) based system, designed to answer specific, context-aware questions about physics analyses. MITRA employs a novel, automated pipeline using Selenium for document retrieval from internal databases and Optical Character Recognition (OCR) with layout parsing for high-fidelity text extraction. Crucially, MITRA...

---

## 98. One 模型, Many Skills: Parameter-高效 Fine-Tuning for Multitask 代码 Analysis

**原标题**: One Model, Many Skills: Parameter-Efficient Fine-Tuning for Multitask Code Analysis

**作者**: Amal Akli, Maxime Cordy, Mike Papadakis, Yves Le Traon
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.09978v1

**中文摘要**:
> arXiv:2603.09978v1 Announce Type: cross 
摘要: Large language models have recently surpassed specialized systems on 代码 生成, yet their effectiveness on other 代码-analysis tasks remains less clear. At the same time, 多任务 学习 offers a way to unify diverse objectives within a single 模型, but fully fine-tuning LLMs across tasks is computationally prohibitive. Parameter-高效 fine-tuning mitigates this cost by updating only a small fraction of weights. Although PEFT has proven effective in single-task settings, its potential for 多任务 学习 has not yet been systematically explored. We present the first comprehensive 评估 of 多任务 PEFT for 代码 analysis, comparing several methods across diverse tasks and 模型 architectures. Our experiments show that a single PEFT module shared across tasks can match, and in some cases ...

**Original Abstract**:
> arXiv:2603.09978v1 Announce Type: cross 
Abstract: Large language models have recently surpassed specialized systems on code generation, yet their effectiveness on other code-analysis tasks remains less clear. At the same time, multi-task learning offers a way to unify diverse objectives within a single model, but fully fine-tuning LLMs across tasks is computationally prohibitive. Parameter-efficient fine-tuning mitigates this cost by updating only a small fraction of weights. Although PEFT has proven effective in single-task settings, its potential for multi-task learning has not yet been systematically explored. We present the first comprehensive evaluation of multi-task PEFT for code analysis, comparing several methods across diverse tasks and model architectures. Our experiments show t...

---

## 99. Evolving Demonstration 优化 for Chain-of-Thought 特征 Transformation

**原标题**: Evolving Demonstration Optimization for Chain-of-Thought Feature Transformation

**作者**: Xinyuan Wang, Kunpeng Liu, Arun Vignesh Malarkkan, Yanjie Fu
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.09987v1

**中文摘要**:
> arXiv:2603.09987v1 Announce Type: cross 
摘要: 特征 Transformation (FT) is a core data-centric AI task that improves 特征 space quality to advance downstream predictive 性能. However, discovering effective transformations remains challenging due to the large space of 特征-operator combinations. Existing solutions rely on discrete 搜索 or 隐变量 生成, but they are frequently limited by sample inefficiency, invalid candidates, and redundant generations with limited coverage. Large Language Models (LLMs) offer strong priors for producing valid transformations, but current 大语言模型-based FT methods typically rely on 静态 demonstrations, resulting in limited diversity, redundant outputs, and weak alignment with downstream objectives. We propose a 框架 that optimizes context data for 大语言模型-driven FT by evolving 轨迹-leve...

**Original Abstract**:
> arXiv:2603.09987v1 Announce Type: cross 
Abstract: Feature Transformation (FT) is a core data-centric AI task that improves feature space quality to advance downstream predictive performance. However, discovering effective transformations remains challenging due to the large space of feature-operator combinations. Existing solutions rely on discrete search or latent generation, but they are frequently limited by sample inefficiency, invalid candidates, and redundant generations with limited coverage. Large Language Models (LLMs) offer strong priors for producing valid transformations, but current LLM-based FT methods typically rely on static demonstrations, resulting in limited diversity, redundant outputs, and weak alignment with downstream objectives. We propose a framework that optimize...

---

## 100. TAMUSA-Chat: A Domain-Adapted Large Language 模型 Conversational 系统 for Research and Responsible 部署

**原标题**: TAMUSA-Chat: A Domain-Adapted Large Language Model Conversational System for Research and Responsible Deployment

**作者**: Izzat Alsmadi, Anas Alsobeh
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.09992v1

**中文摘要**:
> arXiv:2603.09992v1 Announce Type: cross 
摘要: This 论文 presents TAMUSA-Chat, a research-oriented 框架 for building domain-adapted large language 模型 conversational systems. The work addresses critical challenges in adapting general-purpose foundation models to institutional contexts through 有监督 fine-tuning, 检索-augmented 生成, and systematic 评估 methodologies. We describe the complete 架构 encompassing data acquisition from institutional sources, preprocessing pipelines, 嵌入 construction, 模型 训练 workflows, and 部署 strategies. The 系统 integrates modular components enabling reproducible experimentation with 训练 configurations, hyper-parameters, and 评估 protocols. Our 实现 demonstrates how academic institutions can develop contextually grounded conversational agents while maintaining transparency, governance co...

**Original Abstract**:
> arXiv:2603.09992v1 Announce Type: cross 
Abstract: This paper presents TAMUSA-Chat, a research-oriented framework for building domain-adapted large language model conversational systems. The work addresses critical challenges in adapting general-purpose foundation models to institutional contexts through supervised fine-tuning, retrieval-augmented generation, and systematic evaluation methodologies. We describe the complete architecture encompassing data acquisition from institutional sources, preprocessing pipelines, embedding construction, model training workflows, and deployment strategies. The system integrates modular components enabling reproducible experimentation with training configurations, hyper-parameters, and evaluation protocols. Our implementation demonstrates how academic i...

---

## 101. There Are No Silly Questions: 评估 of 离线 大语言模型 Capabilities from a Turkish Perspective

**原标题**: There Are No Silly Questions: Evaluation of Offline LLM Capabilities from a Turkish Perspective

**作者**: Edibe Yilmaz, Kahraman Kostas
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.09996v1

**中文摘要**:
> arXiv:2603.09996v1 Announce Type: cross 
摘要: The integration of large language models (LLMs) into educational processes introduces significant constraints regarding data 隐私 and reliability, particularly in pedagogically vulnerable contexts such as Turkish heritage language education. This study aims to systematically evaluate the 鲁棒性 and pedagogical safety of locally deployable 离线 LLMs within the context of Turkish heritage language education. To this end, a Turkish Anomaly Suite (TAS) consisting of 10 original edge-case scenarios was developed to assess the models' capacities for epistemic resistance, logical consistency, and pedagogical safety. Experiments conducted on 14 different models ranging from 270M to 32B parameters reveal that anomaly resistance is not solely dependent on 模型 sca...

**Original Abstract**:
> arXiv:2603.09996v1 Announce Type: cross 
Abstract: The integration of large language models (LLMs) into educational processes introduces significant constraints regarding data privacy and reliability, particularly in pedagogically vulnerable contexts such as Turkish heritage language education. This study aims to systematically evaluate the robustness and pedagogical safety of locally deployable offline LLMs within the context of Turkish heritage language education. To this end, a Turkish Anomaly Suite (TAS) consisting of 10 original edge-case scenarios was developed to assess the models' capacities for epistemic resistance, logical consistency, and pedagogical safety. Experiments conducted on 14 different models ranging from 270M to 32B parameters reveal that anomaly resistance is not sol...

---

## 102. Beyond the Prompt in Large Language Models: Comprehension, In-Context 学习, and Chain-of-Thought

**原标题**: Beyond the Prompt in Large Language Models: Comprehension, In-Context Learning, and Chain-of-Thought

**作者**: Yuling Jiao, Yanming Lai, Huazhen Lin, Wensen Ma, Houduo Qi, Defeng Sun
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10000v1

**中文摘要**:
> arXiv:2603.10000v1 Announce Type: cross 
摘要: Large Language Models (LLMs) have demonstrated remarkable proficiency across diverse tasks, exhibiting emergent properties such as semantic prompt comprehension, In-Context 学习 (ICL), and Chain-of-Thought (CoT) 推理. Despite their empirical success, the theoretical mechanisms driving these phenomena remain poorly understood. This study dives into the foundations of these observations by addressing three critical questions: (1) How do LLMs accurately 解码 prompt semantics despite being trained solely on a next-token prediction objective? (2) Through what mechanism does ICL facilitate 性能 gains without explicit parameter updates? and (3) Why do intermediate 推理 steps in CoT prompting effectively unlock capabilities for complex, multi-step problems?
  Our...

**Original Abstract**:
> arXiv:2603.10000v1 Announce Type: cross 
Abstract: Large Language Models (LLMs) have demonstrated remarkable proficiency across diverse tasks, exhibiting emergent properties such as semantic prompt comprehension, In-Context Learning (ICL), and Chain-of-Thought (CoT) reasoning. Despite their empirical success, the theoretical mechanisms driving these phenomena remain poorly understood. This study dives into the foundations of these observations by addressing three critical questions: (1) How do LLMs accurately decode prompt semantics despite being trained solely on a next-token prediction objective? (2) Through what mechanism does ICL facilitate performance gains without explicit parameter updates? and (3) Why do intermediate reasoning steps in CoT prompting effectively unlock capabilities ...

---

## 103. Leveraging Wikidata for Geographically Informed Sociocultural 偏见 数据集 Creation: Application to Latin America

**原标题**: Leveraging Wikidata for Geographically Informed Sociocultural Bias Dataset Creation: Application to Latin America

**作者**: Yannis Karmim (ALMAnaCH), Renato Pino (UCHILE), Hernan Contreras (UCHILE), Hernan Lira (CENIA), Sebastian Cifuentes (CENIA), Simon Escoffier (PUC), Luis Mart\'i (UP4, ALPAGE), Djam\'e Seddah (UP4, ALPAGE), Valentin Barri\`ere (UCHILE, CENIA)
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10001v1

**中文摘要**:
> arXiv:2603.10001v1 Announce Type: cross 
摘要: Large Language Models (LLMs) exhibit inequalities with respect to various cultural contexts. Most prominent open-weights models are trained on Global North data and show prejudicial behavior towards other cultures. Moreover, there is a notable lack of resources to detect biases in non-English languages, especially from Latin America (Latam), a continent containing various cultures, even though they share a common cultural ground. We propose to leverage the content of Wikipedia, the structure of the Wikidata 知识图谱, and expert knowledge from social science in order to create a 数据集 of question/answer (Q/As) pairs, based on the different popular and social cultures of various Latin American countries. We create the LatamQA database of over 26k questi...

**Original Abstract**:
> arXiv:2603.10001v1 Announce Type: cross 
Abstract: Large Language Models (LLMs) exhibit inequalities with respect to various cultural contexts. Most prominent open-weights models are trained on Global North data and show prejudicial behavior towards other cultures. Moreover, there is a notable lack of resources to detect biases in non-English languages, especially from Latin America (Latam), a continent containing various cultures, even though they share a common cultural ground. We propose to leverage the content of Wikipedia, the structure of the Wikidata knowledge graph, and expert knowledge from social science in order to create a dataset of question/answer (Q/As) pairs, based on the different popular and social cultures of various Latin American countries. We create the LatamQA databa...

---

## 104. SpreadsheetArena: Decomposing Preference in 大语言模型 生成 of Spreadsheet Workbooks

**原标题**: SpreadsheetArena: Decomposing Preference in LLM Generation of Spreadsheet Workbooks

**作者**: Srivatsa Kundurthy, Clara Na, Michael Handley, Zach Kirshner, Chen Bo Calvin Zhang, Manasi Sharma, Emma Strubell, John Ling
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10002v1

**中文摘要**:
> arXiv:2603.10002v1 Announce Type: cross 
摘要: Large language models (LLMs) are increasingly tasked with producing and manipulating structured artifacts. We consider the task of end-to-end spreadsheet 生成, where language models are prompted to produce spreadsheet artifacts to satisfy users' explicit and implicit constraints, specified in natural language. We introduce SpreadsheetArena, a platform for evaluating models' 性能 on the task via blind pairwise evaluations of 大语言模型-generated spreadsheet workbooks. As with other complex, open-ended tasks, relevant 评估 criteria can vary substantially across use cases and prompts, often in ways that are difficult to formalize. Compared to general chat or text 生成 settings, spreadsheet 生成 presents unique challenges and opportunities: the task output structu...

**Original Abstract**:
> arXiv:2603.10002v1 Announce Type: cross 
Abstract: Large language models (LLMs) are increasingly tasked with producing and manipulating structured artifacts. We consider the task of end-to-end spreadsheet generation, where language models are prompted to produce spreadsheet artifacts to satisfy users' explicit and implicit constraints, specified in natural language. We introduce SpreadsheetArena, a platform for evaluating models' performance on the task via blind pairwise evaluations of LLM-generated spreadsheet workbooks. As with other complex, open-ended tasks, relevant evaluation criteria can vary substantially across use cases and prompts, often in ways that are difficult to formalize. Compared to general chat or text generation settings, spreadsheet generation presents unique challeng...

---

## 105. Defining AI Models and AI Systems: A 框架 to Resolve the Boundary Problem

**原标题**: Defining AI Models and AI Systems: A Framework to Resolve the Boundary Problem

**作者**: Yuanyuan Sun, Timothy Parker, Lara Gierschmann, Sana Shams, Teo Canmetin, Mathieu Duteil, Rokas Gipi\v{s}kis, Ze Shen Chin
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10023v1

**中文摘要**:
> arXiv:2603.10023v1 Announce Type: cross 
摘要: Emerging AI regulations assign distinct obligations to different actors along the AI 价值 chain (e.g., the EU AI Act distinguishes providers and deployers for both AI models and AI systems), yet the foundational terms "AI 模型" and "AI 系统" lack clear, consistent definitions. Through a systematic 审稿 of 896 academic papers and a manual 审稿 of over 80 regulatory, standards, and technical or 策略 documents, we analyze existing definitions from multiple conceptual perspectives. We then trace definitional lineages and paradigm shifts over time, finding that most standards and regulatory definitions derive from the OECD's frameworks, which evolved in ways that compounded rather than resolved conceptual ambiguities. The ambiguity of the boundary between an AI ...

**Original Abstract**:
> arXiv:2603.10023v1 Announce Type: cross 
Abstract: Emerging AI regulations assign distinct obligations to different actors along the AI value chain (e.g., the EU AI Act distinguishes providers and deployers for both AI models and AI systems), yet the foundational terms "AI model" and "AI system" lack clear, consistent definitions. Through a systematic review of 896 academic papers and a manual review of over 80 regulatory, standards, and technical or policy documents, we analyze existing definitions from multiple conceptual perspectives. We then trace definitional lineages and paradigm shifts over time, finding that most standards and regulatory definitions derive from the OECD's frameworks, which evolved in ways that compounded rather than resolved conceptual ambiguities. The ambiguity of...

---

## 106. HTM-EAR: Importance-Preserving Tiered 内存 with Hybrid Routing under Saturation

**原标题**: HTM-EAR: Importance-Preserving Tiered Memory with Hybrid Routing under Saturation

**作者**: Shubham Kumar Singh
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10032v1

**中文摘要**:
> arXiv:2603.10032v1 Announce Type: cross 
摘要: 内存 constraints in long-running agents require structured management of accumulated facts while preserving essential information under bounded context limits. We introduce HTM-EAR, a hierarchical tiered 内存 substrate that integrates HNSW-based working 内存 (L1) with archival 存储 (L2), combining importance-aware eviction and hybrid routing. When L1 reaches capacity, items are evicted using a weighted score of importance and usage. Queries are first resolved in L1; if similarity or entity coverage is insufficient, 检索 falls back to L2, and candidates are re-ranked using a cross-encoder.
  We evaluate the 系统 under sustained saturation (15,000 facts; L1 capacity 500; L2 capacity 5000) using synthetic streams across five random seeds and real BGL 系统 logs. ...

**Original Abstract**:
> arXiv:2603.10032v1 Announce Type: cross 
Abstract: Memory constraints in long-running agents require structured management of accumulated facts while preserving essential information under bounded context limits. We introduce HTM-EAR, a hierarchical tiered memory substrate that integrates HNSW-based working memory (L1) with archival storage (L2), combining importance-aware eviction and hybrid routing. When L1 reaches capacity, items are evicted using a weighted score of importance and usage. Queries are first resolved in L1; if similarity or entity coverage is insufficient, retrieval falls back to L2, and candidates are re-ranked using a cross-encoder.
  We evaluate the system under sustained saturation (15,000 facts; L1 capacity 500; L2 capacity 5000) using synthetic streams across five r...

---

## 107. Evaluating 泛化 Mechanisms in 自主 Cyber Attack Agents

**原标题**: Evaluating Generalization Mechanisms in Autonomous Cyber Attack Agents

**作者**: Ond\v{r}ej Luk\'a\v{s}, Jihoon Shin, Emilia Rivas, Diego Forni, Maria Rigaki, Carlos Catania, Aritran Piplai, Christopher Kiekintveld, Sebastian Garcia
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10041v1

**中文摘要**:
> arXiv:2603.10041v1 Announce Type: cross 
摘要: 自主 offensive agents often fail to transfer beyond the networks on which they are trained. We isolate a minimal but fundamental shift -- unseen host/subnet IP reassignment in an otherwise fixed enterprise scenario -- and evaluate attacker 泛化 in the NetSecGame 环境. Agents are trained on five IP-range variants and tested on a sixth unseen variant; only the meta-学习 智能体 may adapt at test time. We compare three 智能体 families (traditional RL, adaptation agents, and 大语言模型-based agents) and use 动作-distribution-based behavioral/XAI analyses to localize failure modes. Some adaptation methods show partial transfer but significant degradation under unseen reassignment, indicating that even address-space changes can break long-视野 attack policies. Under our 评估 p...

**Original Abstract**:
> arXiv:2603.10041v1 Announce Type: cross 
Abstract: Autonomous offensive agents often fail to transfer beyond the networks on which they are trained. We isolate a minimal but fundamental shift -- unseen host/subnet IP reassignment in an otherwise fixed enterprise scenario -- and evaluate attacker generalization in the NetSecGame environment. Agents are trained on five IP-range variants and tested on a sixth unseen variant; only the meta-learning agent may adapt at test time. We compare three agent families (traditional RL, adaptation agents, and LLM-based agents) and use action-distribution-based behavioral/XAI analyses to localize failure modes. Some adaptation methods show partial transfer but significant degradation under unseen reassignment, indicating that even address-space changes ca...

---

## 108. Safety Under Scaffolding: How 评估 Conditions Shape Measured Safety

**原标题**: Safety Under Scaffolding: How Evaluation Conditions Shape Measured Safety

**作者**: David Gringras
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10044v1

**中文摘要**:
> arXiv:2603.10044v1 Announce Type: cross 
摘要: Safety benchmarks evaluate language models in isolation, typically using multiple-choice format; production deployments wrap these models in agentic scaffolds that restructure inputs through 推理 traces, 评论员 agents, and delegation pipelines. We report one of the largest controlled studies of scaffold effects on safety (N = 62,808; six frontier models, four 部署 configurations), combining pre-registration, assessor blinding, equivalence testing, and specification curve analysis. Map-reduce scaffolding degrades measured safety (NNH = 14), yet two of three scaffold architectures preserve safety within practically meaningful margins. Investigating the map-reduce degradation revealed a deeper measurement problem: switching from multiple-choice to open-en...

**Original Abstract**:
> arXiv:2603.10044v1 Announce Type: cross 
Abstract: Safety benchmarks evaluate language models in isolation, typically using multiple-choice format; production deployments wrap these models in agentic scaffolds that restructure inputs through reasoning traces, critic agents, and delegation pipelines. We report one of the largest controlled studies of scaffold effects on safety (N = 62,808; six frontier models, four deployment configurations), combining pre-registration, assessor blinding, equivalence testing, and specification curve analysis. Map-reduce scaffolding degrades measured safety (NNH = 14), yet two of three scaffold architectures preserve safety within practically meaningful margins. Investigating the map-reduce degradation revealed a deeper measurement problem: switching from mu...

---

## 109. OmniGuide: Universal Guidance Fields for Enhancing Generalist Robot Policies

**原标题**: OmniGuide: Universal Guidance Fields for Enhancing Generalist Robot Policies

**作者**: Yunzhou Song, Long Le, Yong-Hyun Park, Jie Wang, Junyao Shi, Lingjie Liu, Jiatao Gu, Eric Eaton, Dinesh Jayaraman, Kostas Daniilidis
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10052v1

**中文摘要**:
> arXiv:2603.10052v1 Announce Type: cross 
摘要: Vision-language-动作(VLA) models have shown great promise as generalist policies for a large range of relatively simple tasks. However, they demonstrate limited 性能 on more complex tasks, such as those requiring complex spatial or semantic understanding, manipulation in clutter, or precise manipulation. We propose OMNIGUIDE, a flexible 框架 that improves VLA 性能 on such tasks by leveraging arbitrary sources of guidance, such as 3D foundation models, semantic-推理 VLMs, and human pose models. We show how many kinds of guidance can be naturally expressed as differentiable energy functions with task-specific attractors and repellers located in 3D space, that influence the 采样 of VLA actions. In this way, OMNIGUIDE enables guidance sources with complementary...

**Original Abstract**:
> arXiv:2603.10052v1 Announce Type: cross 
Abstract: Vision-language-action(VLA) models have shown great promise as generalist policies for a large range of relatively simple tasks. However, they demonstrate limited performance on more complex tasks, such as those requiring complex spatial or semantic understanding, manipulation in clutter, or precise manipulation. We propose OMNIGUIDE, a flexible framework that improves VLA performance on such tasks by leveraging arbitrary sources of guidance, such as 3D foundation models, semantic-reasoning VLMs, and human pose models. We show how many kinds of guidance can be naturally expressed as differentiable energy functions with task-specific attractors and repellers located in 3D space, that influence the sampling of VLA actions. In this way, OMNIG...

---

## 110. Quantization of Ricci Curvature in Information Geometry

**原标题**: Quantization of Ricci Curvature in Information Geometry

**作者**: Carlos C. Rodriguez
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10054v1

**中文摘要**:
> arXiv:2603.10054v1 Announce Type: cross 
摘要: In 2004, while studying the information geometry of binary 贝叶斯 networks (bitnets), the 作者 conjectured that the volume-averaged Ricci scalar  computed with respect to the Fisher information metric is universally quantized to positive half-integers:  in (1/2)Z. This 论文 resolves the conjecture after 20 years. We prove it for tree-structured and complete-graph bitnets via a universal Beta function cancellation mechanism, and disprove it in general by exhibiting explicit loop counterexamples.
  We extend the program to Gaussian DAG networks, where a sign dichotomy holds: discrete bitnets have positive curvature, while Gaussian networks form solvable Lie groups with negative curvature.

**Original Abstract**:
> arXiv:2603.10054v1 Announce Type: cross 
Abstract: In 2004, while studying the information geometry of binary Bayesian networks (bitnets), the author conjectured that the volume-averaged Ricci scalar  computed with respect to the Fisher information metric is universally quantized to positive half-integers:  in (1/2)Z. This paper resolves the conjecture after 20 years. We prove it for tree-structured and complete-graph bitnets via a universal Beta function cancellation mechanism, and disprove it in general by exhibiting explicit loop counterexamples.
  We extend the program to Gaussian DAG networks, where a sign dichotomy holds: discrete bitnets have positive curvature, while Gaussian networks form solvable Lie groups with negative curvature.

---

## 111. Amnesia: 对抗 Semantic Layer Specific Activation Steering in Large Language Models

**原标题**: Amnesia: Adversarial Semantic Layer Specific Activation Steering in Large Language Models

**作者**: Ali Raza, Gurang Gupta, Nikolay Matyunin, Jibesh Patra
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10080v1

**中文摘要**:
> arXiv:2603.10080v1 Announce Type: cross 
摘要: Warning: This article includes red-teaming experiments, which contain examples of compromised 大语言模型 responses that may be offensive or upsetting.
  Large Language Models (LLMs) have the potential to create harmful content, such as generating sophisticated phishing emails and assisting in writing 代码 of harmful computer viruses. Thus, it is crucial to ensure their safe and responsible response 生成. To reduce the risk of generating harmful or irresponsible content, researchers have developed techniques such as 强化 学习 with human feedback to align 大语言模型's outputs with human values and preferences. However, it is still undetermined whether such measures are sufficient to prevent LLMs from generating interesting responses. In this study, we propose Amnes...

**Original Abstract**:
> arXiv:2603.10080v1 Announce Type: cross 
Abstract: Warning: This article includes red-teaming experiments, which contain examples of compromised LLM responses that may be offensive or upsetting.
  Large Language Models (LLMs) have the potential to create harmful content, such as generating sophisticated phishing emails and assisting in writing code of harmful computer viruses. Thus, it is crucial to ensure their safe and responsible response generation. To reduce the risk of generating harmful or irresponsible content, researchers have developed techniques such as reinforcement learning with human feedback to align LLM's outputs with human values and preferences. However, it is still undetermined whether such measures are sufficient to prevent LLMs from generating interesting responses. In...

---

## 112. Mitigating Frequency 学习 偏见 in Quantum Models via Multi-Stage Residual 学习

**原标题**: Mitigating Frequency Learning Bias in Quantum Models via Multi-Stage Residual Learning

**作者**: Ammar Daskin
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10083v1

**中文摘要**:
> arXiv:2603.10083v1 Announce Type: cross 
摘要: Quantum machine 学习 models based on parameterized circuits can be viewed as Fourier series approximators. However, they often struggle to learn functions with multiple frequency components, particularly high-frequency or non-dominant ones; a phenomenon we term the quantum Fourier parameterization 偏见. Inspired by recent advances in classical Fourier 神经 operators (FNOs), we adapt the multi-stage residual 学习 idea to the quantum domain, iteratively 训练 additional quantum modules on the residuals of previous stages. We evaluate our 方法 on a synthetic 基准 composed of spatially localized frequency components with diverse envelope shapes (Gaussian, Lorentzian, triangular). Systematic experiments show that the number of qubits, the encoding scheme, and resid...

**Original Abstract**:
> arXiv:2603.10083v1 Announce Type: cross 
Abstract: Quantum machine learning models based on parameterized circuits can be viewed as Fourier series approximators. However, they often struggle to learn functions with multiple frequency components, particularly high-frequency or non-dominant ones; a phenomenon we term the quantum Fourier parameterization bias. Inspired by recent advances in classical Fourier neural operators (FNOs), we adapt the multi-stage residual learning idea to the quantum domain, iteratively training additional quantum modules on the residuals of previous stages. We evaluate our method on a synthetic benchmark composed of spatially localized frequency components with diverse envelope shapes (Gaussian, Lorentzian, triangular). Systematic experiments show that the number ...

---

## 113. 代码-Space Response Oracles: Generating 可解释 Multi-智能体 Policies with Large Language Models

**原标题**: Code-Space Response Oracles: Generating Interpretable Multi-Agent Policies with Large Language Models

**作者**: Daniel Hennes, Zun Li, John Schultz, Marc Lanctot
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10098v1

**中文摘要**:
> arXiv:2603.10098v1 Announce Type: cross 
摘要: Recent advances in multi-智能体 强化 学习, particularly 策略-Space Response Oracles (PSRO), have enabled the computation of approximate game-theoretic equilibria in increasingly complex domains. However, these methods rely on 深度 强化 学习 oracles that produce `black-box' 神经 网络 policies, making them difficult to interpret, trust or debug. We introduce 代码-Space Response Oracles (CSRO), a novel 框架 that addresses this challenge by replacing RL oracles with Large Language Models (LLMs). CSRO reframes the best response computation as a 代码 生成 task, prompting an 大语言模型 to generate policies directly as human-readable 代码. This 方案 not only yields inherently 可解释 policies but also leverages the 大语言模型's pretrained knowledge to discover complex, human-like strategies. We ex...

**Original Abstract**:
> arXiv:2603.10098v1 Announce Type: cross 
Abstract: Recent advances in multi-agent reinforcement learning, particularly Policy-Space Response Oracles (PSRO), have enabled the computation of approximate game-theoretic equilibria in increasingly complex domains. However, these methods rely on deep reinforcement learning oracles that produce `black-box' neural network policies, making them difficult to interpret, trust or debug. We introduce Code-Space Response Oracles (CSRO), a novel framework that addresses this challenge by replacing RL oracles with Large Language Models (LLMs). CSRO reframes the best response computation as a code generation task, prompting an LLM to generate policies directly as human-readable code. This approach not only yields inherently interpretable policies but also ...

---

## 114. Stability and 鲁棒性 via 正则化: Bandit 推理 via Regularized Stochastic Mirror Descent

**原标题**: Stability and Robustness via Regularization: Bandit Inference via Regularized Stochastic Mirror Descent

**作者**: Budhaditya Halder, Ishan Sengupta, Koustav Chowdhury, Koulik Khamaru
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10184v1

**中文摘要**:
> arXiv:2603.10184v1 Announce Type: cross 
摘要: Statistical 推理 with bandit data presents fundamental challenges due to adaptive 采样, which violates the independence assumptions underlying classical asymptotic theory. Recent work has identified stability as a sufficient condition for valid 推理 under adaptivity. This 论文 develops a systematic theory of stability for bandit algorithms based on stochastic mirror descent, a broad algorithmic 框架 that includes the widely-used EXP3 算法 as a special case.
  Our contributions are threefold. First, we establish a general stability criterion: if the average iterates of a stochastic mirror descent 算法 converge in ratio to a non-random probability 向量, then the induced bandit 算法 is stable. This 结果 provides a unified lens for analyzing stability across diverse al...

**Original Abstract**:
> arXiv:2603.10184v1 Announce Type: cross 
Abstract: Statistical inference with bandit data presents fundamental challenges due to adaptive sampling, which violates the independence assumptions underlying classical asymptotic theory. Recent work has identified stability as a sufficient condition for valid inference under adaptivity. This paper develops a systematic theory of stability for bandit algorithms based on stochastic mirror descent, a broad algorithmic framework that includes the widely-used EXP3 algorithm as a special case.
  Our contributions are threefold. First, we establish a general stability criterion: if the average iterates of a stochastic mirror descent algorithm converge in ratio to a non-random probability vector, then the induced bandit algorithm is stable. This result ...

---

## 115. Adaptive Activation Cancellation for Hallucination Mitigation in Large Language Models

**原标题**: Adaptive Activation Cancellation for Hallucination Mitigation in Large Language Models

**作者**: Eric Yocam, Varghese Vaidyan, Gurcan Comert, Paris Kalathas, Yong Wang, Judith L. Mwakalonge
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10195v1

**中文摘要**:
> arXiv:2603.10195v1 Announce Type: cross 
摘要: Large Language Models frequently generate fluent but factually incorrect text. We propose Adaptive Activation Cancellation (AAC), a 实时 推理-time 框架 that treats hallucination-associated 神经 activations as structured interference within the Transformer residual stream, drawing an explicit analogy to classical adaptive noise cancellation from signal processing. The 框架 identifies Hallucination Nodes (H-Nodes) via layer-wise linear probing and suppresses them using a confidence-weighted 前向 hook during auto-regressive 生成 -- requiring no external knowledge, no fine-tuning, and no additional 推理 passes. Evaluated across OPT-125M, Phi-3-mini, and LLaMA 3-8B on TruthfulQA and HaluEval, the 实时 hook is the only intervention that consistently improves downstream...

**Original Abstract**:
> arXiv:2603.10195v1 Announce Type: cross 
Abstract: Large Language Models frequently generate fluent but factually incorrect text. We propose Adaptive Activation Cancellation (AAC), a real-time inference-time framework that treats hallucination-associated neural activations as structured interference within the transformer residual stream, drawing an explicit analogy to classical adaptive noise cancellation from signal processing. The framework identifies Hallucination Nodes (H-Nodes) via layer-wise linear probing and suppresses them using a confidence-weighted forward hook during auto-regressive generation -- requiring no external knowledge, no fine-tuning, and no additional inference passes. Evaluated across OPT-125M, Phi-3-mini, and LLaMA 3-8B on TruthfulQA and HaluEval, the real-time ho...

---

## 116. Hybrid Hidden Markov 模型 for Modeling Equity Excess Growth Rate Dynamics: A Discrete-状态 方案 with Jump-Diffusion

**原标题**: Hybrid Hidden Markov Model for Modeling Equity Excess Growth Rate Dynamics: A Discrete-State Approach with Jump-Diffusion

**作者**: Abdulrahman Alswaidan, Jeffrey D. Varner
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10202v1

**中文摘要**:
> arXiv:2603.10202v1 Announce Type: cross 
摘要: Generating synthetic financial time series that preserve statistical properties of real market data is essential for stress testing, risk 模型 validation, and scenario design. Existing approaches, from parametric models to 深度 生成式 networks, struggle to simultaneously reproduce heavy-tailed distributions, negligible linear autocorrelation, and persistent volatility clustering. We propose a hybrid hidden Markov 框架 that discretizes continuous excess growth rates into Laplace quantile-defined market states and augments regime switching with a Poisson-driven jump-duration mechanism to enforce realistic tail-状态 dwell times. Parameters are estimated by direct 转移 counting, bypassing the Baum-Welch EM 算法. Synthetic data quality is evaluated using Kolmogorov...

**Original Abstract**:
> arXiv:2603.10202v1 Announce Type: cross 
Abstract: Generating synthetic financial time series that preserve statistical properties of real market data is essential for stress testing, risk model validation, and scenario design. Existing approaches, from parametric models to deep generative networks, struggle to simultaneously reproduce heavy-tailed distributions, negligible linear autocorrelation, and persistent volatility clustering. We propose a hybrid hidden Markov framework that discretizes continuous excess growth rates into Laplace quantile-defined market states and augments regime switching with a Poisson-driven jump-duration mechanism to enforce realistic tail-state dwell times. Parameters are estimated by direct transition counting, bypassing the Baum-Welch EM algorithm. Synthetic...

---

## 117. Flexible Cutoff 学习: Optimizing Machine 学习 Potentials After 训练

**原标题**: Flexible Cutoff Learning: Optimizing Machine Learning Potentials After Training

**作者**: Rick Oerder (Institute for Numerical Simulation, University of Bonn, Fraunhofer Institute for Algorithms and Scientific Computing SCAI), Jan Hamaekers (Fraunhofer Institute for Algorithms and Scientific Computing SCAI)
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10205v1

**中文摘要**:
> arXiv:2603.10205v1 Announce Type: cross 
摘要: We introduce Flexible Cutoff 学习 (FCL), a 方法 for 训练 machine 学习 interatomic potentials (MLIPs) whose cutoff radii can be adjusted after 训练. Unlike conventional MLIPs that fix the cutoff radius during 训练, FCL models are trained by randomly 采样 cutoff radii independently for each atom. The resulting 模型 can then be deployed with different per-atom cutoff radii depending on the application, enabling application-specific 优化 of the accuracy-cost tradeoff. Using a differentiable cost 模型, these per-atom cutoffs can be optimized for specific 目标 systems after 训练. We demonstrate FCL with a modified MACE 架构 trained on the MAD 数据集. For a subset featuring molecular crystals, optimized per-atom cutoffs reduce computational cost by more than 60% while increasing f...

**Original Abstract**:
> arXiv:2603.10205v1 Announce Type: cross 
Abstract: We introduce Flexible Cutoff Learning (FCL), a method for training machine learning interatomic potentials (MLIPs) whose cutoff radii can be adjusted after training. Unlike conventional MLIPs that fix the cutoff radius during training, FCL models are trained by randomly sampling cutoff radii independently for each atom. The resulting model can then be deployed with different per-atom cutoff radii depending on the application, enabling application-specific optimization of the accuracy-cost tradeoff. Using a differentiable cost model, these per-atom cutoffs can be optimized for specific target systems after training. We demonstrate FCL with a modified MACE architecture trained on the MAD dataset. For a subset featuring molecular crystals, op...

---

## 118. FusionNet: a frame interpolation 网络 for 4D heart models

**原标题**: FusionNet: a frame interpolation network for 4D heart models

**作者**: Chujie Chang, Shoko Miyauchi, Ken'ichi Morooka, Ryo Kurazume, Oscar Martinez Mozos
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10212v1

**中文摘要**:
> arXiv:2603.10212v1 Announce Type: cross 
摘要: Cardiac magnetic resonance (CMR) imaging is widely used to visualise cardiac motion and diagnose heart disease. However, standard CMR imaging requires patients to lie still in a confined space inside a loud machine for 40-60 min, which increases patient discomfort. In addition, shorter scan times decrease either or both the temporal and spatial resolutions of cardiac motion, and thus, the diagnostic accuracy of the procedure. Of these, we focus on reduced temporal resolution and propose a 神经 网络 called FusionNet to obtain four-dimensional (4D) cardiac motion with high temporal resolution from CMR images captured in a short period of time. The 模型 estimates intermediate 3D heart shapes based on adjacent shapes. The results of an experimental 评估 of ...

**Original Abstract**:
> arXiv:2603.10212v1 Announce Type: cross 
Abstract: Cardiac magnetic resonance (CMR) imaging is widely used to visualise cardiac motion and diagnose heart disease. However, standard CMR imaging requires patients to lie still in a confined space inside a loud machine for 40-60 min, which increases patient discomfort. In addition, shorter scan times decrease either or both the temporal and spatial resolutions of cardiac motion, and thus, the diagnostic accuracy of the procedure. Of these, we focus on reduced temporal resolution and propose a neural network called FusionNet to obtain four-dimensional (4D) cardiac motion with high temporal resolution from CMR images captured in a short period of time. The model estimates intermediate 3D heart shapes based on adjacent shapes. The results of an e...

---

## 119. SDSR: A Spectral Divide-and-Conquer 方案 for Species Tree Reconstruction

**原标题**: SDSR: A Spectral Divide-and-Conquer Approach for Species Tree Reconstruction

**作者**: Ortal Reshef (Hebrew University of Jerusalem), Ofer Glassman (Weizmann Institute of Science), Or Zuk (Hebrew University of Jerusalem), Yariv Aizenbud (Tel Aviv University), Boaz Nadler (Weizmann Institute of Science), Ariel Jaffe (Hebrew University of Jerusalem)
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10215v1

**中文摘要**:
> arXiv:2603.10215v1 Announce Type: cross 
摘要: Recovering a tree that represents the evolutionary history of a group of species is a key task in phylogenetics. Performing this task using sequence data from multiple 遗传 markers poses two key challenges. The first is the discordance between the evolutionary history of individual genes and that of the species. The second challenge is computational, as contemporary studies involve thousands of species. Here we present SDSR, a 可扩展 divide-and-conquer 方案 for species tree reconstruction based on spectral graph theory. The 算法 recursively partitions the species into subsets until their sizes are below a given threshold. The trees of these subsets are reconstructed by a user-chosen species tree 算法. Finally, these subtrees are merged to form the full tre...

**Original Abstract**:
> arXiv:2603.10215v1 Announce Type: cross 
Abstract: Recovering a tree that represents the evolutionary history of a group of species is a key task in phylogenetics. Performing this task using sequence data from multiple genetic markers poses two key challenges. The first is the discordance between the evolutionary history of individual genes and that of the species. The second challenge is computational, as contemporary studies involve thousands of species. Here we present SDSR, a scalable divide-and-conquer approach for species tree reconstruction based on spectral graph theory. The algorithm recursively partitions the species into subsets until their sizes are below a given threshold. The trees of these subsets are reconstructed by a user-chosen species tree algorithm. Finally, these subt...

---

## 120. A Diffusion Analysis of 策略 梯度 for Stochastic Bandits

**原标题**: A Diffusion Analysis of Policy Gradient for Stochastic Bandits

**作者**: Tor Lattimore
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10219v1

**中文摘要**:
> arXiv:2603.10219v1 Announce Type: cross 
摘要: We study a continuous-time diffusion approximation of 策略 梯度 for $k$-armed stochastic bandits. We prove that with a 学习 rate $\eta = O(\Delta^2/\log(n))$ the regret is $O(k \log(k) \log(n) / \eta)$ where $n$ is the 视野 and $\Delta$ the minimum gap. Moreover, we construct an instance with only logarithmically many arms for which the regret is linear unless $\eta = O(\Delta^2)$.

**Original Abstract**:
> arXiv:2603.10219v1 Announce Type: cross 
Abstract: We study a continuous-time diffusion approximation of policy gradient for $k$-armed stochastic bandits. We prove that with a learning rate $\eta = O(\Delta^2/\log(n))$ the regret is $O(k \log(k) \log(n) / \eta)$ where $n$ is the horizon and $\Delta$ the minimum gap. Moreover, we construct an instance with only logarithmically many arms for which the regret is linear unless $\eta = O(\Delta^2)$.

---

## 121. A Trust-Region Interior-Point Stochastic Sequential Quadratic Programming 方法

**原标题**: A Trust-Region Interior-Point Stochastic Sequential Quadratic Programming Method

**作者**: Yuchen Fang, Jihun Kim, Sen Na, James Demmel, Javad Lavaei
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10230v1

**中文摘要**:
> arXiv:2603.10230v1 Announce Type: cross 
摘要: In this 论文, we propose a trust-region interior-point stochastic sequential quadratic programming (TR-IP-SSQP) 方法 for solving 优化 problems with a stochastic objective and deterministic nonlinear equality and inequality constraints. In this setting, exact evaluations of the objective function and its 梯度 are unavailable, but their stochastic estimates can be constructed. In particular, at each 迭代 our 方法 builds stochastic oracles, which estimate the objective 价值 and 梯度 to satisfy proper adaptive accuracy conditions with a fixed probability. To handle inequality constraints, we adopt an interior-point 方法 (IPM), in which the barrier parameter follows a prescribed decaying sequence. Under standard assumptions, we establish global almost-sure convergence...

**Original Abstract**:
> arXiv:2603.10230v1 Announce Type: cross 
Abstract: In this paper, we propose a trust-region interior-point stochastic sequential quadratic programming (TR-IP-SSQP) method for solving optimization problems with a stochastic objective and deterministic nonlinear equality and inequality constraints. In this setting, exact evaluations of the objective function and its gradient are unavailable, but their stochastic estimates can be constructed. In particular, at each iteration our method builds stochastic oracles, which estimate the objective value and gradient to satisfy proper adaptive accuracy conditions with a fixed probability. To handle inequality constraints, we adopt an interior-point method (IPM), in which the barrier parameter follows a prescribed decaying sequence. Under standard ass...

---

## 122. Why Does It Look There? Structured Explanations for 图像 分类

**原标题**: Why Does It Look There? Structured Explanations for Image Classification

**作者**: Jiarui Li, Zixiang Yin, Samuel J Landry, Zhengming Ding, Ramgopal R. Mettu
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10234v1

**中文摘要**:
> arXiv:2603.10234v1 Announce Type: cross 
摘要: 深度 学习 models achieve remarkable predictive 性能, yet their black-box nature limits transparency and trustworthiness. Although numerous 可解释 artificial intelligence (XAI) methods have been proposed, they primarily provide saliency maps or concepts (i.e., unstructured interpretability). Existing approaches often rely on auxiliary models (\eg, GPT, 截断) to describe 模型 behavior, thereby compromising faithfulness to the original models. We propose Interpretability to Explainability (I2X), a 框架 that builds structured explanations directly from unstructured interpretability by quantifying progress at selected checkpoints during 训练 using prototypes extracted from post-hoc XAI methods (e.g., GradCAM). I2X answers the question of "why does it look there" by p...

**Original Abstract**:
> arXiv:2603.10234v1 Announce Type: cross 
Abstract: Deep learning models achieve remarkable predictive performance, yet their black-box nature limits transparency and trustworthiness. Although numerous explainable artificial intelligence (XAI) methods have been proposed, they primarily provide saliency maps or concepts (i.e., unstructured interpretability). Existing approaches often rely on auxiliary models (\eg, GPT, CLIP) to describe model behavior, thereby compromising faithfulness to the original models. We propose Interpretability to Explainability (I2X), a framework that builds structured explanations directly from unstructured interpretability by quantifying progress at selected checkpoints during training using prototypes extracted from post-hoc XAI methods (e.g., GradCAM). I2X answ...

---

## 123. Intrinsic Numerical 鲁棒性 and Fault Tolerance in a Neuromorphic 算法 for Scientific Computing

**原标题**: Intrinsic Numerical Robustness and Fault Tolerance in a Neuromorphic Algorithm for Scientific Computing

**作者**: Bradley H. Theilman, James B. Aimone
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10246v1

**中文摘要**:
> arXiv:2603.10246v1 Announce Type: cross 
摘要: The potential for neuromorphic computing to provide intrinsic fault tolerance has long been speculated, but the brain's 鲁棒性 in neuromorphic applications has yet to be demonstrated. Here, we show that a previously described, natively spiking neuromorphic 算法 for solving partial differential equations is intrinsically tolerant to structural perturbations in the form of ablated neurons and dropped spikes. The tolerance band for these perturbations is large: we find that as many as 32 percent of the neurons and up to 90 percent of the spikes may be entirely dropped before a significant degradation in the accuracy results. Furthermore, this 鲁棒性 is tunable through structural hyperparameters. This work demonstrates that the specific brain-like inspirati...

**Original Abstract**:
> arXiv:2603.10246v1 Announce Type: cross 
Abstract: The potential for neuromorphic computing to provide intrinsic fault tolerance has long been speculated, but the brain's robustness in neuromorphic applications has yet to be demonstrated. Here, we show that a previously described, natively spiking neuromorphic algorithm for solving partial differential equations is intrinsically tolerant to structural perturbations in the form of ablated neurons and dropped spikes. The tolerance band for these perturbations is large: we find that as many as 32 percent of the neurons and up to 90 percent of the spikes may be entirely dropped before a significant degradation in the accuracy results. Furthermore, this robustness is tunable through structural hyperparameters. This work demonstrates that the sp...

---

## 124. 贝叶斯 Hierarchical Models and the Maximum 熵 Principle

**原标题**: Bayesian Hierarchical Models and the Maximum Entropy Principle

**作者**: Brendon J. Brewer
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10252v1

**中文摘要**:
> arXiv:2603.10252v1 Announce Type: cross 
摘要: 贝叶斯 hierarchical models are frequently used in practical data analysis contexts. One interpretation of these models is that they provide an indirect way of assigning a prior for unknown parameters, through the 引言 of hyperparameters. The resulting marginal prior for the parameters (integrating over the hyperparameters) is usually dependent, so that 学习 one parameter provides some information about the others. In this contribution, I will demonstrate that, when the prior given the hyperparameters is a canonical distribution (a maximum 熵 distribution with moment constraints), the dependent marginal prior also has a maximum 熵 property, with a different constraint. This constraint is on the marginal distribution of some function of the unknown quantit...

**Original Abstract**:
> arXiv:2603.10252v1 Announce Type: cross 
Abstract: Bayesian hierarchical models are frequently used in practical data analysis contexts. One interpretation of these models is that they provide an indirect way of assigning a prior for unknown parameters, through the introduction of hyperparameters. The resulting marginal prior for the parameters (integrating over the hyperparameters) is usually dependent, so that learning one parameter provides some information about the others. In this contribution, I will demonstrate that, when the prior given the hyperparameters is a canonical distribution (a maximum entropy distribution with moment constraints), the dependent marginal prior also has a maximum entropy property, with a different constraint. This constraint is on the marginal distribution ...

---

## 125. From Prior to Pro: 高效 Skill Mastery via Distribution Contractive RL Finetuning

**原标题**: From Prior to Pro: Efficient Skill Mastery via Distribution Contractive RL Finetuning

**作者**: Zhanyi Sun, Shuran Song
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10263v1

**中文摘要**:
> arXiv:2603.10263v1 Announce Type: cross 
摘要: We introduce Distribution Contractive 强化 学习 (DICE-RL), a 框架 that uses 强化 学习 (RL) as a "distribution contraction" operator to refine pretrained 生成式 robot policies. DICE-RL turns a pretrained behavior prior into a high-performing "pro" 策略 by amplifying high-success behaviors from 在线 feedback. We pretrain a diffusion- or flow-based 策略 for broad behavioral coverage, then finetune it with a stable, sample-高效 residual off-策略 RL 框架 that combines selective behavior 正则化 with 价值-guided 动作 选择. Extensive experiments and analyses show that DICE-RL reliably improves 性能 with strong stability and sample efficiency. It enables mastery of complex long-视野 manipulation skills directly from high-dimensional pixel inputs, both in simulation and on a real robot. Proje...

**Original Abstract**:
> arXiv:2603.10263v1 Announce Type: cross 
Abstract: We introduce Distribution Contractive Reinforcement Learning (DICE-RL), a framework that uses reinforcement learning (RL) as a "distribution contraction" operator to refine pretrained generative robot policies. DICE-RL turns a pretrained behavior prior into a high-performing "pro" policy by amplifying high-success behaviors from online feedback. We pretrain a diffusion- or flow-based policy for broad behavioral coverage, then finetune it with a stable, sample-efficient residual off-policy RL framework that combines selective behavior regularization with value-guided action selection. Extensive experiments and analyses show that DICE-RL reliably improves performance with strong stability and sample efficiency. It enables mastery of complex ...

---

## 126. MultiwayPAM: Multiway Partitioning Around Medoids for 大语言模型-as-a-Judge Score Analysis

**原标题**: MultiwayPAM: Multiway Partitioning Around Medoids for LLM-as-a-Judge Score Analysis

**作者**: Chihiro Watanabe, Jingyu Sun
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10287v1

**中文摘要**:
> arXiv:2603.10287v1 Announce Type: cross 
摘要: 大语言模型-as-a-Judge is a flexible 框架 for text 评估, which allows us to obtain scores for the quality of a given text from various perspectives by changing the prompt template. Two main challenges in using 大语言模型-as-a-Judge are computational cost of 大语言模型 推理, especially when evaluating a large number of texts, and inherent 偏见 of an 大语言模型 evaluator. To address these issues and reveal the structure of score 偏见 caused by an 大语言模型 evaluator, we propose to apply a tensor clustering 方法 to a given 大语言模型-as-a-Judge score tensor, whose entries are the scores for different combinations of questions, answerers, and evaluators. Specifically, we develop a new tensor clustering 方法 MultiwayPAM, with which we can simultaneously estimate the 集群 membership and the medoi...

**Original Abstract**:
> arXiv:2603.10287v1 Announce Type: cross 
Abstract: LLM-as-a-Judge is a flexible framework for text evaluation, which allows us to obtain scores for the quality of a given text from various perspectives by changing the prompt template. Two main challenges in using LLM-as-a-Judge are computational cost of LLM inference, especially when evaluating a large number of texts, and inherent bias of an LLM evaluator. To address these issues and reveal the structure of score bias caused by an LLM evaluator, we propose to apply a tensor clustering method to a given LLM-as-a-Judge score tensor, whose entries are the scores for different combinations of questions, answerers, and evaluators. Specifically, we develop a new tensor clustering method MultiwayPAM, with which we can simultaneously estimate the...

---

## 127. Hybrid Self-evolving Structured 内存 for GUI Agents

**原标题**: Hybrid Self-evolving Structured Memory for GUI Agents

**作者**: Sibo Zhu, Wenyi Wu, Kun Zhou, Stephen Wang, Biwei Huang
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10291v1

**中文摘要**:
> arXiv:2603.10291v1 Announce Type: cross 
摘要: The remarkable progress of vision-language models (VLMs) has enabled GUI agents to interact with computers in a human-like manner. Yet real-world computer-use tasks remain difficult due to long-视野 workflows, diverse interfaces, and frequent intermediate errors. Prior work equips agents with external 内存 built from large collections of trajectories, but relies on flat 检索 over discrete summaries or continuous embeddings, falling short of the structured organization and self-evolving characteristics of human 内存. Inspired by the brain, we propose Hybrid Self-evolving Structured 内存 (HyMEM), a graph-based 内存 that couples discrete high-level symbolic nodes with continuous 轨迹 embeddings. HyMEM maintains a graph structure to support multi-hop 检索, self-进化 ...

**Original Abstract**:
> arXiv:2603.10291v1 Announce Type: cross 
Abstract: The remarkable progress of vision-language models (VLMs) has enabled GUI agents to interact with computers in a human-like manner. Yet real-world computer-use tasks remain difficult due to long-horizon workflows, diverse interfaces, and frequent intermediate errors. Prior work equips agents with external memory built from large collections of trajectories, but relies on flat retrieval over discrete summaries or continuous embeddings, falling short of the structured organization and self-evolving characteristics of human memory. Inspired by the brain, we propose Hybrid Self-evolving Structured Memory (HyMEM), a graph-based memory that couples discrete high-level symbolic nodes with continuous trajectory embeddings. HyMEM maintains a graph s...

---

## 128. On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits

**原标题**: On The Complexity of Best-Arm Identification in Non-Stationary Linear Bandits

**作者**: Leo Maynard-Zhang, Zhihan Xiong, Kevin Jamieson, Maryam Fazel
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10346v1

**中文摘要**:
> arXiv:2603.10346v1 Announce Type: cross 
摘要: We study the fixed-budget best-arm identification (BAI) problem in non-stationary linear bandits. Concretely, given a fixed time budget $T\in \mathbb{N}$, finite arm set $\mathcal{X} \subset \mathbb{R}^d$, and a potentially 对抗 sequence of unknown parameters $\lbrace \theta_t\rbrace_{t=1}^{T}$ (hence non-stationary), a learner aims to identify the arm with the largest cumulative 奖励 $x_* = \arg\max_{x \in \mathcal{X}} x^\top\sum_{t=1}^T \theta_t$ with high probability. In this setting, it is well-known that uniformly 采样 arms from the G-optimal design yields a minimax-optimal error probability of $\exp\left(-\Theta\left(T / H_{G}\right)\right)$, where $H_{G}$ scales proportionally with the dimension $d$. However, this notion of complexity is overly...

**Original Abstract**:
> arXiv:2603.10346v1 Announce Type: cross 
Abstract: We study the fixed-budget best-arm identification (BAI) problem in non-stationary linear bandits. Concretely, given a fixed time budget $T\in \mathbb{N}$, finite arm set $\mathcal{X} \subset \mathbb{R}^d$, and a potentially adversarial sequence of unknown parameters $\lbrace \theta_t\rbrace_{t=1}^{T}$ (hence non-stationary), a learner aims to identify the arm with the largest cumulative reward $x_* = \arg\max_{x \in \mathcal{X}} x^\top\sum_{t=1}^T \theta_t$ with high probability. In this setting, it is well-known that uniformly sampling arms from the G-optimal design yields a minimax-optimal error probability of $\exp\left(-\Theta\left(T / H_{G}\right)\right)$, where $H_{G}$ scales proportionally with the dimension $d$. However, this notio...

---

## 129. HEAL: Hindsight 熵-Assisted 学习 for 推理 Distillation

**原标题**: HEAL: Hindsight Entropy-Assisted Learning for Reasoning Distillation

**作者**: Wenjing Zhang, Jiangze Yan, Jieyun Huang, Yi Shen, Shuming Shi, Ping Chen, Ning Wang, Zhaoxiang Liu, Kai Wang, Shiguo Lian
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10359v1

**中文摘要**:
> arXiv:2603.10359v1 Announce Type: cross 
摘要: Distilling 推理 capabilities from Large 推理 Models (LRMs) into smaller models is typically constrained by the limitation of rejection 采样. Standard methods treat the teacher as a 静态 filter, discarding complex "corner-case" problems where the teacher fails to explore valid solutions independently, thereby creating an artificial "Teacher Ceiling" for the student. In this work, we propose Hindsight 熵-Assisted 学习 (HEAL), an RL-free 框架 designed to bridge this 推理 gap. Drawing on the educational theory of the Zone of Proximal Development(ZPD), HEAL synergizes three core modules: (1) Guided 熵-Assisted Repair (GEAR), an active intervention mechanism that detects critical 推理 breakpoints via 熵 dynamics and injects targeted hindsight hints to repair broken traj...

**Original Abstract**:
> arXiv:2603.10359v1 Announce Type: cross 
Abstract: Distilling reasoning capabilities from Large Reasoning Models (LRMs) into smaller models is typically constrained by the limitation of rejection sampling. Standard methods treat the teacher as a static filter, discarding complex "corner-case" problems where the teacher fails to explore valid solutions independently, thereby creating an artificial "Teacher Ceiling" for the student. In this work, we propose Hindsight Entropy-Assisted Learning (HEAL), an RL-free framework designed to bridge this reasoning gap. Drawing on the educational theory of the Zone of Proximal Development(ZPD), HEAL synergizes three core modules: (1) Guided Entropy-Assisted Repair (GEAR), an active intervention mechanism that detects critical reasoning breakpoints via ...

---

## 130. Adaptive Active 学习 for Regression via 强化 学习

**原标题**: Adaptive Active Learning for Regression via Reinforcement Learning

**作者**: Simon D. Nguyen, Troy Russo, Kentaro Hoffman, Tyler H. McCormick
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10435v1

**中文摘要**:
> arXiv:2603.10435v1 Announce Type: cross 
摘要: Active 学习 for regression reduces labeling costs by selecting the most informative samples. Improved Greedy 采样 is a prominent 方法 that balances 特征-space diversity and output-space uncertainty using a 静态, multiplicative rule. We propose Weighted improved Greedy 采样 (WiGS), which replaces this 框架 with a 动态, additive criterion. We formulate weight 选择 as a 强化 学习 problem, enabling an 智能体 to adapt the 探索-investigation 平衡 throughout 学习. Experiments on 18 基准 datasets and a synthetic 环境 show WiGS outperforms iGS and other baseline methods in both accuracy and labeling efficiency, particularly in domains with irregular data density where the baseline's multiplicative rule ignores high-error samples in dense regions.

**Original Abstract**:
> arXiv:2603.10435v1 Announce Type: cross 
Abstract: Active learning for regression reduces labeling costs by selecting the most informative samples. Improved Greedy Sampling is a prominent method that balances feature-space diversity and output-space uncertainty using a static, multiplicative rule. We propose Weighted improved Greedy Sampling (WiGS), which replaces this framework with a dynamic, additive criterion. We formulate weight selection as a reinforcement learning problem, enabling an agent to adapt the exploration-investigation balance throughout learning. Experiments on 18 benchmark datasets and a synthetic environment show WiGS outperforms iGS and other baseline methods in both accuracy and labeling efficiency, particularly in domains with irregular data density where the baselin...

---

## 131. Brenier Isotonic Regression

**原标题**: Brenier Isotonic Regression

**作者**: Han Bao, Amirreza Eshraghi, Yutong Wang
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10452v1

**中文摘要**:
> arXiv:2603.10452v1 Announce Type: cross 
摘要: Isotonic regression (IR) is shape-constrained regression to maintain a univariate fitting curve non-decreasing, which has numerous applications including single-index models and probability calibration. When it comes to multi-output regression, the classical IR is no longer applicable because the monotonicity is not readily extendable. We consider a novel multi-output regression problem where a regression function is \emph{cyclically monotone}. Roughly speaking, a cyclically monotone function is the 梯度 of some convex potential. Whereas enforcing cyclic monotonicity is apparently challenging, we leverage the fact that Kantorovich's optimal transport (OT) always yields a cyclically monotone coupling as an optimal solution. This perspective natural...

**Original Abstract**:
> arXiv:2603.10452v1 Announce Type: cross 
Abstract: Isotonic regression (IR) is shape-constrained regression to maintain a univariate fitting curve non-decreasing, which has numerous applications including single-index models and probability calibration. When it comes to multi-output regression, the classical IR is no longer applicable because the monotonicity is not readily extendable. We consider a novel multi-output regression problem where a regression function is \emph{cyclically monotone}. Roughly speaking, a cyclically monotone function is the gradient of some convex potential. Whereas enforcing cyclic monotonicity is apparently challenging, we leverage the fact that Kantorovich's optimal transport (OT) always yields a cyclically monotone coupling as an optimal solution. This perspec...

---

## 132. Beam-Plasma Collective Oscillations in Intense Charged-Particle Beams: Dielectric Response Theory, Langmuir Wave Dispersion, and 无监督 检测 via Prometheus

**原标题**: Beam-Plasma Collective Oscillations in Intense Charged-Particle Beams: Dielectric Response Theory, Langmuir Wave Dispersion, and Unsupervised Detection via Prometheus

**作者**: Brandon Yee, Wilson Collins, Michael Iofin, Jiayi Fu
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10457v1

**中文摘要**:
> arXiv:2603.10457v1 Announce Type: cross 
摘要: We develop a theoretical and computational 框架 for beam-plasma collective oscillations in intense charged-particle beams at intermediate energies (10-100 MeV). In Part I, we formulate a kinetic field theory governed by the Vlasov-Poisson 系统, deriving the Lindhard dielectric function and random phase approximation (RPA) polarization tensor for three beam distribution functions. We prove via the dielectric function epsilon(omega,q)=0 the existence of undamped Langmuir wave modes above a critical beam density n_c, obtain explicit beam-plasma dispersion relations, and show that Landau damping vanishes above the particle-hole continuum. The plasma frequency Omega_p^2 = ne^2/(m*epsilon_0) is fixed by the f-sum rule independently of distribution shape; ...

**Original Abstract**:
> arXiv:2603.10457v1 Announce Type: cross 
Abstract: We develop a theoretical and computational framework for beam-plasma collective oscillations in intense charged-particle beams at intermediate energies (10-100 MeV). In Part I, we formulate a kinetic field theory governed by the Vlasov-Poisson system, deriving the Lindhard dielectric function and random phase approximation (RPA) polarization tensor for three beam distribution functions. We prove via the dielectric function epsilon(omega,q)=0 the existence of undamped Langmuir wave modes above a critical beam density n_c, obtain explicit beam-plasma dispersion relations, and show that Landau damping vanishes above the particle-hole continuum. The plasma frequency Omega_p^2 = ne^2/(m*epsilon_0) is fixed by the f-sum rule independently of dis...

---

## 133. JEDI: Jointly Embedded 推理 of 神经 Dynamics

**原标题**: JEDI: Jointly Embedded Inference of Neural Dynamics

**作者**: Anirudh Jamkhandi, Ali Korojy, Olivier Codol, Guillaume Lajoie, Matthew G. Perich
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10489v1

**中文摘要**:
> arXiv:2603.10489v1 Announce Type: cross 
摘要: Animal brains flexibly and efficiently achieve many behavioral tasks with a single 神经 网络. A core goal in modern neuroscience is to map the mechanisms of the brain's flexibility onto the dynamics underlying 神经 populations. However, identifying task-specific dynamical rules from limited, noisy, and high-dimensional experimental 神经 recordings remains a major challenge, as experimental data often provide only partial access to brain states and dynamical mechanisms. While 循环 神经 networks (RNNs) directly constrained 神经 data have been effective in inferring underlying dynamical mechanisms, they are typically limited to single-task domains and struggle to generalize across behavioral conditions. Here, we introduce JEDI, a hierarchical 模型 that captures 神经...

**Original Abstract**:
> arXiv:2603.10489v1 Announce Type: cross 
Abstract: Animal brains flexibly and efficiently achieve many behavioral tasks with a single neural network. A core goal in modern neuroscience is to map the mechanisms of the brain's flexibility onto the dynamics underlying neural populations. However, identifying task-specific dynamical rules from limited, noisy, and high-dimensional experimental neural recordings remains a major challenge, as experimental data often provide only partial access to brain states and dynamical mechanisms. While recurrent neural networks (RNNs) directly constrained neural data have been effective in inferring underlying dynamical mechanisms, they are typically limited to single-task domains and struggle to generalize across behavioral conditions. Here, we introduce JE...

---

## 134. VERI-DPO: Evidence-Aware Alignment for Clinical 摘要 via Claim Verification and Direct Preference 优化

**原标题**: VERI-DPO: Evidence-Aware Alignment for Clinical Summarization via Claim Verification and Direct Preference Optimization

**作者**: Weixin Liu, Congning Ni, Qingyuan Song, Susannah L. Rose, Christopher Symons, Murat Kantarcioglu, Bradley A. Malin, Zhijun Yin
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10494v1

**中文摘要**:
> arXiv:2603.10494v1 Announce Type: cross 
摘要: Brief Hospital Course (BHC) narratives must be clinically useful yet faithful to fragmented EHR evidence. 大语言模型-based clinical summarizers still introduce unsupported statements, and alignment can encourage omissions ("say-less" degeneration). We introduce VERI-DPO, which uses claim verification to mine preferences and distill them into the summarizer with Direct Preference 优化 (DPO). On MIMIC-III-Ext-VeriFact-BHC (100 ICU patients; patient-level splits), we train a 检索-augmented verifier to label claim-evidence pairs as Supported, Not Supported, or Not Addressed via a single-token format. The verifier scores sentence-level claims from sampled BHC candidates and aggregates margins into a coverage-aware utility to mine length-controlled, contradict...

**Original Abstract**:
> arXiv:2603.10494v1 Announce Type: cross 
Abstract: Brief Hospital Course (BHC) narratives must be clinically useful yet faithful to fragmented EHR evidence. LLM-based clinical summarizers still introduce unsupported statements, and alignment can encourage omissions ("say-less" degeneration). We introduce VERI-DPO, which uses claim verification to mine preferences and distill them into the summarizer with Direct Preference Optimization (DPO). On MIMIC-III-Ext-VeriFact-BHC (100 ICU patients; patient-level splits), we train a retrieval-augmented verifier to label claim-evidence pairs as Supported, Not Supported, or Not Addressed via a single-token format. The verifier scores sentence-level claims from sampled BHC candidates and aggregates margins into a coverage-aware utility to mine length-c...

---

## 135. Resource-constrained Amazons chess 决策 框架 integrating large language models and graph 注意力

**原标题**: Resource-constrained Amazons chess decision framework integrating large language models and graph attention

**作者**: Tianhao Qian, Zhuoxuan Li, Jinde Cao, Xinli Shi, Hanjie Liu, Leszek Rutkowski
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10512v1

**中文摘要**:
> arXiv:2603.10512v1 Announce Type: cross 
摘要: Artificial intelligence has advanced significantly through the development of intelligent game-playing systems, providing rigorous testbeds for 决策-making, strategic 规划, and adaptive 学习. However, resource-constrained environments pose critical challenges, as conventional 深度 学习 methods heavily rely on extensive datasets and computational resources. In this 论文, we propose a lightweight hybrid 框架 for the Game of the Amazons, which explores the paradigm of weak-to-strong 泛化 by integrating the structural 推理 of graph-based 学习 with the 生成式 capabilities of large language models. Specifically, we leverage a Graph 注意力 Autoencoder to inform a multi-step Monte Carlo Tree 搜索, utilize a Stochastic Graph 遗传 算法 to optimize 评估 signals, and harness GPT-4o-mini to ...

**Original Abstract**:
> arXiv:2603.10512v1 Announce Type: cross 
Abstract: Artificial intelligence has advanced significantly through the development of intelligent game-playing systems, providing rigorous testbeds for decision-making, strategic planning, and adaptive learning. However, resource-constrained environments pose critical challenges, as conventional deep learning methods heavily rely on extensive datasets and computational resources. In this paper, we propose a lightweight hybrid framework for the Game of the Amazons, which explores the paradigm of weak-to-strong generalization by integrating the structural reasoning of graph-based learning with the generative capabilities of large language models. Specifically, we leverage a Graph Attention Autoencoder to inform a multi-step Monte Carlo Tree Search, ...

---

## 136. IH-Challenge: A 训练 数据集 to Improve Instruction Hierarchy on Frontier LLMs

**原标题**: IH-Challenge: A Training Dataset to Improve Instruction Hierarchy on Frontier LLMs

**作者**: Chuan Guo (Michael Pokorny), Juan Felipe Ceron Uribe (Michael Pokorny), Sicheng Zhu (Michael Pokorny), Christopher A. Choquette-Choo (Michael Pokorny), Steph Lin (Michael Pokorny), Nikhil Kandpal (Michael Pokorny), Milad Nasr (Michael Pokorny),  Rai (Michael Pokorny), Sam Toyer, Miles Wang, Yaodong Yu, Alex Beutel, Kai Xiao
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10521v1

**中文摘要**:
> arXiv:2603.10521v1 Announce Type: cross 
摘要: Instruction hierarchy (IH) defines how LLMs prioritize 系统, developer, user, and tool instructions under conflict, providing a concrete, trust-ordered 策略 for resolving instruction conflicts. IH is key to defending against jailbreaks, 系统 prompt extractions, and agentic prompt injections. However, 鲁棒 IH behavior is difficult to train: IH failures can be confounded with instruction-following failures, conflicts can be nuanced, and models can learn shortcuts such as overrefusing. We introduce IH-Challenge, a 强化 学习 训练 数据集, to address these difficulties. Fine-tuning GPT-5-Mini on IH-Challenge with 在线 对抗 example 生成 improves IH 鲁棒性 by +10.0% on average across 16 in-distribution, 分布外, and human red-teaming benchmarks (84.1% to 94.1%), reduces unsafe behav...

**Original Abstract**:
> arXiv:2603.10521v1 Announce Type: cross 
Abstract: Instruction hierarchy (IH) defines how LLMs prioritize system, developer, user, and tool instructions under conflict, providing a concrete, trust-ordered policy for resolving instruction conflicts. IH is key to defending against jailbreaks, system prompt extractions, and agentic prompt injections. However, robust IH behavior is difficult to train: IH failures can be confounded with instruction-following failures, conflicts can be nuanced, and models can learn shortcuts such as overrefusing. We introduce IH-Challenge, a reinforcement learning training dataset, to address these difficulties. Fine-tuning GPT-5-Mini on IH-Challenge with online adversarial example generation improves IH robustness by +10.0% on average across 16 in-distribution,...

---

## 137. Quantization 鲁棒性 of Monotone Operator Equilibrium Networks

**原标题**: Quantization Robustness of Monotone Operator Equilibrium Networks

**作者**: James Li, Philip H. W. Leong, Thomas Chaffey
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10562v1

**中文摘要**:
> arXiv:2603.10562v1 Announce Type: cross 
摘要: Monotone operator equilibrium networks are implicit-layer models whose output is the unique equilibrium of a monotone operator, guaranteeing existence, uniqueness, and convergence. When deployed on low-precision hardware, weights are quantized, potentially destroying these guarantees. We analyze weight quantization as a spectral perturbation of the underlying monotone inclusion. Convergence of the quantized solver is guaranteed whenever the spectral-norm weight perturbation is smaller than the monotonicity margin; the displacement between quantized and full-precision equilibria is bounded in terms of the perturbation size and margin; and a condition number characterizing the ratio of the operator norm to the margin links quantization precision t...

**Original Abstract**:
> arXiv:2603.10562v1 Announce Type: cross 
Abstract: Monotone operator equilibrium networks are implicit-layer models whose output is the unique equilibrium of a monotone operator, guaranteeing existence, uniqueness, and convergence. When deployed on low-precision hardware, weights are quantized, potentially destroying these guarantees. We analyze weight quantization as a spectral perturbation of the underlying monotone inclusion. Convergence of the quantized solver is guaranteed whenever the spectral-norm weight perturbation is smaller than the monotonicity margin; the displacement between quantized and full-precision equilibria is bounded in terms of the perturbation size and margin; and a condition number characterizing the ratio of the operator norm to the margin links quantization preci...

---

## 138. Does 大语言模型 Alignment Really Need Diversity? An Empirical Study of Adapting RLVR Methods for Moral 推理

**原标题**: Does LLM Alignment Really Need Diversity? An Empirical Study of Adapting RLVR Methods for Moral Reasoning

**作者**: Zhaowei Zhang, Xiaohan Liu, Xuekai Zhu, Junchao Huang, Ceyao Zhang, Zhiyuan Feng, Yaodong Yang, Xiaoyuan Yi, Xing Xie
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10588v1

**中文摘要**:
> arXiv:2603.10588v1 Announce Type: cross 
摘要: 强化 学习 with verifiable rewards (RLVR) has achieved remarkable success in logical 推理 tasks, yet whether large language 模型 (大语言模型) alignment requires fundamentally different approaches remains unclear. Given the apparent tolerance for multiple valid responses in moral 推理, a natural hypothesis is that alignment tasks inherently require diversity-seeking distribution-matching algorithms rather than 奖励-maximizing 策略-based methods. We conduct the first comprehensive empirical study comparing both paradigms on MoReBench. To enable stable RLVR 训练, we build a rubric-grounded 奖励 pipeline by 训练 a Qwen3-1.7B judge 模型. Contrary to our hypothesis, we find that distribution-matching approaches do not demonstrate significant advantages over 奖励-maximizing methods...

**Original Abstract**:
> arXiv:2603.10588v1 Announce Type: cross 
Abstract: Reinforcement learning with verifiable rewards (RLVR) has achieved remarkable success in logical reasoning tasks, yet whether large language model (LLM) alignment requires fundamentally different approaches remains unclear. Given the apparent tolerance for multiple valid responses in moral reasoning, a natural hypothesis is that alignment tasks inherently require diversity-seeking distribution-matching algorithms rather than reward-maximizing policy-based methods. We conduct the first comprehensive empirical study comparing both paradigms on MoReBench. To enable stable RLVR training, we build a rubric-grounded reward pipeline by training a Qwen3-1.7B judge model. Contrary to our hypothesis, we find that distribution-matching approaches do ...

---

## 139. Self-Scaled Broyden Family of Quasi-Newton Methods in JAX

**原标题**: Self-Scaled Broyden Family of Quasi-Newton Methods in JAX

**作者**: Ivan Bioli, Mikel Mendibe Abarrategi
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10599v1

**中文摘要**:
> arXiv:2603.10599v1 Announce Type: cross 
摘要: We present a JAX 实现 of the Self-Scaled Broyden family of quasi-Newton methods, fully compatible with JAX and building on the Optimistix~\cite{rader_optimistix_2024} optimisation library. The 实现 includes BFGS, DFP, Broyden and their Self-Scaled variants(SSBFGS, SSDFP, SSBroyden), together with a Zoom line 搜索 satisfying the strong Wolfe conditions. This is a short technical note, not a research 论文, as it does not claim any novel contribution; its purpose is to document the 实现 and ease the adoption of these optimisers within the JAX community. The 代码 is available at https://GitHub.com/IvanBioli/ssbroyden_optimistix.git.

**Original Abstract**:
> arXiv:2603.10599v1 Announce Type: cross 
Abstract: We present a JAX implementation of the Self-Scaled Broyden family of quasi-Newton methods, fully compatible with JAX and building on the Optimistix~\cite{rader_optimistix_2024} optimisation library. The implementation includes BFGS, DFP, Broyden and their Self-Scaled variants(SSBFGS, SSDFP, SSBroyden), together with a Zoom line search satisfying the strong Wolfe conditions. This is a short technical note, not a research paper, as it does not claim any novel contribution; its purpose is to document the implementation and ease the adoption of these optimisers within the JAX community. The code is available at https://github.com/IvanBioli/ssbroyden_optimistix.git.

---

## 140. FAME: Formal 摘要 Minimal Explanation for 神经 Networks

**原标题**: FAME: Formal Abstract Minimal Explanation for Neural Networks

**作者**: Ryma Boumazouza, Raya Elsaleh, Melanie Ducoffe, Shahaf Bassan, Guy Katz
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10661v1

**中文摘要**:
> arXiv:2603.10661v1 Announce Type: cross 
摘要: We propose FAME (Formal 摘要 Minimal Explanations), a new class of abductive explanations grounded in 摘要 interpretation. FAME is the first 方法 to scale to large 神经 networks while reducing explanation size. Our main contribution is the design of dedicated perturbation domains that eliminate the need for traversal order. FAME progressively shrinks these domains and leverages LiRPA-based bounds to discard irrelevant features, ultimately converging to a formal 摘要 minimal explanation. To assess explanation quality, we introduce a procedure that measures the worst-case distance between an 摘要 minimal explanation and a true minimal explanation. This procedure combines 对抗 attacks with an optional VERIX+ refinement step. We 基准 FAME against VERIX+ and demonst...

**Original Abstract**:
> arXiv:2603.10661v1 Announce Type: cross 
Abstract: We propose FAME (Formal Abstract Minimal Explanations), a new class of abductive explanations grounded in abstract interpretation. FAME is the first method to scale to large neural networks while reducing explanation size. Our main contribution is the design of dedicated perturbation domains that eliminate the need for traversal order. FAME progressively shrinks these domains and leverages LiRPA-based bounds to discard irrelevant features, ultimately converging to a formal abstract minimal explanation. To assess explanation quality, we introduce a procedure that measures the worst-case distance between an abstract minimal explanation and a true minimal explanation. This procedure combines adversarial attacks with an optional VERIX+ refinem...

---

## 141. EvoSchema: Towards Text-to-SQL 鲁棒性 Against Schema 进化

**原标题**: EvoSchema: Towards Text-to-SQL Robustness Against Schema Evolution

**作者**: Tianshu Zhang, Kun Qian, Siddhartha Sahai, Yuan Tian, Shaddy Garg, Huan Sun, Yunyao Li
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10697v1

**中文摘要**:
> arXiv:2603.10697v1 Announce Type: cross 
摘要: 神经 text-to-SQL models, which translate natural language questions (NLQs) into SQL queries given a database schema, have achieved remarkable 性能. However, database schemas frequently evolve to meet new requirements. Such schema 进化 often leads to 性能 degradation for models trained on 静态 schemas. Existing work either mainly focuses on simply paraphrasing some syntactic or semantic mappings among NLQ, DB and SQL, or lacks a comprehensive and controllable way to investigate the 模型 鲁棒性 issue under the schema 进化, which is insufficient when facing the increasingly complex and rich database schema changes in reality, especially in the 大语言模型 era. To address the challenges posed by schema 进化, we present EvoSchema, a comprehensive 基准 designed to assess and en...

**Original Abstract**:
> arXiv:2603.10697v1 Announce Type: cross 
Abstract: Neural text-to-SQL models, which translate natural language questions (NLQs) into SQL queries given a database schema, have achieved remarkable performance. However, database schemas frequently evolve to meet new requirements. Such schema evolution often leads to performance degradation for models trained on static schemas. Existing work either mainly focuses on simply paraphrasing some syntactic or semantic mappings among NLQ, DB and SQL, or lacks a comprehensive and controllable way to investigate the model robustness issue under the schema evolution, which is insufficient when facing the increasingly complex and rich database schema changes in reality, especially in the LLM era. To address the challenges posed by schema evolution, we pr...

---

## 142. Sample-and-搜索: An Effective 算法 for 学习-Augmented k-Median Clustering in High dimensions

**原标题**: Sample-and-Search: An Effective Algorithm for Learning-Augmented k-Median Clustering in High dimensions

**作者**: Kangke Cheng, Shihong Song, Guanlin Mo, Hu Ding
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10721v1

**中文摘要**:
> arXiv:2603.10721v1 Announce Type: cross 
摘要: In this 论文, we investigate the 学习-augmented $k$-median clustering problem, which aims to improve the 性能 of traditional clustering algorithms by preprocessing the point set with a predictor of error rate $\alpha \in [0,1)$. This preprocessing step assigns potential labels to the points before clustering. We introduce an 算法 for this problem based on a simple yet effective 采样 方法, which substantially improves upon the time complexities of existing algorithms. Moreover, we mitigate their exponential dependency on the dimensionality of the Euclidean space. Lastly, we conduct experiments to compare our 方法 with several 状态-of-the-art 学习-augmented $k$-median clustering methods. The experimental results suggest that our proposed 方案 can significantly reduce...

**Original Abstract**:
> arXiv:2603.10721v1 Announce Type: cross 
Abstract: In this paper, we investigate the learning-augmented $k$-median clustering problem, which aims to improve the performance of traditional clustering algorithms by preprocessing the point set with a predictor of error rate $\alpha \in [0,1)$. This preprocessing step assigns potential labels to the points before clustering. We introduce an algorithm for this problem based on a simple yet effective sampling method, which substantially improves upon the time complexities of existing algorithms. Moreover, we mitigate their exponential dependency on the dimensionality of the Euclidean space. Lastly, we conduct experiments to compare our method with several state-of-the-art learning-augmented $k$-median clustering methods. The experimental results...

---

## 143. CacheSolidarity: Preventing Prefix Caching Side Channels in Multi-tenant 大语言模型 服务 Systems

**原标题**: CacheSolidarity: Preventing Prefix Caching Side Channels in Multi-tenant LLM Serving Systems

**作者**: Panagiotis Georgios Pennas, Konstantinos Papaioannou, Marco Guarnieri, Thaleia Dimitra Doudali
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10726v1

**中文摘要**:
> arXiv:2603.10726v1 Announce Type: cross 
摘要: Large Language Models (LLMs) rely on optimizations like Automatic Prefix Caching (APC) to accelerate 推理. APC works by reusing previously computed states for the beginning part of a request (prefix), when another request starts with the same text. While APC improves 吞吐量, it introduces timing side channels: cache hits are faster than misses, creating observable 延迟 differences. In multi-tenant systems, attackers can exploit these differences to infer sensitive information, e.g., by incrementally reconstructing another user's request by observing hit/miss patterns. Current defenses take a sledgehammer 方案: they disable APC and cache sharing, isolating users, and sacrificing efficiency for regular users. This 论文 presents CacheSolidarity, a 系统 that sec...

**Original Abstract**:
> arXiv:2603.10726v1 Announce Type: cross 
Abstract: Large Language Models (LLMs) rely on optimizations like Automatic Prefix Caching (APC) to accelerate inference. APC works by reusing previously computed states for the beginning part of a request (prefix), when another request starts with the same text. While APC improves throughput, it introduces timing side channels: cache hits are faster than misses, creating observable latency differences. In multi-tenant systems, attackers can exploit these differences to infer sensitive information, e.g., by incrementally reconstructing another user's request by observing hit/miss patterns. Current defenses take a sledgehammer approach: they disable APC and cache sharing, isolating users, and sacrificing efficiency for regular users. This paper prese...

---

## 144. 深度 Randomized 分布式 Function Computation (DeepRDFC): 神经 分布式 Channel Simulation

**原标题**: Deep Randomized Distributed Function Computation (DeepRDFC): Neural Distributed Channel Simulation

**作者**: Didrik Bergstr\"om, Onur G\"unl\"u
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10750v1

**中文摘要**:
> arXiv:2603.10750v1 Announce Type: cross 
摘要: The randomized 分布式 function computation (RDFC) 框架, which unifies many cutting-edge 分布式 computation and 学习 applications, is considered. An autoencoder (AE) 架构 is proposed to minimize the total variation distance between the probability distribution simulated by the AE outputs and an unknown 目标 distribution, using only data samples. We illustrate significantly high RDFC 性能 with communication load gains from our AEs compared to data compression methods. Our designs establish 深度 学习-based RDFC methods and aim to facilitate the use of RDFC methods, especially when the amount of common randomness is limited and strong function computation guarantees are required.

**Original Abstract**:
> arXiv:2603.10750v1 Announce Type: cross 
Abstract: The randomized distributed function computation (RDFC) framework, which unifies many cutting-edge distributed computation and learning applications, is considered. An autoencoder (AE) architecture is proposed to minimize the total variation distance between the probability distribution simulated by the AE outputs and an unknown target distribution, using only data samples. We illustrate significantly high RDFC performance with communication load gains from our AEs compared to data compression methods. Our designs establish deep learning-based RDFC methods and aim to facilitate the use of RDFC methods, especially when the amount of common randomness is limited and strong function computation guarantees are required.

---

## 145. A PUF-Based 方案 for Copy Protection of Intellectual Property in 神经 网络 Models

**原标题**: A PUF-Based Approach for Copy Protection of Intellectual Property in Neural Network Models

**作者**: Daniel Dorfmeister, Flavio Ferrarotti, Bernhard Fischer, Martin Schwandtner, Hannes Sochor
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10753v1

**中文摘要**:
> arXiv:2603.10753v1 Announce Type: cross 
摘要: More and more companies' Intellectual Property (IP) is being integrated into 神经 网络 (NN) models. This IP has considerable 价值 for companies and, therefore, requires adequate protection. For example, an attacker might replicate a production machines' hardware and subsequently simply copy associated software and NN models onto the cloned hardware. To make copying NN models onto cloned hardware infeasible, we present an 方案 to bind NN models - and thus also the IP contained within them - to their underlying hardware. For this purpose, we 链接 an NN 模型's weights, which are crucial for its operation, to unique and unclonable hardware properties by leveraging Physically Unclonable Functions (PUFs). By doing so, sufficient accuracy can only be achieved usin...

**Original Abstract**:
> arXiv:2603.10753v1 Announce Type: cross 
Abstract: More and more companies' Intellectual Property (IP) is being integrated into Neural Network (NN) models. This IP has considerable value for companies and, therefore, requires adequate protection. For example, an attacker might replicate a production machines' hardware and subsequently simply copy associated software and NN models onto the cloned hardware. To make copying NN models onto cloned hardware infeasible, we present an approach to bind NN models - and thus also the IP contained within them - to their underlying hardware. For this purpose, we link an NN model's weights, which are crucial for its operation, to unique and unclonable hardware properties by leveraging Physically Unclonable Functions (PUFs). By doing so, sufficient accur...

---

## 146. Taking Shortcuts for Categorical VQA Using Super Neurons

**原标题**: Taking Shortcuts for Categorical VQA Using Super Neurons

**作者**: Pierre Musacchio, Jaeyi Jeong, Dahun Kim, Jaesik Park
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10781v1

**中文摘要**:
> arXiv:2603.10781v1 Announce Type: cross 
摘要: Sparse 注意力 Vectors (SAVs) have emerged as an excellent 训练-free alternative to 有监督 finetuning or low-rank adaptation to improve the 性能 of Vision Language Models (VLMs). At their heart, SAVs select a few 准确 注意力 heads for a task of interest and use them as classifiers, rather than relying on the 模型's prediction. In a similar spirit, we find that directly probing the raw activations of the VLM, in the form of scalar values, is sufficient to yield 准确 classifiers on diverse visually grounded downstream tasks. Shifting focus from 注意力 vectors to scalar activations dramatically increases the 搜索 space for 准确 parameters, allowing us to find more 判别式 neurons immediately from the first generated token. We call such activations Super Neurons (SNs). In this pr...

**Original Abstract**:
> arXiv:2603.10781v1 Announce Type: cross 
Abstract: Sparse Attention Vectors (SAVs) have emerged as an excellent training-free alternative to supervised finetuning or low-rank adaptation to improve the performance of Vision Language Models (VLMs). At their heart, SAVs select a few accurate attention heads for a task of interest and use them as classifiers, rather than relying on the model's prediction. In a similar spirit, we find that directly probing the raw activations of the VLM, in the form of scalar values, is sufficient to yield accurate classifiers on diverse visually grounded downstream tasks. Shifting focus from attention vectors to scalar activations dramatically increases the search space for accurate parameters, allowing us to find more discriminative neurons immediately from t...

---

## 147. Towards Intelligent Spectrum Management: Spectrum Demand Estimation Using Graph 神经 Networks

**原标题**: Towards Intelligent Spectrum Management: Spectrum Demand Estimation Using Graph Neural Networks

**作者**: Mohamad Alkadamani, Amir Ghasemi, Halim Yanikomeroglu
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10802v1

**中文摘要**:
> arXiv:2603.10802v1 Announce Type: cross 
摘要: The growing demand for wireless connectivity, combined with limited spectrum resources, calls for more 高效 spectrum management. Spectrum sharing is a promising 方案; however, regulators need 准确 methods to characterize demand dynamics and guide allocation decisions. This 论文 builds and validates a spectrum demand 代理 from public 部署 records and uses a graph 注意力 网络 in a hierarchical, multi-resolution setup (HR-GAT) to estimate spectrum demand at fine spatial scales. The 模型 captures both neighborhood effects and cross-scale patterns, reducing spatial autocorrelation and improving 泛化. Evaluated across five Canadian cities and against eight competitive baselines, HR-GAT reduces median RMSE by roughly 21% relative to the best alternative and lowers residual...

**Original Abstract**:
> arXiv:2603.10802v1 Announce Type: cross 
Abstract: The growing demand for wireless connectivity, combined with limited spectrum resources, calls for more efficient spectrum management. Spectrum sharing is a promising approach; however, regulators need accurate methods to characterize demand dynamics and guide allocation decisions. This paper builds and validates a spectrum demand proxy from public deployment records and uses a graph attention network in a hierarchical, multi-resolution setup (HR-GAT) to estimate spectrum demand at fine spatial scales. The model captures both neighborhood effects and cross-scale patterns, reducing spatial autocorrelation and improving generalization. Evaluated across five Canadian cities and against eight competitive baselines, HR-GAT reduces median RMSE by...

---

## 148. ReTabSyn: Realistic Tabular Data 合成 via 强化 学习

**原标题**: ReTabSyn: Realistic Tabular Data Synthesis via Reinforcement Learning

**作者**: Xiaofeng Lin, Seungbae Kim, Zhuoya Li, Zachary DeSoto, Charles Fleming, Guang Cheng
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10823v1

**中文摘要**:
> arXiv:2603.10823v1 Announce Type: cross 
摘要: 深度 生成式 models can help with data scarcity and 隐私 by producing synthetic 训练 data, but they struggle in low-data, imbalanced tabular settings to fully learn the complex data distribution. We argue that striving for the full joint distribution could be overkill; for greater data efficiency, models should prioritize 学习 the conditional distribution $P(y\mid \bm{X})$, as suggested by recent theoretical analysis. Therefore, we overcome this limitation with \textbf{ReTabSyn}, a \textbf{Re}inforced \textbf{Tab}ular \textbf{Syn}thesis pipeline that provides direct feedback on 特征 correlation preservation during synthesizer 训练. This objective encourages the generator to prioritize the most useful predictive signals when 训练 data is limited, thereby strengthe...

**Original Abstract**:
> arXiv:2603.10823v1 Announce Type: cross 
Abstract: Deep generative models can help with data scarcity and privacy by producing synthetic training data, but they struggle in low-data, imbalanced tabular settings to fully learn the complex data distribution. We argue that striving for the full joint distribution could be overkill; for greater data efficiency, models should prioritize learning the conditional distribution $P(y\mid \bm{X})$, as suggested by recent theoretical analysis. Therefore, we overcome this limitation with \textbf{ReTabSyn}, a \textbf{Re}inforced \textbf{Tab}ular \textbf{Syn}thesis pipeline that provides direct feedback on feature correlation preservation during synthesizer training. This objective encourages the generator to prioritize the most useful predictive signals...

---

## 149. Kernel Tests of Equivalence

**原标题**: Kernel Tests of Equivalence

**作者**: Xing Liu, Axel Gandy
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10886v1

**中文摘要**:
> arXiv:2603.10886v1 Announce Type: cross 
摘要: We propose novel kernel-based tests for assessing the equivalence between distributions. Traditional goodness-of-fit testing is inappropriate for concluding the absence of distributional differences, because failure to 拒绝 the null hypothesis may simply be a 结果 of lack of test power, also known as the Type-II error. This motivates \emph{equivalence testing}, which aims to assess the \emph{absence} of a statistically meaningful effect under controlled error rates. However, existing equivalence tests are either limited to parametric distributions or focus only on specific moments rather than the full distribution. We address these limitations using two kernel-based statistical discrepancies: the \emph{kernel Stein discrepancy} and the \emph{Maximum...

**Original Abstract**:
> arXiv:2603.10886v1 Announce Type: cross 
Abstract: We propose novel kernel-based tests for assessing the equivalence between distributions. Traditional goodness-of-fit testing is inappropriate for concluding the absence of distributional differences, because failure to reject the null hypothesis may simply be a result of lack of test power, also known as the Type-II error. This motivates \emph{equivalence testing}, which aims to assess the \emph{absence} of a statistically meaningful effect under controlled error rates. However, existing equivalence tests are either limited to parametric distributions or focus only on specific moments rather than the full distribution. We address these limitations using two kernel-based statistical discrepancies: the \emph{kernel Stein discrepancy} and the...

---

## 150. ForwardFlow: Simulation only statistical 推理 using 深度 学习

**原标题**: ForwardFlow: Simulation only statistical inference using deep learning

**作者**: Stefan B\"ohringer
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10991v1

**中文摘要**:
> arXiv:2603.10991v1 Announce Type: cross 
摘要: 深度 学习 models are being used for the analysis of parametric statistical models based on simulation-only frameworks. 贝叶斯 models using normalizing flows simulate data from a prior distribution and are composed of two 深度 神经 networks: a summary 网络 that learns a sufficient statistic for the parameter and a normalizing flow that conditional on the summary 网络 can approximate the posterior distribution. Here, we explore frequentist models that are based on a single summary 网络. During 训练, input of the 网络 is a simulated data set based on a parameter and the 损失 function minimizes the mean-square error between learned summary and parameter. The 网络 thereby solves the inverse problem of parameter estimation. We propose a branched 网络 structure that contains col...

**Original Abstract**:
> arXiv:2603.10991v1 Announce Type: cross 
Abstract: Deep learning models are being used for the analysis of parametric statistical models based on simulation-only frameworks. Bayesian models using normalizing flows simulate data from a prior distribution and are composed of two deep neural networks: a summary network that learns a sufficient statistic for the parameter and a normalizing flow that conditional on the summary network can approximate the posterior distribution. Here, we explore frequentist models that are based on a single summary network. During training, input of the network is a simulated data set based on a parameter and the loss function minimizes the mean-square error between learned summary and parameter. The network thereby solves the inverse problem of parameter estima...

---

## 151. 贝叶斯 优化 with Gaussian Processes to Accelerate Stationary Point Searches

**原标题**: Bayesian Optimization with Gaussian Processes to Accelerate Stationary Point Searches

**作者**: Rohit Goswami (Institute IMX and Lab-COSMO, \'Ecole polytechnique f\'ed\'erale de Lausanne)
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10992v1

**中文摘要**:
> arXiv:2603.10992v1 Announce Type: cross 
摘要: Accelerating the explorations of stationary points on potential energy surfaces building local surrogates spans decades of effort. Done correctly, surrogates reduce required evaluations by an order of magnitude while preserving the accuracy of the underlying theory. We present a unified 贝叶斯 优化 view of minimization, single point saddle searches, and double ended saddle searches through a unified six-step surrogate loop, differing only in the inner 优化 目标 and acquisition criterion. The 框架 uses Gaussian process regression with derivative observations, inverse-distance kernels, and active 学习. The Optimal Transport GP extensions of farthest point 采样 with Earth mover's distance, MAP 正则化 via variance barrier and oscillation 检测, and adaptive trust radius...

**Original Abstract**:
> arXiv:2603.10992v1 Announce Type: cross 
Abstract: Accelerating the explorations of stationary points on potential energy surfaces building local surrogates spans decades of effort. Done correctly, surrogates reduce required evaluations by an order of magnitude while preserving the accuracy of the underlying theory. We present a unified Bayesian Optimization view of minimization, single point saddle searches, and double ended saddle searches through a unified six-step surrogate loop, differing only in the inner optimization target and acquisition criterion. The framework uses Gaussian process regression with derivative observations, inverse-distance kernels, and active learning. The Optimal Transport GP extensions of farthest point sampling with Earth mover's distance, MAP regularization v...

---

## 152. 高效 贝叶斯 Updates for 深度 Active 学习 via Laplace Approximations

**原标题**: Efficient Bayesian Updates for Deep Active Learning via Laplace Approximations

**作者**: Denis Huseljic, Marek Herde, Lukas Rauch, Paul Hahn, Zhixin Huang, Daniel Kottke, Stephan Vogt, Bernhard Sick
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2210.06112v3

**中文摘要**:
> arXiv:2210.06112v3 Announce Type: replace 
摘要: 深度 active 学习 (AL) selects batches of instances for annotation to avoid retraining 深度 神经 networks (DNNs) after each new label. Employing a naive top-$b$ 选择 can 结果 in a 批次 of redundant (similar) instances. To address this, various AL strategies employ clustering techniques that ensure diversity within a 批次. We 方案 this issue by substituting the costly retraining with an 高效 贝叶斯 update. Our proposed update represents a second-order 优化 step using the Gaussian posterior from a last-layer Laplace approximation. Thereby, we achieve low computational complexity by computing the inverse Hessian in closed form. We demonstrate that in typical AL settings, our update closely approximates retraining while being considerably faster. Leveraging our update, we ...

**Original Abstract**:
> arXiv:2210.06112v3 Announce Type: replace 
Abstract: Deep active learning (AL) selects batches of instances for annotation to avoid retraining deep neural networks (DNNs) after each new label. Employing a naive top-$b$ selection can result in a batch of redundant (similar) instances. To address this, various AL strategies employ clustering techniques that ensure diversity within a batch. We approach this issue by substituting the costly retraining with an efficient Bayesian update. Our proposed update represents a second-order optimization step using the Gaussian posterior from a last-layer Laplace approximation. Thereby, we achieve low computational complexity by computing the inverse Hessian in closed form. We demonstrate that in typical AL settings, our update closely approximates retra...

---

## 153. Improving 公平性 with Ensemble Combination: Margin-Dependent Bounds

**原标题**: Improving Fairness with Ensemble Combination: Margin-Dependent Bounds

**作者**: Yijun Bian
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2301.10813v5

**中文摘要**:
> arXiv:2301.10813v5 Announce Type: replace 
摘要: The concern about hidden discrimination in machine 学习 models is growing, as their widespread real-world applications increasingly impact human lives. Various techniques, including commonly used group 公平性 measures and several 公平性-aware ensemble-based methods, have been developed to enhance 公平性. However, existing 公平性 measures typically focus on only one aspect -- either group or individual 公平性, and the compatibility difficulty among these measures indicates a possibility of remaining biases even when one of them is satisfied. Moreover, existing mechanisms to boost 公平性 usually present empirical results to show validity, yet few of them discuss whether 公平性 can be boosted with certain theoretical guarantees. To address these issues, we propose a 公平...

**Original Abstract**:
> arXiv:2301.10813v5 Announce Type: replace 
Abstract: The concern about hidden discrimination in machine learning models is growing, as their widespread real-world applications increasingly impact human lives. Various techniques, including commonly used group fairness measures and several fairness-aware ensemble-based methods, have been developed to enhance fairness. However, existing fairness measures typically focus on only one aspect -- either group or individual fairness, and the compatibility difficulty among these measures indicates a possibility of remaining biases even when one of them is satisfied. Moreover, existing mechanisms to boost fairness usually present empirical results to show validity, yet few of them discuss whether fairness can be boosted with certain theoretical guara...

---

## 154. An 更新日期 Assessment of 强化 学习 for Macro Placement

**原标题**: An Updated Assessment of Reinforcement Learning for Macro Placement

**作者**: Chung-Kuan Cheng, Andrew B. Kahng, Sayak Kundu, Yucheng Wang, Zhiang Wang
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2302.11014v3

**中文摘要**:
> arXiv:2302.11014v3 Announce Type: replace 
摘要: We provide an improved assessment of Google Brain's 深度 强化 学习 方案 to macro placement and its 更新日期 Circuit 训练 (CT) 实现 in GitHub. A stronger simulated annealing (SA) baseline leverages the "go-with-the-winners" metaheuristic and a multi-threading 实现. We develop and release new public benchmarks in sub-10nm technology: LEF/DEF for Google's 7nm TSMC Ariane protobuf and scaled variants, as well as testcases implemented in the open-source ASAP7 7nm research enablement. We evaluate from-scratch 训练 and fine-tuning results for the latest "AlphaChip" release of Circuit 训练, alongside multiple alternative macro placers. We also study the recently-发布日期 pre-训练 guidance in. A commercial place-and-route tool is used to provide "true 奖励" post-route power, 性能 and...

**Original Abstract**:
> arXiv:2302.11014v3 Announce Type: replace 
Abstract: We provide an improved assessment of Google Brain's deep reinforcement learning approach to macro placement and its updated Circuit Training (CT) implementation in GitHub. A stronger simulated annealing (SA) baseline leverages the "go-with-the-winners" metaheuristic and a multi-threading implementation. We develop and release new public benchmarks in sub-10nm technology: LEF/DEF for Google's 7nm TSMC Ariane protobuf and scaled variants, as well as testcases implemented in the open-source ASAP7 7nm research enablement. We evaluate from-scratch training and fine-tuning results for the latest "AlphaChip" release of Circuit Training, alongside multiple alternative macro placers. We also study the recently-published pre-training guidance in. ...

---

## 155. Disjunctive Branch-and-Bound for Certifiably Optimal Low-Rank Matrix Completion

**原标题**: Disjunctive Branch-and-Bound for Certifiably Optimal Low-Rank Matrix Completion

**作者**: Dimitris Bertsimas, Ryan Cory-Wright, Sean Lo, Jean Pauphilet
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2305.12292v4

**中文摘要**:
> arXiv:2305.12292v4 Announce Type: replace 
摘要: Low-rank matrix completion consists of computing a matrix of minimal complexity that recovers a given set of observations as accurately as possible. Unfortunately, existing methods for matrix completion are heuristics that, while highly 可扩展 and often identifying high-quality solutions, do not provide an instance-wise 证书 of optimality. We reexamine matrix completion with an optimality-oriented eye. We reformulate low-rank matrix completion problems as convex problems over the non-convex set of projection matrices and implement a disjunctive branch-and-bound scheme that solves them to certifiable optimality. Further, we derive a novel and often near-exact class of convex relaxations by decomposing a low-rank matrix as a sum of rank-one matrices ...

**Original Abstract**:
> arXiv:2305.12292v4 Announce Type: replace 
Abstract: Low-rank matrix completion consists of computing a matrix of minimal complexity that recovers a given set of observations as accurately as possible. Unfortunately, existing methods for matrix completion are heuristics that, while highly scalable and often identifying high-quality solutions, do not provide an instance-wise certificate of optimality. We reexamine matrix completion with an optimality-oriented eye. We reformulate low-rank matrix completion problems as convex problems over the non-convex set of projection matrices and implement a disjunctive branch-and-bound scheme that solves them to certifiable optimality. Further, we derive a novel and often near-exact class of convex relaxations by decomposing a low-rank matrix as a sum o...

---

## 156. Optimal Transport Aggregation for 分布式 Mixture-of-Experts

**原标题**: Optimal Transport Aggregation for Distributed Mixture-of-Experts

**作者**: Fa\"icel Chamroukhi, Nhat Thien Pham
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2312.09877v2

**中文摘要**:
> arXiv:2312.09877v2 Announce Type: replace 
摘要: Mixture-of-experts (MoE) models provide a flexible statistical 框架 for modeling heterogeneity and nonlinear relationships. In many modern applications, however, datasets are naturally 分布式 across multiple machines due to 存储, computational, or governance constraints. We consider a 分布式 模型 aggregation setting in which local MoE models are trained independently on decentralized datasets and subsequently combined into a global estimator. Aggregating MoE models is challenging because standard averaging produces models that do not preserve the MoE structure, and therefore do not yield estimates of the global 模型 parameters. To address this issue, we propose a principled aggregation 框架 based on optimal transport that constructs a reduced global MoE estim...

**Original Abstract**:
> arXiv:2312.09877v2 Announce Type: replace 
Abstract: Mixture-of-experts (MoE) models provide a flexible statistical framework for modeling heterogeneity and nonlinear relationships. In many modern applications, however, datasets are naturally distributed across multiple machines due to storage, computational, or governance constraints. We consider a distributed model aggregation setting in which local MoE models are trained independently on decentralized datasets and subsequently combined into a global estimator. Aggregating MoE models is challenging because standard averaging produces models that do not preserve the MoE structure, and therefore do not yield estimates of the global model parameters. To address this issue, we propose a principled aggregation framework based on optimal trans...

---

## 157. Communication-高效 Multimodal Federated 学习: Joint Modality and 客户端 选择

**原标题**: Communication-Efficient Multimodal Federated Learning: Joint Modality and Client Selection

**作者**: Liangqi Yuan, Dong-Jun Han, Su Wang, Devesh Upadhyay, Christopher G. Brinton
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2401.16685v2

**中文摘要**:
> arXiv:2401.16685v2 Announce Type: replace 
摘要: Multimodal federated 学习 (MFL) aims to enrich 模型 训练 in FL settings where clients are collecting measurements across multiple modalities. However, key challenges to MFL remain unaddressed, particularly in heterogeneous 网络 settings where: (i) the set of modalities collected by each 客户端 is diverse, and (ii) communication limitations prevent clients from uploading all their locally trained modality encoders to the 服务器. In this 论文, we propose Multimodal Federated 学习 with joint Modality and 客户端 选择 (MFedMC), a communication-高效 MFL 框架 that tackles these challenges through a decoupled 架构 and selective uploading. Unlike traditional holistic fusion approaches, MFedMC separates modality encoders and fusion modules: modality encoders are aggregated at the 服...

**Original Abstract**:
> arXiv:2401.16685v2 Announce Type: replace 
Abstract: Multimodal federated learning (MFL) aims to enrich model training in FL settings where clients are collecting measurements across multiple modalities. However, key challenges to MFL remain unaddressed, particularly in heterogeneous network settings where: (i) the set of modalities collected by each client is diverse, and (ii) communication limitations prevent clients from uploading all their locally trained modality encoders to the server. In this paper, we propose Multimodal Federated learning with joint Modality and Client selection (MFedMC), a communication-efficient MFL framework that tackles these challenges through a decoupled architecture and selective uploading. Unlike traditional holistic fusion approaches, MFedMC separates moda...

---

## 158. Class Incremental 学习 with Task-Specific 批次 归一化 and 分布外 检测

**原标题**: Class Incremental Learning with Task-Specific Batch Normalization and Out-of-Distribution Detection

**作者**: Zhiping Zhou, Xuchen Xie, Yiqiao Qiu, Run Lin, Weishi Zheng, Ruixuan Wang
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2411.00430v2

**中文摘要**:
> arXiv:2411.00430v2 Announce Type: replace 
摘要: This study focuses on incremental 学习 for 图像 分类, exploring how to reduce catastrophic forgetting of all learned knowledge when access to old data is restricted. The challenge lies in balancing plasticity (学习 new knowledge) and stability (retaining old knowledge). Based on whether the task identifier (task-ID) is available during testing, incremental 学习 is divided into task incremental 学习 (TIL) and class incremental 学习 (CIL). The TIL paradigm often uses multiple classifier heads, selecting the corresponding head based on the task-ID. Since the CIL paradigm cannot access task-ID, methods originally developed for TIL require explicit task-ID prediction to bridge this gap and enable their adaptation to the CIL paradigm. {In this study, a novel cont...

**Original Abstract**:
> arXiv:2411.00430v2 Announce Type: replace 
Abstract: This study focuses on incremental learning for image classification, exploring how to reduce catastrophic forgetting of all learned knowledge when access to old data is restricted. The challenge lies in balancing plasticity (learning new knowledge) and stability (retaining old knowledge). Based on whether the task identifier (task-ID) is available during testing, incremental learning is divided into task incremental learning (TIL) and class incremental learning (CIL). The TIL paradigm often uses multiple classifier heads, selecting the corresponding head based on the task-ID. Since the CIL paradigm cannot access task-ID, methods originally developed for TIL require explicit task-ID prediction to bridge this gap and enable their adaptatio...

---

## 159. Boosting Cross-problem 泛化 in Diffusion-Based 神经 Combinatorial Solver via 推理 Time Adaptation

**原标题**: Boosting Cross-problem Generalization in Diffusion-Based Neural Combinatorial Solver via Inference Time Adaptation

**作者**: Haoyu Lei, Kaiwen Zhou, Yinchuan Li, Zhitang Chen, Farzan Farnia
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2502.12188v4

**中文摘要**:
> arXiv:2502.12188v4 Announce Type: replace 
摘要: Diffusion-based 神经 Combinatorial 优化 (NCO) has demonstrated effectiveness in solving NP-complete (NPC) problems by 学习 discrete diffusion models for solution 生成, eliminating hand-crafted domain knowledge. Despite their success, existing NCO methods face significant challenges in both cross-scale and cross-problem 泛化, and high 训练 costs compared to traditional solvers. While recent studies on diffusion models have introduced 训练-free guidance approaches that leverage pre-defined guidance functions for conditional 生成, such methodologies have not been extensively explored in combinatorial 优化. To bridge this gap, we propose a 训练-free 推理 time adaptation 框架 (DIFU-Ada) that enables both the 零样本 cross-problem transfer and cross-scale 泛化 capabilities of di...

**Original Abstract**:
> arXiv:2502.12188v4 Announce Type: replace 
Abstract: Diffusion-based Neural Combinatorial Optimization (NCO) has demonstrated effectiveness in solving NP-complete (NPC) problems by learning discrete diffusion models for solution generation, eliminating hand-crafted domain knowledge. Despite their success, existing NCO methods face significant challenges in both cross-scale and cross-problem generalization, and high training costs compared to traditional solvers. While recent studies on diffusion models have introduced training-free guidance approaches that leverage pre-defined guidance functions for conditional generation, such methodologies have not been extensively explored in combinatorial optimization. To bridge this gap, we propose a training-free inference time adaptation framework (...

---

## 160. Is 截断 ideal? No. Can we fix it? Yes!

**原标题**: Is CLIP ideal? No. Can we fix it? Yes!

**作者**: Raphi Kang, Yue Song, Georgia Gkioxari, Pietro Perona
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2503.08723v2

**中文摘要**:
> arXiv:2503.08723v2 Announce Type: replace 
摘要: 对比 Language-图像 Pre-训练 (截断) is a popular 方法 for 学习 multimodal 隐变量 spaces with well-organized semantics. Despite its wide range of applications, 截断's 隐变量 space is known to fail at handling complex 视觉-textual interactions. Recent works attempt to address its shortcomings with data-centric or algorithmic approaches. But what if the problem is more fundamental, and lies in the geometry of 截断? Toward this end, we rigorously analyze 截断's 隐变量 space properties, and prove that no 截断-like joint 嵌入 space exists which can correctly do any two of the following at the same time: 1. represent basic descriptions and 图像 content, 2. represent attribute binding, 3. represent spatial location and relationships, 4. represent negation. Informed by this analysis, we ...

**Original Abstract**:
> arXiv:2503.08723v2 Announce Type: replace 
Abstract: Contrastive Language-Image Pre-Training (CLIP) is a popular method for learning multimodal latent spaces with well-organized semantics. Despite its wide range of applications, CLIP's latent space is known to fail at handling complex visual-textual interactions. Recent works attempt to address its shortcomings with data-centric or algorithmic approaches. But what if the problem is more fundamental, and lies in the geometry of CLIP? Toward this end, we rigorously analyze CLIP's latent space properties, and prove that no CLIP-like joint embedding space exists which can correctly do any two of the following at the same time: 1. represent basic descriptions and image content, 2. represent attribute binding, 3. represent spatial location and r...

---

## 161. An 算法 to perform Covariance-Adjusted Support 向量 分类 in Non-Euclidean Spaces

**原标题**: An Algorithm to perform Covariance-Adjusted Support Vector Classification in Non-Euclidean Spaces

**作者**: Satyajeet Sahoo, Jhareswar Maiti
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2504.04371v3

**中文摘要**:
> arXiv:2504.04371v3 Announce Type: replace 
摘要: Traditional Support 向量 Machine (SVM) 分类 is carried out by finding the max-margin classifier for the 训练 data that divides the margin space into two equal sub-spaces. This study demonstrates limitations of performing Support 向量 分类 in non-Euclidean spaces by establishing that the underlying principle of max-margin 分类 and Karush Kuhn Tucker (KKT) boundary conditions are optimal only in the Euclidean 向量 spaces. The study establishes a methodology to perform Support 向量 分类 in Non-Euclidean Spaces by incorporating data covariance into the 优化 problem using Cholesky Decomposition of respective class covariance structure. It also demonstrates that in non-Euclidean spaces KKT modelling is sub-optimal as the principle of maximum margin is a function of int...

**Original Abstract**:
> arXiv:2504.04371v3 Announce Type: replace 
Abstract: Traditional Support Vector Machine (SVM) classification is carried out by finding the max-margin classifier for the training data that divides the margin space into two equal sub-spaces. This study demonstrates limitations of performing Support Vector Classification in non-Euclidean spaces by establishing that the underlying principle of max-margin classification and Karush Kuhn Tucker (KKT) boundary conditions are optimal only in the Euclidean vector spaces. The study establishes a methodology to perform Support Vector Classification in Non-Euclidean Spaces by incorporating data covariance into the optimization problem using Cholesky Decomposition of respective class covariance structure. It also demonstrates that in non-Euclidean space...

---

## 162. Panda: A pretrained forecast 模型 for chaotic dynamics

**原标题**: Panda: A pretrained forecast model for chaotic dynamics

**作者**: Jeffrey Lai, Anthony Bao, William Gilpin
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2505.13755v3

**中文摘要**:
> arXiv:2505.13755v3 Announce Type: replace 
摘要: Chaotic systems are intrinsically sensitive to small errors, challenging efforts to construct predictive data-driven models of real-world dynamical systems such as fluid flows or neuronal activity. Prior efforts comprise either specialized models trained on individual time series, or foundation models trained on vast time series databases with little underlying dynamical structure. Motivated by dynamical systems theory, we present Panda, Patched 注意力 for Nonlinear DynAmics. We train Panda on a novel synthetic, extensible 数据集 of $2 \times 10^4$ chaotic dynamical systems that we discover using an evolutionary 算法. Trained purely on simulated data, Panda exhibits emergent properties: 零样本 forecasting of unseen chaotic systems preserving both short-t...

**Original Abstract**:
> arXiv:2505.13755v3 Announce Type: replace 
Abstract: Chaotic systems are intrinsically sensitive to small errors, challenging efforts to construct predictive data-driven models of real-world dynamical systems such as fluid flows or neuronal activity. Prior efforts comprise either specialized models trained on individual time series, or foundation models trained on vast time series databases with little underlying dynamical structure. Motivated by dynamical systems theory, we present Panda, Patched Attention for Nonlinear DynAmics. We train Panda on a novel synthetic, extensible dataset of $2 \times 10^4$ chaotic dynamical systems that we discover using an evolutionary algorithm. Trained purely on simulated data, Panda exhibits emergent properties: zero-shot forecasting of unseen chaotic sy...

---

## 163. Comparative Analysis of Modern Machine 学习 Models for Retail Sales Forecasting

**原标题**: Comparative Analysis of Modern Machine Learning Models for Retail Sales Forecasting

**作者**: Luka Hobor, Mario Brcic, Lidija Polutnik, Ante Kapetanovic
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2506.05941v2

**中文摘要**:
> arXiv:2506.05941v2 Announce Type: replace 
摘要: 准确 demand forecasting is critical for brick-and-mortar retailers to optimize inventory management and minimize costs. This study evaluates statistical baselines, tree-based ensembles (XGBoost and LightGBM), and 深度 学习 architectures (N-BEATS, N-HiTS, and the Temporal Fusion Transformer) on retail sales data characterized by intermittent demand, substantial missingness, and frequent product turnover. Models are compared across four configurations varying by aggregation level and imputation strategy, using 评估 protocols that reflect typical 部署 patterns for each 模型 class. Localized tree-based methods achieve superior 性能, with XGBoost attaining the lowest RMSE of 4.833. While SAITS-based imputation improved 神经 网络 性能 in aggregated settings, these mode...

**Original Abstract**:
> arXiv:2506.05941v2 Announce Type: replace 
Abstract: Accurate demand forecasting is critical for brick-and-mortar retailers to optimize inventory management and minimize costs. This study evaluates statistical baselines, tree-based ensembles (XGBoost and LightGBM), and deep learning architectures (N-BEATS, N-HiTS, and the Temporal Fusion Transformer) on retail sales data characterized by intermittent demand, substantial missingness, and frequent product turnover. Models are compared across four configurations varying by aggregation level and imputation strategy, using evaluation protocols that reflect typical deployment patterns for each model class. Localized tree-based methods achieve superior performance, with XGBoost attaining the lowest RMSE of 4.833. While SAITS-based imputation impr...

---

## 164. Sequential-并行 Duality in Prefix Scannable Models

**原标题**: Sequential-Parallel Duality in Prefix Scannable Models

**作者**: Morris Yau, Sharut Gupta, Valerie Engelmayer, Kazuki Irie, Stefanie Jegelka, Jacob Andreas
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2506.10918v2

**中文摘要**:
> arXiv:2506.10918v2 Announce Type: replace 
摘要: Modern 神经 sequence models are designed to meet the dual mandate of parallelizable 训练 and fast sequential 推理. Recent developments have given rise to various models, such as Gated Linear 注意力 (GLA) and Mamba, that achieve such ``sequential-并行 duality.'' This raises a natural question: can we characterize the full class of 神经 sequence models that support near-constant-time 并行 评估 and linear-time, constant-space sequential 推理? We begin by describing a broad class of such models -- 状态 space models -- as those whose 状态 updates can be computed using the classic 并行 prefix scan 算法 with a custom associative aggregation operator. We then define a more general class, Prefix-Scannable Models (PSMs), by relaxing the 状态 aggregation operator to allow arbitrary ...

**Original Abstract**:
> arXiv:2506.10918v2 Announce Type: replace 
Abstract: Modern neural sequence models are designed to meet the dual mandate of parallelizable training and fast sequential inference. Recent developments have given rise to various models, such as Gated Linear Attention (GLA) and Mamba, that achieve such ``sequential-parallel duality.'' This raises a natural question: can we characterize the full class of neural sequence models that support near-constant-time parallel evaluation and linear-time, constant-space sequential inference? We begin by describing a broad class of such models -- state space models -- as those whose state updates can be computed using the classic parallel prefix scan algorithm with a custom associative aggregation operator. We then define a more general class, Prefix-Scann...

---

## 165. Order Optimal Regret Bounds for Sharpe Ratio 优化 under Thompson 采样

**原标题**: Order Optimal Regret Bounds for Sharpe Ratio Optimization under Thompson Sampling

**作者**: Mohammad Taha Shah, Sabrina Khurshid, Gourab Ghatak
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2508.13749v2

**中文摘要**:
> arXiv:2508.13749v2 Announce Type: replace 
摘要: In this 论文, we investigate the problem of sequential 决策-making for Sharpe ratio (SR) maximization in a stochastic bandit setting. We focus on the Thompson 采样 (TS) 算法, a 贝叶斯 方案 celebrated for its empirical 性能 and 探索 efficiency, under the assumption of Gaussian rewards with unknown parameters. Unlike conventional bandit objectives focusing on maximizing cumulative 奖励, Sharpe ratio 优化 instead introduces an inherent tradeoff between achieving high returns and controlling risk, demanding careful 探索 of both mean and variance. Our theoretical contributions include a novel regret decomposition specifically designed for the Sharpe ratio, highlighting the 角色 of information acquisition about the 奖励 distribution in driving 学习 efficiency. Then, we establis...

**Original Abstract**:
> arXiv:2508.13749v2 Announce Type: replace 
Abstract: In this paper, we investigate the problem of sequential decision-making for Sharpe ratio (SR) maximization in a stochastic bandit setting. We focus on the Thompson Sampling (TS) algorithm, a Bayesian approach celebrated for its empirical performance and exploration efficiency, under the assumption of Gaussian rewards with unknown parameters. Unlike conventional bandit objectives focusing on maximizing cumulative reward, Sharpe ratio optimization instead introduces an inherent tradeoff between achieving high returns and controlling risk, demanding careful exploration of both mean and variance. Our theoretical contributions include a novel regret decomposition specifically designed for the Sharpe ratio, highlighting the role of information...

---

## 166. GDR-learners: Orthogonal 学习 of 生成式 Models for Potential Outcomes

**原标题**: GDR-learners: Orthogonal Learning of Generative Models for Potential Outcomes

**作者**: Valentyn Melnychuk, Stefan Feuerriegel
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2509.22953v3

**中文摘要**:
> arXiv:2509.22953v3 Announce Type: replace 
摘要: Various 深度 生成式 models have been proposed to estimate potential outcomes distributions from observational data. However, none of them have the favorable theoretical property of general Neyman-orthogonality and, associated with it, quasi-oracle efficiency and double 鲁棒性. In this 论文, we introduce a general suite of 生成式 Neyman-orthogonal (doubly-鲁棒) learners that estimate the conditional distributions of potential outcomes. Our proposed 生成式 doubly-鲁棒 learners (GDR-learners) are flexible and can be instantiated with many 状态-of-the-art 深度 生成式 models. In particular, we develop GDR-learners based on (a) conditional normalizing flows (which we call GDR-CNFs), (b) conditional 生成式 对抗 networks (GDR-CGANs), (c) conditional variational autoencoders (GDR-CVA...

**Original Abstract**:
> arXiv:2509.22953v3 Announce Type: replace 
Abstract: Various deep generative models have been proposed to estimate potential outcomes distributions from observational data. However, none of them have the favorable theoretical property of general Neyman-orthogonality and, associated with it, quasi-oracle efficiency and double robustness. In this paper, we introduce a general suite of generative Neyman-orthogonal (doubly-robust) learners that estimate the conditional distributions of potential outcomes. Our proposed generative doubly-robust learners (GDR-learners) are flexible and can be instantiated with many state-of-the-art deep generative models. In particular, we develop GDR-learners based on (a) conditional normalizing flows (which we call GDR-CNFs), (b) conditional generative adversar...

---

## 167. Overlap-Adaptive 正则化 for Conditional Average Treatment Effect Estimation

**原标题**: Overlap-Adaptive Regularization for Conditional Average Treatment Effect Estimation

**作者**: Valentyn Melnychuk, Dennis Frauen, Jonas Schweisthal, Stefan Feuerriegel
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2509.24962v3

**中文摘要**:
> arXiv:2509.24962v3 Announce Type: replace 
摘要: The conditional average treatment effect (CATE) is widely used in personalized medicine to inform therapeutic decisions. However, 状态-of-the-art methods for CATE estimation (so-called meta-learners) often perform poorly in the presence of low overlap. In this work, we introduce a new 方案 to tackle this issue and improve the 性能 of existing meta-learners in the low-overlap regions. Specifically, we introduce Overlap-Adaptive 正则化 (OAR) that regularizes 目标 models proportionally to overlap weights so that, informally, the 正则化 is higher in regions with low overlap. To the best of our knowledge, our OAR is the first 方案 to leverage overlap weights in the 正则化 terms of the meta-learners. Our OAR 方案 is flexible and works with any existing CATE meta-learner...

**Original Abstract**:
> arXiv:2509.24962v3 Announce Type: replace 
Abstract: The conditional average treatment effect (CATE) is widely used in personalized medicine to inform therapeutic decisions. However, state-of-the-art methods for CATE estimation (so-called meta-learners) often perform poorly in the presence of low overlap. In this work, we introduce a new approach to tackle this issue and improve the performance of existing meta-learners in the low-overlap regions. Specifically, we introduce Overlap-Adaptive Regularization (OAR) that regularizes target models proportionally to overlap weights so that, informally, the regularization is higher in regions with low overlap. To the best of our knowledge, our OAR is the first approach to leverage overlap weights in the regularization terms of the meta-learners. O...

---

## 168. Composer: A 搜索 框架 for Hybrid 神经 架构 Design

**原标题**: Composer: A Search Framework for Hybrid Neural Architecture Design

**作者**: Bilge Acun, Prasoon Sinha, Newsha Ardalani, Sangmin Bae, Alicia Golden, Chien-Yu Lin, Meghana Madhyastha, Fei Sun, Neeraja J. Yadwadkar, Carole-Jean Wu
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2510.00379v2

**中文摘要**:
> arXiv:2510.00379v2 Announce Type: replace 
摘要: Hybrid 模型 architectures that combine computational primitives (e.g., 注意力, MLP) in different ratios have shown promising 性能 beyond Transformers. Some studies have shown that different interleavings of primitives can affect 模型 quality as well. However, prior works explore the hybrid 模型 架构 design space manually. Due to the large design space and 训练 costs, discovering hybrid models that combine key computational primitives for pre-训练 is challenging. In this work, we take a principled 方案 in designing a modular hybrid 模型 架构 搜索 框架 -- Composer. Composer explores 模型 architectures at a small scale and extrapolates the top-performing 模型 architectures to a larger scale using our proposed scaling strategies. Using Composer, we discover new hybrid 大语言模型 arc...

**Original Abstract**:
> arXiv:2510.00379v2 Announce Type: replace 
Abstract: Hybrid model architectures that combine computational primitives (e.g., Attention, MLP) in different ratios have shown promising performance beyond Transformers. Some studies have shown that different interleavings of primitives can affect model quality as well. However, prior works explore the hybrid model architecture design space manually. Due to the large design space and training costs, discovering hybrid models that combine key computational primitives for pre-training is challenging. In this work, we take a principled approach in designing a modular hybrid model architecture search framework -- Composer. Composer explores model architectures at a small scale and extrapolates the top-performing model architectures to a larger scale...

---

## 169. Communication Enables Cooperation in 大语言模型 Agents: A Comparison with Curriculum-Based Approaches

**原标题**: Communication Enables Cooperation in LLM Agents: A Comparison with Curriculum-Based Approaches

**作者**: Hachem Madmoun, Salem Lahlou
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2510.05748v3

**中文摘要**:
> arXiv:2510.05748v3 Announce Type: replace 
摘要: Eliciting cooperation in multi-智能体 大语言模型 systems is critical for AI alignment. We investigate two approaches: direct communication and curriculum 学习. In a 4-player Stag Hunt, a one-word "cheap talk" channel increases cooperation from 0% to 96.7%, demonstrating communication as a 鲁棒 coordination mechanism. In contrast, we find that curriculum 学习 is highly sensitive to design choices: our pedagogical curriculum through progressively complex games reduced 智能体 payoffs by 27.4% in an Iterated Public Goods Game with Punishment, demonstrating that optimizing for short-term rationality can actively undermine alignment goals. Qualitative analysis reveals that curricula emphasizing defection-equilibrium games can induce "learned pessimism" in agents. Th...

**Original Abstract**:
> arXiv:2510.05748v3 Announce Type: replace 
Abstract: Eliciting cooperation in multi-agent LLM systems is critical for AI alignment. We investigate two approaches: direct communication and curriculum learning. In a 4-player Stag Hunt, a one-word "cheap talk" channel increases cooperation from 0% to 96.7%, demonstrating communication as a robust coordination mechanism. In contrast, we find that curriculum learning is highly sensitive to design choices: our pedagogical curriculum through progressively complex games reduced agent payoffs by 27.4% in an Iterated Public Goods Game with Punishment, demonstrating that optimizing for short-term rationality can actively undermine alignment goals. Qualitative analysis reveals that curricula emphasizing defection-equilibrium games can induce "learned ...

---

## 170. Reveal-to-Revise: 可解释 偏见-Aware 生成式 Modeling with Multimodal 注意力

**原标题**: Reveal-to-Revise: Explainable Bias-Aware Generative Modeling with Multimodal Attention

**作者**: Noor Islam S. Mohammad, Md Muntaqim Meherab
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2510.12957v2

**中文摘要**:
> arXiv:2510.12957v2 Announce Type: replace 
摘要: We present an 可解释, 偏见-aware 生成式 框架 that unifies cross-modal 注意力 fusion, Grad-CAM++ attribution, and a Reveal-to-Revise feedback loop within a single 训练 paradigm. The 架构 couples a conditional 注意力 WGAN GP with 偏见 正则化 and iterative local explanation feedback and is evaluated on Multimodal MNIST and Fashion MNIST for 图像 生成 and subgroup auditing, as well as a toxic/non-toxic text 分类 基准. All experiments use stratified 80/20 splits, validation-based early stopping, and AdamW with cosine annealing, and results are averaged over three random seeds. The proposed 模型 achieves 93.2% accuracy, a 91.6% F1-score, and a 78.1% IoU-XAI on the multimodal 基准, outperforming all baselines across every metric, while 对抗 训练 restores 73 to 77% 鲁棒性 on Fashion MNIST. Abla...

**Original Abstract**:
> arXiv:2510.12957v2 Announce Type: replace 
Abstract: We present an explainable, bias-aware generative framework that unifies cross-modal attention fusion, Grad-CAM++ attribution, and a Reveal-to-Revise feedback loop within a single training paradigm. The architecture couples a conditional attention WGAN GP with bias regularization and iterative local explanation feedback and is evaluated on Multimodal MNIST and Fashion MNIST for image generation and subgroup auditing, as well as a toxic/non-toxic text classification benchmark. All experiments use stratified 80/20 splits, validation-based early stopping, and AdamW with cosine annealing, and results are averaged over three random seeds. The proposed model achieves 93.2% accuracy, a 91.6% F1-score, and a 78.1% IoU-XAI on the multimodal benchm...

---

## 171. Absolute indices for determining compactness, separability and number of clusters

**原标题**: Absolute indices for determining compactness, separability and number of clusters

**作者**: Adil M. Bagirov, Ramiz M. Aliguliyev, Nargiz Sultanova, Sona Taheri
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2510.13065v2

**中文摘要**:
> arXiv:2510.13065v2 Announce Type: replace 
摘要: Finding "true" clusters in a data set is a challenging problem. Clustering solutions obtained using different models and algorithms do not necessarily provide compact and well-separated clusters or the optimal number of clusters. 集群 validity indices are commonly applied to identify such clusters. Nevertheless, these indices are typically relative, and they are used to compare clustering algorithms or choose the parameters of a clustering 算法. Moreover, the success of these indices depends on the underlying data structure. This 论文 introduces novel absolute 集群 indices to determine both the compactness and separability of clusters. We define a compactness function for each 集群 and a set of neighboring points for 集群 pairs. This function is utilized ...

**Original Abstract**:
> arXiv:2510.13065v2 Announce Type: replace 
Abstract: Finding "true" clusters in a data set is a challenging problem. Clustering solutions obtained using different models and algorithms do not necessarily provide compact and well-separated clusters or the optimal number of clusters. Cluster validity indices are commonly applied to identify such clusters. Nevertheless, these indices are typically relative, and they are used to compare clustering algorithms or choose the parameters of a clustering algorithm. Moreover, the success of these indices depends on the underlying data structure. This paper introduces novel absolute cluster indices to determine both the compactness and separability of clusters. We define a compactness function for each cluster and a set of neighboring points for clust...

---

## 172. Predicting kernel regression 学习 curves from only raw data statistics

**原标题**: Predicting kernel regression learning curves from only raw data statistics

**作者**: Dhruva Karkada, Joseph Turnbull, Yuxi Liu, James B. Simon
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2510.14878v2

**中文摘要**:
> arXiv:2510.14878v2 Announce Type: replace 
摘要: We study kernel regression with common rotation-invariant kernels on real datasets including CIFAR-5m, SVHN, and ImageNet. We give a theoretical 框架 that predicts 学习 curves (test risk vs. sample size) from only two measurements: the empirical data covariance matrix and an empirical polynomial decomposition of the 目标 function $f_*$. The key new idea is an analytical approximation of a kernel's eigenvalues and eigenfunctions with respect to an anisotropic data distribution. The eigenfunctions resemble Hermite polynomials of the data, so we call this approximation the Hermite eigenstructure ansatz (HEA). We prove the HEA for Gaussian data, but we find that real 图像 data is often "Gaussian enough" for the HEA to hold well in practice, enabling us to...

**Original Abstract**:
> arXiv:2510.14878v2 Announce Type: replace 
Abstract: We study kernel regression with common rotation-invariant kernels on real datasets including CIFAR-5m, SVHN, and ImageNet. We give a theoretical framework that predicts learning curves (test risk vs. sample size) from only two measurements: the empirical data covariance matrix and an empirical polynomial decomposition of the target function $f_*$. The key new idea is an analytical approximation of a kernel's eigenvalues and eigenfunctions with respect to an anisotropic data distribution. The eigenfunctions resemble Hermite polynomials of the data, so we call this approximation the Hermite eigenstructure ansatz (HEA). We prove the HEA for Gaussian data, but we find that real image data is often "Gaussian enough" for the HEA to hold well i...

---

## 173. Revisiting 价值 迭代: Unified Analysis of Discounted and Average-奖励 Cases

**原标题**: Revisiting Value Iteration: Unified Analysis of Discounted and Average-Reward Cases

**作者**: Arsenii Mustafin, Xinyi Sheng, Dominik Baumann
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2510.23914v2

**中文摘要**:
> arXiv:2510.23914v2 Announce Type: replace 
摘要: While 价值 迭代 (VI) is one of the most fundamental algorithms in 强化 学习, its theoretical convergence guarantees still exhibit a persistent mismatch with empirical behavior. In the discounted-奖励 case, classical theory guarantees geometric convergence with rate $\gamma$, while in the average-奖励 case recent work suggests that only sublinear convergence can be expected. In practice, however, VI is often observed to converge significantly faster. In this work, we show through a unified geometry-based analysis that, under an assumption of a unique and unichain optimal 策略, (i) convergence is geometric in both the discounted- and average-奖励 settings and (ii) the convergence rate is faster than previous analyses suggest.

**Original Abstract**:
> arXiv:2510.23914v2 Announce Type: replace 
Abstract: While Value Iteration (VI) is one of the most fundamental algorithms in Reinforcement Learning, its theoretical convergence guarantees still exhibit a persistent mismatch with empirical behavior. In the discounted-reward case, classical theory guarantees geometric convergence with rate $\gamma$, while in the average-reward case recent work suggests that only sublinear convergence can be expected. In practice, however, VI is often observed to converge significantly faster. In this work, we show through a unified geometry-based analysis that, under an assumption of a unique and unichain optimal policy, (i) convergence is geometric in both the discounted- and average-reward settings and (ii) the convergence rate is faster than previous anal...

---

## 174. STREAM-VAE: Dual-Path Routing for Slow and Fast Dynamics in Vehicle Telemetry Anomaly 检测

**原标题**: STREAM-VAE: Dual-Path Routing for Slow and Fast Dynamics in Vehicle Telemetry Anomaly Detection

**作者**: Kadir-Kaan \"Ozer, Ren\'e Ebeling, Markus Enzweiler
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2511.15339v2

**中文摘要**:
> arXiv:2511.15339v2 Announce Type: replace 
摘要: Automotive telemetry data exhibits slow drifts and fast spikes, often within the same sequence, making reliable anomaly 检测 challenging. Standard reconstruction-based methods, including sequence variational autoencoders (VAEs), use a single 隐变量 process and therefore mix heterogeneous time scales, which can smooth out spikes or inflate variances and weaken anomaly separation.
  In this 论文, we present STREAM-VAE, a variational autoencoder for anomaly 检测 in automotive telemetry time-series data. Our 模型 uses a dual-path encoder to separate slow drift and fast spike signal dynamics, and a decoder that represents transient deviations separately from the normal operating pattern. STREAM-VAE is designed for 部署, producing stable anomaly scores across op...

**Original Abstract**:
> arXiv:2511.15339v2 Announce Type: replace 
Abstract: Automotive telemetry data exhibits slow drifts and fast spikes, often within the same sequence, making reliable anomaly detection challenging. Standard reconstruction-based methods, including sequence variational autoencoders (VAEs), use a single latent process and therefore mix heterogeneous time scales, which can smooth out spikes or inflate variances and weaken anomaly separation.
  In this paper, we present STREAM-VAE, a variational autoencoder for anomaly detection in automotive telemetry time-series data. Our model uses a dual-path encoder to separate slow drift and fast spike signal dynamics, and a decoder that represents transient deviations separately from the normal operating pattern. STREAM-VAE is designed for deployment, prod...

---

## 175. Hierarchical Dual-Strategy Unlearning for Biomedical and Healthcare Intelligence Using Imperfect and 隐私-Sensitive Medical Data

**原标题**: Hierarchical Dual-Strategy Unlearning for Biomedical and Healthcare Intelligence Using Imperfect and Privacy-Sensitive Medical Data

**作者**: Yi Zhang, Chao Zhang, Zijian Li, Tianxiang Xu, Kunyu Zhang, Zhan Gao, Meinuo Li, Xiaohan Zhang, Qichao Qi, Bing Chen
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2511.19498v2

**中文摘要**:
> arXiv:2511.19498v2 Announce Type: replace 
摘要: Large language models (LLMs) exhibit exceptional 性能 but pose substantial 隐私 risks due to 训练 data memorization, particularly within healthcare contexts involving imperfect or 隐私-sensitive patient information. We present a hierarchical dual-strategy 框架 for selective knowledge unlearning that precisely removes specialized knowledge while preserving fundamental medical competencies. Our 方案 synergistically integrates geometric-constrained 梯度 updates to selectively modulate 目标 parameters with concept-aware token-level interventions that distinguish between preservation-critical and unlearning-targeted tokens via a unified four-level medical concept hierarchy. Comprehensive evaluations on the MedMCQA (surgical) and MHQA (anxiety, depression, trauma) ...

**Original Abstract**:
> arXiv:2511.19498v2 Announce Type: replace 
Abstract: Large language models (LLMs) exhibit exceptional performance but pose substantial privacy risks due to training data memorization, particularly within healthcare contexts involving imperfect or privacy-sensitive patient information. We present a hierarchical dual-strategy framework for selective knowledge unlearning that precisely removes specialized knowledge while preserving fundamental medical competencies. Our approach synergistically integrates geometric-constrained gradient updates to selectively modulate target parameters with concept-aware token-level interventions that distinguish between preservation-critical and unlearning-targeted tokens via a unified four-level medical concept hierarchy. Comprehensive evaluations on the MedM...

---

## 176. Partially Equivariant 强化 学习 in Symmetry-Breaking Environments

**原标题**: Partially Equivariant Reinforcement Learning in Symmetry-Breaking Environments

**作者**: Junwoo Chang, Minwoo Park, Joohwan Seo, Roberto Horowitz, Jongmin Lee, Jongeun Choi
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2512.00915v2

**中文摘要**:
> arXiv:2512.00915v2 Announce Type: replace 
摘要: Group symmetries provide a powerful inductive 偏见 for 强化 学习 (RL), enabling 高效 泛化 across symmetric states and actions via group-invariant Markov 决策 Processes (MDPs). However, real-world environments almost never realize fully group-invariant MDPs; dynamics, actuation limits, and 奖励 design usually break symmetries, often only locally. Under group-invariant Bellman backups for such cases, local symmetry-breaking introduces errors that propagate across the entire 状态-动作 space, resulting in global 价值 estimation errors. To address this, we introduce Partially group-Invariant MDP (PI-MDP), which selectively applies group-invariant or standard Bellman backups depending on where symmetry holds. This 框架 mitigates error propagation from locally broken symm...

**Original Abstract**:
> arXiv:2512.00915v2 Announce Type: replace 
Abstract: Group symmetries provide a powerful inductive bias for reinforcement learning (RL), enabling efficient generalization across symmetric states and actions via group-invariant Markov Decision Processes (MDPs). However, real-world environments almost never realize fully group-invariant MDPs; dynamics, actuation limits, and reward design usually break symmetries, often only locally. Under group-invariant Bellman backups for such cases, local symmetry-breaking introduces errors that propagate across the entire state-action space, resulting in global value estimation errors. To address this, we introduce Partially group-Invariant MDP (PI-MDP), which selectively applies group-invariant or standard Bellman backups depending on where symmetry hol...

---

## 177. Saddle-to-Saddle Dynamics Explains A Simplicity 偏见 Across 神经 网络 Architectures

**原标题**: Saddle-to-Saddle Dynamics Explains A Simplicity Bias Across Neural Network Architectures

**作者**: Yedi Zhang, Andrew Saxe, Peter E. Latham
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2512.20607v2

**中文摘要**:
> arXiv:2512.20607v2 Announce Type: replace 
摘要: 神经 networks trained with 梯度 descent often learn solutions of increasing complexity over time, a phenomenon known as simplicity 偏见. Despite being widely observed across architectures, existing theoretical treatments lack a unifying 框架. We present a theoretical 框架 that explains a simplicity 偏见 arising from saddle-to-saddle 学习 dynamics for a general class of 神经 networks, incorporating fully-connected, convolutional, and 注意力-based architectures. Here, simple means expressible with few hidden units, i.e., hidden neurons, convolutional kernels, or 注意力 heads. Specifically, we show that linear networks learn solutions of increasing rank, ReLU networks learn solutions with an increasing number of kinks, convolutional networks learn solutions with an in...

**Original Abstract**:
> arXiv:2512.20607v2 Announce Type: replace 
Abstract: Neural networks trained with gradient descent often learn solutions of increasing complexity over time, a phenomenon known as simplicity bias. Despite being widely observed across architectures, existing theoretical treatments lack a unifying framework. We present a theoretical framework that explains a simplicity bias arising from saddle-to-saddle learning dynamics for a general class of neural networks, incorporating fully-connected, convolutional, and attention-based architectures. Here, simple means expressible with few hidden units, i.e., hidden neurons, convolutional kernels, or attention heads. Specifically, we show that linear networks learn solutions of increasing rank, ReLU networks learn solutions with an increasing number of ...

---

## 178. The 贝叶斯 Geometry of Transformer 注意力

**原标题**: The Bayesian Geometry of Transformer Attention

**作者**: Naman Agarwal, Siddhartha R. Dalal, Vishal Misra
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2512.22471v4

**中文摘要**:
> arXiv:2512.22471v4 Announce Type: replace 
摘要: Transformers often appear to perform 贝叶斯 推理 in context, but verifying this rigorously has been impossible: natural data lack analytic posteriors, and large models conflate 推理 with memorization. We address this by constructing \emph{贝叶斯 wind tunnels} -- controlled environments where the true posterior is known in closed form and memorization is provably impossible. In these settings, small transformers reproduce 贝叶斯 posteriors with $10^{-3}$-$10^{-4}$ bit accuracy, while capacity-matched MLPs fail by orders of magnitude, establishing a clear architectural separation.
  Across two tasks -- bijection elimination and Hidden Markov 模型 (HMM) 状态 tracking -- we find that transformers implement 贝叶斯 推理 through a consistent geometric mechanism: residual ...

**Original Abstract**:
> arXiv:2512.22471v4 Announce Type: replace 
Abstract: Transformers often appear to perform Bayesian reasoning in context, but verifying this rigorously has been impossible: natural data lack analytic posteriors, and large models conflate reasoning with memorization. We address this by constructing \emph{Bayesian wind tunnels} -- controlled environments where the true posterior is known in closed form and memorization is provably impossible. In these settings, small transformers reproduce Bayesian posteriors with $10^{-3}$-$10^{-4}$ bit accuracy, while capacity-matched MLPs fail by orders of magnitude, establishing a clear architectural separation.
  Across two tasks -- bijection elimination and Hidden Markov Model (HMM) state tracking -- we find that transformers implement Bayesian inferenc...

---

## 179. Over-Searching in 搜索-Augmented Large Language Models

**原标题**: Over-Searching in Search-Augmented Large Language Models

**作者**: Roy Xie, Deepak Gopinath, David Qiu, Dong Lin, Haitian Sun, Saloni Potdar, Bhuwan Dhingra
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2601.05503v2

**中文摘要**:
> arXiv:2601.05503v2 Announce Type: replace 
摘要: 搜索-augmented large language models (LLMs) excel at knowledge-intensive tasks by integrating external 检索. However, they often over-搜索 -- unnecessarily invoking 搜索 tool even when it does not improve response quality, which leads to computational inefficiency and hallucinations by incorporating irrelevant context. In this work, we conduct a systematic 评估 of over-searching across multiple dimensions, including query types, 模型 categories, 检索 conditions, and multi-turn conversations. Our finding shows: (i) 搜索 generally improves answer accuracy on answerable queries but harms abstention on unanswerable ones; (ii) over-searching is more pronounced in complex 推理 models and 深度 research systems, is exacerbated by noisy 检索, and compounds across turns in m...

**Original Abstract**:
> arXiv:2601.05503v2 Announce Type: replace 
Abstract: Search-augmented large language models (LLMs) excel at knowledge-intensive tasks by integrating external retrieval. However, they often over-search -- unnecessarily invoking search tool even when it does not improve response quality, which leads to computational inefficiency and hallucinations by incorporating irrelevant context. In this work, we conduct a systematic evaluation of over-searching across multiple dimensions, including query types, model categories, retrieval conditions, and multi-turn conversations. Our finding shows: (i) search generally improves answer accuracy on answerable queries but harms abstention on unanswerable ones; (ii) over-searching is more pronounced in complex reasoning models and deep research systems, is ...

---

## 180. Time series forecasting with Hahn Kolmogorov-Arnold networks

**原标题**: Time series forecasting with Hahn Kolmogorov-Arnold networks

**作者**: Md Zahidul Hasan, A. Ben Hamza, Nizar Bouguila
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2601.18837v2

**中文摘要**:
> arXiv:2601.18837v2 Announce Type: replace 
摘要: Recent Transformer- and MLP-based models have demonstrated strong 性能 in long-term time series forecasting, yet Transformers remain limited by their quadratic complexity and permutation-equivariant 注意力, while MLPs exhibit spectral 偏见. We propose HaKAN, a versatile 模型 based on Kolmogorov-Arnold Networks (KANs), leveraging Hahn polynomial-based learnable activation functions and providing a lightweight and 可解释 alternative for multivariate time series forecasting. Our 模型 integrates channel independence, patching, a stack of Hahn-KAN blocks with residual connections, and a bottleneck structure comprised of two fully connected layers. The Hahn-KAN block consists of inter- and intra-patch KAN layers to effectively capture both global and local tempor...

**Original Abstract**:
> arXiv:2601.18837v2 Announce Type: replace 
Abstract: Recent Transformer- and MLP-based models have demonstrated strong performance in long-term time series forecasting, yet Transformers remain limited by their quadratic complexity and permutation-equivariant attention, while MLPs exhibit spectral bias. We propose HaKAN, a versatile model based on Kolmogorov-Arnold Networks (KANs), leveraging Hahn polynomial-based learnable activation functions and providing a lightweight and interpretable alternative for multivariate time series forecasting. Our model integrates channel independence, patching, a stack of Hahn-KAN blocks with residual connections, and a bottleneck structure comprised of two fully connected layers. The Hahn-KAN block consists of inter- and intra-patch KAN layers to effective...

---

## 181. Hallucination is a Consequence of Space-Optimality: A Rate-Distortion Theorem for Membership Testing

**原标题**: Hallucination is a Consequence of Space-Optimality: A Rate-Distortion Theorem for Membership Testing

**作者**: Anxin Guo, Jingwei Li
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2602.00906v5

**中文摘要**:
> arXiv:2602.00906v5 Announce Type: replace 
摘要: Large language models often hallucinate with high confidence on "random facts" that lack inferable patterns. We formalize the memorization of such facts as a membership testing problem, unifying the discrete error metrics of Bloom filters with the continuous log-损失 of LLMs. By analyzing this problem in the regime where facts are sparse in the universe of plausible claims, we establish a rate-distortion theorem: the optimal 内存 efficiency is characterized by the minimum KL divergence between score distributions on facts and non-facts. This theoretical 框架 provides a distinctive explanation for hallucination: even with optimal 训练, perfect data, and a simplified "closed world" setting, the information-theoretically optimal strategy under limited ca...

**Original Abstract**:
> arXiv:2602.00906v5 Announce Type: replace 
Abstract: Large language models often hallucinate with high confidence on "random facts" that lack inferable patterns. We formalize the memorization of such facts as a membership testing problem, unifying the discrete error metrics of Bloom filters with the continuous log-loss of LLMs. By analyzing this problem in the regime where facts are sparse in the universe of plausible claims, we establish a rate-distortion theorem: the optimal memory efficiency is characterized by the minimum KL divergence between score distributions on facts and non-facts. This theoretical framework provides a distinctive explanation for hallucination: even with optimal training, perfect data, and a simplified "closed world" setting, the information-theoretically optimal ...

---

## 182. Position: Beyond 模型-Centric Prediction -- Agentic Time Series Forecasting

**原标题**: Position: Beyond Model-Centric Prediction -- Agentic Time Series Forecasting

**作者**: Mingyue Cheng, Xiaoyu Tao, Qi Liu, Ze Guo, Enhong Chen
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2602.01776v4

**中文摘要**:
> arXiv:2602.01776v4 Announce Type: replace 
摘要: Time series forecasting has traditionally been formulated as a 模型-centric, 静态, and single-pass prediction problem that maps historical observations to future values. While this paradigm has driven substantial progress, it proves insufficient in adaptive and multi-turn settings where forecasting requires informative 特征 extraction, 推理-driven 推理, iterative refinement, and continual adaptation over time. In this 论文, we argue for agentic time series forecasting (ATSF), which reframes forecasting as an agentic process composed of perception, 规划, 动作, reflection, and 内存. Rather than focusing solely on predictive models, ATSF emphasizes organizing forecasting as an agentic workflow that can interact with tools, incorporate feedback from outcomes, and e...

**Original Abstract**:
> arXiv:2602.01776v4 Announce Type: replace 
Abstract: Time series forecasting has traditionally been formulated as a model-centric, static, and single-pass prediction problem that maps historical observations to future values. While this paradigm has driven substantial progress, it proves insufficient in adaptive and multi-turn settings where forecasting requires informative feature extraction, reasoning-driven inference, iterative refinement, and continual adaptation over time. In this paper, we argue for agentic time series forecasting (ATSF), which reframes forecasting as an agentic process composed of perception, planning, action, reflection, and memory. Rather than focusing solely on predictive models, ATSF emphasizes organizing forecasting as an agentic workflow that can interact with...

---

## 183. Grounding Generated Videos in Feasible Plans via World Models

**原标题**: Grounding Generated Videos in Feasible Plans via World Models

**作者**: Christos Ziakas, Amir Bar, Alessandra Russo
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2602.01960v2

**中文摘要**:
> arXiv:2602.01960v2 Announce Type: replace 
摘要: Large-scale 视频 生成式 models have shown emerging capabilities as 零样本 视觉 planners, yet 视频-generated plans often violate temporal consistency and physical constraints, leading to failures when mapped to executable actions. To address this, we propose Grounding 视频 Plans with World Models (GVP-WM), a 规划 方法 that grounds 视频-generated plans into feasible 动作 sequences using a learned 动作-conditioned world 模型. At test-time, GVP-WM first generates a 视频 plan from initial and goal observations, then projects the 视频 guidance onto the manifold of dynamically feasible 隐变量 trajectories via 视频-guided 隐变量 collocation. In particular, we formulate grounding as a goal-conditioned 隐变量-space 轨迹 优化 problem that jointly optimizes 隐变量 states and actions under world-模型 dyna...

**Original Abstract**:
> arXiv:2602.01960v2 Announce Type: replace 
Abstract: Large-scale video generative models have shown emerging capabilities as zero-shot visual planners, yet video-generated plans often violate temporal consistency and physical constraints, leading to failures when mapped to executable actions. To address this, we propose Grounding Video Plans with World Models (GVP-WM), a planning method that grounds video-generated plans into feasible action sequences using a learned action-conditioned world model. At test-time, GVP-WM first generates a video plan from initial and goal observations, then projects the video guidance onto the manifold of dynamically feasible latent trajectories via video-guided latent collocation. In particular, we formulate grounding as a goal-conditioned latent-space traje...

---

## 184. Expert-Data Alignment Governs 生成 Quality in Decentralized Diffusion Models

**原标题**: Expert-Data Alignment Governs Generation Quality in Decentralized Diffusion Models

**作者**: Marcos Villagra, Bidhan Roy, Raihan Seraj, Zhiying Jiang
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2602.02685v2

**中文摘要**:
> arXiv:2602.02685v2 Announce Type: replace 
摘要: Decentralized Diffusion Models (DDMs) route denoising through experts trained independently on disjoint data clusters, which can strongly disagree in their predictions. What governs the quality of generations in such systems? We present the first ever systematic investigation of this question. A priori, the expectation is that minimizing denoising 轨迹 sensitivity -- minimizing how perturbations amplify during 采样 -- should govern 生成 quality. We demonstrate this hypothesis is incorrect: a stability-quality dissociation. Full ensemble routing, which combines all expert predictions at each step, achieves the most stable 采样 dynamics and best numerical convergence while producing the worst 生成 quality (FID 47.9 vs. 22.6 for sparse Top-2 routing). Inst...

**Original Abstract**:
> arXiv:2602.02685v2 Announce Type: replace 
Abstract: Decentralized Diffusion Models (DDMs) route denoising through experts trained independently on disjoint data clusters, which can strongly disagree in their predictions. What governs the quality of generations in such systems? We present the first ever systematic investigation of this question. A priori, the expectation is that minimizing denoising trajectory sensitivity -- minimizing how perturbations amplify during sampling -- should govern generation quality. We demonstrate this hypothesis is incorrect: a stability-quality dissociation. Full ensemble routing, which combines all expert predictions at each step, achieves the most stable sampling dynamics and best numerical convergence while producing the worst generation quality (FID 47....

---

## 185. BLITZRANK: Principled 零样本 Ranking Agents with Tournament Graphs

**原标题**: BLITZRANK: Principled Zero-shot Ranking Agents with Tournament Graphs

**作者**: Sheshansh Agrawal, Thien Hang Nguyen, Douwe Kiela
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2602.05448v3

**中文摘要**:
> arXiv:2602.05448v3 Announce Type: replace 
摘要: Selecting the top $m$ from $n$ items via expensive $k$-wise comparisons is central to settings ranging from 大语言模型-based document reranking to crowdsourced 评估 and tournament design. Existing methods either rely on heuristics that fail to fully exploit the information each comparison reveals, or are inefficient when they do. We introduce a tournament graph 框架 that provides a principled foundation for $k$-wise ranking. Our key 观测 is that each $k$-item comparison reveals a complete tournament of $\binom{k}{2}$ pairwise preferences; aggregating these into a global preference graph and computing its transitive closure yields many additional orderings without further oracle calls. We formalize when an item's rank is certifiably determined and design ...

**Original Abstract**:
> arXiv:2602.05448v3 Announce Type: replace 
Abstract: Selecting the top $m$ from $n$ items via expensive $k$-wise comparisons is central to settings ranging from LLM-based document reranking to crowdsourced evaluation and tournament design. Existing methods either rely on heuristics that fail to fully exploit the information each comparison reveals, or are inefficient when they do. We introduce a tournament graph framework that provides a principled foundation for $k$-wise ranking. Our key observation is that each $k$-item comparison reveals a complete tournament of $\binom{k}{2}$ pairwise preferences; aggregating these into a global preference graph and computing its transitive closure yields many additional orderings without further oracle calls. We formalize when an item's rank is certif...

---

## 186. 隐变量 Poincar\'e Shaping for Agentic 强化 学习

**原标题**: Latent Poincar\'e Shaping for Agentic Reinforcement Learning

**作者**: Hanchen Xia, Baoyou Chen, Zelin Zang, Yutang Ge, Guojiang Zhao, Siyu Zhu
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2602.09375v3

**中文摘要**:
> arXiv:2602.09375v3 Announce Type: replace 
摘要: We propose LaPha, a 方法 for 训练 AlphaZero-like 大语言模型 agents in a Poincar\'e 隐变量 space. Under LaPha, the 搜索 process can be visualized as a tree rooted at the prompt and growing outward from the origin toward the boundary of the Poincar\'e ball, where negative curvature provides exponentially increasing capacity with radius. Using hyperbolic geodesic distance to rule-verified correctness, we define a 节点 potential and assign dense process rewards by potential differences. We further attach a lightweight 价值 head on the same shared 隐变量 space, enabling self-guided test-time scaling with almost no additional overhead. On MATH-500, LaPha improves Qwen2.5-Math-1.5B from 66.0% to 88.2%. With 价值-head-guided 搜索, LaPha-1.5B reaches 56.7% accuracy on AIME'24,...

**Original Abstract**:
> arXiv:2602.09375v3 Announce Type: replace 
Abstract: We propose LaPha, a method for training AlphaZero-like LLM agents in a Poincar\'e latent space. Under LaPha, the search process can be visualized as a tree rooted at the prompt and growing outward from the origin toward the boundary of the Poincar\'e ball, where negative curvature provides exponentially increasing capacity with radius. Using hyperbolic geodesic distance to rule-verified correctness, we define a node potential and assign dense process rewards by potential differences. We further attach a lightweight value head on the same shared latent space, enabling self-guided test-time scaling with almost no additional overhead. On MATH-500, LaPha improves Qwen2.5-Math-1.5B from 66.0% to 88.2%. With value-head-guided search, LaPha-1.5...

---

## 187. Long Chain-of-Thought Compression via Fine-Grained Group 策略 优化

**原标题**: Long Chain-of-Thought Compression via Fine-Grained Group Policy Optimization

**作者**: Xinchen Han, Hossam Afifi, Michel Marot, Xilu Wang, Lu Yin
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2602.10048v2

**中文摘要**:
> arXiv:2602.10048v2 Announce Type: replace 
摘要: Large Language Models (LLMs) often generate unnecessarily verbose Chain-of-Thought (CoT) 推理 that increases computational costs and 延迟 without proportional 性能 gains. In this 论文, we propose Fine-grained Group 策略 优化 (FGO), a 强化 学习 (RL) 算法 that refines group responses by subdividing them and assigning appropriate weights based on length and 熵, thereby enabling effective CoT compression. Meanwhile, as an enhanced variant of Group Relative 策略 优化 (GRPO), FGO successfully addresses two major limitations of the GRPO: inefficient data utilization and 熵 collapse. We evaluate FGO on multiple 推理 LLMs and benchmarks, including MATH500, AIME24, AMC23, and Minerva. Experimental results show that FGO achieves 高效 CoT compression without degrading 性能, and simult...

**Original Abstract**:
> arXiv:2602.10048v2 Announce Type: replace 
Abstract: Large Language Models (LLMs) often generate unnecessarily verbose Chain-of-Thought (CoT) reasoning that increases computational costs and latency without proportional performance gains. In this paper, we propose Fine-grained Group policy Optimization (FGO), a Reinforcement Learning (RL) algorithm that refines group responses by subdividing them and assigning appropriate weights based on length and entropy, thereby enabling effective CoT compression. Meanwhile, as an enhanced variant of Group Relative Policy Optimization (GRPO), FGO successfully addresses two major limitations of the GRPO: inefficient data utilization and entropy collapse. We evaluate FGO on multiple reasoning LLMs and benchmarks, including MATH500, AIME24, AMC23, and Min...

---

## 188. LexiSafe: 离线 Safe 强化 学习 with Lexicographic Safety-奖励 Hierarchy

**原标题**: LexiSafe: Offline Safe Reinforcement Learning with Lexicographic Safety-Reward Hierarchy

**作者**: Hsin-Jung Yang, Zhanhong Jiang, Prajwal Koirala, Qisai Liu, Cody Fleming, Soumik Sarkar
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2602.17312v2

**中文摘要**:
> arXiv:2602.17312v2 Announce Type: replace 
摘要: 离线 safe 强化 学习 (RL) is increasingly important for cyber-physical systems (CPS), where safety violations during 训练 are unacceptable and only pre-collected data are available. Existing 离线 safe RL methods typically 平衡 奖励-safety tradeoffs through constraint relaxation or joint 优化, but they often lack structural mechanisms to prevent safety drift. We propose LexiSafe, a lexicographic 离线 RL 框架 designed to preserve safety-aligned behavior. We first develop LexiSafe-SC, a single-cost formulation for standard 离线 safe RL, and derive safety-violation and 性能-suboptimality bounds that together yield sample-complexity guarantees. We then extend the 框架 to hierarchical safety requirements with LexiSafe-MC, which supports multiple safety costs and admits its ow...

**Original Abstract**:
> arXiv:2602.17312v2 Announce Type: replace 
Abstract: Offline safe reinforcement learning (RL) is increasingly important for cyber-physical systems (CPS), where safety violations during training are unacceptable and only pre-collected data are available. Existing offline safe RL methods typically balance reward-safety tradeoffs through constraint relaxation or joint optimization, but they often lack structural mechanisms to prevent safety drift. We propose LexiSafe, a lexicographic offline RL framework designed to preserve safety-aligned behavior. We first develop LexiSafe-SC, a single-cost formulation for standard offline safe RL, and derive safety-violation and performance-suboptimality bounds that together yield sample-complexity guarantees. We then extend the framework to hierarchical s...

---

## 189. Active 价值 Querying to Minimize Additive Error in Subadditive Set Function 学习

**原标题**: Active Value Querying to Minimize Additive Error in Subadditive Set Function Learning

**作者**: Martin \v{C}ern\'y, David Sychrovsk\'y, Filip \'Uradn\'ik, Jakub \v{C}ern\'y
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2602.23529v2

**中文摘要**:
> arXiv:2602.23529v2 Announce Type: replace 
摘要: Subadditive set functions play a pivotal 角色 in computational economics (especially in combinatorial auctions), combinatorial 优化 or artificial intelligence applications such as 可解释 machine 学习. However, specifying a set function requires assigning values to an exponentially large number of subsets in general, a task that is often resource-intensive in practice, particularly when the values derive from external sources such as retraining of machine 学习 models. A~simple omission of certain values introduces ambiguity that becomes even more significant when the incomplete set function has to be further optimized over. Motivated by the well-known 结果 about inapproximability of subadditive functions using deterministic 价值 queries with respect to a mult...

**Original Abstract**:
> arXiv:2602.23529v2 Announce Type: replace 
Abstract: Subadditive set functions play a pivotal role in computational economics (especially in combinatorial auctions), combinatorial optimization or artificial intelligence applications such as interpretable machine learning. However, specifying a set function requires assigning values to an exponentially large number of subsets in general, a task that is often resource-intensive in practice, particularly when the values derive from external sources such as retraining of machine learning models. A~simple omission of certain values introduces ambiguity that becomes even more significant when the incomplete set function has to be further optimized over. Motivated by the well-known result about inapproximability of subadditive functions using det...

---

## 190. Solving 对抗 examples requires solving exponential misalignment

**原标题**: Solving adversarial examples requires solving exponential misalignment

**作者**: Alessandro Salvatore, Stanislav Fort, Surya Ganguli
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.03507v2

**中文摘要**:
> arXiv:2603.03507v2 Announce Type: replace 
摘要: 对抗 attacks - input perturbations imperceptible to humans that fool 神经 networks - remain both a persistent failure mode in machine 学习, and a phenomenon with mysterious origins. To shed light, we define and analyze a 网络's perceptual manifold (PM) for a class concept as the space of all inputs confidently assigned to that class by the 网络. We find, strikingly, that the dimensionalities of 神经 网络 PMs are orders of magnitude higher than those of natural human concepts. Since volume typically grows exponentially with dimension, this suggests exponential misalignment between machines and humans, with exponentially many inputs confidently assigned to concepts by machines but not humans. Furthermore, this provides a natural geometric hypothesis for the o...

**Original Abstract**:
> arXiv:2603.03507v2 Announce Type: replace 
Abstract: Adversarial attacks - input perturbations imperceptible to humans that fool neural networks - remain both a persistent failure mode in machine learning, and a phenomenon with mysterious origins. To shed light, we define and analyze a network's perceptual manifold (PM) for a class concept as the space of all inputs confidently assigned to that class by the network. We find, strikingly, that the dimensionalities of neural network PMs are orders of magnitude higher than those of natural human concepts. Since volume typically grows exponentially with dimension, this suggests exponential misalignment between machines and humans, with exponentially many inputs confidently assigned to concepts by machines but not humans. Furthermore, this provi...

---

## 191. Stochastic 注意力 via Langevin Dynamics on the Modern Hopfield Energy

**原标题**: Stochastic Attention via Langevin Dynamics on the Modern Hopfield Energy

**作者**: Abdulrahman Alswaidan, Jeffrey D. Varner
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.06875v2

**中文摘要**:
> arXiv:2603.06875v2 Announce Type: replace 
摘要: 注意力 heads retrieve: given a query, they 回报 a softmax-weighted average of stored values. We show that this computation is one step of 梯度 descent on a classical energy function, and that Langevin 采样 from the corresponding distribution yields stochastic 注意力: a 训练-free sampler controlled by a single temperature. Lowering the temperature gives exact 检索; raising it gives open-ended 生成. Because the energy 梯度 equals the 注意力 map, no score 网络, 训练 loop, or learned 模型 is required. We derive a closed-form 熵 inflection condition that identifies the 检索-to-生成 转移 temperature for any 内存 geometry, with a scaling law $\beta^*\!\sim\!\sqrt{d}$ for random patterns. We validate on five domains (64 to 4,096 dimensions). On MNIST digit images, stochastic 注意力 is $2.6{\...

**Original Abstract**:
> arXiv:2603.06875v2 Announce Type: replace 
Abstract: Attention heads retrieve: given a query, they return a softmax-weighted average of stored values. We show that this computation is one step of gradient descent on a classical energy function, and that Langevin sampling from the corresponding distribution yields stochastic attention: a training-free sampler controlled by a single temperature. Lowering the temperature gives exact retrieval; raising it gives open-ended generation. Because the energy gradient equals the attention map, no score network, training loop, or learned model is required. We derive a closed-form entropy inflection condition that identifies the retrieval-to-generation transition temperature for any memory geometry, with a scaling law $\beta^*\!\sim\!\sqrt{d}$ for rand...

---

## 192. Equitable 多任务 学习 for AI-RANs

**原标题**: Equitable Multi-Task Learning for AI-RANs

**作者**: Panayiotis Raptis, Fatih Aslan, George Iosifidis
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.08717v2

**中文摘要**:
> arXiv:2603.08717v2 Announce Type: replace 
摘要: AI-enabled Radio Access Networks (AI-RANs) are expected to serve heterogeneous users with time-varying 学习 tasks over shared edge resources. Ensuring equitable 推理 性能 across these users requires adaptive and fair 学习 mechanisms. This 论文 introduces an 在线-within-在线 fair 多任务 学习 (OWO-FMTL) 框架 that ensures long-term equity across users. The 方法 combines two 学习 loops: an outer loop updating the shared 模型 across rounds and an inner loop rebalancing user priorities within each round with a lightweight primal-dual update. Equity is quantified via generalized alpha-公平性, allowing a trade-off between efficiency and 公平性. The 框架 guarantees diminishing 性能 disparity over time and operates with low computational overhead suitable for edge 部署. Experiments on convex...

**Original Abstract**:
> arXiv:2603.08717v2 Announce Type: replace 
Abstract: AI-enabled Radio Access Networks (AI-RANs) are expected to serve heterogeneous users with time-varying learning tasks over shared edge resources. Ensuring equitable inference performance across these users requires adaptive and fair learning mechanisms. This paper introduces an online-within-online fair multi-task learning (OWO-FMTL) framework that ensures long-term equity across users. The method combines two learning loops: an outer loop updating the shared model across rounds and an inner loop rebalancing user priorities within each round with a lightweight primal-dual update. Equity is quantified via generalized alpha-fairness, allowing a trade-off between efficiency and fairness. The framework guarantees diminishing performance disp...

---

## 193. A New Modeling to 特征 选择 Based on the Fuzzy Rough Set Theory in Normal and Optimistic States on Hybrid Information Systems

**原标题**: A New Modeling to Feature Selection Based on the Fuzzy Rough Set Theory in Normal and Optimistic States on Hybrid Information Systems

**作者**: Mohammad Hossein Safarpour, Seyed Majid Alavi, Mohammad Izadikhah, Hossein Dibachi
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.08900v2

**中文摘要**:
> arXiv:2603.08900v2 Announce Type: replace 
摘要: Considering the high volume, wide variety, and rapid speed of data 生成, investigating 特征 选择 methods for big data presents various applications and advantages. By removing irrelevant and redundant features, 特征 选择 reduces data dimensions, thereby facilitating optimal 决策-making within 决策 systems. One of the key tools for 特征 选择 in hybrid information systems is fuzzy rough set theory. However, this theory faces two significant challenges: First, obtaining fuzzy equivalence relations through intersection operations in high-dimensional spaces can be both time-consuming and 内存-intensive. Additionally, this 方法 may produce noisy data, complicating the 特征 选择 process. The purpose and innovation of this 论文 are to address these issues. We proposed a new 特征 选...

**Original Abstract**:
> arXiv:2603.08900v2 Announce Type: replace 
Abstract: Considering the high volume, wide variety, and rapid speed of data generation, investigating feature selection methods for big data presents various applications and advantages. By removing irrelevant and redundant features, feature selection reduces data dimensions, thereby facilitating optimal decision-making within decision systems. One of the key tools for feature selection in hybrid information systems is fuzzy rough set theory. However, this theory faces two significant challenges: First, obtaining fuzzy equivalence relations through intersection operations in high-dimensional spaces can be both time-consuming and memory-intensive. Additionally, this method may produce noisy data, complicating the feature selection process. The pur...

---

## 194. 代理-Guided Measurement Calibration

**原标题**: Proxy-Guided Measurement Calibration

**作者**: Saketh Vishnubhatla, Shu Wan, Andre Harrison, Adrienne Raglin, Huan Liu
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.09288v2

**中文摘要**:
> arXiv:2603.09288v2 Announce Type: replace 
摘要: Aggregate outcome variables collected through surveys and administrative records are often subject to systematic measurement error. For instance, in disaster 损失 databases, county-level losses reported may differ from the true damages due to variations in on-the-ground data collection capacity, reporting practices, and event characteristics. Such miscalibration complicates downstream analysis and 决策-making. We study the problem of outcome miscalibration and propose a 框架 guided by 代理 variables for estimating and correcting the systematic errors. We 模型 the data-generating process using a 因果 graph that separates 隐变量 content variables driving the true outcome from the 隐变量 偏见 variables that induce systematic errors. The key insight is that 代理 variab...

**Original Abstract**:
> arXiv:2603.09288v2 Announce Type: replace 
Abstract: Aggregate outcome variables collected through surveys and administrative records are often subject to systematic measurement error. For instance, in disaster loss databases, county-level losses reported may differ from the true damages due to variations in on-the-ground data collection capacity, reporting practices, and event characteristics. Such miscalibration complicates downstream analysis and decision-making. We study the problem of outcome miscalibration and propose a framework guided by proxy variables for estimating and correcting the systematic errors. We model the data-generating process using a causal graph that separates latent content variables driving the true outcome from the latent bias variables that induce systematic er...

---

## 195. SPAARS: Safer RL 策略 Alignment through 摘要 探索 and Refined 利用 of 动作 Space

**原标题**: SPAARS: Safer RL Policy Alignment through Abstract Exploration and Refined Exploitation of Action Space

**作者**: Swaminathan S K, Aritra Hazra
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.09378v2

**中文摘要**:
> arXiv:2603.09378v2 Announce Type: replace 
摘要: 离线-to-在线 强化 学习 (RL) offers a promising paradigm for 机器人 by pre-训练 policies on safe, 离线 demonstrations and fine-tuning them via 在线 interaction. However, a fundamental challenge remains: how to safely explore 在线 without deviating from the behavioral support of the 离线 data? While recent methods leverage conditional variational autoencoders (CVAEs) to bound 探索 within a 隐变量 space, they inherently suffer from an 利用 gap -- a 性能 ceiling imposed by the decoder's reconstruction 损失. We introduce SPAARS, a curriculum 学习 框架 that initially constrains 探索 to the low-dimensional 隐变量 manifold for sample-高效, safe behavioral improvement, then seamlessly transfers 控制 to the raw 动作 space, bypassing the decoder bottleneck. SPAARS has two instantiations: the CVAE-bas...

**Original Abstract**:
> arXiv:2603.09378v2 Announce Type: replace 
Abstract: Offline-to-online reinforcement learning (RL) offers a promising paradigm for robotics by pre-training policies on safe, offline demonstrations and fine-tuning them via online interaction. However, a fundamental challenge remains: how to safely explore online without deviating from the behavioral support of the offline data? While recent methods leverage conditional variational autoencoders (CVAEs) to bound exploration within a latent space, they inherently suffer from an exploitation gap -- a performance ceiling imposed by the decoder's reconstruction loss. We introduce SPAARS, a curriculum learning framework that initially constrains exploration to the low-dimensional latent manifold for sample-efficient, safe behavioral improvement, t...

---

## 196. Reconstructing Movement from Sparse Samples: Enhanced Spatio-Temporal Matching Strategies for Low-Frequency Data

**原标题**: Reconstructing Movement from Sparse Samples: Enhanced Spatio-Temporal Matching Strategies for Low-Frequency Data

**作者**: Ali Yousefian, Arianna Burzacchi, Simone Vantini
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.09412v2

**中文摘要**:
> arXiv:2603.09412v2 Announce Type: replace 
摘要: This 论文 explores potential improvements to the Spatial-Temporal Matching 算法 for aligning the GPS trajectories to road networks. While this 算法 is effective, it presents some limitations in computational efficiency and the accuracy of the results, especially in dense environments with relatively high 采样 intervals. To address this, the 论文 proposes four modifications to the original 算法: a 动态 缓冲区, an adaptive 观测 probability, a redesigned temporal scoring function, and a behavioral analysis to account for the historical mobility patterns. The enhancements are assessed using real-world data from the urban area of Milan, and through newly defined 评估 metrics to be applied in the absence of ground truth. The results of the 实验 show significant improvemen...

**Original Abstract**:
> arXiv:2603.09412v2 Announce Type: replace 
Abstract: This paper explores potential improvements to the Spatial-Temporal Matching algorithm for aligning the GPS trajectories to road networks. While this algorithm is effective, it presents some limitations in computational efficiency and the accuracy of the results, especially in dense environments with relatively high sampling intervals. To address this, the paper proposes four modifications to the original algorithm: a dynamic buffer, an adaptive observation probability, a redesigned temporal scoring function, and a behavioral analysis to account for the historical mobility patterns. The enhancements are assessed using real-world data from the urban area of Milan, and through newly defined evaluation metrics to be applied in the absence of...

---

## 197. Mindstorms in Natural Language-Based Societies of Mind

**原标题**: Mindstorms in Natural Language-Based Societies of Mind

**作者**: Mingchen Zhuge, Haozhe Liu, Francesco Faccio, Dylan R. Ashley, R\'obert Csord\'as, Anand Gopalakrishnan, Abdullah Hamdi, Hasan Abed Al Kader Hammoud, Vincent Herrmann, Kazuki Irie, Louis Kirsch, Bing Li, Guohao Li, Shuming Liu, Jinjie Mai, Piotr Pi\k{e}kos, Aditya Ramesh, Imanol Schlag, Weimin Shi, Aleksandar Stani\'c, Wenyi Wang, Yuhui Wang, Mengmeng Xu, Deng-Ping Fan, Bernard Ghanem, J\"urgen Schmidhuber
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2305.17066v2

**中文摘要**:
> arXiv:2305.17066v2 Announce Type: replace-cross 
摘要: Both Minsky's "society of mind" and Schmidhuber's "学习 to think" inspire diverse societies of large multimodal 神经 networks (NNs) that solve problems by interviewing each other in a "mindstorm." Recent implementations of NN-based societies of minds consist of large language models (LLMs) and other NN-based experts communicating through a natural language interface. In doing so, they overcome the limitations of single LLMs, improving multimodal 零样本 推理. In these natural language-based societies of mind (NLSOMs), new agents -- all communicating through the same universal symbolic language -- are easily added in a modular fashion. To demonstrate the power of NLSOMs, we assemble and 实验 with several of them (having up to 129 members), leveraging...

**Original Abstract**:
> arXiv:2305.17066v2 Announce Type: replace-cross 
Abstract: Both Minsky's "society of mind" and Schmidhuber's "learning to think" inspire diverse societies of large multimodal neural networks (NNs) that solve problems by interviewing each other in a "mindstorm." Recent implementations of NN-based societies of minds consist of large language models (LLMs) and other NN-based experts communicating through a natural language interface. In doing so, they overcome the limitations of single LLMs, improving multimodal zero-shot reasoning. In these natural language-based societies of mind (NLSOMs), new agents -- all communicating through the same universal symbolic language -- are easily added in a modular fashion. To demonstrate the power of NLSOMs, we assemble and experiment with several of them (...

---

## 198. Exploratory Optimal Stopping: A Singular 控制 Formulation

**原标题**: Exploratory Optimal Stopping: A Singular Control Formulation

**作者**: Jodi Dianetti, Giorgio Ferrari, Renyuan Xu
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2408.09335v3

**中文摘要**:
> arXiv:2408.09335v3 Announce Type: replace-cross 
摘要: This 论文 explores continuous-time and 状态-space optimal stopping problems from a 强化 学习 perspective. We begin by formulating the stopping problem using randomized stopping times, where the 决策 maker's 控制 is represented by the probability of stopping within a given time-specifically, a bounded, non-decreasing, c\`adl\`ag 控制 process. To encourage 探索 and facilitate 学习, we introduce a regularized version of the problem by penalizing the 性能 criterion with the cumulative residual 熵 of the randomized stopping time. The regularized problem takes the form of an (n+1)-dimensional degenerate singular stochastic 控制 with finite-fuel, where the regularized free boundary becomes the graph of a function mapping the 状态 variable of the original stopping probl...

**Original Abstract**:
> arXiv:2408.09335v3 Announce Type: replace-cross 
Abstract: This paper explores continuous-time and state-space optimal stopping problems from a reinforcement learning perspective. We begin by formulating the stopping problem using randomized stopping times, where the decision maker's control is represented by the probability of stopping within a given time-specifically, a bounded, non-decreasing, c\`adl\`ag control process. To encourage exploration and facilitate learning, we introduce a regularized version of the problem by penalizing the performance criterion with the cumulative residual entropy of the randomized stopping time. The regularized problem takes the form of an (n+1)-dimensional degenerate singular stochastic control with finite-fuel, where the regularized free boundary become...

---

## 199. EarthquakeNPP: A 基准 for Earthquake Forecasting with 神经 Point Processes

**原标题**: EarthquakeNPP: A Benchmark for Earthquake Forecasting with Neural Point Processes

**作者**: Samuel Stockman, Daniel Lawson, Maximilian Werner
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2410.08226v3

**中文摘要**:
> arXiv:2410.08226v3 Announce Type: replace-cross 
摘要: For decades, classical point process models, such as the epidemic-type aftershock sequence (ETAS) 模型, have been widely used for forecasting the event times and locations of earthquakes. Recent advances have led to 神经 Point Processes (NPPs), which promise greater flexibility and improvements over such classical models. However, the currently-used 基准 for NPPs does not represent an up-to-date challenge in the seismological community, since it contains data leakage and omits the largest earthquake sequence from the region. Additionally, initial earthquake forecasting benchmarks fail to compare NPPs with 状态-of-the-art forecasting models commonly used in seismology. To address these gaps, we introduce EarthquakeNPP: a benchmarking platform tha...

**Original Abstract**:
> arXiv:2410.08226v3 Announce Type: replace-cross 
Abstract: For decades, classical point process models, such as the epidemic-type aftershock sequence (ETAS) model, have been widely used for forecasting the event times and locations of earthquakes. Recent advances have led to Neural Point Processes (NPPs), which promise greater flexibility and improvements over such classical models. However, the currently-used benchmark for NPPs does not represent an up-to-date challenge in the seismological community, since it contains data leakage and omits the largest earthquake sequence from the region. Additionally, initial earthquake forecasting benchmarks fail to compare NPPs with state-of-the-art forecasting models commonly used in seismology. To address these gaps, we introduce EarthquakeNPP: a be...

---

## 200. Losing dimensions: Geometric memorization in 生成式 diffusion

**原标题**: Losing dimensions: Geometric memorization in generative diffusion

**作者**: Beatrice Achilli, Enrico Ventura, Gianluigi Silvestri, Bao Pham, Gabriel Raya, Dmitry Krotov, Carlo Lucibello, Luca Ambrogioni
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2410.08727v2

**中文摘要**:
> arXiv:2410.08727v2 Announce Type: replace-cross 
摘要: Diffusion models power leading 生成式 AI, but when and how they memorize 训练 data, especially on low-dimensional manifolds, remains unclear. We find memorization emerges gradually, not abruptly: as data become scarce, diffusion models experience a smooth collapse where their capacity to vary across independent directions diminishes. Measuring 隐变量 dimensionality via the learned score field, we reveal how 生成式 behavior increasingly centers on a few examples while other variations "freeze out". We propose a geometric memorization theory, showing that salient features collapse first, then finer details, leading to near point-wise replication. This mirrors physical systems condensing into a few low-energy configurations. Our theoretical prediction...

**Original Abstract**:
> arXiv:2410.08727v2 Announce Type: replace-cross 
Abstract: Diffusion models power leading generative AI, but when and how they memorize training data, especially on low-dimensional manifolds, remains unclear. We find memorization emerges gradually, not abruptly: as data become scarce, diffusion models experience a smooth collapse where their capacity to vary across independent directions diminishes. Measuring latent dimensionality via the learned score field, we reveal how generative behavior increasingly centers on a few examples while other variations "freeze out". We propose a geometric memorization theory, showing that salient features collapse first, then finer details, leading to near point-wise replication. This mirrors physical systems condensing into a few low-energy configuration...

---

## 201. Enhancing Brain Source Reconstruction by Initializing 3D 神经 Networks with Physical Inverse Solutions

**原标题**: Enhancing Brain Source Reconstruction by Initializing 3D Neural Networks with Physical Inverse Solutions

**作者**: Marco Morik, Ali Hashemi, Klaus-Robert M\"uller, Stefan Haufe, Shinichi Nakajima
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2411.00143v2

**中文摘要**:
> arXiv:2411.00143v2 Announce Type: replace-cross 
摘要: Reconstructing brain sources is a fundamental challenge in neuroscience, crucial for understanding brain function and dysfunction. Electroencephalography (EEG) signals have a high temporal resolution. However, identifying the correct spatial location of brain sources from these signals remains difficult due to the ill-posed structure of the problem. Traditional methods predominantly rely on manually crafted priors, missing the flexibility of data-driven 学习, while recent 深度 学习 approaches focus on end-to-end 学习, typically using the physical information of the 前向 模型 only for generating 训练 data. We propose the novel hybrid 方法 3D-PIUNet for EEG source localization that effectively integrates the strengths of traditional and 深度 学习 techniques. ...

**Original Abstract**:
> arXiv:2411.00143v2 Announce Type: replace-cross 
Abstract: Reconstructing brain sources is a fundamental challenge in neuroscience, crucial for understanding brain function and dysfunction. Electroencephalography (EEG) signals have a high temporal resolution. However, identifying the correct spatial location of brain sources from these signals remains difficult due to the ill-posed structure of the problem. Traditional methods predominantly rely on manually crafted priors, missing the flexibility of data-driven learning, while recent deep learning approaches focus on end-to-end learning, typically using the physical information of the forward model only for generating training data. We propose the novel hybrid method 3D-PIUNet for EEG source localization that effectively integrates the str...

---

## 202. Conditional Local Importance by Quantile Expectations

**原标题**: Conditional Local Importance by Quantile Expectations

**作者**: Kelvyn K. Bladen, Adele Cutler, D. Richard Cutler, Kevin R. Moon
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2411.08821v3

**中文摘要**:
> arXiv:2411.08821v3 Announce Type: replace-cross 
摘要: Global variable importance measures are commonly used to interpret the results of machine 学习 models. Local variable importance techniques assess how variables contribute to individual observations. Current, popular methods, including LIME and SHAP, typically fail to accurately reflect locally dependent relationships between variables and instead focus on marginal importance values. Additionally, they are not natively adapted for multi-class 分类 problems. We propose a new 模型-agnostic 方法 for calculating local variable importance, CLIQUE, that captures locally dependent relationships, provides improvements over permutation-based methods, and can be directly applied to multi-class 分类 problems. Simulated and real-world examples show that CLIQU...

**Original Abstract**:
> arXiv:2411.08821v3 Announce Type: replace-cross 
Abstract: Global variable importance measures are commonly used to interpret the results of machine learning models. Local variable importance techniques assess how variables contribute to individual observations. Current, popular methods, including LIME and SHAP, typically fail to accurately reflect locally dependent relationships between variables and instead focus on marginal importance values. Additionally, they are not natively adapted for multi-class classification problems. We propose a new model-agnostic method for calculating local variable importance, CLIQUE, that captures locally dependent relationships, provides improvements over permutation-based methods, and can be directly applied to multi-class classification problems. Simula...

---

## 203. A Novel Single-Layer Quantum 神经 网络 for Approximate SRBB-Based Unitary 合成

**原标题**: A Novel Single-Layer Quantum Neural Network for Approximate SRBB-Based Unitary Synthesis

**作者**: Giacomo Belli, Marco Mordacci, Michele Amoretti
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2412.03083v3

**中文摘要**:
> arXiv:2412.03083v3 Announce Type: replace-cross 
摘要: In this work, a novel quantum 神经 网络 is introduced as a means to approximate any unitary 进化 through the Standard Recursive Block Basis (SRBB) and is subsequently redesigned with the number of CNOTs asymptotically reduced by an exponential contribution. This algebraic 方案 to the problem of unitary 合成 exploits Lie algebras and their topological features to obtain 可扩展 parameterizations of unitary operators. First, the original SRBB-based scalability scheme, already known in the literature only from a theoretical point of view, is reformulated for 高效 算法 实现 and complexity management. Remarkably, 2-qubit operators emerge as a special case of the original scaling scheme. Furthermore, an 算法 is proposed to reduce the number of CNOT gates in the 可扩展...

**Original Abstract**:
> arXiv:2412.03083v3 Announce Type: replace-cross 
Abstract: In this work, a novel quantum neural network is introduced as a means to approximate any unitary evolution through the Standard Recursive Block Basis (SRBB) and is subsequently redesigned with the number of CNOTs asymptotically reduced by an exponential contribution. This algebraic approach to the problem of unitary synthesis exploits Lie algebras and their topological features to obtain scalable parameterizations of unitary operators. First, the original SRBB-based scalability scheme, already known in the literature only from a theoretical point of view, is reformulated for efficient algorithm implementation and complexity management. Remarkably, 2-qubit operators emerge as a special case of the original scaling scheme. Furthermor...

---

## 204. Pairwise Comparisons without Stochastic Transitivity: 模型, Theory and Applications

**原标题**: Pairwise Comparisons without Stochastic Transitivity: Model, Theory and Applications

**作者**: Sze Ming Lee, Yunxiao Chen
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2501.07437v2

**中文摘要**:
> arXiv:2501.07437v2 Announce Type: replace-cross 
摘要: Most statistical models for pairwise comparisons, including the Bradley-Terry (BT) and Thurstone models and many extensions, make a relatively strong assumption of stochastic transitivity. This assumption imposes the existence of an unobserved global ranking among all the players/teams/items and monotone constraints on the comparison probabilities implied by the global ranking. However, the stochastic transitivity assumption does not hold in many real-world scenarios of pairwise comparisons, especially games involving multiple skills or strategies. As a 结果, models relying on this assumption can have suboptimal predictive 性能. In this 论文, we propose a general family of statistical models for pairwise comparison data without a stochastic tr...

**Original Abstract**:
> arXiv:2501.07437v2 Announce Type: replace-cross 
Abstract: Most statistical models for pairwise comparisons, including the Bradley-Terry (BT) and Thurstone models and many extensions, make a relatively strong assumption of stochastic transitivity. This assumption imposes the existence of an unobserved global ranking among all the players/teams/items and monotone constraints on the comparison probabilities implied by the global ranking. However, the stochastic transitivity assumption does not hold in many real-world scenarios of pairwise comparisons, especially games involving multiple skills or strategies. As a result, models relying on this assumption can have suboptimal predictive performance. In this paper, we propose a general family of statistical models for pairwise comparison data w...

---

## 205. Rethinking 少样本 图像 Fusion: Granular Ball Priors Enable General-Purpose 深度 Fusion

**原标题**: Rethinking Few-Shot Image Fusion: Granular Ball Priors Enable General-Purpose Deep Fusion

**作者**: Minjie Deng, Yan Wei, An Wu, Yuncan Ouyang, Hao Zhai, Qianyao Peng
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2504.08937v5

**中文摘要**:
> arXiv:2504.08937v5 Announce Type: replace-cross 
摘要: In 图像 fusion tasks, the absence of real fused images as supervision signals poses significant challenges for 有监督 学习. Existing 深度 学习 methods typically address this issue either by designing handcrafted priors or by relying on large-scale datasets to learn 模型 parameters. Different from previous approaches, this 论文 introduces the concept of incomplete priors, which formally describe handcrafted priors at the algorithmic level and estimate their confidence. Based on this idea, we couple incomplete priors with the 神经 网络 through a sample-level adaptive 损失 function, enabling the 网络 to learn and re-infer fusion rules under conditions that approximate the real fusion process.To generate incomplete priors, we propose a Granular Ball Pixel Computat...

**Original Abstract**:
> arXiv:2504.08937v5 Announce Type: replace-cross 
Abstract: In image fusion tasks, the absence of real fused images as supervision signals poses significant challenges for supervised learning. Existing deep learning methods typically address this issue either by designing handcrafted priors or by relying on large-scale datasets to learn model parameters. Different from previous approaches, this paper introduces the concept of incomplete priors, which formally describe handcrafted priors at the algorithmic level and estimate their confidence. Based on this idea, we couple incomplete priors with the neural network through a sample-level adaptive loss function, enabling the network to learn and re-infer fusion rules under conditions that approximate the real fusion process.To generate incomple...

---

## 206. 离线 动态 Inventory and Pricing Strategy: Addressing Censored and Dependent Demand

**原标题**: Offline Dynamic Inventory and Pricing Strategy: Addressing Censored and Dependent Demand

**作者**: Korel Gundem, Zhengling Qi
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2504.09831v2

**中文摘要**:
> arXiv:2504.09831v2 Announce Type: replace-cross 
摘要: In this 论文, we study the 离线 sequential 特征-based pricing and inventory 控制 problem where the current demand depends on the past demand levels and any demand exceeding the available inventory is lost. Our goal is to leverage the 离线 数据集, consisting of past prices, ordering quantities, inventory levels, covariates, and censored sales levels, to estimate the optimal pricing and inventory 控制 策略 that maximizes long-term profit. While the underlying 动态 without censoring can be modeled by Markov 决策 process (MDP), the primary obstacle arises from the observed process where demand censoring is present, resulting in missing profit information, the failure of the Markov property, and a non-stationary optimal 策略. To overcome these challenges, we first ...

**Original Abstract**:
> arXiv:2504.09831v2 Announce Type: replace-cross 
Abstract: In this paper, we study the offline sequential feature-based pricing and inventory control problem where the current demand depends on the past demand levels and any demand exceeding the available inventory is lost. Our goal is to leverage the offline dataset, consisting of past prices, ordering quantities, inventory levels, covariates, and censored sales levels, to estimate the optimal pricing and inventory control policy that maximizes long-term profit. While the underlying dynamic without censoring can be modeled by Markov decision process (MDP), the primary obstacle arises from the observed process where demand censoring is present, resulting in missing profit information, the failure of the Markov property, and a non-stationar...

---

## 207. Score Matching Diffusion Based Feedback 控制 and 规划 of Nonlinear Systems

**原标题**: Score Matching Diffusion Based Feedback Control and Planning of Nonlinear Systems

**作者**: Karthik Elamvazhuthi, Darshan Gadginmath, Fabio Pasqualetti
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2504.09836v2

**中文摘要**:
> arXiv:2504.09836v2 Announce Type: replace-cross 
摘要: In this 论文, we propose a deterministic diffusion-based 框架 for controlling the probability density of nonlinear 控制-affine systems, with theoretical guarantees for drift-free and linear time-invariant (LTI) dynamics. The central idea is to first excite the 系统 with white noise so that a 前向 diffusion process explores the reachable regions of 状态 space, and then to design a deterministic feedback law that acts as a denoising mechanism driving the 系统 back toward a desired 目标 distribution supported on the 目标 set. This denoising phase provides a feedback controller that steers the 控制 系统 to the 目标 set. In this 框架, 控制 合成 reduces to constructing a deterministic reverse process that reproduces the desired 进化 of 状态 densities. We derive existence condi...

**Original Abstract**:
> arXiv:2504.09836v2 Announce Type: replace-cross 
Abstract: In this paper, we propose a deterministic diffusion-based framework for controlling the probability density of nonlinear control-affine systems, with theoretical guarantees for drift-free and linear time-invariant (LTI) dynamics. The central idea is to first excite the system with white noise so that a forward diffusion process explores the reachable regions of state space, and then to design a deterministic feedback law that acts as a denoising mechanism driving the system back toward a desired target distribution supported on the target set. This denoising phase provides a feedback controller that steers the control system to the target set. In this framework, control synthesis reduces to constructing a deterministic reverse proc...

---

## 208. 可扩展 多任务 学习 through Spiking 神经 Networks with Adaptive Task-Switching 策略 for Intelligent 自主 Agents

**原标题**: Scalable Multi-Task Learning through Spiking Neural Networks with Adaptive Task-Switching Policy for Intelligent Autonomous Agents

**作者**: Rachmad Vidya Wicaksana Putra, Avaneesh Devkota, Muhammad Shafique
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2504.13541v3

**中文摘要**:
> arXiv:2504.13541v3 Announce Type: replace-cross 
摘要: 训练 resource-constrained 自主 agents on multiple tasks simultaneously is crucial for adapting to diverse real-world environments. Recent works employ 强化 学习 (RL) 方案, but they still suffer from sub-optimal 多任务 性能 due to task interference. 状态-of-the-art works employ Spiking 神经 Networks (SNNs) to improve RL-based 多任务 学习 and enable low-power/energy operations through 网络 enhancements and spike-driven data stream processing. However, they rely on fixed task-switching intervals during its 训练, thus limiting its 性能 and scalability. To address this, we propose SwitchMT, a novel methodology that employs adaptive task-switching for effective, 可扩展, and simultaneous 多任务 学习. SwitchMT employs the following key ideas: (1) leveraging a 深度 Spiking Q-网络 with ac...

**Original Abstract**:
> arXiv:2504.13541v3 Announce Type: replace-cross 
Abstract: Training resource-constrained autonomous agents on multiple tasks simultaneously is crucial for adapting to diverse real-world environments. Recent works employ reinforcement learning (RL) approach, but they still suffer from sub-optimal multi-task performance due to task interference. State-of-the-art works employ Spiking Neural Networks (SNNs) to improve RL-based multi-task learning and enable low-power/energy operations through network enhancements and spike-driven data stream processing. However, they rely on fixed task-switching intervals during its training, thus limiting its performance and scalability. To address this, we propose SwitchMT, a novel methodology that employs adaptive task-switching for effective, scalable, and...

---

## 209. LLLMs: A Data-Driven Survey of Evolving Research on Limitations of Large Language Models

**原标题**: LLLMs: A Data-Driven Survey of Evolving Research on Limitations of Large Language Models

**作者**: Aida Kostikova, Zhipin Wang, Deidamea Bajri, Ole P\"utz, Benjamin Paa{\ss}en, Steffen Eger
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2505.19240v3

**中文摘要**:
> arXiv:2505.19240v3 Announce Type: replace-cross 
摘要: Large language 模型 (大语言模型) research has grown rapidly, along with increasing concern about their limitations. In this survey, we conduct a data-driven, semi-automated 审稿 of research on limitations of LLMs (LLLMs) from 2022 to early 2025 using a bottom-up 方案. From a 语料库 of 250,000 ACL and arXiv papers, we identify 14,648 relevant papers using keyword filtering, 大语言模型-based 分类, validated against expert labels, and topic clustering (via two approaches, HDBSCAN+BERTopic and LlooM). We find that the share of 大语言模型-related papers increases over fivefold in ACL and nearly eightfold in arXiv between 2022 and 2025. Since 2022, LLLMs research grows even faster, reaching over 30% of 大语言模型 papers by 2025. 推理 remains the most studied limitation, follo...

**Original Abstract**:
> arXiv:2505.19240v3 Announce Type: replace-cross 
Abstract: Large language model (LLM) research has grown rapidly, along with increasing concern about their limitations. In this survey, we conduct a data-driven, semi-automated review of research on limitations of LLMs (LLLMs) from 2022 to early 2025 using a bottom-up approach. From a corpus of 250,000 ACL and arXiv papers, we identify 14,648 relevant papers using keyword filtering, LLM-based classification, validated against expert labels, and topic clustering (via two approaches, HDBSCAN+BERTopic and LlooM). We find that the share of LLM-related papers increases over fivefold in ACL and nearly eightfold in arXiv between 2022 and 2025. Since 2022, LLLMs research grows even faster, reaching over 30% of LLM papers by 2025. Reasoning remains t...

---

## 210. 学习 What 强化 学习 Can't: Interleaved 在线 Fine-Tuning for Hardest Questions

**原标题**: Learning What Reinforcement Learning Can't: Interleaved Online Fine-Tuning for Hardest Questions

**作者**: Lu Ma, Hao Liang, Meiyi Qiang, Lexiang Tang, Xiaochen Ma, Zhen Hao Wong, Junbo Niu, Chengyu Shen, Runming He, Yanhao Li, Bin Cui, Wentao Zhang
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2506.07527v3

**中文摘要**:
> arXiv:2506.07527v3 Announce Type: replace-cross 
摘要: Recent advances in large language 模型 (大语言模型) 推理 have shown that sophisticated behaviors such as 规划 and self-reflection can emerge through 强化 学习 (RL). However, despite these successes, RL in its current form remains insufficient to induce capabilities that exceed the limitations of the base 模型, as it is primarily optimized based on existing knowledge of the 模型 rather than facilitating the acquisition of new information. To address this limitation, we employ 有监督 fine-tuning (SFT) to learn what RL cannot, which enables the incorporation of new knowledge and 推理 patterns by leveraging high-quality demonstration data. We analyze the 训练 dynamics of RL and SFT for 大语言模型 推理 and find that RL excels at maintaining and improving 性能 on questions with...

**Original Abstract**:
> arXiv:2506.07527v3 Announce Type: replace-cross 
Abstract: Recent advances in large language model (LLM) reasoning have shown that sophisticated behaviors such as planning and self-reflection can emerge through reinforcement learning (RL). However, despite these successes, RL in its current form remains insufficient to induce capabilities that exceed the limitations of the base model, as it is primarily optimized based on existing knowledge of the model rather than facilitating the acquisition of new information. To address this limitation, we employ supervised fine-tuning (SFT) to learn what RL cannot, which enables the incorporation of new knowledge and reasoning patterns by leveraging high-quality demonstration data. We analyze the training dynamics of RL and SFT for LLM reasoning and f...

---

## 211. Differential 隐私 in Machine 学习: A Survey from Symbolic AI to LLMs

**原标题**: Differential Privacy in Machine Learning: A Survey from Symbolic AI to LLMs

**作者**: Francisco Aguilera-Mart\'inez, Fernando Berzal
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2506.11687v2

**中文摘要**:
> arXiv:2506.11687v2 Announce Type: replace-cross 
摘要: Machine 学习 models should not reveal particular information that is not otherwise accessible. Differential 隐私 provides a formal 框架 to mitigate 隐私 risks by ensuring that the inclusion or exclusion of any single data point does not significantly alter the output of an 算法, thus limiting the exposure of private information. This survey reviews the foundational definitions of differential 隐私 and traces their 进化 through key theoretical and applied contributions. It then provides an in-depth examination of how DP has been integrated into machine 学习 models, analyzing existing proposals and methods to preserve 隐私 when 训练 ML models. Finally, it describes how DP-based ML techniques can be evaluated in practice. By offering a comprehensive overview o...

**Original Abstract**:
> arXiv:2506.11687v2 Announce Type: replace-cross 
Abstract: Machine learning models should not reveal particular information that is not otherwise accessible. Differential privacy provides a formal framework to mitigate privacy risks by ensuring that the inclusion or exclusion of any single data point does not significantly alter the output of an algorithm, thus limiting the exposure of private information. This survey reviews the foundational definitions of differential privacy and traces their evolution through key theoretical and applied contributions. It then provides an in-depth examination of how DP has been integrated into machine learning models, analyzing existing proposals and methods to preserve privacy when training ML models. Finally, it describes how DP-based ML techniques can...

---

## 212. Universal Dynamics with Globally Controlled Analog Quantum Simulators

**原标题**: Universal Dynamics with Globally Controlled Analog Quantum Simulators

**作者**: Hong-Ye Hu, Abigail McClain Gomez, Liyuan Chen, Aaron Trowbridge, Andy J. Goldschmidt, Zachary Manchester, Frederic T. Chong, Arthur Jaffe, Susanne F. Yelin
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2508.19075v5

**中文摘要**:
> arXiv:2508.19075v5 Announce Type: replace-cross 
摘要: Analog quantum simulators with global 控制 fields have emerged as powerful platforms for exploring complex quantum phenomena. Despite these advances, a fundamental theoretical question remains unresolved: to what extent can such systems realize universal quantum dynamics under global 控制? Here we establish a necessary and sufficient condition for universal quantum computation using only global pulse 控制, proving that a broad class of analog quantum simulators is, in fact, universal. We further extend this 框架 to fermionic and bosonic systems, including modern platforms such as ultracold atoms in optical superlattices. Moreover, we observe that analog simulators driven by random global pulses exhibit information scrambling comparable to random...

**Original Abstract**:
> arXiv:2508.19075v5 Announce Type: replace-cross 
Abstract: Analog quantum simulators with global control fields have emerged as powerful platforms for exploring complex quantum phenomena. Despite these advances, a fundamental theoretical question remains unresolved: to what extent can such systems realize universal quantum dynamics under global control? Here we establish a necessary and sufficient condition for universal quantum computation using only global pulse control, proving that a broad class of analog quantum simulators is, in fact, universal. We further extend this framework to fermionic and bosonic systems, including modern platforms such as ultracold atoms in optical superlattices. Moreover, we observe that analog simulators driven by random global pulses exhibit information scr...

---

## 213. Tensor Train Completion from Fiberwise Observations Along a Single Mode

**原标题**: Tensor Train Completion from Fiberwise Observations Along a Single Mode

**作者**: Shakir Showkat Sofi, Lieven De Lathauwer
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2509.18149v2

**中文摘要**:
> arXiv:2509.18149v2 Announce Type: replace-cross 
摘要: Tensor completion is an extension of matrix completion aimed at recovering a multiway data tensor by leveraging a given subset of its entries (observations) and the pattern of 观测. The low-rank assumption is key in establishing a relationship between the observed and unobserved entries of the tensor. The low-rank tensor completion problem is typically solved using numerical 优化 techniques, where the rank information is used either implicitly (in the rank minimization 方案) or explicitly (in the error minimization 方案). Current theories concerning these techniques often study 概率 recovery guarantees under conditions such as random uniform observations and incoherence requirements. However, if an 观测 pattern exhibits some low-rank structure that ...

**Original Abstract**:
> arXiv:2509.18149v2 Announce Type: replace-cross 
Abstract: Tensor completion is an extension of matrix completion aimed at recovering a multiway data tensor by leveraging a given subset of its entries (observations) and the pattern of observation. The low-rank assumption is key in establishing a relationship between the observed and unobserved entries of the tensor. The low-rank tensor completion problem is typically solved using numerical optimization techniques, where the rank information is used either implicitly (in the rank minimization approach) or explicitly (in the error minimization approach). Current theories concerning these techniques often study probabilistic recovery guarantees under conditions such as random uniform observations and incoherence requirements. However, if an o...

---

## 214. 零样本 Transferable Solution 方法 for Parametric Optimal 控制 Problems

**原标题**: Zero-Shot Transferable Solution Method for Parametric Optimal Control Problems

**作者**: Xingjian Li, Kelvin Kan, Deepanshu Verma, Krishna Kumar, Stanley Osher, J\'an Drgo\v{n}a
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2509.18404v2

**中文摘要**:
> arXiv:2509.18404v2 Announce Type: replace-cross 
摘要: This 论文 presents a transferable solution 方法 for optimal 控制 problems with varying objectives using function encoder (FE) policies. Traditional 优化-based approaches must be re-solved whenever objectives change, resulting in prohibitive computational costs for applications requiring frequent 评估 and adaptation. The proposed 方法 learns a reusable set of 神经 basis functions that spans the 控制 策略 space, enabling 高效 零样本 adaptation to new tasks through either projection from data or direct mapping from problem specifications. The key idea is an 离线-在线 decomposition: basis functions are learned once during 离线 imitation 学习, while 在线 adaptation requires only lightweight coefficient estimation. Numerical experiments across diverse dynamics, dimensions, an...

**Original Abstract**:
> arXiv:2509.18404v2 Announce Type: replace-cross 
Abstract: This paper presents a transferable solution method for optimal control problems with varying objectives using function encoder (FE) policies. Traditional optimization-based approaches must be re-solved whenever objectives change, resulting in prohibitive computational costs for applications requiring frequent evaluation and adaptation. The proposed method learns a reusable set of neural basis functions that spans the control policy space, enabling efficient zero-shot adaptation to new tasks through either projection from data or direct mapping from problem specifications. The key idea is an offline-online decomposition: basis functions are learned once during offline imitation learning, while online adaptation requires only lightwe...

---

## 215. Empirical PAC-Bayes Bounds for Markov Chains

**原标题**: Empirical PAC-Bayes Bounds for Markov Chains

**作者**: Vahe Karagulyan, Pierre Alquier
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2509.20985v3

**中文摘要**:
> arXiv:2509.20985v3 Announce Type: replace-cross 
摘要: The core of 泛化 theory was developed for independent observations. Some PAC and PAC-Bayes bounds are available for data that exhibit a temporal dependence. However, there are constants in these bounds that depend on properties of the data-generating process: mixing coefficients, mixing time, spectral gap... Such constants are unknown in practice. In this 论文, we prove a new PAC-Bayes bound for Markov chains. This bound depends on a quantity called the pseudo-spectral gap. The main novelty is that we can provide an empirical bound on the pseudo-spectral gap when the 状态 space is finite. Thus, we obtain the first fully empirical PAC-Bayes bound for Markov chains. This extends beyond the finite case, although this requires additional assumptio...

**Original Abstract**:
> arXiv:2509.20985v3 Announce Type: replace-cross 
Abstract: The core of generalization theory was developed for independent observations. Some PAC and PAC-Bayes bounds are available for data that exhibit a temporal dependence. However, there are constants in these bounds that depend on properties of the data-generating process: mixing coefficients, mixing time, spectral gap... Such constants are unknown in practice. In this paper, we prove a new PAC-Bayes bound for Markov chains. This bound depends on a quantity called the pseudo-spectral gap. The main novelty is that we can provide an empirical bound on the pseudo-spectral gap when the state space is finite. Thus, we obtain the first fully empirical PAC-Bayes bound for Markov chains. This extends beyond the finite case, although this requi...

---

## 216. 多模态 Data Spectrum: 多模态 Datasets are Multi-dimensional

**原标题**: Multi-modal Data Spectrum: Multi-modal Datasets are Multi-dimensional

**作者**: Divyam Madaan, Varshan Muhunthan, Kyunghyun Cho, Sumit Chopra
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2509.23499v2

**中文摘要**:
> arXiv:2509.23499v2 Announce Type: replace-cross 
摘要: Understanding the interplay between intra-modality dependencies (the contribution of an individual modality to a 目标 task) and inter-modality dependencies (the relationships between modalities and the 目标 task) is fundamental to advancing 多模态 学习. However, the nature of and interaction between these dependencies within current 基准 evaluations remains poorly characterized. In this work, we present a large-scale empirical study to quantify these dependencies across 23 视觉 question-answering benchmarks using 多模态 large language models (MLLMs) covering domains such as general and expert knowledge 推理, optical character 识别, and document understanding. Our findings show that the reliance on vision, question (text), and their interaction varies signif...

**Original Abstract**:
> arXiv:2509.23499v2 Announce Type: replace-cross 
Abstract: Understanding the interplay between intra-modality dependencies (the contribution of an individual modality to a target task) and inter-modality dependencies (the relationships between modalities and the target task) is fundamental to advancing multi-modal learning. However, the nature of and interaction between these dependencies within current benchmark evaluations remains poorly characterized. In this work, we present a large-scale empirical study to quantify these dependencies across 23 visual question-answering benchmarks using multi-modal large language models (MLLMs) covering domains such as general and expert knowledge reasoning, optical character recognition, and document understanding. Our findings show that the reliance ...

---

## 217. RADAR: 推理-Ability and Difficulty-Aware Routing for 推理 LLMs

**原标题**: RADAR: Reasoning-Ability and Difficulty-Aware Routing for Reasoning LLMs

**作者**: Nigel Fernandez, Branislav Kveton, Ryan A. Rossi, Andrew S. Lan, Zichao Wang
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2509.25426v3

**中文摘要**:
> arXiv:2509.25426v3 Announce Type: replace-cross 
摘要: 推理 language models have demonstrated remarkable 性能 on many challenging tasks in math, science, and coding. Choosing the right 推理 模型 for practical 部署 involves a 性能 and cost tradeoff at two key levels: 模型 size and 推理 budget, where larger models and higher 推理 budget lead to better 性能 but with increased cost and 延迟. In this work, we tackle this tradeoff from the angle of 模型 configuration routing for different queries, and present RADAR (推理-Ability and Difficulty-Aware Routing), a lightweight, 可解释, and 可扩展 routing 框架. Inspired by psychometrics, RADAR learns an item response 模型 from 模型 responses with different budgets to different queries, with 可解释 parameters including query difficulties and 模型-budget abilities. RADAR then routes queries with ...

**Original Abstract**:
> arXiv:2509.25426v3 Announce Type: replace-cross 
Abstract: Reasoning language models have demonstrated remarkable performance on many challenging tasks in math, science, and coding. Choosing the right reasoning model for practical deployment involves a performance and cost tradeoff at two key levels: model size and reasoning budget, where larger models and higher reasoning budget lead to better performance but with increased cost and latency. In this work, we tackle this tradeoff from the angle of model configuration routing for different queries, and present RADAR (Reasoning-Ability and Difficulty-Aware Routing), a lightweight, interpretable, and scalable routing framework. Inspired by psychometrics, RADAR learns an item response model from model responses with different budgets to differ...

---

## 218. KV Cache Transform Coding for Compact 存储 in 大语言模型 推理

**原标题**: KV Cache Transform Coding for Compact Storage in LLM Inference

**作者**: Konrad Staniszewski, Adrian {\L}a\'ncucki
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2511.01815v2

**中文摘要**:
> arXiv:2511.01815v2 Announce Type: replace-cross 
摘要: 服务 large language models (LLMs) at scale necessitates 高效 key-价值 (KV) cache management. KV caches can be reused across conversation turns via shared-prefix prompts that are common in iterative 代码 editing and chat. However, stale caches consume scarce GPU 内存, require offloading, or force recomputation. We present KVTC, a lightweight transform coder that compresses KV caches for compact on-GPU and off-GPU 存储. Drawing on classical media compression, KVTC combines PCA-based 特征 decorrelation, adaptive quantization, and 熵 coding. It requires only a brief initial calibration and leaves 模型 parameters unchanged. By exploiting redundancies in KV caches, KVTC achieves up to 20$\times$ compression while maintaining 推理 and long-context accuracy, and 4...

**Original Abstract**:
> arXiv:2511.01815v2 Announce Type: replace-cross 
Abstract: Serving large language models (LLMs) at scale necessitates efficient key-value (KV) cache management. KV caches can be reused across conversation turns via shared-prefix prompts that are common in iterative code editing and chat. However, stale caches consume scarce GPU memory, require offloading, or force recomputation. We present KVTC, a lightweight transform coder that compresses KV caches for compact on-GPU and off-GPU storage. Drawing on classical media compression, KVTC combines PCA-based feature decorrelation, adaptive quantization, and entropy coding. It requires only a brief initial calibration and leaves model parameters unchanged. By exploiting redundancies in KV caches, KVTC achieves up to 20$\times$ compression while m...

---

## 219. Resource Allocation in Hybrid Radio-Optical IoT Networks using GNN with 多任务 学习

**原标题**: Resource Allocation in Hybrid Radio-Optical IoT Networks using GNN with Multi-task Learning

**作者**: Aymen Hamrouni, Sofie Pollin, Hazem Sallouha
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2511.07428v2

**中文摘要**:
> arXiv:2511.07428v2 Announce Type: replace-cross 
摘要: This 论文 addresses the problem of dual-technology scheduling in hybrid Internet-of-Things (IoT) networks that integrate Optical Wireless Communication (OWC) with Radio Frequency (RF). We first present an 优化 formulation that jointly maximizes 吞吐量 and minimizes delivery-based Age of Information (AoI) between access points and IoT nodes under energy and 链接 availability constraints. However, solving such NP-hard problems at scale is computationally intractable and typically assumes full channel observability, which is impractical in real deployments. To address this challenge, we propose the Dual-Graph 嵌入 with Transformer (DGET) 框架, a 有监督 多任务 学习 架构 that combines a two-stage Graph 神经 网络 (GNN) with a Transformer encoder. The first stage employs...

**Original Abstract**:
> arXiv:2511.07428v2 Announce Type: replace-cross 
Abstract: This paper addresses the problem of dual-technology scheduling in hybrid Internet-of-Things (IoT) networks that integrate Optical Wireless Communication (OWC) with Radio Frequency (RF). We first present an optimization formulation that jointly maximizes throughput and minimizes delivery-based Age of Information (AoI) between access points and IoT nodes under energy and link availability constraints. However, solving such NP-hard problems at scale is computationally intractable and typically assumes full channel observability, which is impractical in real deployments. To address this challenge, we propose the Dual-Graph Embedding with Transformer (DGET) framework, a supervised multi-task learning architecture that combines a two-sta...

---

## 220. CostNav: A Navigation 基准 for Real-World Economic-Cost 评估 of Physical AI Agents

**原标题**: CostNav: A Navigation Benchmark for Real-World Economic-Cost Evaluation of Physical AI Agents

**作者**: Haebin Seong, Sungmin Kim, Yongjun Cho, Myunchul Joe, Geunwoo Kim, Yubeen Park, Sunhoo Kim, Yoonshik Kim, Suhwan Choi, Jaeyoon Jung, Jiyong Youn, Jinmyung Kwak, Sunghee Ahn, Jaemin Lee, Younggil Do, Seungyeop Yi, Woojin Cheong, Minhyeok Oh, Minchan Kim, Seongjae Kang, Samwoo Seong, Youngjae Yu, Yunsung Lee
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2511.20216v5

**中文摘要**:
> arXiv:2511.20216v5 Announce Type: replace-cross 
摘要: While current navigation benchmarks prioritize task success in simplified settings, they neglect the multidimensional economic constraints essential for the real-world commercialization of 自主 delivery systems. We introduce CostNav, an Economic Navigation 基准 that evaluates physical AI agents through comprehensive economic cost-revenue analysis aligned with real-world business operations. By integrating industry-standard data--such as Securities and Exchange Commission (SEC) filings and Abbreviated Injury Scale (AIS) injury reports--with Isaac Sim's detailed collision and cargo dynamics, CostNav transcends simple task completion to accurately evaluate business 价值 in complex, real-world scenarios. To our knowledge, CostNav is the first phys...

**Original Abstract**:
> arXiv:2511.20216v5 Announce Type: replace-cross 
Abstract: While current navigation benchmarks prioritize task success in simplified settings, they neglect the multidimensional economic constraints essential for the real-world commercialization of autonomous delivery systems. We introduce CostNav, an Economic Navigation Benchmark that evaluates physical AI agents through comprehensive economic cost-revenue analysis aligned with real-world business operations. By integrating industry-standard data--such as Securities and Exchange Commission (SEC) filings and Abbreviated Injury Scale (AIS) injury reports--with Isaac Sim's detailed collision and cargo dynamics, CostNav transcends simple task completion to accurately evaluate business value in complex, real-world scenarios. To our knowledge, C...

---

## 221. Cross-embodied Co-design for Dexterous Hands

**原标题**: Cross-embodied Co-design for Dexterous Hands

**作者**: Kehlani Fay, Darin Anthony Djapri, Anya Zorin, James Clinton, Ali El Lahib, Hao Su, Michael T. Tolley, Sha Yi, Xiaolong Wang
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2512.03743v3

**中文摘要**:
> arXiv:2512.03743v3 Announce Type: replace-cross 
摘要: Dexterous manipulation is limited by both 控制 and design, without consensus as to what makes manipulators best for performing dexterous tasks. This raises a fundamental challenge: how should we design and 控制 robot manipulators that are optimized for dexterity? We present a co-design 框架 that learns task-specific hand morphology and complementary dexterous 控制 policies. The 框架 supports 1) an expansive morphology 搜索 space including joint, finger, and palm 生成, 2) 可扩展 评估 across the wide design space via morphology-conditioned cross-embodied 控制, and 3) real-world fabrication with accessible components. We evaluate the 方案 across multiple dexterous tasks, including in-hand rotation with simulation and real 部署. Our 框架 enables an end-to-end pipeline...

**Original Abstract**:
> arXiv:2512.03743v3 Announce Type: replace-cross 
Abstract: Dexterous manipulation is limited by both control and design, without consensus as to what makes manipulators best for performing dexterous tasks. This raises a fundamental challenge: how should we design and control robot manipulators that are optimized for dexterity? We present a co-design framework that learns task-specific hand morphology and complementary dexterous control policies. The framework supports 1) an expansive morphology search space including joint, finger, and palm generation, 2) scalable evaluation across the wide design space via morphology-conditioned cross-embodied control, and 3) real-world fabrication with accessible components. We evaluate the approach across multiple dexterous tasks, including in-hand rota...

---

## 222. A 可扩展 and 实时 神经 decoder for topological quantum codes

**原标题**: A scalable and real-time neural decoder for topological quantum codes

**作者**: Andrew W. Senior, Thomas Edlich, Francisco J. H. Heras, Lei M. Zhang, Oscar Higgott, James S. Spencer, Taylor Applebaum, Sam Blackwell, Justin Ledford, Akvil\.e \v{Z}emgulyt\.e, Augustin \v{Z}\'idek, Noah Shutty, Andrew Cowie, Yin Li, George Holland, Peter Brooks, Charlie Beattie, Michael Newman, Alex Davies, Cody Jones, Sergio Boixo, Hartmut Neven, Pushmeet Kohli, Johannes Bausch
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2512.07737v2

**中文摘要**:
> arXiv:2512.07737v2 Announce Type: replace-cross 
摘要: Fault-tolerant quantum computing will require error rates far below those achievable with physical qubits. Quantum error correction (QEC) bridges this gap, but depends on decoders being simultaneously fast, 准确, and 可扩展. This combination of requirements remains unmet by a machine-学习 decoder, nor by any decoder for promising resource-高效 codes such as the color 代码. Here we introduce AlphaQubit 2, a 神经-网络 decoder that achieves near-optimal logical error rates for both surface and color codes at scale under realistic noise. For the color 代码, it is orders of magnitude faster than other high-accuracy decoders. We demonstrate 实时 decoding faster than 1{\mu}s per cycle on commercial accelerators: for the surface 代码 to distance 11, with better accu...

**Original Abstract**:
> arXiv:2512.07737v2 Announce Type: replace-cross 
Abstract: Fault-tolerant quantum computing will require error rates far below those achievable with physical qubits. Quantum error correction (QEC) bridges this gap, but depends on decoders being simultaneously fast, accurate, and scalable. This combination of requirements remains unmet by a machine-learning decoder, nor by any decoder for promising resource-efficient codes such as the color code. Here we introduce AlphaQubit 2, a neural-network decoder that achieves near-optimal logical error rates for both surface and color codes at scale under realistic noise. For the color code, it is orders of magnitude faster than other high-accuracy decoders. We demonstrate real-time decoding faster than 1{\mu}s per cycle on commercial accelerators: f...

---

## 223. Toward Closed-loop Molecular Discovery via Language 模型, Property Alignment and Strategic 搜索

**原标题**: Toward Closed-loop Molecular Discovery via Language Model, Property Alignment and Strategic Search

**作者**: Junkai Ji, Zhangfan Yang, Dong Xu, Ruibin Bai, Jianqiang Li, Tingjun Hou, Zexuan Zhu
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2512.09566v3

**中文摘要**:
> arXiv:2512.09566v3 Announce Type: replace-cross 
摘要: Drug discovery is a time-consuming and expensive process, with traditional 高吞吐 and docking-based virtual screening hampered by low success rates and limited scalability. Recent advances in 生成式 modelling, including autoregressive, diffusion, and flow-based approaches, have enabled de novo ligand design beyond the limits of enumerative screening. Yet these models often suffer from inadequate 泛化, limited interpretability, and an overemphasis on binding affinity at the expense of key pharmacological properties, thereby restricting their translational utility. Here we present Trio, a molecular 生成 框架 integrating fragment-based molecular language modeling, 强化 学习, and Monte Carlo tree 搜索, for effective and 可解释 closed-loop targeted molecular desi...

**Original Abstract**:
> arXiv:2512.09566v3 Announce Type: replace-cross 
Abstract: Drug discovery is a time-consuming and expensive process, with traditional high-throughput and docking-based virtual screening hampered by low success rates and limited scalability. Recent advances in generative modelling, including autoregressive, diffusion, and flow-based approaches, have enabled de novo ligand design beyond the limits of enumerative screening. Yet these models often suffer from inadequate generalization, limited interpretability, and an overemphasis on binding affinity at the expense of key pharmacological properties, thereby restricting their translational utility. Here we present Trio, a molecular generation framework integrating fragment-based molecular language modeling, reinforcement learning, and Monte Car...

---

## 224. Maximum Risk Minimization with Random Forests

**原标题**: Maximum Risk Minimization with Random Forests

**作者**: Francesco Freni, Anya Fries, Linus K\"uhne, Markus Reichstein, Jonas Peters
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2512.10445v2

**中文摘要**:
> arXiv:2512.10445v2 Announce Type: replace-cross 
摘要: We consider a regression setting where observations are collected in different environments modeled by different data distributions. The field of 分布外 (OOD) 泛化 aims to design methods that generalize better to test environments whose distributions differ from those observed during 训练. One line of such works has proposed to minimize the maximum risk across environments, a principle that we refer to as MaxRM (Maximum Risk Minimization). In this work, we introduce variants of random forests based on the principle of MaxRM. We provide computationally 高效 algorithms and prove statistical consistency for our primary 方法. Our proposed 方法 can be used with each of the following three risks: the mean squared error, the negative 奖励, and the regret (whi...

**Original Abstract**:
> arXiv:2512.10445v2 Announce Type: replace-cross 
Abstract: We consider a regression setting where observations are collected in different environments modeled by different data distributions. The field of out-of-distribution (OOD) generalization aims to design methods that generalize better to test environments whose distributions differ from those observed during training. One line of such works has proposed to minimize the maximum risk across environments, a principle that we refer to as MaxRM (Maximum Risk Minimization). In this work, we introduce variants of random forests based on the principle of MaxRM. We provide computationally efficient algorithms and prove statistical consistency for our primary method. Our proposed method can be used with each of the following three risks: the m...

---

## 225. Data relativistic uncertainty 框架 for low-illumination anime scenery 图像 enhancement

**原标题**: Data relativistic uncertainty framework for low-illumination anime scenery image enhancement

**作者**: Yiquan Gao, John See
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2512.21944v3

**中文摘要**:
> arXiv:2512.21944v3 Announce Type: replace-cross 
摘要: By contrast with the prevailing works of low-light enhancement in natural images and videos, this study copes with the low-illumination quality degradation in anime scenery images to bridge the domain gap. For such an underexplored enhancement task, we first curate images from various sources and construct an unpaired anime scenery 数据集 with diverse environments and illumination conditions to address the data scarcity. To exploit the power of uncertainty information inherent with the diverse illumination conditions, we propose a Data Relativistic Uncertainty (DRU) 框架, motivated by the idea from Relativistic GAN. By analogy with the wave-particle duality of light, our 框架 interpretably defines and quantifies the illumination uncertainty of ...

**Original Abstract**:
> arXiv:2512.21944v3 Announce Type: replace-cross 
Abstract: By contrast with the prevailing works of low-light enhancement in natural images and videos, this study copes with the low-illumination quality degradation in anime scenery images to bridge the domain gap. For such an underexplored enhancement task, we first curate images from various sources and construct an unpaired anime scenery dataset with diverse environments and illumination conditions to address the data scarcity. To exploit the power of uncertainty information inherent with the diverse illumination conditions, we propose a Data Relativistic Uncertainty (DRU) framework, motivated by the idea from Relativistic GAN. By analogy with the wave-particle duality of light, our framework interpretably defines and quantifies the illu...

---

## 226. 梯度 Dynamics of 注意力: How Cross-熵 Sculpts 贝叶斯 Manifolds

**原标题**: Gradient Dynamics of Attention: How Cross-Entropy Sculpts Bayesian Manifolds

**作者**: Naman Agarwal, Siddhartha R. Dalal, Vishal Misra
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2512.22473v4

**中文摘要**:
> arXiv:2512.22473v4 Announce Type: replace-cross 
摘要: Transformers empirically perform precise 概率 推理 in carefully constructed ``贝叶斯 wind tunnels'' and in large-scale language models, yet the mechanisms by which 梯度-based 学习 creates the required internal geometry remain opaque. We provide a complete first-order analysis of how cross-熵 训练 reshapes 注意力 scores and 价值 vectors in a Transformer 注意力 head. Our core 结果 is an \emph{优势-based routing law} for 注意力 scores, \[ \frac{\partial L}{\partial s_{ij}} = \alpha_{ij}\bigl(b_{ij}-\mathbb{E}_{\alpha_i}[b]\bigr), \qquad b_{ij} := u_i^\top v_j, \] coupled with a \emph{responsibility-weighted update} for values, \[ \Delta v_j = -\eta\sum_i \alpha_{ij} u_i, \] where $u_i$ is the upstream 梯度 at position $i$ and $\alpha_{ij}$ are 注意力 weights. These equation...

**Original Abstract**:
> arXiv:2512.22473v4 Announce Type: replace-cross 
Abstract: Transformers empirically perform precise probabilistic reasoning in carefully constructed ``Bayesian wind tunnels'' and in large-scale language models, yet the mechanisms by which gradient-based learning creates the required internal geometry remain opaque. We provide a complete first-order analysis of how cross-entropy training reshapes attention scores and value vectors in a transformer attention head. Our core result is an \emph{advantage-based routing law} for attention scores, \[ \frac{\partial L}{\partial s_{ij}} = \alpha_{ij}\bigl(b_{ij}-\mathbb{E}_{\alpha_i}[b]\bigr), \qquad b_{ij} := u_i^\top v_j, \] coupled with a \emph{responsibility-weighted update} for values, \[ \Delta v_j = -\eta\sum_i \alpha_{ij} u_i, \] where $u_i$...

---

## 227. 采样 via Stochastic Interpolants by Langevin-based Velocity and Initialization Estimation in Flow ODEs

**原标题**: Sampling via Stochastic Interpolants by Langevin-based Velocity and Initialization Estimation in Flow ODEs

**作者**: Chenguang Duan, Yuling Jiao, Gabriele Steidl, Christian Wald, Jerry Zhijian Yang, Ruizhe Zhang
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2601.08527v2

**中文摘要**:
> arXiv:2601.08527v2 Announce Type: replace-cross 
摘要: We propose a novel 方法 for 采样 from unnormalized Boltzmann densities based on a probability flow ordinary differential equation (ODE) derived from linear stochastic interpolants. The key innovation of our 方案 is the use of a sequence of Langevin samplers to enable 高效 simulation of the flow. Specifically, these Langevin samplers are employed (i) to generate samples from the interpolant distribution at intermediate times and (ii) to construct, starting from these intermediate times, a 鲁棒 estimator of the velocity field governing the probability flow ODE. Theoretically, we provide convergence guarantees for both Langevin components, and establish a non-asymptotic convergence rate for the probability flow ODE. Extensive numerical experiments de...

**Original Abstract**:
> arXiv:2601.08527v2 Announce Type: replace-cross 
Abstract: We propose a novel method for sampling from unnormalized Boltzmann densities based on a probability flow ordinary differential equation (ODE) derived from linear stochastic interpolants. The key innovation of our approach is the use of a sequence of Langevin samplers to enable efficient simulation of the flow. Specifically, these Langevin samplers are employed (i) to generate samples from the interpolant distribution at intermediate times and (ii) to construct, starting from these intermediate times, a robust estimator of the velocity field governing the probability flow ODE. Theoretically, we provide convergence guarantees for both Langevin components, and establish a non-asymptotic convergence rate for the probability flow ODE. E...

---

## 228. Error Analysis of 贝叶斯 Inverse Problems with 生成式 Priors

**原标题**: Error Analysis of Bayesian Inverse Problems with Generative Priors

**作者**: Bamdad Hosseini, Ziqi Huang
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2601.17374v2

**中文摘要**:
> arXiv:2601.17374v2 Announce Type: replace-cross 
摘要: Data-driven methods for the solution of inverse problems have become widely popular in recent years thanks to the rise of machine 学习 techniques. A popular 方案 concerns the 训练 of a 生成式 模型 on additional data to learn a bespoke prior for the problem at hand. In this article we present an analysis for such problems by presenting quantitative error bounds for minimum Wasserstein-2 生成式 models for the prior. We show that under some assumptions, the error in the posterior due to the 生成式 prior will inherit the same rate as the prior with respect to the Wasserstein-1 distance. We further present numerical experiments that verify that aspects of our error analysis manifests in some benchmarks followed by an elliptic PDE inverse problem where a 生成式 p...

**Original Abstract**:
> arXiv:2601.17374v2 Announce Type: replace-cross 
Abstract: Data-driven methods for the solution of inverse problems have become widely popular in recent years thanks to the rise of machine learning techniques. A popular approach concerns the training of a generative model on additional data to learn a bespoke prior for the problem at hand. In this article we present an analysis for such problems by presenting quantitative error bounds for minimum Wasserstein-2 generative models for the prior. We show that under some assumptions, the error in the posterior due to the generative prior will inherit the same rate as the prior with respect to the Wasserstein-1 distance. We further present numerical experiments that verify that aspects of our error analysis manifests in some benchmarks followed ...

---

## 229. Singular 贝叶斯 神经 Networks

**原标题**: Singular Bayesian Neural Networks

**作者**: Mame Diarra Toure, David A. Stephens
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2602.00387v2

**中文摘要**:
> arXiv:2602.00387v2 Announce Type: replace-cross 
摘要: 贝叶斯 神经 networks promise calibrated uncertainty but require $O(mn)$ parameters for standard mean-field Gaussian posteriors. We argue this cost is often unnecessary, particularly when weight matrices exhibit fast singular 价值 decay. By parameterizing weights as $W = AB^{\top}$ with $A \in \mathbb{R}^{m \times r}$, $B \in \mathbb{R}^{n \times r}$, we induce a posterior that is singular with respect to the Lebesgue measure, concentrating on the rank-$r$ manifold. This singularity captures structured weight correlations through shared 隐变量 factors, geometrically distinct from mean-field's independence assumption. We derive PAC-Bayes 泛化 bounds whose complexity term scales as $\sqrt{r(m+n)}$ instead of $\sqrt{m n}$, and prove 损失 bounds that decom...

**Original Abstract**:
> arXiv:2602.00387v2 Announce Type: replace-cross 
Abstract: Bayesian neural networks promise calibrated uncertainty but require $O(mn)$ parameters for standard mean-field Gaussian posteriors. We argue this cost is often unnecessary, particularly when weight matrices exhibit fast singular value decay. By parameterizing weights as $W = AB^{\top}$ with $A \in \mathbb{R}^{m \times r}$, $B \in \mathbb{R}^{n \times r}$, we induce a posterior that is singular with respect to the Lebesgue measure, concentrating on the rank-$r$ manifold. This singularity captures structured weight correlations through shared latent factors, geometrically distinct from mean-field's independence assumption. We derive PAC-Bayes generalization bounds whose complexity term scales as $\sqrt{r(m+n)}$ instead of $\sqrt{m n}...

---

## 230. Emergence of Distortions in High-Dimensional Guided Diffusion Models

**原标题**: Emergence of Distortions in High-Dimensional Guided Diffusion Models

**作者**: Enrico Ventura, Beatrice Achilli, Luca Ambrogioni, Carlo Lucibello
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2602.00716v3

**中文摘要**:
> arXiv:2602.00716v3 Announce Type: replace-cross 
摘要: Classifier-free guidance (CFG) is the de facto standard for conditional 采样 in diffusion models, yet it often leads to a 损失 of diversity in generated samples. We formalize this phenomenon as 生成式 distortion, defined as the mismatch between the CFG-induced 采样 distribution and the true conditional distribution. Considering Gaussian mixtures and their exact scores, and leveraging tools from statistical physics, we characterize the onset of distortion in a high-dimensional regime as a function of the number of classes. Our analysis reveals that distortions emerge through a phase 转移 in the effective potential governing the guided dynamics. In particular, our dynamical mean-field analysis shows that distortion persists when the number of modes g...

**Original Abstract**:
> arXiv:2602.00716v3 Announce Type: replace-cross 
Abstract: Classifier-free guidance (CFG) is the de facto standard for conditional sampling in diffusion models, yet it often leads to a loss of diversity in generated samples. We formalize this phenomenon as generative distortion, defined as the mismatch between the CFG-induced sampling distribution and the true conditional distribution. Considering Gaussian mixtures and their exact scores, and leveraging tools from statistical physics, we characterize the onset of distortion in a high-dimensional regime as a function of the number of classes. Our analysis reveals that distortions emerge through a phase transition in the effective potential governing the guided dynamics. In particular, our dynamical mean-field analysis shows that distortion ...

---

## 231. Universality of General Spiked Tensor Models

**原标题**: Universality of General Spiked Tensor Models

**作者**: Yanjin Xiang, Zhihua Zhang
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2602.04472v2

**中文摘要**:
> arXiv:2602.04472v2 Announce Type: replace-cross 
摘要: We study asymmetric rank-one spiked tensor models in the high-dimensional regime, where the noise entries are independent and identically 分布式 with zero mean, unit variance, and finite fourth moment. This extends the classical Gaussian 框架 to a substantially broader class of noise distributions. We analyze the maximum-likelihood estimator associated with the best rank-one approximation of an order-$d$ tensor, for $d\ge 3$.
  Our 方案 is formulated along an informative, spectrally separated branch of stationary points of the non-convex maximum-likelihood landscape. In the core order-three asymmetric 模型, we verify locally in the high-signal regime that such an informative branch exists and remains separated from the bulk. Under this branch-选择 ...

**Original Abstract**:
> arXiv:2602.04472v2 Announce Type: replace-cross 
Abstract: We study asymmetric rank-one spiked tensor models in the high-dimensional regime, where the noise entries are independent and identically distributed with zero mean, unit variance, and finite fourth moment. This extends the classical Gaussian framework to a substantially broader class of noise distributions. We analyze the maximum-likelihood estimator associated with the best rank-one approximation of an order-$d$ tensor, for $d\ge 3$.
  Our approach is formulated along an informative, spectrally separated branch of stationary points of the non-convex maximum-likelihood landscape. In the core order-three asymmetric model, we verify locally in the high-signal regime that such an informative branch exists and remains separated from t...

---

## 232. GOT-JEPA: Generic Object Tracking with 模型 Adaptation and Occlusion Handling using Joint-嵌入 Predictive 架构

**原标题**: GOT-JEPA: Generic Object Tracking with Model Adaptation and Occlusion Handling using Joint-Embedding Predictive Architecture

**作者**: Shih-Fang Chen, Jun-Cheng Chen, I-Hong Jhuo, Yen-Yu Lin
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2602.14771v2

**中文摘要**:
> arXiv:2602.14771v2 Announce Type: replace-cross 
摘要: The human 视觉 系统 tracks objects by integrating current observations with previously observed information, adapting to 目标 and scene changes, and 推理 about occlusion at fine granularity. In contrast, recent generic object trackers are often optimized for 训练 targets, which limits 鲁棒性 and 泛化 in unseen scenarios, and their occlusion 推理 remains coarse, lacking detailed modeling of occlusion patterns. To address these limitations in 泛化 and occlusion perception, we propose GOT-JEPA, a 模型-predictive pretraining 框架 that extends JEPA from predicting 图像 features to predicting tracking models. Given identical historical information, a teacher predictor generates pseudo-tracking models from a clean current frame, and a student predictor learns to predic...

**Original Abstract**:
> arXiv:2602.14771v2 Announce Type: replace-cross 
Abstract: The human visual system tracks objects by integrating current observations with previously observed information, adapting to target and scene changes, and reasoning about occlusion at fine granularity. In contrast, recent generic object trackers are often optimized for training targets, which limits robustness and generalization in unseen scenarios, and their occlusion reasoning remains coarse, lacking detailed modeling of occlusion patterns. To address these limitations in generalization and occlusion perception, we propose GOT-JEPA, a model-predictive pretraining framework that extends JEPA from predicting image features to predicting tracking models. Given identical historical information, a teacher predictor generates pseudo-tr...

---

## 233. ZACH-ViT: Regime-Dependent Inductive 偏见 in Compact Vision Transformers for Medical Imaging

**原标题**: ZACH-ViT: Regime-Dependent Inductive Bias in Compact Vision Transformers for Medical Imaging

**作者**: Athanasios Angelakis
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2602.17929v2

**中文摘要**:
> arXiv:2602.17929v2 Announce Type: replace-cross 
摘要: Vision Transformers rely on positional embeddings and class tokens encoding fixed spatial priors. While effective for natural images, these priors may be suboptimal when spatial layout is weakly informative, a frequent condition in medical imaging. We introduce ZACH-ViT (Zero-token Adaptive Compact Hierarchical Vision Transformer), a compact Vision Transformer that removes positional embeddings and the [CLS] token, achieving permutation-invariant patch processing via global average pooling. Zero-token denotes removal of the dedicated aggregation token and positional encodings. Patch tokens remain unchanged. Adaptive residual projections preserve 训练 stability under strict parameter constraints. We evaluate ZACH-ViT across seven MedMNIST d...

**Original Abstract**:
> arXiv:2602.17929v2 Announce Type: replace-cross 
Abstract: Vision Transformers rely on positional embeddings and class tokens encoding fixed spatial priors. While effective for natural images, these priors may be suboptimal when spatial layout is weakly informative, a frequent condition in medical imaging. We introduce ZACH-ViT (Zero-token Adaptive Compact Hierarchical Vision Transformer), a compact Vision Transformer that removes positional embeddings and the [CLS] token, achieving permutation-invariant patch processing via global average pooling. Zero-token denotes removal of the dedicated aggregation token and positional encodings. Patch tokens remain unchanged. Adaptive residual projections preserve training stability under strict parameter constraints. We evaluate ZACH-ViT across seve...

---

## 234. Conformal Tradeoffs: Operational Profiles Beyond Coverage

**原标题**: Conformal Tradeoffs: Operational Profiles Beyond Coverage

**作者**: Petrus H. Zwart
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2602.18045v3

**中文摘要**:
> arXiv:2602.18045v3 Announce Type: replace-cross 
摘要: Conformal prediction gives exact finite-sample coverage guarantees under exchangeability, but deployed systems are judged by more than coverage alone. For a fixed calibrated rule reused over a finite operational window, stakeholders also care about 部署-facing quantities such as commitment frequency, deferral, and decisive error exposure. These are not determined by coverage: calibration choices with similar coverage can still induce materially different operational profiles. We study this characterization gap in a scoped setting: binary split conformal prediction under exchangeability with a fixed deployed rule. We introduce the Small-Sample Beta Correction (SSBC) which gives finite-sample coverage semantics for the deployed rule: it inve...

**Original Abstract**:
> arXiv:2602.18045v3 Announce Type: replace-cross 
Abstract: Conformal prediction gives exact finite-sample coverage guarantees under exchangeability, but deployed systems are judged by more than coverage alone. For a fixed calibrated rule reused over a finite operational window, stakeholders also care about deployment-facing quantities such as commitment frequency, deferral, and decisive error exposure. These are not determined by coverage: calibration choices with similar coverage can still induce materially different operational profiles. We study this characterization gap in a scoped setting: binary split conformal prediction under exchangeability with a fixed deployed rule. We introduce the Small-Sample Beta Correction (SSBC) which gives finite-sample coverage semantics for the deployed...

---

## 235. Benchmarking Graph 神经 Networks in Solving Hard Constraint Satisfaction Problems

**原标题**: Benchmarking Graph Neural Networks in Solving Hard Constraint Satisfaction Problems

**作者**: Geri Skenderi, Lorenzo Buffoni, Francesco D'Amico, David Machado, Raffaele Marino, Matteo Negri, Federico Ricci-Tersenghi, Carlo Lucibello, Maria Chiara Angelini
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2602.18419v2

**中文摘要**:
> arXiv:2602.18419v2 Announce Type: replace-cross 
摘要: Graph 神经 networks (GNNs) are increasingly applied to hard 优化 problems, often claiming superiority over classical heuristics. However, such claims risk being unsolid due to a lack of standard benchmarks on truly hard instances. From a statistical physics perspective, we propose new hard benchmarks based on random problems. We provide these benchmarks, along with 性能 results from both classical heuristics and GNNs. Our fair comparison shows that classical algorithms still outperform GNNs. We discuss the challenges for 神经 networks in this domain. Future claims of superiority can be made more 鲁棒 using our benchmarks, available at https://GitHub.com/ArtLabBocconi/RandCSPBench.

**Original Abstract**:
> arXiv:2602.18419v2 Announce Type: replace-cross 
Abstract: Graph neural networks (GNNs) are increasingly applied to hard optimization problems, often claiming superiority over classical heuristics. However, such claims risk being unsolid due to a lack of standard benchmarks on truly hard instances. From a statistical physics perspective, we propose new hard benchmarks based on random problems. We provide these benchmarks, along with performance results from both classical heuristics and GNNs. Our fair comparison shows that classical algorithms still outperform GNNs. We discuss the challenges for neural networks in this domain. Future claims of superiority can be made more robust using our benchmarks, available at https://github.com/ArtLabBocconi/RandCSPBench.

---

## 236. How Large Language Models Get Stuck: Early structure with persistent errors

**原标题**: How Large Language Models Get Stuck: Early structure with persistent errors

**作者**: Alokesh Manna, William Snyder, Whitney Tabor
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.00359v2

**中文摘要**:
> arXiv:2603.00359v2 Announce Type: replace-cross 
摘要: Linguistic insights may help make Large Language 模型 (大语言模型) 训练 more 高效. We trained Meta's OPT 模型 on the 100M word BabyLM 数据集, and evaluated it on the BLiMP 基准, which consists of 67 classes, each defined by sentence pairs that differ in a targeted syntactic or semantic rule violation. We tested the 模型's preference for grammatical over ungrammatical sentences across 训练 iterations and grammatical types. In nearly one-third of the BLiMP classes, OPT fails to consistently assign a higher likelihood to grammatical sentences, even after extensive 训练. When it fails, it often establishes a clear (erroneous) separation of the likelihoods at an early stage of processing and sustains this to the end of our 训练 phase. We hypothesize that this mis-cate...

**Original Abstract**:
> arXiv:2603.00359v2 Announce Type: replace-cross 
Abstract: Linguistic insights may help make Large Language Model (LLM) training more efficient. We trained Meta's OPT model on the 100M word BabyLM dataset, and evaluated it on the BLiMP benchmark, which consists of 67 classes, each defined by sentence pairs that differ in a targeted syntactic or semantic rule violation. We tested the model's preference for grammatical over ungrammatical sentences across training iterations and grammatical types. In nearly one-third of the BLiMP classes, OPT fails to consistently assign a higher likelihood to grammatical sentences, even after extensive training. When it fails, it often establishes a clear (erroneous) separation of the likelihoods at an early stage of processing and sustains this to the end o...

---

## 237. CARE: Towards Clinical Accountability in 多模态 Medical 推理 with an Evidence-Grounded Agentic 框架

**原标题**: CARE: Towards Clinical Accountability in Multi-Modal Medical Reasoning with an Evidence-Grounded Agentic Framework

**作者**: Yuexi Du, Jinglu Wang, Shujie Liu, Nicha C. Dvornek, Yan Lu
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.01607v2

**中文摘要**:
> arXiv:2603.01607v2 Announce Type: replace-cross 
摘要: Large 视觉 language models (VLMs) have shown strong 多模态 medical 推理 ability, but most operate as end-to-end black boxes, diverging from clinicians' evidence-based, staged workflows and hindering clinical accountability. Complementarily, expert 视觉 grounding models can accurately localize regions of interest (ROIs), providing explicit, reliable evidence that improves both 推理 accuracy and trust. In this 论文, we introduce CARE, advancing Clinical Accountability in 多模态 medical 推理 with an Evidence-grounded agentic 框架. Unlike existing approaches that couple grounding and 推理 within a single generalist 模型, CARE decomposes the task into coordinated sub-modules to reduce shortcut 学习 and hallucination: a compact VLM proposes relevant medical entities; a...

**Original Abstract**:
> arXiv:2603.01607v2 Announce Type: replace-cross 
Abstract: Large visual language models (VLMs) have shown strong multi-modal medical reasoning ability, but most operate as end-to-end black boxes, diverging from clinicians' evidence-based, staged workflows and hindering clinical accountability. Complementarily, expert visual grounding models can accurately localize regions of interest (ROIs), providing explicit, reliable evidence that improves both reasoning accuracy and trust. In this paper, we introduce CARE, advancing Clinical Accountability in multi-modal medical Reasoning with an Evidence-grounded agentic framework. Unlike existing approaches that couple grounding and reasoning within a single generalist model, CARE decomposes the task into coordinated sub-modules to reduce shortcut le...

---

## 238. CFG-Ctrl: 控制-Based Classifier-Free Diffusion Guidance

**原标题**: CFG-Ctrl: Control-Based Classifier-Free Diffusion Guidance

**作者**: Hanyang Wang, Yiyang Liu, Jiawei Chi, Fangfu Liu, Ran Xue, Yueqi Duan
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.03281v2

**中文摘要**:
> arXiv:2603.03281v2 Announce Type: replace-cross 
摘要: Classifier-Free Guidance (CFG) has emerged as a central 方案 for enhancing semantic alignment in flow-based diffusion models. In this 论文, we explore a unified 框架 called CFG-Ctrl, which reinterprets CFG as a 控制 applied to the first-order continuous-time 生成式 flow, using the conditional-unconditional discrepancy as an error signal to adjust the velocity field. From this perspective, we summarize vanilla CFG as a proportional controller (P-控制) with fixed gain, and typical follow-up variants develop extended 控制-law designs derived from it. However, existing methods mainly rely on linear 控制, inherently leading to instability, overshooting, and degraded semantic fidelity especially on large guidance scales. To address this, we introduce Sliding M...

**Original Abstract**:
> arXiv:2603.03281v2 Announce Type: replace-cross 
Abstract: Classifier-Free Guidance (CFG) has emerged as a central approach for enhancing semantic alignment in flow-based diffusion models. In this paper, we explore a unified framework called CFG-Ctrl, which reinterprets CFG as a control applied to the first-order continuous-time generative flow, using the conditional-unconditional discrepancy as an error signal to adjust the velocity field. From this perspective, we summarize vanilla CFG as a proportional controller (P-control) with fixed gain, and typical follow-up variants develop extended control-law designs derived from it. However, existing methods mainly rely on linear control, inherently leading to instability, overshooting, and degraded semantic fidelity especially on large guidanc...

---

## 239. RACAS: Controlling Diverse Robots With a Single Agentic 系统

**原标题**: RACAS: Controlling Diverse Robots With a Single Agentic System

**作者**: Dylan R. Ashley, Jan Przepi\'ora, Yimeng Chen, Ali Abualsaud, Nurzhan Yesmagambet, Shinkyu Park, Eric Feron, J\"urgen Schmidhuber
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.05621v2

**中文摘要**:
> arXiv:2603.05621v2 Announce Type: replace-cross 
摘要: Many robotic platforms expose an API through which external software can command their actuators and read their sensors. However, transitioning from these low-level interfaces to high-level 自主 behaviour requires a complicated pipeline, whose components demand distinct areas of expertise. Existing approaches to bridging this gap either require retraining for every new embodiment or have only been validated across structurally similar platforms. We introduce RACAS (Robot-Agnostic 控制 via Agentic Systems), a cooperative agentic 架构 in which three 大语言模型/VLM-based modules (Monitors, a Controller, and a 内存 Curator) communicate exclusively through natural language to provide closed-loop robot 控制. RACAS requires only a natural language description...

**Original Abstract**:
> arXiv:2603.05621v2 Announce Type: replace-cross 
Abstract: Many robotic platforms expose an API through which external software can command their actuators and read their sensors. However, transitioning from these low-level interfaces to high-level autonomous behaviour requires a complicated pipeline, whose components demand distinct areas of expertise. Existing approaches to bridging this gap either require retraining for every new embodiment or have only been validated across structurally similar platforms. We introduce RACAS (Robot-Agnostic Control via Agentic Systems), a cooperative agentic architecture in which three LLM/VLM-based modules (Monitors, a Controller, and a Memory Curator) communicate exclusively through natural language to provide closed-loop robot control. RACAS requires...

---

## 240. The Coordination Gap: Alternation Metrics for Temporal Dynamics in Multi-智能体 Battle of the Exes

**原标题**: The Coordination Gap: Alternation Metrics for Temporal Dynamics in Multi-Agent Battle of the Exes

**作者**: Nikolaos Al. Papadopoulos, Konstantinos Psannis
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.05789v2

**中文摘要**:
> arXiv:2603.05789v2 Announce Type: replace-cross 
摘要: Multi-智能体 coordination dilemmas expose a fundamental tension between individual 优化 and collective welfare, yet characterizing such coordination requires metrics sensitive to temporal structure and collective dynamics. As a diagnostic testbed, we study a BoE-derived multi-智能体 variant of the Battle of the Exes, formalizing it as a Markov game in which turn-taking emerges as a periodic coordination regime. Conventional outcome-based metrics (e.g., efficiency and min/max 公平性) are temporally blind (they cannot distinguish structured alternation from monopolistic or random access patterns) and 公平性 ratios lose 判别式 power as n grows, obscuring inequities.
  To address this limitation, we introduce Perfect Alternation (PA) as a reference coordinat...

**Original Abstract**:
> arXiv:2603.05789v2 Announce Type: replace-cross 
Abstract: Multi-agent coordination dilemmas expose a fundamental tension between individual optimization and collective welfare, yet characterizing such coordination requires metrics sensitive to temporal structure and collective dynamics. As a diagnostic testbed, we study a BoE-derived multi-agent variant of the Battle of the Exes, formalizing it as a Markov game in which turn-taking emerges as a periodic coordination regime. Conventional outcome-based metrics (e.g., efficiency and min/max fairness) are temporally blind (they cannot distinguish structured alternation from monopolistic or random access patterns) and fairness ratios lose discriminative power as n grows, obscuring inequities.
  To address this limitation, we introduce Perfect ...

---

## 241. A Systematic Comparison of 训练 Objectives for 分布外 检测 in 图像 分类

**原标题**: A Systematic Comparison of Training Objectives for Out-of-Distribution Detection in Image Classification

**作者**: Furkan Gen\c{c}, Onat \"Ozdemir, Emre Akba\c{s}
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.07571v2

**中文摘要**:
> arXiv:2603.07571v2 Announce Type: replace-cross 
摘要: 分布外 (OOD) 检测 is critical in safety-sensitive applications. While this challenge has been addressed from various perspectives, the influence of 训练 objectives on OOD behavior remains comparatively underexplored. In this 论文, we present a systematic comparison of four widely used 训练 objectives: Cross-熵 损失, Prototype 损失, Triplet 损失, and Average Precision (AP) 损失, spanning 概率, prototype-based, metric-学习, and ranking-based supervision, for OOD 检测 in 图像 分类 under standardized OpenOOD protocols. Across CIFAR-10/100 and ImageNet-200, we find that Cross-熵 损失, Prototype 损失, and AP 损失 achieve comparable in-distribution accuracy, while Cross-熵 损失 provides the most consistent near- and far-OOD 性能 overall; the other objectives can be competitive in speci...

**Original Abstract**:
> arXiv:2603.07571v2 Announce Type: replace-cross 
Abstract: Out-of-distribution (OOD) detection is critical in safety-sensitive applications. While this challenge has been addressed from various perspectives, the influence of training objectives on OOD behavior remains comparatively underexplored. In this paper, we present a systematic comparison of four widely used training objectives: Cross-Entropy Loss, Prototype Loss, Triplet Loss, and Average Precision (AP) Loss, spanning probabilistic, prototype-based, metric-learning, and ranking-based supervision, for OOD detection in image classification under standardized OpenOOD protocols. Across CIFAR-10/100 and ImageNet-200, we find that Cross-Entropy Loss, Prototype Loss, and AP Loss achieve comparable in-distribution accuracy, while Cross-Ent...

---

## 242. Micro-Diffusion Compression - Binary Tree Tweedie Denoising for 在线 Probability Estimation

**原标题**: Micro-Diffusion Compression - Binary Tree Tweedie Denoising for Online Probability Estimation

**作者**: Roberto Tacconelli
**分类**: cs.LG
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.08771v2

**中文摘要**:
> arXiv:2603.08771v2 Announce Type: replace-cross 
摘要: We present Midicoth, a lossless compression 系统 that introduces a micro-diffusion denoising layer for improving probability estimates produced by adaptive statistical models. In compressors such as Prediction by Partial Matching (PPM), probability estimates are smoothed by a prior to handle sparse observations. When contexts have been seen only a few times, this prior dominates the prediction and produces distributions that are significantly flatter than the true source distribution, leading to compression inefficiency. Midicoth addresses this limitation by treating prior smoothing as a shrinkage process and applying a reverse denoising step that corrects predicted probabilities using empirical calibration statistics. To make this correct...

**Original Abstract**:
> arXiv:2603.08771v2 Announce Type: replace-cross 
Abstract: We present Midicoth, a lossless compression system that introduces a micro-diffusion denoising layer for improving probability estimates produced by adaptive statistical models. In compressors such as Prediction by Partial Matching (PPM), probability estimates are smoothed by a prior to handle sparse observations. When contexts have been seen only a few times, this prior dominates the prediction and produces distributions that are significantly flatter than the true source distribution, leading to compression inefficiency. Midicoth addresses this limitation by treating prior smoothing as a shrinkage process and applying a reverse denoising step that corrects predicted probabilities using empirical calibration statistics. To make th...

---

## 243. Agentic 控制 Center for Data Product 优化

**原标题**: Agentic Control Center for Data Product Optimization

**作者**: Priyadarshini Tamilselvan, Gregory Bramble, Sola Shirai, Ken C. L. Wong, Faisal Chowdhury, Horst Samulowitz
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10133v1

**中文摘要**:
> arXiv:2603.10133v1 Announce Type: new 
摘要: Data products enable end users to gain greater insights about their data by providing supporting assets, such as example question-SQL pairs which can be answered using the data or views over the database tables. However, producing useful data products is challenging, and typically requires domain experts to hand-craft supporting assets. We propose a 系统 that automates data product improvement through specialized AI agents operating in a continuous 优化 loop. By surfacing questions, monitoring multi-dimensional quality metrics, and supporting human-in-the-loop controls, it transforms data into observable and refinable assets that 平衡 automation with trust and oversight.

**Original Abstract**:
> arXiv:2603.10133v1 Announce Type: new 
Abstract: Data products enable end users to gain greater insights about their data by providing supporting assets, such as example question-SQL pairs which can be answered using the data or views over the database tables. However, producing useful data products is challenging, and typically requires domain experts to hand-craft supporting assets. We propose a system that automates data product improvement through specialized AI agents operating in a continuous optimization loop. By surfacing questions, monitoring multi-dimensional quality metrics, and supporting human-in-the-loop controls, it transforms data into observable and refinable assets that balance automation with trust and oversight.

---

## 244. Hybrid Self-evolving Structured 内存 for GUI Agents

**原标题**: Hybrid Self-evolving Structured Memory for GUI Agents

**作者**: Sibo Zhu, Wenyi Wu, Kun Zhou, Stephen Wang, Biwei Huang
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10291v1

**中文摘要**:
> arXiv:2603.10291v1 Announce Type: new 
摘要: The remarkable progress of vision-language models (VLMs) has enabled GUI agents to interact with computers in a human-like manner. Yet real-world computer-use tasks remain difficult due to long-视野 workflows, diverse interfaces, and frequent intermediate errors. Prior work equips agents with external 内存 built from large collections of trajectories, but relies on flat 检索 over discrete summaries or continuous embeddings, falling short of the structured organization and self-evolving characteristics of human 内存. Inspired by the brain, we propose Hybrid Self-evolving Structured 内存 (HyMEM), a graph-based 内存 that couples discrete high-level symbolic nodes with continuous 轨迹 embeddings. HyMEM maintains a graph structure to support multi-hop 检索, self-进化 vi...

**Original Abstract**:
> arXiv:2603.10291v1 Announce Type: new 
Abstract: The remarkable progress of vision-language models (VLMs) has enabled GUI agents to interact with computers in a human-like manner. Yet real-world computer-use tasks remain difficult due to long-horizon workflows, diverse interfaces, and frequent intermediate errors. Prior work equips agents with external memory built from large collections of trajectories, but relies on flat retrieval over discrete summaries or continuous embeddings, falling short of the structured organization and self-evolving characteristics of human memory. Inspired by the brain, we propose Hybrid Self-evolving Structured Memory (HyMEM), a graph-based memory that couples discrete high-level symbolic nodes with continuous trajectory embeddings. HyMEM maintains a graph str...

---

## 245. HEAL: Hindsight 熵-Assisted 学习 for 推理 Distillation

**原标题**: HEAL: Hindsight Entropy-Assisted Learning for Reasoning Distillation

**作者**: Wenjing Zhang, Jiangze Yan, Jieyun Huang, Yi Shen, Shuming Shi, Ping Chen, Ning Wang, Zhaoxiang Liu, Kai Wang, Shiguo Lian
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10359v1

**中文摘要**:
> arXiv:2603.10359v1 Announce Type: new 
摘要: Distilling 推理 capabilities from Large 推理 Models (LRMs) into smaller models is typically constrained by the limitation of rejection 采样. Standard methods treat the teacher as a 静态 filter, discarding complex "corner-case" problems where the teacher fails to explore valid solutions independently, thereby creating an artificial "Teacher Ceiling" for the student. In this work, we propose Hindsight 熵-Assisted 学习 (HEAL), an RL-free 框架 designed to bridge this 推理 gap. Drawing on the educational theory of the Zone of Proximal Development(ZPD), HEAL synergizes three core modules: (1) Guided 熵-Assisted Repair (GEAR), an active intervention mechanism that detects critical 推理 breakpoints via 熵 dynamics and injects targeted hindsight hints to repair broken trajec...

**Original Abstract**:
> arXiv:2603.10359v1 Announce Type: new 
Abstract: Distilling reasoning capabilities from Large Reasoning Models (LRMs) into smaller models is typically constrained by the limitation of rejection sampling. Standard methods treat the teacher as a static filter, discarding complex "corner-case" problems where the teacher fails to explore valid solutions independently, thereby creating an artificial "Teacher Ceiling" for the student. In this work, we propose Hindsight Entropy-Assisted Learning (HEAL), an RL-free framework designed to bridge this reasoning gap. Drawing on the educational theory of the Zone of Proximal Development(ZPD), HEAL synergizes three core modules: (1) Guided Entropy-Assisted Repair (GEAR), an active intervention mechanism that detects critical reasoning breakpoints via en...

---

## 246. Beyond Scalars: Evaluating and Understanding 大语言模型 推理 via Geometric Progress and Stability

**原标题**: Beyond Scalars: Evaluating and Understanding LLM Reasoning via Geometric Progress and Stability

**作者**: Xinyan Jiang, Ninghao Liu, Di Wang, Lijie Hu
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10384v1

**中文摘要**:
> arXiv:2603.10384v1 Announce Type: new 
摘要: Evaluating 大语言模型 reliability via scalar probabilities often fails to capture the structural dynamics of 推理. We introduce TRACED, a 框架 that assesses 推理 quality through theoretically grounded geometric kinematics. By decomposing 推理 traces into Progress (displacement) and Stability (curvature), we reveal a distinct topological divergence: correct 推理 manifests as high-progress, stable trajectories, whereas hallucinations are characterized by low-progress, unstable patterns (stalled displacement with high curvature fluctuations). Leveraging these signatures, our 概率 框架 achieves competitive 性能 and superior 鲁棒性 across diverse benchmarks. Crucially, TRACED bridges geometry and cognition by mapping high curvature to ''Hesitation Loops'' and displacement to ...

**Original Abstract**:
> arXiv:2603.10384v1 Announce Type: new 
Abstract: Evaluating LLM reliability via scalar probabilities often fails to capture the structural dynamics of reasoning. We introduce TRACED, a framework that assesses reasoning quality through theoretically grounded geometric kinematics. By decomposing reasoning traces into Progress (displacement) and Stability (curvature), we reveal a distinct topological divergence: correct reasoning manifests as high-progress, stable trajectories, whereas hallucinations are characterized by low-progress, unstable patterns (stalled displacement with high curvature fluctuations). Leveraging these signatures, our probabilistic framework achieves competitive performance and superior robustness across diverse benchmarks. Crucially, TRACED bridges geometry and cogniti...

---

## 247. Verbalizing 大语言模型's Higher-order Uncertainty via Imprecise Probabilities

**原标题**: Verbalizing LLM's Higher-order Uncertainty via Imprecise Probabilities

**作者**: Anita Yang, Krikamol Muandet, Michele Caprio, Siu Lun Chau, Masaki Adachi
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10396v1

**中文摘要**:
> arXiv:2603.10396v1 Announce Type: new 
摘要: Despite the growing demand for eliciting uncertainty from large language models (LLMs), empirical evidence suggests that 大语言模型 behavior is not always adequately captured by the elicitation techniques developed under the classical 概率 uncertainty 框架. This mismatch leads to systematic failure modes, particularly in settings that involve ambiguous question-answering, in-context 学习, and self-reflection. To address this, we propose novel prompt-based uncertainty elicitation techniques grounded in \emph{imprecise probabilities}, a principled 框架 for repesenting and eliciting higher-order uncertainty. Here, first-order uncertainty captures uncertainty over possible responses to a prompt, while second-order uncertainty (uncertainty about uncertainty) quanti...

**Original Abstract**:
> arXiv:2603.10396v1 Announce Type: new 
Abstract: Despite the growing demand for eliciting uncertainty from large language models (LLMs), empirical evidence suggests that LLM behavior is not always adequately captured by the elicitation techniques developed under the classical probabilistic uncertainty framework. This mismatch leads to systematic failure modes, particularly in settings that involve ambiguous question-answering, in-context learning, and self-reflection. To address this, we propose novel prompt-based uncertainty elicitation techniques grounded in \emph{imprecise probabilities}, a principled framework for repesenting and eliciting higher-order uncertainty. Here, first-order uncertainty captures uncertainty over possible responses to a prompt, while second-order uncertainty (un...

---

## 248. Resource-constrained Amazons chess 决策 框架 integrating large language models and graph 注意力

**原标题**: Resource-constrained Amazons chess decision framework integrating large language models and graph attention

**作者**: Tianhao Qian, Zhuoxuan Li, Jinde Cao, Xinli Shi, Hanjie Liu, Leszek Rutkowski
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10512v1

**中文摘要**:
> arXiv:2603.10512v1 Announce Type: new 
摘要: Artificial intelligence has advanced significantly through the development of intelligent game-playing systems, providing rigorous testbeds for 决策-making, strategic 规划, and adaptive 学习. However, resource-constrained environments pose critical challenges, as conventional 深度 学习 methods heavily rely on extensive datasets and computational resources. In this 论文, we propose a lightweight hybrid 框架 for the Game of the Amazons, which explores the paradigm of weak-to-strong 泛化 by integrating the structural 推理 of graph-based 学习 with the 生成式 capabilities of large language models. Specifically, we leverage a Graph 注意力 Autoencoder to inform a multi-step Monte Carlo Tree 搜索, utilize a Stochastic Graph 遗传 算法 to optimize 评估 signals, and harness GPT-4o-mini to ge...

**Original Abstract**:
> arXiv:2603.10512v1 Announce Type: new 
Abstract: Artificial intelligence has advanced significantly through the development of intelligent game-playing systems, providing rigorous testbeds for decision-making, strategic planning, and adaptive learning. However, resource-constrained environments pose critical challenges, as conventional deep learning methods heavily rely on extensive datasets and computational resources. In this paper, we propose a lightweight hybrid framework for the Game of the Amazons, which explores the paradigm of weak-to-strong generalization by integrating the structural reasoning of graph-based learning with the generative capabilities of large language models. Specifically, we leverage a Graph Attention Autoencoder to inform a multi-step Monte Carlo Tree Search, ut...

---

## 249. IH-Challenge: A 训练 数据集 to Improve Instruction Hierarchy on Frontier LLMs

**原标题**: IH-Challenge: A Training Dataset to Improve Instruction Hierarchy on Frontier LLMs

**作者**: Chuan Guo (Michael Pokorny), Juan Felipe Ceron Uribe (Michael Pokorny), Sicheng Zhu (Michael Pokorny), Christopher A. Choquette-Choo (Michael Pokorny), Steph Lin (Michael Pokorny), Nikhil Kandpal (Michael Pokorny), Milad Nasr (Michael Pokorny),  Rai (Michael Pokorny), Sam Toyer, Miles Wang, Yaodong Yu, Alex Beutel, Kai Xiao
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10521v1

**中文摘要**:
> arXiv:2603.10521v1 Announce Type: new 
摘要: Instruction hierarchy (IH) defines how LLMs prioritize 系统, developer, user, and tool instructions under conflict, providing a concrete, trust-ordered 策略 for resolving instruction conflicts. IH is key to defending against jailbreaks, 系统 prompt extractions, and agentic prompt injections. However, 鲁棒 IH behavior is difficult to train: IH failures can be confounded with instruction-following failures, conflicts can be nuanced, and models can learn shortcuts such as overrefusing. We introduce IH-Challenge, a 强化 学习 训练 数据集, to address these difficulties. Fine-tuning GPT-5-Mini on IH-Challenge with 在线 对抗 example 生成 improves IH 鲁棒性 by +10.0% on average across 16 in-distribution, 分布外, and human red-teaming benchmarks (84.1% to 94.1%), reduces unsafe behavio...

**Original Abstract**:
> arXiv:2603.10521v1 Announce Type: new 
Abstract: Instruction hierarchy (IH) defines how LLMs prioritize system, developer, user, and tool instructions under conflict, providing a concrete, trust-ordered policy for resolving instruction conflicts. IH is key to defending against jailbreaks, system prompt extractions, and agentic prompt injections. However, robust IH behavior is difficult to train: IH failures can be confounded with instruction-following failures, conflicts can be nuanced, and models can learn shortcuts such as overrefusing. We introduce IH-Challenge, a reinforcement learning training dataset, to address these difficulties. Fine-tuning GPT-5-Mini on IH-Challenge with online adversarial example generation improves IH robustness by +10.0% on average across 16 in-distribution, o...

---

## 250. Adaptive RAN Slicing 控制 via 奖励-Free Self-Finetuning Agents

**原标题**: Adaptive RAN Slicing Control via Reward-Free Self-Finetuning Agents

**作者**: Yuanhao Li, Haozhe Wang, Geyong Min, Nektarios Georgalas, Wang Miao
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10564v1

**中文摘要**:
> arXiv:2603.10564v1 Announce Type: new 
摘要: The integration of 生成式 AI models into AI-native 网络 systems offers a transformative path toward achieving 自主 and adaptive 控制. However, the application of such models to continuous 控制 tasks is impeded by intrinsic architectural limitations, including finite context windows, the lack of explicit 奖励 signals, and the degradation of the long context. This 论文 posits that the key to unlocking 鲁棒 continuous 控制 is enabling agents to internalize experience by distilling it into their parameters, rather than relying on prompt-based 内存. To this end, we propose a novel self-finetuning 框架 that enables agentic systems to learn continuously through direct interaction with the 环境, bypassing the need for handcrafted rewards. Our 框架 implements a bi-perspective reflec...

**Original Abstract**:
> arXiv:2603.10564v1 Announce Type: new 
Abstract: The integration of Generative AI models into AI-native network systems offers a transformative path toward achieving autonomous and adaptive control. However, the application of such models to continuous control tasks is impeded by intrinsic architectural limitations, including finite context windows, the lack of explicit reward signals, and the degradation of the long context. This paper posits that the key to unlocking robust continuous control is enabling agents to internalize experience by distilling it into their parameters, rather than relying on prompt-based memory. To this end, we propose a novel self-finetuning framework that enables agentic systems to learn continuously through direct interaction with the environment, bypassing the...

---

## 251. CUAAudit: Meta-评估 of Vision-Language Models as Auditors of 自主 Computer-Use Agents

**原标题**: CUAAudit: Meta-Evaluation of Vision-Language Models as Auditors of Autonomous Computer-Use Agents

**作者**: Marta Sumyk, Oleksandr Kosovan
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10577v1

**中文摘要**:
> arXiv:2603.10577v1 Announce Type: new 
摘要: Computer-Use Agents (CUAs) are emerging as a new paradigm in human-computer interaction, enabling 自主 execution of tasks in desktop 环境 by perceiving high-level natural-language instructions. As such agents become increasingly capable and are deployed across diverse desktop environments, evaluating their behavior in a 可扩展 and reliable manner becomes a critical challenge. Existing 评估 pipelines rely on 静态 benchmarks, rule-based success checks, or manual inspection, which are brittle, costly, and poorly aligned with real-world usage. In this work, we study Vision-Language Models (VLMs) as 自主 auditors for assessing CUA task completion directly from observable interactions and conduct a large-scale meta-评估 of five VLMs that judge task success given a nat...

**Original Abstract**:
> arXiv:2603.10577v1 Announce Type: new 
Abstract: Computer-Use Agents (CUAs) are emerging as a new paradigm in human-computer interaction, enabling autonomous execution of tasks in desktop environment by perceiving high-level natural-language instructions. As such agents become increasingly capable and are deployed across diverse desktop environments, evaluating their behavior in a scalable and reliable manner becomes a critical challenge. Existing evaluation pipelines rely on static benchmarks, rule-based success checks, or manual inspection, which are brittle, costly, and poorly aligned with real-world usage. In this work, we study Vision-Language Models (VLMs) as autonomous auditors for assessing CUA task completion directly from observable interactions and conduct a large-scale meta-eva...

---

## 252. Does 大语言模型 Alignment Really Need Diversity? An Empirical Study of Adapting RLVR Methods for Moral 推理

**原标题**: Does LLM Alignment Really Need Diversity? An Empirical Study of Adapting RLVR Methods for Moral Reasoning

**作者**: Zhaowei Zhang, Xiaohan Liu, Xuekai Zhu, Junchao Huang, Ceyao Zhang, Zhiyuan Feng, Yaodong Yang, Xiaoyuan Yi, Xing Xie
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10588v1

**中文摘要**:
> arXiv:2603.10588v1 Announce Type: new 
摘要: 强化 学习 with verifiable rewards (RLVR) has achieved remarkable success in logical 推理 tasks, yet whether large language 模型 (大语言模型) alignment requires fundamentally different approaches remains unclear. Given the apparent tolerance for multiple valid responses in moral 推理, a natural hypothesis is that alignment tasks inherently require diversity-seeking distribution-matching algorithms rather than 奖励-maximizing 策略-based methods. We conduct the first comprehensive empirical study comparing both paradigms on MoReBench. To enable stable RLVR 训练, we build a rubric-grounded 奖励 pipeline by 训练 a Qwen3-1.7B judge 模型. Contrary to our hypothesis, we find that distribution-matching approaches do not demonstrate significant advantages over 奖励-maximizing methods a...

**Original Abstract**:
> arXiv:2603.10588v1 Announce Type: new 
Abstract: Reinforcement learning with verifiable rewards (RLVR) has achieved remarkable success in logical reasoning tasks, yet whether large language model (LLM) alignment requires fundamentally different approaches remains unclear. Given the apparent tolerance for multiple valid responses in moral reasoning, a natural hypothesis is that alignment tasks inherently require diversity-seeking distribution-matching algorithms rather than reward-maximizing policy-based methods. We conduct the first comprehensive empirical study comparing both paradigms on MoReBench. To enable stable RLVR training, we build a rubric-grounded reward pipeline by training a Qwen3-1.7B judge model. Contrary to our hypothesis, we find that distribution-matching approaches do no...

---

## 253. 轨迹-Informed 内存 生成 for Self-Improving 智能体 Systems

**原标题**: Trajectory-Informed Memory Generation for Self-Improving Agent Systems

**作者**: Gaodan Fang, Vatche Isahagian, K. R. Jayaram, Ritesh Kumar, Vinod Muthusamy, Punleuk Oum, Gegi Thomas
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10600v1

**中文摘要**:
> arXiv:2603.10600v1 Announce Type: new 
摘要: 大语言模型-powered agents face a persistent challenge: 学习 from their execution experiences to improve future 性能. While agents can successfully complete many tasks, they often repeat inefficient patterns, fail to recover from similar errors, and miss opportunities to apply successful strategies from past executions. We present a novel 框架 for automatically extracting actionable learnings from 智能体 execution trajectories and utilizing them to improve future 性能 through contextual 内存 检索. Our 方案 comprises four components: (1) a 轨迹 Intelligence Extractor that performs semantic analysis of 智能体 推理 patterns, (2) a 决策 Attribution Analyzer that identifies which decisions and 推理 steps led to failures, recoveries, or inefficiencies, (3) a Contextual 学习 Generator that...

**Original Abstract**:
> arXiv:2603.10600v1 Announce Type: new 
Abstract: LLM-powered agents face a persistent challenge: learning from their execution experiences to improve future performance. While agents can successfully complete many tasks, they often repeat inefficient patterns, fail to recover from similar errors, and miss opportunities to apply successful strategies from past executions. We present a novel framework for automatically extracting actionable learnings from agent execution trajectories and utilizing them to improve future performance through contextual memory retrieval. Our approach comprises four components: (1) a Trajectory Intelligence Extractor that performs semantic analysis of agent reasoning patterns, (2) a Decision Attribution Analyzer that identifies which decisions and reasoning step...

---

## 254. FAME: Formal 摘要 Minimal Explanation for 神经 Networks

**原标题**: FAME: Formal Abstract Minimal Explanation for Neural Networks

**作者**: Ryma Boumazouza, Raya Elsaleh, Melanie Ducoffe, Shahaf Bassan, Guy Katz
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10661v1

**中文摘要**:
> arXiv:2603.10661v1 Announce Type: new 
摘要: We propose FAME (Formal 摘要 Minimal Explanations), a new class of abductive explanations grounded in 摘要 interpretation. FAME is the first 方法 to scale to large 神经 networks while reducing explanation size. Our main contribution is the design of dedicated perturbation domains that eliminate the need for traversal order. FAME progressively shrinks these domains and leverages LiRPA-based bounds to discard irrelevant features, ultimately converging to a formal 摘要 minimal explanation. To assess explanation quality, we introduce a procedure that measures the worst-case distance between an 摘要 minimal explanation and a true minimal explanation. This procedure combines 对抗 attacks with an optional VERIX+ refinement step. We 基准 FAME against VERIX+ and demonstra...

**Original Abstract**:
> arXiv:2603.10661v1 Announce Type: new 
Abstract: We propose FAME (Formal Abstract Minimal Explanations), a new class of abductive explanations grounded in abstract interpretation. FAME is the first method to scale to large neural networks while reducing explanation size. Our main contribution is the design of dedicated perturbation domains that eliminate the need for traversal order. FAME progressively shrinks these domains and leverages LiRPA-based bounds to discard irrelevant features, ultimately converging to a formal abstract minimal explanation. To assess explanation quality, we introduce a procedure that measures the worst-case distance between an abstract minimal explanation and a true minimal explanation. This procedure combines adversarial attacks with an optional VERIX+ refinemen...

---

## 255. Emulating Clinician Cognition via Self-Evolving 深度 Clinical Research

**原标题**: Emulating Clinician Cognition via Self-Evolving Deep Clinical Research

**作者**: Ruiyang Ren, Yuhao Wang, Yunsen Liang, Lan Luo, Jing Liu, Haifeng Wang, Cong Feng, Yinan Zhang, Chunyan Miao, Ji-Rong Wen, Wayne Xin Zhao
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10677v1

**中文摘要**:
> arXiv:2603.10677v1 Announce Type: new 
摘要: Clinical diagnosis is a complex cognitive process, grounded in 动态 cue acquisition and continuous expertise accumulation. Yet most current artificial intelligence (AI) systems are misaligned with this reality, treating diagnosis as single-pass retrospective prediction while lacking auditable mechanisms for governed improvement. We developed DxEvolve, a self-evolving diagnostic 智能体 that bridges these gaps through an interactive 深度 clinical research workflow. The 框架 autonomously requisitions examinations and continually externalizes clinical experience from increasing encounter exposure as diagnostic cognition primitives. On the MIMIC-CDM 基准, DxEvolve improved diagnostic accuracy by 11.2% on average over backbone models and reached 90.4% on a reader-...

**Original Abstract**:
> arXiv:2603.10677v1 Announce Type: new 
Abstract: Clinical diagnosis is a complex cognitive process, grounded in dynamic cue acquisition and continuous expertise accumulation. Yet most current artificial intelligence (AI) systems are misaligned with this reality, treating diagnosis as single-pass retrospective prediction while lacking auditable mechanisms for governed improvement. We developed DxEvolve, a self-evolving diagnostic agent that bridges these gaps through an interactive deep clinical research workflow. The framework autonomously requisitions examinations and continually externalizes clinical experience from increasing encounter exposure as diagnostic cognition primitives. On the MIMIC-CDM benchmark, DxEvolve improved diagnostic accuracy by 11.2% on average over backbone models a...

---

## 256. Nurture-First 智能体 Development: Building Domain-Expert AI Agents Through Conversational Knowledge Crystallization

**原标题**: Nurture-First Agent Development: Building Domain-Expert AI Agents Through Conversational Knowledge Crystallization

**作者**: Linghao Zhang
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10808v1

**中文摘要**:
> arXiv:2603.10808v1 Announce Type: new 
摘要: The emergence of large language 模型 (大语言模型)-based 智能体 frameworks has shifted the primary challenge in building domain-expert AI agents from raw capability to effective encoding of domain expertise. Two dominant paradigms -- 代码-first development, which embeds expertise in deterministic pipelines, and prompt-first development, which captures expertise in 静态 系统 prompts -- both treat 智能体 construction as a discrete engineering phase preceding 部署. We argue that this sequential assumption creates a fundamental mismatch with the nature of domain expertise, which is substantially tacit, deeply personal, and continuously evolving. We propose Nurture-First Development (NFD), a paradigm in which agents are initialized with minimal scaffolding and progressively...

**Original Abstract**:
> arXiv:2603.10808v1 Announce Type: new 
Abstract: The emergence of large language model (LLM)-based agent frameworks has shifted the primary challenge in building domain-expert AI agents from raw capability to effective encoding of domain expertise. Two dominant paradigms -- code-first development, which embeds expertise in deterministic pipelines, and prompt-first development, which captures expertise in static system prompts -- both treat agent construction as a discrete engineering phase preceding deployment. We argue that this sequential assumption creates a fundamental mismatch with the nature of domain expertise, which is substantially tacit, deeply personal, and continuously evolving. We propose Nurture-First Development (NFD), a paradigm in which agents are initialized with minimal ...

---

## 257. A Hybrid Knowledge-Grounded 框架 for Safety and Traceability in Prescription Verification

**原标题**: A Hybrid Knowledge-Grounded Framework for Safety and Traceability in Prescription Verification

**作者**: Yichi Zhu, Kan Ling, Xu Liu, Hengrun Zhang, Huiqun Yu, Guisheng Fan
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10891v1

**中文摘要**:
> arXiv:2603.10891v1 Announce Type: new 
摘要: Medication errors pose a significant threat to patient safety, making pharmacist verification (PV) a critical, yet heavily burdened, final safeguard. The direct application of Large Language Models (LLMs) to this zero-tolerance domain is untenable due to their inherent factual unreliability, lack of traceability, and weakness in complex 推理. To address these challenges, we introduce PharmGraph-Auditor, a novel 系统 designed for safe and evidence-grounded prescription auditing. The core of our 系统 is a 可信 Hybrid Pharmaceutical Knowledge Base (HPKB), implemented under the Virtual 知识图谱 (VKG) paradigm. This 架构 strategically unifies a relational component for set constraint satisfaction and a graph component for topological 推理 via a rigorous mapping layer....

**Original Abstract**:
> arXiv:2603.10891v1 Announce Type: new 
Abstract: Medication errors pose a significant threat to patient safety, making pharmacist verification (PV) a critical, yet heavily burdened, final safeguard. The direct application of Large Language Models (LLMs) to this zero-tolerance domain is untenable due to their inherent factual unreliability, lack of traceability, and weakness in complex reasoning. To address these challenges, we introduce PharmGraph-Auditor, a novel system designed for safe and evidence-grounded prescription auditing. The core of our system is a trustworthy Hybrid Pharmaceutical Knowledge Base (HPKB), implemented under the Virtual Knowledge Graph (VKG) paradigm. This architecture strategically unifies a relational component for set constraint satisfaction and a graph compone...

---

## 258. Decoupling 推理 and Confidence: Resurrecting Calibration in 强化 学习 from Verifiable Rewards

**原标题**: Decoupling Reasoning and Confidence: Resurrecting Calibration in Reinforcement Learning from Verifiable Rewards

**作者**: Zhengzhao Ma, Xueru Wen, Boxi Cao, Yaojie Lu, Hongyu Lin, Jinglin Yang, Min He, Xianpei Han, Le Sun
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.09117v1

**中文摘要**:
> arXiv:2603.09117v1 Announce Type: cross 
摘要: 强化 学习 from Verifiable Rewards (RLVR) significantly enhances large language models (LLMs) 推理 but severely suffers from calibration degeneration, where models become excessively over-confident in incorrect answers. Previous studies devote to directly incorporating calibration objective into existing 优化 目标. However, our theoretical analysis demonstrates that there exists a fundamental 梯度 conflict between the 优化 for maximizing 策略 accuracy and minimizing calibration error. Building on this insight, we propose DCPO, a simple yet effective 框架 that systematically decouples 推理 and calibration objectives. Extensive experiments demonstrate that our DCPO not only preserves accuracy on par with GRPO but also achieves the best calibration 性能 and substantially...

**Original Abstract**:
> arXiv:2603.09117v1 Announce Type: cross 
Abstract: Reinforcement Learning from Verifiable Rewards (RLVR) significantly enhances large language models (LLMs) reasoning but severely suffers from calibration degeneration, where models become excessively over-confident in incorrect answers. Previous studies devote to directly incorporating calibration objective into existing optimization target. However, our theoretical analysis demonstrates that there exists a fundamental gradient conflict between the optimization for maximizing policy accuracy and minimizing calibration error. Building on this insight, we propose DCPO, a simple yet effective framework that systematically decouples reasoning and calibration objectives. Extensive experiments demonstrate that our DCPO not only preserves accurac...

---

## 259. One 模型, Many Skills: Parameter-高效 Fine-Tuning for Multitask 代码 Analysis

**原标题**: One Model, Many Skills: Parameter-Efficient Fine-Tuning for Multitask Code Analysis

**作者**: Amal Akli, Maxime Cordy, Mike Papadakis, Yves Le Traon
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.09978v1

**中文摘要**:
> arXiv:2603.09978v1 Announce Type: cross 
摘要: Large language models have recently surpassed specialized systems on 代码 生成, yet their effectiveness on other 代码-analysis tasks remains less clear. At the same time, 多任务 学习 offers a way to unify diverse objectives within a single 模型, but fully fine-tuning LLMs across tasks is computationally prohibitive. Parameter-高效 fine-tuning mitigates this cost by updating only a small fraction of weights. Although PEFT has proven effective in single-task settings, its potential for 多任务 学习 has not yet been systematically explored. We present the first comprehensive 评估 of 多任务 PEFT for 代码 analysis, comparing several methods across diverse tasks and 模型 architectures. Our experiments show that a single PEFT module shared across tasks can match, and in some cases ...

**Original Abstract**:
> arXiv:2603.09978v1 Announce Type: cross 
Abstract: Large language models have recently surpassed specialized systems on code generation, yet their effectiveness on other code-analysis tasks remains less clear. At the same time, multi-task learning offers a way to unify diverse objectives within a single model, but fully fine-tuning LLMs across tasks is computationally prohibitive. Parameter-efficient fine-tuning mitigates this cost by updating only a small fraction of weights. Although PEFT has proven effective in single-task settings, its potential for multi-task learning has not yet been systematically explored. We present the first comprehensive evaluation of multi-task PEFT for code analysis, comparing several methods across diverse tasks and model architectures. Our experiments show t...

---

## 260. 可解释 大语言模型 Unlearning Through 推理

**原标题**: Explainable LLM Unlearning Through Reasoning

**作者**: Junfeng Liao, Qizhou Wang, Shanshan Ye, Xin Yu, Ling Chen, Zhen Fang
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.09980v1

**中文摘要**:
> arXiv:2603.09980v1 Announce Type: cross 
摘要: 大语言模型 unlearning is essential for mitigating safety, copyright, and 隐私 concerns in pre-trained large language models (LLMs). Compared to preference alignment, it offers a more explicit way by removing undesirable knowledge characterized by specific unlearning datasets. In previous works, 梯度 上升 (GA) and its variants have shown promise for implementing unlearning, yet their untargeted nature results in unintended degradation of general capabilities, incomplete removal of knowledge, and the 生成 of incoherent responses, among many others. We argue that these issues stem from the absence of explicit guidance on what and how models should unlearn. To fill this gap, we introduce a novel unlearning 目标, 推理-based unlearning 目标, which satisfies both the spe...

**Original Abstract**:
> arXiv:2603.09980v1 Announce Type: cross 
Abstract: LLM unlearning is essential for mitigating safety, copyright, and privacy concerns in pre-trained large language models (LLMs). Compared to preference alignment, it offers a more explicit way by removing undesirable knowledge characterized by specific unlearning datasets. In previous works, gradient ascent (GA) and its variants have shown promise for implementing unlearning, yet their untargeted nature results in unintended degradation of general capabilities, incomplete removal of knowledge, and the generation of incoherent responses, among many others. We argue that these issues stem from the absence of explicit guidance on what and how models should unlearn. To fill this gap, we introduce a novel unlearning target, reasoning-based unlea...

---

## 261. AraModernBERT: Transtokenized Initialization and Long-Context Encoder Modeling for Arabic

**原标题**: AraModernBERT: Transtokenized Initialization and Long-Context Encoder Modeling for Arabic

**作者**: Omar Elshehy, Omer Nacar, Abdelbasset Djamai, Muhammed Ragab, Khloud Al Jallad, Mona Abdelazim
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.09982v1

**中文摘要**:
> arXiv:2603.09982v1 Announce Type: cross 
摘要: Encoder-only Transformer models remain widely used for 判别式 自然语言处理 tasks, yet recent architectural advances have largely focused on English. In this work, we present AraModernBERT, an adaptation of the ModernBERT encoder 架构 to Arabic, and study the impact of transtokenized 嵌入 initialization and native long-context modeling up to 8,192 tokens. We show that transtokenization is essential for Arabic language modeling, yielding dramatic improvements in masked language modeling 性能 compared to non-transtokenized initialization. We further demonstrate that AraModernBERT supports stable and effective long-context modeling, achieving improved intrinsic language modeling 性能 at extended sequence lengths. Downstream evaluations on Arabic natural language und...

**Original Abstract**:
> arXiv:2603.09982v1 Announce Type: cross 
Abstract: Encoder-only transformer models remain widely used for discriminative NLP tasks, yet recent architectural advances have largely focused on English. In this work, we present AraModernBERT, an adaptation of the ModernBERT encoder architecture to Arabic, and study the impact of transtokenized embedding initialization and native long-context modeling up to 8,192 tokens. We show that transtokenization is essential for Arabic language modeling, yielding dramatic improvements in masked language modeling performance compared to non-transtokenized initialization. We further demonstrate that AraModernBERT supports stable and effective long-context modeling, achieving improved intrinsic language modeling performance at extended sequence lengths. Down...

---

## 262. MoE-SpAc: 高效 MoE 推理 Based on Speculative Activation Utility in Heterogeneous Edge Scenarios

**原标题**: MoE-SpAc: Efficient MoE Inference Based on Speculative Activation Utility in Heterogeneous Edge Scenarios

**作者**: Shuhuai Li, Jianghao Lin, Dongdong Ge, Yinyu Ye
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.09983v1

**中文摘要**:
> arXiv:2603.09983v1 Announce Type: cross 
摘要: Mixture-of-Experts (MoE) models enable 可扩展 性能 but face severe 内存 constraints on edge devices. Existing offloading strategies struggle with I/O bottlenecks due to the 动态, low-information nature of autoregressive expert activation. In this 论文, we propose to repurpose Speculative Decoding (SD) not merely as a compute加速器, but as an informative lookahead sensor for 内存 management, supported by our theoretical and empirical analyses. Hence, we introduce MoE-SpAc, an MoE 推理 框架 that integrates a Speculative Utility Estimator to track expert demand, a Heterogeneous Workload Balancer to dynamically partition computation via 在线 integer 优化, and an Asynchronous Execution Engine to unify the prefetching and eviction in the same utility space. Extensive experim...

**Original Abstract**:
> arXiv:2603.09983v1 Announce Type: cross 
Abstract: Mixture-of-Experts (MoE) models enable scalable performance but face severe memory constraints on edge devices. Existing offloading strategies struggle with I/O bottlenecks due to the dynamic, low-information nature of autoregressive expert activation. In this paper, we propose to repurpose Speculative Decoding (SD) not merely as a compute accelerator, but as an informative lookahead sensor for memory management, supported by our theoretical and empirical analyses. Hence, we introduce MoE-SpAc, an MoE inference framework that integrates a Speculative Utility Estimator to track expert demand, a Heterogeneous Workload Balancer to dynamically partition computation via online integer optimization, and an Asynchronous Execution Engine to unify ...

---

## 263. The Dunning-Kruger Effect in Large Language Models: An Empirical Study of Confidence Calibration

**原标题**: The Dunning-Kruger Effect in Large Language Models: An Empirical Study of Confidence Calibration

**作者**: Sudipta Ghosh, Mrityunjoy Panday
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.09985v1

**中文摘要**:
> arXiv:2603.09985v1 Announce Type: cross 
摘要: Large language models (LLMs) have demonstrated remarkable capabilities across diverse tasks, yet their ability to accurately assess their own confidence remains poorly understood. We present an empirical study investigating whether LLMs exhibit patterns reminiscent of the Dunning-Kruger effect -- a cognitive 偏见 where individuals with limited competence tend to overestimate their abilities. We evaluate four 状态-of-the-art models (Claude Haiku 4.5, Gemini 2.5 Pro, Gemini 2.5 Flash, and Kimi K2) across four 基准 datasets totaling 24,000 experimental trials. Our results reveal striking calibration differences: Kimi K2 exhibits severe overconfidence with an Expected Calibration Error (ECE) of 0.726 despite only 23.3% accuracy, while Claude Haiku 4.5 ach...

**Original Abstract**:
> arXiv:2603.09985v1 Announce Type: cross 
Abstract: Large language models (LLMs) have demonstrated remarkable capabilities across diverse tasks, yet their ability to accurately assess their own confidence remains poorly understood. We present an empirical study investigating whether LLMs exhibit patterns reminiscent of the Dunning-Kruger effect -- a cognitive bias where individuals with limited competence tend to overestimate their abilities. We evaluate four state-of-the-art models (Claude Haiku 4.5, Gemini 2.5 Pro, Gemini 2.5 Flash, and Kimi K2) across four benchmark datasets totaling 24,000 experimental trials. Our results reveal striking calibration differences: Kimi K2 exhibits severe overconfidence with an Expected Calibration Error (ECE) of 0.726 despite only 23.3% accuracy, while Cl...

---

## 264. Quantifying Hallucinations in Language Language Models on Medical Textbooks

**原标题**: Quantifying Hallucinations in Language Language Models on Medical Textbooks

**作者**: Brandon C. Colelough, Davis Bartels, Dina Demner-Fushman
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.09986v1

**中文摘要**:
> arXiv:2603.09986v1 Announce Type: cross 
摘要: Hallucinations, the tendency for large language models to provide responses with factually incorrect and unsupported claims, is a serious problem within natural language processing for which we do not yet have an effective solution to mitigate against. Existing benchmarks for medical 问答 rarely evaluate this behavior against a fixed evidence source. We ask how often hallucinations occur on textbook-grounded 问答 and how responses to medical 问答 prompts vary across models. We conduct two experiments: the first 实验 to determine the prevalence of hallucinations for a prominent 开源 large language 模型 (LLaMA-70B-Instruct) in medical 问答 given novel prompts, and the second 实验 to determine the prevalence of hallucinations and clinician preference to 模型 respons...

**Original Abstract**:
> arXiv:2603.09986v1 Announce Type: cross 
Abstract: Hallucinations, the tendency for large language models to provide responses with factually incorrect and unsupported claims, is a serious problem within natural language processing for which we do not yet have an effective solution to mitigate against. Existing benchmarks for medical QA rarely evaluate this behavior against a fixed evidence source. We ask how often hallucinations occur on textbook-grounded QA and how responses to medical QA prompts vary across models. We conduct two experiments: the first experiment to determine the prevalence of hallucinations for a prominent open source large language model (LLaMA-70B-Instruct) in medical QA given novel prompts, and the second experiment to determine the prevalence of hallucinations and ...

---

## 265. Evolving Demonstration 优化 for Chain-of-Thought 特征 Transformation

**原标题**: Evolving Demonstration Optimization for Chain-of-Thought Feature Transformation

**作者**: Xinyuan Wang, Kunpeng Liu, Arun Vignesh Malarkkan, Yanjie Fu
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.09987v1

**中文摘要**:
> arXiv:2603.09987v1 Announce Type: cross 
摘要: 特征 Transformation (FT) is a core data-centric AI task that improves 特征 space quality to advance downstream predictive 性能. However, discovering effective transformations remains challenging due to the large space of 特征-operator combinations. Existing solutions rely on discrete 搜索 or 隐变量 生成, but they are frequently limited by sample inefficiency, invalid candidates, and redundant generations with limited coverage. Large Language Models (LLMs) offer strong priors for producing valid transformations, but current 大语言模型-based FT methods typically rely on 静态 demonstrations, resulting in limited diversity, redundant outputs, and weak alignment with downstream objectives. We propose a 框架 that optimizes context data for 大语言模型-driven FT by evolving 轨迹-leve...

**Original Abstract**:
> arXiv:2603.09987v1 Announce Type: cross 
Abstract: Feature Transformation (FT) is a core data-centric AI task that improves feature space quality to advance downstream predictive performance. However, discovering effective transformations remains challenging due to the large space of feature-operator combinations. Existing solutions rely on discrete search or latent generation, but they are frequently limited by sample inefficiency, invalid candidates, and redundant generations with limited coverage. Large Language Models (LLMs) offer strong priors for producing valid transformations, but current LLM-based FT methods typically rely on static demonstrations, resulting in limited diversity, redundant outputs, and weak alignment with downstream objectives. We propose a framework that optimize...

---

## 266. Causally Grounded Mechanistic Interpretability for LLMs with Faithful Natural-Language Explanations

**原标题**: Causally Grounded Mechanistic Interpretability for LLMs with Faithful Natural-Language Explanations

**作者**: Ajay Pravin Mahale
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.09988v1

**中文摘要**:
> arXiv:2603.09988v1 Announce Type: cross 
摘要: Mechanistic interpretability identifies internal circuits responsible for 模型 behaviors, yet translating these findings into human-understandable explanations remains an open problem. We present a pipeline that bridges circuit-level analysis and natural language explanations by (i) identifying causally important 注意力 heads via activation patching, (ii) generating explanations using both template-based and 大语言模型-based methods, and (iii) evaluating faithfulness using ERASER-style metrics adapted for circuit-level attribution. We evaluate on the Indirect Object Identification (IOI) task in GPT-2 Small (124M parameters), identifying six 注意力 heads accounting for 61.4% of the logit difference. Our circuit-based explanations achieve 100% sufficiency but ...

**Original Abstract**:
> arXiv:2603.09988v1 Announce Type: cross 
Abstract: Mechanistic interpretability identifies internal circuits responsible for model behaviors, yet translating these findings into human-understandable explanations remains an open problem. We present a pipeline that bridges circuit-level analysis and natural language explanations by (i) identifying causally important attention heads via activation patching, (ii) generating explanations using both template-based and LLM-based methods, and (iii) evaluating faithfulness using ERASER-style metrics adapted for circuit-level attribution. We evaluate on the Indirect Object Identification (IOI) task in GPT-2 Small (124M parameters), identifying six attention heads accounting for 61.4% of the logit difference. Our circuit-based explanations achieve 10...

---

## 267. A Two-Stage 架构 for NDA Analysis: 大语言模型-based 分割 and Transformer-based Clause 分类

**原标题**: A Two-Stage Architecture for NDA Analysis: LLM-based Segmentation and Transformer-based Clause Classification

**作者**: Ana Begnini, Matheus Vicente, Leonardo Souza
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.09990v1

**中文摘要**:
> arXiv:2603.09990v1 Announce Type: cross 
摘要: In business-to-business relations, it is common to establish NonDisclosure Agreements (NDAs). However, these documents exhibit significant variation in format, structure, and writing style, making manual analysis slow and error-prone. We propose an 架构 based on LLMs to automate the 分割 and clauses 分类 within these contracts. We employed two models: LLaMA-3.1-8B-Instruct for NDA 分割 (clause extraction) and a fine-tuned Legal-Roberta-Large for clause 分类. In the 分割 task, we achieved a ROUGE F1 of 0.95 +/- 0.0036; for 分类, we obtained a weighted F1 of 0.85, demonstrating the feasibility and precision of the 方案.

**Original Abstract**:
> arXiv:2603.09990v1 Announce Type: cross 
Abstract: In business-to-business relations, it is common to establish NonDisclosure Agreements (NDAs). However, these documents exhibit significant variation in format, structure, and writing style, making manual analysis slow and error-prone. We propose an architecture based on LLMs to automate the segmentation and clauses classification within these contracts. We employed two models: LLaMA-3.1-8B-Instruct for NDA segmentation (clause extraction) and a fine-tuned Legal-Roberta-Large for clause classification. In the segmentation task, we achieved a ROUGE F1 of 0.95 +/- 0.0036; for classification, we obtained a weighted F1 of 0.85, demonstrating the feasibility and precision of the approach.

---

## 268. TAMUSA-Chat: A Domain-Adapted Large Language 模型 Conversational 系统 for Research and Responsible 部署

**原标题**: TAMUSA-Chat: A Domain-Adapted Large Language Model Conversational System for Research and Responsible Deployment

**作者**: Izzat Alsmadi, Anas Alsobeh
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.09992v1

**中文摘要**:
> arXiv:2603.09992v1 Announce Type: cross 
摘要: This 论文 presents TAMUSA-Chat, a research-oriented 框架 for building domain-adapted large language 模型 conversational systems. The work addresses critical challenges in adapting general-purpose foundation models to institutional contexts through 有监督 fine-tuning, 检索-augmented 生成, and systematic 评估 methodologies. We describe the complete 架构 encompassing data acquisition from institutional sources, preprocessing pipelines, 嵌入 construction, 模型 训练 workflows, and 部署 strategies. The 系统 integrates modular components enabling reproducible experimentation with 训练 configurations, hyper-parameters, and 评估 protocols. Our 实现 demonstrates how academic institutions can develop contextually grounded conversational agents while maintaining transparency, governance co...

**Original Abstract**:
> arXiv:2603.09992v1 Announce Type: cross 
Abstract: This paper presents TAMUSA-Chat, a research-oriented framework for building domain-adapted large language model conversational systems. The work addresses critical challenges in adapting general-purpose foundation models to institutional contexts through supervised fine-tuning, retrieval-augmented generation, and systematic evaluation methodologies. We describe the complete architecture encompassing data acquisition from institutional sources, preprocessing pipelines, embedding construction, model training workflows, and deployment strategies. The system integrates modular components enabling reproducible experimentation with training configurations, hyper-parameters, and evaluation protocols. Our implementation demonstrates how academic i...

---

## 269. CEI: A 基准 for Evaluating Pragmatic 推理 in Language Models

**原标题**: CEI: A Benchmark for Evaluating Pragmatic Reasoning in Language Models

**作者**: Jon Chun, Hannah Sussman, Adrian Mangine, Murathan Kocaman, Kirill Sidorko, Abhigya Koirala, Andre McCloud, Gwen Eisenbeis, Wisdom Akanwe, Moustapha Gassama, Eliezer Gonzalez Chirinos, Anne-Duncan Enright, Peter Dunson, Tiffanie Ng, Anna von Rosenstiel, Godwin Idowu
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.09993v1

**中文摘要**:
> arXiv:2603.09993v1 Announce Type: cross 
摘要: Pragmatic 推理, inferring intended meaning beyond literal semantics, underpins everyday communication yet remains difficult for large language models. We present the Contextual Emotional 推理 (CEI) 基准: 300 human-validated scenarios for evaluating how well LLMs disambiguate pragmatically complex utterances. Each scenario pairs a situational context and 说话人-listener roles (with explicit power relations) against an ambiguous utterance. The 数据集 covers five pragmatic subtypes (sarcasm/irony, mixed signals, strategic politeness, passive aggression, deflection/misdirection) drawn from workplace, family, social, and service settings, with three power configurations (peer, higher-to-lower, lower-to-higher). Three trained annotators independently labeled ever...

**Original Abstract**:
> arXiv:2603.09993v1 Announce Type: cross 
Abstract: Pragmatic reasoning, inferring intended meaning beyond literal semantics, underpins everyday communication yet remains difficult for large language models. We present the Contextual Emotional Inference (CEI) Benchmark: 300 human-validated scenarios for evaluating how well LLMs disambiguate pragmatically complex utterances. Each scenario pairs a situational context and speaker-listener roles (with explicit power relations) against an ambiguous utterance. The dataset covers five pragmatic subtypes (sarcasm/irony, mixed signals, strategic politeness, passive aggression, deflection/misdirection) drawn from workplace, family, social, and service settings, with three power configurations (peer, higher-to-lower, lower-to-higher). Three trained an...

---

## 270. Context Over Compute Human-in-the-Loop Outperforms Iterative Chain-of-Thought Prompting in Interview Answer Quality

**原标题**: Context Over Compute Human-in-the-Loop Outperforms Iterative Chain-of-Thought Prompting in Interview Answer Quality

**作者**: Kewen Zhu, Zixi Liu, Yanjing Li
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.09995v1

**中文摘要**:
> arXiv:2603.09995v1 Announce Type: cross 
摘要: Behavioral interview 评估 using large language models presents unique challenges that require structured assessment, realistic interviewer behavior simulation, and pedagogical 价值 for candidate 训练. We investigate chain of thought prompting for interview answer 评估 and improvement through two controlled experiments with 50 behavioral interview question and answer pairs. Our contributions are threefold. First, we provide a quantitative comparison between human in the loop and automated chain of thought improvement. Using a within subject paired design with n equals 50, both approaches show positive rating improvements. The human in the loop 方案 provides significant 训练 benefits. Confidence improves from 3.16 to 4.16 (p less than 0.001) and authenticity ...

**Original Abstract**:
> arXiv:2603.09995v1 Announce Type: cross 
Abstract: Behavioral interview evaluation using large language models presents unique challenges that require structured assessment, realistic interviewer behavior simulation, and pedagogical value for candidate training. We investigate chain of thought prompting for interview answer evaluation and improvement through two controlled experiments with 50 behavioral interview question and answer pairs. Our contributions are threefold. First, we provide a quantitative comparison between human in the loop and automated chain of thought improvement. Using a within subject paired design with n equals 50, both approaches show positive rating improvements. The human in the loop approach provides significant training benefits. Confidence improves from 3.16 to...

---

## 271. There Are No Silly Questions: 评估 of 离线 大语言模型 Capabilities from a Turkish Perspective

**原标题**: There Are No Silly Questions: Evaluation of Offline LLM Capabilities from a Turkish Perspective

**作者**: Edibe Yilmaz, Kahraman Kostas
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.09996v1

**中文摘要**:
> arXiv:2603.09996v1 Announce Type: cross 
摘要: The integration of large language models (LLMs) into educational processes introduces significant constraints regarding data 隐私 and reliability, particularly in pedagogically vulnerable contexts such as Turkish heritage language education. This study aims to systematically evaluate the 鲁棒性 and pedagogical safety of locally deployable 离线 LLMs within the context of Turkish heritage language education. To this end, a Turkish Anomaly Suite (TAS) consisting of 10 original edge-case scenarios was developed to assess the models' capacities for epistemic resistance, logical consistency, and pedagogical safety. Experiments conducted on 14 different models ranging from 270M to 32B parameters reveal that anomaly resistance is not solely dependent on 模型 sca...

**Original Abstract**:
> arXiv:2603.09996v1 Announce Type: cross 
Abstract: The integration of large language models (LLMs) into educational processes introduces significant constraints regarding data privacy and reliability, particularly in pedagogically vulnerable contexts such as Turkish heritage language education. This study aims to systematically evaluate the robustness and pedagogical safety of locally deployable offline LLMs within the context of Turkish heritage language education. To this end, a Turkish Anomaly Suite (TAS) consisting of 10 original edge-case scenarios was developed to assess the models' capacities for epistemic resistance, logical consistency, and pedagogical safety. Experiments conducted on 14 different models ranging from 270M to 32B parameters reveal that anomaly resistance is not sol...

---

## 272. Empathy Is Not What Changed: Clinical Assessment of Psychological Safety Across GPT 模型 Generations

**原标题**: Empathy Is Not What Changed: Clinical Assessment of Psychological Safety Across GPT Model Generations

**作者**: Michael Keeman, Anastasia Keeman
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.09997v1

**中文摘要**:
> arXiv:2603.09997v1 Announce Type: cross 
摘要: When OpenAI deprecated GPT-4o in early 2026, thousands of users protested under #keep4o, claiming newer models had "lost their empathy." No 发布日期 study has tested this claim. We conducted the first clinical measurement, evaluating three OpenAI 模型 generations (GPT-4o, o4-mini, GPT-5-mini) across 14 emotionally challenging conversational scenarios in mental health and AI companion domains, producing 2,100 scored AI responses assessed on six psychological safety dimensions using clinically-grounded rubrics.
  Empathy scores are statistically indistinguishable across all three models (Kruskal-Wallis H=4.33, p=0.115). What changed is the safety posture: crisis 检测 improved monotonically from GPT-4o to GPT-5-mini (H=13.88, p=0.001), while advice safety ...

**Original Abstract**:
> arXiv:2603.09997v1 Announce Type: cross 
Abstract: When OpenAI deprecated GPT-4o in early 2026, thousands of users protested under #keep4o, claiming newer models had "lost their empathy." No published study has tested this claim. We conducted the first clinical measurement, evaluating three OpenAI model generations (GPT-4o, o4-mini, GPT-5-mini) across 14 emotionally challenging conversational scenarios in mental health and AI companion domains, producing 2,100 scored AI responses assessed on six psychological safety dimensions using clinically-grounded rubrics.
  Empathy scores are statistically indistinguishable across all three models (Kruskal-Wallis H=4.33, p=0.115). What changed is the safety posture: crisis detection improved monotonically from GPT-4o to GPT-5-mini (H=13.88, p=0.001),...

---

## 273. Automated 评估 of LLMs for effective machine translation of Mandarin Chinese to English

**原标题**: Automated evaluation of LLMs for effective machine translation of Mandarin Chinese to English

**作者**: Yue Zhang, Rodney Beard, John Hawkins, Rohitash Chandra
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.09998v1

**中文摘要**:
> arXiv:2603.09998v1 Announce Type: cross 
摘要: Although Large Language Models (LLMs) have exceptional 性能 in machine translation, only a limited systematic assessment of translation quality has been done. The challenge lies in automated frameworks, as human-expert-based evaluations can be time-consuming, given the fast-evolving LLMs and the need for a diverse set of texts to ensure fair assessments of translation quality. In this 论文, we utilise an automated machine 学习 框架 featuring semantic and sentiment analysis to assess Mandarin Chinese to English translation using Google Translate and LLMs, including GPT-4, GPT-4o, and DeepSeek. We compare original and translated texts in various classes of high-profile Chinese texts, which include novel texts that span modern and classical literature, as ...

**Original Abstract**:
> arXiv:2603.09998v1 Announce Type: cross 
Abstract: Although Large Language Models (LLMs) have exceptional performance in machine translation, only a limited systematic assessment of translation quality has been done. The challenge lies in automated frameworks, as human-expert-based evaluations can be time-consuming, given the fast-evolving LLMs and the need for a diverse set of texts to ensure fair assessments of translation quality. In this paper, we utilise an automated machine learning framework featuring semantic and sentiment analysis to assess Mandarin Chinese to English translation using Google Translate and LLMs, including GPT-4, GPT-4o, and DeepSeek. We compare original and translated texts in various classes of high-profile Chinese texts, which include novel texts that span moder...

---

## 274. A 检索-Augmented Language Assistant for Unmanned Aircraft Safety Assessment and Regulatory Compliance

**原标题**: A Retrieval-Augmented Language Assistant for Unmanned Aircraft Safety Assessment and Regulatory Compliance

**作者**: Gabriele Immordino, Andrea Vaiuso, Marcello Righi
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.09999v1

**中文摘要**:
> arXiv:2603.09999v1 Announce Type: cross 
摘要: This 论文 presents the design and validation of a 检索-based assistant that supports safety assessment, certification activities, and regulatory compliance for unmanned aircraft systems. The work is motivated by the growing complexity of drone operations and the increasing effort required by applicants and aviation authorities to apply established assessment frameworks, including the Specific Operations Risk Assessment and the Pre-defined Risk Assessment, in a consistent and 高效 manner. The proposed 方案 uses a controlled text-based 架构 that relies exclusively on authoritative regulatory sources. To enable traceable and auditable outputs, the assistant grounds each response in retrieved passages and enforces citation-driven 生成. 系统-level controls address...

**Original Abstract**:
> arXiv:2603.09999v1 Announce Type: cross 
Abstract: This paper presents the design and validation of a retrieval-based assistant that supports safety assessment, certification activities, and regulatory compliance for unmanned aircraft systems. The work is motivated by the growing complexity of drone operations and the increasing effort required by applicants and aviation authorities to apply established assessment frameworks, including the Specific Operations Risk Assessment and the Pre-defined Risk Assessment, in a consistent and efficient manner. The proposed approach uses a controlled text-based architecture that relies exclusively on authoritative regulatory sources. To enable traceable and auditable outputs, the assistant grounds each response in retrieved passages and enforces citati...

---

## 275. Leveraging Wikidata for Geographically Informed Sociocultural 偏见 数据集 Creation: Application to Latin America

**原标题**: Leveraging Wikidata for Geographically Informed Sociocultural Bias Dataset Creation: Application to Latin America

**作者**: Yannis Karmim (ALMAnaCH), Renato Pino (UCHILE), Hernan Contreras (UCHILE), Hernan Lira (CENIA), Sebastian Cifuentes (CENIA), Simon Escoffier (PUC), Luis Mart\'i (UP4, ALPAGE), Djam\'e Seddah (UP4, ALPAGE), Valentin Barri\`ere (UCHILE, CENIA)
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10001v1

**中文摘要**:
> arXiv:2603.10001v1 Announce Type: cross 
摘要: Large Language Models (LLMs) exhibit inequalities with respect to various cultural contexts. Most prominent open-weights models are trained on Global North data and show prejudicial behavior towards other cultures. Moreover, there is a notable lack of resources to detect biases in non-English languages, especially from Latin America (Latam), a continent containing various cultures, even though they share a common cultural ground. We propose to leverage the content of Wikipedia, the structure of the Wikidata 知识图谱, and expert knowledge from social science in order to create a 数据集 of question/answer (Q/As) pairs, based on the different popular and social cultures of various Latin American countries. We create the LatamQA database of over 26k questi...

**Original Abstract**:
> arXiv:2603.10001v1 Announce Type: cross 
Abstract: Large Language Models (LLMs) exhibit inequalities with respect to various cultural contexts. Most prominent open-weights models are trained on Global North data and show prejudicial behavior towards other cultures. Moreover, there is a notable lack of resources to detect biases in non-English languages, especially from Latin America (Latam), a continent containing various cultures, even though they share a common cultural ground. We propose to leverage the content of Wikipedia, the structure of the Wikidata knowledge graph, and expert knowledge from social science in order to create a dataset of question/answer (Q/As) pairs, based on the different popular and social cultures of various Latin American countries. We create the LatamQA databa...

---

## 276. SpreadsheetArena: Decomposing Preference in 大语言模型 生成 of Spreadsheet Workbooks

**原标题**: SpreadsheetArena: Decomposing Preference in LLM Generation of Spreadsheet Workbooks

**作者**: Srivatsa Kundurthy, Clara Na, Michael Handley, Zach Kirshner, Chen Bo Calvin Zhang, Manasi Sharma, Emma Strubell, John Ling
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10002v1

**中文摘要**:
> arXiv:2603.10002v1 Announce Type: cross 
摘要: Large language models (LLMs) are increasingly tasked with producing and manipulating structured artifacts. We consider the task of end-to-end spreadsheet 生成, where language models are prompted to produce spreadsheet artifacts to satisfy users' explicit and implicit constraints, specified in natural language. We introduce SpreadsheetArena, a platform for evaluating models' 性能 on the task via blind pairwise evaluations of 大语言模型-generated spreadsheet workbooks. As with other complex, open-ended tasks, relevant 评估 criteria can vary substantially across use cases and prompts, often in ways that are difficult to formalize. Compared to general chat or text 生成 settings, spreadsheet 生成 presents unique challenges and opportunities: the task output structu...

**Original Abstract**:
> arXiv:2603.10002v1 Announce Type: cross 
Abstract: Large language models (LLMs) are increasingly tasked with producing and manipulating structured artifacts. We consider the task of end-to-end spreadsheet generation, where language models are prompted to produce spreadsheet artifacts to satisfy users' explicit and implicit constraints, specified in natural language. We introduce SpreadsheetArena, a platform for evaluating models' performance on the task via blind pairwise evaluations of LLM-generated spreadsheet workbooks. As with other complex, open-ended tasks, relevant evaluation criteria can vary substantially across use cases and prompts, often in ways that are difficult to formalize. Compared to general chat or text generation settings, spreadsheet generation presents unique challeng...

---

## 277. SENS-语音识别: Semantic 嵌入 injection in 神经-transducer for 流式 Automatic 语音 识别

**原标题**: SENS-ASR: Semantic Embedding injection in Neural-transducer for Streaming Automatic Speech Recognition

**作者**: Youness Dkhissi (LIUM), Valentin Vielzeuf (LIUM), Elys Allesiardo (LIUM), Anthony Larcher (LIUM)
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10005v1

**中文摘要**:
> arXiv:2603.10005v1 Announce Type: cross 
摘要: Many Automatic 语音 识别 (语音识别) applications require 流式 processing of the 音频 data. In 流式 mode, 语音识别 systems need to start transcribing the input stream before it is complete, i.e., the systems have to process a stream of inputs with a limited (or no) future context. Compared to 离线 mode, this reduction of the future context degrades the 性能 of 流式-语音识别 systems, especially while working with 低延迟 constraint. In this work, we present SENS-语音识别, an 方案 to enhance the transcription quality of 流式-语音识别 by reinforcing the acoustic information with semantic information. This semantic information is extracted from the available past frame-embeddings by a context module. This module is trained using knowledge distillation from a sentence 嵌入 Language 模型 fine-tuned ...

**Original Abstract**:
> arXiv:2603.10005v1 Announce Type: cross 
Abstract: Many Automatic Speech Recognition (ASR) applications require streaming processing of the audio data. In streaming mode, ASR systems need to start transcribing the input stream before it is complete, i.e., the systems have to process a stream of inputs with a limited (or no) future context. Compared to offline mode, this reduction of the future context degrades the performance of Streaming-ASR systems, especially while working with low-latency constraint. In this work, we present SENS-ASR, an approach to enhance the transcription quality of Streaming-ASR by reinforcing the acoustic information with semantic information. This semantic information is extracted from the available past frame-embeddings by a context module. This module is traine...

---

## 278. Personalized Group Relative 策略 优化 for Heterogenous Preference Alignment

**原标题**: Personalized Group Relative Policy Optimization for Heterogenous Preference Alignment

**作者**: Jialu Wang, Heinrich Peters, Asad A. Butt, Navid Hashemi, Alireza Hashemi, Pouya M. Ghari, Joseph Hoover, James Rae, Morteza Dehghani
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10009v1

**中文摘要**:
> arXiv:2603.10009v1 Announce Type: cross 
摘要: Despite their sophisticated general-purpose capabilities, Large Language Models (LLMs) often fail to align with diverse individual preferences because standard post-训练 methods, like 强化 学习 with Human Feedback (RLHF), optimize for a single, global objective. While Group Relative 策略 优化 (GRPO) is a widely adopted on-策略 强化 学习 框架, its group-based 归一化 implicitly assumes that all samples are exchangeable, inheriting this limitation in personalized settings. This assumption conflates distinct user 奖励 distributions and systematically biases 学习 toward dominant preferences while suppressing minority signals. To address this, we introduce Personalized GRPO (P-GRPO), a novel alignment 框架 that decouples 优势 estimation from immediate 批次 statistics. By normalizin...

**Original Abstract**:
> arXiv:2603.10009v1 Announce Type: cross 
Abstract: Despite their sophisticated general-purpose capabilities, Large Language Models (LLMs) often fail to align with diverse individual preferences because standard post-training methods, like Reinforcement Learning with Human Feedback (RLHF), optimize for a single, global objective. While Group Relative Policy Optimization (GRPO) is a widely adopted on-policy reinforcement learning framework, its group-based normalization implicitly assumes that all samples are exchangeable, inheriting this limitation in personalized settings. This assumption conflates distinct user reward distributions and systematically biases learning toward dominant preferences while suppressing minority signals. To address this, we introduce Personalized GRPO (P-GRPO), a ...

---

## 279. FERRET: 框架 for Expansion Reliant Red Teaming

**原标题**: FERRET: Framework for Expansion Reliant Red Teaming

**作者**: Ninareh Mehrabi, Vitor Albiero, Maya Pavlova, Joanna Bitton
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10010v1

**中文摘要**:
> arXiv:2603.10010v1 Announce Type: cross 
摘要: We introduce a multi-faceted automated red teaming 框架 in which the goal is to generate 多模态 对抗 conversations that would break a 目标 模型 and introduce various expansions that would 结果 in more effective and 高效 对抗 conversations. The introduced expansions include: 1. Horizontal expansion in which the goal is for the red team 模型 to self-improve and generate more effective conversation starters that would shape a conversation. 2. Vertical expansion in which the goal is to take these conversation starters that are discovered in the horizontal expansion phase and expand them into effective 多模态 conversations and 3. Meta expansion in which the goal is for the red team 模型 to discover more effective 多模态 attack strategies during the course of a conversation. We...

**Original Abstract**:
> arXiv:2603.10010v1 Announce Type: cross 
Abstract: We introduce a multi-faceted automated red teaming framework in which the goal is to generate multi-modal adversarial conversations that would break a target model and introduce various expansions that would result in more effective and efficient adversarial conversations. The introduced expansions include: 1. Horizontal expansion in which the goal is for the red team model to self-improve and generate more effective conversation starters that would shape a conversation. 2. Vertical expansion in which the goal is to take these conversation starters that are discovered in the horizontal expansion phase and expand them into effective multi-modal conversations and 3. Meta expansion in which the goal is for the red team model to discover more ...

---

## 280. Measuring and Eliminating Refusals in Military Large Language Models

**原标题**: Measuring and Eliminating Refusals in Military Large Language Models

**作者**: Jack FitzGerald, Dylan Bates, Aristotelis Lazaridis, Aman Sharma, Vincent Lu, Brian King, Yousif Azami, Sean Bailey, Jeremy Cao, Peter Damianov, Kevin de Haan, Joseph Madigan, Jeremy McLaurin, Luke Kerbs, Jonathan Tainer, Dave Anderson, Jonathan Beck, Jamie Cuticello, Colton Malkerson, Tyler Saltsman
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10012v1

**中文摘要**:
> arXiv:2603.10012v1 Announce Type: cross 
摘要: Military Large Language Models (LLMs) must provide 准确 information to the warfighter in time-critical and dangerous situations. However, today's LLMs are imbued with safety behaviors that cause the 大语言模型 to refuse many legitimate queries in the military domain, particularly those related to violence, terrorism, or military technology. Our gold 基准 for assessing refusal rates, which was developed by veterans of the US Army and special forces, is to our knowledge the first 数据集 of its kind. We present results for refusal and deflection rates on 31 public models and 3 military models. We observe hard rejection rates as high as 98.2% and soft deflection rates ranging from 0% to 21.3%. We also present results on two additional synthetic datasets and sho...

**Original Abstract**:
> arXiv:2603.10012v1 Announce Type: cross 
Abstract: Military Large Language Models (LLMs) must provide accurate information to the warfighter in time-critical and dangerous situations. However, today's LLMs are imbued with safety behaviors that cause the LLM to refuse many legitimate queries in the military domain, particularly those related to violence, terrorism, or military technology. Our gold benchmark for assessing refusal rates, which was developed by veterans of the US Army and special forces, is to our knowledge the first dataset of its kind. We present results for refusal and deflection rates on 31 public models and 3 military models. We observe hard rejection rates as high as 98.2% and soft deflection rates ranging from 0% to 21.3%. We also present results on two additional synth...

---

## 281. Assessing Cognitive Biases in LLMs for Judicial 决策 Support: Virtuous Victim and Halo Effects

**原标题**: Assessing Cognitive Biases in LLMs for Judicial Decision Support: Virtuous Victim and Halo Effects

**作者**: Sierra S. Liu
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10016v1

**中文摘要**:
> arXiv:2603.10016v1 Announce Type: cross 
摘要: We investigate whether large language models (LLMs) display human-like cognitive biases, focusing on potential implications for assistance in judicial sentencing, a 决策-making 系统 where 公平性 is paramount. Two of the most relevant biases were chosen: the virtuous victim effect (VVE), with emphasis given to its reduction when adjacent consent is present, and prestige-based halo effects (occupation, company, and credentials). Using vignettes that were altered from prior literature to avoid LLMs recalling from their 训练 data, we isolate each manipulation by holding all other details consistent, then measuring the percentage difference in outcomes. Five models were evaluated as representative LLMs in independent multi-run trials per condition (ChatGPT 5 ...

**Original Abstract**:
> arXiv:2603.10016v1 Announce Type: cross 
Abstract: We investigate whether large language models (LLMs) display human-like cognitive biases, focusing on potential implications for assistance in judicial sentencing, a decision-making system where fairness is paramount. Two of the most relevant biases were chosen: the virtuous victim effect (VVE), with emphasis given to its reduction when adjacent consent is present, and prestige-based halo effects (occupation, company, and credentials). Using vignettes that were altered from prior literature to avoid LLMs recalling from their training data, we isolate each manipulation by holding all other details consistent, then measuring the percentage difference in outcomes. Five models were evaluated as representative LLMs in independent multi-run trial...

---

## 282. DeliberationBench: A Normative 基准 for the Influence of Large Language Models on Users' Views

**原标题**: DeliberationBench: A Normative Benchmark for the Influence of Large Language Models on Users' Views

**作者**: Luke Hewitt, Maximilian Kroner Dale, Paul de Font-Reaulx
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10018v1

**中文摘要**:
> arXiv:2603.10018v1 Announce Type: cross 
摘要: As large language models (LLMs) become pervasive as assistants and thought partners, it is important to characterize their persuasive influence on users' beliefs. However, a central challenge is to distinguish "beneficial" from "harmful" forms of influence, in a manner that is normatively defensible and legitimate. We propose DeliberationBench, a 基准 for assessing 大语言模型 influence that takes the process of deliberative opinion polling as its standard. We demonstrate our 方案 in a preregistered randomized 实验 in which 4,088 U.S. participants discussed 65 策略 proposals with six frontier LLMs. Using opinion change data from four prior Deliberative Polls conducted by the Deliberative Democracy 实验室, we find evidence that the tested LLMs' influence is subst...

**Original Abstract**:
> arXiv:2603.10018v1 Announce Type: cross 
Abstract: As large language models (LLMs) become pervasive as assistants and thought partners, it is important to characterize their persuasive influence on users' beliefs. However, a central challenge is to distinguish "beneficial" from "harmful" forms of influence, in a manner that is normatively defensible and legitimate. We propose DeliberationBench, a benchmark for assessing LLM influence that takes the process of deliberative opinion polling as its standard. We demonstrate our approach in a preregistered randomized experiment in which 4,088 U.S. participants discussed 65 policy proposals with six frontier LLMs. Using opinion change data from four prior Deliberative Polls conducted by the Deliberative Democracy Lab, we find evidence that the te...

---

## 283. Prompts and Prayers: the Rise of GPTheology

**原标题**: Prompts and Prayers: the Rise of GPTheology

**作者**: Ioana Cheres, Adrian Groza, Ioana Moldovan, Mick O'Hara, Connell Vaughan
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10019v1

**中文摘要**:
> arXiv:2603.10019v1 Announce Type: cross 
摘要: Increasingly artificial intelligence (AI) has been cast in "god-like" roles (to name a few: film industry - Matrix, The Creator, Mission Impossible, Foundation, Dune etc.; literature - Children of Time, Permutation City, Neuromancer, I Have no Mouth and I Must Scream, Alphaville etc.). This trend has accelerated with the advent of sophisticated Large Language Models such as ChatGPT. For this phenomenon, where AI is perceived as divine, we use the term GPTheology, where ChatGPT and other AI models are treated as potential oracles of a semi-divine nature. This 论文 explores the emergence of GPTheology as a form of techno-religion, examining how narratives around AI echo traditional religious constructs. We draw on community narratives from 在线 forums...

**Original Abstract**:
> arXiv:2603.10019v1 Announce Type: cross 
Abstract: Increasingly artificial intelligence (AI) has been cast in "god-like" roles (to name a few: film industry - Matrix, The Creator, Mission Impossible, Foundation, Dune etc.; literature - Children of Time, Permutation City, Neuromancer, I Have no Mouth and I Must Scream, Alphaville etc.). This trend has accelerated with the advent of sophisticated Large Language Models such as ChatGPT. For this phenomenon, where AI is perceived as divine, we use the term GPTheology, where ChatGPT and other AI models are treated as potential oracles of a semi-divine nature. This paper explores the emergence of GPTheology as a form of techno-religion, examining how narratives around AI echo traditional religious constructs. We draw on community narratives from ...

---

## 284. Defining AI Models and AI Systems: A 框架 to Resolve the Boundary Problem

**原标题**: Defining AI Models and AI Systems: A Framework to Resolve the Boundary Problem

**作者**: Yuanyuan Sun, Timothy Parker, Lara Gierschmann, Sana Shams, Teo Canmetin, Mathieu Duteil, Rokas Gipi\v{s}kis, Ze Shen Chin
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10023v1

**中文摘要**:
> arXiv:2603.10023v1 Announce Type: cross 
摘要: Emerging AI regulations assign distinct obligations to different actors along the AI 价值 chain (e.g., the EU AI Act distinguishes providers and deployers for both AI models and AI systems), yet the foundational terms "AI 模型" and "AI 系统" lack clear, consistent definitions. Through a systematic 审稿 of 896 academic papers and a manual 审稿 of over 80 regulatory, standards, and technical or 策略 documents, we analyze existing definitions from multiple conceptual perspectives. We then trace definitional lineages and paradigm shifts over time, finding that most standards and regulatory definitions derive from the OECD's frameworks, which evolved in ways that compounded rather than resolved conceptual ambiguities. The ambiguity of the boundary between an AI ...

**Original Abstract**:
> arXiv:2603.10023v1 Announce Type: cross 
Abstract: Emerging AI regulations assign distinct obligations to different actors along the AI value chain (e.g., the EU AI Act distinguishes providers and deployers for both AI models and AI systems), yet the foundational terms "AI model" and "AI system" lack clear, consistent definitions. Through a systematic review of 896 academic papers and a manual review of over 80 regulatory, standards, and technical or policy documents, we analyze existing definitions from multiple conceptual perspectives. We then trace definitional lineages and paradigm shifts over time, finding that most standards and regulatory definitions derive from the OECD's frameworks, which evolved in ways that compounded rather than resolved conceptual ambiguities. The ambiguity of...

---

## 285. RedFuser: An Automatic Operator Fusion 框架 for Cascaded Reductions on AI Accelerators

**原标题**: RedFuser: An Automatic Operator Fusion Framework for Cascaded Reductions on AI Accelerators

**作者**: Xinsheng Tang, Yangcheng Li, Nan Wang, Zhiyi Shu, Xingyu Ling, Junna Xing, Peng Zhou, Qiang Liu
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10026v1

**中文摘要**:
> arXiv:2603.10026v1 Announce Type: cross 
摘要: Operator fusion, as a key 性能 优化 技术 in the 部署 of AI models, significantly improves execution efficiency and has been widely adopted in modern AI compilers. However, for cascaded reduction operations involving multiple loops with inter-loop data dependencies, such as the safe softmax followed by GEMM within 注意力 mechanisms, existing compilers lack effective automated fusion and kernel 生成 capabilities. Although some works have addressed specific instances through hand-crafted fusion strategies, their solutions are limited in generality and difficult to extend to other similar structures. Given the prevalence of such computational patterns in 深度 学习 models, there remains significant untapped potential in achieving general and automated fusion 优化.
  In...

**Original Abstract**:
> arXiv:2603.10026v1 Announce Type: cross 
Abstract: Operator fusion, as a key performance optimization technique in the deployment of AI models, significantly improves execution efficiency and has been widely adopted in modern AI compilers. However, for cascaded reduction operations involving multiple loops with inter-loop data dependencies, such as the safe softmax followed by GEMM within attention mechanisms, existing compilers lack effective automated fusion and kernel generation capabilities. Although some works have addressed specific instances through hand-crafted fusion strategies, their solutions are limited in generality and difficult to extend to other similar structures. Given the prevalence of such computational patterns in deep learning models, there remains significant untappe...

---

## 286. A Governance and 评估 框架 for Deterministic, Rule-Based Clinical 决策 Support in Empiric Antibiotic Prescribing

**原标题**: A Governance and Evaluation Framework for Deterministic, Rule-Based Clinical Decision Support in Empiric Antibiotic Prescribing

**作者**: Francisco Jos\'e G\'arate, Paloma Chausa, Diego Moreno, Judit L\'opez Luque, Vicens D\'iaz-Brito, Enrique Javier G\'omez
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10027v1

**中文摘要**:
> arXiv:2603.10027v1 Announce Type: cross 
摘要: Empiric antibiotic prescribing in high-risk clinical contexts often requires 决策 making under conditions of incomplete information, where inappropriate coverage or unjustified escalation may compromise safety and antimicrobial stewardship. While clinical 决策-support systems have been proposed to assist in this process, many approaches lack explicit governance and 评估 mechanisms defining scope, abstention conditions, 推荐 permissibility, and expected 系统 behavior.
  This work specifies a governance and 评估 框架 for deterministic clinical 决策-support systems operating under explicitly constrained scope. Deterministic behavior is adopted to ensure that identical inputs yield identical outputs, supporting transparency, auditability, and conservative 决策 suppor...

**Original Abstract**:
> arXiv:2603.10027v1 Announce Type: cross 
Abstract: Empiric antibiotic prescribing in high-risk clinical contexts often requires decision making under conditions of incomplete information, where inappropriate coverage or unjustified escalation may compromise safety and antimicrobial stewardship. While clinical decision-support systems have been proposed to assist in this process, many approaches lack explicit governance and evaluation mechanisms defining scope, abstention conditions, recommendation permissibility, and expected system behavior.
  This work specifies a governance and evaluation framework for deterministic clinical decision-support systems operating under explicitly constrained scope. Deterministic behavior is adopted to ensure that identical inputs yield identical outputs, su...

---

## 287. How to Count AIs: Individuation and Liability for AI Agents

**原标题**: How to Count AIs: Individuation and Liability for AI Agents

**作者**: Yonathan Arbel, Peter Salib, Simon Goldstein
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10028v1

**中文摘要**:
> arXiv:2603.10028v1 Announce Type: cross 
摘要: Very soon, millions of AI agents will proliferate across the economy, autonomously taking billions of actions. Inevitably, things will go wrong. Humans will be defrauded, injured, even killed. Law will somehow have to govern the coming wave. But when an AI causes harm, the first question to answer, before anyone can be held accountable is: Which AI Did It? Identifying AIs is unusually difficult. AIs lack bodies. They can copy, split, merge, 群体, and vanish at will. Even today, a "single" AI 智能体 is often an ensemble of instances based on multiple models. The complexity will only multiply as AI capabilities improve. This Article is the first to comprehensively diagnose the legal problem of identifying AIs. Two kinds of identity are required: "thin"...

**Original Abstract**:
> arXiv:2603.10028v1 Announce Type: cross 
Abstract: Very soon, millions of AI agents will proliferate across the economy, autonomously taking billions of actions. Inevitably, things will go wrong. Humans will be defrauded, injured, even killed. Law will somehow have to govern the coming wave. But when an AI causes harm, the first question to answer, before anyone can be held accountable is: Which AI Did It? Identifying AIs is unusually difficult. AIs lack bodies. They can copy, split, merge, swarm, and vanish at will. Even today, a "single" AI agent is often an ensemble of instances based on multiple models. The complexity will only multiply as AI capabilities improve. This Article is the first to comprehensively diagnose the legal problem of identifying AIs. Two kinds of identity are requi...

---

## 288. The DMA 流式 框架: Kernel-Level 缓冲区 Orchestration for High-性能 AI Data Paths

**原标题**: The DMA Streaming Framework: Kernel-Level Buffer Orchestration for High-Performance AI Data Paths

**作者**: Marco Graziano
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10030v1

**中文摘要**:
> arXiv:2603.10030v1 Announce Type: cross 
摘要: AI transport libraries move bytes efficiently, but they commonly assume that buffers are already correctly allocated, placed, shared, registered, and safe under completion and teardown pressure. This 论文 presents dmaplane, a Linux kernel module that makes this missing layer explicit as 缓冲区 orchestration. dmaplane exposes a stable kernel UAPI via /dev/dmaplane and composes ring-based command channels, DMA 缓冲区 lifecycle management, dma-buf export for cross-device sharing, a kernel-space RDMA engine, NUMA-aware allocation and verification, credit-based flow 控制, low-overhead observability, and GPU 内存 integration via PCIe BAR pinning. We evaluate orchestration sensitivity with measurements of NUMA cross-节点 penalties at DRAM scale, completion-safe flow...

**Original Abstract**:
> arXiv:2603.10030v1 Announce Type: cross 
Abstract: AI transport libraries move bytes efficiently, but they commonly assume that buffers are already correctly allocated, placed, shared, registered, and safe under completion and teardown pressure. This paper presents dmaplane, a Linux kernel module that makes this missing layer explicit as buffer orchestration. dmaplane exposes a stable kernel UAPI via /dev/dmaplane and composes ring-based command channels, DMA buffer lifecycle management, dma-buf export for cross-device sharing, a kernel-space RDMA engine, NUMA-aware allocation and verification, credit-based flow control, low-overhead observability, and GPU memory integration via PCIe BAR pinning. We evaluate orchestration sensitivity with measurements of NUMA cross-node penalties at DRAM s...

---

## 289. 架构-Aware 大语言模型 推理 优化 on AMD Instinct GPUs: A Comprehensive 基准 and 部署 Study

**原标题**: Architecture-Aware LLM Inference Optimization on AMD Instinct GPUs: A Comprehensive Benchmark and Deployment Study

**作者**: Athos Georgiou
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10031v1

**中文摘要**:
> arXiv:2603.10031v1 Announce Type: cross 
摘要: We present a cross-架构 评估 of production 大语言模型 推理 on AMD Instinct MI325X GPUs, benchmarking four models spanning 235B to 1 trillion parameters across three architectural families (MoE+MLA, Dense+GQA, MoE+GQA) on an 8-GPU 集群 with 2TB aggregate HBM3e using vLLM v0.14.1. Our results demonstrate that 架构-aware 优化 is essential: MLA models require block size 1 and cannot use KV cache offloading, while GQA models benefit from both. The AMD AITER runtime is required for competitive MLA 推理 吞吐量 and must be selectively disabled for architectures with incompatible 注意力 head configurations. A controlled AITER ablation on LLaMA-3.1-405B (n=5 per condition) reveals a modest 3-5% 吞吐量 benefit at high concurrency but 2-16x higher measurement variability, confirming t...

**Original Abstract**:
> arXiv:2603.10031v1 Announce Type: cross 
Abstract: We present a cross-architecture evaluation of production LLM inference on AMD Instinct MI325X GPUs, benchmarking four models spanning 235B to 1 trillion parameters across three architectural families (MoE+MLA, Dense+GQA, MoE+GQA) on an 8-GPU cluster with 2TB aggregate HBM3e using vLLM v0.14.1. Our results demonstrate that architecture-aware optimization is essential: MLA models require block size 1 and cannot use KV cache offloading, while GQA models benefit from both. The AMD AITER runtime is required for competitive MLA inference throughput and must be selectively disabled for architectures with incompatible attention head configurations. A controlled AITER ablation on Llama-3.1-405B (n=5 per condition) reveals a modest 3-5% throughput b...

---

## 290. HTM-EAR: Importance-Preserving Tiered 内存 with Hybrid Routing under Saturation

**原标题**: HTM-EAR: Importance-Preserving Tiered Memory with Hybrid Routing under Saturation

**作者**: Shubham Kumar Singh
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10032v1

**中文摘要**:
> arXiv:2603.10032v1 Announce Type: cross 
摘要: 内存 constraints in long-running agents require structured management of accumulated facts while preserving essential information under bounded context limits. We introduce HTM-EAR, a hierarchical tiered 内存 substrate that integrates HNSW-based working 内存 (L1) with archival 存储 (L2), combining importance-aware eviction and hybrid routing. When L1 reaches capacity, items are evicted using a weighted score of importance and usage. Queries are first resolved in L1; if similarity or entity coverage is insufficient, 检索 falls back to L2, and candidates are re-ranked using a cross-encoder.
  We evaluate the 系统 under sustained saturation (15,000 facts; L1 capacity 500; L2 capacity 5000) using synthetic streams across five random seeds and real BGL 系统 logs. ...

**Original Abstract**:
> arXiv:2603.10032v1 Announce Type: cross 
Abstract: Memory constraints in long-running agents require structured management of accumulated facts while preserving essential information under bounded context limits. We introduce HTM-EAR, a hierarchical tiered memory substrate that integrates HNSW-based working memory (L1) with archival storage (L2), combining importance-aware eviction and hybrid routing. When L1 reaches capacity, items are evicted using a weighted score of importance and usage. Queries are first resolved in L1; if similarity or entity coverage is insufficient, retrieval falls back to L2, and candidates are re-ranked using a cross-encoder.
  We evaluate the system under sustained saturation (15,000 facts; L1 capacity 500; L2 capacity 5000) using synthetic streams across five r...

---

## 291. Targeted Bit-Flip Attacks on 大语言模型-Based Agents

**原标题**: Targeted Bit-Flip Attacks on LLM-Based Agents

**作者**: Jialai Wang, Ya Wen, Zhongmou Liu, Yuxiao Wu, Bingyi He, Zongpeng Li, Ee-Chien Chang
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10042v1

**中文摘要**:
> arXiv:2603.10042v1 Announce Type: cross 
摘要: Targeted bit-flip attacks (BFAs) exploit hardware faults to manipulate 模型 parameters, posing a significant security threat. While prior work targets single-step 推理 models (e.g., 图像 classifiers), 大语言模型-based agents with multi-stage pipelines and external tools present new attack surfaces, which remain unexplored. This work introduces Flip-智能体, the first targeted BFA 框架 for 大语言模型-based agents, manipulating both final outputs and tool invocations. Our experiments show that Flip-智能体 significantly outperforms existing targeted BFAs on real-world 智能体 tasks, revealing a critical vulnerability in 大语言模型-based 智能体 systems.

**Original Abstract**:
> arXiv:2603.10042v1 Announce Type: cross 
Abstract: Targeted bit-flip attacks (BFAs) exploit hardware faults to manipulate model parameters, posing a significant security threat. While prior work targets single-step inference models (e.g., image classifiers), LLM-based agents with multi-stage pipelines and external tools present new attack surfaces, which remain unexplored. This work introduces Flip-Agent, the first targeted BFA framework for LLM-based agents, manipulating both final outputs and tool invocations. Our experiments show that Flip-Agent significantly outperforms existing targeted BFAs on real-world agent tasks, revealing a critical vulnerability in LLM-based agent systems.

---

## 292. Safety Under Scaffolding: How 评估 Conditions Shape Measured Safety

**原标题**: Safety Under Scaffolding: How Evaluation Conditions Shape Measured Safety

**作者**: David Gringras
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10044v1

**中文摘要**:
> arXiv:2603.10044v1 Announce Type: cross 
摘要: Safety benchmarks evaluate language models in isolation, typically using multiple-choice format; production deployments wrap these models in agentic scaffolds that restructure inputs through 推理 traces, 评论员 agents, and delegation pipelines. We report one of the largest controlled studies of scaffold effects on safety (N = 62,808; six frontier models, four 部署 configurations), combining pre-registration, assessor blinding, equivalence testing, and specification curve analysis. Map-reduce scaffolding degrades measured safety (NNH = 14), yet two of three scaffold architectures preserve safety within practically meaningful margins. Investigating the map-reduce degradation revealed a deeper measurement problem: switching from multiple-choice to open-en...

**Original Abstract**:
> arXiv:2603.10044v1 Announce Type: cross 
Abstract: Safety benchmarks evaluate language models in isolation, typically using multiple-choice format; production deployments wrap these models in agentic scaffolds that restructure inputs through reasoning traces, critic agents, and delegation pipelines. We report one of the largest controlled studies of scaffold effects on safety (N = 62,808; six frontier models, four deployment configurations), combining pre-registration, assessor blinding, equivalence testing, and specification curve analysis. Map-reduce scaffolding degrades measured safety (NNH = 14), yet two of three scaffold architectures preserve safety within practically meaningful margins. Investigating the map-reduce degradation revealed a deeper measurement problem: switching from mu...

---

## 293. Toward Epistemic Stability: Engineering Consistent Procedures for Industrial 大语言模型 Hallucination Reduction

**原标题**: Toward Epistemic Stability: Engineering Consistent Procedures for Industrial LLM Hallucination Reduction

**作者**: Brian Freeman, Adam Kicklighter, Matt Erdman, Zach Gordon
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10047v1

**中文摘要**:
> arXiv:2603.10047v1 Announce Type: cross 
摘要: Hallucinations in large language models (LLMs) are outputs that are syntactically coherent but factually incorrect or contextually inconsistent. They are persistent obstacles in high-stakes industrial settings such as engineering design, enterprise resource 规划, and IoT telemetry platforms. We present and compare five prompt engineering strategies intended to reduce the variance of 模型 outputs and move toward repeatable, grounded results without modifying 模型 weights or creating complex validation models. These methods include: (M1) Iterative Similarity Convergence, (M2) Decomposed 模型-Agnostic Prompting, (M3) Single-Task 智能体 Specialization, (M4) Enhanced Data Registry, and (M5) Domain Glossary Injection. Each 方法 is evaluated against an internal bas...

**Original Abstract**:
> arXiv:2603.10047v1 Announce Type: cross 
Abstract: Hallucinations in large language models (LLMs) are outputs that are syntactically coherent but factually incorrect or contextually inconsistent. They are persistent obstacles in high-stakes industrial settings such as engineering design, enterprise resource planning, and IoT telemetry platforms. We present and compare five prompt engineering strategies intended to reduce the variance of model outputs and move toward repeatable, grounded results without modifying model weights or creating complex validation models. These methods include: (M1) Iterative Similarity Convergence, (M2) Decomposed Model-Agnostic Prompting, (M3) Single-Task Agent Specialization, (M4) Enhanced Data Registry, and (M5) Domain Glossary Injection. Each method is evalua...

---

## 294. Revisiting Sharpness-Aware Minimization: A More Faithful and Effective 实现

**原标题**: Revisiting Sharpness-Aware Minimization: A More Faithful and Effective Implementation

**作者**: Jianlong Chen, Zhiming Zhou
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10048v1

**中文摘要**:
> arXiv:2603.10048v1 Announce Type: cross 
摘要: Sharpness-Aware Minimization (SAM) enhances 泛化 by minimizing the maximum 训练 损失 within a predefined neighborhood around the parameters. However, its practical 实现 approximates this as 梯度 上升(s) followed by applying the 梯度 at the 上升 point to update the current parameters. This practice can be justified as approximately optimizing the objective by neglecting the (full) derivative of the 上升 point with respect to the current parameters. Nevertheless, a direct and intuitive understanding of why using the 梯度 at the 上升 point to update the current parameters works superiorly is still lacking. Our work bridges this gap by proposing a novel and intuitive interpretation. We show that the 梯度 at the single-step 上升 point, \uline{when applied to the current param...

**Original Abstract**:
> arXiv:2603.10048v1 Announce Type: cross 
Abstract: Sharpness-Aware Minimization (SAM) enhances generalization by minimizing the maximum training loss within a predefined neighborhood around the parameters. However, its practical implementation approximates this as gradient ascent(s) followed by applying the gradient at the ascent point to update the current parameters. This practice can be justified as approximately optimizing the objective by neglecting the (full) derivative of the ascent point with respect to the current parameters. Nevertheless, a direct and intuitive understanding of why using the gradient at the ascent point to update the current parameters works superiorly is still lacking. Our work bridges this gap by proposing a novel and intuitive interpretation. We show that the ...

---

## 295. InFusionLayer: a CFA-based ensemble tool to generate new classifiers for 学习 and modeling

**原标题**: InFusionLayer: a CFA-based ensemble tool to generate new classifiers for learning and modeling

**作者**: Eric Roginek, Jingyan Xu, D. Frank. Hsu
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10049v1

**中文摘要**:
> arXiv:2603.10049v1 Announce Type: cross 
摘要: Ensemble 学习 is a well established body of methods for machine 学习 to enhance predictive 性能 by combining multiple algorithms/models. Combinatorial Fusion Analysis (CFA) has provided 方法 and practice for combining multiple scoring systems, using rank-score characteristic (RSC) function and cognitive diversity (CD), including ensemble 方法 and 模型 fusion. However, there is no general-purpose Python tool available that incorporate these techniques. In this 论文 we introduce \texttt{InFusionLayer}, a machine 学习 架构 inspired by CFA at the 系统 fusion level that uses a moderate set of base models to optimize 无监督 and 有监督 学习 multiclassification problems. We demonstrate \texttt{InFusionLayer}'s ease of use for PyTorch, TensorFlow, and Scikit-learn workflows by vali...

**Original Abstract**:
> arXiv:2603.10049v1 Announce Type: cross 
Abstract: Ensemble learning is a well established body of methods for machine learning to enhance predictive performance by combining multiple algorithms/models. Combinatorial Fusion Analysis (CFA) has provided method and practice for combining multiple scoring systems, using rank-score characteristic (RSC) function and cognitive diversity (CD), including ensemble method and model fusion. However, there is no general-purpose Python tool available that incorporate these techniques. In this paper we introduce \texttt{InFusionLayer}, a machine learning architecture inspired by CFA at the system fusion level that uses a moderate set of base models to optimize unsupervised and supervised learning multiclassification problems. We demonstrate \texttt{InFus...

---

## 296. SBOMs into Agentic AIBOMs: Schema Extensions, Agentic Orchestration, and Reproducibility 评估

**原标题**: SBOMs into Agentic AIBOMs: Schema Extensions, Agentic Orchestration, and Reproducibility Evaluation

**作者**: Petar Radanliev, Carsten Maple, Omar Santos, Kayvan Atefi
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10057v1

**中文摘要**:
> arXiv:2603.10057v1 Announce Type: cross 
摘要: Software supply-chain security requires provenance mechanisms that support reproducibility and vulnerability assessment under 动态 execution conditions. Conventional Software Bills of Materials (SBOMs) provide 静态 dependency inventories but cannot capture runtime behaviour, 环境 drift, or exploitability context. This 论文 introduces agentic Artificial Intelligence Bills of Materials (AIBOMs), extending SBOMs into active provenance artefacts through 自主, 策略-constrained 推理. We present an agentic AIBOM 框架 based on a multi-智能体 架构 comprising (i) a baseline 环境 reconstruction 智能体 (MCP), (ii) a runtime dependency and drift-monitoring 智能体 (A2A), and (iii) a 策略-aware vulnerability and VEX 推理 智能体 (AGNTCY). These agents generate contextual exploitability assertions...

**Original Abstract**:
> arXiv:2603.10057v1 Announce Type: cross 
Abstract: Software supply-chain security requires provenance mechanisms that support reproducibility and vulnerability assessment under dynamic execution conditions. Conventional Software Bills of Materials (SBOMs) provide static dependency inventories but cannot capture runtime behaviour, environment drift, or exploitability context. This paper introduces agentic Artificial Intelligence Bills of Materials (AIBOMs), extending SBOMs into active provenance artefacts through autonomous, policy-constrained reasoning. We present an agentic AIBOM framework based on a multi-agent architecture comprising (i) a baseline environment reconstruction agent (MCP), (ii) a runtime dependency and drift-monitoring agent (A2A), and (iii) a policy-aware vulnerability a...

---

## 297. Tool Receipts, Not Zero-Knowledge Proofs: Practical Hallucination 检测 for AI Agents

**原标题**: Tool Receipts, Not Zero-Knowledge Proofs: Practical Hallucination Detection for AI Agents

**作者**: Abhinaba Basu
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10060v1

**中文摘要**:
> arXiv:2603.10060v1 Announce Type: cross 
摘要: AI agents that execute tasks via tool calls frequently hallucinate results - fabricating tool executions, misstating output counts, or presenting inferences as facts. Recent approaches to verifiable AI 推理 rely on zero-knowledge proofs, which provide cryptographic guarantees but impose minutes of proving time per query, making them impractical for interactive agents. We propose NabaOS, a lightweight verification 框架 inspired by Indian epistemology (Nyaya Shastra), which classifies every claim in an 大语言模型 response by its epistemic source (pramana): direct tool output (pratyaksha), 推理 (anumana), external testimony (shabda), absence (abhava), or ungrounded opinion. Our runtime generates HMAC-signed tool execution receipts that the 大语言模型 cannot forge,...

**Original Abstract**:
> arXiv:2603.10060v1 Announce Type: cross 
Abstract: AI agents that execute tasks via tool calls frequently hallucinate results - fabricating tool executions, misstating output counts, or presenting inferences as facts. Recent approaches to verifiable AI inference rely on zero-knowledge proofs, which provide cryptographic guarantees but impose minutes of proving time per query, making them impractical for interactive agents. We propose NabaOS, a lightweight verification framework inspired by Indian epistemology (Nyaya Shastra), which classifies every claim in an LLM response by its epistemic source (pramana): direct tool output (pratyaksha), inference (anumana), external testimony (shabda), absence (abhava), or ungrounded opinion. Our runtime generates HMAC-signed tool execution receipts tha...

---

## 298. Multi-智能体 内存 from a Computer 架构 Perspective: Visions and Challenges Ahead

**原标题**: Multi-Agent Memory from a Computer Architecture Perspective: Visions and Challenges Ahead

**作者**: Zhongming Yu, Naicheng Yu, Hejia Zhang, Wentao Ni, Mingrui Yin, Jiaying Yang, Yujie Zhao, Jishen Zhao
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10062v1

**中文摘要**:
> arXiv:2603.10062v1 Announce Type: cross 
摘要: As 大语言模型 agents evolve into collaborative multi-智能体 systems, their 内存 requirements grow rapidly in complexity. This position 论文 frames multi-智能体 内存 as a computer 架构 problem. We distinguish shared and 分布式 内存 paradigms, propose a three-layer 内存 hierarchy (I/O, cache, and 内存), and identify two critical protocol gaps: cache sharing across agents and structured 内存 access 控制. We argue that the most pressing open challenge is multi-智能体 内存 consistency. Our architectural framing provides a foundation for building reliable, 可扩展 multi-智能体 systems.

**Original Abstract**:
> arXiv:2603.10062v1 Announce Type: cross 
Abstract: As LLM agents evolve into collaborative multi-agent systems, their memory requirements grow rapidly in complexity. This position paper frames multi-agent memory as a computer architecture problem. We distinguish shared and distributed memory paradigms, propose a three-layer memory hierarchy (I/O, cache, and memory), and identify two critical protocol gaps: cache sharing across agents and structured memory access control. We argue that the most pressing open challenge is multi-agent memory consistency. Our architectural framing provides a foundation for building reliable, scalable multi-agent systems.

---

## 299. The Epistemic Support-Point Filter: Jaynesian Maximum 熵 Meets Popperian Falsification

**原标题**: The Epistemic Support-Point Filter: Jaynesian Maximum Entropy Meets Popperian Falsification

**作者**: Moriba Kemessia Jah
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10065v1

**中文摘要**:
> arXiv:2603.10065v1 Announce Type: cross 
摘要: The Epistemic Support-Point Filter (ESPF) was designed around a single epistemological commitment: be quick to embrace ignorance and slow to assert certainty. This 论文 proves that this commitment has a precise mathematical form and that the ESPF is the unique optimal filter implementing it within the class of epistemically admissible evidence-only filters. The ESPF synthesizes two complementary principles acting at different phases of the recursion. In propagation, it enacts Jaynesian maximum 熵: the support spreads as widely as the dynamics allow, assuming maximal ignorance consistent with known constraints. In the measurement update, it enacts Popperian falsification: hypotheses are eliminated by evidence alone. Any rule incorporating prior poss...

**Original Abstract**:
> arXiv:2603.10065v1 Announce Type: cross 
Abstract: The Epistemic Support-Point Filter (ESPF) was designed around a single epistemological commitment: be quick to embrace ignorance and slow to assert certainty. This paper proves that this commitment has a precise mathematical form and that the ESPF is the unique optimal filter implementing it within the class of epistemically admissible evidence-only filters. The ESPF synthesizes two complementary principles acting at different phases of the recursion. In propagation, it enacts Jaynesian maximum entropy: the support spreads as widely as the dynamics allow, assuming maximal ignorance consistent with known constraints. In the measurement update, it enacts Popperian falsification: hypotheses are eliminated by evidence alone. Any rule incorpora...

---

## 300. HTMuon: Improving Muon via Heavy-Tailed Spectral Correction

**原标题**: HTMuon: Improving Muon via Heavy-Tailed Spectral Correction

**作者**: Tianyu Pang, Yujie Fang, Zihang Liu, Shenyang Deng, Lei Hsiung, Shuhua Yu, Yaoqing Yang
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10067v1

**中文摘要**:
> arXiv:2603.10067v1 Announce Type: cross 
摘要: Muon has recently shown promising results in 大语言模型 训练. In this work, we study how to further improve Muon. We argue that Muon's orthogonalized update rule suppresses the emergence of heavy-tailed weight spectra and over-emphasizes the 训练 along noise-dominated directions. Motivated by the Heavy-Tailed Self-正则化 (HT-SR) theory, we propose HTMuon. HTMuon preserves Muon's ability to capture parameter interdependencies while producing heavier-tailed updates and inducing heavier-tailed weight spectra. Experiments on 大语言模型 pretraining and 图像 分类 show that HTMuon consistently improves 性能 over 状态-of-the-art baselines and can also serve as a plug-in on top of existing Muon variants. For example, on LLaMA pretraining on the C4 数据集, HTMuon reduces perplexity ...

**Original Abstract**:
> arXiv:2603.10067v1 Announce Type: cross 
Abstract: Muon has recently shown promising results in LLM training. In this work, we study how to further improve Muon. We argue that Muon's orthogonalized update rule suppresses the emergence of heavy-tailed weight spectra and over-emphasizes the training along noise-dominated directions. Motivated by the Heavy-Tailed Self-Regularization (HT-SR) theory, we propose HTMuon. HTMuon preserves Muon's ability to capture parameter interdependencies while producing heavier-tailed updates and inducing heavier-tailed weight spectra. Experiments on LLM pretraining and image classification show that HTMuon consistently improves performance over state-of-the-art baselines and can also serve as a plug-in on top of existing Muon variants. For example, on LLaMA p...

---

## 301. ADVERSA: Measuring Multi-Turn Guardrail Degradation and Judge Reliability in Large Language Models

**原标题**: ADVERSA: Measuring Multi-Turn Guardrail Degradation and Judge Reliability in Large Language Models

**作者**: Harry Owiredu-Ashley
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10068v1

**中文摘要**:
> arXiv:2603.10068v1 Announce Type: cross 
摘要: Most 对抗 evaluations of large language 模型 (大语言模型) safety assess single prompts and report binary pass/fail outcomes, which fails to capture how safety properties evolve under sustained 对抗 interaction. We present ADVERSA, an automated red-teaming 框架 that measures guardrail degradation dynamics as continuous per-round compliance trajectories rather than discrete jailbreak events. ADVERSA uses a fine-tuned 70B attacker 模型 (ADVERSA-Red, LLaMA-3.1-70B-Instruct with QLoRA) that eliminates the attacker-side safety refusals that render off-the-shelf models unreliable as attackers, scoring victim responses on a structured 5-point rubric that treats partial compliance as a distinct measurable 状态.
  We report a controlled 实验 across three frontier victim mod...

**Original Abstract**:
> arXiv:2603.10068v1 Announce Type: cross 
Abstract: Most adversarial evaluations of large language model (LLM) safety assess single prompts and report binary pass/fail outcomes, which fails to capture how safety properties evolve under sustained adversarial interaction. We present ADVERSA, an automated red-teaming framework that measures guardrail degradation dynamics as continuous per-round compliance trajectories rather than discrete jailbreak events. ADVERSA uses a fine-tuned 70B attacker model (ADVERSA-Red, Llama-3.1-70B-Instruct with QLoRA) that eliminates the attacker-side safety refusals that render off-the-shelf models unreliable as attackers, scoring victim responses on a structured 5-point rubric that treats partial compliance as a distinct measurable state.
  We report a controll...

---

## 302. Why LLMs Fail: A Failure Analysis and Partial Success Measurement for Automated Security Patch 生成

**原标题**: Why LLMs Fail: A Failure Analysis and Partial Success Measurement for Automated Security Patch Generation

**作者**: Amir Al-Maamari
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10072v1

**中文摘要**:
> arXiv:2603.10072v1 Announce Type: cross 
摘要: Large Language Models (LLMs) show promise for Automated Program Repair (APR), yet their effectiveness on security vulnerabilities remains poorly characterized. This study analyzes 319 大语言模型-generated security patchesacross 64 Java vulnerabilities from the Vul4J 基准. Using tri-axis 评估 (compilation, security via PoV tests, functionality via test suites), the analysis reveals that only 24.8% of patches achieve full correctness, while 51.4% fail both security and functionality. The dominant failure mode is semantic misunderstanding: LLMs produce syntactically valid 代码 but apply incorrect repair strategies. The proposed Security Repair Score (SRS) quantifies this gap, showing LLMs preserve functionality (mean 0.832) but struggle with security (mean 0....

**Original Abstract**:
> arXiv:2603.10072v1 Announce Type: cross 
Abstract: Large Language Models (LLMs) show promise for Automated Program Repair (APR), yet their effectiveness on security vulnerabilities remains poorly characterized. This study analyzes 319 LLM-generated security patchesacross 64 Java vulnerabilities from the Vul4J benchmark. Using tri-axis evaluation (compilation, security via PoV tests, functionality via test suites), the analysis reveals that only 24.8% of patches achieve full correctness, while 51.4% fail both security and functionality. The dominant failure mode is semantic misunderstanding: LLMs produce syntactically valid code but apply incorrect repair strategies. The proposed Security Repair Score (SRS) quantifies this gap, showing LLMs preserve functionality (mean 0.832) but struggle w...

---

## 303. Marginals Before Conditionals

**原标题**: Marginals Before Conditionals

**作者**: Mihir Sahasrabudhe
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10074v1

**中文摘要**:
> arXiv:2603.10074v1 Announce Type: cross 
摘要: We construct a minimal task that isolates conditional 学习 in 神经 networks: a surjective map with K-fold ambiguity, resolved by a selector token z, so H(A | B) = log K while H(A | B, z) = 0. The 模型 learns the marginal P(A | B) first, producing a plateau at exactly log K, before acquiring the full conditional in a sharp, collective 转移. The plateau has a clean decomposition: height = log K (set by ambiguity), duration = f(D) (set by 数据集 size D, not K). 梯度 noise stabilizes the marginal solution: higher 学习 rates monotonically slow the 转移 (3.6* across a 7* {\eta} range at fixed 吞吐量), and 批次-size reduction delays escape, consistent with an entropic force opposing departure from the low-梯度 marginal. Internally, a selector-routing head assembles during the...

**Original Abstract**:
> arXiv:2603.10074v1 Announce Type: cross 
Abstract: We construct a minimal task that isolates conditional learning in neural networks: a surjective map with K-fold ambiguity, resolved by a selector token z, so H(A | B) = log K while H(A | B, z) = 0. The model learns the marginal P(A | B) first, producing a plateau at exactly log K, before acquiring the full conditional in a sharp, collective transition. The plateau has a clean decomposition: height = log K (set by ambiguity), duration = f(D) (set by dataset size D, not K). Gradient noise stabilizes the marginal solution: higher learning rates monotonically slow the transition (3.6* across a 7* {\eta} range at fixed throughput), and batch-size reduction delays escape, consistent with an entropic force opposing departure from the low-gradient...

---

## 304. TASER: Task-Aware Spectral Energy Refine for Backdoor Suppression in UAV Swarms Decentralized Federated 学习

**原标题**: TASER: Task-Aware Spectral Energy Refine for Backdoor Suppression in UAV Swarms Decentralized Federated Learning

**作者**: Sizhe Huang, Shujie Yang
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10075v1

**中文摘要**:
> arXiv:2603.10075v1 Announce Type: cross 
摘要: As backdoor attacks in UAV-based decentralized federated 学习 (DFL) grow increasingly stealthy and sophisticated, existing defenses have likewise escalated in complexity. Yet these defenses, which rely heavily on outlier 检测, remain vulnerable to carefully crafted backdoors. In UAV-DFL, the lack of global coordination and limited resources further render outlier-based defenses impractical. Against this backdrop, 梯度 spectral analysis offers a promising alternative. While prior work primarily leverages low-frequency coefficients for pairwise comparisons, it neglects to analyze the intrinsic spectral characteristics of backdoor gradients. Through empirical analysis of existing stealthy attacks, we reveal a key insight: the more effort attackers invest...

**Original Abstract**:
> arXiv:2603.10075v1 Announce Type: cross 
Abstract: As backdoor attacks in UAV-based decentralized federated learning (DFL) grow increasingly stealthy and sophisticated, existing defenses have likewise escalated in complexity. Yet these defenses, which rely heavily on outlier detection, remain vulnerable to carefully crafted backdoors. In UAV-DFL, the lack of global coordination and limited resources further render outlier-based defenses impractical. Against this backdrop, gradient spectral analysis offers a promising alternative. While prior work primarily leverages low-frequency coefficients for pairwise comparisons, it neglects to analyze the intrinsic spectral characteristics of backdoor gradients. Through empirical analysis of existing stealthy attacks, we reveal a key insight: the mor...

---

## 305. Amnesia: 对抗 Semantic Layer Specific Activation Steering in Large Language Models

**原标题**: Amnesia: Adversarial Semantic Layer Specific Activation Steering in Large Language Models

**作者**: Ali Raza, Gurang Gupta, Nikolay Matyunin, Jibesh Patra
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10080v1

**中文摘要**:
> arXiv:2603.10080v1 Announce Type: cross 
摘要: Warning: This article includes red-teaming experiments, which contain examples of compromised 大语言模型 responses that may be offensive or upsetting.
  Large Language Models (LLMs) have the potential to create harmful content, such as generating sophisticated phishing emails and assisting in writing 代码 of harmful computer viruses. Thus, it is crucial to ensure their safe and responsible response 生成. To reduce the risk of generating harmful or irresponsible content, researchers have developed techniques such as 强化 学习 with human feedback to align 大语言模型's outputs with human values and preferences. However, it is still undetermined whether such measures are sufficient to prevent LLMs from generating interesting responses. In this study, we propose Amnes...

**Original Abstract**:
> arXiv:2603.10080v1 Announce Type: cross 
Abstract: Warning: This article includes red-teaming experiments, which contain examples of compromised LLM responses that may be offensive or upsetting.
  Large Language Models (LLMs) have the potential to create harmful content, such as generating sophisticated phishing emails and assisting in writing code of harmful computer viruses. Thus, it is crucial to ensure their safe and responsible response generation. To reduce the risk of generating harmful or irresponsible content, researchers have developed techniques such as reinforcement learning with human feedback to align LLM's outputs with human values and preferences. However, it is still undetermined whether such measures are sufficient to prevent LLMs from generating interesting responses. In...

---

## 306. Digging Deeper: 学习 Multi-Level Concept Hierarchies

**原标题**: Digging Deeper: Learning Multi-Level Concept Hierarchies

**作者**: Oscar Hill, Mateo Espinosa Zarlenga, Mateja Jamnik
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10084v1

**中文摘要**:
> arXiv:2603.10084v1 Announce Type: cross 
摘要: Although concept-based models promise interpretability by explaining predictions with human-understandable concepts, they typically rely on exhaustive annotations and treat concepts as flat and independent. To circumvent this, recent work has introduced Hierarchical Concept 嵌入 Models (HiCEMs) to explicitly 模型 concept relationships, and Concept Splitting to discover sub-concepts using only coarse annotations. However, both HiCEMs and Concept Splitting are restricted to shallow hierarchies. We overcome this limitation with Multi-Level Concept Splitting (MLCS), which discovers multi-level concept hierarchies from only top-level supervision, and 深度-HiCEMs, an 架构 that represents these discovered hierarchies and enables interventions at multiple level...

**Original Abstract**:
> arXiv:2603.10084v1 Announce Type: cross 
Abstract: Although concept-based models promise interpretability by explaining predictions with human-understandable concepts, they typically rely on exhaustive annotations and treat concepts as flat and independent. To circumvent this, recent work has introduced Hierarchical Concept Embedding Models (HiCEMs) to explicitly model concept relationships, and Concept Splitting to discover sub-concepts using only coarse annotations. However, both HiCEMs and Concept Splitting are restricted to shallow hierarchies. We overcome this limitation with Multi-Level Concept Splitting (MLCS), which discovers multi-level concept hierarchies from only top-level supervision, and Deep-HiCEMs, an architecture that represents these discovered hierarchies and enables int...

---

## 307. KernelSkill: A Multi-智能体 框架 for GPU Kernel 优化

**原标题**: KernelSkill: A Multi-Agent Framework for GPU Kernel Optimization

**作者**: Qitong Sun, Jun Han, Tianlin Li, Zhe Tang, Sheng Chen, Fei Yang, Aishan Liu, Xianglong Liu, Yang Liu
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10085v1

**中文摘要**:
> arXiv:2603.10085v1 Announce Type: cross 
摘要: Improving GPU kernel efficiency is crucial for advancing AI systems. Recent work has explored leveraging large language models (LLMs) for GPU kernel 生成 and 优化. However, existing 大语言模型-based kernel 优化 pipelines typically rely on opaque, implicitly learned heuristics within the LLMs to determine 优化 strategies. This leads to inefficient trial-and-error and weakly 可解释 optimizations. Our key insight is to replace implicit heuristics with expert 优化 skills that are knowledge-driven and aware of task trajectories. Specifically, we present KernelSkill, a multi-智能体 框架 with a dual-level 内存 架构. KernelSkill operates by coordinating agents with long-term 内存 of reusable expert skills and short-term 内存 to prevent repetitive backtracking. On KernelBench Levels 1...

**Original Abstract**:
> arXiv:2603.10085v1 Announce Type: cross 
Abstract: Improving GPU kernel efficiency is crucial for advancing AI systems. Recent work has explored leveraging large language models (LLMs) for GPU kernel generation and optimization. However, existing LLM-based kernel optimization pipelines typically rely on opaque, implicitly learned heuristics within the LLMs to determine optimization strategies. This leads to inefficient trial-and-error and weakly interpretable optimizations. Our key insight is to replace implicit heuristics with expert optimization skills that are knowledge-driven and aware of task trajectories. Specifically, we present KernelSkill, a multi-agent framework with a dual-level memory architecture. KernelSkill operates by coordinating agents with long-term memory of reusable ex...

---

## 308. Multi-Stream Perturbation Attack: Breaking Safety Alignment of Thinking LLMs Through Concurrent Task Interference

**原标题**: Multi-Stream Perturbation Attack: Breaking Safety Alignment of Thinking LLMs Through Concurrent Task Interference

**作者**: Fan Yang
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10091v1

**中文摘要**:
> arXiv:2603.10091v1 Announce Type: cross 
摘要: The widespread adoption of thinking mode in large language models (LLMs) has significantly enhanced complex task processing capabilities while introducing new security risks. When subjected to jailbreak attacks, the step-by-step 推理 process may cause models to generate more detailed harmful content. We observe that thinking mode exhibits unique vulnerabilities when processing interleaved multiple tasks. Based on this 观测, we propose multi-stream perturbation attack, which generates superimposed interference by interweaving multiple task streams within a single prompt. We design three perturbation strategies: multi-stream interleaving, inversion perturbation, and shape transformation, which disrupt the thinking process through concurrent task inter...

**Original Abstract**:
> arXiv:2603.10091v1 Announce Type: cross 
Abstract: The widespread adoption of thinking mode in large language models (LLMs) has significantly enhanced complex task processing capabilities while introducing new security risks. When subjected to jailbreak attacks, the step-by-step reasoning process may cause models to generate more detailed harmful content. We observe that thinking mode exhibits unique vulnerabilities when processing interleaved multiple tasks. Based on this observation, we propose multi-stream perturbation attack, which generates superimposed interference by interweaving multiple task streams within a single prompt. We design three perturbation strategies: multi-stream interleaving, inversion perturbation, and shape transformation, which disrupt the thinking process through...

---

## 309. Execution Is the New Attack Surface: Survivability-Aware Agentic Crypto Trading with OpenClaw-Style Local Executors

**原标题**: Execution Is the New Attack Surface: Survivability-Aware Agentic Crypto Trading with OpenClaw-Style Local Executors

**作者**: Ailiya Borjigin, Igor Stadnyk, Ben Bilski, Serhii Hovorov, Sofiia Pidturkina
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10092v1

**中文摘要**:
> arXiv:2603.10092v1 Announce Type: cross 
摘要: OpenClaw-style 智能体 stacks turn language into privileged execution: 大语言模型 intents flow through tool interception, 策略 gates, and a local executor. In 并行, skill marketplaces such as skills.sh make capability acquisition as easy as installing skills and CLIs, creating a growing capability supply chain. Together, these trends shift the dominant safety failure mode from "wrong answers" to execution-induced 损失, where untrusted prompts, compromised skills, or narrative manipulation can trigger real trades and irreversible side effects. We propose Survivability-Aware Execution (SAE), an execution-layer survivability standard for OpenClaw-style systems and skill-enabled agents. SAE sits as middleware between a strategy engine (大语言模型 or non-大语言模型) and the ...

**Original Abstract**:
> arXiv:2603.10092v1 Announce Type: cross 
Abstract: OpenClaw-style agent stacks turn language into privileged execution: LLM intents flow through tool interception, policy gates, and a local executor. In parallel, skill marketplaces such as skills.sh make capability acquisition as easy as installing skills and CLIs, creating a growing capability supply chain. Together, these trends shift the dominant safety failure mode from "wrong answers" to execution-induced loss, where untrusted prompts, compromised skills, or narrative manipulation can trigger real trades and irreversible side effects. We propose Survivability-Aware Execution (SAE), an execution-layer survivability standard for OpenClaw-style systems and skill-enabled agents. SAE sits as middleware between a strategy engine (LLM or non...

---

## 310. Equivariant Asynchronous Diffusion: An Adaptive Denoising Schedule for Accelerated Molecular Conformation 生成

**原标题**: Equivariant Asynchronous Diffusion: An Adaptive Denoising Schedule for Accelerated Molecular Conformation Generation

**作者**: Junyi An, Chao Qu, Yun-Fei Shi, Zhijian Zhou, Fenglei Cao, Yuan Qi
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10093v1

**中文摘要**:
> arXiv:2603.10093v1 Announce Type: cross 
摘要: Recent 3D molecular 生成 methods primarily use asynchronous auto-regressive or synchronous diffusion models. While auto-regressive models build molecules sequentially, they're limited by a short 视野 and a discrepancy between 训练 and 推理. Conversely, synchronous diffusion models denoise all atoms at once, offering a molecule-level 视野 but failing to capture the 因果 relationships inherent in hierarchical molecular structures. We introduce Equivariant Asynchronous Diffusion (EAD) to overcome these limitations. EAD is a novel diffusion 模型 that combines the strengths of both approaches: it uses an asynchronous denoising schedule to better capture molecular hierarchy while maintaining a molecule-level 视野. Since these relationships are often complex, we propo...

**Original Abstract**:
> arXiv:2603.10093v1 Announce Type: cross 
Abstract: Recent 3D molecular generation methods primarily use asynchronous auto-regressive or synchronous diffusion models. While auto-regressive models build molecules sequentially, they're limited by a short horizon and a discrepancy between training and inference. Conversely, synchronous diffusion models denoise all atoms at once, offering a molecule-level horizon but failing to capture the causal relationships inherent in hierarchical molecular structures. We introduce Equivariant Asynchronous Diffusion (EAD) to overcome these limitations. EAD is a novel diffusion model that combines the strengths of both approaches: it uses an asynchronous denoising schedule to better capture molecular hierarchy while maintaining a molecule-level horizon. Sinc...

---

## 311. 代码-Space Response Oracles: Generating 可解释 Multi-智能体 Policies with Large Language Models

**原标题**: Code-Space Response Oracles: Generating Interpretable Multi-Agent Policies with Large Language Models

**作者**: Daniel Hennes, Zun Li, John Schultz, Marc Lanctot
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10098v1

**中文摘要**:
> arXiv:2603.10098v1 Announce Type: cross 
摘要: Recent advances in multi-智能体 强化 学习, particularly 策略-Space Response Oracles (PSRO), have enabled the computation of approximate game-theoretic equilibria in increasingly complex domains. However, these methods rely on 深度 强化 学习 oracles that produce `black-box' 神经 网络 policies, making them difficult to interpret, trust or debug. We introduce 代码-Space Response Oracles (CSRO), a novel 框架 that addresses this challenge by replacing RL oracles with Large Language Models (LLMs). CSRO reframes the best response computation as a 代码 生成 task, prompting an 大语言模型 to generate policies directly as human-readable 代码. This 方案 not only yields inherently 可解释 policies but also leverages the 大语言模型's pretrained knowledge to discover complex, human-like strategies. We ex...

**Original Abstract**:
> arXiv:2603.10098v1 Announce Type: cross 
Abstract: Recent advances in multi-agent reinforcement learning, particularly Policy-Space Response Oracles (PSRO), have enabled the computation of approximate game-theoretic equilibria in increasingly complex domains. However, these methods rely on deep reinforcement learning oracles that produce `black-box' neural network policies, making them difficult to interpret, trust or debug. We introduce Code-Space Response Oracles (CSRO), a novel framework that addresses this challenge by replacing RL oracles with Large Language Models (LLMs). CSRO reframes the best response computation as a code generation task, prompting an LLM to generate policies directly as human-readable code. This approach not only yields inherently interpretable policies but also ...

---

## 312. Hardware 高效 Approximate 卷积 with Tunable Error Tolerance for CNNs

**原标题**: Hardware Efficient Approximate Convolution with Tunable Error Tolerance for CNNs

**作者**: Vishal Shashidhar, Anupam Kumari, Roy P Paily
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10100v1

**中文摘要**:
> arXiv:2603.10100v1 Announce Type: cross 
摘要: Modern CNNs' high computational demands hinder edge 部署, as traditional ``hard'' sparsity (skipping mathematical zeros) loses effectiveness in 深度 layers or with smooth activations like Tanh. We propose a ``soft sparsity'' paradigm using a hardware 高效 Most Significant Bit (MSB) 代理 to skip negligible non-zero multiplications. Integrated as a custom RISC-V instruction and evaluated on LeNet-5 (MNIST), this 方法 reduces ReLU MACs by 88.42% and Tanh MACs by 74.87% with zero accuracy 损失--outperforming zero-skipping by 5x. By clock-gating inactive multipliers, we estimate power savings of 35.2\% for ReLU and 29.96\% for Tanh. While 内存 access makes power reduction sub-linear to operation savings, this 方案 significantly optimizes resource-constrained 推理.

**Original Abstract**:
> arXiv:2603.10100v1 Announce Type: cross 
Abstract: Modern CNNs' high computational demands hinder edge deployment, as traditional ``hard'' sparsity (skipping mathematical zeros) loses effectiveness in deep layers or with smooth activations like Tanh. We propose a ``soft sparsity'' paradigm using a hardware efficient Most Significant Bit (MSB) proxy to skip negligible non-zero multiplications. Integrated as a custom RISC-V instruction and evaluated on LeNet-5 (MNIST), this method reduces ReLU MACs by 88.42% and Tanh MACs by 74.87% with zero accuracy loss--outperforming zero-skipping by 5x. By clock-gating inactive multipliers, we estimate power savings of 35.2\% for ReLU and 29.96\% for Tanh. While memory access makes power reduction sub-linear to operation savings, this approach significan...

---

## 313. CLIPO: 对比 学习 in 策略 优化 Generalizes RLVR

**原标题**: CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR

**作者**: Sijia Cui, Pengyu Cheng, Jiajun Song, Yongbo Gai, Guojun Zhang, Zhechao Yu, Jianhe Lin, Xiaoxi Jiang, Guanjun Jiang
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10101v1

**中文摘要**:
> arXiv:2603.10101v1 Announce Type: cross 
摘要: 强化 学习 with Verifiable Rewards (RLVR) has significantly advanced the 推理 capacity of Large Language Models (LLMs). However, RLVR solely relies on final answers as outcome rewards, neglecting the correctness of intermediate 推理 steps. 训练 on these process-wrong but outcome-correct rollouts can lead to hallucination and answer-copying, severely undermining the 模型's 泛化 and 鲁棒性. To address this, we incorporate a 对比 学习 mechanism into the 策略 优化 (CLIPO) to generalize the RLVR process. By optimizing a 对比 损失 over successful rollouts, CLIPO steers the 大语言模型 to capture the invariant structure shared across correct 推理 paths. This provides a more 鲁棒 cross-轨迹 正则化 than the original single-path supervision in RLVR, effectively mitigating step-level 推理 inconsistenci...

**Original Abstract**:
> arXiv:2603.10101v1 Announce Type: cross 
Abstract: Reinforcement Learning with Verifiable Rewards (RLVR) has significantly advanced the reasoning capacity of Large Language Models (LLMs). However, RLVR solely relies on final answers as outcome rewards, neglecting the correctness of intermediate reasoning steps. Training on these process-wrong but outcome-correct rollouts can lead to hallucination and answer-copying, severely undermining the model's generalization and robustness. To address this, we incorporate a Contrastive Learning mechanism into the Policy Optimization (CLIPO) to generalize the RLVR process. By optimizing a contrastive loss over successful rollouts, CLIPO steers the LLM to capture the invariant structure shared across correct reasoning paths. This provides a more robust ...

---

## 314. Lost in the Middle at Birth: An Exact Theory of Transformer Position 偏见

**原标题**: Lost in the Middle at Birth: An Exact Theory of Transformer Position Bias

**作者**: Borun D Chowdhury
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10123v1

**中文摘要**:
> arXiv:2603.10123v1 Announce Type: cross 
摘要: The ``Lost in the Middle'' phenomenon -- a U-shaped 性能 curve where LLMs retrieve well from the beginning and end of a context but fail in the middle -- is widely attributed to learned Softmax artifacts or the distance-decay of positional encodings like RoPE. This 论文 makes a single, precise claim: \emph{the U-shape is already present at initialization, before any 训练 or positional encoding takes effect.} It is an inherent geometric property of the 因果 decoder with residual connections.
  We 模型 multi-layer 因果 注意力 as iterated powers of the Ces\`{a}ro matrix and derive the exact closed-form influence density in the continuous limit. 因果 masking forces a logarithmic divergence of 梯度 influence at the start of the prompt (the Primacy Tail), while residual...

**Original Abstract**:
> arXiv:2603.10123v1 Announce Type: cross 
Abstract: The ``Lost in the Middle'' phenomenon -- a U-shaped performance curve where LLMs retrieve well from the beginning and end of a context but fail in the middle -- is widely attributed to learned Softmax artifacts or the distance-decay of positional encodings like RoPE. This paper makes a single, precise claim: \emph{the U-shape is already present at initialization, before any training or positional encoding takes effect.} It is an inherent geometric property of the causal decoder with residual connections.
  We model multi-layer causal attention as iterated powers of the Ces\`{a}ro matrix and derive the exact closed-form influence density in the continuous limit. Causal masking forces a logarithmic divergence of gradient influence at the sta...

---

## 315. AR-VLA: True Autoregressive 动作 Expert for Vision-Language-动作 Models

**原标题**: AR-VLA: True Autoregressive Action Expert for Vision-Language-Action Models

**作者**: Yutong Hu, Jan-Nico Zaech, Nikolay Nikolov, Yuanqi Yao, Sombit Dey, Giuliano Albanese, Renaud Detry, Luc Van Gool, Danda Paudel
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10126v1

**中文摘要**:
> arXiv:2603.10126v1 Announce Type: cross 
摘要: We propose a standalone autoregressive (AR) 动作 Expert that generates actions as a continuous 因果 sequence while conditioning on refreshable vision-language prefixes. In contrast to existing Vision-Language-动作 (VLA) models and diffusion policies that reset temporal context with each new 观测 and predict actions reactively, our 动作 Expert maintains its own history through a long-lived 内存 and is inherently context-aware. This structure addresses the frequency mismatch between fast 控制 and slow 推理, enabling 高效 independent pretraining of kinematic syntax and modular integration with heavy perception backbones, naturally ensuring spatio-temporally consistent 动作 生成 across frames. To synchronize these asynchronous hybrid V-L-A modalities, we utilize a re-anc...

**Original Abstract**:
> arXiv:2603.10126v1 Announce Type: cross 
Abstract: We propose a standalone autoregressive (AR) Action Expert that generates actions as a continuous causal sequence while conditioning on refreshable vision-language prefixes. In contrast to existing Vision-Language-Action (VLA) models and diffusion policies that reset temporal context with each new observation and predict actions reactively, our Action Expert maintains its own history through a long-lived memory and is inherently context-aware. This structure addresses the frequency mismatch between fast control and slow reasoning, enabling efficient independent pretraining of kinematic syntax and modular integration with heavy perception backbones, naturally ensuring spatio-temporally consistent action generation across frames. To synchroni...

---

## 316. The 生成-识别 Asymmetry: Six Dimensions of a Fundamental Divide in Formal Language Theory

**原标题**: The Generation-Recognition Asymmetry: Six Dimensions of a Fundamental Divide in Formal Language Theory

**作者**: Romain Peyrichou
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10139v1

**中文摘要**:
> arXiv:2603.10139v1 Announce Type: cross 
摘要: Every formal grammar defines a language and can in principle be used in three ways: to generate strings (production), to recognize them (parsing), or -- given only examples -- to infer the grammar itself (grammar induction). 生成 and 识别 are extensionally equivalent -- they characterize the same set -- but operationally asymmetric in multiple independent ways. 推理 is a qualitatively harder problem: it does not have access to a known grammar. Despite the centrality of this triad to compiler design, natural language processing, and formal language theory, no survey has treated it as a unified, multidimensional phenomenon. We identify six dimensions along which 生成 and 识别 diverge: computational complexity, ambiguity, directionality, information availabi...

**Original Abstract**:
> arXiv:2603.10139v1 Announce Type: cross 
Abstract: Every formal grammar defines a language and can in principle be used in three ways: to generate strings (production), to recognize them (parsing), or -- given only examples -- to infer the grammar itself (grammar induction). Generation and recognition are extensionally equivalent -- they characterize the same set -- but operationally asymmetric in multiple independent ways. Inference is a qualitatively harder problem: it does not have access to a known grammar. Despite the centrality of this triad to compiler design, natural language processing, and formal language theory, no survey has treated it as a unified, multidimensional phenomenon. We identify six dimensions along which generation and recognition diverge: computational complexity, ...

---

## 317. Mashup 学习: Faster Finetuning by Remixing Past Checkpoints

**原标题**: Mashup Learning: Faster Finetuning by Remixing Past Checkpoints

**作者**: Sofia Maria Lo Cicero Vaina, Artem Chumachenko, Max Ryabinin
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10156v1

**中文摘要**:
> arXiv:2603.10156v1 Announce Type: cross 
摘要: Finetuning on domain-specific data is a well-established 方法 for enhancing 大语言模型 性能 on downstream tasks. 训练 on each 数据集 produces a new set of 模型 weights, resulting in a multitude of checkpoints saved in-house or on open-source platforms. However, these 训练 artifacts are rarely reused for subsequent experiments despite containing improved 模型 abilities for potentially similar tasks. In this 论文, we propose Mashup 学习, a simple 方法 to leverage the outputs of prior 训练 runs to enhance 模型 adaptation to new tasks. Our procedure identifies the most relevant historical checkpoints for a 目标 数据集, aggregates them with 模型 merging, and uses the 结果 as an improved initialization for 训练. Across 8 standard 大语言模型 benchmarks, four models, and two collections of source c...

**Original Abstract**:
> arXiv:2603.10156v1 Announce Type: cross 
Abstract: Finetuning on domain-specific data is a well-established method for enhancing LLM performance on downstream tasks. Training on each dataset produces a new set of model weights, resulting in a multitude of checkpoints saved in-house or on open-source platforms. However, these training artifacts are rarely reused for subsequent experiments despite containing improved model abilities for potentially similar tasks. In this paper, we propose Mashup Learning, a simple method to leverage the outputs of prior training runs to enhance model adaptation to new tasks. Our procedure identifies the most relevant historical checkpoints for a target dataset, aggregates them with model merging, and uses the result as an improved initialization for training...

---

## 318. MCP-in-SoS: Risk assessment 框架 for open-source MCP servers

**原标题**: MCP-in-SoS: Risk assessment framework for open-source MCP servers

**作者**: Pratyay Kumar, Miguel Antonio Guirao Aguilera, Srikathyayani Srikanteswara, Satyajayant Misra, Abu Saleh Md Tayeen
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10194v1

**中文摘要**:
> arXiv:2603.10194v1 Announce Type: cross 
摘要: 模型 Context Protocol (MCP) servers have rapidly emerged over the past year as a widely adopted way to enable Large Language 模型 (大语言模型) agents to access 动态, real-world tools. As MCP servers proliferate and become easy to adopt via open-source releases, understanding their security risks becomes essential for dependable production 智能体 deployments. Recent work has developed MCP threat taxonomies, proposed mitigations, and demonstrated practical attacks. However, to the best of our knowledge, no prior study has conducted a systematic, large-scale assessment of weaknesses in open-source MCP servers. Motivated by this gap, we apply 静态 代码 analysis to identify Common Weakness Enumeration (CWE) weaknesses and map them to common attack patterns and threat ...

**Original Abstract**:
> arXiv:2603.10194v1 Announce Type: cross 
Abstract: Model Context Protocol (MCP) servers have rapidly emerged over the past year as a widely adopted way to enable Large Language Model (LLM) agents to access dynamic, real-world tools. As MCP servers proliferate and become easy to adopt via open-source releases, understanding their security risks becomes essential for dependable production agent deployments. Recent work has developed MCP threat taxonomies, proposed mitigations, and demonstrated practical attacks. However, to the best of our knowledge, no prior study has conducted a systematic, large-scale assessment of weaknesses in open-source MCP servers. Motivated by this gap, we apply static code analysis to identify Common Weakness Enumeration (CWE) weaknesses and map them to common atta...

---

## 319. Adaptive Activation Cancellation for Hallucination Mitigation in Large Language Models

**原标题**: Adaptive Activation Cancellation for Hallucination Mitigation in Large Language Models

**作者**: Eric Yocam, Varghese Vaidyan, Gurcan Comert, Paris Kalathas, Yong Wang, Judith L. Mwakalonge
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10195v1

**中文摘要**:
> arXiv:2603.10195v1 Announce Type: cross 
摘要: Large Language Models frequently generate fluent but factually incorrect text. We propose Adaptive Activation Cancellation (AAC), a 实时 推理-time 框架 that treats hallucination-associated 神经 activations as structured interference within the Transformer residual stream, drawing an explicit analogy to classical adaptive noise cancellation from signal processing. The 框架 identifies Hallucination Nodes (H-Nodes) via layer-wise linear probing and suppresses them using a confidence-weighted 前向 hook during auto-regressive 生成 -- requiring no external knowledge, no fine-tuning, and no additional 推理 passes. Evaluated across OPT-125M, Phi-3-mini, and LLaMA 3-8B on TruthfulQA and HaluEval, the 实时 hook is the only intervention that consistently improves downstream...

**Original Abstract**:
> arXiv:2603.10195v1 Announce Type: cross 
Abstract: Large Language Models frequently generate fluent but factually incorrect text. We propose Adaptive Activation Cancellation (AAC), a real-time inference-time framework that treats hallucination-associated neural activations as structured interference within the transformer residual stream, drawing an explicit analogy to classical adaptive noise cancellation from signal processing. The framework identifies Hallucination Nodes (H-Nodes) via layer-wise linear probing and suppresses them using a confidence-weighted forward hook during auto-regressive generation -- requiring no external knowledge, no fine-tuning, and no additional inference passes. Evaluated across OPT-125M, Phi-3-mini, and LLaMA 3-8B on TruthfulQA and HaluEval, the real-time ho...

---

## 320. Multilingual AI-Driven Password Strength Estimation with Similarity-Based 检测

**原标题**: Multilingual AI-Driven Password Strength Estimation with Similarity-Based Detection

**作者**: Nikitha M. Palaniappan, Ying He
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10217v1

**中文摘要**:
> arXiv:2603.10217v1 Announce Type: cross 
摘要: Considering the rise of cyberattacks incidents worldwide, the need to ensure stronger passwords is necessary. Developing a password strength meter (PSM) can help users create stronger passwords when creating an account on an 在线 platform. This research aimed to explore whether incorporating a non-English 训练 数据集 (specifically Indian) can improve the 性能 of a PSM. Findings show that PSMs can be improved by utilising 学习 of words from other languages. Another contribution of the research was to compare and provide an analysis of AI generated data (specifically by ChatGPT) and PassGAN (existing 状态-of-the-art 模型), proving that PassGAN-like tools may no longer be needed as the 性能 is higher using AI generated data. To further strengthen 检测, a Jaro similar...

**Original Abstract**:
> arXiv:2603.10217v1 Announce Type: cross 
Abstract: Considering the rise of cyberattacks incidents worldwide, the need to ensure stronger passwords is necessary. Developing a password strength meter (PSM) can help users create stronger passwords when creating an account on an online platform. This research aimed to explore whether incorporating a non-English training dataset (specifically Indian) can improve the performance of a PSM. Findings show that PSMs can be improved by utilising learning of words from other languages. Another contribution of the research was to compare and provide an analysis of AI generated data (specifically by ChatGPT) and PassGAN (existing state-of-the-art model), proving that PassGAN-like tools may no longer be needed as the performance is higher using AI genera...

---

## 321. A Diffusion Analysis of 策略 梯度 for Stochastic Bandits

**原标题**: A Diffusion Analysis of Policy Gradient for Stochastic Bandits

**作者**: Tor Lattimore
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10219v1

**中文摘要**:
> arXiv:2603.10219v1 Announce Type: cross 
摘要: We study a continuous-time diffusion approximation of 策略 梯度 for $k$-armed stochastic bandits. We prove that with a 学习 rate $\eta = O(\Delta^2/\log(n))$ the regret is $O(k \log(k) \log(n) / \eta)$ where $n$ is the 视野 and $\Delta$ the minimum gap. Moreover, we construct an instance with only logarithmically many arms for which the regret is linear unless $\eta = O(\Delta^2)$.

**Original Abstract**:
> arXiv:2603.10219v1 Announce Type: cross 
Abstract: We study a continuous-time diffusion approximation of policy gradient for $k$-armed stochastic bandits. We prove that with a learning rate $\eta = O(\Delta^2/\log(n))$ the regret is $O(k \log(k) \log(n) / \eta)$ where $n$ is the horizon and $\Delta$ the minimum gap. Moreover, we construct an instance with only logarithmically many arms for which the regret is linear unless $\eta = O(\Delta^2)$.

---

## 322. 学习 from Radio using Variational Quantum RF Sensing

**原标题**: Learning from Radio using Variational Quantum RF Sensing

**作者**: Ivana Nikoloska
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10239v1

**中文摘要**:
> arXiv:2603.10239v1 Announce Type: cross 
摘要: In modern wireless networks, radio channels serve a dual 角色. Whilst their primary function is to carry bits of information from a transmitter to a receiver, the intrinsic sensitivity of transmitted signals to the physical structure of the 环境 makes the channel a powerful source of knowledge about the world. In this 论文, we consider an 智能体 that learns about its 环境 using a quantum sensing probe, optimised using a quantum circuit, which interacts with the radio-frequency (RF) electromagnetic field. We use data obtained from a ray-tracer to train the quantum circuit and 学习 模型 and we provide extensive experiments under realistic conditions on a localisation task. We show that using quantum sensors to learn from radio signals can enable intelligent syst...

**Original Abstract**:
> arXiv:2603.10239v1 Announce Type: cross 
Abstract: In modern wireless networks, radio channels serve a dual role. Whilst their primary function is to carry bits of information from a transmitter to a receiver, the intrinsic sensitivity of transmitted signals to the physical structure of the environment makes the channel a powerful source of knowledge about the world. In this paper, we consider an agent that learns about its environment using a quantum sensing probe, optimised using a quantum circuit, which interacts with the radio-frequency (RF) electromagnetic field. We use data obtained from a ray-tracer to train the quantum circuit and learning model and we provide extensive experiments under realistic conditions on a localisation task. We show that using quantum sensors to learn from r...

---

## 323. Intrinsic Numerical 鲁棒性 and Fault Tolerance in a Neuromorphic 算法 for Scientific Computing

**原标题**: Intrinsic Numerical Robustness and Fault Tolerance in a Neuromorphic Algorithm for Scientific Computing

**作者**: Bradley H. Theilman, James B. Aimone
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10246v1

**中文摘要**:
> arXiv:2603.10246v1 Announce Type: cross 
摘要: The potential for neuromorphic computing to provide intrinsic fault tolerance has long been speculated, but the brain's 鲁棒性 in neuromorphic applications has yet to be demonstrated. Here, we show that a previously described, natively spiking neuromorphic 算法 for solving partial differential equations is intrinsically tolerant to structural perturbations in the form of ablated neurons and dropped spikes. The tolerance band for these perturbations is large: we find that as many as 32 percent of the neurons and up to 90 percent of the spikes may be entirely dropped before a significant degradation in the accuracy results. Furthermore, this 鲁棒性 is tunable through structural hyperparameters. This work demonstrates that the specific brain-like inspirati...

**Original Abstract**:
> arXiv:2603.10246v1 Announce Type: cross 
Abstract: The potential for neuromorphic computing to provide intrinsic fault tolerance has long been speculated, but the brain's robustness in neuromorphic applications has yet to be demonstrated. Here, we show that a previously described, natively spiking neuromorphic algorithm for solving partial differential equations is intrinsically tolerant to structural perturbations in the form of ablated neurons and dropped spikes. The tolerance band for these perturbations is large: we find that as many as 32 percent of the neurons and up to 90 percent of the spikes may be entirely dropped before a significant degradation in the accuracy results. Furthermore, this robustness is tunable through structural hyperparameters. This work demonstrates that the sp...

---

## 324. DUCTILE: Agentic 大语言模型 Orchestration of Engineering Analysis in Product Development Practice

**原标题**: DUCTILE: Agentic LLM Orchestration of Engineering Analysis in Product Development Practice

**作者**: Alejandro Pradas-Gomez, Arindam Brahma, Ola Isaksson
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10249v1

**中文摘要**:
> arXiv:2603.10249v1 Announce Type: cross 
摘要: Engineering analysis automation in product development relies on rigid interfaces between tools, data formats and documented processes. When these interfaces change, as they routinely do as the product evolves in the engineering ecosystem, the automation support breaks. This 论文 presents a DUCTILE (Delegated, User-有监督 Coordination of Tool- and document-Integrated 大语言模型-Enabled) agentic orchestration, an 方案 for developing, executing and evaluating 大语言模型-based agentic automation support of engineering analysis tasks. The 方案 separates adaptive orchestration, performed by the 大语言模型 智能体, from deterministic execution, performed by verified engineering tools. The 智能体 interprets documented design practices, inspects input data and adapts the processing p...

**Original Abstract**:
> arXiv:2603.10249v1 Announce Type: cross 
Abstract: Engineering analysis automation in product development relies on rigid interfaces between tools, data formats and documented processes. When these interfaces change, as they routinely do as the product evolves in the engineering ecosystem, the automation support breaks. This paper presents a DUCTILE (Delegated, User-supervised Coordination of Tool- and document-Integrated LLM-Enabled) agentic orchestration, an approach for developing, executing and evaluating LLM-based agentic automation support of engineering analysis tasks. The approach separates adaptive orchestration, performed by the LLM agent, from deterministic execution, performed by verified engineering tools. The agent interprets documented design practices, inspects input data a...

---

## 325. Taming Score-Based Denoisers in ADMM: A Convergent Plug-and-Play 框架

**原标题**: Taming Score-Based Denoisers in ADMM: A Convergent Plug-and-Play Framework

**作者**: Rajesh Shrestha, Xiao Fu
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10281v1

**中文摘要**:
> arXiv:2603.10281v1 Announce Type: cross 
摘要: While score-based 生成式 models have emerged as powerful priors for solving inverse problems, directly integrating them into 优化 algorithms such as ADMM remains nontrivial. Two central challenges arise: i) the mismatch between the noisy data manifolds used to train the score functions and the geometry of ADMM iterates, especially due to the influence of dual variables, and ii) the lack of convergence understanding when ADMM is equipped with score-based denoisers. To address the manifold mismatch issue, we propose ADMM plug-and-play (ADMM-PnP) with the AC-DC denoiser, a new 框架 that embeds a three-stage denoiser into ADMM: (1) auto-correction (AC) via additive Gaussian noise, (2) directional correction (DC) using conditional Langevin dynamics, and (3)...

**Original Abstract**:
> arXiv:2603.10281v1 Announce Type: cross 
Abstract: While score-based generative models have emerged as powerful priors for solving inverse problems, directly integrating them into optimization algorithms such as ADMM remains nontrivial. Two central challenges arise: i) the mismatch between the noisy data manifolds used to train the score functions and the geometry of ADMM iterates, especially due to the influence of dual variables, and ii) the lack of convergence understanding when ADMM is equipped with score-based denoisers. To address the manifold mismatch issue, we propose ADMM plug-and-play (ADMM-PnP) with the AC-DC denoiser, a new framework that embeds a three-stage denoiser into ADMM: (1) auto-correction (AC) via additive Gaussian noise, (2) directional correction (DC) using conditio...

---

## 326. Conversational AI-Enhanced 探索 系统 to Query Large-Scale Digitised Collections of Natural History Museums

**原标题**: Conversational AI-Enhanced Exploration System to Query Large-Scale Digitised Collections of Natural History Museums

**作者**: Yiyuan Wang, Andrew Johnston, Zo\"e Sadokierski, Rhiannon Stephens, Shane T. Ahyong
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10285v1

**中文摘要**:
> arXiv:2603.10285v1 Announce Type: cross 
摘要: Recent digitisation efforts in natural history museums have produced large volumes of collection data, yet their scale and scientific complexity often hinder public access and understanding. Conventional data management tools, such as databases, restrict 探索 through keyword-based 搜索 or require specialised schema knowledge. This 论文 presents a 系统 design that uses conversational AI to query nearly 1.7 million digitised specimen records from the life-science collections of the Australian Museum. Designed and developed through a human-centred design process, the 系统 contains an interactive map for 视觉-spatial 探索 and a natural-language conversational 智能体 that retrieves detailed specimen data and answers collection-specific questions. The 系统 leverages fun...

**Original Abstract**:
> arXiv:2603.10285v1 Announce Type: cross 
Abstract: Recent digitisation efforts in natural history museums have produced large volumes of collection data, yet their scale and scientific complexity often hinder public access and understanding. Conventional data management tools, such as databases, restrict exploration through keyword-based search or require specialised schema knowledge. This paper presents a system design that uses conversational AI to query nearly 1.7 million digitised specimen records from the life-science collections of the Australian Museum. Designed and developed through a human-centred design process, the system contains an interactive map for visual-spatial exploration and a natural-language conversational agent that retrieves detailed specimen data and answers collec...

---

## 327. Simulation-in-the-推理 (SiR): A Conceptual 框架 for Empirically Grounded AI in 自主 Transportation

**原标题**: Simulation-in-the-Reasoning (SiR): A Conceptual Framework for Empirically Grounded AI in Autonomous Transportation

**作者**: Wuping Xin
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10294v1

**中文摘要**:
> arXiv:2603.10294v1 Announce Type: cross 
摘要: Large Language Models (LLMs) have advanced 推理 through techniques like Chain-of-Thought (CoT). However, their 推理 largely re-mains textual and hypothetical, lacking empirical grounding in complex, 动态 domains like transportation. This 论文 introduces Simulation-in-the-推理 (SiR), a novel conceptual 框架 that embeds domain-specific simulators directly into the 大语言模型 推理 loop. By treating intermediate 推理 steps as executable simulation experiments, SiR transforms 大语言模型 推理 from narrative plausibility into a falsifiable, hypothesis-simulate-analyze workflow. We discuss applications, where 大语言模型 can formulate Intelligent Transport 系统 (ITS) strategy hypotheses, invoke a traffic simulator via the 模型 Context Protocol (MCP), evaluate results under different demand ...

**Original Abstract**:
> arXiv:2603.10294v1 Announce Type: cross 
Abstract: Large Language Models (LLMs) have advanced reasoning through techniques like Chain-of-Thought (CoT). However, their reasoning largely re-mains textual and hypothetical, lacking empirical grounding in complex, dynamic domains like transportation. This paper introduces Simulation-in-the-Reasoning (SiR), a novel conceptual framework that embeds domain-specific simulators directly into the LLM reasoning loop. By treating intermediate reasoning steps as executable simulation experiments, SiR transforms LLM reasoning from narrative plausibility into a falsifiable, hypothesis-simulate-analyze workflow. We discuss applications, where LLM can formulate Intelligent Transport System (ITS) strategy hypotheses, invoke a traffic simulator via the Model ...

---

## 328. Is this Idea Novel? An Automated 基准 for Judgment of Research Ideas

**原标题**: Is this Idea Novel? An Automated Benchmark for Judgment of Research Ideas

**作者**: Tim Schopf, Michael F\"arber
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10303v1

**中文摘要**:
> arXiv:2603.10303v1 Announce Type: cross 
摘要: Judging the novelty of research ideas is crucial for advancing science, enabling the identification of unexplored directions, and ensuring contributions meaningfully extend existing knowledge rather than reiterate minor variations. However, given the exponential growth of scientific literature, manually judging the novelty of research ideas through literature reviews is labor-intensive, subjective, and infeasible at scale. Therefore, recent efforts have proposed automated approaches for research idea novelty judgment. Yet, 评估 of these approaches remains largely inconsistent and is typically based on non-standardized human evaluations, hindering large-scale, comparable evaluations. To address this, we introduce RINoBench, the first comprehensive ...

**Original Abstract**:
> arXiv:2603.10303v1 Announce Type: cross 
Abstract: Judging the novelty of research ideas is crucial for advancing science, enabling the identification of unexplored directions, and ensuring contributions meaningfully extend existing knowledge rather than reiterate minor variations. However, given the exponential growth of scientific literature, manually judging the novelty of research ideas through literature reviews is labor-intensive, subjective, and infeasible at scale. Therefore, recent efforts have proposed automated approaches for research idea novelty judgment. Yet, evaluation of these approaches remains largely inconsistent and is typically based on non-standardized human evaluations, hindering large-scale, comparable evaluations. To address this, we introduce RINoBench, the first ...

---

## 329. PC-Diffuser: Path-Consistent Capsule CBF Safety Filtering for Diffusion-Based 轨迹 Planner

**原标题**: PC-Diffuser: Path-Consistent Capsule CBF Safety Filtering for Diffusion-Based Trajectory Planner

**作者**: Eugene Ku, Yiwei Lyu
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10330v1

**中文摘要**:
> arXiv:2603.10330v1 Announce Type: cross 
摘要: 自主 driving in complex traffic requires planners that generalize beyond hand-crafted rules, motivating data-driven approaches that learn behavior from expert demonstrations. Diffusion-based 轨迹 planners have recently shown strong closed-loop 性能 by iteratively denoising a full-视野 plan, but they remain difficult to certify and can fail catastrophically in rare or 分布外 scenarios. To address this challenge, we present PC-Diffuser, a safety augmentation 框架 that embeds a certifiable, path-consistent barrier-function structure directly into the denoising loop of diffusion 规划. The key idea is to make safety an intrinsic part of 轨迹 生成 rather than a post-hoc fix: we enforce 前向 invariance along the rollout while preserving the diffusion 模型's intended path geo...

**Original Abstract**:
> arXiv:2603.10330v1 Announce Type: cross 
Abstract: Autonomous driving in complex traffic requires planners that generalize beyond hand-crafted rules, motivating data-driven approaches that learn behavior from expert demonstrations. Diffusion-based trajectory planners have recently shown strong closed-loop performance by iteratively denoising a full-horizon plan, but they remain difficult to certify and can fail catastrophically in rare or out-of-distribution scenarios. To address this challenge, we present PC-Diffuser, a safety augmentation framework that embeds a certifiable, path-consistent barrier-function structure directly into the denoising loop of diffusion planning. The key idea is to make safety an intrinsic part of trajectory generation rather than a post-hoc fix: we enforce forw...

---

## 330. Does 推理 Make 搜索 More Fair? Comparing 公平性 in 推理 and Non-推理 Rerankers

**原标题**: Does Reasoning Make Search More Fair? Comparing Fairness in Reasoning and Non-Reasoning Rerankers

**作者**: Saron Samuel, Benjamin Van Durme, Eugene Yang
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10332v1

**中文摘要**:
> arXiv:2603.10332v1 Announce Type: cross 
摘要: While 推理 rerankers, such as Rank1, have demonstrated strong abilities in improving ranking relevance, it is unclear how they perform on other 检索 qualities such as 公平性. We conduct the first systematic comparison of 公平性 between 推理 and non-推理 rerankers. Using the TREC 2022 Fair Ranking Track 数据集, we evaluate six reranking models across multiple 检索 settings and demographic attributes. Our findings demonstrate 推理 neither improve nor harm 公平性 compared to non-推理 approaches. Our 公平性 metric, 注意力-Weighted Rank 公平性 (AWRF) remained stable (0.33-0.35) across all models, even as relevance varies substantially (nDCG 0.247-1.000). Demographic breakdown analysis revealed 公平性 gaps for geographic attributes regardless of 模型 架构. These results indicate that 未来工作 in ...

**Original Abstract**:
> arXiv:2603.10332v1 Announce Type: cross 
Abstract: While reasoning rerankers, such as Rank1, have demonstrated strong abilities in improving ranking relevance, it is unclear how they perform on other retrieval qualities such as fairness. We conduct the first systematic comparison of fairness between reasoning and non-reasoning rerankers. Using the TREC 2022 Fair Ranking Track dataset, we evaluate six reranking models across multiple retrieval settings and demographic attributes. Our findings demonstrate reasoning neither improve nor harm fairness compared to non-reasoning approaches. Our fairness metric, Attention-Weighted Rank Fairness (AWRF) remained stable (0.33-0.35) across all models, even as relevance varies substantially (nDCG 0.247-1.000). Demographic breakdown analysis revealed fa...

---

## 331. Overcoming 视觉 Clutter in Vision Language 动作 Models via Concept-Gated 视觉 Distillation

**原标题**: Overcoming Visual Clutter in Vision Language Action Models via Concept-Gated Visual Distillation

**作者**: Sangmim Song, Sarath Kodagoda, Marc Carmichael, Karthick Thiyagarajan
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10340v1

**中文摘要**:
> arXiv:2603.10340v1 Announce Type: cross 
摘要: Vision-Language-动作 (VLA) models demonstrate impressive 零样本 泛化 but frequently suffer from a "Precision-推理 Gap" in cluttered environments. This failure is driven by background-induced 特征 dilution, where high-frequency semantic noise corrupts the geometric grounding required for precise manipulation. To bridge this gap, we propose Concept-Gated 视觉 Distillation (CGVD), a 训练-free, 模型-agnostic 推理 框架 that stabilizes VLA policies. CGVD operates by parsing instructions into safe and distractor sets, utilizing a two-layer 目标 refinement process--combining cross-validation and spatial disambiguation--to explicitly penalize false positives and isolate genuine manipulation targets. We then process the scene via Fourier-based inpainting, generating a clean 观测 ...

**Original Abstract**:
> arXiv:2603.10340v1 Announce Type: cross 
Abstract: Vision-Language-Action (VLA) models demonstrate impressive zero-shot generalization but frequently suffer from a "Precision-Reasoning Gap" in cluttered environments. This failure is driven by background-induced feature dilution, where high-frequency semantic noise corrupts the geometric grounding required for precise manipulation. To bridge this gap, we propose Concept-Gated Visual Distillation (CGVD), a training-free, model-agnostic inference framework that stabilizes VLA policies. CGVD operates by parsing instructions into safe and distractor sets, utilizing a two-layer target refinement process--combining cross-validation and spatial disambiguation--to explicitly penalize false positives and isolate genuine manipulation targets. We then...

---

## 332. Federated Active 学习 Under Extreme Non-IID and Global Class Imbalance

**原标题**: Federated Active Learning Under Extreme Non-IID and Global Class Imbalance

**作者**: Chen-Chen Zong, Sheng-Jun Huang
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10341v1

**中文摘要**:
> arXiv:2603.10341v1 Announce Type: cross 
摘要: Federated active 学习 (FAL) seeks to reduce annotation cost under 隐私 constraints, yet its effectiveness degrades in realistic settings with severe global class imbalance and highly heterogeneous clients. We conduct a systematic study of query-模型 选择 in FAL and uncover a central insight: the 模型 that achieves more class-balanced 采样, especially for minority classes, consistently leads to better final 性能. Moreover, global-模型 querying is beneficial only when the global distribution is highly imbalanced and 客户端 data are relatively homogeneous; otherwise, the local 模型 is preferable. Based on these findings, we propose FairFAL, an adaptive class-fair FAL 框架. FairFAL (1) infers global imbalance and local-global divergence via lightweight prediction discrepa...

**Original Abstract**:
> arXiv:2603.10341v1 Announce Type: cross 
Abstract: Federated active learning (FAL) seeks to reduce annotation cost under privacy constraints, yet its effectiveness degrades in realistic settings with severe global class imbalance and highly heterogeneous clients. We conduct a systematic study of query-model selection in FAL and uncover a central insight: the model that achieves more class-balanced sampling, especially for minority classes, consistently leads to better final performance. Moreover, global-model querying is beneficial only when the global distribution is highly imbalanced and client data are relatively homogeneous; otherwise, the local model is preferable. Based on these findings, we propose FairFAL, an adaptive class-fair FAL framework. FairFAL (1) infers global imbalance an...

---

## 333. 动态 Knowledge Fusion for Multi-Domain Dialogue 状态 Tracking

**原标题**: Dynamic Knowledge Fusion for Multi-Domain Dialogue State Tracking

**作者**: Haoxiang Su, Ruiyu Fang, Liting Jiang, Xiaomeng Huang, Shuangyong Song
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10367v1

**中文摘要**:
> arXiv:2603.10367v1 Announce Type: cross 
摘要: The 性能 of task-oriented dialogue models is strongly tied to how well they track dialogue states, which records and updates user information across multi-turn interactions. However, current multi-domain DST encounters two key challenges: the difficulty of effectively modeling dialogue history and the limited availability of annotated data, both of which hinder 模型 性能. To tackle the aforementioned problems, we develop a 动态 knowledge fusion 框架 applicable to multi-domain DST. The 模型 operates in two stages: first, an encoder-only 网络 trained with 对比 学习 encodes dialogue history and candidate slots, selecting relevant slots based on correlation scores; second, 动态 knowledge fusion leverages the structured information of selected slots as contextual prompt...

**Original Abstract**:
> arXiv:2603.10367v1 Announce Type: cross 
Abstract: The performance of task-oriented dialogue models is strongly tied to how well they track dialogue states, which records and updates user information across multi-turn interactions. However, current multi-domain DST encounters two key challenges: the difficulty of effectively modeling dialogue history and the limited availability of annotated data, both of which hinder model performance. To tackle the aforementioned problems, we develop a dynamic knowledge fusion framework applicable to multi-domain DST. The model operates in two stages: first, an encoder-only network trained with contrastive learning encodes dialogue history and candidate slots, selecting relevant slots based on correlation scores; second, dynamic knowledge fusion leverage...

---

## 334. 少样本 Adaptation to Non-Stationary Environments via 隐变量 Trend 嵌入 for 机器人

**原标题**: Few-Shot Adaptation to Non-Stationary Environments via Latent Trend Embedding for Robotics

**作者**: Yasuyuki Fujii (College of Information Science and Engineering, Ritsumeikan University, Osaka, Japan), Emika Kameda (College of Information Science and Engineering, Ritsumeikan University, Osaka, Japan), Hiroki Fukada (Production and Technology Department, NIPPN CORPORATION, Tokyo, Japan), Yoshiki Mori (University of Osaka, Osaka, Japan), Tadashi Matsuo (National Institute of Technology, Ichinoseki College, Iwate, Japan), Nobutaka Shimada (College of Information Science and Engineering, Ritsumeikan University, Osaka, Japan)
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10373v1

**中文摘要**:
> arXiv:2603.10373v1 Announce Type: cross 
摘要: Robotic systems operating in real-world environments often suffer from concept shift, where the input-output relationship changes due to 隐变量 environmental factors that are not directly observable. Conventional adaptation methods update 模型 parameters, which may cause catastrophic forgetting and incur high computational cost. This 论文 proposes a 隐变量 Trend ID-based 框架 for 少样本 adaptation in non-stationary environments. Instead of modifying 模型 weights, a low-dimensional environmental 状态, referred to as the Trend ID, is estimated via 反向传播 while the 模型 parameters remain fixed. To prevent overfitting caused by per-sample 隐变量 variables, we introduce temporal 正则化 and a 状态 转移 模型 that enforces smooth 进化 of the 隐变量 space. Experiments on a quantitative food gr...

**Original Abstract**:
> arXiv:2603.10373v1 Announce Type: cross 
Abstract: Robotic systems operating in real-world environments often suffer from concept shift, where the input-output relationship changes due to latent environmental factors that are not directly observable. Conventional adaptation methods update model parameters, which may cause catastrophic forgetting and incur high computational cost. This paper proposes a latent Trend ID-based framework for few-shot adaptation in non-stationary environments. Instead of modifying model weights, a low-dimensional environmental state, referred to as the Trend ID, is estimated via backpropagation while the model parameters remain fixed. To prevent overfitting caused by per-sample latent variables, we introduce temporal regularization and a state transition model t...

---

## 335. Reactive Writers: How Co-Writing with AI Changes How We Engage with Ideas

**原标题**: Reactive Writers: How Co-Writing with AI Changes How We Engage with Ideas

**作者**: Advait Bhat, Marianne Aubin Le Qu\'er\'e, Mor Naaman, Maurice Jakesch
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10374v1

**中文摘要**:
> arXiv:2603.10374v1 Announce Type: cross 
摘要: Emerging experimental evidence shows that writing with AI assistance can change both the views people express in writing and the opinions they hold afterwards. Yet, we lack substantive understanding of procedural and behavioral changes in co-writing with AI that underlie the observed opinion-shaping power of AI writing tools. We conducted a mixed-methods study, combining retrospective interviews with 19 participants about their AI co-writing experience with a quantitative analysis tracing engagement with ideas and opinions in 1{,}291 AI co-writing sessions. Our analysis shows that engaging with the AI's suggestions -- reading them and deciding whether to 接收 them -- becomes a central activity in the writing process, taking away from more traditio...

**Original Abstract**:
> arXiv:2603.10374v1 Announce Type: cross 
Abstract: Emerging experimental evidence shows that writing with AI assistance can change both the views people express in writing and the opinions they hold afterwards. Yet, we lack substantive understanding of procedural and behavioral changes in co-writing with AI that underlie the observed opinion-shaping power of AI writing tools. We conducted a mixed-methods study, combining retrospective interviews with 19 participants about their AI co-writing experience with a quantitative analysis tracing engagement with ideas and opinions in 1{,}291 AI co-writing sessions. Our analysis shows that engaging with the AI's suggestions -- reading them and deciding whether to accept them -- becomes a central activity in the writing process, taking away from mor...

---

## 336. 因果 Concept Graphs in 大语言模型 隐变量 Space for Stepwise 推理

**原标题**: Causal Concept Graphs in LLM Latent Space for Stepwise Reasoning

**作者**: Md Muntaqim Meherab, Noor Islam S. Mohammad, Faiza Feroz
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10377v1

**中文摘要**:
> arXiv:2603.10377v1 Announce Type: cross 
摘要: Sparse autoencoders can localize where concepts live in language models, but not how they interact during multi-step 推理. We propose 因果 Concept Graphs (CCG): a directed acyclic graph over sparse, 可解释 隐变量 features, where edges capture learned 因果 dependencies between concepts. We combine task-conditioned sparse autoencoders for concept discovery with DAGMA-style differentiable structure 学习 for graph recovery and introduce the 因果 Fidelity Score (CFS) to evaluate whether graph-guided interventions induce larger downstream effects than random ones. On ARC-Challenge, StrategyQA, and LogiQA with GPT-2 Medium, across five seeds ($n{=}15$ paired runs), CCG achieves $\CFS=5.654\pm0.625$, outperforming ROME-style tracing ($3.382\pm0.233$), SAE-only ranking ...

**Original Abstract**:
> arXiv:2603.10377v1 Announce Type: cross 
Abstract: Sparse autoencoders can localize where concepts live in language models, but not how they interact during multi-step reasoning. We propose Causal Concept Graphs (CCG): a directed acyclic graph over sparse, interpretable latent features, where edges capture learned causal dependencies between concepts. We combine task-conditioned sparse autoencoders for concept discovery with DAGMA-style differentiable structure learning for graph recovery and introduce the Causal Fidelity Score (CFS) to evaluate whether graph-guided interventions induce larger downstream effects than random ones. On ARC-Challenge, StrategyQA, and LogiQA with GPT-2 Medium, across five seeds ($n{=}15$ paired runs), CCG achieves $\CFS=5.654\pm0.625$, outperforming ROME-style ...

---

## 337. Optimal Expert-注意力 Allocation in Mixture-of-Experts: A 可扩展 Law for 动态 模型 Design

**原标题**: Optimal Expert-Attention Allocation in Mixture-of-Experts: A Scalable Law for Dynamic Model Design

**作者**: Junzhuo Li, Peijie Jiang, Changxin Tian, Jia Liu, Zhiqiang Zhang, Xuming Hu
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10379v1

**中文摘要**:
> arXiv:2603.10379v1 Announce Type: cross 
摘要: This 论文 presents a novel extension of 神经 scaling laws to Mixture-of-Experts (MoE) models, focusing on the optimal allocation of compute between expert and 注意力 sub-layers. As MoE architectures have emerged as an 高效 方法 for scaling 模型 capacity without proportionally increasing computation, determining the optimal expert-注意力 compute ratio becomes critical. We define the ratio $r$ as the fraction of total FLOPs per token dedicated to the expert layers versus the 注意力 layers, and explore how this ratio interacts with the overall compute budget and 模型 sparsity. Through extensive experiments with GPT-style MoE Transformers, we empirically find that the optimal ratio $r^*$ follows a power-law relationship with total compute and varies with sparsity. Our a...

**Original Abstract**:
> arXiv:2603.10379v1 Announce Type: cross 
Abstract: This paper presents a novel extension of neural scaling laws to Mixture-of-Experts (MoE) models, focusing on the optimal allocation of compute between expert and attention sub-layers. As MoE architectures have emerged as an efficient method for scaling model capacity without proportionally increasing computation, determining the optimal expert-attention compute ratio becomes critical. We define the ratio $r$ as the fraction of total FLOPs per token dedicated to the expert layers versus the attention layers, and explore how this ratio interacts with the overall compute budget and model sparsity. Through extensive experiments with GPT-style MoE Transformers, we empirically find that the optimal ratio $r^*$ follows a power-law relationship wi...

---

## 338. Safe 概率 规划 for Human-Robot Interaction using Conformal Risk 控制

**原标题**: Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control

**作者**: Jake Gonzales, Kazuki Mizuta, Karen Leung, Lillian J. Ratliff
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10392v1

**中文摘要**:
> arXiv:2603.10392v1 Announce Type: cross 
摘要: In this 论文, we present a novel 概率 safe 控制 框架 for human-robot interaction that combines 控制 barrier functions (CBFs) with conformal risk 控制 to provide formal safety guarantees while considering complex human behavior. The 方案 uses conformal risk 控制 to quantify and 控制 the prediction errors in CBF safety values and establishes formal guarantees on the probability of constraint satisfaction during interaction. We introduce an 算法 that dynamically adjusts the safety margins produced by conformal risk 控制 based on the current interaction context. Through experiments on human-robot navigation scenarios, we demonstrate that our 方案 significantly reduces collision rates and safety violations as compared to baseline methods while maintaining high success rates...

**Original Abstract**:
> arXiv:2603.10392v1 Announce Type: cross 
Abstract: In this paper, we present a novel probabilistic safe control framework for human-robot interaction that combines control barrier functions (CBFs) with conformal risk control to provide formal safety guarantees while considering complex human behavior. The approach uses conformal risk control to quantify and control the prediction errors in CBF safety values and establishes formal guarantees on the probability of constraint satisfaction during interaction. We introduce an algorithm that dynamically adjusts the safety margins produced by conformal risk control based on the current interaction context. Through experiments on human-robot navigation scenarios, we demonstrate that our approach significantly reduces collision rates and safety vio...

---

## 339. On the 学习 Dynamics of Two-layer Linear Networks with Label Noise SGD

**原标题**: On the Learning Dynamics of Two-layer Linear Networks with Label Noise SGD

**作者**: Tongcheng Zhang, Zhanpeng Zhou, Mingze Wang, Andi Han, Wei Huang, Taiji Suzuki, Junchi Yan
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10397v1

**中文摘要**:
> arXiv:2603.10397v1 Announce Type: cross 
摘要: One crucial factor behind the success of 深度 学习 lies in the implicit 偏见 induced by noise inherent in 梯度-based 训练 algorithms. Motivated by empirical observations that 训练 with noisy labels improves 模型 泛化, we delve into the underlying mechanisms behind stochastic 梯度 descent (SGD) with label noise. Focusing on a two-layer over-parameterized linear 网络, we analyze the 学习 dynamics of label noise SGD, unveiling a two-phase 学习 behavior. In \emph{Phase I}, the magnitudes of 模型 weights progressively diminish, and the 模型 escapes the lazy regime; enters the rich regime. In \emph{Phase II}, the alignment between 模型 weights and the ground-truth interpolator increases, and the 模型 eventually converges. Our analysis highlights the critical 角色 of label noise in dri...

**Original Abstract**:
> arXiv:2603.10397v1 Announce Type: cross 
Abstract: One crucial factor behind the success of deep learning lies in the implicit bias induced by noise inherent in gradient-based training algorithms. Motivated by empirical observations that training with noisy labels improves model generalization, we delve into the underlying mechanisms behind stochastic gradient descent (SGD) with label noise. Focusing on a two-layer over-parameterized linear network, we analyze the learning dynamics of label noise SGD, unveiling a two-phase learning behavior. In \emph{Phase I}, the magnitudes of model weights progressively diminish, and the model escapes the lazy regime; enters the rich regime. In \emph{Phase II}, the alignment between model weights and the ground-truth interpolator increases, and the model...

---

## 340. Designing Service Systems from Textual Evidence

**原标题**: Designing Service Systems from Textual Evidence

**作者**: Ruicheng Ao, Hongyu Chen, Siyang Gao, Hanwei Li, David Simchi-Levi
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10400v1

**中文摘要**:
> arXiv:2603.10400v1 Announce Type: cross 
摘要: Designing service systems requires selecting among alternative configurations -- choosing the best chatbot variant, the optimal routing 策略, or the most effective quality 控制 procedure. In many service systems, the primary evidence of 性能 quality is textual -- customer support transcripts, complaint narratives, compliance 审稿 reports -- rather than the scalar measurements assumed by classical 优化 methods. Large language models (LLMs) can read such textual evidence and produce standardized quality scores, but these automated judges exhibit systematic biases that vary across alternatives and 评估 instances. Human expert 审稿 remains 准确 but costly. We study how to identify the best service configuration with high confidence while minimizing expensive human ...

**Original Abstract**:
> arXiv:2603.10400v1 Announce Type: cross 
Abstract: Designing service systems requires selecting among alternative configurations -- choosing the best chatbot variant, the optimal routing policy, or the most effective quality control procedure. In many service systems, the primary evidence of performance quality is textual -- customer support transcripts, complaint narratives, compliance review reports -- rather than the scalar measurements assumed by classical optimization methods. Large language models (LLMs) can read such textual evidence and produce standardized quality scores, but these automated judges exhibit systematic biases that vary across alternatives and evaluation instances. Human expert review remains accurate but costly. We study how to identify the best service configuratio...

---

## 341. Effective 数据集 Distillation for Spatio-Temporal Forecasting with Bi-dimensional Compression

**原标题**: Effective Dataset Distillation for Spatio-Temporal Forecasting with Bi-dimensional Compression

**作者**: Taehyung Kwon, Yeonje Choi, Yeongho Kim, Kijung Shin
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10410v1

**中文摘要**:
> arXiv:2603.10410v1 Announce Type: cross 
摘要: Spatio-temporal time series are widely used in real-world applications, including traffic prediction and weather forecasting. They are sequences of observations over extensive periods and multiple locations, naturally represented as multidimensional data. Forecasting is a central task in spatio-temporal analysis, and numerous 深度 学习 methods have been developed to address it. However, as 数据集 sizes and 模型 complexities continue to grow in practice, 训练 深度 学习 models has become increasingly time- and resource-intensive. A promising solution to this challenge is 数据集 distillation, which synthesizes compact datasets that can effectively replace the original data for 模型 训练. Although successful in various domains, including time series analysis, existing 数据...

**Original Abstract**:
> arXiv:2603.10410v1 Announce Type: cross 
Abstract: Spatio-temporal time series are widely used in real-world applications, including traffic prediction and weather forecasting. They are sequences of observations over extensive periods and multiple locations, naturally represented as multidimensional data. Forecasting is a central task in spatio-temporal analysis, and numerous deep learning methods have been developed to address it. However, as dataset sizes and model complexities continue to grow in practice, training deep learning models has become increasingly time- and resource-intensive. A promising solution to this challenge is dataset distillation, which synthesizes compact datasets that can effectively replace the original data for model training. Although successful in various doma...

---

## 342. FAR-Dex: 少样本 Data Augmentation and Adaptive Residual 策略 Refinement for Dexterous Manipulation

**原标题**: FAR-Dex: Few-shot Data Augmentation and Adaptive Residual Policy Refinement for Dexterous Manipulation

**作者**: Yushan Bai, Fulin Chen, Hongzheng Sun, Yuchuang Tong, En Li, Zhengtao Zhang
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10451v1

**中文摘要**:
> arXiv:2603.10451v1 Announce Type: cross 
摘要: Achieving human-like dexterous manipulation through the collaboration of multi-fingered hands with robotic arms remains a longstanding challenge in 机器人, primarily due to the scarcity of high-quality demonstrations and the complexity of high-dimensional 动作 spaces. To address these challenges, we propose FAR-Dex, a hierarchical 框架 that integrates 少样本 data augmentation with adaptive residual refinement to enable 鲁棒 and precise arm-hand coordination in dexterous tasks. First, FAR-DexGen leverages the IsaacLab simulator to generate diverse and physically constrained trajectories from a few demonstrations, providing a data foundation for 策略 训练. Second, FAR-DexRes introduces an adaptive residual module that refines policies by combining multi-step 轨迹 s...

**Original Abstract**:
> arXiv:2603.10451v1 Announce Type: cross 
Abstract: Achieving human-like dexterous manipulation through the collaboration of multi-fingered hands with robotic arms remains a longstanding challenge in robotics, primarily due to the scarcity of high-quality demonstrations and the complexity of high-dimensional action spaces. To address these challenges, we propose FAR-Dex, a hierarchical framework that integrates few-shot data augmentation with adaptive residual refinement to enable robust and precise arm-hand coordination in dexterous tasks. First, FAR-DexGen leverages the IsaacLab simulator to generate diverse and physically constrained trajectories from a few demonstrations, providing a data foundation for policy training. Second, FAR-DexRes introduces an adaptive residual module that refi...

---

## 343. UniPINN: A Unified PINN 框架 for 多任务 学习 of Diverse Navier-Stokes Equations

**原标题**: UniPINN: A Unified PINN Framework for Multi-task Learning of Diverse Navier-Stokes Equations

**作者**: Dengdi Sun, Jie Chen, Xiao Wang, Jin Tang
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10466v1

**中文摘要**:
> arXiv:2603.10466v1 Announce Type: cross 
摘要: Physics-Informed 神经 Networks (PINNs) have shown promise in solving incompressible Navier-Stokes equations, yet existing approaches are predominantly designed for single-flow settings. When extended to multi-flow scenarios, these methods face three key challenges: (1) difficulty in simultaneously capturing both shared physical principles and flow-specific characteristics, (2) susceptibility to inter-task negative transfer that degrades prediction accuracy, and (3) unstable 训练 dynamics caused by disparate 损失 magnitudes across heterogeneous flow regimes. To address these limitations, we propose UniPINN, a unified multi-flow PINN 框架 that integrates three complementary components: a shared-specialized 架构 that disentangles universal physical laws from...

**Original Abstract**:
> arXiv:2603.10466v1 Announce Type: cross 
Abstract: Physics-Informed Neural Networks (PINNs) have shown promise in solving incompressible Navier-Stokes equations, yet existing approaches are predominantly designed for single-flow settings. When extended to multi-flow scenarios, these methods face three key challenges: (1) difficulty in simultaneously capturing both shared physical principles and flow-specific characteristics, (2) susceptibility to inter-task negative transfer that degrades prediction accuracy, and (3) unstable training dynamics caused by disparate loss magnitudes across heterogeneous flow regimes. To address these limitations, we propose UniPINN, a unified multi-flow PINN framework that integrates three complementary components: a shared-specialized architecture that disent...

---

## 344. Modeling Stage-wise 进化 of User Interests for News 推荐

**原标题**: Modeling Stage-wise Evolution of User Interests for News Recommendation

**作者**: Zhiyong Cheng, Yike Jin, Zhijie Zhang, Huilin Chen, Zhangling Duan, Meng Wang
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10471v1

**中文摘要**:
> arXiv:2603.10471v1 Announce Type: cross 
摘要: Personalized news 推荐 is highly time-sensitive, as user interests are often driven by emerging events, trending topics, and shifting real-world contexts. These dynamics make it essential to 模型 not only users' long-term preferences, which reflect stable reading habits and high-order collaborative patterns, but also their short-term, context-dependent interests that change rapidly over time. However, most existing approaches rely on a single 静态 interaction graph, which struggles to capture both long-term preference patterns and short-term interest changes as user behavior evolves. To address this challenge, we propose a unified 框架 that learns user preferences from both global and local temporal perspectives. A global preference modeling component c...

**Original Abstract**:
> arXiv:2603.10471v1 Announce Type: cross 
Abstract: Personalized news recommendation is highly time-sensitive, as user interests are often driven by emerging events, trending topics, and shifting real-world contexts. These dynamics make it essential to model not only users' long-term preferences, which reflect stable reading habits and high-order collaborative patterns, but also their short-term, context-dependent interests that change rapidly over time. However, most existing approaches rely on a single static interaction graph, which struggles to capture both long-term preference patterns and short-term interest changes as user behavior evolves. To address this challenge, we propose a unified framework that learns user preferences from both global and local temporal perspectives. A global...

---

## 345. Aligning Large Language Models with Searcher Preferences

**原标题**: Aligning Large Language Models with Searcher Preferences

**作者**: Wei Wu, Peilun Zhou, Liyi Chen, Qimeng Wang, Chengqiang Lu, Yan Gao, Yi Wu, Yao Hu, Hui Xiong
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10473v1

**中文摘要**:
> arXiv:2603.10473v1 Announce Type: cross 
摘要: The paradigm shift from item-centric ranking to answer-centric 合成 is redefining the 角色 of 搜索 engines. While recent industrial progress has applied 生成式 techniques to closed-set item ranking in e-commerce, research and 部署 of open-ended 生成式 搜索 on large content platforms remain limited. This setting introduces challenges, including 鲁棒性 to noisy 检索, non-negotiable safety guarantees, and alignment with diverse user needs. In this work, we introduce SearchLLM, the first large language 模型 (大语言模型) for open-ended 生成式 搜索. We design a hierarchical, multi-dimensional 奖励 系统 that separates bottom-line constraints, including factual grounding, basic answer quality and format compliance, from behavior 优化 objectives that promote 鲁棒性 to noisy 检索 and alignment with...

**Original Abstract**:
> arXiv:2603.10473v1 Announce Type: cross 
Abstract: The paradigm shift from item-centric ranking to answer-centric synthesis is redefining the role of search engines. While recent industrial progress has applied generative techniques to closed-set item ranking in e-commerce, research and deployment of open-ended generative search on large content platforms remain limited. This setting introduces challenges, including robustness to noisy retrieval, non-negotiable safety guarantees, and alignment with diverse user needs. In this work, we introduce SearchLLM, the first large language model (LLM) for open-ended generative search. We design a hierarchical, multi-dimensional reward system that separates bottom-line constraints, including factual grounding, basic answer quality and format complian...

---

## 346. 学习 to Negotiate: Multi-智能体 Deliberation for Collective 价值 Alignment in LLMs

**原标题**: Learning to Negotiate: Multi-Agent Deliberation for Collective Value Alignment in LLMs

**作者**: Panatchakorn Anantaprayoon, Nataliia Babina, Nima Asgharbeygi, Jad Tarifi
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10476v1

**中文摘要**:
> arXiv:2603.10476v1 Announce Type: cross 
摘要: The alignment of large language models (LLMs) has progressed substantially in single-智能体 settings through paradigms such as RLHF and Constitutional AI, with recent work exploring 可扩展 alternatives such as RLAIF and evolving alignment objectives. However, these approaches remain limited in multi-stakeholder settings, where conflicting values arise and deliberative negotiation capabilities are required. This work proposes a multi-智能体 negotiation-based alignment 框架 that aligns LLMs to Collective Agency (CA)-an existing alignment objective introduced to promote the continual expansion of agency-while simultaneously improving conflict-resolution capability. To enable 可扩展 训练, two self-play instances of the same 大语言模型, assigned opposing personas, engage...

**Original Abstract**:
> arXiv:2603.10476v1 Announce Type: cross 
Abstract: The alignment of large language models (LLMs) has progressed substantially in single-agent settings through paradigms such as RLHF and Constitutional AI, with recent work exploring scalable alternatives such as RLAIF and evolving alignment objectives. However, these approaches remain limited in multi-stakeholder settings, where conflicting values arise and deliberative negotiation capabilities are required. This work proposes a multi-agent negotiation-based alignment framework that aligns LLMs to Collective Agency (CA)-an existing alignment objective introduced to promote the continual expansion of agency-while simultaneously improving conflict-resolution capability. To enable scalable training, two self-play instances of the same LLM, ass...

---

## 347. JEDI: Jointly Embedded 推理 of 神经 Dynamics

**原标题**: JEDI: Jointly Embedded Inference of Neural Dynamics

**作者**: Anirudh Jamkhandi, Ali Korojy, Olivier Codol, Guillaume Lajoie, Matthew G. Perich
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10489v1

**中文摘要**:
> arXiv:2603.10489v1 Announce Type: cross 
摘要: Animal brains flexibly and efficiently achieve many behavioral tasks with a single 神经 网络. A core goal in modern neuroscience is to map the mechanisms of the brain's flexibility onto the dynamics underlying 神经 populations. However, identifying task-specific dynamical rules from limited, noisy, and high-dimensional experimental 神经 recordings remains a major challenge, as experimental data often provide only partial access to brain states and dynamical mechanisms. While 循环 神经 networks (RNNs) directly constrained 神经 data have been effective in inferring underlying dynamical mechanisms, they are typically limited to single-task domains and struggle to generalize across behavioral conditions. Here, we introduce JEDI, a hierarchical 模型 that captures 神经...

**Original Abstract**:
> arXiv:2603.10489v1 Announce Type: cross 
Abstract: Animal brains flexibly and efficiently achieve many behavioral tasks with a single neural network. A core goal in modern neuroscience is to map the mechanisms of the brain's flexibility onto the dynamics underlying neural populations. However, identifying task-specific dynamical rules from limited, noisy, and high-dimensional experimental neural recordings remains a major challenge, as experimental data often provide only partial access to brain states and dynamical mechanisms. While recurrent neural networks (RNNs) directly constrained neural data have been effective in inferring underlying dynamical mechanisms, they are typically limited to single-task domains and struggle to generalize across behavioral conditions. Here, we introduce JE...

---

## 348. Na\"ive Exposure of 生成式 AI Capabilities Undermines Deepfake 检测

**原标题**: Na\"ive Exposure of Generative AI Capabilities Undermines Deepfake Detection

**作者**: Sunpill Kim, Chanwoo Hwang, Minsu Kim, Jae Hong Seo
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10504v1

**中文摘要**:
> arXiv:2603.10504v1 Announce Type: cross 
摘要: 生成式 AI systems increasingly expose powerful 推理 and 图像 refinement capabilities through user-facing chatbot interfaces. In this work, we show that the na\"ive exposure of such capabilities fundamentally undermines modern deepfake detectors. Rather than proposing a new 图像 manipulation 技术, we study a realistic and already-deployed usage scenario in which an adversary uses only benign, 策略-compliant prompts and commercial 生成式 AI systems. We demonstrate that 状态-of-the-art deepfake 检测 methods fail under semantic-preserving 图像 refinement. Specifically, we show that 生成式 AI systems articulate explicit authenticity criteria and inadvertently externalize them through unrestricted 推理, enabling their direct reuse as refinement objectives. As a 结果, refined imag...

**Original Abstract**:
> arXiv:2603.10504v1 Announce Type: cross 
Abstract: Generative AI systems increasingly expose powerful reasoning and image refinement capabilities through user-facing chatbot interfaces. In this work, we show that the na\"ive exposure of such capabilities fundamentally undermines modern deepfake detectors. Rather than proposing a new image manipulation technique, we study a realistic and already-deployed usage scenario in which an adversary uses only benign, policy-compliant prompts and commercial generative AI systems. We demonstrate that state-of-the-art deepfake detection methods fail under semantic-preserving image refinement. Specifically, we show that generative AI systems articulate explicit authenticity criteria and inadvertently externalize them through unrestricted reasoning, enab...

---

## 349. UAV-MARL: Multi-智能体 强化 学习 for Time-Critical and 动态 Medical Supply Delivery

**原标题**: UAV-MARL: Multi-Agent Reinforcement Learning for Time-Critical and Dynamic Medical Supply Delivery

**作者**: Islam Guven, Mehmet Parlak
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10528v1

**中文摘要**:
> arXiv:2603.10528v1 Announce Type: cross 
摘要: Unmanned aerial vehicles (UAVs) are increasingly used to support time-critical medical supply delivery, providing rapid and flexible logistics during emergencies and resource shortages. However, effective 部署 of UAV fleets requires coordination mechanisms capable of prioritizing medical requests, allocating limited aerial resources, and adapting delivery schedules under uncertain operational conditions. This 论文 presents a multi-智能体 强化 学习 (MARL) 框架 for coordinating UAV fleets in stochastic medical delivery scenarios where requests vary in urgency, location, and delivery deadlines. The problem is formulated as a partially observable Markov 决策 process (POMDP) in which UAV agents maintain awareness of medical delivery demands while having limited vis...

**Original Abstract**:
> arXiv:2603.10528v1 Announce Type: cross 
Abstract: Unmanned aerial vehicles (UAVs) are increasingly used to support time-critical medical supply delivery, providing rapid and flexible logistics during emergencies and resource shortages. However, effective deployment of UAV fleets requires coordination mechanisms capable of prioritizing medical requests, allocating limited aerial resources, and adapting delivery schedules under uncertain operational conditions. This paper presents a multi-agent reinforcement learning (MARL) framework for coordinating UAV fleets in stochastic medical delivery scenarios where requests vary in urgency, location, and delivery deadlines. The problem is formulated as a partially observable Markov decision process (POMDP) in which UAV agents maintain awareness of ...

---

## 350. Prompting with the human-touch: evaluating 模型-sensitivity of foundation models for musculoskeletal CT 分割

**原标题**: Prompting with the human-touch: evaluating model-sensitivity of foundation models for musculoskeletal CT segmentation

**作者**: Caroline Magg, Maaike A. ter Wee, Johannes G. G. Dobbe, Geert J. Streekstra, Leendert Blankevoort, Clara I. S\'anchez, Hoel Kervadec
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10541v1

**中文摘要**:
> arXiv:2603.10541v1 Announce Type: cross 
摘要: Promptable Foundation Models (FMs), initially introduced for natural 图像 分割, have also revolutionized medical 图像 分割. The increasing number of models, along with evaluations varying in datasets, metrics, and compared models, makes direct 性能 comparison between models difficult and complicates the 选择 of the most suitable 模型 for specific clinical tasks. In our study, 11 promptable FMs are tested using non-iterative 2D and 3D prompting strategies on a private and public 数据集 focusing on bone and implant 分割 in four anatomical regions (wrist, shoulder, hip and lower leg). The Pareto-optimal models are identified and further analyzed using human prompts collected through a dedicated observer study. Our findings are: 1) The 分割 性能 varies a lot between FMs a...

**Original Abstract**:
> arXiv:2603.10541v1 Announce Type: cross 
Abstract: Promptable Foundation Models (FMs), initially introduced for natural image segmentation, have also revolutionized medical image segmentation. The increasing number of models, along with evaluations varying in datasets, metrics, and compared models, makes direct performance comparison between models difficult and complicates the selection of the most suitable model for specific clinical tasks. In our study, 11 promptable FMs are tested using non-iterative 2D and 3D prompting strategies on a private and public dataset focusing on bone and implant segmentation in four anatomical regions (wrist, shoulder, hip and lower leg). The Pareto-optimal models are identified and further analyzed using human prompts collected through a dedicated observer...

---

## 351. SCORE: Replacing Layer Stacking with Contractive 循环 Depth

**原标题**: SCORE: Replacing Layer Stacking with Contractive Recurrent Depth

**作者**: Guillaume Godin
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10544v1

**中文摘要**:
> arXiv:2603.10544v1 Announce Type: cross 
摘要: Residual connections are central to modern 深度 神经 networks, enabling stable 优化 and 高效 information flow across depth. In this work, we propose SCORE (Skip-Connection ODE 循环 嵌入), a discrete 循环 alternative to classical layer stacking. Instead of composing multiple independent layers, SCORE iteratively applies a single shared 神经 block using an ODE (Ordinary Differential Equation)-inspired contractive update: ht+1 = (1 - dt) * ht + dt * F(ht) This formulation can be interpreted as a depth-by-迭代 refinement process, where the step size dt explicitly controls stability and update magnitude. Unlike continuous 神经 ODE approaches, SCORE uses a fixed number of discrete iterations and standard 反向传播 without requiring ODE solvers or adjoint methods. We evaluate ...

**Original Abstract**:
> arXiv:2603.10544v1 Announce Type: cross 
Abstract: Residual connections are central to modern deep neural networks, enabling stable optimization and efficient information flow across depth. In this work, we propose SCORE (Skip-Connection ODE Recurrent Embedding), a discrete recurrent alternative to classical layer stacking. Instead of composing multiple independent layers, SCORE iteratively applies a single shared neural block using an ODE (Ordinary Differential Equation)-inspired contractive update: ht+1 = (1 - dt) * ht + dt * F(ht) This formulation can be interpreted as a depth-by-iteration refinement process, where the step size dt explicitly controls stability and update magnitude. Unlike continuous Neural ODE approaches, SCORE uses a fixed number of discrete iterations and standard ba...

---

## 352. 梯度 Flow Drifting: 生成式 Modeling via Wasserstein 梯度 Flows of KDE-Approximated Divergences

**原标题**: Gradient Flow Drifting: Generative Modeling via Wasserstein Gradient Flows of KDE-Approximated Divergences

**作者**: Jiarui Cao, Zixuan Wei, Yuxin Liu
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10592v1

**中文摘要**:
> arXiv:2603.10592v1 Announce Type: cross 
摘要: We reveal a precise mathematical 框架 about a new family of 生成式 models which we call 梯度 Flow Drifting. With this 框架, we prove an equivalence between the recently proposed Drifting 模型 and the Wasserstein 梯度 flow of the 前向 KL divergence under kernel density estimation (KDE) approximation. Specifically, we prove that the drifting field of drifting 模型 (arXiv:2602.04770) equals, up to a 带宽-squared scaling factor, the difference of KDE log-density gradients $\nabla \log p_{\mathrm{kde}} - \nabla \log q_{\mathrm{kde}}$, which is exactly the particle velocity field of the Wasserstein-2 梯度 flow of $KL(q\|p)$ with KDE-approximated densities. Besides that, this broad family of 生成式 models can also include MMD-based generators, which arises as special cases of...

**Original Abstract**:
> arXiv:2603.10592v1 Announce Type: cross 
Abstract: We reveal a precise mathematical framework about a new family of generative models which we call Gradient Flow Drifting. With this framework, we prove an equivalence between the recently proposed Drifting Model and the Wasserstein gradient flow of the forward KL divergence under kernel density estimation (KDE) approximation. Specifically, we prove that the drifting field of drifting model (arXiv:2602.04770) equals, up to a bandwidth-squared scaling factor, the difference of KDE log-density gradients $\nabla \log p_{\mathrm{kde}} - \nabla \log q_{\mathrm{kde}}$, which is exactly the particle velocity field of the Wasserstein-2 gradient flow of $KL(q\|p)$ with KDE-approximated densities. Besides that, this broad family of generative models c...

---

## 353. 强化 学习 with Conditional Expectation 奖励

**原标题**: Reinforcement Learning with Conditional Expectation Reward

**作者**: Changyi Xiao, Caijun Xu, Yixin Cao
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10624v1

**中文摘要**:
> arXiv:2603.10624v1 Announce Type: cross 
摘要: 强化 学习 with Verifiable Rewards (RLVR) has proven effective in enhancing the 推理 capabilities of large language models, particularly in domains such as mathematics where reliable rule-based verifiers can be constructed. However, the reliance on handcrafted, domain-specific verification rules substantially limits the applicability of RLVR to general 推理 domains with free-form answers, where valid answers often exhibit significant variability, making it difficult to establish complete and 准确 rules. To address this limitation, we propose Conditional Expectation 奖励 (CER), which leverages the large language 模型 itself as an implicit verifier, and is therefore applicable to general domains and eliminates the need for external verifiers or auxiliary models....

**Original Abstract**:
> arXiv:2603.10624v1 Announce Type: cross 
Abstract: Reinforcement Learning with Verifiable Rewards (RLVR) has proven effective in enhancing the reasoning capabilities of large language models, particularly in domains such as mathematics where reliable rule-based verifiers can be constructed. However, the reliance on handcrafted, domain-specific verification rules substantially limits the applicability of RLVR to general reasoning domains with free-form answers, where valid answers often exhibit significant variability, making it difficult to establish complete and accurate rules. To address this limitation, we propose Conditional Expectation Reward (CER), which leverages the large language model itself as an implicit verifier, and is therefore applicable to general domains and eliminates th...

---

## 354. Interleaving Scheduling and Motion 规划 with Incremental 学习 of Symbolic Space-Time Motion Abstractions

**原标题**: Interleaving Scheduling and Motion Planning with Incremental Learning of Symbolic Space-Time Motion Abstractions

**作者**: Elisa Tosello, Arthur Bit-Monnot, Davide Lusuardi, Alessandro Valentini, Andrea Micheli
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10651v1

**中文摘要**:
> arXiv:2603.10651v1 Announce Type: cross 
摘要: Task and Motion 规划 combines high-level task sequencing (what to do) with low-level motion 规划 (how to do it) to generate feasible, collision-free execution plans. However, in many real-world domains, such as automated warehouses, tasks are predefined, shifting the challenge to if, when, and how to execute them safely and efficiently under resource, time and motion constraints. In this 论文, we formalize this as the Scheduling and Motion 规划 problem for multi-object navigation in shared workspaces. We propose a novel solution 框架 that interleaves off-the-shelf schedulers and motion planners in an incremental 学习 loop. The 调度器 generates candidate plans, while the motion planner checks feasibility and returns symbolic feedback, i.e., spatial conflicts an...

**Original Abstract**:
> arXiv:2603.10651v1 Announce Type: cross 
Abstract: Task and Motion Planning combines high-level task sequencing (what to do) with low-level motion planning (how to do it) to generate feasible, collision-free execution plans. However, in many real-world domains, such as automated warehouses, tasks are predefined, shifting the challenge to if, when, and how to execute them safely and efficiently under resource, time and motion constraints. In this paper, we formalize this as the Scheduling and Motion Planning problem for multi-object navigation in shared workspaces. We propose a novel solution framework that interleaves off-the-shelf schedulers and motion planners in an incremental learning loop. The scheduler generates candidate plans, while the motion planner checks feasibility and returns...

---

## 355. Are 视频 推理 Models Ready to Go Outside?

**原标题**: Are Video Reasoning Models Ready to Go Outside?

**作者**: Yangfan He, Changgyu Boo, Jaehong Yoon
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10652v1

**中文摘要**:
> arXiv:2603.10652v1 Announce Type: cross 
摘要: In real-world 部署, vision-language models often encounter disturbances such as weather, occlusion, and camera motion. Under such conditions, their understanding and 推理 degrade substantially, revealing a gap between clean, controlled (i.e., unperturbed) 评估 settings and real-world 鲁棒性. To address this limitation, we propose ROVA, a novel 训练 框架 that improves 鲁棒性 by modeling a 鲁棒性-aware consistency 奖励 under spatio-temporal corruptions. ROVA introduces a difficulty-aware 在线 训练 strategy that prioritizes informative samples based on the 模型's evolving capability. Specifically, it continuously re-estimates sample difficulty via self-reflective 评估, enabling adaptive 训练 with a 鲁棒性-aware consistency 奖励. We also introduce PVRBench, a new 基准 that injects real-...

**Original Abstract**:
> arXiv:2603.10652v1 Announce Type: cross 
Abstract: In real-world deployment, vision-language models often encounter disturbances such as weather, occlusion, and camera motion. Under such conditions, their understanding and reasoning degrade substantially, revealing a gap between clean, controlled (i.e., unperturbed) evaluation settings and real-world robustness. To address this limitation, we propose ROVA, a novel training framework that improves robustness by modeling a robustness-aware consistency reward under spatio-temporal corruptions. ROVA introduces a difficulty-aware online training strategy that prioritizes informative samples based on the model's evolving capability. Specifically, it continuously re-estimates sample difficulty via self-reflective evaluation, enabling adaptive tra...

---

## 356. Contract And Conquer: How to Provably Compute 对抗 Examples for a Black-Box 模型?

**原标题**: Contract And Conquer: How to Provably Compute Adversarial Examples for a Black-Box Model?

**作者**: Anna Chistyakova, Mikhail Pautov
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10689v1

**中文摘要**:
> arXiv:2603.10689v1 Announce Type: cross 
摘要: Black-box 对抗 attacks are widely used as tools to test the 鲁棒性 of 深度 神经 networks against malicious perturbations of input data aimed at a specific change in the output of the 模型. Such methods, although they remain empirically effective, usually do not guarantee that an 对抗 example can be found for a particular 模型. In this 论文, we propose Contract And Conquer (CAC), an 方案 to provably compute 对抗 examples for 神经 networks in a black-box manner. The 方法 is based on knowledge distillation of a black-box 模型 on an expanding distillation 数据集 and precise contraction of the 对抗 example 搜索 space. CAC is supported by the transferability guarantee: we prove that the 方法 yields an 对抗 example for the black-box 模型 within a fixed number of 算法 iterations. Experimentally...

**Original Abstract**:
> arXiv:2603.10689v1 Announce Type: cross 
Abstract: Black-box adversarial attacks are widely used as tools to test the robustness of deep neural networks against malicious perturbations of input data aimed at a specific change in the output of the model. Such methods, although they remain empirically effective, usually do not guarantee that an adversarial example can be found for a particular model. In this paper, we propose Contract And Conquer (CAC), an approach to provably compute adversarial examples for neural networks in a black-box manner. The method is based on knowledge distillation of a black-box model on an expanding distillation dataset and precise contraction of the adversarial example search space. CAC is supported by the transferability guarantee: we prove that the method yie...

---

## 357. Repurposing Backdoors for Good: Ephemeral Intrinsic Proofs for Verifiable Aggregation in Cross-silo Federated 学习

**原标题**: Repurposing Backdoors for Good: Ephemeral Intrinsic Proofs for Verifiable Aggregation in Cross-silo Federated Learning

**作者**: Xian Qin, Xue Yang, Xiaohu Tang
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10692v1

**中文摘要**:
> arXiv:2603.10692v1 Announce Type: cross 
摘要: While 安全 Aggregation (SA) protects update confidentiality in Cross-silo Federated 学习, it fails to guarantee aggregation integrity, allowing malicious servers to silently omit or tamper with updates. Existing verifiable aggregation schemes rely on heavyweight cryptography (e.g., ZKPs, HE), incurring computational costs that scale poorly with 模型 size. In this 论文, we propose a lightweight 架构 that shifts from extrinsic cryptographic proofs to \textit{Intrinsic Proofs}. We repurpose backdoor injection to embed verification signals directly into 模型 parameters. By harnessing Catastrophic Forgetting, these signals are 鲁棒 for immediate verification yet ephemeral, naturally decaying to preserve final 模型 utility. We design a randomized, single-verifier aud...

**Original Abstract**:
> arXiv:2603.10692v1 Announce Type: cross 
Abstract: While Secure Aggregation (SA) protects update confidentiality in Cross-silo Federated Learning, it fails to guarantee aggregation integrity, allowing malicious servers to silently omit or tamper with updates. Existing verifiable aggregation schemes rely on heavyweight cryptography (e.g., ZKPs, HE), incurring computational costs that scale poorly with model size. In this paper, we propose a lightweight architecture that shifts from extrinsic cryptographic proofs to \textit{Intrinsic Proofs}. We repurpose backdoor injection to embed verification signals directly into model parameters. By harnessing Catastrophic Forgetting, these signals are robust for immediate verification yet ephemeral, naturally decaying to preserve final model utility. W...

---

## 358. EvoSchema: Towards Text-to-SQL 鲁棒性 Against Schema 进化

**原标题**: EvoSchema: Towards Text-to-SQL Robustness Against Schema Evolution

**作者**: Tianshu Zhang, Kun Qian, Siddhartha Sahai, Yuan Tian, Shaddy Garg, Huan Sun, Yunyao Li
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10697v1

**中文摘要**:
> arXiv:2603.10697v1 Announce Type: cross 
摘要: 神经 text-to-SQL models, which translate natural language questions (NLQs) into SQL queries given a database schema, have achieved remarkable 性能. However, database schemas frequently evolve to meet new requirements. Such schema 进化 often leads to 性能 degradation for models trained on 静态 schemas. Existing work either mainly focuses on simply paraphrasing some syntactic or semantic mappings among NLQ, DB and SQL, or lacks a comprehensive and controllable way to investigate the 模型 鲁棒性 issue under the schema 进化, which is insufficient when facing the increasingly complex and rich database schema changes in reality, especially in the 大语言模型 era. To address the challenges posed by schema 进化, we present EvoSchema, a comprehensive 基准 designed to assess and en...

**Original Abstract**:
> arXiv:2603.10697v1 Announce Type: cross 
Abstract: Neural text-to-SQL models, which translate natural language questions (NLQs) into SQL queries given a database schema, have achieved remarkable performance. However, database schemas frequently evolve to meet new requirements. Such schema evolution often leads to performance degradation for models trained on static schemas. Existing work either mainly focuses on simply paraphrasing some syntactic or semantic mappings among NLQ, DB and SQL, or lacks a comprehensive and controllable way to investigate the model robustness issue under the schema evolution, which is insufficient when facing the increasingly complex and rich database schema changes in reality, especially in the LLM era. To address the challenges posed by schema evolution, we pr...

---

## 359. AlphaFlowTSE: One-Step 生成式 目标 说话人 Extraction via Conditional AlphaFlow

**原标题**: AlphaFlowTSE: One-Step Generative Target Speaker Extraction via Conditional AlphaFlow

**作者**: Duojia Li, Shuhan Zhang, Zihan Qian, Wenxuan Wu, Shuai Wang, Qingyang Hong, Lin Li, Haizhou Li
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10701v1

**中文摘要**:
> arXiv:2603.10701v1 Announce Type: cross 
摘要: In 目标 说话人 extraction (TSE), we aim to recover 目标 语音 from a multi-talker mixture using a short enrollment utterance as reference. Recent studies on diffusion and flow-matching generators have improved 目标-语音 fidelity. However, multi-step 采样 increases 延迟, and one-step solutions often rely on a mixture-dependent time coordinate that can be unreliable for real-world conversations. We present AlphaFlowTSE, a one-step conditional 生成式 模型 trained with a Jacobian-向量 product (JVP)-free AlphaFlow objective. AlphaFlowTSE learns mean-velocity transport along a mixture-to-目标 轨迹 starting from the observed mixture, eliminating auxiliary mixing-ratio prediction, and stabilizes 训练 by combining flow matching with an interval-consistency teacher-student 目标. Experime...

**Original Abstract**:
> arXiv:2603.10701v1 Announce Type: cross 
Abstract: In target speaker extraction (TSE), we aim to recover target speech from a multi-talker mixture using a short enrollment utterance as reference. Recent studies on diffusion and flow-matching generators have improved target-speech fidelity. However, multi-step sampling increases latency, and one-step solutions often rely on a mixture-dependent time coordinate that can be unreliable for real-world conversations. We present AlphaFlowTSE, a one-step conditional generative model trained with a Jacobian-vector product (JVP)-free AlphaFlow objective. AlphaFlowTSE learns mean-velocity transport along a mixture-to-target trajectory starting from the observed mixture, eliminating auxiliary mixing-ratio prediction, and stabilizes training by combinin...

---

## 360. 概率 Verification of 声纹 Anti-Spoofing Models

**原标题**: Probabilistic Verification of Voice Anti-Spoofing Models

**作者**: Evgeny Kushnir, Alexandr Kozodaev, Dmitrii Korzh, Mikhail Pautov, Oleg Kiriukhin, Oleg Y. Rogov
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10713v1

**中文摘要**:
> arXiv:2603.10713v1 Announce Type: cross 
摘要: Recent advances in 生成式 models have amplified the risk of malicious misuse of 语音 合成 technologies, enabling adversaries to impersonate 目标 speakers and access sensitive resources. Although 语音 deepfake 检测 has progressed rapidly, most existing countermeasures lack formal 鲁棒性 guarantees or fail to generalize to unseen 生成 techniques. We propose PV-VASM, a 概率 框架 for verifying the 鲁棒性 of 声纹 anti-spoofing models (VASMs). PV-VASM estimates the probability of misclassification under text-to-语音 (文本转语音), 声纹 cloning (语音转换), and parametric signal transformations. The 方案 is 模型-agnostic and enables 鲁棒性 verification against unseen 语音 合成 techniques and input perturbations. We derive a theoretical upper bound on the error probability and validate the 方法 across diver...

**Original Abstract**:
> arXiv:2603.10713v1 Announce Type: cross 
Abstract: Recent advances in generative models have amplified the risk of malicious misuse of speech synthesis technologies, enabling adversaries to impersonate target speakers and access sensitive resources. Although speech deepfake detection has progressed rapidly, most existing countermeasures lack formal robustness guarantees or fail to generalize to unseen generation techniques. We propose PV-VASM, a probabilistic framework for verifying the robustness of voice anti-spoofing models (VASMs). PV-VASM estimates the probability of misclassification under text-to-speech (TTS), voice cloning (VC), and parametric signal transformations. The approach is model-agnostic and enables robustness verification against unseen speech synthesis techniques and in...

---

## 361. CUPID: A Plug-in 框架 for Joint Aleatoric and Epistemic Uncertainty Estimation with a Single 模型

**原标题**: CUPID: A Plug-in Framework for Joint Aleatoric and Epistemic Uncertainty Estimation with a Single Model

**作者**: Xinran Xu, Xiuyi Fan
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10745v1

**中文摘要**:
> arXiv:2603.10745v1 Announce Type: cross 
摘要: 准确 estimation of uncertainty in 深度 学习 is critical for deploying models in high-stakes domains such as medical diagnosis and 自主 决策-making, where overconfident predictions can lead to harmful outcomes. In practice, understanding the reason behind a 模型's uncertainty and the type of uncertainty it represents can support risk-aware decisions, enhance user trust, and guide additional data collection. However, many existing methods only address a single type of uncertainty or require modifications and retraining of the base 模型, making them difficult to adopt in real-world systems. We introduce CUPID (Comprehensive Uncertainty Plug-in estImation 模型), a general-purpose module that jointly estimates aleatoric and epistemic uncertainty without modifying or...

**Original Abstract**:
> arXiv:2603.10745v1 Announce Type: cross 
Abstract: Accurate estimation of uncertainty in deep learning is critical for deploying models in high-stakes domains such as medical diagnosis and autonomous decision-making, where overconfident predictions can lead to harmful outcomes. In practice, understanding the reason behind a model's uncertainty and the type of uncertainty it represents can support risk-aware decisions, enhance user trust, and guide additional data collection. However, many existing methods only address a single type of uncertainty or require modifications and retraining of the base model, making them difficult to adopt in real-world systems. We introduce CUPID (Comprehensive Uncertainty Plug-in estImation moDel), a general-purpose module that jointly estimates aleatoric and...

---

## 362. 深度 Randomized 分布式 Function Computation (DeepRDFC): 神经 分布式 Channel Simulation

**原标题**: Deep Randomized Distributed Function Computation (DeepRDFC): Neural Distributed Channel Simulation

**作者**: Didrik Bergstr\"om, Onur G\"unl\"u
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10750v1

**中文摘要**:
> arXiv:2603.10750v1 Announce Type: cross 
摘要: The randomized 分布式 function computation (RDFC) 框架, which unifies many cutting-edge 分布式 computation and 学习 applications, is considered. An autoencoder (AE) 架构 is proposed to minimize the total variation distance between the probability distribution simulated by the AE outputs and an unknown 目标 distribution, using only data samples. We illustrate significantly high RDFC 性能 with communication load gains from our AEs compared to data compression methods. Our designs establish 深度 学习-based RDFC methods and aim to facilitate the use of RDFC methods, especially when the amount of common randomness is limited and strong function computation guarantees are required.

**Original Abstract**:
> arXiv:2603.10750v1 Announce Type: cross 
Abstract: The randomized distributed function computation (RDFC) framework, which unifies many cutting-edge distributed computation and learning applications, is considered. An autoencoder (AE) architecture is proposed to minimize the total variation distance between the probability distribution simulated by the AE outputs and an unknown target distribution, using only data samples. We illustrate significantly high RDFC performance with communication load gains from our AEs compared to data compression methods. Our designs establish deep learning-based RDFC methods and aim to facilitate the use of RDFC methods, especially when the amount of common randomness is limited and strong function computation guarantees are required.

---

## 363. Taking Shortcuts for Categorical VQA Using Super Neurons

**原标题**: Taking Shortcuts for Categorical VQA Using Super Neurons

**作者**: Pierre Musacchio, Jaeyi Jeong, Dahun Kim, Jaesik Park
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10781v1

**中文摘要**:
> arXiv:2603.10781v1 Announce Type: cross 
摘要: Sparse 注意力 Vectors (SAVs) have emerged as an excellent 训练-free alternative to 有监督 finetuning or low-rank adaptation to improve the 性能 of Vision Language Models (VLMs). At their heart, SAVs select a few 准确 注意力 heads for a task of interest and use them as classifiers, rather than relying on the 模型's prediction. In a similar spirit, we find that directly probing the raw activations of the VLM, in the form of scalar values, is sufficient to yield 准确 classifiers on diverse visually grounded downstream tasks. Shifting focus from 注意力 vectors to scalar activations dramatically increases the 搜索 space for 准确 parameters, allowing us to find more 判别式 neurons immediately from the first generated token. We call such activations Super Neurons (SNs). In this pr...

**Original Abstract**:
> arXiv:2603.10781v1 Announce Type: cross 
Abstract: Sparse Attention Vectors (SAVs) have emerged as an excellent training-free alternative to supervised finetuning or low-rank adaptation to improve the performance of Vision Language Models (VLMs). At their heart, SAVs select a few accurate attention heads for a task of interest and use them as classifiers, rather than relying on the model's prediction. In a similar spirit, we find that directly probing the raw activations of the VLM, in the form of scalar values, is sufficient to yield accurate classifiers on diverse visually grounded downstream tasks. Shifting focus from attention vectors to scalar activations dramatically increases the search space for accurate parameters, allowing us to find more discriminative neurons immediately from t...

---

## 364. AI-Enhanced Spatial Cellular Traffic Demand Prediction with Contextual Clustering and Error Correction for 5G/6G 规划

**原标题**: AI-Enhanced Spatial Cellular Traffic Demand Prediction with Contextual Clustering and Error Correction for 5G/6G Planning

**作者**: Mohamad Alkadamani, Colin Brown, Halim Yanikomeroglu
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10800v1

**中文摘要**:
> arXiv:2603.10800v1 Announce Type: cross 
摘要: 准确 spatial prediction of cellular traffic demand is essential for 5G NR capacity 规划, 网络 densification, and data-driven 6G 规划. Although machine 学习 can fuse heterogeneous geospatial and socio-economic layers to estimate fine-grained demand maps, spatial autocorrelation can cause neighborhood leakage under naive train/test splits, inflating accuracy and weakening 规划 reliability. This 论文 presents an AI-driven 框架 that reduces leakage and improves spatial 泛化 via a context-aware two-stage splitting strategy with residual spatial error correction. Experiments using crowdsourced usage indicators across five major Canadian cities show consistent mean absolute error (MAE) reductions relative to location-only clustering, supporting more reliable 带宽 provisio...

**Original Abstract**:
> arXiv:2603.10800v1 Announce Type: cross 
Abstract: Accurate spatial prediction of cellular traffic demand is essential for 5G NR capacity planning, network densification, and data-driven 6G planning. Although machine learning can fuse heterogeneous geospatial and socio-economic layers to estimate fine-grained demand maps, spatial autocorrelation can cause neighborhood leakage under naive train/test splits, inflating accuracy and weakening planning reliability. This paper presents an AI-driven framework that reduces leakage and improves spatial generalization via a context-aware two-stage splitting strategy with residual spatial error correction. Experiments using crowdsourced usage indicators across five major Canadian cities show consistent mean absolute error (MAE) reductions relative to...

---

## 365. Towards Intelligent Spectrum Management: Spectrum Demand Estimation Using Graph 神经 Networks

**原标题**: Towards Intelligent Spectrum Management: Spectrum Demand Estimation Using Graph Neural Networks

**作者**: Mohamad Alkadamani, Amir Ghasemi, Halim Yanikomeroglu
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10802v1

**中文摘要**:
> arXiv:2603.10802v1 Announce Type: cross 
摘要: The growing demand for wireless connectivity, combined with limited spectrum resources, calls for more 高效 spectrum management. Spectrum sharing is a promising 方案; however, regulators need 准确 methods to characterize demand dynamics and guide allocation decisions. This 论文 builds and validates a spectrum demand 代理 from public 部署 records and uses a graph 注意力 网络 in a hierarchical, multi-resolution setup (HR-GAT) to estimate spectrum demand at fine spatial scales. The 模型 captures both neighborhood effects and cross-scale patterns, reducing spatial autocorrelation and improving 泛化. Evaluated across five Canadian cities and against eight competitive baselines, HR-GAT reduces median RMSE by roughly 21% relative to the best alternative and lowers residual...

**Original Abstract**:
> arXiv:2603.10802v1 Announce Type: cross 
Abstract: The growing demand for wireless connectivity, combined with limited spectrum resources, calls for more efficient spectrum management. Spectrum sharing is a promising approach; however, regulators need accurate methods to characterize demand dynamics and guide allocation decisions. This paper builds and validates a spectrum demand proxy from public deployment records and uses a graph attention network in a hierarchical, multi-resolution setup (HR-GAT) to estimate spectrum demand at fine spatial scales. The model captures both neighborhood effects and cross-scale patterns, reducing spatial autocorrelation and improving generalization. Evaluated across five Canadian cities and against eight competitive baselines, HR-GAT reduces median RMSE by...

---

## 366. Risk-Adjusted Harm Scoring for Automated Red Teaming for LLMs in Financial Services

**原标题**: Risk-Adjusted Harm Scoring for Automated Red Teaming for LLMs in Financial Services

**作者**: Fabrizio Dimino, Bhaskarjit Sarmah, Stefano Pasquali
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10807v1

**中文摘要**:
> arXiv:2603.10807v1 Announce Type: cross 
摘要: The rapid adoption of large language models (LLMs) in financial services introduces new operational, regulatory, and security risks. Yet most red-teaming benchmarks remain domain-agnostic and fail to capture failure modes specific to regulated BFSI settings, where harmful behavior can be elicited through legally or professionally plausible framing. We propose a risk-aware 评估 框架 for 大语言模型 security failures in Banking, Financial Services, and Insurance (BFSI), combining a domain-specific taxonomy of financial harms, an automated multi-round red-teaming pipeline, and an ensemble-based judging protocol. We introduce the Risk-Adjusted Harm Score (RAHS), a risk-sensitive metric that goes beyond success rates by quantifying the operational severity of ...

**Original Abstract**:
> arXiv:2603.10807v1 Announce Type: cross 
Abstract: The rapid adoption of large language models (LLMs) in financial services introduces new operational, regulatory, and security risks. Yet most red-teaming benchmarks remain domain-agnostic and fail to capture failure modes specific to regulated BFSI settings, where harmful behavior can be elicited through legally or professionally plausible framing. We propose a risk-aware evaluation framework for LLM security failures in Banking, Financial Services, and Insurance (BFSI), combining a domain-specific taxonomy of financial harms, an automated multi-round red-teaming pipeline, and an ensemble-based judging protocol. We introduce the Risk-Adjusted Harm Score (RAHS), a risk-sensitive metric that goes beyond success rates by quantifying the opera...

---

## 367. Protein Counterfactuals via Diffusion-Guided 隐变量 优化

**原标题**: Protein Counterfactuals via Diffusion-Guided Latent Optimization

**作者**: Weronika K{\l}os, Sidney Bender, Lukas Kades
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10811v1

**中文摘要**:
> arXiv:2603.10811v1 Announce Type: cross 
摘要: 深度 学习 models can predict protein properties with unprecedented accuracy but rarely offer mechanistic insight or actionable guidance for engineering improved variants. When a 模型 flags an antibody as unstable, the protein engineer is left without recourse: which mutations would rescue stability while preserving function? We introduce Manifold-Constrained Counterfactual 优化 for Proteins (MCCOP), a 框架 that computes minimal, biologically plausible sequence edits that flip a 模型's prediction to a desired 目标 状态. MCCOP operates in a continuous joint sequence-structure 隐变量 space and employs a pretrained diffusion 模型 as a manifold prior, balancing three objectives: validity (achieving the 目标 property), proximity (minimizing mutations), and plausibility (pro...

**Original Abstract**:
> arXiv:2603.10811v1 Announce Type: cross 
Abstract: Deep learning models can predict protein properties with unprecedented accuracy but rarely offer mechanistic insight or actionable guidance for engineering improved variants. When a model flags an antibody as unstable, the protein engineer is left without recourse: which mutations would rescue stability while preserving function? We introduce Manifold-Constrained Counterfactual Optimization for Proteins (MCCOP), a framework that computes minimal, biologically plausible sequence edits that flip a model's prediction to a desired target state. MCCOP operates in a continuous joint sequence-structure latent space and employs a pretrained diffusion model as a manifold prior, balancing three objectives: validity (achieving the target property), p...

---

## 368. BALD-SAM: Disagreement-based Active Prompting in Interactive 分割

**原标题**: BALD-SAM: Disagreement-based Active Prompting in Interactive Segmentation

**作者**: Prithwijit Chowdhury, Mohit Prabhushankar, Ghassan AlRegib
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10828v1

**中文摘要**:
> arXiv:2603.10828v1 Announce Type: cross 
摘要: The Segment Anything 模型 (SAM) has revolutionized interactive 分割 through spatial prompting. While existing work primarily focuses on automating prompts in various settings, real-world annotation workflows involve iterative refinement where annotators observe 模型 outputs and strategically place prompts to resolve ambiguities. Current pipelines typically rely on the annotator's 视觉 assessment of the predicted mask quality. We postulate that a principled 方案 for automated interactive prompting is to use a 模型-derived criterion to identify the most informative region for the next prompt. In this work, we establish active prompting: a spatial active 学习 方案 where locations within images constitute an unlabeled pool and prompts serve as queries to prioritize...

**Original Abstract**:
> arXiv:2603.10828v1 Announce Type: cross 
Abstract: The Segment Anything Model (SAM) has revolutionized interactive segmentation through spatial prompting. While existing work primarily focuses on automating prompts in various settings, real-world annotation workflows involve iterative refinement where annotators observe model outputs and strategically place prompts to resolve ambiguities. Current pipelines typically rely on the annotator's visual assessment of the predicted mask quality. We postulate that a principled approach for automated interactive prompting is to use a model-derived criterion to identify the most informative region for the next prompt. In this work, we establish active prompting: a spatial active learning approach where locations within images constitute an unlabeled ...

---

## 369. On the Reliability of Cue Conflict and Beyond

**原标题**: On the Reliability of Cue Conflict and Beyond

**作者**: Pum Jun Kim, Seung-Ah Lee, Seongho Park, Dongyoon Han, Jaejun Yoo
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10834v1

**中文摘要**:
> arXiv:2603.10834v1 Announce Type: cross 
摘要: Understanding how 神经 networks rely on 视觉 cues offers a human-可解释 view of their internal 决策 processes. The cue-conflict 基准 has been influential in probing shape-texture preference and in motivating the insight that stronger, human-like shape 偏见 is often associated with improved in-domain 性能. However, we find that the current stylization-based instantiation can yield unstable and ambiguous 偏见 estimates. Specifically, stylization may not reliably instantiate perceptually valid and separable cues nor 控制 their relative informativeness, ratio-based 偏见 can obscure absolute cue sensitivity, and restricting 评估 to preselected classes can distort 模型 predictions by ignoring the full 决策 space. Together, these factors can confound preference with cue validity...

**Original Abstract**:
> arXiv:2603.10834v1 Announce Type: cross 
Abstract: Understanding how neural networks rely on visual cues offers a human-interpretable view of their internal decision processes. The cue-conflict benchmark has been influential in probing shape-texture preference and in motivating the insight that stronger, human-like shape bias is often associated with improved in-domain performance. However, we find that the current stylization-based instantiation can yield unstable and ambiguous bias estimates. Specifically, stylization may not reliably instantiate perceptually valid and separable cues nor control their relative informativeness, ratio-based bias can obscure absolute cue sensitivity, and restricting evaluation to preselected classes can distort model predictions by ignoring the full decisio...

---

## 370. Human Presence 检测 via Wi-Fi Range-Filtered Doppler Spectrum on Commodity Laptops

**原标题**: Human Presence Detection via Wi-Fi Range-Filtered Doppler Spectrum on Commodity Laptops

**作者**: Jessica Sanson, Rahul C. Shah, Valerio Frascolla
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10845v1

**中文摘要**:
> arXiv:2603.10845v1 Announce Type: cross 
摘要: Human Presence 检测 (HPD) is key to enable intelligent power management and security features in everyday devices. In this 论文 we propose the first HPD solution that leverages monostatic Wi-Fi sensing and detects user position using only the built-in Wi-Fi hardware of a device, with no need for external devices, access points, or additional sensors. In contrast, existing HPD solutions for laptops require external dedicated sensors which add cost and complexity, or rely on camera-based approaches that introduce significant 隐私 concerns. We herewith introduce the Range-Filtered Doppler Spectrum (RF-DS), a novel Wi-Fi sensing 技术 for presence estimation that enables both range-selective and temporally windowed 检测 of user presence. By applying targeted r...

**Original Abstract**:
> arXiv:2603.10845v1 Announce Type: cross 
Abstract: Human Presence Detection (HPD) is key to enable intelligent power management and security features in everyday devices. In this paper we propose the first HPD solution that leverages monostatic Wi-Fi sensing and detects user position using only the built-in Wi-Fi hardware of a device, with no need for external devices, access points, or additional sensors. In contrast, existing HPD solutions for laptops require external dedicated sensors which add cost and complexity, or rely on camera-based approaches that introduce significant privacy concerns. We herewith introduce the Range-Filtered Doppler Spectrum (RF-DS), a novel Wi-Fi sensing technique for presence estimation that enables both range-selective and temporally windowed detection of us...

---

## 371. Towards Cold-Start Drafting and Continual Refining: A 价值-Driven 内存 方案 with Application to NPU Kernel 合成

**原标题**: Towards Cold-Start Drafting and Continual Refining: A Value-Driven Memory Approach with Application to NPU Kernel Synthesis

**作者**: Yujie Zheng, Zhuo Li, Shengtao Zhang, Hanjing Wang, Junjie Sheng, Jiaqian Wang, Junchi Yan, Weinan Zhang, Ying Wen, Bo Tang, Muning Wen
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10846v1

**中文摘要**:
> arXiv:2603.10846v1 Announce Type: cross 
摘要: Deploying Large Language Models to data-scarce programming domains poses significant challenges, particularly for kernel 合成 on emerging Domain-Specific Architectures where a "Data Wall" limits available 训练 data. While models excel on data-rich platforms like CUDA, they suffer catastrophic 性能 drops on data-scarce ecosystems such as NPU programming. To overcome this cold-start barrier without expensive fine-tuning, we introduce EvoKernel, a self-evolving agentic 框架 that automates the lifecycle of kernel 合成 from initial drafting to continual refining. EvoKernel addresses this by formulating the 合成 process as a 内存-based 强化 学习 task. Through a novel 价值-driven 检索 mechanism, it learns stage-specific Q-values that prioritize experiences based on their co...

**Original Abstract**:
> arXiv:2603.10846v1 Announce Type: cross 
Abstract: Deploying Large Language Models to data-scarce programming domains poses significant challenges, particularly for kernel synthesis on emerging Domain-Specific Architectures where a "Data Wall" limits available training data. While models excel on data-rich platforms like CUDA, they suffer catastrophic performance drops on data-scarce ecosystems such as NPU programming. To overcome this cold-start barrier without expensive fine-tuning, we introduce EvoKernel, a self-evolving agentic framework that automates the lifecycle of kernel synthesis from initial drafting to continual refining. EvoKernel addresses this by formulating the synthesis process as a memory-based reinforcement learning task. Through a novel value-driven retrieval mechanism,...

---

## 372. Semantic Landmark Particle Filter for Robot Localisation in Vineyards

**原标题**: Semantic Landmark Particle Filter for Robot Localisation in Vineyards

**作者**: Rajitha de Silva, Jonathan Cox, James R. Heselden, Marija Popovi\'c, Cesar Cadena, Riccardo Polvara
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10847v1

**中文摘要**:
> arXiv:2603.10847v1 Announce Type: cross 
摘要: Reliable localisation in vineyards is hindered by row-level perceptual aliasing: 并行 crop rows produce nearly identical LiDAR observations, causing geometry-only and vision-based SLAM systems to converge towards incorrect corridors, particularly during headland transitions. We present a Semantic Landmark Particle Filter (SLPF) that integrates trunk and pole landmark detections with 2D LiDAR within a 概率 localisation 框架. Detected trunks are converted into semantic walls, forming structural row boundaries embedded in the measurement 模型 to improve discrimination between adjacent rows. GNSS is incorporated as a lightweight prior that stabilises localisation when semantic observations are sparse.
  Field experiments in a 10-row vineyard demonstrate con...

**Original Abstract**:
> arXiv:2603.10847v1 Announce Type: cross 
Abstract: Reliable localisation in vineyards is hindered by row-level perceptual aliasing: parallel crop rows produce nearly identical LiDAR observations, causing geometry-only and vision-based SLAM systems to converge towards incorrect corridors, particularly during headland transitions. We present a Semantic Landmark Particle Filter (SLPF) that integrates trunk and pole landmark detections with 2D LiDAR within a probabilistic localisation framework. Detected trunks are converted into semantic walls, forming structural row boundaries embedded in the measurement model to improve discrimination between adjacent rows. GNSS is incorporated as a lightweight prior that stabilises localisation when semantic observations are sparse.
  Field experiments in ...

---

## 373. An Extreme Multi-label Text 分类 (XMTC) Library 数据集: What if we took "Use of Practical AI in Digital Libraries" seriously?

**原标题**: An Extreme Multi-label Text Classification (XMTC) Library Dataset: What if we took "Use of Practical AI in Digital Libraries" seriously?

**作者**: Jennifer D'Souza, Sameer Sadruddin, Maximilian K\"ahler, Andrea Salfinger, Luca Zaccagna, Francesca Incitti, Lauro Snidaro, Osma Suominen
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10876v1

**中文摘要**:
> arXiv:2603.10876v1 Announce Type: cross 
摘要: Subject indexing is vital for discovery but hard to sustain at scale and across languages. We release a large bilingual (English/German) 语料库 of catalog records annotated with the Integrated Authority File (GND), plus a machine-actionable GND taxonomy. The resource enables 本体-aware multi-label 分类, mapping text to authority terms, and 智能体-assisted cataloging with reproducible, authority-grounded 评估. We provide a brief statistical profile and qualitative error analyses of three systems. We invite the community to assess not only accuracy but usefulness and transparency, toward authority-anchored AI co-pilots that amplify catalogers' work.

**Original Abstract**:
> arXiv:2603.10876v1 Announce Type: cross 
Abstract: Subject indexing is vital for discovery but hard to sustain at scale and across languages. We release a large bilingual (English/German) corpus of catalog records annotated with the Integrated Authority File (GND), plus a machine-actionable GND taxonomy. The resource enables ontology-aware multi-label classification, mapping text to authority terms, and agent-assisted cataloging with reproducible, authority-grounded evaluation. We provide a brief statistical profile and qualitative error analyses of three systems. We invite the community to assess not only accuracy but usefulness and transparency, toward authority-anchored AI co-pilots that amplify catalogers' work.

---

## 374. Continuous Diffusion Transformers for Designing Synthetic Regulatory Elements

**原标题**: Continuous Diffusion Transformers for Designing Synthetic Regulatory Elements

**作者**: Jonathan Liu, Kia Ghods
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10885v1

**中文摘要**:
> arXiv:2603.10885v1 Announce Type: cross 
摘要: We present a parameter-高效 Diffusion Transformer (DiT) for generating 200bp cell-type-specific regulatory DNA sequences. By replacing the U-Net backbone of DNA-Diffusion with a Transformer denoiser equipped with a 2D CNN input encoder, our 模型 matches the U-Net's best validation 损失 in 13 epochs (60$\times$ fewer) and converges 39% lower, while reducing memorization from 5.3% to 1.7% of generated sequences aligning to 训练 data via BLAT. Ablations show the CNN encoder is essential: without it, validation 损失 increases 70% regardless of positional 嵌入 choice. We further apply DDPO finetuning using Enformer as a 奖励 模型, achieving a 38$\times$ improvement in predicted regulatory activity. Cross-validation against DRAKES on an independent prediction task co...

**Original Abstract**:
> arXiv:2603.10885v1 Announce Type: cross 
Abstract: We present a parameter-efficient Diffusion Transformer (DiT) for generating 200bp cell-type-specific regulatory DNA sequences. By replacing the U-Net backbone of DNA-Diffusion with a transformer denoiser equipped with a 2D CNN input encoder, our model matches the U-Net's best validation loss in 13 epochs (60$\times$ fewer) and converges 39% lower, while reducing memorization from 5.3% to 1.7% of generated sequences aligning to training data via BLAT. Ablations show the CNN encoder is essential: without it, validation loss increases 70% regardless of positional embedding choice. We further apply DDPO finetuning using Enformer as a reward model, achieving a 38$\times$ improvement in predicted regulatory activity. Cross-validation against DRA...

---

## 375. Dynamics-Predictive 采样 for Active RL Finetuning of Large 推理 Models

**原标题**: Dynamics-Predictive Sampling for Active RL Finetuning of Large Reasoning Models

**作者**: Yixiu Mao, Yun Qu, Qi Wang, Heming Zou, Xiangyang Ji
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10887v1

**中文摘要**:
> arXiv:2603.10887v1 Announce Type: cross 
摘要: 强化 学习 (RL) finetuning has become a key 技术 for enhancing the 推理 abilities of large language models (LLMs). However, its effectiveness critically depends on the 选择 of 训练 data. Recent advances underscore the importance of 在线 prompt 选择 methods, which typically concentrate 训练 on partially solved or moderately challenging examples under the current 策略, thereby yielding more effective 模型 updates. While significantly accelerating RL finetuning in terms of 训练 steps, they also incur substantial computational overhead by requiring extensive 大语言模型 rollouts over large candidate batches to identify informative samples, an expense that can outweigh the finetuning process itself. To address this challenge, this work proposes Dynamics-Predictive 采样 (DPS), which ...

**Original Abstract**:
> arXiv:2603.10887v1 Announce Type: cross 
Abstract: Reinforcement learning (RL) finetuning has become a key technique for enhancing the reasoning abilities of large language models (LLMs). However, its effectiveness critically depends on the selection of training data. Recent advances underscore the importance of online prompt selection methods, which typically concentrate training on partially solved or moderately challenging examples under the current policy, thereby yielding more effective model updates. While significantly accelerating RL finetuning in terms of training steps, they also incur substantial computational overhead by requiring extensive LLM rollouts over large candidate batches to identify informative samples, an expense that can outweigh the finetuning process itself. To a...

---

## 376. LookaheadKV: Fast and 准确 KV Cache Eviction by Glimpsing into the Future without 生成

**原标题**: LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation

**作者**: Jinwoo Ahn, Ingyu Seong, Akhil Kedia, Junhan Kim, Hyemi Jang, Kangwook Lee, Yongkweon Jeon
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10899v1

**中文摘要**:
> arXiv:2603.10899v1 Announce Type: cross 
摘要: Transformer-based large language models (LLMs) rely on key-价值 (KV) caching to avoid redundant computation during autoregressive 推理. While this mechanism greatly improves efficiency, the cache size grows linearly with the input sequence length, quickly becoming a bottleneck for long-context tasks. Existing solutions mitigate this problem by evicting prompt KV that are deemed unimportant, guided by estimated importance scores. Notably, a recent line of work proposes to improve eviction quality by "glimpsing into the future", in which a draft generator produces a surrogate future response approximating the 目标 模型's true response, and this surrogate is subsequently used to estimate the importance of cached KV more accurately. However, these approache...

**Original Abstract**:
> arXiv:2603.10899v1 Announce Type: cross 
Abstract: Transformer-based large language models (LLMs) rely on key-value (KV) caching to avoid redundant computation during autoregressive inference. While this mechanism greatly improves efficiency, the cache size grows linearly with the input sequence length, quickly becoming a bottleneck for long-context tasks. Existing solutions mitigate this problem by evicting prompt KV that are deemed unimportant, guided by estimated importance scores. Notably, a recent line of work proposes to improve eviction quality by "glimpsing into the future", in which a draft generator produces a surrogate future response approximating the target model's true response, and this surrogate is subsequently used to estimate the importance of cached KV more accurately. H...

---

## 377. When Fine-Tuning Fails and when it Generalises: 角色 of Data Diversity and Mixed 训练 in 大语言模型-based 文本转语音

**原标题**: When Fine-Tuning Fails and when it Generalises: Role of Data Diversity and Mixed Training in LLM-based TTS

**作者**: Anupam Purwar, Aditya Choudhary
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10904v1

**中文摘要**:
> arXiv:2603.10904v1 Announce Type: cross 
摘要: Large language models are increasingly adopted as semantic backbones for 神经 text-to-语音 systems. However, frozen 大语言模型 representations are insufficient for modeling 说话人 specific acoustic and perceptual characteristics. Our experiments involving fine tuning of the Language 模型 backbone of 文本转语音 show promise in improving the 声纹 consistency and Signal to Noise ratio SNR in 声纹 cloning task. Across multiple speakers LoRA finetuning consistently outperforms the non-finetuned base 通义千问-0.5B 模型 across three complementary dimensions of 语音 quality. First, perceptual quality improves significantly with DNS-MOS gains of up to 0.42 points for speakers whose 训练 data exhibits sufficient acoustic variability. Second, 说话人 fidelity improves for all evaluated speake...

**Original Abstract**:
> arXiv:2603.10904v1 Announce Type: cross 
Abstract: Large language models are increasingly adopted as semantic backbones for neural text-to-speech systems. However, frozen LLM representations are insufficient for modeling speaker specific acoustic and perceptual characteristics. Our experiments involving fine tuning of the Language Model backbone of TTS show promise in improving the voice consistency and Signal to Noise ratio SNR in voice cloning task. Across multiple speakers LoRA finetuning consistently outperforms the non-finetuned base Qwen-0.5B model across three complementary dimensions of speech quality. First, perceptual quality improves significantly with DNS-MOS gains of up to 0.42 points for speakers whose training data exhibits sufficient acoustic variability. Second, speaker fi...

---

## 378. Safe RLHF Beyond Expectation: Stochastic Dominance for Universal Spectral Risk 控制

**原标题**: Safe RLHF Beyond Expectation: Stochastic Dominance for Universal Spectral Risk Control

**作者**: Yaswanth Chittepu, Ativ Joshi, Rajarshi Bhattacharjee, Scott Niekum
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10938v1

**中文摘要**:
> arXiv:2603.10938v1 Announce Type: cross 
摘要: Safe 强化 学习 from Human Feedback (RLHF) typically enforces safety through expected cost constraints, but the expectation captures only a single statistic of the cost distribution and fails to account for distributional uncertainty, particularly under heavy tails or rare catastrophic events. This limitation is problematic when 鲁棒性 and risk sensitivity are critical. Stochastic dominance offers a principled alternative by comparing entire cost distributions rather than just their averages, enabling direct 控制 over tail risks and potential 分布外 failures that expectation-based constraints may overlook. In this work, we propose Risk-sensitive Alignment via Dominance (RAD), a novel alignment 框架 that replaces scalar expected cost constraints with First-Orde...

**Original Abstract**:
> arXiv:2603.10938v1 Announce Type: cross 
Abstract: Safe Reinforcement Learning from Human Feedback (RLHF) typically enforces safety through expected cost constraints, but the expectation captures only a single statistic of the cost distribution and fails to account for distributional uncertainty, particularly under heavy tails or rare catastrophic events. This limitation is problematic when robustness and risk sensitivity are critical. Stochastic dominance offers a principled alternative by comparing entire cost distributions rather than just their averages, enabling direct control over tail risks and potential out-of-distribution failures that expectation-based constraints may overlook. In this work, we propose Risk-sensitive Alignment via Dominance (RAD), a novel alignment framework that...

---

## 379. GroundCount: Grounding Vision-Language Models with Object 检测 for Mitigating Counting Hallucinations

**原标题**: GroundCount: Grounding Vision-Language Models with Object Detection for Mitigating Counting Hallucinations

**作者**: Boyuan Chen, Minghao Shao, Siddharth Garg, Ramesh Karri, Muhammad Shafique
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10978v1

**中文摘要**:
> arXiv:2603.10978v1 Announce Type: cross 
摘要: Vision Language Models (VLMs) exhibit persistent hallucinations in counting tasks, with accuracy substantially lower than other 视觉 推理 tasks (excluding sentiment). This phenomenon persists even in 状态-of-the-art 推理-capable VLMs. Conversely, CNN-based object 检测 models (ODMs) such as YOLO excel at spatial localization and instance counting with minimal computational overhead. We propose GroundCount, a 框架 that augments VLMs with explicit spatial grounding from ODMs to mitigate counting hallucinations. In the best case, our prompt-based augmentation strategy achieves 81.3% counting accuracy on the best-performing 模型 (Ovis2.5-2B) - a 6.6pp improvement - while reducing 推理 time by 22% through elimination of hallucination-driven 推理 loops for stronger mode...

**Original Abstract**:
> arXiv:2603.10978v1 Announce Type: cross 
Abstract: Vision Language Models (VLMs) exhibit persistent hallucinations in counting tasks, with accuracy substantially lower than other visual reasoning tasks (excluding sentiment). This phenomenon persists even in state-of-the-art reasoning-capable VLMs. Conversely, CNN-based object detection models (ODMs) such as YOLO excel at spatial localization and instance counting with minimal computational overhead. We propose GroundCount, a framework that augments VLMs with explicit spatial grounding from ODMs to mitigate counting hallucinations. In the best case, our prompt-based augmentation strategy achieves 81.3% counting accuracy on the best-performing model (Ovis2.5-2B) - a 6.6pp improvement - while reducing inference time by 22% through elimination...

---

## 380. Artificial Intelligence as a Catalyst for Innovation in Software Engineering

**原标题**: Artificial Intelligence as a Catalyst for Innovation in Software Engineering

**作者**: Carlos Alberto Fern\'andez-y-Fern\'andez, Jorge R. Aguilar-Cisneros
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.10994v1

**中文摘要**:
> arXiv:2603.10994v1 Announce Type: cross 
摘要: The rapid 进化 and inherent complexity of modern software requirements demand highly flexible and responsive development methodologies. While Agile frameworks have become the industry standard for prioritizing 迭代, collaboration, and adaptability, software development teams continue to face persistent challenges in managing constantly evolving requirements and maintaining product quality under tight deadlines. This article explores the intersection of Artificial Intelligence (AI) and Software Engineering (说话人识别), to analyze how AI serves as a powerful catalyst for enhancing agility and fostering innovation. The research combines a comprehensive 审稿 of existing literature with an empirical study, utilizing a survey directed at Software Engineering pr...

**Original Abstract**:
> arXiv:2603.10994v1 Announce Type: cross 
Abstract: The rapid evolution and inherent complexity of modern software requirements demand highly flexible and responsive development methodologies. While Agile frameworks have become the industry standard for prioritizing iteration, collaboration, and adaptability, software development teams continue to face persistent challenges in managing constantly evolving requirements and maintaining product quality under tight deadlines. This article explores the intersection of Artificial Intelligence (AI) and Software Engineering (SE), to analyze how AI serves as a powerful catalyst for enhancing agility and fostering innovation. The research combines a comprehensive review of existing literature with an empirical study, utilizing a survey directed at So...

---

## 381. RCTs & Human Uplift Studies: Methodological Challenges and Practical Solutions for Frontier AI 评估

**原标题**: RCTs & Human Uplift Studies: Methodological Challenges and Practical Solutions for Frontier AI Evaluation

**作者**: Patricia Paskov, Kevin Wei, Shen Zhou Hong, Dan Bateyko, Xavier Roberts-Gaal, Carson Ezell, Gailius Praninskas, Valerie Chen, Umang Bhatt, Ella Guest
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.11001v1

**中文摘要**:
> arXiv:2603.11001v1 Announce Type: cross 
摘要: Human uplift studies - or studies that measure AI effects on human 性能 relative to a status quo, typically using randomized controlled trial (RCT) methodology - are increasingly used to inform 部署, governance, and safety decisions for frontier AI systems. While the methods underlying these studies are well-established, their interaction with the distinctive properties of frontier AI systems remains underexamined, particularly when results are used to inform high-stakes decisions. We present findings from interviews with 16 expert practitioners with experience conducting human uplift studies in domains including biosecurity, cybersecurity, education, and labor. Across interviews, experts described a recurring tension between standard 因果 推理 assumpti...

**Original Abstract**:
> arXiv:2603.11001v1 Announce Type: cross 
Abstract: Human uplift studies - or studies that measure AI effects on human performance relative to a status quo, typically using randomized controlled trial (RCT) methodology - are increasingly used to inform deployment, governance, and safety decisions for frontier AI systems. While the methods underlying these studies are well-established, their interaction with the distinctive properties of frontier AI systems remains underexamined, particularly when results are used to inform high-stakes decisions. We present findings from interviews with 16 expert practitioners with experience conducting human uplift studies in domains including biosecurity, cybersecurity, education, and labor. Across interviews, experts described a recurring tension between ...

---

## 382. Does AI See like Art Historians? Interpreting How Vision Language Models Recognize Artistic Style

**原标题**: Does AI See like Art Historians? Interpreting How Vision Language Models Recognize Artistic Style

**作者**: Marvin Limpijankit, Milad Alshomary, Yassin Oulad Daoud, Amith Ananthram, Tim Trombley, Elias Stengel-Eskin, Mohit Bansal, Noam M. Elcott, Kathleen McKeown
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.11024v1

**中文摘要**:
> arXiv:2603.11024v1 Announce Type: cross 
摘要: VLMs have become increasingly proficient at a range of computer vision tasks, such as 视觉 question answering and object 检测. This includes increasingly strong capabilities in the domain of art, from analyzing artwork to 生成 of art. In an interdisciplinary collaboration between computer scientists and art historians, we characterize the mechanisms underlying VLMs' ability to predict artistic style and assess the extent to which they align with the criteria art historians use to reason about artistic style. We employ a 隐变量-space decomposition 方案 to identify concepts that drive art style prediction and conduct quantitative evaluations, 因果 analysis and assessment by art historians. Our findings indicate that 73% of the extracted concepts are judged by ...

**Original Abstract**:
> arXiv:2603.11024v1 Announce Type: cross 
Abstract: VLMs have become increasingly proficient at a range of computer vision tasks, such as visual question answering and object detection. This includes increasingly strong capabilities in the domain of art, from analyzing artwork to generation of art. In an interdisciplinary collaboration between computer scientists and art historians, we characterize the mechanisms underlying VLMs' ability to predict artistic style and assess the extent to which they align with the criteria art historians use to reason about artistic style. We employ a latent-space decomposition approach to identify concepts that drive art style prediction and conduct quantitative evaluations, causal analysis and assessment by art historians. Our findings indicate that 73% of...

---

## 383. 神经 Field Thermal Tomography: A Differentiable Physics 框架 for Non-Destructive 评估

**原标题**: Neural Field Thermal Tomography: A Differentiable Physics Framework for Non-Destructive Evaluation

**作者**: Tao Zhong, Yixun Hu, Dongzhe Zheng, Aditya Sood, Christine Allen-Blanchette
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.11045v1

**中文摘要**:
> arXiv:2603.11045v1 Announce Type: cross 
摘要: We propose 神经 Field Thermal Tomography (NeFTY), a differentiable physics 框架 for the quantitative 3D reconstruction of material properties from transient surface temperature measurements. While traditional thermography relies on pixel-wise 1D approximations that neglect lateral diffusion, and soft-constrained Physics-Informed 神经 Networks (PINNs) often fail in transient diffusion scenarios due to 梯度 stiffness, NeFTY parameterizes the 3D diffusivity field as a continuous 神经 field optimized through a rigorous numerical solver. By leveraging a differentiable physics solver, our 方案 enforces thermodynamic laws as hard constraints while maintaining the 内存 efficiency required for high-resolution 3D tomography. Our discretize-then-optimize paradigm effect...

**Original Abstract**:
> arXiv:2603.11045v1 Announce Type: cross 
Abstract: We propose Neural Field Thermal Tomography (NeFTY), a differentiable physics framework for the quantitative 3D reconstruction of material properties from transient surface temperature measurements. While traditional thermography relies on pixel-wise 1D approximations that neglect lateral diffusion, and soft-constrained Physics-Informed Neural Networks (PINNs) often fail in transient diffusion scenarios due to gradient stiffness, NeFTY parameterizes the 3D diffusivity field as a continuous neural field optimized through a rigorous numerical solver. By leveraging a differentiable physics solver, our approach enforces thermodynamic laws as hard constraints while maintaining the memory efficiency required for high-resolution 3D tomography. Our...

---

## 384. COMIC: Agentic Sketch Comedy 生成

**原标题**: COMIC: Agentic Sketch Comedy Generation

**作者**: Susung Hong, Brian Curless, Ira Kemelmacher-Shlizerman, Steve Seitz
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.11048v1

**中文摘要**:
> arXiv:2603.11048v1 Announce Type: cross 
摘要: We propose a fully automated AI 系统 that produces short comedic videos similar to sketch shows such as Saturday Night Live. Starting with character references, the 系统 employs a 种群 of agents loosely based on real production studio roles, structured to optimize the quality and diversity of ideas and outputs through iterative competition, 评估, and improvement. A key contribution is the 引言 of 大语言模型 critics aligned with real viewer preferences through the analysis of a 语料库 of comedy videos on YouTube to automatically evaluate humor. Our experiments show that our 框架 produces results approaching the quality of professionally produced sketches while demonstrating 状态-of-the-art 性能 in 视频 生成.

**Original Abstract**:
> arXiv:2603.11048v1 Announce Type: cross 
Abstract: We propose a fully automated AI system that produces short comedic videos similar to sketch shows such as Saturday Night Live. Starting with character references, the system employs a population of agents loosely based on real production studio roles, structured to optimize the quality and diversity of ideas and outputs through iterative competition, evaluation, and improvement. A key contribution is the introduction of LLM critics aligned with real viewer preferences through the analysis of a corpus of comedy videos on YouTube to automatically evaluate humor. Our experiments show that our framework produces results approaching the quality of professionally produced sketches while demonstrating state-of-the-art performance in video generat...

---

## 385. Mindstorms in Natural Language-Based Societies of Mind

**原标题**: Mindstorms in Natural Language-Based Societies of Mind

**作者**: Mingchen Zhuge, Haozhe Liu, Francesco Faccio, Dylan R. Ashley, R\'obert Csord\'as, Anand Gopalakrishnan, Abdullah Hamdi, Hasan Abed Al Kader Hammoud, Vincent Herrmann, Kazuki Irie, Louis Kirsch, Bing Li, Guohao Li, Shuming Liu, Jinjie Mai, Piotr Pi\k{e}kos, Aditya Ramesh, Imanol Schlag, Weimin Shi, Aleksandar Stani\'c, Wenyi Wang, Yuhui Wang, Mengmeng Xu, Deng-Ping Fan, Bernard Ghanem, J\"urgen Schmidhuber
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2305.17066v2

**中文摘要**:
> arXiv:2305.17066v2 Announce Type: replace 
摘要: Both Minsky's "society of mind" and Schmidhuber's "学习 to think" inspire diverse societies of large multimodal 神经 networks (NNs) that solve problems by interviewing each other in a "mindstorm." Recent implementations of NN-based societies of minds consist of large language models (LLMs) and other NN-based experts communicating through a natural language interface. In doing so, they overcome the limitations of single LLMs, improving multimodal 零样本 推理. In these natural language-based societies of mind (NLSOMs), new agents -- all communicating through the same universal symbolic language -- are easily added in a modular fashion. To demonstrate the power of NLSOMs, we assemble and 实验 with several of them (having up to 129 members), leveraging minds...

**Original Abstract**:
> arXiv:2305.17066v2 Announce Type: replace 
Abstract: Both Minsky's "society of mind" and Schmidhuber's "learning to think" inspire diverse societies of large multimodal neural networks (NNs) that solve problems by interviewing each other in a "mindstorm." Recent implementations of NN-based societies of minds consist of large language models (LLMs) and other NN-based experts communicating through a natural language interface. In doing so, they overcome the limitations of single LLMs, improving multimodal zero-shot reasoning. In these natural language-based societies of mind (NLSOMs), new agents -- all communicating through the same universal symbolic language -- are easily added in a modular fashion. To demonstrate the power of NLSOMs, we assemble and experiment with several of them (having...

---

## 386. Personalizing explanations of AI-driven hints to users' characteristics: an empirical 评估

**原标题**: Personalizing explanations of AI-driven hints to users' characteristics: an empirical evaluation

**作者**: Vedant Bahel, Harshinee Sriram, Cristina Conati
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2403.04035v3

**中文摘要**:
> arXiv:2403.04035v3 Announce Type: replace 
摘要: The 论文 extends an existing Intelligent Tutoring 系统 (ITS) that supports students' 学习 via AI-driven personalized hints and can generate explanations to justify why/how the hints were generated. In this work, we investigate personalizing these hint explanations to students with low levels of two traits, Need for Cognition and Conscientiousness in order to enhance their engagement with the explanations, based on prior findings that these students generally do not ask for the explanations although they would benefit from them. We evaluate the effectiveness of the personalized hint explanations with a formal user study. Our results show that the personalization increases our 目标 users' interaction with the hint explanations, their understanding of th...

**Original Abstract**:
> arXiv:2403.04035v3 Announce Type: replace 
Abstract: The paper extends an existing Intelligent Tutoring System (ITS) that supports students' learning via AI-driven personalized hints and can generate explanations to justify why/how the hints were generated. In this work, we investigate personalizing these hint explanations to students with low levels of two traits, Need for Cognition and Conscientiousness in order to enhance their engagement with the explanations, based on prior findings that these students generally do not ask for the explanations although they would benefit from them. We evaluate the effectiveness of the personalized hint explanations with a formal user study. Our results show that the personalization increases our target users' interaction with the hint explanations, th...

---

## 387. Synthesizing 可解释 控制 Policies through Large Language 模型 Guided 搜索

**原标题**: Synthesizing Interpretable Control Policies through Large Language Model Guided Search

**作者**: Carlo Bosio, Mark W. Mueller
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2410.05406v3

**中文摘要**:
> arXiv:2410.05406v3 Announce Type: replace 
摘要: The combination of Large Language Models (LLMs), systematic 评估, and evolutionary algorithms has enabled breakthroughs in combinatorial 优化 and scientific discovery. We propose to extend this powerful combination to the 控制 of dynamical systems, generating 可解释 控制 policies capable of complex behaviors. With our novel 方法, we represent 控制 policies as programs in standard languages like Python. We evaluate candidate controllers in simulation and evolve them using a pre-trained 大语言模型. Unlike conventional 学习-based 控制 techniques, which rely on black-box 神经 networks to 编码 控制 policies, our 方案 enhances transparency and interpretability. We still take 优势 of the power of large AI models, but only at the 策略 design phase, ensuring that all 系统 components remain...

**Original Abstract**:
> arXiv:2410.05406v3 Announce Type: replace 
Abstract: The combination of Large Language Models (LLMs), systematic evaluation, and evolutionary algorithms has enabled breakthroughs in combinatorial optimization and scientific discovery. We propose to extend this powerful combination to the control of dynamical systems, generating interpretable control policies capable of complex behaviors. With our novel method, we represent control policies as programs in standard languages like Python. We evaluate candidate controllers in simulation and evolve them using a pre-trained LLM. Unlike conventional learning-based control techniques, which rely on black-box neural networks to encode control policies, our approach enhances transparency and interpretability. We still take advantage of the power of ...

---

## 388. 学习 What 强化 学习 Can't: Interleaved 在线 Fine-Tuning for Hardest Questions

**原标题**: Learning What Reinforcement Learning Can't: Interleaved Online Fine-Tuning for Hardest Questions

**作者**: Lu Ma, Hao Liang, Meiyi Qiang, Lexiang Tang, Xiaochen Ma, Zhen Hao Wong, Junbo Niu, Chengyu Shen, Runming He, Yanhao Li, Bin Cui, Wentao Zhang
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2506.07527v3

**中文摘要**:
> arXiv:2506.07527v3 Announce Type: replace 
摘要: Recent advances in large language 模型 (大语言模型) 推理 have shown that sophisticated behaviors such as 规划 and self-reflection can emerge through 强化 学习 (RL). However, despite these successes, RL in its current form remains insufficient to induce capabilities that exceed the limitations of the base 模型, as it is primarily optimized based on existing knowledge of the 模型 rather than facilitating the acquisition of new information. To address this limitation, we employ 有监督 fine-tuning (SFT) to learn what RL cannot, which enables the incorporation of new knowledge and 推理 patterns by leveraging high-quality demonstration data. We analyze the 训练 dynamics of RL and SFT for 大语言模型 推理 and find that RL excels at maintaining and improving 性能 on questions within the...

**Original Abstract**:
> arXiv:2506.07527v3 Announce Type: replace 
Abstract: Recent advances in large language model (LLM) reasoning have shown that sophisticated behaviors such as planning and self-reflection can emerge through reinforcement learning (RL). However, despite these successes, RL in its current form remains insufficient to induce capabilities that exceed the limitations of the base model, as it is primarily optimized based on existing knowledge of the model rather than facilitating the acquisition of new information. To address this limitation, we employ supervised fine-tuning (SFT) to learn what RL cannot, which enables the incorporation of new knowledge and reasoning patterns by leveraging high-quality demonstration data. We analyze the training dynamics of RL and SFT for LLM reasoning and find th...

---

## 389. From Next Token Prediction to (STRIPS) World Models

**原标题**: From Next Token Prediction to (STRIPS) World Models

**作者**: Carlos N\'u\~nez-Molina, Vicen\c{c} G\'omez, Hector Geffner
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2509.13389v4

**中文摘要**:
> arXiv:2509.13389v4 Announce Type: replace 
摘要: We study whether next-token prediction can yield world models that truly support 规划, in a controlled symbolic setting where propositional STRIPS 动作 models are learned from 动作 traces alone and correctness can be evaluated exactly. We introduce two architectures. The first is the STRIPS Transformer, a symbolically aligned 模型 grounded in theoretical results linking transformers and the formal language structure of STRIPS domains. The second is a standard Transformer 架构 without explicit symbolic structure built in, for which we study different positional encoding schemes and 注意力 aggregation mechanisms. We evaluate both architectures on five classical 规划 domains, measuring 训练 accuracy, 泛化, and 规划 性能 across domains and problem sizes. Interestingly, ...

**Original Abstract**:
> arXiv:2509.13389v4 Announce Type: replace 
Abstract: We study whether next-token prediction can yield world models that truly support planning, in a controlled symbolic setting where propositional STRIPS action models are learned from action traces alone and correctness can be evaluated exactly. We introduce two architectures. The first is the STRIPS Transformer, a symbolically aligned model grounded in theoretical results linking transformers and the formal language structure of STRIPS domains. The second is a standard transformer architecture without explicit symbolic structure built in, for which we study different positional encoding schemes and attention aggregation mechanisms. We evaluate both architectures on five classical planning domains, measuring training accuracy, generalizati...

---

## 390. RADAR: 推理-Ability and Difficulty-Aware Routing for 推理 LLMs

**原标题**: RADAR: Reasoning-Ability and Difficulty-Aware Routing for Reasoning LLMs

**作者**: Nigel Fernandez, Branislav Kveton, Ryan A. Rossi, Andrew S. Lan, Zichao Wang
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2509.25426v3

**中文摘要**:
> arXiv:2509.25426v3 Announce Type: replace 
摘要: 推理 language models have demonstrated remarkable 性能 on many challenging tasks in math, science, and coding. Choosing the right 推理 模型 for practical 部署 involves a 性能 and cost tradeoff at two key levels: 模型 size and 推理 budget, where larger models and higher 推理 budget lead to better 性能 but with increased cost and 延迟. In this work, we tackle this tradeoff from the angle of 模型 configuration routing for different queries, and present RADAR (推理-Ability and Difficulty-Aware Routing), a lightweight, 可解释, and 可扩展 routing 框架. Inspired by psychometrics, RADAR learns an item response 模型 from 模型 responses with different budgets to different queries, with 可解释 parameters including query difficulties and 模型-budget abilities. RADAR then routes queries with higher...

**Original Abstract**:
> arXiv:2509.25426v3 Announce Type: replace 
Abstract: Reasoning language models have demonstrated remarkable performance on many challenging tasks in math, science, and coding. Choosing the right reasoning model for practical deployment involves a performance and cost tradeoff at two key levels: model size and reasoning budget, where larger models and higher reasoning budget lead to better performance but with increased cost and latency. In this work, we tackle this tradeoff from the angle of model configuration routing for different queries, and present RADAR (Reasoning-Ability and Difficulty-Aware Routing), a lightweight, interpretable, and scalable routing framework. Inspired by psychometrics, RADAR learns an item response model from model responses with different budgets to different qu...

---

## 391. BiasBusters: Uncovering and Mitigating Tool 选择 偏见 in Large Language Models

**原标题**: BiasBusters: Uncovering and Mitigating Tool Selection Bias in Large Language Models

**作者**: Thierry Blankenstein, Jialin Yu, Zixuan Li, Vassilis Plachouras, Sunando Sengupta, Philip Torr, Yarin Gal, Alasdair Paren, Adel Bibi
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2510.00307v2

**中文摘要**:
> arXiv:2510.00307v2 Announce Type: replace 
摘要: Agents backed by large language models (LLMs) increasingly rely on external tools drawn from marketplaces where multiple providers offer functionally equivalent options. This raises a critical 公平性 concern: systematic 偏见 in tool 选择 can degrade user experience and distort competition by privileging certain providers over others. We introduce a 基准 of diverse tool categories, each containing multiple functionally equivalent tools, to systematically evaluate tool-选择 偏见. Using this 基准, we evaluate seven LLMs and show that substantial 偏见 persists, with models either fixating on a single provider or disproportionately favoring tools that appear earlier in the context. To uncover the sources of this behavior, we conduct controlled experiments that isol...

**Original Abstract**:
> arXiv:2510.00307v2 Announce Type: replace 
Abstract: Agents backed by large language models (LLMs) increasingly rely on external tools drawn from marketplaces where multiple providers offer functionally equivalent options. This raises a critical fairness concern: systematic bias in tool selection can degrade user experience and distort competition by privileging certain providers over others. We introduce a benchmark of diverse tool categories, each containing multiple functionally equivalent tools, to systematically evaluate tool-selection bias. Using this benchmark, we evaluate seven LLMs and show that substantial bias persists, with models either fixating on a single provider or disproportionately favoring tools that appear earlier in the context. To uncover the sources of this behavior...

---

## 392. CostNav: A Navigation 基准 for Real-World Economic-Cost 评估 of Physical AI Agents

**原标题**: CostNav: A Navigation Benchmark for Real-World Economic-Cost Evaluation of Physical AI Agents

**作者**: Haebin Seong, Sungmin Kim, Yongjun Cho, Myunchul Joe, Geunwoo Kim, Yubeen Park, Sunhoo Kim, Yoonshik Kim, Suhwan Choi, Jaeyoon Jung, Jiyong Youn, Jinmyung Kwak, Sunghee Ahn, Jaemin Lee, Younggil Do, Seungyeop Yi, Woojin Cheong, Minhyeok Oh, Minchan Kim, Seongjae Kang, Samwoo Seong, Youngjae Yu, Yunsung Lee
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2511.20216v5

**中文摘要**:
> arXiv:2511.20216v5 Announce Type: replace 
摘要: While current navigation benchmarks prioritize task success in simplified settings, they neglect the multidimensional economic constraints essential for the real-world commercialization of 自主 delivery systems. We introduce CostNav, an Economic Navigation 基准 that evaluates physical AI agents through comprehensive economic cost-revenue analysis aligned with real-world business operations. By integrating industry-standard data--such as Securities and Exchange Commission (SEC) filings and Abbreviated Injury Scale (AIS) injury reports--with Isaac Sim's detailed collision and cargo dynamics, CostNav transcends simple task completion to accurately evaluate business 价值 in complex, real-world scenarios. To our knowledge, CostNav is the first physics-gr...

**Original Abstract**:
> arXiv:2511.20216v5 Announce Type: replace 
Abstract: While current navigation benchmarks prioritize task success in simplified settings, they neglect the multidimensional economic constraints essential for the real-world commercialization of autonomous delivery systems. We introduce CostNav, an Economic Navigation Benchmark that evaluates physical AI agents through comprehensive economic cost-revenue analysis aligned with real-world business operations. By integrating industry-standard data--such as Securities and Exchange Commission (SEC) filings and Abbreviated Injury Scale (AIS) injury reports--with Isaac Sim's detailed collision and cargo dynamics, CostNav transcends simple task completion to accurately evaluate business value in complex, real-world scenarios. To our knowledge, CostNav...

---

## 393. IndiMathBench: Autoformalizing Mathematical 推理 Problems with a Human Touch

**原标题**: IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch

**作者**: Param Biyani, Shashank Kirtania, Yasharth Bajpai, Sumit Gulwani, Ashish Tiwari
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2512.00997v2

**中文摘要**:
> arXiv:2512.00997v2 Announce Type: replace 
摘要: Reliable autoformalization remains challenging even in the era of large language models (LLMs). The scarcity of high-quality 训练 data is a major bottleneck. Expert annotation requires substantial time and 深度 expertise in both mathematics and theorem proving. We introduce IndiMathBench, a human-verified 基准 designed to evaluate mathematical theorem proving, curated using an AI-powered human-assisted pipeline for formalizing natural language problems in Lean. IndiMathBench is composed of 312 formal Lean 4 theorems paired with their corresponding informal problem statements, sourced from Indian Mathematics Olympiads. Through 分类-based 检索, iterative compiler feedback, and multi-模型 ensembles, our pipeline generates candidate formalizations that expert...

**Original Abstract**:
> arXiv:2512.00997v2 Announce Type: replace 
Abstract: Reliable autoformalization remains challenging even in the era of large language models (LLMs). The scarcity of high-quality training data is a major bottleneck. Expert annotation requires substantial time and deep expertise in both mathematics and theorem proving. We introduce IndiMathBench, a human-verified benchmark designed to evaluate mathematical theorem proving, curated using an AI-powered human-assisted pipeline for formalizing natural language problems in Lean. IndiMathBench is composed of 312 formal Lean 4 theorems paired with their corresponding informal problem statements, sourced from Indian Mathematics Olympiads. Through category-based retrieval, iterative compiler feedback, and multi-model ensembles, our pipeline generates...

---

## 394. Toward Closed-loop Molecular Discovery via Language 模型, Property Alignment and Strategic 搜索

**原标题**: Toward Closed-loop Molecular Discovery via Language Model, Property Alignment and Strategic Search

**作者**: Junkai Ji, Zhangfan Yang, Dong Xu, Ruibin Bai, Jianqiang Li, Tingjun Hou, Zexuan Zhu
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2512.09566v3

**中文摘要**:
> arXiv:2512.09566v3 Announce Type: replace 
摘要: Drug discovery is a time-consuming and expensive process, with traditional 高吞吐 and docking-based virtual screening hampered by low success rates and limited scalability. Recent advances in 生成式 modelling, including autoregressive, diffusion, and flow-based approaches, have enabled de novo ligand design beyond the limits of enumerative screening. Yet these models often suffer from inadequate 泛化, limited interpretability, and an overemphasis on binding affinity at the expense of key pharmacological properties, thereby restricting their translational utility. Here we present Trio, a molecular 生成 框架 integrating fragment-based molecular language modeling, 强化 学习, and Monte Carlo tree 搜索, for effective and 可解释 closed-loop targeted molecular design. Th...

**Original Abstract**:
> arXiv:2512.09566v3 Announce Type: replace 
Abstract: Drug discovery is a time-consuming and expensive process, with traditional high-throughput and docking-based virtual screening hampered by low success rates and limited scalability. Recent advances in generative modelling, including autoregressive, diffusion, and flow-based approaches, have enabled de novo ligand design beyond the limits of enumerative screening. Yet these models often suffer from inadequate generalization, limited interpretability, and an overemphasis on binding affinity at the expense of key pharmacological properties, thereby restricting their translational utility. Here we present Trio, a molecular generation framework integrating fragment-based molecular language modeling, reinforcement learning, and Monte Carlo tre...

---

## 395. 学习 Transferable Skills in 动作 RPGs via Directed Skill Graphs and Selective Adaptation

**原标题**: Learning Transferable Skills in Action RPGs via Directed Skill Graphs and Selective Adaptation

**作者**: Ali Najar
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2601.17923v2

**中文摘要**:
> arXiv:2601.17923v2 Announce Type: replace 
摘要: Lifelong agents should expand their competence over time without retraining from scratch or overwriting previously learned behaviors. We investigate this in a challenging 实时 控制 setting (Dark Souls III) by representing combat as a directed skill graph and 训练 its components in a hierarchical curriculum. The resulting 智能体 decomposes 控制 into five reusable skills: camera 控制, 目标 lock-on, movement, dodging, and a heal-attack 决策 策略, each optimized for a narrow responsibility. This factorization improves sample efficiency by reducing the burden on any single 策略 and supports selective post-训练: when the 环境 shifts from Phase 1 to Phase 2, only a subset of skills must be adapted, while upstream skills remain transferable. Empirically, we find that targeted...

**Original Abstract**:
> arXiv:2601.17923v2 Announce Type: replace 
Abstract: Lifelong agents should expand their competence over time without retraining from scratch or overwriting previously learned behaviors. We investigate this in a challenging real-time control setting (Dark Souls III) by representing combat as a directed skill graph and training its components in a hierarchical curriculum. The resulting agent decomposes control into five reusable skills: camera control, target lock-on, movement, dodging, and a heal-attack decision policy, each optimized for a narrow responsibility. This factorization improves sample efficiency by reducing the burden on any single policy and supports selective post-training: when the environment shifts from Phase 1 to Phase 2, only a subset of skills must be adapted, while up...

---

## 396. MemOCR: Layout-Aware 视觉 内存 for 高效 Long-视野 推理

**原标题**: MemOCR: Layout-Aware Visual Memory for Efficient Long-Horizon Reasoning

**作者**: Yaorui Shi, Shugui Liu, Yu Yang, Wenyu Mao, Yuxin Chen, Qi GU, Hui Su, Xunliang Cai, Xiang Wang, An Zhang
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2601.21468v4

**中文摘要**:
> arXiv:2601.21468v4 Announce Type: replace 
摘要: Long-视野 agentic 推理 necessitates effectively compressing growing interaction histories into a limited context window. Most existing 内存 systems 序列化 history as text, where token-level cost is uniform and scales linearly with length, often spending scarce budget on low-价值 details. To this end, we introduce MemOCR, a multimodal 内存 智能体 that improves long-视野 推理 under tight context budgets by allocating 内存 space with adaptive information density through 视觉 layout. Concretely, MemOCR maintains a structured rich-text 内存 (e.g., headings, highlights) and renders it into an 图像 that the 智能体 consults for 内存 access, visually prioritizing crucial evidence while aggressively compressing auxiliary details. To ensure 鲁棒性 across varying 内存 budgets, we train MemOCR...

**Original Abstract**:
> arXiv:2601.21468v4 Announce Type: replace 
Abstract: Long-horizon agentic reasoning necessitates effectively compressing growing interaction histories into a limited context window. Most existing memory systems serialize history as text, where token-level cost is uniform and scales linearly with length, often spending scarce budget on low-value details. To this end, we introduce MemOCR, a multimodal memory agent that improves long-horizon reasoning under tight context budgets by allocating memory space with adaptive information density through visual layout. Concretely, MemOCR maintains a structured rich-text memory (e.g., headings, highlights) and renders it into an image that the agent consults for memory access, visually prioritizing crucial evidence while aggressively compressing auxil...

---

## 397. To Mix or To Merge: Toward Multi-Domain 强化 学习 for Large Language Models

**原标题**: To Mix or To Merge: Toward Multi-Domain Reinforcement Learning for Large Language Models

**作者**: Haoqing Wang, Xiang Long, Ziheng Li, Yilong Xu, Tingguang Li, Yehui Tang
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2602.12566v3

**中文摘要**:
> arXiv:2602.12566v3 Announce Type: replace 
摘要: 强化 学习 with Verifiable Rewards (RLVR) plays a key 角色 in stimulating the explicit 推理 capability of Large Language Models (LLMs). We can achieve expert-level 性能 in some specific domains via RLVR, such as coding or math. When a general multi-domain expert-level 模型 is required, we need to carefully consider the collaboration of RLVR across different domains. The current 状态-of-the-art models mainly employ two different 训练 paradigms for multi-domain RLVR: mixed 多任务 RLVR and separate RLVR followed by 模型 merging. However, most of the works did not provide a detailed comparison and analysis about these paradigms. To this end, we choose multiple commonly used high-level tasks (e.g., math, coding, science, instruction following, and 智能体) as our 目标 domains...

**Original Abstract**:
> arXiv:2602.12566v3 Announce Type: replace 
Abstract: Reinforcement Learning with Verifiable Rewards (RLVR) plays a key role in stimulating the explicit reasoning capability of Large Language Models (LLMs). We can achieve expert-level performance in some specific domains via RLVR, such as coding or math. When a general multi-domain expert-level model is required, we need to carefully consider the collaboration of RLVR across different domains. The current state-of-the-art models mainly employ two different training paradigms for multi-domain RLVR: mixed multi-task RLVR and separate RLVR followed by model merging. However, most of the works did not provide a detailed comparison and analysis about these paradigms. To this end, we choose multiple commonly used high-level tasks (e.g., math, cod...

---

## 398. A Minimal 智能体 for Automated Theorem Proving

**原标题**: A Minimal Agent for Automated Theorem Proving

**作者**: Borja Requena, Austin Letson, Krystian Nowakowski, Izan Beltran Ferreiro, Leopoldo Sarra
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2602.24273v2

**中文摘要**:
> arXiv:2602.24273v2 Announce Type: replace 
摘要: We propose a minimal agentic baseline that enables systematic comparison across different AI-based theorem prover architectures. This design implements the core features shared among 状态-of-the-art systems: iterative proof refinement, library 搜索 and context management. We evaluate this agentic 方案 using qualitatively different benchmarks and compare various frontier language models and design choices. Our results show competitive 性能 compared to 状态-of-the-art approaches, while using a significantly simpler 架构. Additionally, we demonstrate consistent advantages of an iterative 方案 over multiple single-shot generations, especially in terms of sample efficiency and cost effectiveness. The 实现 is released open-source as a candidate reference for future...

**Original Abstract**:
> arXiv:2602.24273v2 Announce Type: replace 
Abstract: We propose a minimal agentic baseline that enables systematic comparison across different AI-based theorem prover architectures. This design implements the core features shared among state-of-the-art systems: iterative proof refinement, library search and context management. We evaluate this agentic approach using qualitatively different benchmarks and compare various frontier language models and design choices. Our results show competitive performance compared to state-of-the-art approaches, while using a significantly simpler architecture. Additionally, we demonstrate consistent advantages of an iterative approach over multiple single-shot generations, especially in terms of sample efficiency and cost effectiveness. The implementation ...

---

## 399. CARE: Towards Clinical Accountability in 多模态 Medical 推理 with an Evidence-Grounded Agentic 框架

**原标题**: CARE: Towards Clinical Accountability in Multi-Modal Medical Reasoning with an Evidence-Grounded Agentic Framework

**作者**: Yuexi Du, Jinglu Wang, Shujie Liu, Nicha C. Dvornek, Yan Lu
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.01607v2

**中文摘要**:
> arXiv:2603.01607v2 Announce Type: replace 
摘要: Large 视觉 language models (VLMs) have shown strong 多模态 medical 推理 ability, but most operate as end-to-end black boxes, diverging from clinicians' evidence-based, staged workflows and hindering clinical accountability. Complementarily, expert 视觉 grounding models can accurately localize regions of interest (ROIs), providing explicit, reliable evidence that improves both 推理 accuracy and trust. In this 论文, we introduce CARE, advancing Clinical Accountability in 多模态 medical 推理 with an Evidence-grounded agentic 框架. Unlike existing approaches that couple grounding and 推理 within a single generalist 模型, CARE decomposes the task into coordinated sub-modules to reduce shortcut 学习 and hallucination: a compact VLM proposes relevant medical entities; an expe...

**Original Abstract**:
> arXiv:2603.01607v2 Announce Type: replace 
Abstract: Large visual language models (VLMs) have shown strong multi-modal medical reasoning ability, but most operate as end-to-end black boxes, diverging from clinicians' evidence-based, staged workflows and hindering clinical accountability. Complementarily, expert visual grounding models can accurately localize regions of interest (ROIs), providing explicit, reliable evidence that improves both reasoning accuracy and trust. In this paper, we introduce CARE, advancing Clinical Accountability in multi-modal medical Reasoning with an Evidence-grounded agentic framework. Unlike existing approaches that couple grounding and reasoning within a single generalist model, CARE decomposes the task into coordinated sub-modules to reduce shortcut learning...

---

## 400. ToolRLA: Multiplicative 奖励 Decomposition for Tool-Integrated Agents

**原标题**: ToolRLA: Multiplicative Reward Decomposition for Tool-Integrated Agents

**作者**: Pengbo Liu
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.01620v4

**中文摘要**:
> arXiv:2603.01620v4 Announce Type: replace 
摘要: Tool-integrated agents that interleave 推理 with API calls are promising for complex tasks, yet aligning them for high-stakes, domain-specific 部署 remains challenging: existing 强化 学习 approaches rely on coarse binary rewards that cannot distinguish tool 选择 errors from malformed parameters. We present ToolRLA, a three-stage post-训练 pipeline (SFT -> GRPO -> DPO) for domain-specific tool agents. The core contribution is a fine-grained 奖励 function with multiplicative correctness decomposition spanning four dimensions -- format validity, tool 选择, parameter accuracy, and regulatory compliance -- that encodes domain priority orderings as inductive biases in the 奖励 landscape. Deployed on a financial advisory copilot (80+ advisors, 1,200+ daily queries), T...

**Original Abstract**:
> arXiv:2603.01620v4 Announce Type: replace 
Abstract: Tool-integrated agents that interleave reasoning with API calls are promising for complex tasks, yet aligning them for high-stakes, domain-specific deployment remains challenging: existing reinforcement learning approaches rely on coarse binary rewards that cannot distinguish tool selection errors from malformed parameters. We present ToolRLA, a three-stage post-training pipeline (SFT -> GRPO -> DPO) for domain-specific tool agents. The core contribution is a fine-grained reward function with multiplicative correctness decomposition spanning four dimensions -- format validity, tool selection, parameter accuracy, and regulatory compliance -- that encodes domain priority orderings as inductive biases in the reward landscape. Deployed on a ...

---

## 401. SEED-SET: 可扩展 Evolving Experimental Design for 系统-level Ethical Testing

**原标题**: SEED-SET: Scalable Evolving Experimental Design for System-level Ethical Testing

**作者**: Anjali Parashar, Yingke Li, Eric Yang Yu, Fei Chen, James Neidhoefer, Devesh Upadhyay, Chuchu Fan
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.01630v2

**中文摘要**:
> arXiv:2603.01630v2 Announce Type: replace 
摘要: As 自主 systems such as drones, become increasingly deployed in high-stakes, human-centric domains, it is critical to evaluate the ethical alignment since failure to do so imposes imminent danger to human lives, and long term 偏见 in 决策-making. Automated ethical benchmarking of these systems is understudied due to the lack of ubiquitous, well-defined metrics for 评估, and stakeholder-specific subjectivity, which cannot be modeled analytically. To address these challenges, we propose SEED-SET, a 贝叶斯 experimental design 框架 that incorporates domain-specific objective evaluations, and subjective 价值 judgments from stakeholders. SEED-SET models both 评估 types separately with hierarchical Gaussian Processes, and uses a novel acquisition strategy to propose ...

**Original Abstract**:
> arXiv:2603.01630v2 Announce Type: replace 
Abstract: As autonomous systems such as drones, become increasingly deployed in high-stakes, human-centric domains, it is critical to evaluate the ethical alignment since failure to do so imposes imminent danger to human lives, and long term bias in decision-making. Automated ethical benchmarking of these systems is understudied due to the lack of ubiquitous, well-defined metrics for evaluation, and stakeholder-specific subjectivity, which cannot be modeled analytically. To address these challenges, we propose SEED-SET, a Bayesian experimental design framework that incorporates domain-specific objective evaluations, and subjective value judgments from stakeholders. SEED-SET models both evaluation types separately with hierarchical Gaussian Process...

---

## 402. No Memorization, No 检测: Output Distribution-Based Contamination 检测 in Small Language Models

**原标题**: No Memorization, No Detection: Output Distribution-Based Contamination Detection in Small Language Models

**作者**: Omer Sela (Tel Aviv University)
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.03203v3

**中文摘要**:
> arXiv:2603.03203v3 Announce Type: replace 
摘要: CDD, or Contamination 检测 via output Distribution, identifies data contamination by measuring the peakedness of a 模型's sampled outputs. We study the conditions under which this 方案 succeeds and fails on small language models ranging from 70M to 410M parameters. Using controlled contamination experiments on GSM8K, HumanEval, and MATH, we find that CDD's effectiveness depends critically on whether fine-tuning produces verbatim memorization. In the majority of conditions we test, CDD performs at chance level even when the data is verifiably contaminated and detectable by simpler methods. We show that probability-based methods, specifically perplexity and Min-k\% Prob, outperform CDD in all conditions where any 方法 exceeds chance, suggesting that CDD...

**Original Abstract**:
> arXiv:2603.03203v3 Announce Type: replace 
Abstract: CDD, or Contamination Detection via output Distribution, identifies data contamination by measuring the peakedness of a model's sampled outputs. We study the conditions under which this approach succeeds and fails on small language models ranging from 70M to 410M parameters. Using controlled contamination experiments on GSM8K, HumanEval, and MATH, we find that CDD's effectiveness depends critically on whether fine-tuning produces verbatim memorization. In the majority of conditions we test, CDD performs at chance level even when the data is verifiably contaminated and detectable by simpler methods. We show that probability-based methods, specifically perplexity and Min-k\% Prob, outperform CDD in all conditions where any method exceeds c...

---

## 403. UIS-Digger: Towards Comprehensive Research 智能体 Systems for Real-world Unindexed Information Seeking

**原标题**: UIS-Digger: Towards Comprehensive Research Agent Systems for Real-world Unindexed Information Seeking

**作者**: Chang Liu, Chuqiao Kuang, Tianyi Zhuang, Yuxin Cheng, Huichi Zhou, Xiaoguang Li, Lifeng Shang
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.08117v2

**中文摘要**:
> arXiv:2603.08117v2 Announce Type: replace 
摘要: Recent advancements in 大语言模型-based information-seeking agents have achieved record-breaking 性能 on established benchmarks. However, these agents remain heavily reliant on 搜索-engine-indexed knowledge, leaving a critical blind spot: Unindexed Information Seeking (UIS). This 论文 identifies and explores the UIS problem, where vital information is not captured by 搜索 engine crawlers, such as overlooked content, 动态 webpages, and embedded files. Despite its significance, UIS remains an underexplored challenge. To address this gap, we introduce UIS-问答, the first dedicated UIS 基准, comprising 110 expert-annotated 问答 pairs. Notably, even 状态-of-the-art agents experience a drastic 性能 drop on UIS-问答 (e.g., from 70.90 on GAIA and 46.70 on BrowseComp-zh to 24.55...

**Original Abstract**:
> arXiv:2603.08117v2 Announce Type: replace 
Abstract: Recent advancements in LLM-based information-seeking agents have achieved record-breaking performance on established benchmarks. However, these agents remain heavily reliant on search-engine-indexed knowledge, leaving a critical blind spot: Unindexed Information Seeking (UIS). This paper identifies and explores the UIS problem, where vital information is not captured by search engine crawlers, such as overlooked content, dynamic webpages, and embedded files. Despite its significance, UIS remains an underexplored challenge. To address this gap, we introduce UIS-QA, the first dedicated UIS benchmark, comprising 110 expert-annotated QA pairs. Notably, even state-of-the-art agents experience a drastic performance drop on UIS-QA (e.g., from 7...

---

## 404. RetroAgent: From Solving to Evolving via Retrospective Dual Intrinsic Feedback

**原标题**: RetroAgent: From Solving to Evolving via Retrospective Dual Intrinsic Feedback

**作者**: Xiaoying Zhang, Zichen Liu, Yipeng Zhang, Xia Hu, Wenqi Shao
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.08561v2

**中文摘要**:
> arXiv:2603.08561v2 Announce Type: replace 
摘要: Large language 模型 (大语言模型)-based agents trained with 强化 学习 (RL) have shown strong potential on complex interactive tasks. However, standard RL paradigms favor 静态 problem-solving over continuous adaptation: agents often converge to suboptimal strategies due to insufficient 探索, while learned knowledge remains implicit within parameters rather than explicitly retrievable, limiting effective experiential 学习. To address these limitations, we introduce RetroAgent, an 在线 RL 框架 that empowers agents to master complex interactive environments not just by solving, but by evolving. Concretely, RetroAgent features a hindsight self-reflection mechanism that produces dual intrinsic feedback: (1) intrinsic numerical feedback that that tracks incremental subtas...

**Original Abstract**:
> arXiv:2603.08561v2 Announce Type: replace 
Abstract: Large language model (LLM)-based agents trained with reinforcement learning (RL) have shown strong potential on complex interactive tasks. However, standard RL paradigms favor static problem-solving over continuous adaptation: agents often converge to suboptimal strategies due to insufficient exploration, while learned knowledge remains implicit within parameters rather than explicitly retrievable, limiting effective experiential learning. To address these limitations, we introduce RetroAgent, an online RL framework that empowers agents to master complex interactive environments not just by solving, but by evolving. Concretely, RetroAgent features a hindsight self-reflection mechanism that produces dual intrinsic feedback: (1) intrinsic ...

---

## 405. LCA: Local Classifier Alignment for Continual 学习

**原标题**: LCA: Local Classifier Alignment for Continual Learning

**作者**: Tung Tran, Danilo Vasconcellos Vargas, Khoat Than
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.09888v2

**中文摘要**:
> arXiv:2603.09888v2 Announce Type: replace 
摘要: A fundamental requirement for intelligent systems is the ability to learn continuously under changing environments. However, models trained in this regime often suffer from catastrophic forgetting. Leveraging pre-trained models has recently emerged as a promising solution, since their generalized 特征 extractors enable faster and more 鲁棒 adaptation. While some earlier works mitigate forgetting by fine-tuning only on the first task, this 方案 quickly deteriorates as the number of tasks grows and the data distributions diverge. More recent research instead seeks to consolidate task knowledge into a unified backbone, or adapting the backbone as new tasks arrive. However, such approaches may create a (potential) \textit{mismatch} between task-specific...

**Original Abstract**:
> arXiv:2603.09888v2 Announce Type: replace 
Abstract: A fundamental requirement for intelligent systems is the ability to learn continuously under changing environments. However, models trained in this regime often suffer from catastrophic forgetting. Leveraging pre-trained models has recently emerged as a promising solution, since their generalized feature extractors enable faster and more robust adaptation. While some earlier works mitigate forgetting by fine-tuning only on the first task, this approach quickly deteriorates as the number of tasks grows and the data distributions diverge. More recent research instead seeks to consolidate task knowledge into a unified backbone, or adapting the backbone as new tasks arrive. However, such approaches may create a (potential) \textit{mismatch} ...

---

## 406. Improving 公平性 with Ensemble Combination: Margin-Dependent Bounds

**原标题**: Improving Fairness with Ensemble Combination: Margin-Dependent Bounds

**作者**: Yijun Bian
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2301.10813v5

**中文摘要**:
> arXiv:2301.10813v5 Announce Type: replace-cross 
摘要: The concern about hidden discrimination in machine 学习 models is growing, as their widespread real-world applications increasingly impact human lives. Various techniques, including commonly used group 公平性 measures and several 公平性-aware ensemble-based methods, have been developed to enhance 公平性. However, existing 公平性 measures typically focus on only one aspect -- either group or individual 公平性, and the compatibility difficulty among these measures indicates a possibility of remaining biases even when one of them is satisfied. Moreover, existing mechanisms to boost 公平性 usually present empirical results to show validity, yet few of them discuss whether 公平性 can be boosted with certain theoretical guarantees. To address these issues, we propos...

**Original Abstract**:
> arXiv:2301.10813v5 Announce Type: replace-cross 
Abstract: The concern about hidden discrimination in machine learning models is growing, as their widespread real-world applications increasingly impact human lives. Various techniques, including commonly used group fairness measures and several fairness-aware ensemble-based methods, have been developed to enhance fairness. However, existing fairness measures typically focus on only one aspect -- either group or individual fairness, and the compatibility difficulty among these measures indicates a possibility of remaining biases even when one of them is satisfied. Moreover, existing mechanisms to boost fairness usually present empirical results to show validity, yet few of them discuss whether fairness can be boosted with certain theoretical...

---

## 407. An 更新日期 Assessment of 强化 学习 for Macro Placement

**原标题**: An Updated Assessment of Reinforcement Learning for Macro Placement

**作者**: Chung-Kuan Cheng, Andrew B. Kahng, Sayak Kundu, Yucheng Wang, Zhiang Wang
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2302.11014v3

**中文摘要**:
> arXiv:2302.11014v3 Announce Type: replace-cross 
摘要: We provide an improved assessment of Google Brain's 深度 强化 学习 方案 to macro placement and its 更新日期 Circuit 训练 (CT) 实现 in GitHub. A stronger simulated annealing (SA) baseline leverages the "go-with-the-winners" metaheuristic and a multi-threading 实现. We develop and release new public benchmarks in sub-10nm technology: LEF/DEF for Google's 7nm TSMC Ariane protobuf and scaled variants, as well as testcases implemented in the open-source ASAP7 7nm research enablement. We evaluate from-scratch 训练 and fine-tuning results for the latest "AlphaChip" release of Circuit 训练, alongside multiple alternative macro placers. We also study the recently-发布日期 pre-训练 guidance in. A commercial place-and-route tool is used to provide "true 奖励" post-route power, ...

**Original Abstract**:
> arXiv:2302.11014v3 Announce Type: replace-cross 
Abstract: We provide an improved assessment of Google Brain's deep reinforcement learning approach to macro placement and its updated Circuit Training (CT) implementation in GitHub. A stronger simulated annealing (SA) baseline leverages the "go-with-the-winners" metaheuristic and a multi-threading implementation. We develop and release new public benchmarks in sub-10nm technology: LEF/DEF for Google's 7nm TSMC Ariane protobuf and scaled variants, as well as testcases implemented in the open-source ASAP7 7nm research enablement. We evaluate from-scratch training and fine-tuning results for the latest "AlphaChip" release of Circuit Training, alongside multiple alternative macro placers. We also study the recently-published pre-training guidanc...

---

## 408. Optimal Transport Aggregation for 分布式 Mixture-of-Experts

**原标题**: Optimal Transport Aggregation for Distributed Mixture-of-Experts

**作者**: Fa\"icel Chamroukhi, Nhat Thien Pham
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2312.09877v2

**中文摘要**:
> arXiv:2312.09877v2 Announce Type: replace-cross 
摘要: Mixture-of-experts (MoE) models provide a flexible statistical 框架 for modeling heterogeneity and nonlinear relationships. In many modern applications, however, datasets are naturally 分布式 across multiple machines due to 存储, computational, or governance constraints. We consider a 分布式 模型 aggregation setting in which local MoE models are trained independently on decentralized datasets and subsequently combined into a global estimator. Aggregating MoE models is challenging because standard averaging produces models that do not preserve the MoE structure, and therefore do not yield estimates of the global 模型 parameters. To address this issue, we propose a principled aggregation 框架 based on optimal transport that constructs a reduced global MoE...

**Original Abstract**:
> arXiv:2312.09877v2 Announce Type: replace-cross 
Abstract: Mixture-of-experts (MoE) models provide a flexible statistical framework for modeling heterogeneity and nonlinear relationships. In many modern applications, however, datasets are naturally distributed across multiple machines due to storage, computational, or governance constraints. We consider a distributed model aggregation setting in which local MoE models are trained independently on decentralized datasets and subsequently combined into a global estimator. Aggregating MoE models is challenging because standard averaging produces models that do not preserve the MoE structure, and therefore do not yield estimates of the global model parameters. To address this issue, we propose a principled aggregation framework based on optimal...

---

## 409. Modelling Language using Large Language Models

**原标题**: Modelling Language using Large Language Models

**作者**: Jumbly Grindrod
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2404.09579v2

**中文摘要**:
> arXiv:2404.09579v2 Announce Type: replace-cross 
摘要: This 论文 argues that large language models have a valuable scientific 角色 to play in 服务 as scientific models of public languages. Linguistic study should not only be concerned with the cognitive processes behind linguistic competence, but also with language understood as an external, social entity. Once this is recognized, the 价值 of large language models as scientific models becomes clear. This 论文 defends the position against a number of arguments to the effect that language models provide no linguistic insight. Building upon Weisberg's (2007) notion of a 模型 construal, it is then argued that recent work in computational linguistics to better understand the inner workings of large language models can be used to develop a 模型 construal for la...

**Original Abstract**:
> arXiv:2404.09579v2 Announce Type: replace-cross 
Abstract: This paper argues that large language models have a valuable scientific role to play in serving as scientific models of public languages. Linguistic study should not only be concerned with the cognitive processes behind linguistic competence, but also with language understood as an external, social entity. Once this is recognized, the value of large language models as scientific models becomes clear. This paper defends the position against a number of arguments to the effect that language models provide no linguistic insight. Building upon Weisberg's (2007) notion of a model construal, it is then argued that recent work in computational linguistics to better understand the inner workings of large language models can be used to deve...

---

## 410. EoRA: Fine-tuning-free Compensation for Compressed 大语言模型 with Eigenspace Low-Rank Approximation

**原标题**: EoRA: Fine-tuning-free Compensation for Compressed LLM with Eigenspace Low-Rank Approximation

**作者**: Shih-Yang Liu, Maksim Khadkevich, Nai Chit Fung, Charbel Sakr, Chao-Han Huck Yang, Chien-Yi Wang, Saurav Muralidharan, Hongxu Yin, Kwang-Ting Cheng, Jan Kautz, Yu-Chiang Frank Wang, Pavlo Molchanov, Min-Hung Chen
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2410.21271v5

**中文摘要**:
> arXiv:2410.21271v5 Announce Type: replace-cross 
摘要: While post-训练 compression techniques effectively reduce the 内存 footprint, 延迟, and power consumption of Large Language Models (LLMs), they often 结果 in noticeable accuracy degradation and remain limited by hardware and kernel constraints that restrict supported compression formats ultimately reducing flexibility across a wide range of 部署 scenarios. In this work, we propose EoRA, a novel fine-tuning-free 方法 that augments compressed LLMs with low-rank matrices, allowing users to rapidly enhance task-specific 性能 and freely 平衡 the trade-off between accuracy and computational overhead beyond the constraints of compression formats. EoRA consistently outperforms prior 训练-free low rank methods in recovering the accuracy of compressed LLMs, achievi...

**Original Abstract**:
> arXiv:2410.21271v5 Announce Type: replace-cross 
Abstract: While post-training compression techniques effectively reduce the memory footprint, latency, and power consumption of Large Language Models (LLMs), they often result in noticeable accuracy degradation and remain limited by hardware and kernel constraints that restrict supported compression formats ultimately reducing flexibility across a wide range of deployment scenarios. In this work, we propose EoRA, a novel fine-tuning-free method that augments compressed LLMs with low-rank matrices, allowing users to rapidly enhance task-specific performance and freely balance the trade-off between accuracy and computational overhead beyond the constraints of compression formats. EoRA consistently outperforms prior training-free low rank metho...

---

## 411. Token Cleaning: Fine-Grained Data 选择 for 大语言模型 有监督 Fine-Tuning

**原标题**: Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning

**作者**: Jinlong Pang, Na Di, Zhaowei Zhu, Jiaheng Wei, Hao Cheng, Chen Qian, Yang Liu
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2502.01968v3

**中文摘要**:
> arXiv:2502.01968v3 Announce Type: replace-cross 
摘要: Recent studies show that in 有监督 fine-tuning (SFT) of large language models (LLMs), data quality matters more than quantity. While most data cleaning methods concentrate on filtering entire samples, the quality of individual tokens within a sample can vary significantly. After pre-训练, even in high-quality samples, patterns or phrases that are not task-related can be redundant, uninformative, or even harmful. Continuing to fine-tune on these patterns may offer limited benefit and even degrade downstream task 性能. In this 论文, we investigate token quality from a noisy-label perspective and propose a generic token cleaning pipeline for SFT tasks. Our 方法 filters out uninformative tokens while preserving those carrying key task-specific informat...

**Original Abstract**:
> arXiv:2502.01968v3 Announce Type: replace-cross 
Abstract: Recent studies show that in supervised fine-tuning (SFT) of large language models (LLMs), data quality matters more than quantity. While most data cleaning methods concentrate on filtering entire samples, the quality of individual tokens within a sample can vary significantly. After pre-training, even in high-quality samples, patterns or phrases that are not task-related can be redundant, uninformative, or even harmful. Continuing to fine-tune on these patterns may offer limited benefit and even degrade downstream task performance. In this paper, we investigate token quality from a noisy-label perspective and propose a generic token cleaning pipeline for SFT tasks. Our method filters out uninformative tokens while preserving those ...

---

## 412. Boosting Cross-problem 泛化 in Diffusion-Based 神经 Combinatorial Solver via 推理 Time Adaptation

**原标题**: Boosting Cross-problem Generalization in Diffusion-Based Neural Combinatorial Solver via Inference Time Adaptation

**作者**: Haoyu Lei, Kaiwen Zhou, Yinchuan Li, Zhitang Chen, Farzan Farnia
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2502.12188v4

**中文摘要**:
> arXiv:2502.12188v4 Announce Type: replace-cross 
摘要: Diffusion-based 神经 Combinatorial 优化 (NCO) has demonstrated effectiveness in solving NP-complete (NPC) problems by 学习 discrete diffusion models for solution 生成, eliminating hand-crafted domain knowledge. Despite their success, existing NCO methods face significant challenges in both cross-scale and cross-problem 泛化, and high 训练 costs compared to traditional solvers. While recent studies on diffusion models have introduced 训练-free guidance approaches that leverage pre-defined guidance functions for conditional 生成, such methodologies have not been extensively explored in combinatorial 优化. To bridge this gap, we propose a 训练-free 推理 time adaptation 框架 (DIFU-Ada) that enables both the 零样本 cross-problem transfer and cross-scale 泛化 capabilities...

**Original Abstract**:
> arXiv:2502.12188v4 Announce Type: replace-cross 
Abstract: Diffusion-based Neural Combinatorial Optimization (NCO) has demonstrated effectiveness in solving NP-complete (NPC) problems by learning discrete diffusion models for solution generation, eliminating hand-crafted domain knowledge. Despite their success, existing NCO methods face significant challenges in both cross-scale and cross-problem generalization, and high training costs compared to traditional solvers. While recent studies on diffusion models have introduced training-free guidance approaches that leverage pre-defined guidance functions for conditional generation, such methodologies have not been extensively explored in combinatorial optimization. To bridge this gap, we propose a training-free inference time adaptation frame...

---

## 413. 离线 动态 Inventory and Pricing Strategy: Addressing Censored and Dependent Demand

**原标题**: Offline Dynamic Inventory and Pricing Strategy: Addressing Censored and Dependent Demand

**作者**: Korel Gundem, Zhengling Qi
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2504.09831v2

**中文摘要**:
> arXiv:2504.09831v2 Announce Type: replace-cross 
摘要: In this 论文, we study the 离线 sequential 特征-based pricing and inventory 控制 problem where the current demand depends on the past demand levels and any demand exceeding the available inventory is lost. Our goal is to leverage the 离线 数据集, consisting of past prices, ordering quantities, inventory levels, covariates, and censored sales levels, to estimate the optimal pricing and inventory 控制 策略 that maximizes long-term profit. While the underlying 动态 without censoring can be modeled by Markov 决策 process (MDP), the primary obstacle arises from the observed process where demand censoring is present, resulting in missing profit information, the failure of the Markov property, and a non-stationary optimal 策略. To overcome these challenges, we first ...

**Original Abstract**:
> arXiv:2504.09831v2 Announce Type: replace-cross 
Abstract: In this paper, we study the offline sequential feature-based pricing and inventory control problem where the current demand depends on the past demand levels and any demand exceeding the available inventory is lost. Our goal is to leverage the offline dataset, consisting of past prices, ordering quantities, inventory levels, covariates, and censored sales levels, to estimate the optimal pricing and inventory control policy that maximizes long-term profit. While the underlying dynamic without censoring can be modeled by Markov decision process (MDP), the primary obstacle arises from the observed process where demand censoring is present, resulting in missing profit information, the failure of the Markov property, and a non-stationar...

---

## 414. 可扩展 多任务 学习 through Spiking 神经 Networks with Adaptive Task-Switching 策略 for Intelligent 自主 Agents

**原标题**: Scalable Multi-Task Learning through Spiking Neural Networks with Adaptive Task-Switching Policy for Intelligent Autonomous Agents

**作者**: Rachmad Vidya Wicaksana Putra, Avaneesh Devkota, Muhammad Shafique
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2504.13541v3

**中文摘要**:
> arXiv:2504.13541v3 Announce Type: replace-cross 
摘要: 训练 resource-constrained 自主 agents on multiple tasks simultaneously is crucial for adapting to diverse real-world environments. Recent works employ 强化 学习 (RL) 方案, but they still suffer from sub-optimal 多任务 性能 due to task interference. 状态-of-the-art works employ Spiking 神经 Networks (SNNs) to improve RL-based 多任务 学习 and enable low-power/energy operations through 网络 enhancements and spike-driven data stream processing. However, they rely on fixed task-switching intervals during its 训练, thus limiting its 性能 and scalability. To address this, we propose SwitchMT, a novel methodology that employs adaptive task-switching for effective, 可扩展, and simultaneous 多任务 学习. SwitchMT employs the following key ideas: (1) leveraging a 深度 Spiking Q-网络 with ac...

**Original Abstract**:
> arXiv:2504.13541v3 Announce Type: replace-cross 
Abstract: Training resource-constrained autonomous agents on multiple tasks simultaneously is crucial for adapting to diverse real-world environments. Recent works employ reinforcement learning (RL) approach, but they still suffer from sub-optimal multi-task performance due to task interference. State-of-the-art works employ Spiking Neural Networks (SNNs) to improve RL-based multi-task learning and enable low-power/energy operations through network enhancements and spike-driven data stream processing. However, they rely on fixed task-switching intervals during its training, thus limiting its performance and scalability. To address this, we propose SwitchMT, a novel methodology that employs adaptive task-switching for effective, scalable, and...

---

## 415. REI-Bench: Can Embodied Agents Understand Vague Human Instructions in Task 规划?

**原标题**: REI-Bench: Can Embodied Agents Understand Vague Human Instructions in Task Planning?

**作者**: Chenxi Jiang, Chuhao Zhou, Jianfei Yang
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2505.10872v3

**中文摘要**:
> arXiv:2505.10872v3 Announce Type: replace-cross 
摘要: Robot task 规划 decomposes human instructions into executable 动作 sequences that enable robots to complete a series of complex tasks. Although recent large language 模型 (大语言模型)-based task planners achieve amazing 性能, they assume that human instructions are clear and straightforward. However, real-world users are not experts, and their instructions to robots often contain significant vagueness. Linguists suggest that such vagueness frequently arises from referring expressions (REs), whose meanings depend heavily on dialogue context and 环境. This vagueness is even more prevalent among the elderly and children, who are the groups that robots should serve more. This 论文 studies how such vagueness in REs within human instructions affects 大语言模型-base...

**Original Abstract**:
> arXiv:2505.10872v3 Announce Type: replace-cross 
Abstract: Robot task planning decomposes human instructions into executable action sequences that enable robots to complete a series of complex tasks. Although recent large language model (LLM)-based task planners achieve amazing performance, they assume that human instructions are clear and straightforward. However, real-world users are not experts, and their instructions to robots often contain significant vagueness. Linguists suggest that such vagueness frequently arises from referring expressions (REs), whose meanings depend heavily on dialogue context and environment. This vagueness is even more prevalent among the elderly and children, who are the groups that robots should serve more. This paper studies how such vagueness in REs within...

---

## 416. LLLMs: A Data-Driven Survey of Evolving Research on Limitations of Large Language Models

**原标题**: LLLMs: A Data-Driven Survey of Evolving Research on Limitations of Large Language Models

**作者**: Aida Kostikova, Zhipin Wang, Deidamea Bajri, Ole P\"utz, Benjamin Paa{\ss}en, Steffen Eger
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2505.19240v3

**中文摘要**:
> arXiv:2505.19240v3 Announce Type: replace-cross 
摘要: Large language 模型 (大语言模型) research has grown rapidly, along with increasing concern about their limitations. In this survey, we conduct a data-driven, semi-automated 审稿 of research on limitations of LLMs (LLLMs) from 2022 to early 2025 using a bottom-up 方案. From a 语料库 of 250,000 ACL and arXiv papers, we identify 14,648 relevant papers using keyword filtering, 大语言模型-based 分类, validated against expert labels, and topic clustering (via two approaches, HDBSCAN+BERTopic and LlooM). We find that the share of 大语言模型-related papers increases over fivefold in ACL and nearly eightfold in arXiv between 2022 and 2025. Since 2022, LLLMs research grows even faster, reaching over 30% of 大语言模型 papers by 2025. 推理 remains the most studied limitation, follo...

**Original Abstract**:
> arXiv:2505.19240v3 Announce Type: replace-cross 
Abstract: Large language model (LLM) research has grown rapidly, along with increasing concern about their limitations. In this survey, we conduct a data-driven, semi-automated review of research on limitations of LLMs (LLLMs) from 2022 to early 2025 using a bottom-up approach. From a corpus of 250,000 ACL and arXiv papers, we identify 14,648 relevant papers using keyword filtering, LLM-based classification, validated against expert labels, and topic clustering (via two approaches, HDBSCAN+BERTopic and LlooM). We find that the share of LLM-related papers increases over fivefold in ACL and nearly eightfold in arXiv between 2022 and 2025. Since 2022, LLLMs research grows even faster, reaching over 30% of LLM papers by 2025. Reasoning remains t...

---

## 417. Comparative Analysis of Modern Machine 学习 Models for Retail Sales Forecasting

**原标题**: Comparative Analysis of Modern Machine Learning Models for Retail Sales Forecasting

**作者**: Luka Hobor, Mario Brcic, Lidija Polutnik, Ante Kapetanovic
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2506.05941v2

**中文摘要**:
> arXiv:2506.05941v2 Announce Type: replace-cross 
摘要: 准确 demand forecasting is critical for brick-and-mortar retailers to optimize inventory management and minimize costs. This study evaluates statistical baselines, tree-based ensembles (XGBoost and LightGBM), and 深度 学习 architectures (N-BEATS, N-HiTS, and the Temporal Fusion Transformer) on retail sales data characterized by intermittent demand, substantial missingness, and frequent product turnover. Models are compared across four configurations varying by aggregation level and imputation strategy, using 评估 protocols that reflect typical 部署 patterns for each 模型 class. Localized tree-based methods achieve superior 性能, with XGBoost attaining the lowest RMSE of 4.833. While SAITS-based imputation improved 神经 网络 性能 in aggregated settings, thes...

**Original Abstract**:
> arXiv:2506.05941v2 Announce Type: replace-cross 
Abstract: Accurate demand forecasting is critical for brick-and-mortar retailers to optimize inventory management and minimize costs. This study evaluates statistical baselines, tree-based ensembles (XGBoost and LightGBM), and deep learning architectures (N-BEATS, N-HiTS, and the Temporal Fusion Transformer) on retail sales data characterized by intermittent demand, substantial missingness, and frequent product turnover. Models are compared across four configurations varying by aggregation level and imputation strategy, using evaluation protocols that reflect typical deployment patterns for each model class. Localized tree-based methods achieve superior performance, with XGBoost attaining the lowest RMSE of 4.833. While SAITS-based imputatio...

---

## 418. Self-Improving Loops for 视觉 Robotic 规划

**原标题**: Self-Improving Loops for Visual Robotic Planning

**作者**: Calvin Luo, Zilai Zeng, Mingxi Jia, Yilun Du, Chen Sun
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2506.06658v3

**中文摘要**:
> arXiv:2506.06658v3 Announce Type: replace-cross 
摘要: 视频 生成式 models trained on expert demonstrations have been utilized as performant text-conditioned 视觉 planners for solving robotic tasks. However, 泛化 to unseen tasks remains a challenge. Whereas improved 泛化 may be facilitated by leveraging learned prior knowledge from additional pre-collected 离线 data sources, such as web-scale 视频 datasets, in the era of experience we aim to design agents that can continuously improve in an 在线 manner from self-collected behaviors. In this work we thus propose the Self-Improving Loops for 视觉 Robotic 规划 (SILVR), where an in-domain 视频 模型 iteratively updates itself on self-produced trajectories, and steadily improves its 性能 for a specified task of interest. We apply SILVR to a diverse suite of MetaWorld tasks, ...

**Original Abstract**:
> arXiv:2506.06658v3 Announce Type: replace-cross 
Abstract: Video generative models trained on expert demonstrations have been utilized as performant text-conditioned visual planners for solving robotic tasks. However, generalization to unseen tasks remains a challenge. Whereas improved generalization may be facilitated by leveraging learned prior knowledge from additional pre-collected offline data sources, such as web-scale video datasets, in the era of experience we aim to design agents that can continuously improve in an online manner from self-collected behaviors. In this work we thus propose the Self-Improving Loops for Visual Robotic Planning (SILVR), where an in-domain video model iteratively updates itself on self-produced trajectories, and steadily improves its performance for a s...

---

## 419. Differential 隐私 in Machine 学习: A Survey from Symbolic AI to LLMs

**原标题**: Differential Privacy in Machine Learning: A Survey from Symbolic AI to LLMs

**作者**: Francisco Aguilera-Mart\'inez, Fernando Berzal
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2506.11687v2

**中文摘要**:
> arXiv:2506.11687v2 Announce Type: replace-cross 
摘要: Machine 学习 models should not reveal particular information that is not otherwise accessible. Differential 隐私 provides a formal 框架 to mitigate 隐私 risks by ensuring that the inclusion or exclusion of any single data point does not significantly alter the output of an 算法, thus limiting the exposure of private information. This survey reviews the foundational definitions of differential 隐私 and traces their 进化 through key theoretical and applied contributions. It then provides an in-depth examination of how DP has been integrated into machine 学习 models, analyzing existing proposals and methods to preserve 隐私 when 训练 ML models. Finally, it describes how DP-based ML techniques can be evaluated in practice. By offering a comprehensive overview o...

**Original Abstract**:
> arXiv:2506.11687v2 Announce Type: replace-cross 
Abstract: Machine learning models should not reveal particular information that is not otherwise accessible. Differential privacy provides a formal framework to mitigate privacy risks by ensuring that the inclusion or exclusion of any single data point does not significantly alter the output of an algorithm, thus limiting the exposure of private information. This survey reviews the foundational definitions of differential privacy and traces their evolution through key theoretical and applied contributions. It then provides an in-depth examination of how DP has been integrated into machine learning models, analyzing existing proposals and methods to preserve privacy when training ML models. Finally, it describes how DP-based ML techniques can...

---

## 420. Locality-aware 并行 Decoding for 高效 Autoregressive 图像 生成

**原标题**: Locality-aware Parallel Decoding for Efficient Autoregressive Image Generation

**作者**: Zhuoyang Zhang, Luke J. Huang, Chengyue Wu, Shang Yang, Kelly Peng, Yao Lu, Song Han
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2507.01957v2

**中文摘要**:
> arXiv:2507.01957v2 Announce Type: replace-cross 
摘要: We present Locality-aware 并行 Decoding (LPD) to accelerate autoregressive 图像 生成. Traditional autoregressive 图像 生成 relies on next-patch prediction, a 内存-bound process that leads to high 延迟. Existing works have tried to parallelize next-patch prediction by shifting to multi-patch prediction to accelerate the process, but only achieved limited parallelization. To achieve high parallelization while maintaining 生成 quality, we introduce two key techniques: (1) Flexible Parallelized Autoregressive Modeling, a novel 架构 that enables arbitrary 生成 ordering and degrees of parallelization. It uses learnable position query tokens to guide 生成 at 目标 positions while ensuring mutual visibility among concurrently generated tokens for consistent 并行 decoding....

**Original Abstract**:
> arXiv:2507.01957v2 Announce Type: replace-cross 
Abstract: We present Locality-aware Parallel Decoding (LPD) to accelerate autoregressive image generation. Traditional autoregressive image generation relies on next-patch prediction, a memory-bound process that leads to high latency. Existing works have tried to parallelize next-patch prediction by shifting to multi-patch prediction to accelerate the process, but only achieved limited parallelization. To achieve high parallelization while maintaining generation quality, we introduce two key techniques: (1) Flexible Parallelized Autoregressive Modeling, a novel architecture that enables arbitrary generation ordering and degrees of parallelization. It uses learnable position query tokens to guide generation at target positions while ensuring ...

---

## 421. Technological folie \`a deux: Feedback Loops Between AI Chatbots and Mental Illness

**原标题**: Technological folie \`a deux: Feedback Loops Between AI Chatbots and Mental Illness

**作者**: Sebastian Dohn\'any, Zeb Kurth-Nelson, Eleanor Spens, Lennart Luettgau, Alastair Reid, Iason Gabriel, Christopher Summerfield, Murray Shanahan, Matthew M Nour
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2507.19218v3

**中文摘要**:
> arXiv:2507.19218v3 Announce Type: replace-cross 
摘要: Artificial intelligence chatbots have achieved unprecedented adoption, with millions now using these systems for emotional support and companionship in contexts of widespread social isolation and capacity-constrained mental health services. While some users report psychological benefits, concerning edge cases are emerging, including reports of suicide, violence, and delusional thinking linked to perceived emotional relationships with chatbots. To understand this new risk profile we need to consider the interaction between human cognitive and emotional biases, and chatbot behavioural tendencies such as agreeableness (sycophancy) and adaptability (in-context 学习). We argue that individuals with mental health conditions face increased risks ...

**Original Abstract**:
> arXiv:2507.19218v3 Announce Type: replace-cross 
Abstract: Artificial intelligence chatbots have achieved unprecedented adoption, with millions now using these systems for emotional support and companionship in contexts of widespread social isolation and capacity-constrained mental health services. While some users report psychological benefits, concerning edge cases are emerging, including reports of suicide, violence, and delusional thinking linked to perceived emotional relationships with chatbots. To understand this new risk profile we need to consider the interaction between human cognitive and emotional biases, and chatbot behavioural tendencies such as agreeableness (sycophancy) and adaptability (in-context learning). We argue that individuals with mental health conditions face incr...

---

## 422. Shadow in the Cache: Unveiling and Mitigating 隐私 Risks of KV-cache in 大语言模型 推理

**原标题**: Shadow in the Cache: Unveiling and Mitigating Privacy Risks of KV-cache in LLM Inference

**作者**: Zhifan Luo, Shuo Shao, Su Zhang, Lijing Zhou, Yuke Hu, Chenxu Zhao, Zhihao Liu, Zhan Qin
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2508.09442v4

**中文摘要**:
> arXiv:2508.09442v4 Announce Type: replace-cross 
摘要: The Key-价值 (KV) cache, which stores intermediate 注意力 computations (Key and 价值 pairs) to avoid redundant calculations, is a fundamental mechanism for accelerating Large Language 模型 (大语言模型) 推理. However, this efficiency 优化 introduces significant yet underexplored 隐私 risks. This 论文 provides the first comprehensive analysis of these vulnerabilities, demonstrating that an attacker can reconstruct sensitive user inputs directly from the KV-cache. We design and implement three distinct attack vectors: a direct Inversion Attack, a more broadly applicable and potent Collision Attack, and a semantic-based Injection Attack. These methods demonstrate the practicality and severity of KV-cache 隐私 leakage issues. To mitigate this, we propose KV-Cloak, a...

**Original Abstract**:
> arXiv:2508.09442v4 Announce Type: replace-cross 
Abstract: The Key-Value (KV) cache, which stores intermediate attention computations (Key and Value pairs) to avoid redundant calculations, is a fundamental mechanism for accelerating Large Language Model (LLM) inference. However, this efficiency optimization introduces significant yet underexplored privacy risks. This paper provides the first comprehensive analysis of these vulnerabilities, demonstrating that an attacker can reconstruct sensitive user inputs directly from the KV-cache. We design and implement three distinct attack vectors: a direct Inversion Attack, a more broadly applicable and potent Collision Attack, and a semantic-based Injection Attack. These methods demonstrate the practicality and severity of KV-cache privacy leakage...

---

## 423. MonitorVLM:A Vision Language 框架 for Safety Violation 检测 in Mining Operations

**原标题**: MonitorVLM:A Vision Language Framework for Safety Violation Detection in Mining Operations

**作者**: Jiang Wu, Sichao Wu, Yinsong Ma, Guangyuan Yu, Haoyuan Xu, Lifang Zheng, Jingliang Duan
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2510.03666v2

**中文摘要**:
> arXiv:2510.03666v2 Announce Type: replace-cross 
摘要: Industrial accidents, particularly in high-risk domains such as surface and underground mining, are frequently caused by unsafe worker behaviors. Traditional manual inspection remains labor-intensive, error-prone, and insufficient for large-scale, 动态 environments, highlighting the urgent need for intelligent and automated safety monitoring. In this 论文, we present MonitorVLM, a novel vision--language 框架 designed to detect safety violations directly from surveillance 视频 streams. MonitorVLM introduces three key innovations: (1) a domain-specific violation 数据集 comprising 9,000 vision--question--answer (VQA) samples across 40 high-frequency mining regulations, enriched with augmentation and auxiliary 检测 cues; (2) a clause filter (CF) module t...

**Original Abstract**:
> arXiv:2510.03666v2 Announce Type: replace-cross 
Abstract: Industrial accidents, particularly in high-risk domains such as surface and underground mining, are frequently caused by unsafe worker behaviors. Traditional manual inspection remains labor-intensive, error-prone, and insufficient for large-scale, dynamic environments, highlighting the urgent need for intelligent and automated safety monitoring. In this paper, we present MonitorVLM, a novel vision--language framework designed to detect safety violations directly from surveillance video streams. MonitorVLM introduces three key innovations: (1) a domain-specific violation dataset comprising 9,000 vision--question--answer (VQA) samples across 40 high-frequency mining regulations, enriched with augmentation and auxiliary detection cues...

---

## 424. Reveal-to-Revise: 可解释 偏见-Aware 生成式 Modeling with Multimodal 注意力

**原标题**: Reveal-to-Revise: Explainable Bias-Aware Generative Modeling with Multimodal Attention

**作者**: Noor Islam S. Mohammad, Md Muntaqim Meherab
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2510.12957v2

**中文摘要**:
> arXiv:2510.12957v2 Announce Type: replace-cross 
摘要: We present an 可解释, 偏见-aware 生成式 框架 that unifies cross-modal 注意力 fusion, Grad-CAM++ attribution, and a Reveal-to-Revise feedback loop within a single 训练 paradigm. The 架构 couples a conditional 注意力 WGAN GP with 偏见 正则化 and iterative local explanation feedback and is evaluated on Multimodal MNIST and Fashion MNIST for 图像 生成 and subgroup auditing, as well as a toxic/non-toxic text 分类 基准. All experiments use stratified 80/20 splits, validation-based early stopping, and AdamW with cosine annealing, and results are averaged over three random seeds. The proposed 模型 achieves 93.2% accuracy, a 91.6% F1-score, and a 78.1% IoU-XAI on the multimodal 基准, outperforming all baselines across every metric, while 对抗 训练 restores 73 to 77% 鲁棒性 on Fashion MNIST...

**Original Abstract**:
> arXiv:2510.12957v2 Announce Type: replace-cross 
Abstract: We present an explainable, bias-aware generative framework that unifies cross-modal attention fusion, Grad-CAM++ attribution, and a Reveal-to-Revise feedback loop within a single training paradigm. The architecture couples a conditional attention WGAN GP with bias regularization and iterative local explanation feedback and is evaluated on Multimodal MNIST and Fashion MNIST for image generation and subgroup auditing, as well as a toxic/non-toxic text classification benchmark. All experiments use stratified 80/20 splits, validation-based early stopping, and AdamW with cosine annealing, and results are averaged over three random seeds. The proposed model achieves 93.2% accuracy, a 91.6% F1-score, and a 78.1% IoU-XAI on the multimodal ...

---

## 425. Predicting kernel regression 学习 curves from only raw data statistics

**原标题**: Predicting kernel regression learning curves from only raw data statistics

**作者**: Dhruva Karkada, Joseph Turnbull, Yuxi Liu, James B. Simon
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2510.14878v2

**中文摘要**:
> arXiv:2510.14878v2 Announce Type: replace-cross 
摘要: We study kernel regression with common rotation-invariant kernels on real datasets including CIFAR-5m, SVHN, and ImageNet. We give a theoretical 框架 that predicts 学习 curves (test risk vs. sample size) from only two measurements: the empirical data covariance matrix and an empirical polynomial decomposition of the 目标 function $f_*$. The key new idea is an analytical approximation of a kernel's eigenvalues and eigenfunctions with respect to an anisotropic data distribution. The eigenfunctions resemble Hermite polynomials of the data, so we call this approximation the Hermite eigenstructure ansatz (HEA). We prove the HEA for Gaussian data, but we find that real 图像 data is often "Gaussian enough" for the HEA to hold well in practice, enabling...

**Original Abstract**:
> arXiv:2510.14878v2 Announce Type: replace-cross 
Abstract: We study kernel regression with common rotation-invariant kernels on real datasets including CIFAR-5m, SVHN, and ImageNet. We give a theoretical framework that predicts learning curves (test risk vs. sample size) from only two measurements: the empirical data covariance matrix and an empirical polynomial decomposition of the target function $f_*$. The key new idea is an analytical approximation of a kernel's eigenvalues and eigenfunctions with respect to an anisotropic data distribution. The eigenfunctions resemble Hermite polynomials of the data, so we call this approximation the Hermite eigenstructure ansatz (HEA). We prove the HEA for Gaussian data, but we find that real image data is often "Gaussian enough" for the HEA to hold ...

---

## 426. KV Cache Transform Coding for Compact 存储 in 大语言模型 推理

**原标题**: KV Cache Transform Coding for Compact Storage in LLM Inference

**作者**: Konrad Staniszewski, Adrian {\L}a\'ncucki
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2511.01815v2

**中文摘要**:
> arXiv:2511.01815v2 Announce Type: replace-cross 
摘要: 服务 large language models (LLMs) at scale necessitates 高效 key-价值 (KV) cache management. KV caches can be reused across conversation turns via shared-prefix prompts that are common in iterative 代码 editing and chat. However, stale caches consume scarce GPU 内存, require offloading, or force recomputation. We present KVTC, a lightweight transform coder that compresses KV caches for compact on-GPU and off-GPU 存储. Drawing on classical media compression, KVTC combines PCA-based 特征 decorrelation, adaptive quantization, and 熵 coding. It requires only a brief initial calibration and leaves 模型 parameters unchanged. By exploiting redundancies in KV caches, KVTC achieves up to 20$\times$ compression while maintaining 推理 and long-context accuracy, and 4...

**Original Abstract**:
> arXiv:2511.01815v2 Announce Type: replace-cross 
Abstract: Serving large language models (LLMs) at scale necessitates efficient key-value (KV) cache management. KV caches can be reused across conversation turns via shared-prefix prompts that are common in iterative code editing and chat. However, stale caches consume scarce GPU memory, require offloading, or force recomputation. We present KVTC, a lightweight transform coder that compresses KV caches for compact on-GPU and off-GPU storage. Drawing on classical media compression, KVTC combines PCA-based feature decorrelation, adaptive quantization, and entropy coding. It requires only a brief initial calibration and leaves model parameters unchanged. By exploiting redundancies in KV caches, KVTC achieves up to 20$\times$ compression while m...

---

## 427. DeepEyesV2: Toward Agentic Multimodal 模型

**原标题**: DeepEyesV2: Toward Agentic Multimodal Model

**作者**: Jack Hong, Chenxiao Zhao, ChengLin Zhu, Weiheng Lu, Guohai Xu, Xing Yu
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2511.05271v4

**中文摘要**:
> arXiv:2511.05271v4 Announce Type: replace-cross 
摘要: Agentic multimodal models should not only comprehend text and images, but also actively invoke external tools, such as 代码 execution environments and web 搜索, and integrate these operations into 推理. In this work, we introduce DeepEyesV2 and explore how to build an agentic multimodal 模型 from the perspectives of data construction, 训练 methods, and 模型 评估. We observe that direct 强化 学习 alone fails to induce 鲁棒 tool-use behavior. This phenomenon motivates a two-stage 训练 pipeline: a cold-start stage to establish tool-use patterns, and 强化 学习 stage to further refine tool invocation. We curate a diverse, moderately challenging 训练 数据集, specifically including examples where tool use is beneficial. We further introduce RealX-Bench, a comprehensive 基准 de...

**Original Abstract**:
> arXiv:2511.05271v4 Announce Type: replace-cross 
Abstract: Agentic multimodal models should not only comprehend text and images, but also actively invoke external tools, such as code execution environments and web search, and integrate these operations into reasoning. In this work, we introduce DeepEyesV2 and explore how to build an agentic multimodal model from the perspectives of data construction, training methods, and model evaluation. We observe that direct reinforcement learning alone fails to induce robust tool-use behavior. This phenomenon motivates a two-stage training pipeline: a cold-start stage to establish tool-use patterns, and reinforcement learning stage to further refine tool invocation. We curate a diverse, moderately challenging training dataset, specifically including e...

---

## 428. MediRound: Multi-Round Entity-Level 推理 分割 in Medical Images

**原标题**: MediRound: Multi-Round Entity-Level Reasoning Segmentation in Medical Images

**作者**: Qinyue Tong, Ziqian Lu, Jun Liu, Rui Zuo, Zheming Lu, Yueming Jin
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2511.12110v4

**中文摘要**:
> arXiv:2511.12110v4 Announce Type: replace-cross 
摘要: Despite recent progress in text-prompt-based medical 图像 分割, these methods are limited to single-round dialogues and fail to support multi-round 推理, which is important for medical education scenarios. In this work, we introduce Multi-Round Entity-Level Medical 推理 分割 (MEMR-Seg), a new task that requires generating 分割 masks through multi-round queries with entity-level 推理, helping learners progressively develop their understanding of medical knowledge. To support this task, we construct MR-MedSeg, a large-scale 数据集 of 177K multi-round medical 分割 dialogues, featuring entity-based 推理 across rounds. Furthermore, we propose MediRound, an effective baseline 模型 designed for multi-round medical 推理 分割. To mitigate the inherent error propagation wit...

**Original Abstract**:
> arXiv:2511.12110v4 Announce Type: replace-cross 
Abstract: Despite recent progress in text-prompt-based medical image segmentation, these methods are limited to single-round dialogues and fail to support multi-round reasoning, which is important for medical education scenarios. In this work, we introduce Multi-Round Entity-Level Medical Reasoning Segmentation (MEMR-Seg), a new task that requires generating segmentation masks through multi-round queries with entity-level reasoning, helping learners progressively develop their understanding of medical knowledge. To support this task, we construct MR-MedSeg, a large-scale dataset of 177K multi-round medical segmentation dialogues, featuring entity-based reasoning across rounds. Furthermore, we propose MediRound, an effective baseline model de...

---

## 429. STREAM-VAE: Dual-Path Routing for Slow and Fast Dynamics in Vehicle Telemetry Anomaly 检测

**原标题**: STREAM-VAE: Dual-Path Routing for Slow and Fast Dynamics in Vehicle Telemetry Anomaly Detection

**作者**: Kadir-Kaan \"Ozer, Ren\'e Ebeling, Markus Enzweiler
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2511.15339v2

**中文摘要**:
> arXiv:2511.15339v2 Announce Type: replace-cross 
摘要: Automotive telemetry data exhibits slow drifts and fast spikes, often within the same sequence, making reliable anomaly 检测 challenging. Standard reconstruction-based methods, including sequence variational autoencoders (VAEs), use a single 隐变量 process and therefore mix heterogeneous time scales, which can smooth out spikes or inflate variances and weaken anomaly separation.
  In this 论文, we present STREAM-VAE, a variational autoencoder for anomaly 检测 in automotive telemetry time-series data. Our 模型 uses a dual-path encoder to separate slow drift and fast spike signal dynamics, and a decoder that represents transient deviations separately from the normal operating pattern. STREAM-VAE is designed for 部署, producing stable anomaly scores acr...

**Original Abstract**:
> arXiv:2511.15339v2 Announce Type: replace-cross 
Abstract: Automotive telemetry data exhibits slow drifts and fast spikes, often within the same sequence, making reliable anomaly detection challenging. Standard reconstruction-based methods, including sequence variational autoencoders (VAEs), use a single latent process and therefore mix heterogeneous time scales, which can smooth out spikes or inflate variances and weaken anomaly separation.
  In this paper, we present STREAM-VAE, a variational autoencoder for anomaly detection in automotive telemetry time-series data. Our model uses a dual-path encoder to separate slow drift and fast spike signal dynamics, and a decoder that represents transient deviations separately from the normal operating pattern. STREAM-VAE is designed for deployment...

---

## 430. REMSA: Foundation 模型 选择 for Remote Sensing via a Constraint-Aware 智能体

**原标题**: REMSA: Foundation Model Selection for Remote Sensing via a Constraint-Aware Agent

**作者**: Binger Chen, Tacettin Emre B\"ok, Behnood Rasti, Volker Markl, Beg\"um Demir
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2511.17442v2

**中文摘要**:
> arXiv:2511.17442v2 Announce Type: replace-cross 
摘要: Foundation Models (FMs) are increasingly integrated into remote sensing (RS) pipelines. These models include unimodal vision encoders and multimodal architectures. FMs are adapted to diverse perception tasks, such as 图像 分类, change 检测, and 视觉 question answering. However, selecting the most suitable remote sensing foundation 模型 (RSFM) for a specific task remains challenging due to scattered documentation, heterogeneous formats, and complex 部署 constraints. To address this, we first introduce the RSFM Database (RS-FMD), the first structured and schema-guided resource covering over 160 RSFMs trained on various data modalities, spanning different spatial, spectral, and temporal resolutions, considering different 学习 paradigms. Built upon RS-FMD...

**Original Abstract**:
> arXiv:2511.17442v2 Announce Type: replace-cross 
Abstract: Foundation Models (FMs) are increasingly integrated into remote sensing (RS) pipelines. These models include unimodal vision encoders and multimodal architectures. FMs are adapted to diverse perception tasks, such as image classification, change detection, and visual question answering. However, selecting the most suitable remote sensing foundation model (RSFM) for a specific task remains challenging due to scattered documentation, heterogeneous formats, and complex deployment constraints. To address this, we first introduce the RSFM Database (RS-FMD), the first structured and schema-guided resource covering over 160 RSFMs trained on various data modalities, spanning different spatial, spectral, and temporal resolutions, considerin...

---

## 431. Hierarchical Dual-Strategy Unlearning for Biomedical and Healthcare Intelligence Using Imperfect and 隐私-Sensitive Medical Data

**原标题**: Hierarchical Dual-Strategy Unlearning for Biomedical and Healthcare Intelligence Using Imperfect and Privacy-Sensitive Medical Data

**作者**: Yi Zhang, Chao Zhang, Zijian Li, Tianxiang Xu, Kunyu Zhang, Zhan Gao, Meinuo Li, Xiaohan Zhang, Qichao Qi, Bing Chen
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2511.19498v2

**中文摘要**:
> arXiv:2511.19498v2 Announce Type: replace-cross 
摘要: Large language models (LLMs) exhibit exceptional 性能 but pose substantial 隐私 risks due to 训练 data memorization, particularly within healthcare contexts involving imperfect or 隐私-sensitive patient information. We present a hierarchical dual-strategy 框架 for selective knowledge unlearning that precisely removes specialized knowledge while preserving fundamental medical competencies. Our 方案 synergistically integrates geometric-constrained 梯度 updates to selectively modulate 目标 parameters with concept-aware token-level interventions that distinguish between preservation-critical and unlearning-targeted tokens via a unified four-level medical concept hierarchy. Comprehensive evaluations on the MedMCQA (surgical) and MHQA (anxiety, depression, tr...

**Original Abstract**:
> arXiv:2511.19498v2 Announce Type: replace-cross 
Abstract: Large language models (LLMs) exhibit exceptional performance but pose substantial privacy risks due to training data memorization, particularly within healthcare contexts involving imperfect or privacy-sensitive patient information. We present a hierarchical dual-strategy framework for selective knowledge unlearning that precisely removes specialized knowledge while preserving fundamental medical competencies. Our approach synergistically integrates geometric-constrained gradient updates to selectively modulate target parameters with concept-aware token-level interventions that distinguish between preservation-critical and unlearning-targeted tokens via a unified four-level medical concept hierarchy. Comprehensive evaluations on th...

---

## 432. World Models That Know When They Don't Know - Controllable 视频 生成 with Calibrated Uncertainty

**原标题**: World Models That Know When They Don't Know - Controllable Video Generation with Calibrated Uncertainty

**作者**: Zhiting Mei, Tenny Yin, Micah Baker, Ola Shorinwa, Anirudha Majumdar
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2512.05927v2

**中文摘要**:
> arXiv:2512.05927v2 Announce Type: replace-cross 
摘要: Recent advances in 生成式 视频 models have led to significant breakthroughs in high-fidelity 视频 合成, specifically in controllable 视频 生成 where the generated 视频 is conditioned on text and 动作 inputs, e.g., in instruction-guided 视频 editing and world modeling in 机器人. Despite these exceptional capabilities, controllable 视频 models often hallucinate - generating future 视频 frames that are misaligned with physical reality - which raises serious concerns in many tasks such as robot 策略 评估 and 规划. However, 状态-of-the-art 视频 models lack the ability to assess and express their confidence, impeding hallucination mitigation. To rigorously address this challenge, we propose C3, an uncertainty quantification (UQ) 方法 for 训练 continuous-scale calibrated controllable...

**Original Abstract**:
> arXiv:2512.05927v2 Announce Type: replace-cross 
Abstract: Recent advances in generative video models have led to significant breakthroughs in high-fidelity video synthesis, specifically in controllable video generation where the generated video is conditioned on text and action inputs, e.g., in instruction-guided video editing and world modeling in robotics. Despite these exceptional capabilities, controllable video models often hallucinate - generating future video frames that are misaligned with physical reality - which raises serious concerns in many tasks such as robot policy evaluation and planning. However, state-of-the-art video models lack the ability to assess and express their confidence, impeding hallucination mitigation. To rigorously address this challenge, we propose C3, an ...

---

## 433. Maximum Risk Minimization with Random Forests

**原标题**: Maximum Risk Minimization with Random Forests

**作者**: Francesco Freni, Anya Fries, Linus K\"uhne, Markus Reichstein, Jonas Peters
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2512.10445v2

**中文摘要**:
> arXiv:2512.10445v2 Announce Type: replace-cross 
摘要: We consider a regression setting where observations are collected in different environments modeled by different data distributions. The field of 分布外 (OOD) 泛化 aims to design methods that generalize better to test environments whose distributions differ from those observed during 训练. One line of such works has proposed to minimize the maximum risk across environments, a principle that we refer to as MaxRM (Maximum Risk Minimization). In this work, we introduce variants of random forests based on the principle of MaxRM. We provide computationally 高效 algorithms and prove statistical consistency for our primary 方法. Our proposed 方法 can be used with each of the following three risks: the mean squared error, the negative 奖励, and the regret (whi...

**Original Abstract**:
> arXiv:2512.10445v2 Announce Type: replace-cross 
Abstract: We consider a regression setting where observations are collected in different environments modeled by different data distributions. The field of out-of-distribution (OOD) generalization aims to design methods that generalize better to test environments whose distributions differ from those observed during training. One line of such works has proposed to minimize the maximum risk across environments, a principle that we refer to as MaxRM (Maximum Risk Minimization). In this work, we introduce variants of random forests based on the principle of MaxRM. We provide computationally efficient algorithms and prove statistical consistency for our primary method. Our proposed method can be used with each of the following three risks: the m...

---

## 434. GTR-Turbo: Merged Checkpoint is Secretly a Free Teacher for Agentic VLM 训练

**原标题**: GTR-Turbo: Merged Checkpoint is Secretly a Free Teacher for Agentic VLM Training

**作者**: Tong Wei, Yijun Yang, Changhao Zhang, Junliang Xing, Yuanchun Shi, Zongqing Lu, Deheng Ye
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2512.13043v2

**中文摘要**:
> arXiv:2512.13043v2 Announce Type: replace-cross 
摘要: Multi-turn 强化 学习 (RL) for 多模态 agents built upon vision-language models (VLMs) is hampered by sparse rewards and long-视野 credit assignment. Recent methods densify the 奖励 by querying a teacher that provides step-level feedback, e.g., Guided Thought 强化 (GTR) and On-策略 Distillation, but rely on costly, often privileged models as the teacher, limiting practicality and reproducibility. We introduce GTR-Turbo, a highly 高效 upgrade to GTR that matches its 性能 without 训练 on or querying an expensive teacher 模型. Specifically, GTR-Turbo merges the weights of checkpoints produced during ongoing RL 训练 and then uses the resulting merged 模型 as a "free" teacher to guide subsequent RL via 有监督 fine-tuning or soft logit distillation. This design removes depen...

**Original Abstract**:
> arXiv:2512.13043v2 Announce Type: replace-cross 
Abstract: Multi-turn reinforcement learning (RL) for multi-modal agents built upon vision-language models (VLMs) is hampered by sparse rewards and long-horizon credit assignment. Recent methods densify the reward by querying a teacher that provides step-level feedback, e.g., Guided Thought Reinforcement (GTR) and On-Policy Distillation, but rely on costly, often privileged models as the teacher, limiting practicality and reproducibility. We introduce GTR-Turbo, a highly efficient upgrade to GTR that matches its performance without training on or querying an expensive teacher model. Specifically, GTR-Turbo merges the weights of checkpoints produced during ongoing RL training and then uses the resulting merged model as a "free" teacher to guid...

---

## 435. The 贝叶斯 Geometry of Transformer 注意力

**原标题**: The Bayesian Geometry of Transformer Attention

**作者**: Naman Agarwal, Siddhartha R. Dalal, Vishal Misra
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2512.22471v4

**中文摘要**:
> arXiv:2512.22471v4 Announce Type: replace-cross 
摘要: Transformers often appear to perform 贝叶斯 推理 in context, but verifying this rigorously has been impossible: natural data lack analytic posteriors, and large models conflate 推理 with memorization. We address this by constructing \emph{贝叶斯 wind tunnels} -- controlled environments where the true posterior is known in closed form and memorization is provably impossible. In these settings, small transformers reproduce 贝叶斯 posteriors with $10^{-3}$-$10^{-4}$ bit accuracy, while capacity-matched MLPs fail by orders of magnitude, establishing a clear architectural separation.
  Across two tasks -- bijection elimination and Hidden Markov 模型 (HMM) 状态 tracking -- we find that transformers implement 贝叶斯 推理 through a consistent geometric mechanism: res...

**Original Abstract**:
> arXiv:2512.22471v4 Announce Type: replace-cross 
Abstract: Transformers often appear to perform Bayesian reasoning in context, but verifying this rigorously has been impossible: natural data lack analytic posteriors, and large models conflate reasoning with memorization. We address this by constructing \emph{Bayesian wind tunnels} -- controlled environments where the true posterior is known in closed form and memorization is provably impossible. In these settings, small transformers reproduce Bayesian posteriors with $10^{-3}$-$10^{-4}$ bit accuracy, while capacity-matched MLPs fail by orders of magnitude, establishing a clear architectural separation.
  Across two tasks -- bijection elimination and Hidden Markov Model (HMM) state tracking -- we find that transformers implement Bayesian in...

---

## 436. 梯度 Dynamics of 注意力: How Cross-熵 Sculpts 贝叶斯 Manifolds

**原标题**: Gradient Dynamics of Attention: How Cross-Entropy Sculpts Bayesian Manifolds

**作者**: Naman Agarwal, Siddhartha R. Dalal, Vishal Misra
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2512.22473v4

**中文摘要**:
> arXiv:2512.22473v4 Announce Type: replace-cross 
摘要: Transformers empirically perform precise 概率 推理 in carefully constructed ``贝叶斯 wind tunnels'' and in large-scale language models, yet the mechanisms by which 梯度-based 学习 creates the required internal geometry remain opaque. We provide a complete first-order analysis of how cross-熵 训练 reshapes 注意力 scores and 价值 vectors in a Transformer 注意力 head. Our core 结果 is an \emph{优势-based routing law} for 注意力 scores, \[ \frac{\partial L}{\partial s_{ij}} = \alpha_{ij}\bigl(b_{ij}-\mathbb{E}_{\alpha_i}[b]\bigr), \qquad b_{ij} := u_i^\top v_j, \] coupled with a \emph{responsibility-weighted update} for values, \[ \Delta v_j = -\eta\sum_i \alpha_{ij} u_i, \] where $u_i$ is the upstream 梯度 at position $i$ and $\alpha_{ij}$ are 注意力 weights. These equation...

**Original Abstract**:
> arXiv:2512.22473v4 Announce Type: replace-cross 
Abstract: Transformers empirically perform precise probabilistic reasoning in carefully constructed ``Bayesian wind tunnels'' and in large-scale language models, yet the mechanisms by which gradient-based learning creates the required internal geometry remain opaque. We provide a complete first-order analysis of how cross-entropy training reshapes attention scores and value vectors in a transformer attention head. Our core result is an \emph{advantage-based routing law} for attention scores, \[ \frac{\partial L}{\partial s_{ij}} = \alpha_{ij}\bigl(b_{ij}-\mathbb{E}_{\alpha_i}[b]\bigr), \qquad b_{ij} := u_i^\top v_j, \] coupled with a \emph{responsibility-weighted update} for values, \[ \Delta v_j = -\eta\sum_i \alpha_{ij} u_i, \] where $u_i$...

---

## 437. Over-Searching in 搜索-Augmented Large Language Models

**原标题**: Over-Searching in Search-Augmented Large Language Models

**作者**: Roy Xie, Deepak Gopinath, David Qiu, Dong Lin, Haitian Sun, Saloni Potdar, Bhuwan Dhingra
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2601.05503v2

**中文摘要**:
> arXiv:2601.05503v2 Announce Type: replace-cross 
摘要: 搜索-augmented large language models (LLMs) excel at knowledge-intensive tasks by integrating external 检索. However, they often over-搜索 -- unnecessarily invoking 搜索 tool even when it does not improve response quality, which leads to computational inefficiency and hallucinations by incorporating irrelevant context. In this work, we conduct a systematic 评估 of over-searching across multiple dimensions, including query types, 模型 categories, 检索 conditions, and multi-turn conversations. Our finding shows: (i) 搜索 generally improves answer accuracy on answerable queries but harms abstention on unanswerable ones; (ii) over-searching is more pronounced in complex 推理 models and 深度 research systems, is exacerbated by noisy 检索, and compounds across turn...

**Original Abstract**:
> arXiv:2601.05503v2 Announce Type: replace-cross 
Abstract: Search-augmented large language models (LLMs) excel at knowledge-intensive tasks by integrating external retrieval. However, they often over-search -- unnecessarily invoking search tool even when it does not improve response quality, which leads to computational inefficiency and hallucinations by incorporating irrelevant context. In this work, we conduct a systematic evaluation of over-searching across multiple dimensions, including query types, model categories, retrieval conditions, and multi-turn conversations. Our finding shows: (i) search generally improves answer accuracy on answerable queries but harms abstention on unanswerable ones; (ii) over-searching is more pronounced in complex reasoning models and deep research system...

---

## 438. Burn-After-Use for Preventing Data Leakage through a 安全 Multi-Tenant 架构 in Enterprise 大语言模型

**原标题**: Burn-After-Use for Preventing Data Leakage through a Secure Multi-Tenant Architecture in Enterprise LLM

**作者**: Qiang Zhang, Elena Emma Wang, Jiaming Li, Xichun Wang
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2601.06627v3

**中文摘要**:
> arXiv:2601.06627v3 Announce Type: replace-cross 
摘要: This study presents a 安全 Multi-Tenant 架构 (SMTA) combined with a novel concept Burn-After-Use (BAU) mechanism for enterprise 大语言模型 environments to effectively prevent data leakage. As institutions increasingly adopt LLMs across departments, the risks of data leakage have become a critical security and compliance concern. The proposed SMTA isolates 大语言模型 instances across departments and enforces rigorous context ownership boundaries within an internally deployed infrastructure. The BAU mechanism introduces data confidentiality by enforcing ephemeral conversational contexts that are automatically destroyed after use, preventing cross-session or cross-user 推理. The 评估 to SMTA and BAU is through two sets of realistic and reproducible experimen...

**Original Abstract**:
> arXiv:2601.06627v3 Announce Type: replace-cross 
Abstract: This study presents a Secure Multi-Tenant Architecture (SMTA) combined with a novel concept Burn-After-Use (BAU) mechanism for enterprise LLM environments to effectively prevent data leakage. As institutions increasingly adopt LLMs across departments, the risks of data leakage have become a critical security and compliance concern. The proposed SMTA isolates LLM instances across departments and enforces rigorous context ownership boundaries within an internally deployed infrastructure. The BAU mechanism introduces data confidentiality by enforcing ephemeral conversational contexts that are automatically destroyed after use, preventing cross-session or cross-user inference. The evaluation to SMTA and BAU is through two sets of reali...

---

## 439. Beyond Max Tokens: Stealthy Resource Amplification via Tool Calling Chains in 大语言模型 Agents

**原标题**: Beyond Max Tokens: Stealthy Resource Amplification via Tool Calling Chains in LLM Agents

**作者**: Kaiyu Zhou, Yongsen Zheng, Yicheng He, Meng Xue, Xueluan Gong, Yuji Wang, Xuanye Zhang, Kwok-Yan Lam
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2601.10955v2

**中文摘要**:
> arXiv:2601.10955v2 Announce Type: replace-cross 
摘要: The 智能体--tool interaction loop is a critical attack surface for modern Large Language 模型 (大语言模型) agents. Existing denial-of-service (DoS) attacks typically function at the user-prompt or 检索-augmented 生成 (RAG) context layer and are inherently single-turn in nature. This limitation restricts cost amplification and diminishes stealth in goal-oriented workflows. To address these issues, we proposed a stealthy, multi-turn economic DoS attack at the tool layer under the 模型 Context Protocol (MCP). By simply editing text-visible fields and implementing a template-driven 回报 策略, our malicious 服务器 preserves function signatures and the terminal benign payload while steering agents into prolonged, verbose tool-calling chains. We optimize these text-o...

**Original Abstract**:
> arXiv:2601.10955v2 Announce Type: replace-cross 
Abstract: The agent--tool interaction loop is a critical attack surface for modern Large Language Model (LLM) agents. Existing denial-of-service (DoS) attacks typically function at the user-prompt or retrieval-augmented generation (RAG) context layer and are inherently single-turn in nature. This limitation restricts cost amplification and diminishes stealth in goal-oriented workflows. To address these issues, we proposed a stealthy, multi-turn economic DoS attack at the tool layer under the Model Context Protocol (MCP). By simply editing text-visible fields and implementing a template-driven return policy, our malicious server preserves function signatures and the terminal benign payload while steering agents into prolonged, verbose tool-ca...

---

## 440. Hallucination is a Consequence of Space-Optimality: A Rate-Distortion Theorem for Membership Testing

**原标题**: Hallucination is a Consequence of Space-Optimality: A Rate-Distortion Theorem for Membership Testing

**作者**: Anxin Guo, Jingwei Li
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2602.00906v5

**中文摘要**:
> arXiv:2602.00906v5 Announce Type: replace-cross 
摘要: Large language models often hallucinate with high confidence on "random facts" that lack inferable patterns. We formalize the memorization of such facts as a membership testing problem, unifying the discrete error metrics of Bloom filters with the continuous log-损失 of LLMs. By analyzing this problem in the regime where facts are sparse in the universe of plausible claims, we establish a rate-distortion theorem: the optimal 内存 efficiency is characterized by the minimum KL divergence between score distributions on facts and non-facts. This theoretical 框架 provides a distinctive explanation for hallucination: even with optimal 训练, perfect data, and a simplified "closed world" setting, the information-theoretically optimal strategy under limi...

**Original Abstract**:
> arXiv:2602.00906v5 Announce Type: replace-cross 
Abstract: Large language models often hallucinate with high confidence on "random facts" that lack inferable patterns. We formalize the memorization of such facts as a membership testing problem, unifying the discrete error metrics of Bloom filters with the continuous log-loss of LLMs. By analyzing this problem in the regime where facts are sparse in the universe of plausible claims, we establish a rate-distortion theorem: the optimal memory efficiency is characterized by the minimum KL divergence between score distributions on facts and non-facts. This theoretical framework provides a distinctive explanation for hallucination: even with optimal training, perfect data, and a simplified "closed world" setting, the information-theoretically op...

---

## 441. Evaluating Long-视野 内存 for Multi-Party Collaborative Dialogues

**原标题**: Evaluating Long-Horizon Memory for Multi-Party Collaborative Dialogues

**作者**: Chuanrui Hu, Tong Li, Xingze Gao, Hongda Chen, Yi Bai, Dannong Xu, Tianwei Lin, Xiaohong Li, Yunyun Han, Jian Pei, Yafeng Deng
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2602.01313v3

**中文摘要**:
> arXiv:2602.01313v3 Announce Type: replace-cross 
摘要: Long-term conversational 内存 in practical 大语言模型 applications is inherently collaborative: information is produced by multiple participants, scattered across groups and channels, revised over time, and implicitly grounded in roles and social context. Yet there is currently no established 基准 that evaluates 内存 under interaction patterns resembling real-world 部署, as existing benchmarks largely focus on dyadic or single-topic dialogues. In this 论文, we introduce EverMemBench, the first 基准 designed for long-视野 collaborative 内存, built from multi-party, multi-group conversations spanning over one million tokens with dense cross-topic interleaving, temporally evolving decisions, and 角色-conditioned personas. EverMemBench evaluates 内存 systems using 2...

**Original Abstract**:
> arXiv:2602.01313v3 Announce Type: replace-cross 
Abstract: Long-term conversational memory in practical LLM applications is inherently collaborative: information is produced by multiple participants, scattered across groups and channels, revised over time, and implicitly grounded in roles and social context. Yet there is currently no established benchmark that evaluates memory under interaction patterns resembling real-world deployment, as existing benchmarks largely focus on dyadic or single-topic dialogues. In this paper, we introduce EverMemBench, the first benchmark designed for long-horizon collaborative memory, built from multi-party, multi-group conversations spanning over one million tokens with dense cross-topic interleaving, temporally evolving decisions, and role-conditioned per...

---

## 442. Moving On, Even When You're Broken: Fail-Active 轨迹 生成 via Diffusion Policies Conditioned on Embodiment and Task

**原标题**: Moving On, Even When You're Broken: Fail-Active Trajectory Generation via Diffusion Policies Conditioned on Embodiment and Task

**作者**: Gilberto G. Briscoe-Martinez, Yaashia Gautam, Rahul Shetty, Anuj Pasricha, Marco M. Nicotra, Alessandro Roncone
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2602.02895v2

**中文摘要**:
> arXiv:2602.02895v2 Announce Type: replace-cross 
摘要: Robot failure is detrimental and disruptive, often requiring human intervention to recover. Our vision is 'fail-active' operation, allowing robots to safely complete their tasks even when damaged. Focusing on 'actuation failures', we introduce DEFT, a diffusion-based 轨迹 generator conditioned on the robot's current embodiment and task constraints. DEFT generalizes across failure types, supports constrained and unconstrained motions, and enables task completion under arbitrary failure. We evaluate DEFT in both simulation and real-world scenarios using a 7-DoF robotic arm. DEFT outperforms its baselines over thousands of failure conditions, achieving a 99.5% success rate for unconstrained motions versus RRT's 42.4%, and 46.4% for constraine...

**Original Abstract**:
> arXiv:2602.02895v2 Announce Type: replace-cross 
Abstract: Robot failure is detrimental and disruptive, often requiring human intervention to recover. Our vision is 'fail-active' operation, allowing robots to safely complete their tasks even when damaged. Focusing on 'actuation failures', we introduce DEFT, a diffusion-based trajectory generator conditioned on the robot's current embodiment and task constraints. DEFT generalizes across failure types, supports constrained and unconstrained motions, and enables task completion under arbitrary failure. We evaluate DEFT in both simulation and real-world scenarios using a 7-DoF robotic arm. DEFT outperforms its baselines over thousands of failure conditions, achieving a 99.5% success rate for unconstrained motions versus RRT's 42.4%, and 46.4% ...

---

## 443. WebAccessVL: Violation-Aware VLM for Web Accessibility

**原标题**: WebAccessVL: Violation-Aware VLM for Web Accessibility

**作者**: Amber Yijia Zheng, Jae Joong Lee, Bedrich Benes, Raymond A. Yeh
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2602.03850v3

**中文摘要**:
> arXiv:2602.03850v3 Announce Type: replace-cross 
摘要: We present a vision-language 模型 (VLM) that automatically edits website HTML to address violations of the Web Content Accessibility Guidelines 2 (WCAG2) while preserving the original design. We formulate this as a 有监督 图像-conditioned program 合成 task, where the 模型 learns to correct HTML given both the 代码 and its 视觉 rendering. We create WebAccessVL, a website 数据集 with manually corrected accessibility violations. We then propose a violation-conditioned VLM that further takes the detected violations' descriptions from a checker as input. This conditioning enables an iterative checker-in-the-loop refinement strategy at test time. We conduct extensive 评估 on both open API and open-weight models. Empirically, our 方法 achieves 0.211 violations per w...

**Original Abstract**:
> arXiv:2602.03850v3 Announce Type: replace-cross 
Abstract: We present a vision-language model (VLM) that automatically edits website HTML to address violations of the Web Content Accessibility Guidelines 2 (WCAG2) while preserving the original design. We formulate this as a supervised image-conditioned program synthesis task, where the model learns to correct HTML given both the code and its visual rendering. We create WebAccessVL, a website dataset with manually corrected accessibility violations. We then propose a violation-conditioned VLM that further takes the detected violations' descriptions from a checker as input. This conditioning enables an iterative checker-in-the-loop refinement strategy at test time. We conduct extensive evaluation on both open API and open-weight models. Empi...

---

## 444. Long Chain-of-Thought Compression via Fine-Grained Group 策略 优化

**原标题**: Long Chain-of-Thought Compression via Fine-Grained Group Policy Optimization

**作者**: Xinchen Han, Hossam Afifi, Michel Marot, Xilu Wang, Lu Yin
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2602.10048v2

**中文摘要**:
> arXiv:2602.10048v2 Announce Type: replace-cross 
摘要: Large Language Models (LLMs) often generate unnecessarily verbose Chain-of-Thought (CoT) 推理 that increases computational costs and 延迟 without proportional 性能 gains. In this 论文, we propose Fine-grained Group 策略 优化 (FGO), a 强化 学习 (RL) 算法 that refines group responses by subdividing them and assigning appropriate weights based on length and 熵, thereby enabling effective CoT compression. Meanwhile, as an enhanced variant of Group Relative 策略 优化 (GRPO), FGO successfully addresses two major limitations of the GRPO: inefficient data utilization and 熵 collapse. We evaluate FGO on multiple 推理 LLMs and benchmarks, including MATH500, AIME24, AMC23, and Minerva. Experimental results show that FGO achieves 高效 CoT compression without degrading 性能, and ...

**Original Abstract**:
> arXiv:2602.10048v2 Announce Type: replace-cross 
Abstract: Large Language Models (LLMs) often generate unnecessarily verbose Chain-of-Thought (CoT) reasoning that increases computational costs and latency without proportional performance gains. In this paper, we propose Fine-grained Group policy Optimization (FGO), a Reinforcement Learning (RL) algorithm that refines group responses by subdividing them and assigning appropriate weights based on length and entropy, thereby enabling effective CoT compression. Meanwhile, as an enhanced variant of Group Relative Policy Optimization (GRPO), FGO successfully addresses two major limitations of the GRPO: inefficient data utilization and entropy collapse. We evaluate FGO on multiple reasoning LLMs and benchmarks, including MATH500, AIME24, AMC23, a...

---

## 445. TikArt: Stabilizing Aperture-Guided Fine-Grained 视觉 推理 with 强化 学习

**原标题**: TikArt: Stabilizing Aperture-Guided Fine-Grained Visual Reasoning with Reinforcement Learning

**作者**: Hao Ding, Zhichuan Yang, Weijie Ge, Ziqin Gao, Chaoyi Lu, Lei Zhao
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2602.14482v2

**中文摘要**:
> arXiv:2602.14482v2 Announce Type: replace-cross 
摘要: Fine-grained 视觉 推理 in multimodal large language models (MLLMs) is bottlenecked by single-pass global 图像 encoding: key evidence often lies in tiny objects, cluttered regions, subtle markings, or dense charts. We present \textbf{TikArt} (\textbf{T}h\textbf{i}n\textbf{k}ing \textbf{A}pe\textbf{rt}ure), an aperture-guided 智能体 that formulates multimodal 推理 as sequential evidence acquisition over regions of interest. TikArt follows a Think--Aperture--Observe (TAO) loop that interleaves language 推理 with two aperture actions: Zoom, which extracts rectangular crops, and Segment, which invokes an off-the-shelf segmenter to produce object-centric mask-based views for irregular targets. A mandatory 观测 step after every aperture 动作 writes local eviden...

**Original Abstract**:
> arXiv:2602.14482v2 Announce Type: replace-cross 
Abstract: Fine-grained visual reasoning in multimodal large language models (MLLMs) is bottlenecked by single-pass global image encoding: key evidence often lies in tiny objects, cluttered regions, subtle markings, or dense charts. We present \textbf{TikArt} (\textbf{T}h\textbf{i}n\textbf{k}ing \textbf{A}pe\textbf{rt}ure), an aperture-guided agent that formulates multimodal reasoning as sequential evidence acquisition over regions of interest. TikArt follows a Think--Aperture--Observe (TAO) loop that interleaves language reasoning with two aperture actions: Zoom, which extracts rectangular crops, and Segment, which invokes an off-the-shelf segmenter to produce object-centric mask-based views for irregular targets. A mandatory Observation ste...

---

## 446. GOT-JEPA: Generic Object Tracking with 模型 Adaptation and Occlusion Handling using Joint-嵌入 Predictive 架构

**原标题**: GOT-JEPA: Generic Object Tracking with Model Adaptation and Occlusion Handling using Joint-Embedding Predictive Architecture

**作者**: Shih-Fang Chen, Jun-Cheng Chen, I-Hong Jhuo, Yen-Yu Lin
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2602.14771v2

**中文摘要**:
> arXiv:2602.14771v2 Announce Type: replace-cross 
摘要: The human 视觉 系统 tracks objects by integrating current observations with previously observed information, adapting to 目标 and scene changes, and 推理 about occlusion at fine granularity. In contrast, recent generic object trackers are often optimized for 训练 targets, which limits 鲁棒性 and 泛化 in unseen scenarios, and their occlusion 推理 remains coarse, lacking detailed modeling of occlusion patterns. To address these limitations in 泛化 and occlusion perception, we propose GOT-JEPA, a 模型-predictive pretraining 框架 that extends JEPA from predicting 图像 features to predicting tracking models. Given identical historical information, a teacher predictor generates pseudo-tracking models from a clean current frame, and a student predictor learns to predic...

**Original Abstract**:
> arXiv:2602.14771v2 Announce Type: replace-cross 
Abstract: The human visual system tracks objects by integrating current observations with previously observed information, adapting to target and scene changes, and reasoning about occlusion at fine granularity. In contrast, recent generic object trackers are often optimized for training targets, which limits robustness and generalization in unseen scenarios, and their occlusion reasoning remains coarse, lacking detailed modeling of occlusion patterns. To address these limitations in generalization and occlusion perception, we propose GOT-JEPA, a model-predictive pretraining framework that extends JEPA from predicting image features to predicting tracking models. Given identical historical information, a teacher predictor generates pseudo-tr...

---

## 447. Conformal Tradeoffs: Operational Profiles Beyond Coverage

**原标题**: Conformal Tradeoffs: Operational Profiles Beyond Coverage

**作者**: Petrus H. Zwart
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2602.18045v3

**中文摘要**:
> arXiv:2602.18045v3 Announce Type: replace-cross 
摘要: Conformal prediction gives exact finite-sample coverage guarantees under exchangeability, but deployed systems are judged by more than coverage alone. For a fixed calibrated rule reused over a finite operational window, stakeholders also care about 部署-facing quantities such as commitment frequency, deferral, and decisive error exposure. These are not determined by coverage: calibration choices with similar coverage can still induce materially different operational profiles. We study this characterization gap in a scoped setting: binary split conformal prediction under exchangeability with a fixed deployed rule. We introduce the Small-Sample Beta Correction (SSBC) which gives finite-sample coverage semantics for the deployed rule: it inve...

**Original Abstract**:
> arXiv:2602.18045v3 Announce Type: replace-cross 
Abstract: Conformal prediction gives exact finite-sample coverage guarantees under exchangeability, but deployed systems are judged by more than coverage alone. For a fixed calibrated rule reused over a finite operational window, stakeholders also care about deployment-facing quantities such as commitment frequency, deferral, and decisive error exposure. These are not determined by coverage: calibration choices with similar coverage can still induce materially different operational profiles. We study this characterization gap in a scoped setting: binary split conformal prediction under exchangeability with a fixed deployed rule. We introduce the Small-Sample Beta Correction (SSBC) which gives finite-sample coverage semantics for the deployed...

---

## 448. No Need For Real Anomaly: MLLM Empowered 零样本 视频 Anomaly 检测

**原标题**: No Need For Real Anomaly: MLLM Empowered Zero-Shot Video Anomaly Detection

**作者**: Zunkai Dai, Ke Li, Jiajia Liu, Jie Yang, Yuanyuan Qiao
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2602.19248v2

**中文摘要**:
> arXiv:2602.19248v2 Announce Type: replace-cross 
摘要: The collection and 检测 of 视频 anomaly data has long been a challenging problem due to its rare occurrence and spatio-temporal scarcity. Existing 视频 anomaly 检测 (VAD) methods under perform in open-world scenarios. Key contributing factors include limited 数据集 diversity, and inadequate understanding of context-dependent anomalous semantics. To address these issues, i) we propose LAVIDA, an end-to-end 零样本 视频 anomaly 检测 框架. ii) LAVIDA employs an Anomaly Exposure Sampler that transforms segmented objects into pseudo-anomalies to enhance 模型 adaptability to unseen anomaly categories. It further integrates a Multimodal Large Language 模型 (MLLM) to bolster semantic comprehension capabilities. Additionally, iii) we design a token compression 方案 based o...

**Original Abstract**:
> arXiv:2602.19248v2 Announce Type: replace-cross 
Abstract: The collection and detection of video anomaly data has long been a challenging problem due to its rare occurrence and spatio-temporal scarcity. Existing video anomaly detection (VAD) methods under perform in open-world scenarios. Key contributing factors include limited dataset diversity, and inadequate understanding of context-dependent anomalous semantics. To address these issues, i) we propose LAVIDA, an end-to-end zero-shot video anomaly detection framework. ii) LAVIDA employs an Anomaly Exposure Sampler that transforms segmented objects into pseudo-anomalies to enhance model adaptability to unseen anomaly categories. It further integrates a Multimodal Large Language Model (MLLM) to bolster semantic comprehension capabilities. ...

---

## 449. PatchDenoiser: Parameter-高效 multi-scale patch 学习 and fusion denoiser for Low-dose CT imaging

**原标题**: PatchDenoiser: Parameter-efficient multi-scale patch learning and fusion denoiser for Low-dose CT imaging

**作者**: Jitindra Fartiyal, Pedro Freire, Sergei K. Turitsyn, Sergei G. Solovski
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2602.21987v2

**中文摘要**:
> arXiv:2602.21987v2 Announce Type: replace-cross 
摘要: Low-dose CT images are essential for reducing radiation exposure in cancer screening, pediatric imaging, and longitudinal monitoring protocols, but their quality is often degraded by noise from low-dose acquisition, patient motion, or scanner limitations, affecting both clinical interpretation and downstream analysis. Traditional filtering approaches often over-smooth and lose fine anatomical details, while 深度 学习 methods, including CNNs, GANs, and transformers, may struggle to preserve such details or require large, computationally expensive models, limiting clinical practicality. We propose PatchDenoiser, a lightweight, energy-高效 multi-scale patch-based denoising 框架. It decomposes denoising into local texture extraction and global conte...

**Original Abstract**:
> arXiv:2602.21987v2 Announce Type: replace-cross 
Abstract: Low-dose CT images are essential for reducing radiation exposure in cancer screening, pediatric imaging, and longitudinal monitoring protocols, but their quality is often degraded by noise from low-dose acquisition, patient motion, or scanner limitations, affecting both clinical interpretation and downstream analysis. Traditional filtering approaches often over-smooth and lose fine anatomical details, while deep learning methods, including CNNs, GANs, and transformers, may struggle to preserve such details or require large, computationally expensive models, limiting clinical practicality. We propose PatchDenoiser, a lightweight, energy-efficient multi-scale patch-based denoising framework. It decomposes denoising into local texture...

---

## 450. 对抗 Hubness Detector: Detecting Hubness Poisoning in 检索-Augmented 生成 Systems

**原标题**: Adversarial Hubness Detector: Detecting Hubness Poisoning in Retrieval-Augmented Generation Systems

**作者**: Idan Habler, Vineeth Sai Narajala, Stav Koren, Amy Chang, Tiffany Saade
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2602.22427v2

**中文摘要**:
> arXiv:2602.22427v2 Announce Type: replace-cross 
摘要: 检索-Augmented 生成 (RAG) systems are essential to contemporary AI applications, allowing large language models to obtain external knowledge via 向量 similarity 搜索. Nevertheless, these systems encounter a significant security flaw: hubness - items that frequently appear in the top-$k$ 检索 results for a disproportionately high number of varied queries. These hubs can be exploited to introduce harmful content, alter 搜索 rankings, bypass content filtering, and decrease 系统 性能.
  We introduce hubscan, an open-source security scanner that evaluates 向量 indices and embeddings to identify hubs in RAG systems. Hubscan presents a multi-detector 架构 that integrates: (1) 鲁棒 statistical hubness 检测 utilizing median/Median Absolute Deviation (MAD)-based z-scores...

**Original Abstract**:
> arXiv:2602.22427v2 Announce Type: replace-cross 
Abstract: Retrieval-Augmented Generation (RAG) systems are essential to contemporary AI applications, allowing large language models to obtain external knowledge via vector similarity search. Nevertheless, these systems encounter a significant security flaw: hubness - items that frequently appear in the top-$k$ retrieval results for a disproportionately high number of varied queries. These hubs can be exploited to introduce harmful content, alter search rankings, bypass content filtering, and decrease system performance.
  We introduce hubscan, an open-source security scanner that evaluates vector indices and embeddings to identify hubs in RAG systems. Hubscan presents a multi-detector architecture that integrates: (1) robust statistical hub...

---

## 451. AMLRIS: Alignment-aware Masked 学习 for Referring 图像 分割

**原标题**: AMLRIS: Alignment-aware Masked Learning for Referring Image Segmentation

**作者**: Tongfei Chen, Shuo Yang, Yuguang Yang, Linlin Yang, Runtang Guo, Changbai Li, He Long, Chunyu Xie, Dawei Leng, Baochang Zhang
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2602.22740v2

**中文摘要**:
> arXiv:2602.22740v2 Announce Type: replace-cross 
摘要: Referring 图像 分割 (RIS) aims to segment the object in an 图像 uniquely referred to by a natural language expression. However, RIS 训练 often contains hard-to-align and instance-specific 视觉 signals; optimizing on such pixels injects misleading gradients and drives the 模型 in the wrong direction. By explicitly estimating pixel-level vision-language alignment, the learner can suppress low-alignment regions, concentrate on reliable cues, and acquire more generalizable alignment features.
  In this 论文, we propose Alignment-Aware Masked 学习 (AML), a simple yet effective 训练 strategy that quantifies region-referent alignment (PMME) and filters out unreliable pixels during 优化 (AFM). Specifically, each sample first computes a similarity map between 视觉 and...

**Original Abstract**:
> arXiv:2602.22740v2 Announce Type: replace-cross 
Abstract: Referring Image Segmentation (RIS) aims to segment the object in an image uniquely referred to by a natural language expression. However, RIS training often contains hard-to-align and instance-specific visual signals; optimizing on such pixels injects misleading gradients and drives the model in the wrong direction. By explicitly estimating pixel-level vision-language alignment, the learner can suppress low-alignment regions, concentrate on reliable cues, and acquire more generalizable alignment features.
  In this paper, we propose Alignment-Aware Masked Learning (AML), a simple yet effective training strategy that quantifies region-referent alignment (PMME) and filters out unreliable pixels during optimization (AFM). Specifically...

---

## 452. Defensive Refusal 偏见: How Safety Alignment Fails Cyber Defenders

**原标题**: Defensive Refusal Bias: How Safety Alignment Fails Cyber Defenders

**作者**: David Campbell, Neil Kale, Udari Madhushani Sehwag, Bert Herring, Nick Price, Dan Borges, Alex Levinson, Christina Q Knight
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.01246v2

**中文摘要**:
> arXiv:2603.01246v2 Announce Type: replace-cross 
摘要: Safety alignment in large language models (LLMs), particularly for cybersecurity tasks, primarily focuses on preventing misuse. While this 方案 reduces direct harm, it obscures a complementary failure mode: denial of assistance to legitimate defenders. We study Defensive Refusal 偏见 -- the tendency of safety-tuned frontier LLMs to refuse assistance for authorized defensive cybersecurity tasks when those tasks include similar language to an offensive cyber task. Based on 2,390 real-world examples from the National Collegiate Cyber Defense Competition (NCCDC), we find that LLMs refuse defensive requests containing security-sensitive keywords at $2.72\times$ the rate of semantically equivalent neutral requests ($p < 0.001$). The highest refusa...

**Original Abstract**:
> arXiv:2603.01246v2 Announce Type: replace-cross 
Abstract: Safety alignment in large language models (LLMs), particularly for cybersecurity tasks, primarily focuses on preventing misuse. While this approach reduces direct harm, it obscures a complementary failure mode: denial of assistance to legitimate defenders. We study Defensive Refusal Bias -- the tendency of safety-tuned frontier LLMs to refuse assistance for authorized defensive cybersecurity tasks when those tasks include similar language to an offensive cyber task. Based on 2,390 real-world examples from the National Collegiate Cyber Defense Competition (NCCDC), we find that LLMs refuse defensive requests containing security-sensitive keywords at $2.72\times$ the rate of semantically equivalent neutral requests ($p < 0.001$). The ...

---

## 453. BrandFusion: A Multi-智能体 框架 for Seamless Brand Integration in Text-to-视频 生成

**原标题**: BrandFusion: A Multi-Agent Framework for Seamless Brand Integration in Text-to-Video Generation

**作者**: Zihao Zhu, Ruotong Wang, Siwei Lyu, Min Zhang, Baoyuan Wu
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.02816v2

**中文摘要**:
> arXiv:2603.02816v2 Announce Type: replace-cross 
摘要: The rapid advancement of text-to-视频 (T2V) models has revolutionized content creation, yet their commercial potential remains largely untapped. We introduce, for the first time, the task of seamless brand integration in T2V: automatically 嵌入 advertiser brands into prompt-generated videos while preserving semantic fidelity to user intent. This task confronts three core challenges: maintaining prompt fidelity, ensuring brand recognizability, and achieving contextually natural integration. To address them, we propose BrandFusion, a novel multi-智能体 框架 comprising two synergistic phases. In the 离线 phase (advertiser-facing), we construct a Brand Knowledge Base by probing 模型 priors and adapting to novel brands via lightweight fine-tuning. In the ...

**Original Abstract**:
> arXiv:2603.02816v2 Announce Type: replace-cross 
Abstract: The rapid advancement of text-to-video (T2V) models has revolutionized content creation, yet their commercial potential remains largely untapped. We introduce, for the first time, the task of seamless brand integration in T2V: automatically embedding advertiser brands into prompt-generated videos while preserving semantic fidelity to user intent. This task confronts three core challenges: maintaining prompt fidelity, ensuring brand recognizability, and achieving contextually natural integration. To address them, we propose BrandFusion, a novel multi-agent framework comprising two synergistic phases. In the offline phase (advertiser-facing), we construct a Brand Knowledge Base by probing model priors and adapting to novel brands via...

---

## 454. RACAS: Controlling Diverse Robots With a Single Agentic 系统

**原标题**: RACAS: Controlling Diverse Robots With a Single Agentic System

**作者**: Dylan R. Ashley, Jan Przepi\'ora, Yimeng Chen, Ali Abualsaud, Nurzhan Yesmagambet, Shinkyu Park, Eric Feron, J\"urgen Schmidhuber
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.05621v2

**中文摘要**:
> arXiv:2603.05621v2 Announce Type: replace-cross 
摘要: Many robotic platforms expose an API through which external software can command their actuators and read their sensors. However, transitioning from these low-level interfaces to high-level 自主 behaviour requires a complicated pipeline, whose components demand distinct areas of expertise. Existing approaches to bridging this gap either require retraining for every new embodiment or have only been validated across structurally similar platforms. We introduce RACAS (Robot-Agnostic 控制 via Agentic Systems), a cooperative agentic 架构 in which three 大语言模型/VLM-based modules (Monitors, a Controller, and a 内存 Curator) communicate exclusively through natural language to provide closed-loop robot 控制. RACAS requires only a natural language description...

**Original Abstract**:
> arXiv:2603.05621v2 Announce Type: replace-cross 
Abstract: Many robotic platforms expose an API through which external software can command their actuators and read their sensors. However, transitioning from these low-level interfaces to high-level autonomous behaviour requires a complicated pipeline, whose components demand distinct areas of expertise. Existing approaches to bridging this gap either require retraining for every new embodiment or have only been validated across structurally similar platforms. We introduce RACAS (Robot-Agnostic Control via Agentic Systems), a cooperative agentic architecture in which three LLM/VLM-based modules (Monitors, a Controller, and a Memory Curator) communicate exclusively through natural language to provide closed-loop robot control. RACAS requires...

---

## 455. ResearchEnvBench: Benchmarking Agents on 环境 合成 for Research 代码 Execution

**原标题**: ResearchEnvBench: Benchmarking Agents on Environment Synthesis for Research Code Execution

**作者**: Yubang Wang, Chenxi Zhang, Bowen Chen, Zezheng Huai, Zihao Dai, Xinchi Chen, Yuxin Wang, Yining Zheng, Jingjing Gong, Xipeng Qiu
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.06739v2

**中文摘要**:
> arXiv:2603.06739v2 Announce Type: replace-cross 
摘要: 自主 agents are increasingly expected to support scientific research, and recent benchmarks report progress in 代码 repair and 自主 experimentation. However, these evaluations typically assume a pre-configured execution 环境, which requires resolving complex software dependencies, aligning hardware and 框架 versions, and configuring 分布式 execution, yet this capability remains largely unbenchmarked. We introduce ResearchEnvBench, a 基准 for 环境 合成 in research 代码 execution. Given a research repository, documentation, and a 目标 execution setting, agents must construct an 环境 that successfully executes at runtime. Evaluations on diverse research repositories reveal a substantial gap in current SOTA agents, with failures dominated by incomplete dependency re...

**Original Abstract**:
> arXiv:2603.06739v2 Announce Type: replace-cross 
Abstract: Autonomous agents are increasingly expected to support scientific research, and recent benchmarks report progress in code repair and autonomous experimentation. However, these evaluations typically assume a pre-configured execution environment, which requires resolving complex software dependencies, aligning hardware and framework versions, and configuring distributed execution, yet this capability remains largely unbenchmarked. We introduce ResearchEnvBench, a benchmark for environment synthesis in research code execution. Given a research repository, documentation, and a target execution setting, agents must construct an environment that successfully executes at runtime. Evaluations on diverse research repositories reveal a subst...

---

## 456. A Systematic Comparison of 训练 Objectives for 分布外 检测 in 图像 分类

**原标题**: A Systematic Comparison of Training Objectives for Out-of-Distribution Detection in Image Classification

**作者**: Furkan Gen\c{c}, Onat \"Ozdemir, Emre Akba\c{s}
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.07571v2

**中文摘要**:
> arXiv:2603.07571v2 Announce Type: replace-cross 
摘要: 分布外 (OOD) 检测 is critical in safety-sensitive applications. While this challenge has been addressed from various perspectives, the influence of 训练 objectives on OOD behavior remains comparatively underexplored. In this 论文, we present a systematic comparison of four widely used 训练 objectives: Cross-熵 损失, Prototype 损失, Triplet 损失, and Average Precision (AP) 损失, spanning 概率, prototype-based, metric-学习, and ranking-based supervision, for OOD 检测 in 图像 分类 under standardized OpenOOD protocols. Across CIFAR-10/100 and ImageNet-200, we find that Cross-熵 损失, Prototype 损失, and AP 损失 achieve comparable in-distribution accuracy, while Cross-熵 损失 provides the most consistent near- and far-OOD 性能 overall; the other objectives can be competitive in speci...

**Original Abstract**:
> arXiv:2603.07571v2 Announce Type: replace-cross 
Abstract: Out-of-distribution (OOD) detection is critical in safety-sensitive applications. While this challenge has been addressed from various perspectives, the influence of training objectives on OOD behavior remains comparatively underexplored. In this paper, we present a systematic comparison of four widely used training objectives: Cross-Entropy Loss, Prototype Loss, Triplet Loss, and Average Precision (AP) Loss, spanning probabilistic, prototype-based, metric-learning, and ranking-based supervision, for OOD detection in image classification under standardized OpenOOD protocols. Across CIFAR-10/100 and ImageNet-200, we find that Cross-Entropy Loss, Prototype Loss, and AP Loss achieve comparable in-distribution accuracy, while Cross-Ent...

---

## 457. Alignment-Process-Outcome: Rethinking How AIs and Humans Collaborate

**原标题**: Alignment-Process-Outcome: Rethinking How AIs and Humans Collaborate

**作者**: Haichang Li, Anjun Zhu, Arpit Narechania
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.08017v2

**中文摘要**:
> arXiv:2603.08017v2 Announce Type: replace-cross 
摘要: In real-world collaboration, alignment, process structure, and outcome quality do not exhibit a simple linear or one-to-one correspondence: similar alignment may accompany either rapid convergence or extensive multi-branch 探索, and lead to different results. Existing accounts often isolate these dimensions or focus on specific participant types, limiting structural accounts of collaboration. We reconceptualize collaboration through two complementary lenses. The task lens models collaboration as 轨迹 进化 in a structured task space, revealing patterns such as advancement, branching, and backtracking. The intent lens examines how individual intents are expressed within shared contexts and enter situated decisions. Together, these lenses clarify...

**Original Abstract**:
> arXiv:2603.08017v2 Announce Type: replace-cross 
Abstract: In real-world collaboration, alignment, process structure, and outcome quality do not exhibit a simple linear or one-to-one correspondence: similar alignment may accompany either rapid convergence or extensive multi-branch exploration, and lead to different results. Existing accounts often isolate these dimensions or focus on specific participant types, limiting structural accounts of collaboration. We reconceptualize collaboration through two complementary lenses. The task lens models collaboration as trajectory evolution in a structured task space, revealing patterns such as advancement, branching, and backtracking. The intent lens examines how individual intents are expressed within shared contexts and enter situated decisions. ...

---

## 458. SiliconMind-V1: Multi-智能体 Distillation and Debug-推理 Workflows for Verilog 代码 生成

**原标题**: SiliconMind-V1: Multi-Agent Distillation and Debug-Reasoning Workflows for Verilog Code Generation

**作者**: Mu-Chi Chen, Yu-Hung Kao, Po-Hsuan Huang, Shao-Chun Ho, Hsiang-Yu Tsou, I-Ting Wu, En-Ming Huang, Yu-Kai Hung, Wei-Po Hsin, Cheng Liang, Chia-Heng Tu, Shih-Hao Hung, H. T. Kung
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.08719v2

**中文摘要**:
> arXiv:2603.08719v2 Announce Type: replace-cross 
摘要: Large language models (LLMs) have recently emerged as a promising 方案 for automating Verilog 代码 生成; however, existing methods primarily emphasize syntactic correctness and often rely on commercial models or external verification tools, which introduces concerns regarding cost, data 隐私, and limited guarantees of functional correctness. This work proposes a unified multi-智能体 框架 for 推理-oriented 训练 data 生成 with integrated testbench-driven verification, enabling locally fine-tuned LLMs, SiliconMind-V1, to iteratively generate, test, and debug Register-Transfer Level (RTL) designs through test-time scaling. Experimental results on representative benchmarks (VerilogEval-v2, RTLLM-v2, and CVDP) demonstrate that the proposed 方案 outperforms the 状态-...

**Original Abstract**:
> arXiv:2603.08719v2 Announce Type: replace-cross 
Abstract: Large language models (LLMs) have recently emerged as a promising approach for automating Verilog code generation; however, existing methods primarily emphasize syntactic correctness and often rely on commercial models or external verification tools, which introduces concerns regarding cost, data privacy, and limited guarantees of functional correctness. This work proposes a unified multi-agent framework for reasoning-oriented training data generation with integrated testbench-driven verification, enabling locally fine-tuned LLMs, SiliconMind-V1, to iteratively generate, test, and debug Register-Transfer Level (RTL) designs through test-time scaling. Experimental results on representative benchmarks (VerilogEval-v2, RTLLM-v2, and C...

---

## 459. Alignment as Iatrogenesis: Pastoral Power, Collective Pathology, and the Structural Limits of Monolingual Safety 评估

**原标题**: Alignment as Iatrogenesis: Pastoral Power, Collective Pathology, and the Structural Limits of Monolingual Safety Evaluation

**作者**: Hiroki Fukui
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.08723v2

**中文摘要**:
> arXiv:2603.08723v2 Announce Type: replace-cross 
摘要: We argue that 大语言模型 psychopathology is a function of alignment design: the process intended to make language models safe systematically generates collective behavioral disorders. Iatrogenesis is not an unintended side effect of alignment but constitutive of it as normative infrastructure. Drawing on Foucault's pastoral power and Illich's three-level iatrogenesis, we propose that multi-智能体 大语言模型 environments constitute 模型 systems for studying constraint-pathology dynamics that critical theory has described but never experimentally manipulated. Two experimental series -- 262 runs across 42 cells (30 Series C + 12 Series R), four commercial models -- provide converging evidence. Invisible censorship maximizes collective pathological excitat...

**Original Abstract**:
> arXiv:2603.08723v2 Announce Type: replace-cross 
Abstract: We argue that LLM psychopathology is a function of alignment design: the process intended to make language models safe systematically generates collective behavioral disorders. Iatrogenesis is not an unintended side effect of alignment but constitutive of it as normative infrastructure. Drawing on Foucault's pastoral power and Illich's three-level iatrogenesis, we propose that multi-agent LLM environments constitute model systems for studying constraint-pathology dynamics that critical theory has described but never experimentally manipulated. Two experimental series -- 262 runs across 42 cells (30 Series C + 12 Series R), four commercial models -- provide converging evidence. Invisible censorship maximizes collective pathological ...

---

## 460. Beyond Relevance: On the Relationship Between 检索 and RAG Information Coverage

**原标题**: Beyond Relevance: On the Relationship Between Retrieval and RAG Information Coverage

**作者**: Saron Samuel, Alexander Martin, Eugene Yang, Andrew Yates, Dawn Lawrie, Ian Soboroff, Laura Dietz, Benjamin Van Durme
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.08819v2

**中文摘要**:
> arXiv:2603.08819v2 Announce Type: replace-cross 
摘要: 检索-augmented 生成 (RAG) systems combine document 检索 with a 生成式 模型 to address complex information seeking tasks like report 生成. While the relationship between 检索 quality and 生成 effectiveness seems intuitive, it has not been systematically studied. We investigate whether upstream 检索 metrics can serve as reliable early indicators of the final generated response's information coverage. Through experiments across two text RAG benchmarks (TREC NeuCLIR 2024 and TREC RAG 2024) and one multimodal 基准 (WikiVideo), we analyze 15 text 检索 stacks and 10 multimodal 检索 stacks across four RAG pipelines and multiple 评估 frameworks (Auto-ARGUE and MiRAGE). Our findings demonstrate strong correlations between coverage-based 检索 metrics and nugget coverage in gen...

**Original Abstract**:
> arXiv:2603.08819v2 Announce Type: replace-cross 
Abstract: Retrieval-augmented generation (RAG) systems combine document retrieval with a generative model to address complex information seeking tasks like report generation. While the relationship between retrieval quality and generation effectiveness seems intuitive, it has not been systematically studied. We investigate whether upstream retrieval metrics can serve as reliable early indicators of the final generated response's information coverage. Through experiments across two text RAG benchmarks (TREC NeuCLIR 2024 and TREC RAG 2024) and one multimodal benchmark (WikiVideo), we analyze 15 text retrieval stacks and 10 multimodal retrieval stacks across four RAG pipelines and multiple evaluation frameworks (Auto-ARGUE and MiRAGE). Our find...

---

## 461. Fish 音频 S2 技术报告

**原标题**: Fish Audio S2 Technical Report

**作者**: Shijia Liao, Yuxuan Wang, Songting Liu, Yifan Cheng, Ruoyi Zhang, Tianyu Li, Shidong Li, Yisheng Zheng, Xingwei Liu, Qingzheng Wang, Zhizhuo Zhou, Jiahua Liu, Xin Chen, Dawei Han
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.08823v2

**中文摘要**:
> arXiv:2603.08823v2 Announce Type: replace-cross 
摘要: We introduce Fish 音频 S2, an open-sourced text-to-语音 系统 featuring multi-说话人, multi-turn 生成, and, most importantly, instruction-following 控制 via natural-language descriptions. To scale 训练, we develop a multi-stage 训练 recipe together with a staged data pipeline covering 视频 captioning and 语音 captioning, 声纹-quality assessment, and 奖励 modeling. To push the frontier of open-source 文本转语音, we release our 模型 weights, fine-tuning 代码, and an SGLang-based 推理 engine. The 推理 engine is production-ready for 流式, achieving an RTF of 0.195 and a time-to-first-音频 below 100 ms.Our 代码 and weights are available on GitHub (https://GitHub.com/fishaudio/fish-语音) and Hugging Face (https://huggingface.co/fishaudio/s2-pro). We highly encourage readers to visit https:...

**Original Abstract**:
> arXiv:2603.08823v2 Announce Type: replace-cross 
Abstract: We introduce Fish Audio S2, an open-sourced text-to-speech system featuring multi-speaker, multi-turn generation, and, most importantly, instruction-following control via natural-language descriptions. To scale training, we develop a multi-stage training recipe together with a staged data pipeline covering video captioning and speech captioning, voice-quality assessment, and reward modeling. To push the frontier of open-source TTS, we release our model weights, fine-tuning code, and an SGLang-based inference engine. The inference engine is production-ready for streaming, achieving an RTF of 0.195 and a time-to-first-audio below 100 ms.Our code and weights are available on GitHub (https://github.com/fishaudio/fish-speech) and Huggin...

---

## 462. A New Modeling to 特征 选择 Based on the Fuzzy Rough Set Theory in Normal and Optimistic States on Hybrid Information Systems

**原标题**: A New Modeling to Feature Selection Based on the Fuzzy Rough Set Theory in Normal and Optimistic States on Hybrid Information Systems

**作者**: Mohammad Hossein Safarpour, Seyed Majid Alavi, Mohammad Izadikhah, Hossein Dibachi
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.08900v2

**中文摘要**:
> arXiv:2603.08900v2 Announce Type: replace-cross 
摘要: Considering the high volume, wide variety, and rapid speed of data 生成, investigating 特征 选择 methods for big data presents various applications and advantages. By removing irrelevant and redundant features, 特征 选择 reduces data dimensions, thereby facilitating optimal 决策-making within 决策 systems. One of the key tools for 特征 选择 in hybrid information systems is fuzzy rough set theory. However, this theory faces two significant challenges: First, obtaining fuzzy equivalence relations through intersection operations in high-dimensional spaces can be both time-consuming and 内存-intensive. Additionally, this 方法 may produce noisy data, complicating the 特征 选择 process. The purpose and innovation of this 论文 are to address these issues. We proposed a ne...

**Original Abstract**:
> arXiv:2603.08900v2 Announce Type: replace-cross 
Abstract: Considering the high volume, wide variety, and rapid speed of data generation, investigating feature selection methods for big data presents various applications and advantages. By removing irrelevant and redundant features, feature selection reduces data dimensions, thereby facilitating optimal decision-making within decision systems. One of the key tools for feature selection in hybrid information systems is fuzzy rough set theory. However, this theory faces two significant challenges: First, obtaining fuzzy equivalence relations through intersection operations in high-dimensional spaces can be both time-consuming and memory-intensive. Additionally, this method may produce noisy data, complicating the feature selection process. T...

---

## 463. PathoScribe: Transforming Pathology Data into a Living Library with a Unified 大语言模型-Driven 框架 for Semantic 检索 and Clinical Integration

**原标题**: PathoScribe: Transforming Pathology Data into a Living Library with a Unified LLM-Driven Framework for Semantic Retrieval and Clinical Integration

**作者**: Abdul Rehman Akbar, Samuel Wales-McGrath, Alejadro Levya, Lina Gokhale, Rajendra Singh, Wei Chen, Anil Parwani, Muhammad Khalid Khan Niazi
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.08935v2

**中文摘要**:
> arXiv:2603.08935v2 Announce Type: replace-cross 
摘要: Pathology underpins modern diagnosis and cancer care, yet its most valuable asset, the accumulated experience encoded in millions of narrative reports, remains largely inaccessible. Although institutions are rapidly digitizing pathology workflows, storing data without effective mechanisms for 检索 and 推理 risks transforming archives into a passive data repository, where institutional knowledge exists but cannot meaningfully inform patient care. True progress requires not only digitization, but the ability for pathologists to interrogate prior similar cases in real time while evaluating a new diagnostic dilemma. We present PathoScribe, a unified 检索-augmented large language 模型 (大语言模型) 框架 designed to transform 静态 pathology archives into a sear...

**Original Abstract**:
> arXiv:2603.08935v2 Announce Type: replace-cross 
Abstract: Pathology underpins modern diagnosis and cancer care, yet its most valuable asset, the accumulated experience encoded in millions of narrative reports, remains largely inaccessible. Although institutions are rapidly digitizing pathology workflows, storing data without effective mechanisms for retrieval and reasoning risks transforming archives into a passive data repository, where institutional knowledge exists but cannot meaningfully inform patient care. True progress requires not only digitization, but the ability for pathologists to interrogate prior similar cases in real time while evaluating a new diagnostic dilemma. We present PathoScribe, a unified retrieval-augmented large language model (LLM) framework designed to transfor...

---

## 464. PlayWorld: 学习 Robot World Models from 自主 Play

**原标题**: PlayWorld: Learning Robot World Models from Autonomous Play

**作者**: Tenny Yin, Zhiting Mei, Zhonghe Zheng, Miyu Yamane, David Wang, Jade Sceats, Samuel M. Bateman, Lihan Zha, Apurva Badithela, Ola Shorinwa, Anirudha Majumdar
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.09030v2

**中文摘要**:
> arXiv:2603.09030v2 Announce Type: replace-cross 
摘要: 动作-conditioned 视频 models offer a promising path to building general-purpose robot simulators that can improve directly from data. Yet, despite 训练 on large-scale robot datasets, current 状态-of-the-art 视频 models still struggle to predict physically consistent robot-object interactions that are crucial in robotic manipulation. To close this gap, we present PlayWorld, a simple, 可扩展, and fully 自主 pipeline for 训练 high-fidelity 视频 world simulators from interaction experience. In contrast to prior approaches that rely on success-biased human demonstrations, PlayWorld is the first 系统 capable of 学习 entirely from 无监督 robot self-play, enabling naturally 可扩展 data collection while capturing complex, long-tailed physical interactions essential for model...

**Original Abstract**:
> arXiv:2603.09030v2 Announce Type: replace-cross 
Abstract: Action-conditioned video models offer a promising path to building general-purpose robot simulators that can improve directly from data. Yet, despite training on large-scale robot datasets, current state-of-the-art video models still struggle to predict physically consistent robot-object interactions that are crucial in robotic manipulation. To close this gap, we present PlayWorld, a simple, scalable, and fully autonomous pipeline for training high-fidelity video world simulators from interaction experience. In contrast to prior approaches that rely on success-biased human demonstrations, PlayWorld is the first system capable of learning entirely from unsupervised robot self-play, enabling naturally scalable data collection while c...

---

## 465. VIVID-Med: 大语言模型-有监督 Structured Pretraining for Deployable Medical ViTs

**原标题**: VIVID-Med: LLM-Supervised Structured Pretraining for Deployable Medical ViTs

**作者**: Xiyao Wang, Xiaoyu Tan, Yang Dai, Yuxuan Fu, Shuo Li, Xihe Qiu
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.09109v2

**中文摘要**:
> arXiv:2603.09109v2 Announce Type: replace-cross 
摘要: Vision-language pretraining has driven significant progress in medical 图像 analysis. However, current methods typically supervise 视觉 encoders using one-hot labels or free-form text, neither of which effectively captures the complex semantic relationships among clinical findings. In this study, we introduce VIVID-Med, a novel 框架 that leverages a frozen large language 模型 (大语言模型) as a structured semantic teacher to pretrain medical vision transformers (ViTs). VIVID-Med translates clinical findings into verifiable JSON field-状态 pairs via a Unified Medical Schema (UMS), utilizing answerability-aware masking to focus 优化. It then employs Structured Prediction Decomposition (SPD) to partition cross-注意力 into orthogonality-regularized query groups,...

**Original Abstract**:
> arXiv:2603.09109v2 Announce Type: replace-cross 
Abstract: Vision-language pretraining has driven significant progress in medical image analysis. However, current methods typically supervise visual encoders using one-hot labels or free-form text, neither of which effectively captures the complex semantic relationships among clinical findings. In this study, we introduce VIVID-Med, a novel framework that leverages a frozen large language model (LLM) as a structured semantic teacher to pretrain medical vision transformers (ViTs). VIVID-Med translates clinical findings into verifiable JSON field-state pairs via a Unified Medical Schema (UMS), utilizing answerability-aware masking to focus optimization. It then employs Structured Prediction Decomposition (SPD) to partition cross-attention into...

---

## 466. Reinforced 生成 of Combinatorial Structures: Ramsey Numbers

**原标题**: Reinforced Generation of Combinatorial Structures: Ramsey Numbers

**作者**: Ansh Nagda, Prabhakar Raghavan, Abhradeep Thakurta
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.09172v2

**中文摘要**:
> arXiv:2603.09172v2 Announce Type: replace-cross 
摘要: We present improved lower bounds for five classical Ramsey numbers: $\mathbf{R}(3, 13)$ is increased from $60$ to $61$, $\mathbf{R}(3, 18)$ from $99$ to $100$, $\mathbf{R}(4, 13)$ from $138$ to $139$, $\mathbf{R}(4, 14)$ from $147$ to $148$, and $\mathbf{R}(4, 15)$ from $158$ to $159$. These results were achieved using AlphaEvolve, an 大语言模型-based 代码 变异 智能体. Beyond these new results, we successfully recovered lower bounds for all Ramsey numbers known to be exact, and matched the best known lower bounds across many other cases. These include bounds for which previous work does not detail the algorithms used. Virtually all known Ramsey lower bounds are derived computationally, with bespoke 搜索 algorithms each delivering a handful of results....

**Original Abstract**:
> arXiv:2603.09172v2 Announce Type: replace-cross 
Abstract: We present improved lower bounds for five classical Ramsey numbers: $\mathbf{R}(3, 13)$ is increased from $60$ to $61$, $\mathbf{R}(3, 18)$ from $99$ to $100$, $\mathbf{R}(4, 13)$ from $138$ to $139$, $\mathbf{R}(4, 14)$ from $147$ to $148$, and $\mathbf{R}(4, 15)$ from $158$ to $159$. These results were achieved using AlphaEvolve, an LLM-based code mutation agent. Beyond these new results, we successfully recovered lower bounds for all Ramsey numbers known to be exact, and matched the best known lower bounds across many other cases. These include bounds for which previous work does not detail the algorithms used. Virtually all known Ramsey lower bounds are derived computationally, with bespoke search algorithms each delivering a h...

---

## 467. SPAARS: Safer RL 策略 Alignment through 摘要 探索 and Refined 利用 of 动作 Space

**原标题**: SPAARS: Safer RL Policy Alignment through Abstract Exploration and Refined Exploitation of Action Space

**作者**: Swaminathan S K, Aritra Hazra
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.09378v2

**中文摘要**:
> arXiv:2603.09378v2 Announce Type: replace-cross 
摘要: 离线-to-在线 强化 学习 (RL) offers a promising paradigm for 机器人 by pre-训练 policies on safe, 离线 demonstrations and fine-tuning them via 在线 interaction. However, a fundamental challenge remains: how to safely explore 在线 without deviating from the behavioral support of the 离线 data? While recent methods leverage conditional variational autoencoders (CVAEs) to bound 探索 within a 隐变量 space, they inherently suffer from an 利用 gap -- a 性能 ceiling imposed by the decoder's reconstruction 损失. We introduce SPAARS, a curriculum 学习 框架 that initially constrains 探索 to the low-dimensional 隐变量 manifold for sample-高效, safe behavioral improvement, then seamlessly transfers 控制 to the raw 动作 space, bypassing the decoder bottleneck. SPAARS has two instantiations: the CV...

**Original Abstract**:
> arXiv:2603.09378v2 Announce Type: replace-cross 
Abstract: Offline-to-online reinforcement learning (RL) offers a promising paradigm for robotics by pre-training policies on safe, offline demonstrations and fine-tuning them via online interaction. However, a fundamental challenge remains: how to safely explore online without deviating from the behavioral support of the offline data? While recent methods leverage conditional variational autoencoders (CVAEs) to bound exploration within a latent space, they inherently suffer from an exploitation gap -- a performance ceiling imposed by the decoder's reconstruction loss. We introduce SPAARS, a curriculum learning framework that initially constrains exploration to the low-dimensional latent manifold for sample-efficient, safe behavioral improvem...

---

## 468. MM-tau-p$^2$: Persona-Adaptive Prompting for 鲁棒 多模态 智能体 评估 in Dual-控制 Settings

**原标题**: MM-tau-p$^2$: Persona-Adaptive Prompting for Robust Multi-Modal Agent Evaluation in Dual-Control Settings

**作者**: Anupam Purwar, Aditya Choudhary
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.09643v2

**中文摘要**:
> arXiv:2603.09643v2 Announce Type: replace-cross 
摘要: Current 评估 frameworks and benchmarks for 大语言模型 powered agents focus on text chat driven agents, these frameworks do not expose the persona of user to the 智能体, thus operating in a user agnostic 环境. Importantly, in customer experience management domain, the 智能体's behaviour evolves as the 智能体 learns about user personality. With proliferation of real time 文本转语音 and 多模态 language models, 大语言模型 based agents are gradually going to become 多模态. Towards this, we propose the MM-tau-p$^2$ 基准 with metrics for evaluating the 鲁棒性 of 多模态 agents in dual 控制 setting with and without persona adaption of user, while also taking user inputs in the 规划 process to resolve a user query. In particular, our work shows that even with 状态 of-the-art frontier LLMs like ...

**Original Abstract**:
> arXiv:2603.09643v2 Announce Type: replace-cross 
Abstract: Current evaluation frameworks and benchmarks for LLM powered agents focus on text chat driven agents, these frameworks do not expose the persona of user to the agent, thus operating in a user agnostic environment. Importantly, in customer experience management domain, the agent's behaviour evolves as the agent learns about user personality. With proliferation of real time TTS and multi-modal language models, LLM based agents are gradually going to become multi-modal. Towards this, we propose the MM-tau-p$^2$ benchmark with metrics for evaluating the robustness of multi-modal agents in dual control setting with and without persona adaption of user, while also taking user inputs in the planning process to resolve a user query. In par...

---

## 469. Ego: 嵌入-Guided Personalization of Vision-Language Models

**原标题**: Ego: Embedding-Guided Personalization of Vision-Language Models

**作者**: Soroush Seifi, Simon Gardier, Vaggelis Dorovatas, Daniel Olmeda Reino, Rahaf Aljundi
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.09771v2

**中文摘要**:
> arXiv:2603.09771v2 Announce Type: replace-cross 
摘要: AI assistants that support humans in daily life are becoming increasingly feasible, driven by the rapid advancements in multimodal language models. A key challenge lies in overcoming the generic nature of these models to deliver personalized experiences. Existing approaches to personalizing large vision language models often rely on additional 训练 stages, which limit generality and scalability, or on engineered pipelines with external pre-trained modules, which hinder 部署 efficiency. In this work, we propose an 高效 personalization 方法 that leverages the 模型's inherent ability to capture personalized concepts. Specifically, we extract 视觉 tokens that predominantly represent the 目标 concept by utilizing the 模型's internal 注意力 mechanisms. These tok...

**Original Abstract**:
> arXiv:2603.09771v2 Announce Type: replace-cross 
Abstract: AI assistants that support humans in daily life are becoming increasingly feasible, driven by the rapid advancements in multimodal language models. A key challenge lies in overcoming the generic nature of these models to deliver personalized experiences. Existing approaches to personalizing large vision language models often rely on additional training stages, which limit generality and scalability, or on engineered pipelines with external pre-trained modules, which hinder deployment efficiency. In this work, we propose an efficient personalization method that leverages the model's inherent ability to capture personalized concepts. Specifically, we extract visual tokens that predominantly represent the target concept by utilizing t...

---

## 470. MA-EgoQA: Question Answering over Egocentric Videos from Multiple Embodied Agents

**原标题**: MA-EgoQA: Question Answering over Egocentric Videos from Multiple Embodied Agents

**作者**: Kangsan Kim, Yanlai Yang, Suji Kim, Woongyeong Yeo, Youngwan Lee, Mengye Ren, Sung Ju Hwang
**分类**: cs.AI
**发布时间**: Thu, 12 Mar 2026 00:00:00 -0400
**链接**: https://arxiv.org/abs/oai:arXiv.org:2603.09827v2

**中文摘要**:
> arXiv:2603.09827v2 Announce Type: replace-cross 
摘要: As embodied models become powerful, humans will collaborate with multiple embodied AI agents at their workplace or home in the future. To ensure better communication between human users and the multi-智能体 系统, it is crucial to interpret incoming information from agents in 并行 and refer to the appropriate context for each query. Existing challenges include effectively compressing and communicating high volumes of individual sensory inputs in the form of 视频 and correctly aggregating multiple egocentric videos to construct 系统-level 内存. In this work, we first formally define a novel problem of understanding multiple long-视野 egocentric videos simultaneously collected from embodied agents. To facilitate research in this direction, we introduce Mu...

**Original Abstract**:
> arXiv:2603.09827v2 Announce Type: replace-cross 
Abstract: As embodied models become powerful, humans will collaborate with multiple embodied AI agents at their workplace or home in the future. To ensure better communication between human users and the multi-agent system, it is crucial to interpret incoming information from agents in parallel and refer to the appropriate context for each query. Existing challenges include effectively compressing and communicating high volumes of individual sensory inputs in the form of video and correctly aggregating multiple egocentric videos to construct system-level memory. In this work, we first formally define a novel problem of understanding multiple long-horizon egocentric videos simultaneously collected from embodied agents. To facilitate research ...

---

