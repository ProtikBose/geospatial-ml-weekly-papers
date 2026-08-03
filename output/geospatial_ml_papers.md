# Weekly Geospatial ML Papers

**Search window:** 2026-07-27 to 2026-08-03

**Sources:** arXiv and Semantic Scholar

**Total selected papers:** 10

This digest focuses on geospatial analysis, urban climate, urban planning, infrastructure, and geospatial problem-solving using ML, computer vision, LLMs, VLMs, foundation models, self-supervised learning, and related methods.

Only papers from the selected top journals, conferences, or workshops are included by default. The venue importance score is included in **My Score**.

## Top Papers

### 1. Analyzing the impact of urban form on land surface temperature in arid cities, using machine learning algorithms (Case: Isfahan, Iran)

**Authors:** M. Suleimany

**Published:** 2026-08-01

**Venue:** Urban Climate

**Found via:** Semantic Scholar

**My Score:** 53

**Venue importance score included:** 10

**Semantic Scholar citations:** 0

**DOI:** 10.1016/j.uclim.2026.103053

**Paper link:** https://www.semanticscholar.org/paper/909790dca9eba273a8380e31a00ab017e6607242

**Abstract:**

No abstract available.

**Why this may be relevant:**

It appears in one of the selected top journals, conferences, or workshops. It is relevant to urban climate and heat-resilience research.

---

### 2. TerraNova: A Foundation Model for the Anthropocene

**Authors:** Carlos Rodriguez-Pardo, Massimo Tavoni

**Published:** 2026-07-31

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 43

**Venue importance score included:** 0

**arXiv ID:** 2607.29527v1

**Paper link:** http://arxiv.org/abs/2607.29527v1

**PDF link:** https://arxiv.org/pdf/2607.29527v1

**Abstract:**

A defining problem of the Anthropocene is to model the physical Earth and human societies as one coupled system, yet no learned representation spans their observational breadth. We argue the obstacle is geometric: the physical Earth is measured as continuous fields that ignore political borders, whereas societies are reported for administrative units. Earth-system foundation models serve the first geometry; coupling it to the second has required lossy averaging over borders. We introduce TerraNova, a foundation model trained on 1,024 physical and societal records in their native geometries: 512 gridded Earth-system fields and 512 national indicators. Dedicated encoders represent location, country, time and task, cross-modal transformers fuse them into a shared spatiotemporal state, and a hypernetwork generates a per-query decoder whose evidential head returns a predictive distribution. Two contrastive objectives couple the representation: a population-weighted alignment between each country and coordinates in its territory, and one to pretrained geospatial embeddings carrying image-derived semantics. Read out through that decoder, the representation is competitive with purpose-built geospatial encoders while spanning axes they do not represent (time, oceans and uncertainty) and supporting country-level capabilities. The frozen backbone reconstructs dense fields from sparse observations and adapts to unseen variables in minutes on consumer hardware.

**Why this may be relevant:**

It may help track foundation-model directions for Earth observation or geospatial AI.

---

### 3. Locally Consistent Transductive Information Maximization for Few-Shot Remote Sensing Scene Classification

**Authors:** Karim El Khoury, Benoît Gérin, Benoît Macq, Christophe De Vleeschouwer

**Published:** 2026-07-31

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 37

**Venue importance score included:** 0

**arXiv ID:** 2607.29192v1

**Paper link:** http://arxiv.org/abs/2607.29192v1

**PDF link:** https://arxiv.org/pdf/2607.29192v1

**Abstract:**

Remote sensing scene classification is increasingly relying on foundation models pre-trained on large-scale Earth-observation data. Moreover, transductive inference, which exploits the collective statistical structure of the entire unlabeled query set, appears to naturally match remote sensing pipelines where large images are routinely split into patches and inferred as a batch. In this work, we introduce LC-TIM (Locally Consistent Transductive Information Maximization), which extends the state-of-the-art Transductive Information Maximization for Few-Shot CLIP (TIM++) objective with a local consistency regularizer that enforces prediction agreement between each query sample and its $κ$ nearest feature-space neighbors. The regularizer enters as a single multiplicative factor in the closed-form $q$-update, adding negligible computational overhead. We further propose a multi-source extension that fuses the affinity graph from multiple remote sensing foundation model, further boosting classification accuracy. To assess these methods, we establish the first comprehensive, open-source benchmark for transductive few-shot RS scene classification, evaluating LP++, TransCLIP, TIM++, and LC-TIM across ten diverse datasets, two remote sensing vision-language models, and across various few-shot settings. Our experiments show that transductive methods consistently outperform zero-shot baselines, and that LC-TIM achieves state-of-the-art accuracy, with the largest gains in the low-shot regime where neighborhood cues are most informative. Code is publicly available at: https://github.com/elkhouryk/LC-TIM

**Why this may be relevant:**

It may help track foundation-model directions for Earth observation or geospatial AI. It is directly related to remote sensing or Earth observation workflows.

---

### 4. SatEdit: Mask-Conditioned Image Editing via VLM-Guided Segment Annotation

**Authors:** Muhammad Talha, Muhammad Ahmed Amer

**Published:** 2026-07-31

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 37

**Venue importance score included:** 0

**arXiv ID:** 2607.29367v1

**Paper link:** http://arxiv.org/abs/2607.29367v1

**PDF link:** https://arxiv.org/pdf/2607.29367v1

**Abstract:**

Satellite image editing requires spatially precise object-level control, but supervised editing datasets for overhead imagery are costly to build because object masks, semantic labels, and paired edits are rarely available at scale. We introduce SatEdit, a mask-conditioned satellite image editing framework that constructs training supervision from unlabeled imagery. SatEdit proposes object masks with a seg- mentation foundation model, assigns semantic la- bels to sampled segments with a Vision-Language Model, and applies lightweight human verification before generating paired addition and removal exam- ples through mask-guided inpainting. We fine-tune a high-resolution image editing backbone with LoRA on a SODA-A-derived dataset containing 1,014 im- ages and 852 verified object annotations across 91 classes. In controlled comparisons with open- source and proprietary image editing models, SatE- dit achieves the highest aggregate masked-region se- mantic alignment, with a CLIP score of 0.6322 and CLIP delta of 0.0726, while preserving the surround- ing scene qualitatively. These results suggest that VLM-assisted segment annotation is a practical route to data-efficient, spatially controllable satellite image editing.

**Why this may be relevant:**

It may help track foundation-model directions for Earth observation or geospatial AI. It may be useful for multimodal geospatial understanding using image-text models. It is directly related to remote sensing or Earth observation workflows.

---

### 5. CorrelationFlow: A Training-Free Geometric Approach for LiDAR Scene Flow Estimation

**Authors:** Minh-Quan Dao, Yancong Lin, Julie Stephany Berrio Perez, Holger Caesar

**Published:** 2026-07-31

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 25

**Venue importance score included:** 0

**arXiv ID:** 2607.29237v1

**Paper link:** http://arxiv.org/abs/2607.29237v1

**PDF link:** https://arxiv.org/pdf/2607.29237v1

**Abstract:**

LiDAR scene flow estimation has settled into a monoculture: nearly all recent methods share the same feed-forward architecture and the same family of self-supervised losses, inheriting each other's assumptions, and each other's blind spots. When those assumptions fail, as they do for sparse, distant, or fast-moving objects, every method built on them fails together, and adding parameters or simulated training data does not fix what the formulation itself gets wrong. This paper takes the opposite path. We present CorrelationFlow, a training-free geometric framework that reduces scene flow to two textbook operations: connected-component labeling and correlation maximization on bird's-eye-view occupancy images. Objects are isolated as spatio-temporal connected components, their motions recovered as correlation peaks, and the resulting velocities propagated to all member points. However, this dense correlation evaluates every candidate displacement of every cluster and requires a window of past sweeps; therefore, we develop a sparse counterpart that operates on a single sweep pair by matching lightweight occupancy descriptors at boundary key points. Because nothing is trained, nothing is inherited: on the multi-domain test set of the Argoverse 2 2026 Scene Flow Challenge, spanning five datasets with heterogeneous sensors and platforms, CorrelationFlow ranked second among unsupervised methods and degrades most gracefully at long range, where the shared assumptions of learned methods break down. Our results suggest that a substantial share of the scene flow problem is solvable by classical computer vision, and that progress may require questioning the formulation, not scaling it.

**Why this may be relevant:**

It may be useful for LiDAR-based tree inventory, urban structure mapping, or 3D geospatial analysis.

---

### 6. SAGP: Semantic Affordance-Guided Grasp Planning via Coarse-Zone VLM Reasoning

**Authors:** Muhayy Ud Din, Irfan Hussain

**Published:** 2026-07-31

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 24

**Venue importance score included:** 0

**arXiv ID:** 2607.29374v1

**Paper link:** http://arxiv.org/abs/2607.29374v1

**PDF link:** https://arxiv.org/pdf/2607.29374v1

**Abstract:**

Geometry-based grasp planners ensure physically valid grasps but ignore functional semantics, often generating grasps that are antipodal and collision-free yet practically inappropriate, for example, gripping a mug by its rim, a knife by the blade, or a bottle near its cap. These inconsistencies cause the downstream task to fail even when traditional grasp metrics are met. Existing vision-language model (VLM) approaches either depend on fine-grained, category-specific part segmentation or attempt to directly infer grasp poses, with the latter prone to spatial hallucinations. As a result, no practical, training-free framework has yet been proposed that robustly links high-level semantic reasoning to geometric grasp planning. We introduce Semantic Affordance-Guided Grasp Planning (SAGP), a training-free pipeline built on a coarse-zone abstraction layer. The method first partitions the object point cloud into spatial regions (top, middle, bottom, lateral sides, and protrusions) by applying PCA-based alignment followed by distance-driven DBSCAN clustering, entirely bypassing learned segmentation. A pre-trained VLM then assesses the grasp quality of each region through a structured zero-shot query, and the resulting zone-wise scores are fused with geometric, reachability, and task-alignment signals to re-rank antipodal grasp candidates. Experiments on YCB objects in PyBullet with a Franka Panda robot show that SAGP preserves the high success rate of geometry-only planning while substantially improving the functional appropriateness of selected grasps, particularly on asymmetric, handle-bearing objects where geometry alone is uninformative. The introduced coarse-zone abstraction offers an effective, training-free bridge between VLM-based reasoning and geometric grasp planning, without the need for fine-grained part segmentation.

**Why this may be relevant:**

It may be useful for multimodal geospatial understanding using image-text models. It may be useful for LiDAR-based tree inventory, urban structure mapping, or 3D geospatial analysis.

---

### 7. The Parts Are Greater Than the Sum: Automated Task Sequencing for Efficient Training of Multi-Policy LLMs

**Authors:** Jiajia Tang, Sizhe Yuen, Francisco Gomez Medina, Yali Du, Adam Sobey

**Published:** 2026-07-31

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 21

**Venue importance score included:** 0

**arXiv ID:** 2607.29601v1

**Paper link:** http://arxiv.org/abs/2607.29601v1

**PDF link:** https://arxiv.org/pdf/2607.29601v1

**Abstract:**

Parameter-Efficient Fine-Tuning (PEFT) commonly adapts large language models using a single shared Low-Rank Adapter (LoRA). This shared optimization space often suffers from interference when adapting heterogeneous task sequences, leading to poor transfer and catastrophic forgetting. Existing approaches mainly improve adapter expressiveness by increasing parameter capacity or composing multiple adapters, yet they still rely on a shared optimization path. In this paper, we propose an optimization-path organization framework for parameter-efficient fine-tuning of large language models, implemented as an automatic multi-policy PEFT architecture. Specifically, optimization-compatible adaptation paths are automatically organized through task grouping and task sequencing under a fixed parameter budget. The organized optimization paths are implemented as independent Quantized Low-Rank Adapters (QLoRA), enabling heterogeneous tasks to be optimized in decoupled adaptation spaces while preserving positive transfer among compatible tasks. Experiments on the TRACE benchmark demonstrate that performance consistently improves from conventional single-policy PEFT to multi-policy PEFT, with the proposed automatic multi-policy framework achieving the best performance of 44.78 under the same trainable capacity. This suggests that optimization-path organization is more effective than simply increasing adapter capacity for heterogeneous parameter-efficient fine-tuning.

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis.

---

### 8. Poverty Mapping: Data, Models and Applications

**Authors:** Suoyi Tan, Mengning Wang, Yixiu Kong, Huimin Bai, Jianguo Liu, Dirk Brockmann, Yicheng Zhang, Xin Lu

**Published:** 2026-07-31

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 20

**Venue importance score included:** 0

**arXiv ID:** 2607.29457v1

**Paper link:** http://arxiv.org/abs/2607.29457v1

**PDF link:** https://arxiv.org/pdf/2607.29457v1

**Abstract:**

Poverty mapping is increasingly important for monitoring Sustainable Development Goal 1 (SDG 1) of the United Nations 2030 Agenda, which aims to end poverty in all its forms everywhere. Yet timely and fine-resolution poverty estimation remains difficult because conventional census- and survey-based approaches are costly, infrequent, and often sparse precisely where deprivation is most severe. As poverty emerges from complex socioeconomic systems shaped by human mobility, social interactions, infrastructure, and economic activities, emerging computational methods and nontraditional data sources have created new opportunities for poverty estimation and mapping. At the intersection of statistical physics, complex systems science, and data science, these approaches enable poverty estimation at finer spatial and temporal resolutions. This review summarizes the main concepts of poverty and the principal frameworks used to measure it, and examines recent advances on poverty estimation and mapping using satellite imagery, mobile phone data, social media data, and multisource data fusion. The review also discusses persistent challenges related to representativeness, transferability across regions, interpretability, and uncertainty quantification. Finally, the review clarifies both the analytical promise and the practical limits of contemporary poverty mapping.

**Why this may be relevant:**

It is directly related to remote sensing or Earth observation workflows. It is related to urban planning, infrastructure, or built-environment analysis.

---

### 9. AquaJEPA: Action-Conditioned Multimodal Predictive Representations for Underwater Robot Dynamics

**Authors:** Alan-Barsag Gazzaev, Alexey Gavrilov, Sergey Muravyov

**Published:** 2026-07-31

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 16

**Venue importance score included:** 0

**arXiv ID:** 2607.29393v1

**Paper link:** http://arxiv.org/abs/2607.29393v1

**PDF link:** https://arxiv.org/pdf/2607.29393v1

**Abstract:**

Underwater robots combine complementary sensors whose reliability changes abruptly with water visibility, viewpoint, and vehicle motion. We introduce AquaJEPA, an action-conditioned joint-embedding predictive model that fuses an RGB camera, forward-looking sonar, and proprioception with explicit sensor validity. It predicts a future latent target conditioned on eight-thruster commands and supplies velocity and sonar-profile predictions to a shared receding-horizon planner. We study the method in Stonefish against reactive, state-only, ordinary multimodal, supervised dynamics, and recurrent world-model baselines. We further isolate the EMA target, action margin, masks, and modality dropout. A preregistered 120-environment replication comprises five independent replicates of a grid crossing three unseen obstacle maps, four water-visibility coefficients, and nominal versus shifted dynamics, while intermittently removing DVL observations. In 120 fresh paired environments with scheduled DVL loss, AquaJEPA reaches 74 goals, versus 68 for both state-only and the recurrent world model, and attains the lowest mean final error (0.906 m). Paired final-error reductions relative to ordinary multimodal prediction, supervised dynamics, and the recurrent world model are 0.273 m (95% CI: 0.190-0.356), 0.364 m (0.260-0.468), and 0.106 m (0.025-0.187), respectively. AquaJEPA therefore achieves the best aggregate closed-loop performance and significantly outperforms three action-conditioned predictive baselines in paired final error; its advantage over state-only remains statistically unresolved.

**Why this may be relevant:**

It matched the geospatial machine learning search criteria and may be worth screening.

---

### 10. Training-Free Entity-Level Few-Shot Segmentation of Remote Sensing Images with Advection Refinement

**Authors:** Xueting Bai, Huan Ni

**Published:** 2026-07-31

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 16

**Venue importance score included:** 0

**arXiv ID:** 2607.29278v1

**Paper link:** http://arxiv.org/abs/2607.29278v1

**PDF link:** https://arxiv.org/pdf/2607.29278v1

**Abstract:**

Existing cross-domain few-shot segmentation approaches suffer from high training costs due to source-domain episodic training and pixel-wise dense prediction, while often producing fragmented and noisy predictions. To overcome these issues, we propose a training-free entity-level few-shot segmentation framework for remote sensing images with advection refinement. Specifically, we first leverage SAM3's generic geometric priors to generate category-agnostic entity primitives. By reformulating few-shot inference from pixel-level prediction to entity-level reasoning, foreground and background prototypes are constructed and combined with dense textual semantic responses from SAM3 to build a multi-modal semantic potential field. Furthermore, an advection equation-based semantic refinement mechanism is introduced to propagate category-aware information across both feature and similarity spaces, enhancing semantic continuity and suppressing local texture noise. Extensive experiments on multiple remote sensing datasets demonstrate that the proposed framework effectively mitigates domain shift and local noise, substantially improving SAM3's adaptation capability for remote sensing few-shot segmentation without additional training. Our code will be publicly available at https://github.com/yu-ni1989/ELFSS-AR.

**Why this may be relevant:**

It is directly related to remote sensing or Earth observation workflows.

---

