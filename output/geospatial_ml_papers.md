# Weekly Geospatial ML Papers

**Search window:** 2026-05-13 to 2026-05-20

**Sources:** arXiv and Semantic Scholar

**Total selected papers:** 10

This digest focuses on geospatial analysis, urban climate, urban planning, infrastructure, and geospatial problem-solving using ML, computer vision, LLMs, VLMs, foundation models, self-supervised learning, and related methods.

Only papers from the selected top journals, conferences, or workshops are included by default. The venue importance score is included in **My Score**.

## Top Papers

### 1. MetaEarth-MM: Unified Multimodal Remote Sensing Image Generation with Scene-centered Joint Modeling

**Authors:** Zhiping Yu, Chenyang Liu, Jinqi Cao, Qinzhe Yang, Siwei Yu, Zhengxia Zou, Zhenwei Shi

**Published:** 2026-05-19

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 58

**Venue importance score included:** 0

**arXiv ID:** 2605.20090v1

**Paper link:** http://arxiv.org/abs/2605.20090v1

**PDF link:** https://arxiv.org/pdf/2605.20090v1

**Abstract:**

Multi-modal remote sensing images are vital for Earth observation, yet complete paired observations are often scarce in practice. Existing generative methods commonly address this problem through isolated pairwise modality translation, but their versatility and scalability remain limited as the number of modalities and generation tasks increases. Here, we develop a generative foundation model MetaEarth-MM for multi-modal remote sensing imagery, enabling paired joint generation and any-to-any translation across five modalities within a unified model. Recognizing the intrinsic scene consistency underlying multi-modal observations, we introduce a scene-centered joint modeling paradigm in MetaEarth-MM. Unlike previous methods that rely on direct appearance-level cross-modal mapping, our model organizes the generation around the underlying scene content. Specifically, MetaEarth-MM adopts a decoupled architecture that first infers a latent scene representation from available observations, and then generates target modalities conditioned on this intermediate state. To support training, we further construct EarthMM, a large-scale dataset comprising 2.8 million multi-resolution global images with 2.2 million aligned pairs. Extensive experiments demonstrate that MetaEarth-MM not only exhibits strong generative capability and robust generalization across diverse generation tasks, but also supports downstream tasks at both data and representation levels, highlighting its potential as a general foundation model for cross-modal Earth observation. The code and dataset will be available at https://github.com/YZPioneer/MetaEarth-MM.

**Why this may be relevant:**

It may help track foundation-model directions for Earth observation or geospatial AI. It is directly related to remote sensing or Earth observation workflows. It may help with cross-city, cross-region, or cross-sensor generalization.

---

### 2. GeoX: Mastering Geospatial Reasoning Through Self-Play and Verifiable Rewards

**Authors:** Kyeongjin Ahn, Seungeon Lee, Krishna P. Gummadi, Meeyoung Cha

**Published:** 2026-05-19

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 47

**Venue importance score included:** 0

**arXiv ID:** 2605.20006v1

**Paper link:** http://arxiv.org/abs/2605.20006v1

**PDF link:** https://arxiv.org/pdf/2605.20006v1

**Abstract:**

Geospatial reasoning requires solving image-grounded problems over the complex spatial structure of a scene. However, developing this capability is hindered by the cost of annotating a vast and combinatorial question space. We propose GeoX, a self-play framework that acquires spatial logic through executable programs that yield verifiable rewards, without relying on large-scale human-curated data Given a satellite or aerial image, our framework employs a single multimodal policy that proposes spatial problems as executable programs and solves them under three reasoning modes-abduction, deduction, and induction-over spatial primitives and an image understanding tool. A verifier executes each program to covert a reward signal that jointly optimizes the two roles via reinforcement learning. GeoX consistently improves its base VLMs by up to 5.5 points on average, matching or exceeding conventional baselines trained on millions of curated data. Along-side the proposed method, we release a benchmark for geospatial understanding accumulated through self-play.

**Why this may be relevant:**

It may be useful for multimodal geospatial understanding using image-text models. It is directly related to remote sensing or Earth observation workflows.

---

### 3. deadtrees.earth-aerial: A Multi-Resolution Aerial Image Dataset for Tree Cover and Mortality Detection

**Authors:** Ayushi Sharma, Clemens Mosig, Lukas Drees, Salim Soltani, Janusch Vajna-Jehle, Aaron Sheppard, Belqis Ahmadi, Jonathan Schmid

**Published:** 2026-05-19

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 46

**Venue importance score included:** 0

**arXiv ID:** 2605.19605v1

**Paper link:** http://arxiv.org/abs/2605.19605v1

**PDF link:** https://arxiv.org/pdf/2605.19605v1

**Abstract:**

Forests worldwide are increasingly threatened by climate change and disturbances such as fire, pests, and pathogens, creating an urgent need for scalable monitoring of tree cover and tree mortality. Aerial imagery from drones and aircraft is a key data source for detailed and large-scale mapping of tree crowns and mortality. However, related progress is limited by the lack of globally representative, harmonized datasets for joint segmentation of tree cover and mortality. We introduce two novel, open, machine-learning-ready datasets to enable joint segmentation of tree cover and tree mortality from centimeter-scale aerial imagery for the first time at global scales. With DTE-aerial-train, we provide a training dataset comprising 385K image patches of size 1024x1024 pixels, with resolutions ranging from 2.5 to 20 cm. It includes multi-class expert-annotated and -audited pseudo-labels for tree cover and mortality. With DTE-aerial-bench, we provide a geographically balanced benchmark test set of 25 globally distributed orthoimages totaling 525 patches with high-quality expert annotations for both tree cover and mortality. Both the training and benchmark datasets span tropical, temperate, boreal, and dryland biomes and cover a wide range of forest structures and mortality patterns. Using the benchmark test set for evaluation, we establish strong reference baselines that improve mortality segmentation across all biomes and scales with significant gains in challenging regions, such as boreal forests, where the F1 score increases from 0.40 to 0.58 with around 45% relative improvement. All data, models, and code will be publicly released under permissive open-source licenses. An interactive visualization of the benchmark dataset is available at deadtrees.earth/releases/dte-aerial-bench.

**Why this may be relevant:**

It connects to urban tree detection, canopy mapping, or vegetation analysis.

---

### 4. Smartphone-based Circular Plot Sampling for Forest Inventory

**Authors:** Su Sun, Jui-Cheng Chiu, Nabin Khanal, Songlin Fei, Yingjie Victor Chen

**Published:** 2026-05-19

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 44

**Venue importance score included:** 0

**arXiv ID:** 2605.19213v1

**Paper link:** http://arxiv.org/abs/2605.19213v1

**PDF link:** https://arxiv.org/pdf/2605.19213v1

**Abstract:**

Circular sample plots are a cornerstone of forest inventory, yet accurate measurement of tree diameter at breast height (DBH) and spatial location within such plots remains challenging. Conventional approaches rely either on costly terrestrial LiDAR systems or labor-intensive manual methods involving calipers and compass bearings, limiting their scalability and accessibility in large scale environments. We present a lightweight, smartphone-based pipeline that enables complete plot sampling based tree measurement from a single walkthrough video, requiring no specialized hardware beyond a consumer smartphone mounted on a portable stand. The proposed method integrates pretrained monocular depth estimation and tree instance segmentation with a simultaneous localization and mapping (SLAM) framework to jointly refine camera trajectories and depth across the video sequence. Tree positions and DBH estimates are recovered by fusing SLAM-derived camera poses with segmented depth maps, with absolute real-world scale anchored via a calibrated reference length. The system was evaluated in both managed forest plots and natural forest plot, achieving a mean absolute error of 1.51 cm (MARE 3.98%) and 2.30 cm (MARE 5.69%) respectively, with consistent performance across varying starting directions and positions. Cross-video consistency analysis further demonstrated stable and reproducible tree localization across measurements initiated from different starting positions. The proposed approach achieves accuracy comparable to established field methods while substantially reducing equipment cost and operational complexity, making it accessible to both professional researchers and non-expert forest managers in diverse operational settings.

**Why this may be relevant:**

It may be useful for LiDAR-based tree inventory, urban structure mapping, or 3D geospatial analysis. It connects to urban tree detection, canopy mapping, or vegetation analysis.

---

### 5. PixVerve: Advancing Native UHR Image Generation to 100MP with a Large-Scale High-Quality Dataset

**Authors:** Haojun Chen, Haoyang He, Chengming Xu, Qingdong He, Junwei Zhu, Yabiao Wang, Zhucun Xue, Xianfang Zeng

**Published:** 2026-05-19

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 35

**Venue importance score included:** 0

**arXiv ID:** 2605.20147v1

**Paper link:** http://arxiv.org/abs/2605.20147v1

**PDF link:** https://arxiv.org/pdf/2605.20147v1

**Abstract:**

Text-to-Image (T2I) models have recently seen notable progress around 1K and 2K resolution. With the extreme desire for better visual experience and the rapid development of imaging technology, the demand for Ultra-High-Resolution (UHR) image generation has grown significantly. However, UHR image generation poses great challenges due to the scarcity and complexity of high-resolution content. In this paper, we first introduce PixVerve-95K, a high-quality, open-source UHR T2I dataset curated with a carefully designed data pipeline, which contains 95K images across diverse scenarios (each image has a minimum pixel-count of 100M) and seven-dimensional annotations. Based on our large-scale image-text dataset, we take a pioneering step to extend various T2I foundation models to native 100MP generation with three training schemes. Finally, leveraging both conventional metrics and multimodal large language model-based assessments, our proposed PixVerve-Bench benchmark establishes a comprehensive evaluation protocol for UHR images encompassing visual quality and semantic alignment. Extensive experimental results on our benchmark and the constructive exploration of training strategies collaboratively provide valuable insights for future breakthroughs.

**Why this may be relevant:**

It may help track foundation-model directions for Earth observation or geospatial AI. It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis.

---

### 6. Towards Trust Calibration in Socially Interactive Agents: Investigating Gendered Multimodal Behaviors Generation with LLMs

**Authors:** Lucie Galland, Chloé Clavel, Magalie Ochs

**Published:** 2026-05-19

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 29

**Venue importance score included:** 0

**arXiv ID:** 2605.19798v1

**Paper link:** http://arxiv.org/abs/2605.19798v1

**PDF link:** https://arxiv.org/pdf/2605.19798v1

**Abstract:**

As Socially Interactive Agents (SIAs) become increasingly integrated into daily life, the ability to calibrate user trust to an agent's actual capabilities would help ensure appropriate usage of these agents. In this paper, we explore the capacity of Large Language Models (LLMs) to generate multimodal behaviors (verbal, vocal, gestural, and facial expression modalities) that reflect varying levels of ability and benevolence, two key dimensions of trustworthiness. We propose a novel method for automatically generating behaviors aligned with specific levels of these traits, a first step towards enabling nuanced and trust-calibrated interactions. By analyzing a large dataset of multimodal transcripts generated by LLMs, we demonstrate that GPT-5.4 is able to produce coherent behavior across different modalities (text, intonation, facial expression, and gesture). Using Random Forest feature importance analysis, we show that the generated behaviors align with theoretical expectations for ability and benevolence. However, we also find that when gender is specified in the prompt, LLMs tend to reproduce societal gender stereotypes, associating male agents' behaviors with high ability and female agents' behaviors with high benevolence. To validate our approach, we conducted a user study on Prolific using a within-subjects design. Participants perceived different levels of ability and benevolence in the generated behaviors align with the intended instructions.

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis.

---

### 7. StruMPL: Multi-task Dense Regression under Disjoint Partial Supervision and MNAR Labels

**Authors:** Reza M. Asiyabi, Juan Alberto Molina-Valero, The SEOSAW Partnership, Steven Hancock, Casey M. Ryan

**Published:** 2026-05-19

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 27

**Venue importance score included:** 0

**arXiv ID:** 2605.19931v1

**Paper link:** http://arxiv.org/abs/2605.19931v1

**PDF link:** https://arxiv.org/pdf/2605.19931v1

**Abstract:**

Estimating forest aboveground biomass (AGB) from Earth observation combines two structurally incompatible label sources: spaceborne lidar provides canopy structure at millions of locations but no biomass estimate, and ground-based plots provide biomass at thousands of biased locations but no metrics of structure. No single training sample carries labels for all target variables, plot labels are missing not at random (MNAR), and biomass is linked to the structural variables by known but biome-specific allometric laws. We formalise this as multi-task dense regression under heterogeneous disjoint partial supervision with MNAR labels and inter-task physical constraints, and propose StruMPL to address it jointly. A shared encoder feeds per-variable regression, imputation, and propensity heads for spatial MNAR correction, and a learnable physics module that evaluates the inter-task constraint on the model's own predictions at every pixel. The supervised loss uses an Augmented IPW (AIPW) pseudo-outcome with stop-gradients on the propensity and on the imputation baseline; we show analytically and empirically that both are necessary for joint optimisation to recover IPW-weighted stationary points while keeping the loss bounded. On two ecologically distinct biomes, StruMPL outperforms ablation variants and the closest published method on AGB RMSE and bias, with a stratified analysis showing AIPW reduces high-AGB bias by ~54%.

**Why this may be relevant:**

It is directly related to remote sensing or Earth observation workflows. It may be useful for LiDAR-based tree inventory, urban structure mapping, or 3D geospatial analysis. It connects to urban tree detection, canopy mapping, or vegetation analysis.

---

### 8. Graph Neural Networks for Community Detection in Graph Signal Analysis

**Authors:** Roberto Cavoretto, Alessandra De Rossi, Enrico Montini

**Published:** 2026-05-19

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 26

**Venue importance score included:** 0

**arXiv ID:** 2605.19733v1

**Paper link:** http://arxiv.org/abs/2605.19733v1

**PDF link:** https://arxiv.org/pdf/2605.19733v1

**Abstract:**

Community detection is a central problem in graph analysis, with applications ranging from network science to graph signal processing. In recent years, Graph Neural Networks (GNNs) have emerged as effective tools for learning low-dimensional representations of graph-structured data and have shown strong performance in clustering tasks, particularly on large and high-dimensional graphs. This paper investigates the use of GNN-based community detection within a graph signal interpolation framework. After reviewing the main classes of GNN architectures for community detection according to a standard taxonomy, we integrate the resulting graph communities into a Partition of Unity Method (PUM) for interpolation with Graph Basis Functions (GBFs). In this approach, GNN-derived communities are used to construct local subdomains on which GBF interpolants are computed and subsequently combined into a global approximation. Numerical experiments on benchmark %graph datasets, including geometric and urban network examples demonstrate that the proposed combination of GNN-based clustering and GBF-PUM interpolation yields accurate signal reconstructions. The results indicate that deep learning-based community detection can provide effective graph partitions for localized interpolation schemes, supporting its use in scalable graph signal analysis.

**Why this may be relevant:**

It matched the geospatial machine learning search criteria and may be worth screening.

---

### 9. Ensembling Tabular Foundation Models - A Diversity Ceiling And A Calibration Trap

**Authors:** Aditya Tanna, Yash Desai, Pratinav Seth, Mohamed Bouadi, Nassim Bouarour, Vinay Kumar Sankarapu

**Published:** 2026-05-18

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 24

**Venue importance score included:** 0

**arXiv ID:** 2605.18696v1

**Paper link:** http://arxiv.org/abs/2605.18696v1

**PDF link:** https://arxiv.org/pdf/2605.18696v1

**Abstract:**

Tabular foundation models (TFMs) now match or beat tuned gradient-boosted trees on a growing fraction of tabular tasks, but no single TFM wins on every dataset. Ensembling is the go to fix here, and it works less well than expected. Six modern TFMs form a near-redundant pool: their mean pairwise Q-statistic is $0.961$, close enough to $1$ that any convex combination is bounded above. We benchmark six ensemble strategies over six TFMs on 153 OpenML classification tasks. The best ensemble, two-level cascade stacking, buys $+0.18\%$ accuracy over the strongest single TFM at $253\times$ the compute. A Friedman and Nemenyi analysis places three ensembles and the best base TFM in a single equivalence group; three other ensembles are significantly \emph{worse} than the best base. Stacking with a logistic-regression meta-learner is the most striking case: competitive accuracy and ROC-AUC, the worst log-loss rank among the ensembles. The meta-learner improves accuracy by sharpening class boundaries, which destroys calibration. We recommend greedy selection as the practical default.

**Why this may be relevant:**

It may help track foundation-model directions for Earth observation or geospatial AI. It connects to urban tree detection, canopy mapping, or vegetation analysis.

---

### 10. Deep Tech to Space: Space Data Centers and AI Revolution at the Edge

**Authors:** Jonas Weiss, Patricia Sagmeister, Gabriel Maiolini Capez, Dinesh Verma, Roberto Garello, Alberto Perotti, Dawid Lazaj, Alicja Musial

**Published:** 2026-05-19

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 20

**Venue importance score included:** 0

**arXiv ID:** 2605.19892v1

**Paper link:** http://arxiv.org/abs/2605.19892v1

**PDF link:** https://arxiv.org/pdf/2605.19892v1

**Abstract:**

Dramatic cost reductions driven by private sector innovations have led to a rapid increase in the number of satellites in orbit and a corresponding surge in space-generated data. As this trend continues, transmitting large volumes of data to Earth for processing may become increasingly costly and challenging due to potential space-to-Earth link congestion and increased latency. Moreover, traditional ground station networks may face difficulties accommodating growing data flows and workloads because of capacity constraints, complex scheduling logistics, and restricted visibility windows, which can limit scalability. Space Data Centers (SDCs) -- software-driven, multi-tenant artificial intelligence-based service platforms capable of processing data in orbit to generate actionable insights for client satellites and ground users -- represent a promising approach to address these challenges. This article presents the architecture of a Low Earth Orbit SDC satellite constellation, considering orbital design, inter-satellite links and network topology, computational resource organization, and software service orchestration. We analyze the potential technical feasibility and economic viability of SDCs using forecasting models informed by technology roadmaps and illustrate the concept through Earth observation and lunar exploration use cases.

**Why this may be relevant:**

It is directly related to remote sensing or Earth observation workflows.

---

