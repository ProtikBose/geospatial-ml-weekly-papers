# Weekly Geospatial ML Papers

**Search window:** 2026-05-18 to 2026-05-25

**Sources:** arXiv and Semantic Scholar

**Total selected papers:** 10

This digest focuses on geospatial analysis, urban climate, urban planning, infrastructure, and geospatial problem-solving using ML, computer vision, LLMs, VLMs, foundation models, self-supervised learning, and related methods.

Only papers from the selected top journals, conferences, or workshops are included by default. The venue importance score is included in **My Score**.

## Top Papers

### 1. Recursive Block-Diagonal Coupling for Resource-Efficient Training of Vision Models

**Authors:** Maxim Henry, Adrien Deliège, Sébastien Piérard, Marc Van Droogenbroeck

**Published:** 2026-05-22

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 33

**Venue importance score included:** 0

**arXiv ID:** 2605.23656v1

**Paper link:** http://arxiv.org/abs/2605.23656v1

**PDF link:** https://arxiv.org/pdf/2605.23656v1

**Abstract:**

Training high-capacity vision models from scratch requires substantial computational resources. To improve training efficiency of a wide target model, existing growth methods often assume the availability of narrower models, obscuring the true computational cost of the entire pipeline. We propose an efficient training protocol, RBDC, that builds wide models by coupling in a parameter-free block-diagonal way narrower, independently trained models in a recursive way. This allows a flexible allocation of the training budget available across all the models involved. Evaluated with vision transformers (DeiT) and convolutional networks (ResNet) on ImageNet, our RBDC training protocol shows a much better efficiency than models trained from scratch with the standard protocol, yielding 30% FLOPs reduction at similar test accuracies. It also achieves higher performances at same training FLOPs than training protocols from the model growth literature. Finally, we show that our models can serve as better backbones than their original counterparts for downstream object detection and instance segmentation tasks.

**Why this may be relevant:**

It matched the geospatial machine learning search criteria and may be worth screening.

---

### 2. RS2AD-LiDAR: End-to-End Autonomous Driving LiDAR Data Generation from Roadside Sensor Observations

**Authors:** Runyi Huang, Ni Ding, Ruidan Xing, Yuheng Shi, Lei He, Keqiang Li

**Published:** 2026-05-22

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 30

**Venue importance score included:** 0

**arXiv ID:** 2605.23406v1

**Paper link:** http://arxiv.org/abs/2605.23406v1

**PDF link:** https://arxiv.org/pdf/2605.23406v1

**Abstract:**

End-to-end autonomous driving solutions, which directly process multimodal sensory data and output fine-grained control commands, have gradually become a mainstream direction with the development of autonomous driving technology. However, current methods in this category rely on single-vehicle data collection for model training and optimization, which suffers from high acquisition and annotation costs, scarcity of valuable scenarios, and data silos. To address these challenges, we propose RS2AD-LiDAR, a novel framework for reconstructing and generating vehicle-mounted LiDAR data from roadside sensor observations. Since no public dataset currently provides highly overlapping perception coverage between roadside and vehicle-mounted LiDAR sensors, which is essential for studying roadside-to-vehicle data generation, we constructed a dedicated dataset named R2V-LiDAR which is used solely for evaluation in this work. Specifically, our method transforms roadside LiDAR point clouds into the vehicle-mounted LiDAR coordinate system, and synthesizes high-fidelity vehicle-mounted data via virtual LiDAR modeling and point cloud resampling techniques. To the best of our knowledge, this is the first approach to reconstruct vehicle-mounted LiDAR data from roadside sensor inputs. Extensive experimental comparisons demonstrate the semantic similarity between the generated data and real data. Furthermore, object detection experiments show that incorporating the generated data into real data for model training improves both Bird's Eye View (BEV) and 3D detection accuracy, thereby validating the effectiveness of the proposed method.

**Why this may be relevant:**

It may be useful for LiDAR-based tree inventory, urban structure mapping, or 3D geospatial analysis.

---

### 3. Vision Transformers Need Better Token Interaction

**Authors:** Linxiang Su

**Published:** 2026-05-22

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 28

**Venue importance score included:** 0

**arXiv ID:** 2605.23868v1

**Paper link:** http://arxiv.org/abs/2605.23868v1

**PDF link:** https://arxiv.org/pdf/2605.23868v1

**Abstract:**

Vision Transformers (ViTs) can learn strong image-level representations while their patch representations become less effective for dense prediction during prolonged training. We revisit this dense degradation phenomenon and argue that it is not fully explained by high-norm artifacts alone. Instead, we characterize \emph{semantic diffusion}: an optimization shortcut in which global semantic information spreads through patch tokens beyond what is locally justified. Our analysis shows that dense representation quality is not captured by locality alone: shallow features can remain better aligned with foreground regions yet underperform deeper features, and \texttt{[CLS]} features remain complementary for dense prediction. These observations suggest that the goal should not be to remove global context, but to make token interactions more selective. We therefore study sparse attention as a minimal intervention, replacing softmax attention with entmax-1.5 while preserving global token connectivity. On DINOv1 ViT-S/16 trained for 200 epochs on ImageNet-1K, this change preserves ImageNet linear probing accuracy and substantially improves semantic segmentation performance: VOC mIoU increases from 42.80 to 48.78, ADE20K from 19.85 to 21.97, and Cityscapes from 36.79 to 37.87. These results suggest that selective token mixing is a simple and effective bias for improving dense ViT representations.

**Why this may be relevant:**

It matched the geospatial machine learning search criteria and may be worth screening.

---

### 4. Natural Yet Challenging to Detect: Robust In-the-Wild TTS through EMA and Dual-Scoring Prompt Selection -- Submission for WildSpoof 2026 TTS Track

**Authors:** Renhe Sun, Jiayi Zhou, Haolin He, Yueying Feng, Jian Liu

**Published:** 2026-05-22

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 27

**Venue importance score included:** 0

**arXiv ID:** 2605.23859v1

**Paper link:** http://arxiv.org/abs/2605.23859v1

**PDF link:** https://arxiv.org/pdf/2605.23859v1

**Abstract:**

In this technical report, we describe our submission for the WildSpoof Challenge TTS Track: Text-to-Speech with In-the-Wild Data. We introduce F5-TTS-DPS, a model built upon the F5-TTS architecture. Our approach integrates Exponential Moving Average (EMA) into supervised fine-tuning to stabilize training and improve generalization. To enhance synthesis fidelity, we leverage large language models (LLMs) and large audio language models (LALMs) for dual-scoring prompt selection, filtering reference audio and text prompts to ensure quality while addressing alignment issues in noisy datasets. Experimental evaluation demonstrates that F5-TTS-DPS achieves strong performance with UTMOS of 3.20 and speaker similarity of 0.51 on the development set. More importantly, our model achieves the best a-DCF scores of 0.1582, 0.5233, and 0.2562 across three advanced SASV systems among all submissions, indicating our synthesized speech is the most difficult to detect and exhibits the highest degree of naturalness and authenticity. Combined with competitive WER performance, these results validate the effectiveness of our approach in generating natural-sounding speech with strong spoofing capabilities.

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis. It may help with cross-city, cross-region, or cross-sensor generalization.

---

### 5. Benchmarking LLMs for Community Governance Simulation with Life-history Narratives

**Authors:** Xu Chen, Yuanzi Li, Lei Wang, Nan Lu, Yang Wang, Anding Wang, Lei Shi, Xiaoxing Fu

**Published:** 2026-05-22

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 26

**Venue importance score included:** 0

**arXiv ID:** 2605.23783v1

**Paper link:** http://arxiv.org/abs/2605.23783v1

**PDF link:** https://arxiv.org/pdf/2605.23783v1

**Abstract:**

Effective community governance hinges on understanding what specific residents think and need. Recent work has used large language models (LLMs) to simulate human respondents, offering a scalable, reproducible way to study human attitudes and behaviors at low cost. However, these studies typically prompt the model with just a few demographic variables (age, gender, income), simulating only general role types. This is insufficient for community governance, where decisions depend on the views of specific residents. We bridge this gap with an integrated research framework covering dataset, benchmark, algorithm, and system. The dataset comprises approximately 1.2 million characters of first-person narrative collected through two-hour semi-structured interviews with each of 92 residents in an urban community, organized around nine community-governance domains. The benchmark probes 18 mainstream LLMs across four prompting strategies and shows that adding rich life-history profiles meaningfully raises fidelity above the no-profile baseline, but this gain comes with more input tokens per call from the longer prompts they require. The algorithm, curriculum-LoRA, is a parameter-efficient personalization framework that, by closing this fidelity-cost gap, matches the strongest baseline's fidelity at roughly 10x lower per-call cost and Pareto-dominates every configuration tested. The system integrates curriculum-LoRA into a closed-loop policy-evaluation pipeline. Together, these results bring individual-level LLM-based resident simulation within reach of resource-constrained local administrations, enabling community-governance decisions to be systematically pre-evaluated in silico before real-world deployment.

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis.

---

### 6. Asking For An Old Friend: Diagnosing and Mitigating Temporal Failure Modes in LLM-based Statutory Question Answering

**Authors:** Max Prior, Andreas Schultz, Matthias Grabmair

**Published:** 2026-05-22

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 26

**Venue importance score included:** 0

**arXiv ID:** 2605.23497v1

**Paper link:** http://arxiv.org/abs/2605.23497v1

**PDF link:** https://arxiv.org/pdf/2605.23497v1

**Abstract:**

Large language models are increasingly used for legal research, yet their fixed training cutoffs and reliance on static parametric knowledge are at odds with the evolving nature of statutory law. We study two temporal failure modes: post-cutoff staleness, where models apply superseded rules after legislative amendments, and recency bias, where models prefer newer provisions even when a historical version governs the fact pattern. To this end, we present a benchmark of 312 expert-validated, time-sensitive German statutory QA pairs spanning three categories: Post-Cutoff Amendment Questions, Pre-Amendment Questions, and Multi-Provision Pre-Amendment Questions. We evaluate five LLMs by OpenAI, Anthropic and DeepSeek under four inference settings: Vanilla, Web-search, and two retrieval-augmented variants that enforce temporal validity via a fact date extraction and version filtering. Using an LLM-as-a-judge validated against human expert ratings, we find severe degradation in the Vanilla post-cutoff setting. Both RAG approaches substantially improve performance across all question types, while web search yields unstable gains and exhibits a marked recency bias on historically anchored tasks. Our results indicate that reliable legal QA requires treating temporal validity as a hard constraint.

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis.

---

### 7. Machine learning applied to emerald gemstone grading: framework proposal and creation of a public dataset

**Authors:** FB Pena, D Crabi, Sandro C Izidoro, Érick O Rodrigues, G Bernardes

**Published:** 2026-05-22

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 22

**Venue importance score included:** 0

**DOI:** 10.1007/s10044-021-01041-4

**arXiv ID:** 2605.23777v1

**Paper link:** http://arxiv.org/abs/2605.23777v1

**PDF link:** https://arxiv.org/pdf/2605.23777v1

**Abstract:**

The grading of gemstones is currently a manual procedure performed by gemologists. A popular approach uses reference stones, where those are visually inspected by specialists that decide which one of the available reference stone is the most similar to the inspected stone. This procedure is very subjective as different specialists may end up with different grading choices. This work proposes a complete framework that entails the image acquisition and goes up to the final stone categorization. The proposal is able to automate the entire process apart from including the stone in the created chamber for the image acquisition. It discards the subjective decisions made by specialists. This is the first work to propose a machine learning approach coupled with image processing techniques for emerald grading. The proposed framework achieves 98% of accuracy (correctly categorized stones), outperforming a deep learning approach. Furthermore, we also create and publish the used dataset that contains 192 images of emerald stones along with their extracted and pre-processed features.

**Why this may be relevant:**

It matched the geospatial machine learning search criteria and may be worth screening.

---

### 8. LLMs as Noisy Channels: A Shannon Perspective on Model Capacity and Scaling Laws

**Authors:** Xu Ouyang, Deyi Liu, Yuhang Cai, Jing Liu, Yuan Yang, Chen Zheng, Thomas Hartvigsen, Yiyuan Ma

**Published:** 2026-05-22

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 21

**Venue importance score included:** 0

**arXiv ID:** 2605.23901v1

**Paper link:** http://arxiv.org/abs/2605.23901v1

**PDF link:** https://arxiv.org/pdf/2605.23901v1

**Abstract:**

Existing scaling laws for Large Language Models (LLMs), predominantly monotonic power laws, fail to explain emerging non-monotonic phenomena such as catastrophic overtraining and quantization-induced degradation, where performance deteriorates despite increased compute. We propose the Shannon Scaling Law, a unified theoretical framework that models LLM training as information transmission over a noisy channel, grounded in the Shannon-Hartley theorem. By mapping model parameters to channel bandwidth and training tokens to signal power, our formulation explicitly captures the interaction between learning signal and intrinsic noise. This perspective reveals a fundamental Shannon capacity for LLMs: scaling model size or data without preserving a sufficient signal-to-noise ratio (SNR) inevitably amplifies noise, inducing a transition from monotonic improvement to U-shaped performance degradation. We validate our theory through experiments on Pythia and OLMo2 under perturbations, including Gaussian noise, quantization and supervised fine-tuning on math, QA and code tasks. The Shannon Scaling Law consistently outperforms classical scaling laws and recent perturbation-aware laws, achieving strong $R^2$ scores and accurately capturing loss basins missed by prior approaches. It also extrapolates: fitted on $\leq$6.9B Pythia models with $\leq$180B tokens, it predicts the unseen 12B model up to 307B tokens at pooled $R^2{=}0.847$, while monotonic baselines collapse.

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis.

---

### 9. Detecting Drunk Driving Using Off-the-Shelf Smartwatches

**Authors:** Robin Deuber, Lanlan Yang, Michal Bechny, Christoph Heck, Matthias Pfäffli, Matthias Bantle, Florian von Wangenheim, Elgar Fleisch

**Published:** 2026-05-22

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 19

**Venue importance score included:** 0

**arXiv ID:** 2605.23663v1

**Paper link:** http://arxiv.org/abs/2605.23663v1

**PDF link:** https://arxiv.org/pdf/2605.23663v1

**Abstract:**

Alcohol-impaired driving remains a major yet preventable cause of road traffic injury and death, with many drivers underestimating their level of intoxication. Compared to in-vehicle systems, mobile drunk-driving detection using consumer smartwatches offers a scalable way to trigger preventive interventions and increase awareness without additional in-vehicle hardware. We introduce a system that leverages wrist accelerometer data and heart rate variability-derived physiological signals to detect alcohol-related driving impairment. We collected data in a randomized, controlled three-arm test-track study (n=54) and trained both logistic regression models with window-aggregated features and a two-tower 1D convolutional neural network (CNN), to detect alcohol-impaired driving. The CNN achieved a participant-averaged area under the receiver operating characteristic (AUROC) of 0.88 for detecting any alcohol intoxication and 0.86 for detecting driving above the WHO-recommended limit of 0.05 g/dL. To the best of our knowledge, this is the first work to (1) demonstrate drunk-driving detection using consumer smartwatches, (2) develop and evaluate such a system in a real vehicle on a closed test track, and (3) rigorously assess generalization to unseen participants. Together, these findings highlight the potential of wearable-based sensing to support scalable, measurement-driven prevention of alcohol-related traffic harm.

**Why this may be relevant:**

It may help with cross-city, cross-region, or cross-sensor generalization.

---

### 10. Sparse In-Network Learning via Shortest-Path Backpropagation and Finite-Rate Gating

**Authors:** Mohammad Reza Deylam Salehi

**Published:** 2026-05-22

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 15

**Venue importance score included:** 0

**arXiv ID:** 2605.23424v1

**Paper link:** http://arxiv.org/abs/2605.23424v1

**PDF link:** https://arxiv.org/pdf/2605.23424v1

**Abstract:**

In-network learning (INL) trains distributed neural modules by exchanging latent activations and backpropagated errors over a communication graph. This letter proposes Dijkstra-pruned INL (D-INL), which removes non-tree links by retaining a capacity-aware shortest-path tree rooted at the fusion node. To balance sparsity and predictive information, local routing (or aggregation) is modeled as a finite-rate stochastic gate with rate $R_g=I(Z; T)$. We derive a rate-distortion-generalization bound and validate the method on a reproducible distributed-classification experiment, where D-INL reduces training exchange by $70.4\%$ while preserving accuracy within the standard deviation of dense INL. Adding finite-rate regularization further reduces the estimated latent rate by $45.7\%$ relative to unregularized Dijkstra INL.

**Why this may be relevant:**

It connects to urban tree detection, canopy mapping, or vegetation analysis. It may help with cross-city, cross-region, or cross-sensor generalization.

---

