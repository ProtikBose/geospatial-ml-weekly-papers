# Weekly Geospatial ML Papers

**Search window:** 2026-06-15 to 2026-06-22

**Sources:** arXiv and Semantic Scholar

**Total selected papers:** 10

This digest focuses on geospatial analysis, urban climate, urban planning, infrastructure, and geospatial problem-solving using ML, computer vision, LLMs, VLMs, foundation models, self-supervised learning, and related methods.

Only papers from the selected top journals, conferences, or workshops are included by default. The venue importance score is included in **My Score**.

## Top Papers

### 1. PCFootprint: A Large-Scale Dataset and Benchmark for Vectorized Building Footprint Extraction from Aerial LiDAR Point Clouds

**Authors:** Haoyuan Shen, Kuihao Wang, Ruisheng Wang, Yujun Liu

**Published:** 2026-06-18

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 61

**Venue importance score included:** 0

**arXiv ID:** 2606.20455v1

**Paper link:** http://arxiv.org/abs/2606.20455v1

**PDF link:** https://arxiv.org/pdf/2606.20455v1

**Abstract:**

Building footprint extraction is a fundamental task in photogrammetry, remote sensing, and computer vision. Recent image-based methods have achieved remarkable progress in extracting vectorized footprints from high-resolution optical imagery. However, optical imagery inherently susceptible to occlusions, perspective distortions, and residual relief displacement, yielding incomplete or misaligned footprint extraction. Furthermore, the lack of explicit elevation information limits its direct applicability to Level of Detail building modeling. In this paper, we present PCFootprint, the first large-scale public dataset for footprint extraction from airborne laser scanning point clouds. PCFootprint comprises \num{33000} tiles derived from the Estonian Land and Spatial Development Board, covering diverse urban and rural landscapes. Each tile spans \qtyproduct{128 x 128}{\m} with systematically aligned vectorized footprints aligned to point clouds. The dataset includes a \num{3000} tiles cross-domain test set for evaluating generalization across geographic regions. We establish comprehensive benchmarks by evaluating mainstream methods. Experimental results reveal significant challenges including high intra-class variance, data imbalance, and noise across complex geospatial environments. We believe PCFootprint will advance future research in building modeling, urban scene understanding, and geospatial analysis. The PCFootprint dataset is publicly available at \url{https://huggingface.co/datasets/Haoyuan-Shen/PCFootprint}.

**Why this may be relevant:**

It is directly related to remote sensing or Earth observation workflows. It may be useful for LiDAR-based tree inventory, urban structure mapping, or 3D geospatial analysis. It may help with cross-city, cross-region, or cross-sensor generalization.

---

### 2. Integrating national forest inventory, airborne lidar, and satellite imagery for wall-to-wall mapping of forest structure with computer vision

**Authors:** Luke J. Zachmann, David D. Diaz, Vincent A. Landau, Chelsey Walden-Schreiner, Tony Chang, Nathan E. Rutenbeck, Katharyn A. Duffy, Kiarie Ndegwa

**Published:** 2026-06-18

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 52

**Venue importance score included:** 0

**arXiv ID:** 2606.20291v1

**Paper link:** http://arxiv.org/abs/2606.20291v1

**PDF link:** https://arxiv.org/pdf/2606.20291v1

**Abstract:**

Remote sensing is increasingly relied upon to deliver actionable science for forest and wildfire risk management across large landscapes. Wall-to-wall, annually updated maps are a persistent need for effective forest management. Many planning systems and data collections combine disparate data sources with different purposes, vintages, and prediction quality, which leads to confounding behavior in operational planning systems. We introduce the VibrantForests framework, developed and applied to map forest attributes and provide a coherent foundation for effective forest and wildfire planning. VibrantForests includes a satellite-based forest structure model trained on lidar-derived samples and applied across the contiguous United States to concurrently generate estimates of canopy cover, canopy height, aboveground live tree biomass, basal area, and quadratic mean diameter at 10-meter resolution. We demonstrate predictive capability spanning the full spectrum of forest conditions ranging from sparse-canopy/low-biomass to dense-canopy/high-biomass. Results show that our model extends the range at which saturation is commonly encountered in comparable passive-sensor models, and reduces regression-to-mean behavior that commonly produces overestimation of forest attributes in small/sparse conditions and underestimation in large/dense conditions. The VibrantForests framework addresses a key limitation in large-area forest and wildfire planning by delivering coherent wall-to-wall estimates of management-relevant attributes at annual cadence and 10m resolution.

**Why this may be relevant:**

It is directly related to remote sensing or Earth observation workflows. It may be useful for LiDAR-based tree inventory, urban structure mapping, or 3D geospatial analysis. It connects to urban tree detection, canopy mapping, or vegetation analysis.

---

### 3. Evaluating and Enhancing Negation Comprehension in Remote Sensing MLLMs

**Authors:** Haochen Han, Jue Wang, Alex Jinpeng Wang, Fangming Liu

**Published:** 2026-06-18

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 42

**Venue importance score included:** 0

**arXiv ID:** 2606.20177v1

**Paper link:** http://arxiv.org/abs/2606.20177v1

**PDF link:** https://arxiv.org/pdf/2606.20177v1

**Abstract:**

Multimodal Large Language Models (MLLMs) have demonstrated remarkable success in various Remote Sensing (RS) tasks. However, their ability to comprehend negation remains underexplored, limiting deployment in real-world applications where models must explicitly identify what is false or absent, e.g., emergency responders need to locate non-flooded routes for evacuation. To comprehensively study this limitation, we introduce RS-Neg, the first benchmark to evaluate negation understanding across region-level to scene-level tasks. Specifically, we design an automated data generation pipeline for RS imagery, using LLMs to synthesize diverse negation queries, and introduce a dynamic visual focus module for verification. Our evaluation reveals that advanced RS MLLMs struggle with negation, exhibiting hallucinations and substantial performance degradation. To close this gap, we propose NeFo, a novel test-time learning method that explicitly incorporates the logical role of negation into the model optimization. Remarkably, using about 5\% unlabeled test samples, NeFo significantly improves the negation understanding of models and shows strong generalization to unseen tasks. Code and data will be released upon acceptance.

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis. It is directly related to remote sensing or Earth observation workflows. It may help with cross-city, cross-region, or cross-sensor generalization.

---

### 4. Slow Brain, Fast Planner: Latency-Resilient VLM-Augmented Urban Navigation

**Authors:** Zhenghao "Mark'' Peng, Honglin He, Quanyi Li, Yukai Ma, Bolei Zhou

**Published:** 2026-06-18

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 40

**Venue importance score included:** 0

**arXiv ID:** 2606.20458v1

**Paper link:** http://arxiv.org/abs/2606.20458v1

**PDF link:** https://arxiv.org/pdf/2606.20458v1

**Abstract:**

Learning-based planners for sidewalk navigation can generate diverse candidate trajectories in real time, yet their scoring functions often fail to select the best trajectory in challenging situations, outputting trajectories that make the mobile robot drive onto grass, toward pedestrians, or in the wrong direction, even when better candidates exist in the same set. We call this the trajectory scoring gap: in real-world sidewalk navigation, the gap between an anchor-based planner's top choice and the best possible candidate is substantial, likely due to limited high-level scene understanding capability of the planner. Rather than replacing the planner with an end-to-end Vision-Language-Action model, we propose a VLM-Planner interface that uses a VLM to select a candidate index from the planner's proposal set and then fuse it with the planner's initial output. However, VLMs take 1--3s per query and so cannot directly drive a 5--20Hz control loop. We contribute a training-free, latency-resilient trajectory-level fusion layer that turns a stale VLM selection into real-time planner scoring via geometric similarity with exponential decay. On $\sim$2,000 challenging real-world scenarios (e.g., junctions, pedestrian encounters), VLM selection achieves 30% ADE reduction versus the planner's best selection, while the planner remains competitive in routine situations. In simulation, Score Fusion maintains >80% success rate with delays up to 5s. We demonstrate the full system on a mobile robot navigating challenging campus sidewalks with varied network latency.

**Why this may be relevant:**

It may be useful for multimodal geospatial understanding using image-text models. It may connect to pedestrian infrastructure, road extraction, transportation infrastructure, or walkability mapping.

---

### 5. HilDA: Hierarchical Distillation with Diffusion for Advancing Self-Supervised LiDAR Pre-trainin

**Authors:** Maciej Wozniak, Jesper Ericsson, Hariprasath Govindarajan, Truls Nyberg, Thomas Gustafsson, Patric Jensfelt, Olov Andersson

**Published:** 2026-06-18

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 40

**Venue importance score included:** 0

**arXiv ID:** 2606.20189v1

**Paper link:** http://arxiv.org/abs/2606.20189v1

**PDF link:** https://arxiv.org/pdf/2606.20189v1

**Abstract:**

Leveraging Vision Foundation Models (VFMs) for camera-to-LiDAR knowledge distillation offers a promising solution to the scarcity of annotated data needed to represent the immense geometric and kinematic diversity of real-world autonomous driving (AD). However, current approaches typically treat VFMs as black-box teachers, relying exclusively on frame-wise feature similarity. Consequently, they do not fully exploit the teacher's layer-wise semantic structure and global context, as well as the rich spatiotemporal information inherent in LiDAR sequences. We propose HilDA, a self-supervised pretraining framework for LiDAR backbones that better captures the semantic what and geometric where needed for driving tasks. HilDA combines hierarchical distillation comprising multi-layer distillation for progressive semantic alignment and global context distillation for scene-level semantics, with a temporal occupancy diffusion objective promoting spatiotemporal consistency. Models pre-trained with HilDA achieve state-of-the-art results on cross-modal distillation benchmarks and outperform models trained via prior distillation approaches on 3D object detection, scene flow, and semantic occupancy prediction. Code available at: https://maxiuw.github.io/hilda.

**Why this may be relevant:**

It may help track foundation-model directions for Earth observation or geospatial AI. It may be useful for LiDAR-based tree inventory, urban structure mapping, or 3D geospatial analysis.

---

### 6. Exploring the potential of AlphaEarth and TESSERA embeddings for Fine-scale Local Climate Zone Mapping: A case study across five cities in Switzerland

**Authors:** Htet Yamin Ko Ko, Clement Atzberger

**Published:** 2026-06-18

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 39

**Venue importance score included:** 0

**arXiv ID:** 2606.20034v1

**Paper link:** http://arxiv.org/abs/2606.20034v1

**PDF link:** https://arxiv.org/pdf/2606.20034v1

**Abstract:**

Understanding urban spatial morphology is critical for climate modeling, risk assessment, and sustainable urban design, and Local Climate Zone (LCZ) mapping provides the basic framework for this. However, many cities still use coarse ~100-m resolution LCZ records, which are unsuitable for fine-scale urban research. In this study, precomputed embeddings from TESSERA (Feng et al., 2025) and AlphaEarth (Brown et al., 2025) are compared to traditional Sentinel-1/2 (S1S2) composites in five Swiss cities to see if they can upscale coarse LCZ maps to 10-m resolution using an attention-based U-Net. Three experiments assess multi-city transferability, the impact of higher-resolution reference data, and temporal robustness to year-to-year phenology changes. We find that all datasets achieve strong performance with test data Intersection-over-Union (IoU) ranging from 0.59-0.69 and 0.77-0.82 in the first two experiments. TESSERA consistently outperforms both S1S2 and AlphaEarth across both settings As expected, we find that the transfer of embedding-based models from one year to another remains an open challenge. Overall, however, our results demonstrate the promising potential of embeddings derived from EO foundation models to reduce time consuming preprocessing, respectively, manual feature engineering tasks and to guide a universal deep learning-based LCZ mapping workflow. When combined with a simple location-aware attention U-Net architecture, the embeddings enhance regional transferability and scalability, supporting the development of comprehensive and reproducible fine-scale LCZ maps for global urban climate applications Improving reference data quality remains the strongest lever for further accuracy gains.

**Why this may be relevant:**

It may help track foundation-model directions for Earth observation or geospatial AI. It is relevant to urban climate and heat-resilience research.

---

### 7. Multi-Modal Contrastive Learning for Implicit Earth Embeddings via Location Tying

**Authors:** Jonathan Hecht, Lukas Arzoumanidis, Ziyue Li, Youness Dehbi

**Published:** 2026-06-18

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 38

**Venue importance score included:** 0

**arXiv ID:** 2606.20167v1

**Paper link:** http://arxiv.org/abs/2606.20167v1

**PDF link:** https://arxiv.org/pdf/2606.20167v1

**Abstract:**

Spatial prediction tasks are often limited by a lack of high-quality labelled ground-truth observations. To overcome this challenge, self-supervised pre-training is a possible solution, with contrastive learning dominant for location encoders. Those approaches usually align geographic coordinates with just one additional modality. We propose two multimodal contrastive learning architectures: Multimodal Embedding via Location Tying (MELT) and Sequential Alternating Location Training (SALT). These architectures expand this framework beyond two modalities by utilising unpaired geospatial data. Both methods are technically viable and match the performance of the strongest two-modality baseline (SATCLIP) across four downstream tasks. However, increasing the number of modalities does not consistently improve performance, suggesting that the chosen location encoder is the main limitation - the contrastive objective reaches its peak early, regardless of modality diversity or pre-training volume. MELT provides more stable training than SALT and presents a stronger foundation for future scaling.

**Why this may be relevant:**

It matched the geospatial machine learning search criteria and may be worth screening.

---

### 8. ForEnt: A Multi-Modal Dataset for Characterizing Quadruped Robot Entrapments in Forest Environments

**Authors:** Natapat Kirdwichai, Danesh Tarapore

**Published:** 2026-06-18

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 32

**Venue importance score included:** 0

**arXiv ID:** 2606.19675v1

**Paper link:** http://arxiv.org/abs/2606.19675v1

**PDF link:** https://arxiv.org/pdf/2606.19675v1

**Abstract:**

Legged robots are increasingly deployed in forests for ecological surveying and monitoring, yet their autonomy is often interrupted consequent to the challenges posed in traversing forest environments. Forest entrapments, for example, when a robot's legs are ensnared in vines or other vegetation, result in loss of stability and toppling. Such events not only disrupt the mission and require manual intervention, but also risk damage to the robot hardware. To address the absence of a dedicated dataset to investigate these failure modes in forest environments, we present ForEnt, a multi-modal dataset collected with the low-cost Unitree Go2 quadruped across eight forest sites in the Southampton Common Woodlands, UK. For our dataset, over approximately 1.7 km of traversals in 11 sequences were conducted, yielding 69 recorded entrapment events. ForEnt includes time-synchronized RGB-D images, LiDAR scans, proprioceptive data, and third-person video, enabling analysis of terrain factors contributing to entrapment and providing labeled sensor streams for reproducible benchmarking. By supporting the evaluation of entrapment detection strategies, ForEnt lowers the barrier to developing robust quadruped robot deployments in challenging forest environments.

**Why this may be relevant:**

It may be useful for LiDAR-based tree inventory, urban structure mapping, or 3D geospatial analysis. It connects to urban tree detection, canopy mapping, or vegetation analysis.

---

### 9. Vision-Reasoning-Guided Occlusion Removal from Light Fields

**Authors:** Mohamed Youssef, Oliver Bimber

**Published:** 2026-06-18

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 24

**Venue importance score included:** 0

**arXiv ID:** 2606.19985v1

**Paper link:** http://arxiv.org/abs/2606.19985v1

**PDF link:** https://arxiv.org/pdf/2606.19985v1

**Abstract:**

Occlusion-robust scene recovery remains a major challenge in computational imaging, particularly in natural environments where dense foreground vegetation severely limits visibility. We propose a vision-reasoning-guided light field occlusion removal framework that combines the visibility recovery capability of light field integration (LFI) with the semantic reasoning capacity of vision-language models (VLMs). Multi-view observations are first integrated via LFI to suppress foreground occlusions and produce an initial visibility-enhanced representation. A VLM is then incorporated as a conditional semantic prior to restore degraded structures and recover fine details, guided by the observed measurements. To improve recovery consistency and reduce hallucination artifacts, we introduce a multi-sample fusion strategy that aggregates multiple generated hypotheses into a unified estimate. Experimental results on synthetic and real-world datasets demonstrate state-of-the-art performance, achieving the highest average SSIM across four synthetic light field benchmark scenes (4-Syn) and strong generalization across structured and unstructured acquisition settings. These results highlight the effectiveness of combining physical imaging constraints with vision-language reasoning for robust perception under severe occlusion, with applicability to search-and-rescue and exploratory robotic navigation.

**Why this may be relevant:**

It may be useful for multimodal geospatial understanding using image-text models. It connects to urban tree detection, canopy mapping, or vegetation analysis. It may help with cross-city, cross-region, or cross-sensor generalization.

---

### 10. Lagrange: An Open-Vocabulary, Energy-Based Sparse Framework for Generalized End-to-End Driving

**Authors:** Shihao Ji, HongXi Li, Zihui Song, Mingyu Li

**Published:** 2026-06-18

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 18

**Venue importance score included:** 0

**arXiv ID:** 2606.20274v1

**Paper link:** http://arxiv.org/abs/2606.20274v1

**PDF link:** https://arxiv.org/pdf/2606.20274v1

**Abstract:**

Scaling end-to-end autonomous driving to complex, open-world environments requires perceptual models that generalize to anomalous scenarios and planners that produce kinematically valid trajectories. Existing paradigms face a distinct dichotomy between representational efficiency and generalization capacity. Dense models (e.g., occupancy networks), while geometrically robust, incur critical computational bottlenecks and struggle with high-level semantic reasoning. Conversely, sparse, query-based planners are efficient but reliant on closed-set definitions, rendering them vulnerable to out-of-distribution (OOD) events. Although recent Vision-Language-Action (VLA) models offer open-vocabulary reasoning, their autoregressive, discrete token generation fundamentally conflicts with the continuous, high-frequency control requirements of vehicle dynamics. To address this, we propose Lagrange, an open-vocabulary, computationally sparse driving framework based on Masked Latent Fields (MLF). Rather than relying on dense volumetric reconstructions or closed-set query mechanisms, Lagrange exploits Vision-Language Models (VLMs) to encode class-agnostic object proposals into continuous semantic visual tokens. We introduce an intent-driven masked cross-attention module that temporally filters irrelevant entities, decoding the attended tokens into an implicit continuous energy field defined over spatial coordinates. By framing decision-making as a Lagrangian action minimization problem spanning this energy field, we enforce strict compliance with vehicle kinematics while executing collision avoidance. Extensive offline evaluations on both standard (nuScenes) and long-tail (CODA) benchmarks demonstrate that Lagrange establishes a promising framework for robust, interpretable, and kinematically feasible open-world autonomy.

**Why this may be relevant:**

It may be useful for multimodal geospatial understanding using image-text models. It may help with cross-city, cross-region, or cross-sensor generalization.

---

