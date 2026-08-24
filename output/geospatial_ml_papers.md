# Weekly Geospatial ML Papers

**Search window:** 2026-08-17 to 2026-08-24

**Sources:** arXiv and Semantic Scholar

**Total selected papers:** 10

This digest focuses on geospatial analysis, urban climate, urban planning, infrastructure, and geospatial problem-solving using ML, computer vision, LLMs, VLMs, foundation models, self-supervised learning, and related methods.

Only papers from the selected top journals, conferences, or workshops are included by default. The venue importance score is included in **My Score**.

## Top Papers

### 1. Far from the Crowd: Scalable Self-Supervised Learning via Geographic Isolation

**Authors:** Daniele Rege Cambrin, Francesco Rossi, Mattia Varile

**Published:** 2026-08-20

**Found via:** Semantic Scholar

**My Score:** 49

**Venue importance score included:** 0

**Semantic Scholar citations:** 0

**arXiv ID:** 2608.19766

**Paper link:** https://www.semanticscholar.org/paper/3cf7e40615c32ce9113aa987df61e1b95f98f6d2

**Abstract:**

Self-supervised pretraining on remote sensing imagery typically treats all samples as equally informative, despite large variability in geographic and visual structure. We propose a curriculum learning strategy for self-supervised Earth observation that ranks samples by geographic isolation, a label-free proxy derived entirely from geolocation metadata already present in geospatial datasets, requiring no image decoding, no model feedback, and no manual annotation. Unlike visual complexity proxies, it scales as O(D log D) with dataset size D and is well-defined for both contrastive and reconstructive objectives. We integrate the proposed measure into MoCoV2 and MAE pretraining and evaluate across three downstream tasks from CopernicusBench (BigEarthNet, DFC-2020, LCZ). Our curriculum reaches baseline final-epoch performance using as few as 20% of the training budget (MAE) and at most 40% (MoCo) of the training budget, and improves final downstream performance by up to +5 mAP on BigEarthNet, with gains of 1-5 points across benchmarks, matching visual-complexity curricula while reducing pre-computation cost by more than 140x (4 s vs. 568 s on SSL4EO). A CKA and effective-rank analysis further reveals that curriculum-trained encoders develop higher-dimensional, more uniformly utilized embedding spaces throughout training.

**Why this may be relevant:**

It is directly related to remote sensing or Earth observation workflows.

---

### 2. The Coastline as a Structural Constraint: Harnessing Scene Geometry for Autonomous Surface Vessel Localization

**Authors:** Derek R. Benham, Joshua G. Mangelson

**Published:** 2026-08-21

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 43

**Venue importance score included:** 0

**arXiv ID:** 2608.21276v1

**Paper link:** http://arxiv.org/abs/2608.21276v1

**PDF link:** https://arxiv.org/pdf/2608.21276v1

**Abstract:**

Coastal environments contain rich, largely unexploited geometric structure capable of providing globally referenced localization cues. In this work, we present two complementary localization frameworks that exploit shoreline and water-surface geometry for GPS-denied autonomous surface vessel localization. The first framework leverages LiDAR observations of the water surface to estimate roll, pitch, and heave (vertical motion), while recovering global position and heading through direct registration of shoreline observations against a satellite-derived coastline map. The second framework relies solely on passive imagery to detect the shoreline and horizon through semantic segmentation. Using the proposed coastal scene geometry, shoreline distance is inferred from monocular imagery. Shoreline observations are accumulated into short-duration local submaps, registered against the same satellite-derived coastline map, and fused within a hierarchical factor graph. Evaluated across three real-world coastal datasets, the LiDAR pipeline consistently improves trajectory accuracy over standard baselines, while the monocular architecture maintains bounded long-term drift. In addition, we establish that modern zero-shot foundation models can reliably extract shoreline observations across diverse coastal environments. Together, these results demonstrate that coastal geometry provides a powerful and dependable source of globally referenced information for GPS-denied maritime localization.

**Why this may be relevant:**

It may help track foundation-model directions for Earth observation or geospatial AI. It is directly related to remote sensing or Earth observation workflows. It may be useful for LiDAR-based tree inventory, urban structure mapping, or 3D geospatial analysis.

---

### 3. SuppreSensing: Expert-Guided Feature Recalibration and Discrepancy Augmentation for Multimodal Object Detection

**Authors:** Xin Wu, Zhenyu Gao, Qiankun Zhang, Shaoyong Guo

**Published:** 2026-08-21

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 35

**Venue importance score included:** 0

**arXiv ID:** 2608.20944v1

**Paper link:** http://arxiv.org/abs/2608.20944v1

**PDF link:** https://arxiv.org/pdf/2608.20944v1

**Abstract:**

Multimodal object detection in remote sensing faces challenges due to semantic heterogeneity and modality-specific noise interference. To this end, we propose SuppreSensing, which reformulates multimodal fusion as a selective collaboration process that jointly models shared information and modality-specific cues. SuppreSensing first designs an Expert-driven Multimodal Feature Recalibration (EMFR) module, which reformulates shared-consensus extraction as an input-adaptive multi-expert selection process to alleviate the symmetry trap in multimodal fusion. Complementing this, a modality-specific attribute augmentation strategy is employed to enhance specific modality features by modeling bidirectional discrepancy patterns, mitigating cross-modal heterogeneity. Furthermore, we propose an Expert-driven Customized Feature Purification (ECFP) module based on a "specialized inspection-comprehensive analysis-diagnostic update" physical examination paradigm to iteratively filter redundancies and reinforce task-relevant semantics. Extensive experiments on the DroneVehicle and VEDAI datasets demonstrate that SuppreSensing achieves state-of-the-art detection performance. Cross-domain evaluations on natural scene datasets (FLIR and LLVIP) further validate its superior robustness and generalization capability across diverse environmental conditions.

**Why this may be relevant:**

It is directly related to remote sensing or Earth observation workflows. It may help with cross-city, cross-region, or cross-sensor generalization.

---

### 4. WildFin: An In-the-Wild Dataset for Fish Behavioral Recognition

**Authors:** Abigail G. Grassick, Jerome Tze-Hou Hsu, Ethan Lin, Ziang Liu, Max Whitton, Madelyn Hair, Liam Gutierrez, Haozheng Yu

**Published:** 2026-08-21

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 31

**Venue importance score included:** 0

**arXiv ID:** 2608.21281v1

**Paper link:** http://arxiv.org/abs/2608.21281v1

**PDF link:** https://arxiv.org/pdf/2608.21281v1

**Abstract:**

Recent advances in field technology have led to a massive influx of in-the-wild video data for ecological science. The primary bottleneck in leveraging this data is the high cost of expert annotation. While computer vision offers a potential solution, current models frequently fail when deployed in complex marine environments. To characterize these failures, we introduce WildFin, a novel benchmark for fish behavior recognition collected and annotated by ecologists.WildFin spans two critical real-world paradigms: stationary cameras monitoring groups of fish and dynamic divers following individual subjects. The dataset represents a massive curation effort, involving 1,350 hours of fieldwork and 600 hours of expert annotation to produce 9 hours of behavioral data with over 2 million frame-by-frame labels. We benchmark modern vision foundation models and quantify tradeoffs between static and spatiotemporal architectures, revealing the substantial gap that remains between current model capabilities and the demands of real-world underwater behavioral analysis. Project website: https://team-wildfin.github.io/.

**Why this may be relevant:**

It may help track foundation-model directions for Earth observation or geospatial AI.

---

### 5. Multi-Modal Traffic Sign Detection with Semantic Attributes for Autonomous Driving

**Authors:** Meda Lazar, Sourab Sridhar, Shashwata Gupta, Alexandra Tripcea, Varun Ravi, Senthil Yogamani

**Published:** 2026-08-21

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 29

**Venue importance score included:** 0

**arXiv ID:** 2608.20874v1

**Paper link:** http://arxiv.org/abs/2608.20874v1

**PDF link:** https://arxiv.org/pdf/2608.20874v1

**Abstract:**

Reliable traffic sign detection is a prerequisite for the global deployment of autonomous driving systems, where regulatory compliance and road safety depend on perceiving signs correctly across regions, ranges, and weather conditions. Despite recent progress, vision-based methods continue to face three fundamental limitations: poor cross-regional generalization due to high diversity across countries, degraded performance on small-object detection at long ranges (traffic signs occupy as little as $10{\times}10$ pixels at 200m), and fragile temporal tracking under the strongly non-linear perspective distortion that occurs as a vehicle approaches a sign. In this paper, we address the problem of robust, long-range, region-agnostic traffic sign perception by combining camera and Light Detection and Ranging (LiDAR) sensing. We present a multi-modal detection framework whose Intensity-Aware Deformable Fusion module aligns retro-reflective LiDAR cues with camera features, anchoring detection on geometric invariants rather than region-specific visual appearance. We further introduce a dual motion-model tracker that explicitly accounts for non-linear perspective transformations during vehicle approach, substantially improving temporal consistency over linear motion assumptions. Additionally, we develop a semantic attribute classification pipeline that estimates occlusion level, readability, sign embeddedness, and road relevance, providing actionable context to downstream planning. Extensive evaluation on our dataset, spanning 60+ countries and 2,500+ hours of driving data, shows that the proposed pipeline achieves an Object Miss Ratio (OMR) of 0.49% across 221,068 evaluation sequences, demonstrating globally generalizable traffic sign perception in commercial-grade autonomous driving systems.

**Why this may be relevant:**

It may be useful for LiDAR-based tree inventory, urban structure mapping, or 3D geospatial analysis. It may help with cross-city, cross-region, or cross-sensor generalization.

---

### 6. AI Infrastructure in Space: How Far Can We Go?

**Authors:** Qing Li, Qiyang Zhang, Daliang Xu, Tianze Huang, Dingge Zhang, Yihao Zhao, Xiaolong Huang, Jinfeng Wen

**Published:** 2026-08-21

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 27

**Venue importance score included:** 0

**arXiv ID:** 2608.21034v1

**Paper link:** http://arxiv.org/abs/2608.21034v1

**PDF link:** https://arxiv.org/pdf/2608.21034v1

**Abstract:**

Satellites are becoming programmable computing platforms capable of running increasingly demanding AI workloads. This shift raises a systems problem: how can AI services remain deployable, manageable, and recoverable after launch when compute capacity, connectivity, energy, and thermal headroom vary over orbital time? This paper develops a systems vision for AI infrastructure in space. We define it as the systems layer that manages AI capabilities across spacecraft, orbital networks, ground stations, and cloud backends, while treating orbital and physical state as part of the resource model. We synthesize relevant foundations from terrestrial AI infrastructure, satellite networking, and satellite edge computing, and examine the physical constraints that directly shape system design. We further ground this vision in three in-orbit case studies spanning the node, platform, and service levels. Telemetry from BUPT-1 satellite shows that usable compute capacity is bounded by thermal and energy envelopes. SateLight on BUPT-2 satellite reduces application-update transmission latency by 56.54% on average and up to 91.18%, with 100% update correctness. A stateful VLM serving case further shows that thermal interruptions make execution-state recovery a first-class systems problem. These observations motivate a research agenda for space-native resource management, lifecycle support, and sustained AI service across space and ground.

**Why this may be relevant:**

It may be useful for multimodal geospatial understanding using image-text models. It is directly related to remote sensing or Earth observation workflows. It is related to urban planning, infrastructure, or built-environment analysis.

---

### 7. Move by Move: Measuring and Steering How LLMs Conduct Psychotherapy

**Authors:** Afonso Baldo, Hugo Pitorro, Areti Vassilopoulos, Anabela C. Areias, Maya D'Eon, Fabíola Costa, Ricardo Rei, Nuno M. Guerreiro

**Published:** 2026-08-21

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 26

**Venue importance score included:** 0

**arXiv ID:** 2608.21325v1

**Paper link:** http://arxiv.org/abs/2608.21325v1

**PDF link:** https://arxiv.org/pdf/2608.21325v1

**Abstract:**

Users increasingly turn to large language models for emotional support, yet little is known about how these models actually conduct a psychotherapy interaction. We introduce an ontology of ten therapeutic moves: compact, function-based categories grounded in the MULTI-60 inventory, validated through an annotation campaign with five licensed psychologists, and scaled with a judge-based approach that matches expert agreement. Applying it to real counseling transcripts and model-led sessions, we compare the move distributions between human clinicians and a panel of frontier models. Models over-use inquiry at up to three times the human rate, neglect psychoeducation, and are strongly context-anchored: they carry forward strategies initiated by a human clinician but rarely initiate them themselves. Exposing the ontology as a set of tools roughly halves the mean deviation from the human move distribution and improves turn-level alignment with human therapist by 7-9 percentage points, without any fine-tuning.

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis.

---

### 8. Electronic Navigational Chart Change Classification

**Authors:** Jacob Arndt, Abhishek Potnis, Alexandre Sorokine

**Published:** 2026-08-20

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 22

**Venue importance score included:** 0

**arXiv ID:** 2608.20218v1

**Paper link:** http://arxiv.org/abs/2608.20218v1

**PDF link:** https://arxiv.org/pdf/2608.20218v1

**Abstract:**

Electronic Navigational Charts (ENCs) are geospatial vector datasets used in maritime navigation systems that represent hydrographic and navigational information such as depths, navigational aids, traffic schemes, and hazards. A major challenge for hydrographic offices is determining whether a given chart change poses a critical or non-critical risk to maritime safety. Existing workflows rely heavily on manual review and verification, which is labor-intensive, scales poorly with the volume of incoming chart updates, and introduces inter-analyst inconsistencies. To address this challenge, we propose a method for automated classification of ENC changes. We establish a baseline encoding scheme to translate complex vector data changes into a structured tabular format for classification models. The two crucial components of the encoding scheme include a spatial context encoder to enrich the change representations with surrounding geographic features, and an ENC attribute encoder to represent nuanced attribute-value descriptions of the modified objects. We evaluate the proposed approach across two distinct operational datasets, comprising 1,308 chart pairs containing over 100,000 individual chart modifications. Tuned gradient-boosted trees leveraging the proposed encoding schemes achieve accuracies of 90% and 94% on the two datasets, yielding a 5-7% improvement over default hyperparameterized models trained on encodings without spatial context and attribute embeddings. These results demonstrate the viability of integrating machine learning into operational geospatial pipelines to improve ENC maintenance and enhance maritime safety. Finally, our experiments demonstrate the effectiveness of simple location and spatial aggregation methods, providing a foundation for evaluating more sophisticated spatial representation learning techniques for this application.

**Why this may be relevant:**

It connects to urban tree detection, canopy mapping, or vegetation analysis.

---

### 9. Matching Urban Flood Sensor Placement to Monitoring Objectives Using Bayesian Optimal Experimental Design

**Authors:** Chen Cheng, Vinh Ngoc Tran, Jiayuan Dong, Sarah Whitaker, Shannon Bergt, John Ziker, Valeriy Y. Ivanov, Xun Huan

**Published:** 2026-08-21

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 15

**Venue importance score included:** 0

**arXiv ID:** 2608.21182v1

**Paper link:** http://arxiv.org/abs/2608.21182v1

**PDF link:** https://arxiv.org/pdf/2608.21182v1

**Abstract:**

Flood-monitoring sensors are often placed according to coverage, access, or expected inundation. However, the value of a measurement depends on the prediction or decision it is intended to inform. Using tRIBS-Urban simulations and a neural-network surrogate of the August 2014 metropolitan Detroit flood, we examine how this learning target changes single-sensor placement. Across 2,576 candidate locations, we compare parameter-oriented optimal experimental design (PO-OED), which values expected information gain (EIG) about model parameters, with goal-oriented optimal experimental design (GO-OED), which values EIG about specified flood predictions. We also examine how parameter EIG evolves during the event, and illustrate that parameter learning translates unevenly into reductions in predictive uncertainty across locations and lead times. Under GO-OED, point-depth targets favor nearby locations, whereas regional-average and regional maximum-depth targets can favor nonlocal locations. Weighted multi-point objectives retain similar broad spatial patterns, although their computed max-EIG locations differ. Public geospatial data further provide illustrative feasibility and contextual classifications for deployment screening. These results show how monitoring objectives shape sensor placement in optimal experimental design, and motivates an objective-first workflow that defines the intended prediction and priorities, applies field-verified restrictions, and ranks locations by EIG.

**Why this may be relevant:**

It matched the geospatial machine learning search criteria and may be worth screening.

---

### 10. Mining beyond Earth with Space Robots: Exploration, Sampling, and Extraction

**Authors:** Dong Li, Dujun Nie, Xiaotong Zhang, Ruilin Wang, Yuchen Li, Chang Ge, Chao Xiong, Kaichang Di

**Published:** 2026-08-21

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 15

**Venue importance score included:** 0

**arXiv ID:** 2608.21358v1

**Paper link:** http://arxiv.org/abs/2608.21358v1

**PDF link:** https://arxiv.org/pdf/2608.21358v1

**Abstract:**

Space resource acquisition and utilization, commonly referred to as Space Mining, represent critical pathways for enabling sustained human exploration and unlocking commercial opportunities in space. These resources mainly include helium-3, water, mineral resources on the Moon and Mars, and abundant mineral deposits on asteroids. Due to the harsh conditions of space, communication delays, and high launch costs, the development of autonomous robotic systems is critical to achieving efficient, cost-effective space mining. This paper provides a comprehensive overview of space mining robotics and associated technologies. First, we review the background of space mining, including international policies, commercial entities, and recent advancements. We define a systematic six-stage architecture for space mining: Exploration is initiated by (1) remote sensing for target identification and (2) precise in situ robotic detection; Sampling progresses from (3) single-robot small-scale sampling to (4) multi-robot large-scale excavation; and Extraction integrates (5) autonomous resource extraction and (6) final integration into in situ construction or terrestrial transport. Additionally, we review and curate existing resources for space mining research, including real-world mission data, terrestrial analog datasets, and high-fidelity simulation environments. Finally, we identify critical open challenges in autonomous space mining and delineate a strategic research roadmap to bridge current technological gaps, fostering the transition toward a sustainable off-world economy. To track ongoing developments in space mining, we maintain an updated project page: https://github.com/OpenSpace-Lab/Space-Mining-with-Robotics-List.

**Why this may be relevant:**

It is directly related to remote sensing or Earth observation workflows.

---

