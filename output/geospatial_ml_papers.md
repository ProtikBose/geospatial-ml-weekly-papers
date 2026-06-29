# Weekly Geospatial ML Papers

**Search window:** 2026-06-22 to 2026-06-29

**Sources:** arXiv and Semantic Scholar

**Total selected papers:** 10

This digest focuses on geospatial analysis, urban climate, urban planning, infrastructure, and geospatial problem-solving using ML, computer vision, LLMs, VLMs, foundation models, self-supervised learning, and related methods.

Only papers from the selected top journals, conferences, or workshops are included by default. The venue importance score is included in **My Score**.

## Top Papers

### 1. A Framework for Augmenting Simulation-Based Building Energy Models with Earth Observational Microclimate Data Using Machine Learning Predictions

**Authors:** Amanda Worthy, M. Ashayeri, Julian D. Marshall, N. Abbasabadi

**Published:** 2026-06-23

**Venue:** Urban Science

**Found via:** Semantic Scholar

**My Score:** 72

**Venue importance score included:** 0

**Semantic Scholar citations:** 0

**DOI:** 10.3390/urbansci10070341

**Paper link:** https://www.semanticscholar.org/paper/a8fc2f9ea5878a2061cab1cfc367050afefb3b23

**Abstract:**

Accurate urban building energy modeling (UBEM) is constrained by mismatches between standard climate inputs and actual urban microclimate conditions. This study introduces a scalable, bottom-up, framework that integrates EnergyPlus building energy modeling simulation outputs with Earth observational and geographical-based urban morphology data, which are enhanced through machine learning techniques to improve energy demand predictions in urban settings. Applied to Los Angeles (LA), California, we evaluate the representativeness of typical meteorological year (TMYx) sampling sites against actual urban environmental conditions. We find that while satellite-derived surface temperatures show reasonable alignment with average city conditions, significant discrepancies are observed in urban form metrics such as tree cover, street cover, and building density, suggesting that TMYx stations should be placed in denser urban areas. We augment EnergyPlus simulations for 19 single-family buildings, with remote sensing data using machine learning models, to generate city-wide residential energy consumption heatmaps corrected for microclimate conditions. Models capture substantial intra-urban variation, with predicted energy use differing by approximately 10% between neighborhoods. Feature importance analysis highlights land surface temperature as a key predictor, underscoring its relevance to building energy research. We also find the majority of TMY3 sampling sites to be in low-vulnerability areas, underscoring the structural mismatch that is embedded in urban form and climate. This framework offers a scalable path for integrating urban microclimate effects into energy modeling to enable more precise and equitable energy policy and planning.

**Why this may be relevant:**

It is directly related to remote sensing or Earth observation workflows. It connects to urban tree detection, canopy mapping, or vegetation analysis. It is relevant to urban climate and heat-resilience research.

---

### 2. OctoSense: Self-Supervised Learning for Multimodal Robot Perception

**Authors:** Anthony Bisulco, Jeremy Wang, Kostas Daniilidis, Randall Balestriero, Pratik Chaudhari

**Published:** 2026-06-25

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 63

**Venue importance score included:** 0

**arXiv ID:** 2606.27317v1

**Paper link:** http://arxiv.org/abs/2606.27317v1

**PDF link:** https://arxiv.org/pdf/2606.27317v1

**Abstract:**

We present OctoSense, an open-source sensor platform with stereo RGB and event cameras, LiDAR, a thermal camera, an inertial measurement unit, RTK-corrected global positioning system, and proprioception (CAN bus data from a car, and joint angles for a quadruped robot). The eponymous OctoSense dataset contains 59 hours of time-synchronized driving data across different types of environments at different times of the day, including situations with highly degraded sensors. We demonstrate multi-modal self-supervised learning using such real-world robotics data, where sensors have different representations, frequencies, latencies and noise. Our approach, a "late-fusion" masked autoencoder, (i) uses modality-specific tokenizers to account for different spatiotemporal characteristics of these sensors, and (ii) caches modality-specific tokens at inference time to process new measurements as they come. This architecture (i) is fast (6.68 ms and 112 ms on NVIDIA 5090 and Orin NX respectively, to compute the representation), (ii) performs better than existing image-only foundation models on tasks such as estimation of optical flow, depth, semantic segmentation, and ego-motion (translation, rotation, and steering angle), and (iii) predicts robustly at nighttime or in situations where sensory data is degraded. See our project page for links to the dataset, code, and supplementary videos: https://abisulco.com/octosense/.

**Why this may be relevant:**

It may help track foundation-model directions for Earth observation or geospatial AI. It may be useful for LiDAR-based tree inventory, urban structure mapping, or 3D geospatial analysis.

---

### 3. Flood Mapping from RGB imagery using a Vision Foundation Model

**Authors:** Vladyslav Polushko, Tilman Bucher, Ronald Rosch, Thomas Marz, M. Rauhut, Andreas Weinmann

**Published:** 2026-06-23

**Found via:** Semantic Scholar

**My Score:** 60

**Venue importance score included:** 0

**Semantic Scholar citations:** 0

**arXiv ID:** 2606.24120

**Paper link:** https://www.semanticscholar.org/paper/14a2752ef2b3a4c7de8473645d87c15f50c4af9a

**Abstract:**

Timely, high-resolution maps of flood extent around settlements are essential for emergency response and damage assessment. We consider airborne RGB imagery for flood mapping as it can be collected rapidly at low cost. To produce flood maps, deep learning models for water segmentation are often used. CNN based and small vision transformer models are used. However, they need much data for adaptation to a change of scenery, i.e., another flooding event. Vision foundation models or large vision transformers are known to generalize across domains. Recently, foundation models for Earth observation became available. They are pretrained on satellite data, whose spatial resolution, viewing geometry, and radiometry differ from nadir RGB imagery. Thus, adaptation is required. We investigate how a satellite-pretrained Earth observation foundation model can be adapted to centimeter-scale floodwater mapping from RGB imagery. Specifically, we fine-tune a model we call Prithvi-2.0-UPN consisting of the Prithvi-EO-2.0-600M Vision Transformer combined with a UPerNet decoder for binary water segmentation on two RGB datasets (BlessemFlood21, NeuenahrFlood). In a first experiment we observe that Prithvi-2.0-UPN reaches state-of-the-art results on BlessemFlood21 and NeuenahrFlood, when trained on their datasets. In a second experiment we show that Prithvi-2.0-UPN performs better than state-of-the-art baseline models for transfer to a new flood event (trained on BlessemFlood21, tested on NeuenahrFlood) in a zero-shot setting. However, the performance indicates room for improvement. In this respect, we investigate in a third experiment how performance improves when further fine-tuning the models with small shares of NeuenahrFlood training data: Prithvi-2.0-UPN improves the fastest and reaches almost the performance level when fully trained on NeuenahrFlood, indicating transfer capabilities.

**Why this may be relevant:**

It may help track foundation-model directions for Earth observation or geospatial AI. It is directly related to remote sensing or Earth observation workflows.

---

### 4. SelectAnyTree: A Promptable Instance Segmentation Model for 3D Forest LiDAR Point Clouds

**Authors:** Trung Thanh Nguyen, Daniel Lusk, Kilian Gerberding, Janusch Vajna-Jehle, Tuan-Anh Vu, Duc Viet Le, Tu Vo, Phi Le Nguyen

**Published:** 2026-06-25

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 60

**Venue importance score included:** 0

**arXiv ID:** 2606.27491v1

**Paper link:** http://arxiv.org/abs/2606.27491v1

**PDF link:** https://arxiv.org/pdf/2606.27491v1

**Abstract:**

Automated instance segmentation of forest LiDAR point clouds is increasingly critical as forest monitoring moves toward scalable, detailed, 3D measurement. Yet, progress is constrained by label scarcity for tree instances; a single hectare can hold millions of points and hundreds of overlapping, complex crowns, making manual annotation from scratch with raw data laborious and error-prone. Annotations are often corrected from automatic pre-segmentations, but remain costly as these provide no interactive or AI-assisted refinement. Inspired by the promptable paradigm of foundation segmentation models, we propose SelectAnyTree, a promptable instance segmentation model that delineates any individual tree in a 3D forest point cloud from a few clicks. It introduces two key components: Click-to-query prompt encoder and Canopy Height Model (CHM)-guided first prompt. The former turns each click into a single content query, encoding its 3D position and positive/negative polarity together with a pooled local backbone feature. The latter provides treetops as a geometry- and ecologically guided first prompt without any user input. The resulting prompt query is then decoded into one tree mask by a state-space query decoder to efficiently capture long-range context in large-scale forest scenes with linear-time complexity. We evaluate SelectAnyTree in interactive and instance-level settings across seven diverse forest regions and an independent held-out test dataset, demonstrating strong generalization beyond the training domains. It segments a target tree to 78.2 Intersection over Union (IoU) from a single click, 24.8 points above the strongest promptable baseline, and reaches every accuracy target with the fewest clicks, while using far fewer parameters and less inference time than prior promptable models. The source code is available at https://github.com/thanhhff/SelectAnyTree.

**Why this may be relevant:**

It may be useful for LiDAR-based tree inventory, urban structure mapping, or 3D geospatial analysis. It connects to urban tree detection, canopy mapping, or vegetation analysis. It may help with cross-city, cross-region, or cross-sensor generalization.

---

### 5. GenWorld: Empirically Grounded Urban Simulation Infrastructure for Scalable LLM-Agent Studies

**Authors:** Gen Li, Jieyuan Lan, Pengcheng Xu, Zongyuan Wu, Masaki Ogura, Tao Feng

**Published:** 2026-06-26

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 47

**Venue importance score included:** 0

**arXiv ID:** 2606.27650v1

**Paper link:** http://arxiv.org/abs/2606.27650v1

**PDF link:** https://arxiv.org/pdf/2606.27650v1

**Abstract:**

LLM-agent simulation faces a joint grounding and scaling problem: agents should act in environments that reflect real urban constraints, yet direct online LLM calls for city-scale populations are computationally prohibitive. We present GenWorld, an empirically grounded urban simulation infrastructure that combines a building-level synthetic city, a structured agent-environment interface, and offline compilation of LLM-derived decision signals into lookup policies for scalable rollout. In a reference instantiation for Higashihiroshima, Japan, GenWorld grounds 196,608 synthetic residents in census and geospatial data, validates demographic consistency against census tabulations, and uses YJMob100K mobile-phone data as a commuting-distance diagnostic. We demonstrate the infrastructure through three reproducible cases: a full-city weekday rollout, a weekday-weekend behavioral contrast, and a warning-response perturbation with auditable replanning traces. These cases support GenWorld as a reproducible platform for grounded and scalable LLM-agent studies, while calibrated forecasting for traffic, evacuation, or policy outcomes remains future work.

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis. It is related to urban planning, infrastructure, or built-environment analysis.

---

### 6. RSICCLLM: A Multimodal Large Language Model for Remote Sensing Image Change Captioning

**Authors:** Yelin Wang, Zijia Song, Shuo Ye, Chuanguang Yang, Miaoyu Wang, Yong Xu, Zhulin An, Yongjun Xu

**Published:** 2026-06-26

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 42

**Venue importance score included:** 0

**arXiv ID:** 2606.28266v1

**Paper link:** http://arxiv.org/abs/2606.28266v1

**PDF link:** https://arxiv.org/pdf/2606.28266v1

**Abstract:**

Remote Sensing Image Change Captioning (RSICC) aims to describe changes between bi-temporal remote sensing images and holds significant research and application value. However, most existing methods rely on conventional deep learning architectures, and the limited model capacity constrains performance. Although large-model post-training techniques have achieved great success in general domains, their direct transfer to RSICC remains challenging due to data scarcity and the need for fine-grained change understanding. To address this, we propose RSICCLLM, the first post-training framework for large vision-language models in RSICC. Specifically, we design a data generation paradigm, release the instruction dataset RSICI, and establish a task-specific RSICC benchmark. We further introduce Difference-aware Supervised Fine-tuning to explicitly extract change representations and guide the model in perceiving and understanding temporal differences. In addition, we propose Dual-Negative Preference Optimization (DNPO), which employs two complementary negative-sample construction strategies to construct the preference dataset RSICP and further refine model performance. Extensive experiments validate the superior capability of RSICCLLM, which achieves outstanding results with only 7B parameters, surpassing models of substantially larger scales. The code and dataset will be made publicly available at https://github.com/keaill/RSICCLLM.

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis. It is directly related to remote sensing or Earth observation workflows.

---

### 7. Mind the Gap: Quantifying the Domain Gap in Cross-Sensor Diffusion Super-Resolution

**Authors:** Dawid Kopeć, Katarzyna Jabłońska, Wojciech Kozłowski, Maciej Zięba

**Published:** 2026-06-26

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 39

**Venue importance score included:** 0

**arXiv ID:** 2606.28039v1

**Paper link:** http://arxiv.org/abs/2606.28039v1

**PDF link:** https://arxiv.org/pdf/2606.28039v1

**Abstract:**

Demand for high-resolution satellite imagery has increased interest in super-resolution (SR) to bridge the spatial resolution gap between freely available missions such as Sentinel-2 and commercial systems like PlanetScope. Because no sensor provides true paired low- and high-resolution observations, SR models are usually trained on synthetically degraded data, creating a domain gap on real cross-sensor imagery. In this work, we provide the first systematic study of how this synthetic-to-real mismatch affects the performance of modern diffusion-based SR models. Using a large, geometrically and temporally aligned dataset of Sentinel-2 and PlanetScope imagery, we evaluate five state-of-the-art diffusion architectures under controlled experimental settings. We also introduce LPIPS-Sat, a domain-adapted perceptual metric based on Sentinel-2 self-supervised features. Our results show two persistent challenges: synthetically trained models degrade sharply on real pairs, while models trained on real cross-sensor data exhibit optimisation difficulties and struggle to adapt to the physical and radiometric diversity. These findings highlight a key limitation of current SR and motivate methods that disentangle super-resolution from domain adaptation.

**Why this may be relevant:**

It is directly related to remote sensing or Earth observation workflows. It may help with cross-city, cross-region, or cross-sensor generalization.

---

### 8. Contextual Associations Between Webpage Elements for Web Accessibility: An Empirical Study

**Authors:** Kishan Rakesh, Shiyi Wei

**Published:** 2026-06-25

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 32

**Venue importance score included:** 0

**arXiv ID:** 2606.27506v1

**Paper link:** http://arxiv.org/abs/2606.27506v1

**PDF link:** https://arxiv.org/pdf/2606.27506v1

**Abstract:**

[Context] Screen reader users navigating webpages by element list often encounter accessible names such as "Read more" that are valid under the W3C Accessible Name and Description Computation specification but uninterpretable in isolation. The surrounding elements that would make these names meaningful exist in the page but are not linked to the target by any mechanism. No prior work has empirically studied how to select which surrounding elements are contextually relevant to a given target. [Objective] This registered report investigates whether human-perceived contextual associations between webpage elements can be recovered from the accessibility tree using link prediction, and whether the learned associations generalize across websites. [Method] We will construct a dataset of human-annotated contextual associations on 35 websites, stratified across the Tranco top-million list, with three independent annotators per page. Each page is represented as a graph derived from its accessibility tree, augmented with spatial and semantic features from the DOM and CSS. We compare four machine learning models (MLP, GCN, GAT, and SEAL) against two heuristic baselines under leave-one-site-out cross-validation with a pre-registered statistical framework, using Hit@K and MRR. [Results] We have conducted a five-site author-annotated pilot study to establish the pipelines and parameterize the power simulation, with pilot Hit@10 ranging from 0.16 to 0.85 across four learned models and 0.08 to 0.30 across two heuristic baselines. The final results will be reported after the planned experiments and analyses are completed. [Conclusion] The study contributes a human-annotated dataset of contextual associations on webpages, an empirical evaluation of link prediction for context selection on accessibility-tree graphs, and a cross-site generalization analysis.

**Why this may be relevant:**

It connects to urban tree detection, canopy mapping, or vegetation analysis. It may help with cross-city, cross-region, or cross-sensor generalization.

---

### 9. Drop-Then-Recovery: How Redundant Are Vision-Language-Action Models?

**Authors:** Guoheng Sun, Kaixi Feng, Shwai He, Xiaochuan Gong, Yexiao He, Ziyao Wang, Zheyu Shen, Wanghao Ye

**Published:** 2026-06-26

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 26

**Venue importance score included:** 0

**arXiv ID:** 2606.27755v1

**Paper link:** http://arxiv.org/abs/2606.27755v1

**PDF link:** https://arxiv.org/pdf/2606.27755v1

**Abstract:**

Vision-Language-Action (VLA) models enable instruction-driven robotic manipulation, but they inherit oversized language backbones from pretrained VLMs whose capacity far exceeds what is needed for short robotic instructions. This raises a basic question: how much of a VLA model is actually necessary for closed-loop control? In this work, we study architectural redundancy in VLA models by using transformer block removal as a controlled intervention. We introduce \textbf{Drop-Then-Recovery (DTR)}, an analysis protocol that removes selected blocks from a pretrained VLA model and then fine-tunes the resulting model to measure whether the removed capacity was necessary for downstream control. To make this intervention reliable, we propose \textbf{GateProbe}, a one-shot virtual-gate sensitivity metric that ranks blocks by their contribution to the downstream action loss. Across multiple VLA architectures, manipulation benchmarks and even real-robot industrial scenarios, we find a strong asymmetry in post-removal recoverability: \ul{\textit{language backbones are highly redundant for standard robotic manipulation tasks, whereas vision and action pathways are substantially less tolerant to removal}}. On LIBERO, removing half of the LLM blocks even improves OpenVLA-OFT from 95.0% to 98.3% under the same downstream fine-tuning budget, and retaining only two language blocks still recovers baseline-level performance. These results suggest that current VLA benchmarks may exert limited pressure on deep language grounding and compositional instruction understanding, and that future VLA architectures should allocate capacity more deliberately across language, vision, and action components. The code is available at https://github.com/s1ghhh/VLADrop.

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis. It may be useful for multimodal geospatial understanding using image-text models.

---

### 10. Unleashing Infinite Motion: Scaling Expressive Quadrupedal Motion via Generative Video Priors

**Authors:** Youzhi Liu, Li Gao, Yifei Qian, Liu Liu, Yang Cai, Ziqiao Li

**Published:** 2026-06-26

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 23

**Venue importance score included:** 0

**arXiv ID:** 2606.28237v1

**Paper link:** http://arxiv.org/abs/2606.28237v1

**PDF link:** https://arxiv.org/pdf/2606.28237v1

**Abstract:**

Quadruped robots have achieved remarkable locomotion, yet their behavioral repertoire remains confined to a few gaits--far from the expressive, companion-like presence long envisioned for them. Attempts to import the humanoid recipe of large-scale motion data have inherited one tacit assumption: that robot motion must first pass through an animal body, making data collection dependent on cooperative animals, reconstruction fragile across species, and retargeting ill-posed across incompatible morphologies. We propose Uni-Mo, a fully automated pipeline that removes the animal from the loop by reframing data scarcity as a generation problem: an LLM proposes motion prompts, a video diffusion model synthesizes the corresponding robot behaviors, and the generated videos are lifted into 3D reference trajectories used to train tracking policies deployed on a real Unitree Go2. To make naively-drifting generations reliably extractable, we introduce an Identity Consistency Loss that enforces appearance coherence across frames. We release Quad-Imaginarium at https://github.com/GaoLii/Quad-Imaginarium.git, the resulting open-source dataset of 7,488 language-annotated quadruped motions (18.5 hours) spanning acrobatic and performative behaviors. We validate 392 randomly sampled motions on a real Unitree Go2 with a 96.7% deployment success rate, complemented by a 97.6% success rate across the full dataset in simulation.

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis. It connects to urban tree detection, canopy mapping, or vegetation analysis.

---

