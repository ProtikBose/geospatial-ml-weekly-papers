# Weekly Geospatial ML Papers

**Search window:** 2026-08-10 to 2026-08-17

**Sources:** arXiv and Semantic Scholar

**Total selected papers:** 10

This digest focuses on geospatial analysis, urban climate, urban planning, infrastructure, and geospatial problem-solving using ML, computer vision, LLMs, VLMs, foundation models, self-supervised learning, and related methods.

Only papers from the selected top journals, conferences, or workshops are included by default. The venue importance score is included in **My Score**.

## Top Papers

### 1. Greening Public Infrastructure for Local Climate Resilience: A Case Study of the Mount Vernon District in Virginia

**Authors:** Younsung Kim, Colin Chadduck

**Published:** 2026-08-14

**Venue:** Urban Science

**Found via:** Semantic Scholar

**My Score:** 110

**Venue importance score included:** 0

**Semantic Scholar citations:** 0

**DOI:** 10.3390/urbansci10080468

**Paper link:** https://www.semanticscholar.org/paper/6c5205388e070eb19f0cf16c91b8377ff36799de

**PDF link:** https://doi.org/10.3390/urbansci10080468

**Abstract:**

Urban climate risks, particularly extreme heat and flooding, increasingly threaten public infrastructure in rapidly urbanizing regions. Public schools represent critical community assets, yet their spatial planning often overlooks the role of natural capital in mitigating environmental risks. This study examines the intersection of natural capital and urban design through a case study of public schools in the Mount Vernon District of Fairfax County, Virginia. Using cartographic modeling and spatial analysis, the study assesses school-site exposure to urban heat island effects and localized flood risks by integrating geospatial data on land cover, surface temperature, and hydrological conditions. Results indicate that all analyzed school sites exhibit notable vulnerability to both heat exposure and flooding. The findings highlight the importance of incorporating natural capital—such as expanded tree canopy, green infrastructure, and permeable surfaces—into school site planning to enhance climate resilience and environmental quality.

**Why this may be relevant:**

It connects to urban tree detection, canopy mapping, or vegetation analysis. It is relevant to urban climate and heat-resilience research. It is related to urban planning, infrastructure, or built-environment analysis.

---

### 2. From crown candidates to neighborhood screening: integrating optical GeoAI and spatial modeling for urban-canopy assessment in Davis, California

**Authors:** Mohammadreza Narimani, Shreyan Mitra, Parastoo Farajpoor

**Published:** 2026-08-14

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 50

**Venue importance score included:** 0

**arXiv ID:** 2608.13856v1

**Paper link:** http://arxiv.org/abs/2608.13856v1

**PDF link:** https://arxiv.org/pdf/2608.13856v1

**Abstract:**

Timely urban-canopy information is essential for linking remote sensing with heat, mobility, and neighborhood planning. We developed an optical GeoAI workflow for Davis, California, using 2022 National Agriculture Imagery Program imagery (0.6 m RGB+NIR). DeepForest generated crown candidates; an NDVI threshold, non-maximum suppression, and box-prompted Segment Anything Model (ViT-B) produced a crown-anchored canopy surface. Analyses used the 25.92 km2 Census TIGER municipal boundary and a 100 m grid. The workflow retained 11,741 candidate crowns and mapped 2.43 km2 of canopy (9.37% of the city). On the identical extent, 87.8% of mapped canopy pixels and 97.4% of candidate centers agreed with the 2022 USDA/CAL FIRE LiDAR-assisted canopy product; the optical surface represented 34.2% of the reference canopy area (IoU 0.288; Dice 0.448). Approximately 49% of candidates occurred within 15 m of a road. Canopy was inversely associated with Landsat land-surface temperature (Spearman rho = -0.293; partial rho = -0.370 controlling for built probability), and spatial-lag modeling confirmed clear neighborhood structure. Two transparent attention surfaces combined canopy need with thermal and contextual indicators. The framework provides a reproducible, updateable screening layer that complements structural canopy products and municipal inventories while retaining assumptions, data provenance, and spatial diagnostics for planning interpretation.

**Why this may be relevant:**

It is directly related to remote sensing or Earth observation workflows. It may be useful for LiDAR-based tree inventory, urban structure mapping, or 3D geospatial analysis. It connects to urban tree detection, canopy mapping, or vegetation analysis. It is relevant to urban climate and heat-resilience research.

---

### 3. GhostPoint: Self-Supervised Representation Learning by Hallucinating Occluded LiDAR Structure

**Authors:** Mohamed Abdelsamad, Bin Yang, Michael Ulrich, Miao Zhang, Yakov Miron, Alexandru Paul Condurache, Abhinav Valada

**Published:** 2026-08-14

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 49

**Venue importance score included:** 0

**arXiv ID:** 2608.14428v1

**Paper link:** http://arxiv.org/abs/2608.14428v1

**PDF link:** https://arxiv.org/pdf/2608.14428v1

**Abstract:**

3D object detection from LiDAR point clouds is a core problem in autonomous driving. Recent advances in self-supervised learning (SSL) enable scalable pretraining and transfers well to per-point tasks such as semantic and panoptic segmentation, but transfer to 3D detection remains weaker. We analyze recent SSL methods and find that most objectives are defined only on measured LiDAR returns from visible surfaces, leaving occluded and unobserved regions unconstrained. This visible-surface bias can be sufficient for point-wise prediction, but 3D detection requires robustness to missing structure. To address this gap, we propose GhostPoint, an SSL framework that hallucinates latent features in local neighborhoods around discovered instances, generated via a novel instance voxel dilation. In GhostPoint, an encoder processes observed returns, and an additional predictor infers neighborhood representations from observed context. In addition to standard encoder-level supervision, we introduce a predictor-level supervision scheme on sampled voxels from generated neighborhoods. Specifically, observed (visible/masked) voxels match teacher-encoder targets, while unobserved voxels match teacher-predictor hallucinations. This design encourages the learned representation to explicitly model structure beyond observed returns. Extensive evaluations on nuScenes and Waymo demonstrate that our method achieves state-of-the-art performance, consistently improving downstream 3D detection, especially under sparse scans and limited labels.

**Why this may be relevant:**

It may be useful for LiDAR-based tree inventory, urban structure mapping, or 3D geospatial analysis.

---

### 4. FIRM: Fine-Grained Intra-Token Representation of Masks for Remote Sensing Reasoning Segmentation

**Authors:** Weidong Tang, Kaiyu Li, Yikai Wang, Yanan Wu, Haotian Gan, Shihong Wang, Xiangyong Cao

**Published:** 2026-08-14

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 42

**Venue importance score included:** 0

**arXiv ID:** 2608.13980v1

**Paper link:** http://arxiv.org/abs/2608.13980v1

**PDF link:** https://arxiv.org/pdf/2608.13980v1

**Abstract:**

Reasoning segmentation requires multimodal large language models (MLLMs) to translate implicit instructions into precise pixel-level masks. MLLMs encode an image as visual tokens, each of which merges a group of image patches. In remote sensing images, small targets, thin structures, and adjacent instances can occupy different parts of the same visual token. Assigning a single binary mask label to such a token loses its internal spatial structure, causing nearby targets to merge and object boundaries to become coarse. To bridge this representational gap, we introduce FIRM, a Fine-grained Intra-token Representation of Masks. For each visual token, FIRM predicts a mask code that specifies an $r\times r$ binary sub-cell pattern rather than a single foreground/background label. Given a target identified by the MLLM, the complete grid of mask codes is predicted in one mask pass. Fixed lookup converts the predicted codes into a discrete sub-cell mask, while marginalizing the code distribution yields a soft structural field. To further recover fine-grained boundaries within each sub-cell, we introduce a lightweight continuous renderer that refines this field using pre-merge visual features and image details. Across five reasoning and referring segmentation benchmarks on satellite and UAV images, FIRM achieves leading results, including $70.5/80.5$ gIoU/cIoU on LaSeRS and a $3.0$-point average gain on EarthReason. These results demonstrate the value of explicitly representing intra-token mask patterns for fine-grained MLLM segmentation.

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis. It is directly related to remote sensing or Earth observation workflows.

---

### 5. Can Language Models Understand mmWave Data? Benchmarking Large Language Models for mmWave Radar-Based Human Understanding

**Authors:** Jeongwan Shin, Jaehyeon Kim, Donguk Ko, Jaeho Choi

**Published:** 2026-08-14

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 41

**Venue importance score included:** 0

**arXiv ID:** 2608.14179v1

**Paper link:** http://arxiv.org/abs/2608.14179v1

**PDF link:** https://arxiv.org/pdf/2608.14179v1

**Abstract:**

Large language models (LLMs) have shown remarkable reasoning and generative capabilities, motivating their use as universal reasoning engines for perception. While modern approaches such as vision-language models (VLMs) have attempted to incorporate reasoning capabilities into visual sensing, the integration of LLMs with the millimeter-wave (mmWave) modality-despite its unique advantages under low light and occlusion-remains largely unexplored. The principal bottlenecks stem from the scarcity of radar language pairs, severe cross-dataset heterogeneity, and the absence of a foundational mmWave encoder. We address this gap through a minimal textualization interface that serializes each mmWave point cloud into concise natural language, allowing off-the-shelf LLMs to operate in a question answering (QA) setting. Building on this, we present mmWave-QA, the first benchmark for language-conditioned mmWave human perception. mmWave-QA aggregates heterogeneous public mmWave datasets and harmonizes them via calibration-aware preprocessing and global taxonomy alignment, while providing natural language QA. Spanning six scenarios and five QA tasks, the benchmark enables standardized evaluation across diverse mmWave hardware and experimental conditions, establishing a foundation for scalable research on mmWave-LLM integration. We further evaluate and analyze LLMs on our mmWave-QA, highlighting their zero-shot reasoning potential for radar perception, as well as their robustness under visual degradation.

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis. It may be useful for multimodal geospatial understanding using image-text models. It may be useful for LiDAR-based tree inventory, urban structure mapping, or 3D geospatial analysis.

---

### 6. IRGNN: Efficient Invariant Radar Graph Neural Network for Radar Point Cloud Object Detection

**Authors:** Xiao Guo, Wanke Xia, Lili Yang, Caicong Wu

**Published:** 2026-08-14

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 34

**Venue importance score included:** 0

**arXiv ID:** 2608.14394v1

**Paper link:** http://arxiv.org/abs/2608.14394v1

**PDF link:** https://arxiv.org/pdf/2608.14394v1

**Abstract:**

Perception is a fundamental component of autonomous driving systems. While LiDAR-based methods have achieved remarkable progress in object detection, their reliability can degrade under adverse weather conditions. Radar point clouds provide a robust alternative due to their resilience to bad weather and low-illumination scenarios. However, radar point clouds are typically sparse, unordered, and less informative than LiDAR data, making it challenging to directly apply existing LiDAR-based perception methods. To address these challenges, we propose IRGNN, an Invariant Radar Graph Neural Network for radar point cloud object detection. IRGNN first reconstructs radar point clouds into graph representations using translation- and rotation-invariant feature designs, enabling robust modeling of sparse radar measurements. It then employs an improved message passing neural network (MPNN) with residual connections and a virtual node layer to enhance local feature propagation and global context modeling. Finally, task-specific heads are applied to the learned graph representations for object classification and bounding box prediction. Experimental results on the RadarScenes dataset show that IRGNN outperforms existing radar-based object detection methods and achieves competitive performance. In addition, IRGNN significantly reduces computational cost and memory usage during inference, demonstrating its effectiveness and practical potential for efficient radar-based perception in autonomous driving.

**Why this may be relevant:**

It may be useful for LiDAR-based tree inventory, urban structure mapping, or 3D geospatial analysis.

---

### 7. Learning to Forecast Crop Growth from Earth Observation Data

**Authors:** Dominik Senti, Mehmet Ozgur Turkoglu, Michele Volpi, Helge Aasen

**Published:** 2026-08-14

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 29

**Venue importance score included:** 0

**arXiv ID:** 2608.14281v1

**Paper link:** http://arxiv.org/abs/2608.14281v1

**PDF link:** https://arxiv.org/pdf/2608.14281v1

**Abstract:**

Forecasting crop growth across agricultural landscapes is important for improving the productivity, resilience, and operational management of farming systems. In this work, we investigate whether Earth observation time series and meteorological drivers can be used to predict future canopy development at country scale. We focus on winter wheat and formulate crop growth prediction as forecasting future leaf area index (LAI) trajectories beyond the last available Sentinel-2 observation. We evaluate this task on a multi-year dataset which spans the entire country of Switzerland, containing over 20 million pixel-level Sentinel-2-derived LAI time series paired with meteorological variables. Because cloud cover and revisit gaps leave LAI supervision sparse, models fit the few valid (cloud-free) LAI observations yet oscillate implausibly between them, producing trajectories no real canopy could follow. We introduce a lightweight unimodal shape regulariser which improves trajectory plausibility with negligible loss in accuracy. We compare deep learning sequence-to-sequence (Seq2Seq) models with classic machine learning baselines and show that Seq2Seq models generalise well across years, achieving $\mathrm{R}^2$ above 0.8 and consistently outperforming conventional approaches. Together, these results demonstrate that remote sensing and weather-driven sequence modelling can learn crop growth dynamics at landscape scale. S

**Why this may be relevant:**

It is directly related to remote sensing or Earth observation workflows. It connects to urban tree detection, canopy mapping, or vegetation analysis. It is relevant to urban climate and heat-resilience research.

---

### 8. HiCo-GS: Hierarchical Context Aggregation and Geometric Consistency for Octree Gaussian Splatting

**Authors:** Wei Zhang, Shengkai Yu, Shiqiang Gong, Qi Zhang, Qiang Li, Qi Wang

**Published:** 2026-08-14

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 24

**Venue importance score included:** 0

**DOI:** 10.1145/3767308.3836546

**arXiv ID:** 2608.14136v1

**Paper link:** http://arxiv.org/abs/2608.14136v1

**PDF link:** https://arxiv.org/pdf/2608.14136v1

**Abstract:**

Octree-based anchor Gaussian Splatting has emerged as a scalable representation for city-scale novel view synthesis, where multi-level anchors adaptively capture scene content from coarse building structures to fine architectural details. However, we identify a fundamental limitation in existing methods: cross-level feature isolation, where each level's anchor features are optimized independently with no inter-level communication, causing color drift on building facades and over-smoothing in textured regions. We present HiCo-GS, a high-fidelity reconstruction framework with two complementary modules. Cross-Level Context Aggregation (CLCA) enables bidirectional hierarchical prior injection by leveraging the octree's spatial containment structure to aggregate per-level context vectors into parent-self-child triplets, fused via a lightweight MLP with residual connection. Coarse-level structural priors flow down to inform fine-level anchors, while fine-level detail statistics feed back to prevent over-smoothing, at negligible computational overhead. Depth-Normal Geometric Consistency (DNGC) regularization enforces agreement between rendered normals and depth-derived normals through an alpha-weighted consistency loss, complemented by edge-aware smoothness losses with progressive warmup that exploit the strong planar priors ubiquitous in urban geometry to suppress floating artifacts. We further introduce the China-Pagoda dataset comprising 8 ancient Chinese pagodas with over 1,200 images each, featuring dense ornamental carvings, curved multi-layer eaves, and repetitive fine-grained textures. Extensive experiments on Mill19, UrbanScene3D, MatrixCity, and China-Pagoda demonstrate that HiCo-GS achieves state-of-the-art rendering quality and substantially cleaner geometry across real-world and synthetic urban benchmarks.Code: https://github.com/WZ-CS/HiCo-GS.

**Why this may be relevant:**

It connects to urban tree detection, canopy mapping, or vegetation analysis.

---

### 9. Rollplex: Cross-Phase GPU Spatial Sharing for Vision Language Model Post-Training

**Authors:** Hanfeng Lu, Tianyu Feng, Suyi Li, Yuheng Zhao, Wei Gao, Shaopan Xiong, Ju Huang, Siran Yang

**Published:** 2026-08-14

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 21

**Venue importance score included:** 0

**arXiv ID:** 2608.14498v1

**Paper link:** http://arxiv.org/abs/2608.14498v1

**PDF link:** https://arxiv.org/pdf/2608.14498v1

**Abstract:**

Vision-language models (VLMs) enable embodied agents to reason and act from visual observations and language instructions. Reinforcement learning (RL) post-training enhances these capabilities using task feedback, but current on-policy RL runtimes execute rollout, reference scoring, and actor training in strict serial phases. While effective for text-only RL, this phase-granular execution is wasteful for VLMs, where processing dense video inputs and prompt prefixes occupies a large fraction of each phase. Because prefix processing is independent of the generated response, it can be run alongside rollout decoding, which leaves GPU compute capacity underutilized, without breaking synchronous on-policy semantics. We present Rollplex, a runtime that decomposes the reference and training phase and moves the prefix computation into the rollout decode window. Realizing this schedule requires more than concurrent kernel launches: naive colocation of Qwen2.5-VL-32\,B requires roughly 165\,GiB per GPU, while rollout and training prefer different tensor-parallel (TP) degrees and weight layouts. Rollplex addresses these constraints with two mechanisms. Phase-aware memory management controls HBM residency according to producer--consumer lifetimes. Parallelism-aware weight sharing uses the same physical storage for layout-compatible tensors across distinct TP degrees and reconstructs only incompatible tensors, avoiding a complete second actor copy. On 32 H800 GPUs, Rollplex achieves $1.23\times$--$1.30\times$ speedup over serial colocation and $1.57\times$--$2.24\times$ over disaggregation under the same GPU budget, while preserving the synchronous RL update.

**Why this may be relevant:**

It may be useful for multimodal geospatial understanding using image-text models.

---

### 10. Whose doctor does the AI recommend? An algorithm audit of reputation and demographic signals in large language model-assisted physician choice

**Authors:** Syeda Anshrah Gillani, Mirza Samad Ahmed Baig

**Published:** 2026-08-14

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 21

**Venue importance score included:** 0

**arXiv ID:** 2608.14399v1

**Paper link:** http://arxiv.org/abs/2608.14399v1

**PDF link:** https://arxiv.org/pdf/2608.14399v1

**Abstract:**

Patients increasingly ask large language model (LLM) assistants which doctor to see, making these systems AI infomediaries: algorithms that intermediate one person's choice among other people and thereby decide, silently and at scale, which physicians become visible. We report a prespecified randomized algorithm audit of what causally moves those recommendations. Seven models (six open-weight; gpt-4o-mini) each chose among five synthetic family-medicine physician cards whose attributes were independently randomized across 3,024 choice sets, three patient personas, nine prompt paraphrases and nine experimental arms, yielding 40,068 scored responses; gender and ethnicity were signaled through names following correspondence-audit methodology. Reputation signals dominate: raising a rating from 3.9 to 4.7 increases choice probability by 31.4 percentage points (pp), and raising the fee from $90 to $190 lowers it by 20.0 pp. Demographic parity is rejected, but not in the direction human audit studies predict: female-signaled names gain 2.5 pp, and Hispanic-, South-Asian- and Black-signaled names gain 1.3-2.9 pp over White-signaled names, tilts worth $7-$14 per visit in fee-equivalent terms, and a content-free first-listed position is worth $11. Yet models mentioned gender or ethnicity in at most 0.03% of their stated reasons and abstained in 0.39% of trials, so these effects are invisible in the models' own explanations, and transparency obligations relying on model self-report would not detect them. One reasoning model failed the prespecified auditability gate outright. The frozen design makes the audit repeatable: any new model can be assessed against identical stimuli, making recurring behavioural audit, rather than self-reported explanation, the monitoring technology fit for purpose.

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis.

---

