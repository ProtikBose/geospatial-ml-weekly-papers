# Weekly Geospatial ML Papers

**Search window:** 2026-06-01 to 2026-06-08

**Sources:** arXiv and Semantic Scholar

**Total selected papers:** 10

This digest focuses on geospatial analysis, urban climate, urban planning, infrastructure, and geospatial problem-solving using ML, computer vision, LLMs, VLMs, foundation models, self-supervised learning, and related methods.

Only papers from the selected top journals, conferences, or workshops are included by default. The venue importance score is included in **My Score**.

## Top Papers

### 1. Textual Supervision Enhances Geospatial Representations in Vision-Language Models

**Authors:** M. S. Locatelli, Fernando Tonucci, Jea Kwon, L. Vecchietti, Bryan Nathanael Wijaya, Cheng Yaw Low, Virgílio Almeida, Meeyoung Cha

**Published:** 2026-06-05

**Venue:** arXiv

**Found via:** Semantic Scholar, arXiv

**My Score:** 54

**Venue importance score included:** 0

**Semantic Scholar citations:** 0

**arXiv ID:** 2606.07172

**Paper link:** https://www.semanticscholar.org/paper/195de72a60b5e4912d101edfd1a8115ad89f09bd

**PDF link:** https://arxiv.org/pdf/2606.07172v1

**Abstract:**

Geospatial understanding is a critical yet underexplored dimension in the development of machine learning systems for tasks such as image geolocation and spatial reasoning. In this work, we analyze the geospatial representations acquired by three model families: vision-only architectures (e.g., ViT), vision-language models (e.g., CLIP), and large-scale multimodal foundation models (e.g., LLaVA, Qwen, and Gemma). By evaluating across image clusters, including people, landmarks, and everyday objects, grouped based on the degree of localizability, we reveal systematic gaps in spatial accuracy and show that textual supervision enhances the learning of geospatial representations. Our findings suggest the role of language as an effective complementary modality for encoding spatial context and multimodal learning as a key direction for advancing geospatial AI.

**Why this may be relevant:**

It may help track foundation-model directions for Earth observation or geospatial AI.

---

### 2. OPENPATH: A Supervisor--Specialist Agent System for Personalized, Accessible, and Multi-stop Urban Trip Planning

**Authors:** Ziyang Xiong, He Zong, Zhiyuan Xue, Manxi Wu

**Published:** 2026-06-05

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 31

**Venue importance score included:** 0

**arXiv ID:** 2606.07486v1

**Paper link:** http://arxiv.org/abs/2606.07486v1

**PDF link:** https://arxiv.org/pdf/2606.07486v1

**Abstract:**

Urban trip-planning systems are commonly optimized for travel time and cost, but they offer limited support for the heterogeneous needs that real travelers bring, such as personalized preferences, multi-stop itinerary construction, and end-to-end wheelchair accessibility. We present openpaths, a supervisor-specialist multi-agent system that handles all of these tasks within a single architecture. openpaths adopts a deliberate division of labor: LLM agents parse natural-language input, classify request intent, and orchestrate execution, while classical algorithms perform route optimization over curated mobility and accessibility data. This design ensures that the resulting trip honors heterogeneous user preferences and enforces strict accessibility requirements when requested. Beyond per-user planning, openpaths doubles as a measurement instrument for city-scale accessibility analysis: applied to NYC, the system reveals substantial ADA infrastructure gaps and quantifies their effect on job accessibility for wheelchair users. Overall, this study shows how a supervisor-specialist LLM agentic framework can support heterogeneous trip planning and transparent, equitable transportation analysis in real urban environments.

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis. It is related to urban planning, infrastructure, or built-environment analysis.

---

### 3. Does Appearance Help? A Systematic Study of Image-Based Re-Identification in Online 3D Multi-Pedestrian Tracking

**Authors:** Eduardo Borges, Luís Garrote, Urbano J. Nunes

**Published:** 2026-06-05

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 30

**Venue importance score included:** 0

**arXiv ID:** 2606.07233v1

**Paper link:** http://arxiv.org/abs/2606.07233v1

**PDF link:** https://arxiv.org/pdf/2606.07233v1

**Abstract:**

LiDAR-based 3D Multi-Object Tracking (MOT) typically relies solely on geometric information, which is often insufficient to distinguish between targets during prolonged occlusions or in crowded human-populated environments. While integrating RGB-based Re-Identification (ReID) offers a theoretical solution for preserving identity context, existing approaches often rely on computationally expensive parallel detectors that hinder real-time robot responsiveness. This work presents a systematic study of image-based ReID in online 3D MOT, utilizing a lightweight projection-based framework to decouple geometric and appearance modeling for mobile robots. A comprehensive analysis of feature extraction architectures is conducted, employing lightweight CNNs and Vision Transformers, and evaluating various multi-modal data association strategies to balance computational latency with robust tracking. Experiments on the Pedestrian class of the KITTI dataset reveal that naive linear fusion, of appearance and motion costs, degrades performance due to visual noise. Conversely, a cascaded matching strategy successfully recovers occluded tracks without compromising overall precision, effectively preventing identity switches to maintain human-robot interaction continuity. We show that lightweight architectures can offer an optimal trade-off between the low latency required for safe navigation and the discriminative power needed for social awareness.

**Why this may be relevant:**

It may be useful for LiDAR-based tree inventory, urban structure mapping, or 3D geospatial analysis. It may connect to pedestrian infrastructure, road extraction, transportation infrastructure, or walkability mapping.

---

### 4. Reconstructing Multi-Decadal Forest Disturbances: A Spatio-Temporal Transformer Approach

**Authors:** Linus Scheibenreif, Anton Raichuk, Maxim Neumann

**Published:** 2026-06-05

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 26

**Venue importance score included:** 0

**arXiv ID:** 2606.07249v1

**Paper link:** http://arxiv.org/abs/2606.07249v1

**PDF link:** https://arxiv.org/pdf/2606.07249v1

**Abstract:**

Accurate monitoring of forest disturbances is essential for understanding carbon dynamics and land management, yet traditional approaches typically rely on pixel-wise analysis of satellite time-series, ignoring spatial context. We present a deep learning framework that maps 38 years (1984-2022) of forest disturbance across the contiguous United States by modeling temporal trajectories and spatial neighborhoods simultaneously. By leveraging a vision transformer architecture, our approach effectively filters noise from weak supervision signals to produce spatially coherent disturbance maps. We perform exhaustive evaluations across multiple satellites (Landsat, Sentinel-1, Sentinel-2) and temporal windows (38 years and the more recent 6 years), validating performance against a novel, manually annotated validation dataset (n=300) and independent fire perimeter dataset (n=706). The results highlight the complexity of the task: while our spatio-temporal model demonstrates high precision (up to 98.2% for +-1 year detection on MTBS and up to 71.3% on the CONUS validation datasets, with F1-scores up to 75.8% and 47.3%, respectively) and effectively reduces spatial artifacts, it exhibits performance trade-offs across different disturbance regimes compared to pixel-wise baselines. Our method offers a promising foundation for consistent forest monitoring.

**Why this may be relevant:**

It is directly related to remote sensing or Earth observation workflows.

---

### 5. RhinoVLA Technical Report

**Authors:** Huixi Intelligence, :, Chen Zhang, Chenyang Zhou, Guanglei Ding, Guanghui He, Haibin Gao, Jiajia Chen

**Published:** 2026-06-05

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 25

**Venue importance score included:** 0

**arXiv ID:** 2606.07383v1

**Paper link:** http://arxiv.org/abs/2606.07383v1

**PDF link:** https://arxiv.org/pdf/2606.07383v1

**Abstract:**

Vision-Language-Action (VLA) models have shown strong potential for robotic manipulation, but real-time deployment on edge hardware remains challenging. In this work, we identify VLM visual and context tokens as a major source of deployment latency: for GEMM-dominated projection operators, computation grows linearly with the number of input tokens when model dimensions are fixed. Motivated by this observation, we propose RhinoVLA, a deployment-oriented VLA model co-designed with the Huixi R1 edge SoC. RhinoVLA adopts a token-efficient Qwen3-VL backbone and a continuous Action Expert, reducing the VLM-side token and computation burden while preserving pretrained multimodal capability. To support cross-robot learning, RhinoVLA further introduces a unified interface that combines View Registry, 72D physical state-action slot space, and robotinstance LoRA, allowing heterogeneous robot observations and action schemas to be aligned under a shared policy. On the deployment side, RhinoVLA is optimized through hardware-aware compilation, mixed-precision execution, and parallel visual encoding. Experiments show that RhinoVLA achieves downstream performance comparable to π0.5 at a similar parameter scale, while reaching 11.69 Hz end-to-end inference on Huixi R1, meeting the 10 Hz real-time closedloop control target. The project will be open-sourced at https://github.com/HuixiAI/RhinoVLA.

**Why this may be relevant:**

It may be useful for multimodal geospatial understanding using image-text models.

---

### 6. Geometric-Aware Hypergraph Reasoning for Novel Class Discovery in Point Cloud Segmentation

**Authors:** Zihao Zhang, Aming Wu, Yang Li, Yahong Han, Jialie Shen

**Published:** 2026-06-05

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 22

**Venue importance score included:** 0

**arXiv ID:** 2606.07280v1

**Paper link:** http://arxiv.org/abs/2606.07280v1

**PDF link:** https://arxiv.org/pdf/2606.07280v1

**Abstract:**

Novel class discovery in point cloud segmentation aims to transfer knowledge from known classes to automatically identify and segment unlabeled novel classes in point clouds. Existing methods mainly rely on pairwise associations for class assignment and novel class reasoning, which limits their ability to capture complex relationships among known and novel classes and may lead to inaccurate semantic segmentation. To address this issue, we introduce a hypergraph-based framework that models high-order associations among classes and enables collaborative reasoning from known classes to novel classes beyond traditional pairwise relations. Moreover, existing methods tend to focus on semantic feature extraction while paying insufficient attention to geometric information in point clouds. To better exploit spatial structure, we propose Geometric-Aware Prototypes to enhance the representation of class-level geometric cues. By propagating geometric information through hyperedges, the proposed method improves the understanding of spatial distributions across classes and leads to more accurate segmentation. Experiments on the SemanticKITTI and SemanticPOSS datasets demonstrate the effectiveness and superiority of our method.

**Why this may be relevant:**

It may be useful for LiDAR-based tree inventory, urban structure mapping, or 3D geospatial analysis.

---

### 7. RadiusFPS: Efficient Farthest Point Sampling on CPUs and GPUs via Spherical Voxel Pruning

**Authors:** Ziyang Yu, Xiang Li, Qiong Chang, Jun Miyazaki

**Published:** 2026-06-04

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 22

**Venue importance score included:** 0

**arXiv ID:** 2606.06255v1

**Paper link:** http://arxiv.org/abs/2606.06255v1

**PDF link:** https://arxiv.org/pdf/2606.06255v1

**Abstract:**

Point clouds are a primary sensory representation for robotic perception, underpinning LiDAR-based autonomous driving, simultaneous localization and mapping (SLAM), and navigation. Within these pipelines, Farthest Point Sampling (FPS) is the most well-known downsampling operator, as its uniform coverage preserves the geometric structure on which downstream perception relies. However, the large time complexity of classical FPS scales poorly with the million-point-per-second rates of modern 3D sensors, making it a dominant latency bottleneck that conflicts with the real-time and limited onboard compute budgets of robotic systems. Therefore, we propose RadiusFPS, an FPS acceleration framework based on spherical voxel pruning that preserves the standard FPS update rule under the same initialization and tie-breaking policy. By indexing the point cloud with spherical voxels, RadiusFPS derives a conservative geometric bound that prunes redundant distance computations in each iteration, complemented by a coordinate-wise point-skip test that removes residual updates. We further introduce RadiusFPS-G, a warp-level GPU implementation that fuses voxel selection, pruning, and distance update into memory-coalesced kernels, eliminating costly global-memory round-trips. On indoor (S3DIS, ScanNet) and outdoor LiDAR (SemanticKITTI) benchmarks, RadiusFPS-G attains up to 2.5x speedup over GPU-based FPS and matches or exceeds QuickFPS among the evaluated methods while using roughly half its GPU memory, with comparable segmentation accuracy. When coupled with the learning-based FastPoint sampler, the resulting pipeline achieves the fastest End-to-End inference among all evaluated configurations. These properties make high-quality FPS-style sampling practical for latency- and memory-constrained robotic vision.

**Why this may be relevant:**

It may be useful for LiDAR-based tree inventory, urban structure mapping, or 3D geospatial analysis.

---

### 8. Sparse Subspace-to-Expert Sharing for Task-Agnostic Continual Learning

**Authors:** Fatema Siddika, Md Anwar Hossen, Tanwi Mallick, Ali Jannesari

**Published:** 2026-06-05

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 21

**Venue importance score included:** 0

**arXiv ID:** 2606.07500v1

**Paper link:** http://arxiv.org/abs/2606.07500v1

**PDF link:** https://arxiv.org/pdf/2606.07500v1

**Abstract:**

Continual learning in Large Language Models (LLMs) is hindered by the plasticity-stability dilemma, where acquiring new capabilities often leads to catastrophic forgetting of previous knowledge. Existing methods typically treat parameters uniformly, failing to distinguish between specific task knowledge and shared capabilities. We introduce Mixture of Sparse Experts for Task Agnostic Continual Learning (SETA), a framework that resolves the plasticity-stability conflict through adaptive sparse subspace decomposition into task-specific expert modules. Unlike standard updates, where tasks compete for the same parameters, SETA separates knowledge into unique experts, designed to isolate task-specific patterns, and shared experts, responsible for capturing common features. This structure is maintained through adaptive elastic anchoring and a routing-aware regularization that jointly protect shared knowledge at both the weight and routing levels and enable a unified gating network to automatically retrieve the correct expert combination during inference. Extensive experiments across diverse domain-specific benchmarks demonstrate that SETA achieves competitive or superior overall performance relative to state-of-the-art continual learning baselines, with particularly strong retention of early-task knowledge and improved backward transfer on LLaMA-2 7B and Qwen3-4B.

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis.

---

### 9. Beyond Backscatter: InSAR coherence from detected SAR images

**Authors:** Francescopaolo Sica, Andrea Pulella, Michael Schmitt

**Published:** 2026-06-05

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 19

**Venue importance score included:** 0

**arXiv ID:** 2606.07374v1

**Paper link:** http://arxiv.org/abs/2606.07374v1

**PDF link:** https://arxiv.org/pdf/2606.07374v1

**Abstract:**

In this work, we propose a deep learning framework for coherence regression directly from detected SAR images, without the need for accurate coregistration. A Residual U-Net is trained using coherence maps derived from precisely coregistered Sentinel-1 SLC data to learn the relationship between backscatter magnitudes and coherence. The model is trained on 12-day SLC pairs and evaluated across different datasets, including coregistered SLC products and open access analysis-ready data, covering diverse radiometric properties, geometries, and locations. Experimental results demonstrate that the proposed method achieves high-resolution coherence regression with improved accuracy compared to existing intensity-based approaches. The network generalizes well across diverse geographical locations and even across different temporal baselines that were never seen at training time. Additionally, the ability to operate on globally available analysis-ready data, such as ground range detected data, e.g., distributed through Google Earth Engine, enables its large-scale application in mission design, change monitoring, and diverse mapping tasks.

**Why this may be relevant:**

It matched the geospatial machine learning search criteria and may be worth screening.

---

### 10. An Integrated Roadside Sensing and Communication Framework for Vulnerable Road User Safety at Signalized Intersections

**Authors:** Parvez Anowar

**Published:** 2026-06-05

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 18

**Venue importance score included:** 0

**arXiv ID:** 2606.07016v1

**Paper link:** http://arxiv.org/abs/2606.07016v1

**PDF link:** https://arxiv.org/pdf/2606.07016v1

**Abstract:**

Vulnerable road users (VRUs) account for approximately half of urban traffic deaths globally, with intersections concentrating a disproportionate share of these casualties. Recent reviews of sensing technology for VRU protection have cataloged dozens of single-sensor and dual-sensor deployments, yet none of the surveyed systems couples multi-modal sensing with edge-side near-miss analytics and bidirectional vehicle-to-everything (V2X) and pedestrian-to-everything (P2X) messaging in a single intersection cabinet. This paper presents an integrated framework for VRU protection at signalized intersections, combining LiDAR, radar, RGB camera, and thermal camera at the perception layer, edge-based prediction and surrogate-safety analytics at the computation layer, V2X and P2X messaging at the communication layer, and adaptive signal control at the actuation layer. The framework is grounded in an empirical case study using R-LiViT, the first publicly released roadside LiDAR-Visual-Thermal dataset, which provides 200 multi-modal sequences and 2,400 annotated RGB-T frames at three German intersections. Analysis of 53,319 detection annotations reveals that VRUs comprise approximately 49% of all road-user observations, that day-to-night density drops by 38% for pedestrians and 45% for vehicles while the night distribution shows a higher close-proximity share, that per-frame close-proximity event counts vary approximately 10-fold across the eight unique locations at three intersections, and that 83% of pedestrian bounding boxes are small in image space, indicating that VRUs are typically far from any single sensor. These findings support multi-modal sensing, edge-side analytics, and adaptive context-sensitive deployment rather than uniform single-sensor solutions.

**Why this may be relevant:**

It may be useful for LiDAR-based tree inventory, urban structure mapping, or 3D geospatial analysis. It may connect to pedestrian infrastructure, road extraction, transportation infrastructure, or walkability mapping.

---

