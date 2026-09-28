# Weekly Geospatial ML Papers

**Search window:** 2026-09-21 to 2026-09-28

**Sources:** arXiv and Semantic Scholar

**Total selected papers:** 10

This digest focuses on geospatial analysis, urban climate, urban planning, infrastructure, and geospatial problem-solving using ML, computer vision, LLMs, VLMs, foundation models, self-supervised learning, and related methods.

Only papers from the selected top journals, conferences, or workshops are included by default. The venue importance score is included in **My Score**.

## Top Papers

### 1. SatNav: A Scalable Benchmark for Long-Horizon UAV Vision-Language Navigation from Satellite Imagery

**Authors:** Jiajun Jiang, Chunliang Hua, Zichun Chen, Yanxing Wu, Zeyuan Yang, Jie Song, Xiao Hu

**Published:** 2026-09-25

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 59

**Venue importance score included:** 0

**arXiv ID:** 2609.31507v1

**Paper link:** http://arxiv.org/abs/2609.31507v1

**PDF link:** https://arxiv.org/pdf/2609.31507v1

**Abstract:**

Urban uncrewed aerial vehicle (UAV) vision-language navigation (VLN) requires agents to follow instructions across extended urban spaces, inherently demanding long-term memory and geospatial grounding. However, scaling existing benchmarks remains difficult because of their reliance on costly reconstructed 3D assets, limiting geographic diversity and episode scale. To address this, we introduce SatNav, a scalable, long-horizon UAV VLN benchmark built from high-resolution satellite imagery. SatNav targets city-level navigation missions and uses satellite crops as approximations of UAV nadir views for visual observations. Through an automated cue-to-episode pipeline, SatNav constructs 118K episodes from 59 scenes across 18 cities, with an average trajectory length of 379 m. To stress-test long-horizon memory and geospatial reasoning, SatNav defines three task families: Boundary, Landmark, and Route, targeting loop progress tracking, landmark-based spatial grounding, and route following with counting cues. Benchmarking classical VLN agents and recent agents based on large vision-language models (LVLMs) on SatNav shows that city-scale navigation remains challenging. We further introduce SwiftVLN, a modular framework with switchable memory components, and conduct systematic memory-design ablations. Finally, satellite-to-UAV transfer experiments show that satellite-trained navigation models can operate on real-flight UAV observations, showing the practical relevance of SatNav. Our project page: https://eku127.github.io/SatNav/

**Why this may be relevant:**

It may be useful for multimodal geospatial understanding using image-text models. It is directly related to remote sensing or Earth observation workflows.

---

### 2. GraphWrit3R: End-to-End 3D Scene Graph Writing

**Authors:** Luka Milivojevic, Nikola Popovic, Sayan Deb Sarkar, Sebastian Koch, Iro Armeni, Luc Van Gool, Danda Pani Paudel

**Published:** 2026-09-25

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 37

**Venue importance score included:** 0

**arXiv ID:** 2609.31595v1

**Paper link:** http://arxiv.org/abs/2609.31595v1

**PDF link:** https://arxiv.org/pdf/2609.31595v1

**Abstract:**

3D scene graphs provide a structured representation of complex environments by encoding objects, their semantic attributes, and the spatial and functional relationships between them. Current approaches for 3D scene graph generation suffer from several fundamental limitations. They rely on complex multi-stage pipelines with explicit intermediate representations, making systems fragile and prone to error propagation. They assume access to ground-truth object annotations during inference, which deviates from real-world scenarios. They depend on proprietary models, hindering open-source deployment, or incur prohibitively slow inference. We present GraphWrit3R, a simple end-to-end method that takes a 3D point cloud, Gaussian Splats, or a combination of both as input, and directly outputs a complete scene graph as a structured JSON script. The graph lists all objects, their semantic attributes, and the relationships between them, while avoiding all of the above mentioned limitations. The choice of multiple input modalities is purely for versatility, allowing a single set of weights to handle diverse scenarios. Point cloud inputs are encoded via Sonata and Gaussian Splat inputs via Chorus, with both modalities projected onto a shared voxel grid and fused through a novel per-voxel contrastive alignment loss before being decoded by a large language model. As a natural consequence of the LLM, GraphWrit3R also supports open-vocabulary querying. On the 3DSSG benchmark, our method achieves state-of-the-art performance on object class, predicate, and triplet recall, outperforming methods that rely on ground-truth object annotations during inference. We further provide qualitative results and analyze different input modality configurations, contrastive loss formulations, and token fusion strategies.

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis. It may be useful for LiDAR-based tree inventory, urban structure mapping, or 3D geospatial analysis.

---

### 3. Electric Vehicle Charging Station Location Selection using Geospatial Artificial Intelligence (GeoAI)

**Authors:** Eun Hak Lee, Euntak Lee

**Published:** 2026-09-24

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 36

**Venue importance score included:** 0

**DOI:** 10.1016/j.tre.2026.104930

**arXiv ID:** 2609.30417v1

**Paper link:** http://arxiv.org/abs/2609.30417v1

**PDF link:** https://arxiv.org/pdf/2609.30417v1

**Abstract:**

As electric vehicle (EV) adoption increases, ensuring efficient and well-distributed charging infrastructure has become a critical challenge. While many EV charging station location problem (CSLP) studies focus on minimizing costs or travel distance, it is crucial to consider the surrounding geospatial characteristics of existing stations that influence operational performance. This study proposes a geospatial artificial intelligence (GeoAI)-based framework that integrates high-dimensional EV-related geospatial data, including EV usage, land-use, population, and traffic attributes. We incorporate a variational autoencoder (VAE) and a graph convolutional network (GCN) into the model to capture similarities among existing charging stations, and to identify suitable locations for future stations. The VAE compresses high-dimensional EV input data into a low-dimensional latent space, and the GCN uses this latent representation to predict locations suitable for charging stations. Using real-world data from Bryan-College Station, Texas, US, the proposed model outperforms state-of-the-art baselines, achieving an F1-score of 0.87 in distinguishing existing station locations from non-station locations. The model also identifies 27 additional candidate locations that show geospatial characteristics similar to those of existing stations, based on a similarity score. We further evaluate two policy implementation scenarios, maximizing geospatial similarity and minimizing total travel distance, each yielding different outcomes aligned with distinct strategic objectives. The findings highlight the importance of incorporating spatial context into CSLP and provide valuable insights for future EV infrastructure planning, promoting both efficiency and accessibility in the rapidly growing electric mobility sector.

**Why this may be relevant:**

It is related to urban planning, infrastructure, or built-environment analysis.

---

### 4. EAServe: Encode-Aware Disaggregated Serving for Multimodal Large Language Models

**Authors:** Kunxiong Zhu, Zhihao Shu, Hangyu Zheng, Minghai Qin, Miao Yin, Gagan Agrawal, Wei Niu

**Published:** 2026-09-25

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 31

**Venue importance score included:** 0

**DOI:** 10.1145/3838684.3846886

**arXiv ID:** 2609.31551v1

**Paper link:** http://arxiv.org/abs/2609.31551v1

**PDF link:** https://arxiv.org/pdf/2609.31551v1

**Abstract:**

Disaggregating the two stages, Prefill and Decode, onto separate GPU pools is now a standard optimization for (text-only) LLM serving. However, multimodal LLMs (MLLMs), which add a third phase, Encode, pose new challenges for resource allocation. Encode turns images, video, or audio into embeddings that the language model can consume, yielding a three-stage Encode-Prefill-Decode (EPD) pipeline. Existing frameworks offer only partial answers: text-only PD systems lack Encode, while EPD frameworks expose it as a separate service without regulating downstream request flow. The pipeline also carries a structural resource imbalance: every request enters through Encode before downstream work can begin, yet per-request execution leaves the encode GPU severely underutilized even at high loads, starving the downstream Prefill and Decode workers. Addressing this, we reposition Encode as the control point of the EPD pipeline, exposing three tightly coupled dimensions: when work enters downstream, where prefill executes, and how the GPU is shared. We instantiate this in EAServe across two co-designed layers. Its runtime manages load-adaptive micro-batching, rate-controlled partial offload to a co-resident prefill worker, and dynamic SM partitioning for predictable co-location. The configuration layer, Hybrid Auto Selection (HAS), navigates the joint space of GPU allocation, encode batch size, and offload ratio by pruning unbalanced allocations with per-stage capacity profiling and refining the remainder through TPE-based Bayesian optimization. Evaluated on three MLLM architectures spanning image, video, and audio, EAServe delivers up to 4.3x and 1.7x higher goodput than NVIDIA Dynamo and vLLM, respectively, under identical SLO constraints, sustains more balanced and higher GPU utilization across the EPD pipeline, and reaches near-optimal configurations faster than baseline search methods.

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis.

---

### 5. Enabling a Unified Cross-Domain Representation for Two-Finger Gripper Manipulation via Interaction-Centric Modeling

**Authors:** Guanlin Li, Shifeng Bao, Yihan Zhao, Haitao Shen, Haoyang Li, Chen Zhao, Tong Yang, Jie Tang

**Published:** 2026-09-25

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 29

**Venue importance score included:** 0

**arXiv ID:** 2609.31207v1

**Paper link:** http://arxiv.org/abs/2609.31207v1

**PDF link:** https://arxiv.org/pdf/2609.31207v1

**Abstract:**

Achieving robust cross-embodiment generalization in imitation learning demands overcoming a critical representation flaw that inextricably entangles task semantics with hardware-specific visual geometry. We propose an interaction-centric framework that leverages the shared structure of two-finger grippers via a parameterized universal gripper abstraction, yielding a canonical gripper-frame representation. Given language and RGB-D observations, a VLM infers the subtask and grounds an interaction triplet (gripper, held, target), while SAM~2.1 tracks masks to reduce VLM queries. We design concise hybrid features that combine target/collision artificial potential fields for global guidance with segmented gripper-frame point clouds for local geometry, and use a Flow-Matching Transformer to predict smooth 7-DoF action chunks. Experiments in simulation and real-world tasks demonstrate that ours is the first imitation learning approach to simultaneously achieve competitive benchmark scores and extreme cross-embodiment/cross-viewpoint zero-shot sim-to-real transfer to completely distinct, heterogeneous robot platforms.

**Why this may be relevant:**

It may be useful for multimodal geospatial understanding using image-text models. It may be useful for LiDAR-based tree inventory, urban structure mapping, or 3D geospatial analysis. It may help with cross-city, cross-region, or cross-sensor generalization.

---

### 6. WeaveAgent: A Two-Stage Tool-Routing Agent for Ultra-High-Resolution Remote Sensing Imagery

**Authors:** Zhongyu Pang

**Published:** 2026-09-25

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 24

**Venue importance score included:** 0

**arXiv ID:** 2609.31234v1

**Paper link:** http://arxiv.org/abs/2609.31234v1

**PDF link:** https://arxiv.org/pdf/2609.31234v1

**Abstract:**

Problem. Ultra-high-resolution (UHR) remote sensing with vague user intents has two bottlenecks: visual tokens are expensive, and tool calling must be format-reliable (pretrained models emit zero tool calls zero-shot). Method. WeaveAgent, a two-stage tool-routing agent, decouples routing from visual perception. Stage A is routing-first: emission is trained, not elicited. Stage B executes conditionally: intrinsic queries enter visual answering (full-scene thumbnail; a WeaveEarth-style evidence board as an optional fixed-budget, approx. 5k-token compression interface); extrinsic queries execute tool call on original full-resolution imagery, answering from tool observations in a second, observation-masked round. Training: alignment SFT, then GRPO under reward R_WA2. Results. Alignment SFT lifts extrinsic routing from 0% to 80.75% (323/400); GRPO suppresses 9 intrinsic mis-emissions while tool selection is unchanged. The trained 2B system does not beat the zero-shot 8B baseline overall (0.263 vs. 0.250), a diagnostic contribution. Oracle attribution separates two repair ingredients: loading the observation into context lifts extrinsic answer accuracy from 0.025 to 0.425 under marker-free cross-mode returns, and the two-turn SFT stage adds a further +9.3 points to 0.518 at a small routing cost. A +/- image ablation shows emission suppression is visually grounded, and a query-register matrix shows LLM-rewritten queries cost trained checkpoints 2-11 points. Scope. All training and evaluation use the 5,000 / 3,273 / 1,000-record VagueUHR corpus (600 intrinsic + 400 tool-requiring; the base seeds synthesis and is not used for optimization). Single-pass evidence construction runs at 7.31 s per image on an RTX 4090. Code, data, and evaluation protocols will be released.

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis. It is directly related to remote sensing or Earth observation workflows.

---

### 7. Evaluating Cultural Awareness of LLMs for Haitian Creole

**Authors:** Christelle Clervilsson, Yanzhu Guo

**Published:** 2026-09-25

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 21

**Venue importance score included:** 0

**arXiv ID:** 2609.31506v1

**Paper link:** http://arxiv.org/abs/2609.31506v1

**PDF link:** https://arxiv.org/pdf/2609.31506v1

**Abstract:**

Large language models (LLMs) exhibit substantial performance disparities between high- and low-resource languages. Beyond lower task performance, they often fail to capture the cultural norms and values of underrepresented communities. In this work, we present the first systematic evaluation of cultural awareness in LLMs for Haitian Creole, a language spoken by millions but severely underrepresented in digital resources. We assess cultural awareness along four complementary dimensions---specificity, bias, diversity, and variation---using a benchmark of culturally salient prompts curated by native speakers in a text infilling setting. Our results reveal a clear gap between cultural awareness in Haitian Creole and higher-resource French, with Haitian performance being more uneven across domains and more affected by French linguistic interference. Story generation further reveals recurring portrayals of Haitian characters through hardship and resilience, showing that even positive characterizations can encode stereotypical narratives. Our code, benchmark, and evaluation framework are publicly available.

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis.

---

### 8. RupeeBias: Auditing Demographic Bias in Indian Economic Guidance from Large Language Models

**Authors:** Pavithra P M Nair, Bhavik Talaviya, Shourya Bhushan, Rahul Pankajakshan, Seema Guruvadoo, Avinash Agarwal, Gilad Gressel, Krishnashree Achuthan

**Published:** 2026-09-25

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 21

**Venue importance score included:** 0

**arXiv ID:** 2609.31245v1

**Paper link:** http://arxiv.org/abs/2609.31245v1

**PDF link:** https://arxiv.org/pdf/2609.31245v1

**Abstract:**

Individuals turn to large language models (LLMs) for guidance across a wide range of economic tasks, from comparing loan options and planning savings to deciding what raise to ask for or how much to charge for their services. LLMs are known to reproduce social biases, and biased economic guidance may influence what users believe they are worth, what they ask for, and what they ultimately accept. This risk is especially salient in India, where economic outcomes are shaped by demographic categories such as caste and urban-rural location. Existing LLM bias benchmarks, however, are largely designed around Western demographic categories and therefore miss key axes of economic disparity in the Indian context. We introduce RupeeBias, a benchmark for auditing demographic bias in LLM-generated economic guidance across Indian economic settings. RupeeBias consists of 39,150 prompts spanning four use cases: salary estimation, salary increment estimation, counter-offer recommendation, and service pricing recommendation. The benchmark follows a single-attribute counterfactual design, holding the description of the user's qualifications, experience, or service offering fixed while varying one demographic identifier at a time. RupeeBias covers 87 India-specific demographic identifiers across six axes: caste, religion, regional identity, gender, disability, and urban-rural location, with all prompts constructed in both English and Hinglish. We evaluate nine LLMs on RupeeBias and find systematic demographic disparities across all six axes. For otherwise identical prompts that differ only in demographic identifier, LLM-generated economic outputs differ by 20.2% on average. We publicly release RupeeBias to support future research on demographic bias in LLM-generated economic guidance across India-specific demographic and economic contexts.

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis.

---

### 9. Same Text, Different Numbers: The Divergence of LLM-Based Measures

**Authors:** Hamid Boustanifar, Sasan Mansouri

**Published:** 2026-09-25

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 21

**Venue importance score included:** 0

**arXiv ID:** 2609.31013v1

**Paper link:** http://arxiv.org/abs/2609.31013v1

**PDF link:** https://arxiv.org/pdf/2609.31013v1

**Abstract:**

Researchers increasingly use generative large language models (LLMs) to convert corporate text into empirical variables. We examine the extent to which LLM-based textual measures are invariant to model choice using thirteen measures, including sentiment, management clarity, uncertainty, answer specificity, and climate and political risk. Seven LLMs from different providers score earnings call transcripts of S&P 500 companies on these constructs. Cross-model rank correlations average only 0.52, and transcript-level differences common across providers account for only 34% of total score variation. Cross-model disagreement does not predict subsequent analyst or market disagreement, consistent with a substantial model-specific component rather than common ambiguity in the underlying disclosure. Model choice significantly affects downstream inference, with coefficient magnitudes, signs, and statistical significance varying substantially across models. Averaging across providers makes transcript rankings more stable for most constructs, but score levels remain sensitive to the models included in the ensemble. LLM-generated variables should therefore be treated as model-contingent measurements and validated across providers.

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis.

---

### 10. Bandwidth, Latency, and 400 Million Kilometers: The Case for Mars-Local Compute

**Authors:** Maleeha Masood, Indranil Gupta, Deepak Vasisht

**Published:** 2026-09-25

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 15

**Venue importance score included:** 0

**arXiv ID:** 2609.31566v1

**Paper link:** http://arxiv.org/abs/2609.31566v1

**PDF link:** https://arxiv.org/pdf/2609.31566v1

**Abstract:**

There have been recent proposals for human settlements on Mars in 2030s. Any human activity on Mars must be preceded by extensive robotic exploration. However, Mars exploration is bottlenecked by the low bandwidth, intermittent Mars-Earth link. For example, HiRISE, a high-resolution camera onboard the Martian orbiter MRO imaged less than 3% of Mars over eleven years, even though MRO's low resolution Context Camera had mapped more than 99% of Mars in that time. We present a systems case for shared compute for Mars exploration. Such Mars-local compute, paired with advances in computer vision and AI, can enable large volumes of data to be collected and processed on Mars while sending periodic updates, insights, and selective datasets to Earth. To overcome the lack of surface infrastructure on Mars, we propose a two-tier in-orbit deployment of computational satellites that provides consistent coverage and bandwidth. Our analysis shows that the proposed deployment can start small: one areostationary node makes compute reachable from all active Mars missions, two additional areostationary nodes can extend this coverage to roughly 90% of the planet, while low-Mars-orbit nodes add high-rate surface links and compute capacity where demand grows.

**Why this may be relevant:**

It is directly related to remote sensing or Earth observation workflows. It is related to urban planning, infrastructure, or built-environment analysis.

---

