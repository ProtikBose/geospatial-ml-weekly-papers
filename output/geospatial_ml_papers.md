# Weekly Geospatial ML Papers

**Search window:** 2026-07-13 to 2026-07-20

**Sources:** arXiv and Semantic Scholar

**Total selected papers:** 10

This digest focuses on geospatial analysis, urban climate, urban planning, infrastructure, and geospatial problem-solving using ML, computer vision, LLMs, VLMs, foundation models, self-supervised learning, and related methods.

Only papers from the selected top journals, conferences, or workshops are included by default. The venue importance score is included in **My Score**.

## Top Papers

### 1. AgentFAIR: A Multi-Agent Collaborative Framework for FAIRness Evaluation of Geospatial Datasets

**Authors:** Ming Chen, Pranav Pai

**Published:** 2026-07-17

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 66

**Venue importance score included:** 0

**arXiv ID:** 2607.15781v1

**Paper link:** http://arxiv.org/abs/2607.15781v1

**PDF link:** https://arxiv.org/pdf/2607.15781v1

**Abstract:**

Geospatial datasets support applications from urban planning to climate modeling, yet consistent assessment of FAIR compliance is difficult. Existing evaluators use different rubrics and evidence sources and may fail on JavaScript-rendered pages or repository-specific identifiers. For 50 datasets from 10 repositories, the standard deviation of normalized scores across available tools averages 15.0 percentage points and reaches 30.3 for one dataset. Because these outputs are not equivalent measurements, we use them to characterize disagreement and failure modes, not comparative accuracy. We present AgentFAIR, a multi-agent framework combining structured metadata extraction with 13 sub-principle-specific LLM evaluators. Each produces a 0-3 maturity score, cited evidence, and recommendations; a critic checks evidence and consistency and can request targeted re-evaluation. Mean Findability, Accessibility, Interoperability, and Reusability scores are 79.7%, 70.4%, 45.3%, and 72.0%. Rank correlations with four baseline tools range from 0.31 to 0.61; the FAIR-enough comparison is not statistically significant. On a 10-dataset repeated-run subset, sub-principle agreement averages 89% (standard deviation: 3 percentage points), versus 71% without the critic. A preliminary 15-dataset expert study yields Fleiss' kappa of 0.71 and 82% alignment with expert consensus. API cost is approximately USD 0.054 per dataset. These results support auditability and feasibility, while the limited benchmark, incomplete ablations, and single-model-family validation constrain claims about accuracy and generalization.

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis. It is related to urban planning, infrastructure, or built-environment analysis. It may help with cross-city, cross-region, or cross-sensor generalization.

---

### 2. Establishment and Application of Natural Hazards Database Based on Remote Sensing and GIS : From Hazard Modeling to Risk‐Informed Decision Making

**Authors:** Chong Xu, Xiangli He

**Published:** 2026-07-15

**Venue:** Transactions on GIS

**Found via:** Semantic Scholar

**My Score:** 63

**Venue importance score included:** 0

**Semantic Scholar citations:** 0

**DOI:** 10.1111/tgis.70355

**Paper link:** https://www.semanticscholar.org/paper/d3bbac9ed01dc529cd7c5c971dd73f907a7a79a2

**Abstract:**

Natural hazards databases are valuable not only because they record past events, but also because they provide the foundation for modeling, assessment, prediction, and risk‐informed decision‐making. This editorial focuses on the application of natural hazards databases based on remote sensing and Geographic Information Systems (GIS), shifting attention from database establishment to their use in hazard mechanisms, susceptibility assessment, exposure analysis, resilience evaluation, systemic impact assessment, and operational prediction. The papers discussed in this virtual issue cover diverse hazards and methods, including landslide‐dammed lake outburst floods, snow‐ and ice‐related hazards, earthquake–rainfall coupled landslides, debris flows, floods, urban heat islands, water quality degradation, railway network disruption, and flash flood prediction. Together, these studies demonstrate how geospatial databases can support process reconstruction, scenario analysis, socioeconomic loss assessment, infrastructure network analysis, environmental monitoring, and uncertainty‐aware forecasting. This editorial argues that future applications should place greater emphasis on exposure integration, model robustness, uncertainty communication, interpretability, transferability, and practical usability. As climate change, urbanization, infrastructure expansion, and social interdependence continue to reshape disaster risks, natural hazards databases will become increasingly important bridges between disaster observation, scientific interpretation, and risk‐informed action.

**Why this may be relevant:**

It is directly related to remote sensing or Earth observation workflows. It is relevant to urban climate and heat-resilience research. It is related to urban planning, infrastructure, or built-environment analysis.

---

### 3. Knowing the Self, Understanding the World: A Dual-Cognition Benchmark for UAV Spatio-temporal Reasoning with MLLMs

**Authors:** Like Liu, Zhengzheng Xu, Haitao He, Hongzhe Li, Shuchang Zhang, Dian Shao

**Published:** 2026-07-17

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 55

**Venue importance score included:** 0

**arXiv ID:** 2607.16193v1

**Paper link:** http://arxiv.org/abs/2607.16193v1

**PDF link:** https://arxiv.org/pdf/2607.16193v1

**Abstract:**

Multimodal large language models have achieved strong performance across diverse vision-language tasks, yet their capabilities in UAV scenarios remain insufficiently explored. Recent UAV-oriented benchmarks have begun to evaluate MLLMs in aerial scenarios, but they typically focus on scene understanding, event recognition, or navigation completion, rather than jointly assessing the dual-cognition capability required for UAV agents: reasoning about both the UAV's own state and the external environment in multiview spatio-temporal contexts. To address this gap, we present UAV-DualCog, a benchmark for aerial multiview spatio-temporal reasoning built on this dual-cognition perspective. UAV-DualCog includes both image and video tasks to jointly evaluate self-state and environment-state reasoning, while requiring spatial or temporal grounding beyond discrete answer prediction. We also develop an automated pipeline that constructs data from scene-level semantic point clouds, yielding a scalable benchmark with diverse scenes, hundreds of landmarks, and thousands of QA samples. Extensive evaluations show that current MLLMs remain far from reliable in UAV dual cognition. Self-state reasoning, viewpoint transformation, precise spatial grounding, and temporal interval localization are persistent bottlenecks, and additional validation with thinking/frontier models and a human baseline confirms that the benchmark is understandable to humans but challenging for existing models. We further construct UAV-DualCog-Train from disjoint scenes and show through a lightweight optimization probe that it provides useful structured supervision, suggesting its value not only as an evaluation benchmark but also as a data resource for advancing MLLM-based UAV agents. Project website and supplementary materials: https://uav-dualcog.lozumi.com

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis. It may be useful for LiDAR-based tree inventory, urban structure mapping, or 3D geospatial analysis.

---

### 4. More with Less: a Large Scale Remote Sensing VLM with a Simple Recipe

**Authors:** Stefan Maria Ailuro, Mario Markov, Mohammad Mahdi, L. V. Gool, D. Paudel

**Published:** 2026-07-17

**Venue:** arXiv

**Found via:** Semantic Scholar, arXiv

**My Score:** 45

**Venue importance score included:** 0

**Semantic Scholar citations:** 0

**arXiv ID:** 2607.15942

**Paper link:** https://www.semanticscholar.org/paper/44172ea66643d4a69a7dad0a157dc5b8a845e063

**PDF link:** https://arxiv.org/pdf/2607.15942v1

**Abstract:**

Remote sensing vision-language models are increasingly expected to support open-ended reasoning over Earth Observation data and a variety of tasks. Most recent progress in this area has been driven by remote-sensing-specific architectural designs, often introducing new encoders, alignment modules, or task-specific fusion mechanisms. In this work, we challenge the necessity of such architectural specialization. We show that a generally capable vision-language model can achieve competitive or state-of-the-art performance at challenging remote sensing benchmarks, provided that it is trained at sufficient scale across diverse data and tasks. Our model uses a single language policy that can either answer directly in text or invoke a localization tool for segmentation and grounding. To train this heterogeneous behaviour, we employ a multi-task reinforcement learning framework with adaptive task rewards covering multiple-choice VQA, free-form VQA, captioning, detection, and segmentation across a large variety of input types. Our approach achieves competitive results across a broad set of benchmarks, including high-resolution, multi-temporal, multi-modal and multi-view tasks. Further, as training data scales, our experiments show consistent improvements across most tasks both in and out of distribution, which correlate with per-task data diversity. These findings suggest that, for remote sensing VLMs, data scale is more important than architectural novelty.

**Why this may be relevant:**

It may be useful for multimodal geospatial understanding using image-text models. It is directly related to remote sensing or Earth observation workflows.

---

### 5. DPNeXt: A Lightweight Multi-Scale Feature Fusion Framework for Efficient ViT-Based Multi-Task Dense Prediction

**Authors:** Jehun Kang, Jungha Wang, Youngjun Hwang, David Hyunchul Shim

**Published:** 2026-07-17

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 36

**Venue importance score included:** 0

**arXiv ID:** 2607.16012v1

**Paper link:** http://arxiv.org/abs/2607.16012v1

**PDF link:** https://arxiv.org/pdf/2607.16012v1

**Abstract:**

Multi-Task Learning (MTL) in robotics perception systems supports comprehensive 3D spatial scene understanding by integrating semantic segmentation and depth estimation. While Vision Foundation Models (VFMs) are increasingly adopted as robust feature encoders, existing decoding strategies present a critical bottleneck. To address this, we propose DPNeXt, a streamlined multi-scale feature fusion decoder and efficient alternative to the standard Dense Prediction Transformer (DPT). DPNeXt uses dual depthwise separable inverted bottlenecks to improve frozen VFM utilization through fusion-centric decoding and independent task modularization. To further mitigate negative inductive transfer between tasks, we introduce the Multi-Task Boundary Guidance (MTBG) strategy. Unlike prior boundary-aware methods that add fusion modules or gating, MTBG applies symmetric boundary-focused supervision to encourage geometric consistency without extra annotation or inference cost. Experiments on Cityscapes show that DPNeXt-S outperforms prior state-of-the-art (SOTA) MTL models, while DPNeXt-B further improves the overall performance and achieves the best results among the compared methods. On NYUv2, DPNeXt-B also achieves the best semantic segmentation and depth estimation results among the compared methods while requiring substantially fewer trainable parameters than prior large-scale MTL models. Compared with the standard DPT, DPNeXt-S reduces trainable parameters by 78.6% and achieves the fastest inference speed among the compared models on resource-constrained laptop hardware. The source code, model checkpoints, and a demo video will be made available at https://github.com/kangjehun/DPNeXt.

**Why this may be relevant:**

It may help track foundation-model directions for Earth observation or geospatial AI.

---

### 6. GeoChrono: Benchmarking and Rethinking Long-Term Temporal Understanding in Remote Sensing

**Authors:** Yujie Li, Jiancheng Pan, Zhiwei Wei, Jiuniu Wang, Mugen Peng, Wenjia Xu

**Published:** 2026-07-17

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 36

**Venue importance score included:** 0

**arXiv ID:** 2607.15768v1

**Paper link:** http://arxiv.org/abs/2607.15768v1

**PDF link:** https://arxiv.org/pdf/2607.15768v1

**Abstract:**

Remote sensing offers an unparalleled vantage point for observing the Earth's long-term surface evolution, yet it demands that a model not only perceive land cover at isolated moments, but also track changes, memorize evolution histories, and reason across time and space. However, existing studies lack a systematic evaluation that dissects these distinct competencies. To fill this gap, we introduce ChronoBench, a multidimensional benchmark that decomposes this task into four progressive cognitive levels (i.e., Land Cover Perception, Temporal Recognition, Long-Term Memory, and Spatio-Temporal Reasoning). The ChronoBench comprises 12 sub-tasks and 17,689 rigorously validated QA (Question-Answer) pairs. Extensive evaluations reveal that mainstream MLLMs fall drastically behind human experts, with Long-Term Memory emerging as the most critical bottleneck. Motivated by this finding, we further propose GeoChrono, an MLLM with enhanced capabilities for tracing, memorizing, and reasoning about long-term geographic evolution. Leveraging the physical prior that geographic parcels remain spatially fixed while their semantics evolve, we design a Temporal Trajectory Encoder~(TempEnc) that constructs per-location temporal trajectories for dedicated land cover evolution modeling, and we introduce a Coarse-to-Fine Token Compressor~(C2FComp) that adaptively preserves dynamic regions while compressing the static background. To support training, we also construct ChronoInstruct, a 104K-sample instruction-tuning dataset spanning all competency levels for training. GeoChrono achieves state-of-the-art performance on ChronoBench, surpassing the leading commercial MLLMs by over 20%, while C2FComp reduces visual tokens by over 56% while retaining GeoChrono's 94.6% performance. The code and data will be available at https://github.com/IntelliSensing/GeoChrono

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis. It is directly related to remote sensing or Earth observation workflows.

---

### 7. From Continuous Deployment to Queryable Dataset: Terabyte-Scale AIS-Aligned Passive Acoustic Labelling

**Authors:** Wayne Renaud, Priyanka Aravindan, Gabriel Spadon

**Published:** 2026-07-15

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 35

**Venue importance score included:** 0

**arXiv ID:** 2607.13840v1

**Paper link:** http://arxiv.org/abs/2607.13840v1

**PDF link:** https://arxiv.org/pdf/2607.13840v1

**Abstract:**

Long-duration passive acoustic deployments produce large archives of recordings that are not linked to vessel tracks or encounter structure, leaving range and contact conditions unavailable as variables and requiring manual selection for analysis. To address this limitation, we propose a database-native workflow that aligns hydrophone recordings with Automatic Identification System (AIS) position reports to produce distance-resolved data. Fixed-duration recording windows and AIS messages are stored as persistent geospatial tables and associated through an indexed spatiotemporal join, replacing in-memory nested iteration with a single scalable set-based database process capable of handling continuous, multi-year, million-window archival deployments without exhausting available memory. In this study, the approach processes approximately 9.5x10e5 recording windows and 6.9x10e6 AIS position reports, producing a structured table that separates no-contact, single-contact, and two-contact windows, with the closest point of approach computed directly where applicable and background conditions characterized via deterministic spectral ranking. This formulation enables a GeoAI framework in which spatially indexed, queryable data become directly usable for machine learning. The resulting data product reveals predominantly noise-dominated conditions, with vessel contributions emerging mainly at shorter ranges, indicating that the task lies in extracting structure under background-limited regimes. Spectrogram and quantitative analyses show weak tonal signatures embedded in noise and a consistent decay of signal-to-noise ratio with distance, supporting the use of this representation for scalable machine learning, similarity analysis, and predictive acoustic modelling in real maritime environments.

**Why this may be relevant:**

It matched the geospatial machine learning search criteria and may be worth screening.

---

### 8. Examining the Associations between Visual and Non-Visual Elements and Cyclists' Route Choices for Various Trip Purposes

**Authors:** Heyang Hua, Koichi Ito, Filip Biljecki

**Published:** 2026-07-17

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 34

**Venue importance score included:** 0

**arXiv ID:** 2607.15808v1

**Paper link:** http://arxiv.org/abs/2607.15808v1

**PDF link:** https://arxiv.org/pdf/2607.15808v1

**Abstract:**

Understanding cyclist preferences for the characteristics of the built environment is important in promoting sustainable urban transportation and active mobility. Despite previous studies on cyclists' route choices, the influence of visual and non-visual factors on these choices for different trip purposes remains unclear; thus, this paper fills this gap through a data-driven case study in Montreal, Canada. Non-visual factors include socioeconomic factors and two-dimensional environments, while visual factors involve visual perception during cycling and are computed using street view images. The study consists of two parts: one part analyzes spatiotemporal information to explore the non-visual factors between the start and end points of cycling trips, and the other part investigates the discrepancies in distributions of these factors between the shortest path and the actual one. The findings reveal the spatiotemporal characteristics that influence active riding choices, such as increased greenery and lower levels of motorization. These insights can inform the planning of street networks and the development of infrastructure to improve the use of active transportation.

**Why this may be relevant:**

It connects to urban tree detection, canopy mapping, or vegetation analysis. It is related to urban planning, infrastructure, or built-environment analysis.

---

### 9. DELUGE: Towards Continental-Scale Daily Pluvial Flood Damage Prediction via Interpretable Conditioning on Foundation Model Embeddings

**Authors:** Yuya Kawakami, Daniel Cayan, Dongyu Liu, Kwan-Liu Ma, Tom Corringham

**Published:** 2026-07-17

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 26

**Venue importance score included:** 0

**arXiv ID:** 2607.16050v1

**Paper link:** http://arxiv.org/abs/2607.16050v1

**PDF link:** https://arxiv.org/pdf/2607.16050v1

**Abstract:**

Pluvial (rainfall-driven) flooding accounts for 45% of National Flood Insurance Program (NFIP) claims in the United States and is harder to predict than its riverine and coastal counterparts, with existing approaches limited to coarse resolution, regional domains, or computationally intensive process-based models unsuitable for daily continental-scale use. We present DELUGE, a multimodal deep learning framework for daily pluvial flood damage prediction at ~1 km resolution and national scale, trained on spatially and temporally corrected NFIP claims (2017-2022) and structured around the hazard, exposure, and vulnerability components of disaster risk. Rather than blanket coverage of the Conterminous United States (CONUS), we model the top 100 highest-claim 75 km cells, distributed nationwide and accounting for ~81% of total pluvial flood claims. Our architectural novelty is a pair of parametric modules in the hydrometeorology branch, a Value Modulator and a Temporal Modulator, conditioned on terrain descriptors and AlphaEarth foundation-model embeddings, that expose directly inspectable hydrological response parameters and provide architecture-level interpretability-by-design. Under a spatial block holdout, DELUGE outperforms tuned Random Forest, XGBoost, and LightGBM baselines by 9% to 30% on a dollar-weighted area under the precision-recall curve (PR-AUC), a metric that emphasizes the rare, high-cost claims of greatest operational interest. Beyond DELUGE, we argue this interpretable conditioning scheme is a transferable pattern for integrating foundation-model embeddings into other geospatial prediction tasks.

**Why this may be relevant:**

It may help track foundation-model directions for Earth observation or geospatial AI.

---

### 10. Hardware-triggered Time Synchronization of Roadside Multi-lidar, Multi-camera Measurement System for Accurate Data Alignment

**Authors:** Shiva Agrawal, Savankumar Bhanderi, Zhiran Yan, Gordon Elger

**Published:** 2026-07-17

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 22

**Venue importance score included:** 0

**arXiv ID:** 2607.15889v1

**Paper link:** http://arxiv.org/abs/2607.15889v1

**PDF link:** https://arxiv.org/pdf/2607.15889v1

**Abstract:**

Accurate temporal alignment of heterogeneous sensors is necessary for reliable environment perception in roadside multi-lidar, multi-camera systems, particularly in dense urban traffic. For this purpose, an open-source, simple, modular, and configurable hardware-triggered time-synchronization circuit is presented in this work to perform temporal alignment or accurate time synchronization between a lidar and multiple cameras. In the designed circuit, a lidar synchronization pulse is used as a reference input, and independently programmable, time-delayed trigger pulses are generated for each camera, allowing flexible adaptation to varying sensor setups and mounting geometries. A series of experiments is conducted on a roadside-mounted perception system comprised of lidar and three cameras, in which the trigger delay is systematically varied, and its impact on spatial-temporal alignment is evaluated. For different classes of road users, the overlap between lidar point cloud measurements and camera measurements is quantified to identify delay configurations that maximize cross-sensor consistency. The proposed circuit is shown to achieve robust and repeatable synchronization while remaining straightforward to deploy, reconfigure, and extend due to its simple and open-source design. Following validation on a three-camera roadside system, the circuit is extended to a vehicle platform with seven cameras and a lidar, providing a low-cost, extensible solution for multi-sensor synchronization across infrastructure and vehicle setups. All hardware circuit design files and source codes are available at https://github.com/shiva-THI/hardware-trigger-time-sync-lidar-cameras.

**Why this may be relevant:**

It may be useful for LiDAR-based tree inventory, urban structure mapping, or 3D geospatial analysis. It is related to urban planning, infrastructure, or built-environment analysis.

---

