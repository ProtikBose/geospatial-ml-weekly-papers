# Weekly Geospatial ML Papers

**Search window:** 2026-10-26 to 2026-11-02

**Sources:** arXiv and Semantic Scholar

**Total selected papers:** 10

This digest focuses on geospatial analysis, urban climate, urban planning, infrastructure, and geospatial problem-solving using ML, computer vision, LLMs, VLMs, foundation models, self-supervised learning, and related methods.

Only papers from the selected top journals, conferences, or workshops are included by default. The venue importance score is included in **My Score**.

## Top Papers

### 1. Geospatial analysis of urban heat exposure and environmental vulnerability using remote sensing in Khulna City, Bangladesh

**Authors:** Md Refath Hossan, Mohammad Ismail Hossain, Zahid Hassan Shaon, K. Hyakumura

**Published:** 2026-10-31

**Venue:** GeoJournal

**Found via:** Semantic Scholar

**My Score:** 52

**Venue importance score included:** 0

**Semantic Scholar citations:** 0

**DOI:** 10.1007/s10708-026-11726-0

**Paper link:** https://www.semanticscholar.org/paper/de42cf1e4b57803a7d0a2dc2473c3f5177537b81

**Abstract:**

No abstract available.

**Why this may be relevant:**

It is directly related to remote sensing or Earth observation workflows. It is relevant to urban climate and heat-resilience research.

---

### 2. Movens-Zero: Scaling Humanoid Motion Foundation Models with Large-Scale Human Videos

**Authors:** Wendong Bu, Tinghong Ye, Qizhou Wang, Jiacheng Li, Zhiqi Ge, Yuze Lin, Zhongqi Yue, Yi Su

**Published:** 2026-10-30

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 31

**Venue importance score included:** 0

**arXiv ID:** 2610.41877v1

**Paper link:** http://arxiv.org/abs/2610.41877v1

**PDF link:** https://arxiv.org/pdf/2610.41877v1

**Abstract:**

Scaling humanoid motion foundation models is constrained by the scarcity of diverse, robot-executable data and by the difficulty of jointly learning from heterogeneous multimodal inputs while supporting real-time closed-loop control. We present Movens-5M, constructed from raw Internet videos through clip generation, quality filtering, semantic annotation, motion recovery, and physical refinement with humanoid retargeting and execution verification. It contains 15 million human-motion sequences and 5 million physically executable humanoid-motion sequences spanning over 10,000 hours, aligned with text, RGB video, speech, and music. Building on this data, we introduce Movens-Zero, a scalable understanding-generation-execution architecture that supports joint learning across modalities and real-time closed-loop execution. Task-mixed flow-matching training jointly optimizes a single action expert across seven generation tasks, enabling direct motion generation from text, speech, music, and video. Multimodal Real-Time Chunking connects overlapping chunks under continuously updated instructions and robot states for continuous closed-loop execution. We further introduce Movens-Intent, a four-track benchmark with 8,192 expert-verified condition-motion pairs across text, speech, music, and video. Experiments show consistent gains across all four modalities when scaling execution-verified data from 1% to 100% and action-expert capacity from 64M to 911M parameters, while demonstrating that data quality and cross-modal supervision improve generation and execution.

**Why this may be relevant:**

It may help track foundation-model directions for Earth observation or geospatial AI.

---

### 3. An Empirical Study on Learning Rooftop Solar Potential from Satellite Imagery Directly Without Explicit Geometry

**Authors:** Joshua Lee

**Published:** 2026-10-30

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 27

**Venue importance score included:** 0

**arXiv ID:** 2610.41111v1

**Paper link:** http://arxiv.org/abs/2610.41111v1

**PDF link:** https://arxiv.org/pdf/2610.41111v1

**Abstract:**

Rooftop solar potential estimation often relies on LiDAR, digital surface models (DSMs), or pipelines that explicitly reconstruct roof geometry before estimating solar potential. We propose Direct Rooftop Solar Prediction (DRSP), an end-to-end formulation that maps satellite imagery and coarse regional sunlight information directly to application-level solar outputs. DRSP neither requires explicit geometric representations as input nor predicts roof orientation, slope, height, DSMs, or other geometric quantities as intermediate outputs, and therefore requires no geometric intermediate supervision. To enable large-scale study of this formulation, we develop a programmatic data-curation pipeline that converts per-panel information from the Google Solar API into usable-rooftop masks and spatial solar-energy targets, yielding two geographically distinct datasets containing approximately 60K rooftops from the U.S. Midwest and 87K from Texas. We demonstrate the feasibility of DRSP and systematically characterize the effects of geographic training distribution, model depth, image resolution, regional sunlight conditioning, and heatmap regression objectives. Overall, our results suggest that useful rooftop-scale solar information can be learned directly from 2D imagery without explicit geometric intermediate representations, offering a simpler path toward large-scale solar assessment. Our code and dataset are available at https://github.com/joshualee124/direct_rooftop_solar_prediction.

**Why this may be relevant:**

It is directly related to remote sensing or Earth observation workflows. It may be useful for LiDAR-based tree inventory, urban structure mapping, or 3D geospatial analysis. It is relevant to urban climate and heat-resilience research.

---

### 4. SAR-TS-BERT: Physics-Guided Self-Supervised Pre-Training With Polarimetric Features for SAR Time-Series Crop Classification

**Authors:** Jieqiu Wang, Yuhan Zhang, Bo Zheng, Shaoming Zhang

**Published:** 2026-10-30

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 23

**Venue importance score included:** 0

**arXiv ID:** 2610.41728v1

**Paper link:** http://arxiv.org/abs/2610.41728v1

**PDF link:** https://arxiv.org/pdf/2610.41728v1

**Abstract:**

Multitemporal synthetic aperture radar (SAR) imagery provides continuous, cloud-free observations of crop phenology for agricultural monitoring in cloudy and rainy regions, yet high-accuracy classification typically requires extensive labeled samples. Although self-supervised pre-training mitigates label dependency in remote sensing, existing frameworks primarily target optical imagery or generic spatial SAR scenes, underutilizing temporal backscatter dynamics and polarimetric scattering mechanisms. We propose SAR-TS-BERT, a physics-guided BERT-style self-supervised pre-training framework for SAR time-series crop classification. SAR-TS-BERT integrates backscatter intensities and polarimetric ratio features (VV, VH, and VV/VH) with dual-polarimetric Cloude-Pottier decomposition parameters ($H/α/A$) into a six-band input representation through two core designs: 1) a physics-guided span masking strategy (SpanPhysics) that adaptively selects contiguous masked spans based on temporal backscatter change rates to prioritize key phenological transitions; and 2) a dual-branch cross-modal fusion encoder that models backscatter and polarimetric decomposition features through separate Transformer branches followed by bidirectional cross-attention fusion. On independent test sets in Estonia (EuroCropsML) and the USA (California CDL), SAR-TS-BERT achieves overall accuracies (OAs) of 96.78% and 87.29%, respectively, and attains a mean monthly OA of 99.37% on Chongming Island, Shanghai. On the Estonia benchmark, pre-training improves OA and Macro F1 by 1.17 and 1.59 percentage points over training from scratch under full supervision, and by 2.58 and 5.19 percentage points using only 1% labeled data. Incorporating SAR scattering physics into temporal self-supervised pre-training effectively enhances crop classification accuracy, parcel-level mapping consistency, and few-shot transferability.

**Why this may be relevant:**

It is directly related to remote sensing or Earth observation workflows.

---

### 5. Spectral Haar Binarizer: Compact Boolean Contrast Representations for Hyperspectral Classification

**Authors:** Michał Romaszewski, Przemysław Głomb

**Published:** 2026-10-30

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 22

**Venue importance score included:** 0

**arXiv ID:** 2610.41478v1

**Paper link:** http://arxiv.org/abs/2610.41478v1

**PDF link:** https://arxiv.org/pdf/2610.41478v1

**Abstract:**

Tsetlin Machines offer an interpretable, hardware-friendly alternative to conventional machine learning models, but applying them to continuous hyperspectral measurements requires converting spectral signals into Boolean representations. Standard binarisation methods typically discretise each spectral band independently, potentially discarding important relationships between neighbouring wavelengths. In this paper, we introduce the Spectral Haar Binarizer (SHB), a contrast-based spectral representation method that constructs Boolean predicates from differences between selected spectral intervals. Inspired by Haar-like contrast features, the method uses an AdaBoost-style selection procedure to obtain a compact set of discriminative spectral predicates. We evaluate SHB on five heterogeneous hyperspectral datasets covering forensic blood detection, agricultural and urban remote sensing, and rainforest tree-species classification. Across binary and multiclass tasks, SHB consistently outperforms standard per-band binarisation strategies and provides the strongest or near-strongest results across classifiers. In binary tasks, TM-SHB achieves the best average performance, while RF-SHB is strongest in multiclass settings. Bayesian and rank-based analyses confirm that SHB's advantage is robust across datasets and not driven by isolated cases. The results show that representing continuous hyperspectral measurements is a central processing step for efficient classification. That contrast-based Boolean features provide an effective bridge between information-rich sensor measurements and compact, logic-based processing.

**Why this may be relevant:**

It is directly related to remote sensing or Earth observation workflows. It connects to urban tree detection, canopy mapping, or vegetation analysis.

---

### 6. TradeWar: A Benchmark for Execution-Grounded Trade Negotiation with Adaptive LLM Agents

**Authors:** Xiangyu Kong, Ruirui Yang, Xia Hou

**Published:** 2026-10-30

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 21

**Venue importance score included:** 0

**arXiv ID:** 2610.42004v1

**Paper link:** http://arxiv.org/abs/2610.42004v1

**PDF link:** https://arxiv.org/pdf/2610.42004v1

**Abstract:**

Multi-turn negotiation remains a challenging problem for large language model (LLM) agents. While LLMs can conduct natural-language dialogue, existing benchmarks predominantly assess only agreement rates, overlooking whether negotiated commitments actually create value once executed. To address this gap, we introduce TradeWar, a multi-country simulation benchmark that translates negotiation dialogues into concrete tariff and trade-share policies, enforces capacity and network constraints during settlement, and evaluates outcomes via an Economic Health Index (EHI). To solve this execution-grounded task, we propose TACTIC (Trade-aware Adaptive Consolidation and Theory-of-mind for International Commerce), an agent that iteratively refines its negotiation strategy across episodes-without updating base LLM weights-by leveraging prior experience, opponent behavior, and past settlement outcomes. Despite using zero-shot chain-of-thought (CoT) prompting, PromptLLM attains a 75% agreement rate but only 57.1 final EHI (*100), whereas TACTIC reaches 68.8. Across 20 sequential episodes and three seeds, TACTIC's final EHI improves from 58.2 to 73.2, compared with 65.2 for an ablation without cross-episode updates. Under technology-controls and energy-crisis shocks, TACTIC also exhibits smaller performance degradation than PromptLLM and MemoryLLM. These results indicate that CoT deliberation and interaction memory alone do not fully address delayed execution feedback, whereas settlement-grounded adaptation improves long-horizon negotiation in TradeWar.

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis.

---

### 7. SATFRONT: Detecting Atmospheric Fronts with Satellite Data using Machine Learning

**Authors:** Ioannis Dravilas, Miruna Stoicescu, Roope Tervo, Carlos Horn, Oriol Hinojo Comellas, Sina Montazeri, Andrea Meraner, Ana Lucic

**Published:** 2026-10-30

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 20

**Venue importance score included:** 0

**arXiv ID:** 2610.42111v1

**Paper link:** http://arxiv.org/abs/2610.42111v1

**PDF link:** https://arxiv.org/pdf/2610.42111v1

**Abstract:**

Atmospheric fronts are associated with much of the high-impact weather in the mid-latitudes, yet their identification and classification remain largely manual and subjective. Existing deep learning approaches rely primarily on gridded reanalysis or forecast data, limiting their applicability to satellite observations available for time-critical applications. We introduce SATFRONT, a machine learning framework for detecting cold, warm, and occluded fronts over Europe from geostationary satellite observations, with reanalysis data as an optional additional input. The model is trained on frontal analyses from five European national meteorological services and evaluated against UK Met Office analyses for 2024. Using satellite observations alone, SATFRONT achieves a Critical Success Index (CSI) of 0.428 at a 150 km tolerance, within the range of agreement between analyses from different meteorological services (0.277-0.501) and higher than that of an operational rule-based front detector that uses satellite data (0.133). Adding ERA5 reanalysis increases the CSI to 0.591. ERA5 substantially improves the placement of individual fronts, although its effect on their annual spatial distribution varies by front type. These results demonstrate that cold, warm, and occluded fronts can be detected directly from geostationary satellite observations, providing a basis for automated frontal analyses at the high temporal frequency required for time-critical applications.

**Why this may be relevant:**

It is directly related to remote sensing or Earth observation workflows.

---

### 8. RAMA: Retrieval-Augmented Multi-Agent Routing with Episodic Memory for LEO Satellite Networks

**Authors:** Xin Ming Li, Peng Hu

**Published:** 2026-10-30

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 18

**Venue importance score included:** 0

**arXiv ID:** 2610.42068v1

**Paper link:** http://arxiv.org/abs/2610.42068v1

**PDF link:** https://arxiv.org/pdf/2610.42068v1

**Abstract:**

Low-Earth orbit (LEO) satellite networks present a challenging routing environment due to rapidly changing topology, traffic, and link conditions. Existing deep reinforcement learning (DRL) routing methods typically rely on current observations and information encoded in network weights, limiting their ability to exploit successful past experiences. We propose RAMA, a retrieval-augmented multi-agent DRL framework with Approximate Information State (AIS), in which each satellite combines its local observation, recent routing history, neighboring state information, and retrieved entries from a per-satellite episodic memory. Retrieved experiences are integrated through a Transformer-based decision network trained with AIS-based auxiliary objectives. With weights frozen in a 140-satellite Kepler constellation, RAMA reduces mean end-to-end latency by 13.4% and 99th-percentile latency by 66.7% relative to the state-of-theart double deep Q-network (DDQN) routing method, mainly by avoiding long detours. Updated online, RAMA remains stable while DDQN degrades. On the 1,584-satellite Starlink shell 1, the reduction in mean latency grows to 93.2%, and updating RAMA online lowers its mean latency by a further 25.5%. These results demonstrate the effectiveness of retrieval-augmented memory for scalable decentralized routing in LEO satellite networks.

**Why this may be relevant:**

It is directly related to remote sensing or Earth observation workflows.

---

### 9. SketchMate: Agentic Geometric Reasoning for Zero-Shot Precision Insertion

**Authors:** Jiaming Wang

**Published:** 2026-10-30

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 17

**Venue importance score included:** 0

**arXiv ID:** 2610.41844v1

**Paper link:** http://arxiv.org/abs/2610.41844v1

**PDF link:** https://arxiv.org/pdf/2610.41844v1

**Abstract:**

Inserting an unseen part requires sub-millimetre precision and the correct orientation of keyed features. Current zero-shot agentic manipulation methods built on vision-language models (VLMs) produce spatial outputs that are far too coarse for this. We propose to let a VLM build a sketch model of the task, i.e., a few geometric primitives and two mate frames, which a VLM agent measures with geometric tools in multi-view depth and which a standard planner and compliant controller execute. Because a sketch describes the parts independently of their placement, the robot needs to build it only once per task. A sketch memory stores each agent run and transfers the stored sketch to later placements by point-cloud registration, so that the VLM is called only for unfamiliar parts. After grasping the part, the robot inspects both mating faces at close range and corrects the sketch by shape matching. On 69 simulated insertion episodes, our method inserts 88% of the parts at the assembled pose in a strict kinematic test, while ReKep and MOKA with the same VLM insert none. On new placements of eight tasks, reusing one stored run inserts as many parts as calling the agent in each episode, and it produces the sketch in 3.4 s instead of about 90 s.

**Why this may be relevant:**

It may be useful for multimodal geospatial understanding using image-text models.

---

### 10. Quantitative Ultrasound Characterizes Perfusion Trajectories in Healthy and Inflamed Gingival Wound Healing

**Authors:** Haowei Tai, Oscar Duran-Garnica, Karen Villarreal, Hsun-Liang Chan, Oliver D. Kripfgans

**Published:** 2026-10-30

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 15

**Venue importance score included:** 0

**arXiv ID:** 2610.41897v1

**Paper link:** http://arxiv.org/abs/2610.41897v1

**PDF link:** https://arxiv.org/pdf/2610.41897v1

**Abstract:**

Rationale and Objectives: Visual examination of extraction-site healing provides limited insight into underlying vascular recovery. We developed a quantitative ultrasound framework to assess gingival perfusion and persistent inflammation. Materials and Methods: Patients (n = 51) undergoing extraction and socket preservation were imaged longitudinally using color-flow ultrasound and laser speckle contrast analysis (LASCA) from 2 weeks to 3 months after extraction. Pre-scan-converted Total Recall Imaging (TRI) data with phase information were processed using scan conversion, bilateral filtering, and power estimation to derive velocity-weighted color pixel density (CPDvel). Gingival regions of interest were automatically segmented using deep learning and assessed with Dice and Bland-Altman analyses. CPDvel was compared between healthy and inflamed visits in early ( 35 days) periods and with LASCA. Results: Segmentation achieved a mean Dice score of 0.98 and median of 0.99 (IQR, 0.98-0.99), with minimal area bias (-0.005%; 95% limits of agreement, -1.68% to 1.67%). Median CPDvel decreased by 81% between early and recovery periods in healthy visits (p = 0.01), compared with a nonsignificant 26% reduction in inflamed visits (p = 0.31). During recovery, CPDvel was higher in inflamed than healthy visits (0.12 vs 0.03 cm/s; p = 0.04). LASCA showed smaller reductions (13% and 9%, respectively). CPDvel was positively correlated with LASCA in healthy (one-sided p = 0.03) and inflamed visits (one-sided p = 0.13). Conclusions: TRI-based quantitative ultrasound enabled automated perfusion assessment with reduced dependence on scanner display settings. Distinct perfusion patterns and more pronounced temporal changes than LASCA support its potential for noninvasive monitoring of oral wound healing and persistent inflammation.

**Why this may be relevant:**

It matched the geospatial machine learning search criteria and may be worth screening.

---

