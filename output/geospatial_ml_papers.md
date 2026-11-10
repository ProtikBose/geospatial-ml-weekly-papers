# Weekly Geospatial ML Papers

**Search window:** 2026-11-02 to 2026-11-09

**Sources:** arXiv and Semantic Scholar

**Total selected papers:** 10

This digest focuses on geospatial analysis, urban climate, urban planning, infrastructure, and geospatial problem-solving using ML, computer vision, LLMs, VLMs, foundation models, self-supervised learning, and related methods.

Only papers from the selected top journals, conferences, or workshops are included by default. The venue importance score is included in **My Score**.

## Top Papers

### 1. Using GeoAI and machine learning tools for consistent high-resolution land cover mapping based on time-series NAIP imagery

**Authors:** Jie Liu, Xusheng Tang, Chao Wang, Zhengxiao Yan, Yuchen Dai, Qi Zhang, Conghe Song

**Published:** 2026-11-03

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 38

**Venue importance score included:** 0

**DOI:** 10.1007/s10980-026-02358-3

**arXiv ID:** 2611.04470v1

**Paper link:** http://arxiv.org/abs/2611.04470v1

**PDF link:** https://arxiv.org/pdf/2611.04470v1

**Abstract:**

High-resolution land-cover maps support ecological monitoring, but consistent historical time series remain scarce because aerial imagery varies across years and sensors. We developed a dual-track workflow to produce temporally coherent 1-m land-cover maps from National Agricultural Imagery Program (NAIP) imagery without historical training samples. For higher-quality imagery from 2009-2017, we used a pretrained U-Net/ResNet-34 model and refined boundaries with the Segment Anything Model (SAM). For lower-quality imagery from 2004-2008, we reconstructed land cover through an NLCD-based spatiotemporal bridging and label back-casting pipeline. Evaluation across six counties in North Carolina and Pennsylvania yielded overall accuracies of 0.887 (2014), 0.886 (2017), and 0.733 (2004). Structure, Water, Wetland, and Cropland consistently achieved high F1-scores. The workflow integrates GeoAI and multiple data sources to address temporal heterogeneity in historical aerial imagery, supporting high-resolution land-change analysis and landscape planning across the conterminous United States.

**Why this may be relevant:**

It matched the geospatial machine learning search criteria and may be worth screening.

---

### 2. ROAM: Retrieval-Augmented Optimization for Feasible Multi-Day Itinerary Planning

**Authors:** Ye Zihao, Lin Xiaoheng

**Published:** 2026-11-06

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 37

**Venue importance score included:** 0

**arXiv ID:** 2611.09407v1

**Paper link:** http://arxiv.org/abs/2611.09407v1

**PDF link:** https://arxiv.org/pdf/2611.09407v1

**Abstract:**

Large language models (LLMs) can draft plausible travel itineraries, but the plans they produce are frequently infeasible: attractions are grouped into days without regard for geography, opening hours are ignored, and a single generation pass cannot reliably organize a multi-day trip. We present ROAM, a retrieval-augmented agentic framework for spontaneous multi-day itinerary planning that couples semantic preference retrieval with explicit spatiotemporal optimization. ROAM embeds the natural-language request, retrieves a compact candidate set from a curated point-of-interest (POI) database, partitions candidates into day groups through maximal-clique analysis and K-means, orders each day with a quality-biased simulated-annealing TSP solver, and repairs hard opening-hour violations with greedy exchange. A spatiotemporal retrieval layer injects weather forecasts, real road distances and POI operating hours into the prompt, after which the LLM renders a structured, map-ready itinerary; an interactive ReAct-style replanning agent then supports natural-language edits while re-checking feasibility. Across four Chinese cities and 510 POIs, ROAM produces 27.5 POIs per three-day plan versus 19.3 for a bare LLM and 17.0 for a retrieval-only baseline (+42% and +62%), while reducing route dispersion from 2,101 to 677 (3.1x). Ablations show that spatial optimization is the dominant driver of route efficiency and that hard time-window repair prevents roughly 30% of attractions from violating operating hours.

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis.

---

### 3. AnimWeb-Bench: Benchmarking Animated Webpage Code Generation from Videos

**Authors:** Zhongyi Zhang, Jingyu Xiao, Shuqing Li, Michael R. Lyu

**Published:** 2026-11-06

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 29

**Venue importance score included:** 0

**arXiv ID:** 2611.09769v1

**Paper link:** http://arxiv.org/abs/2611.09769v1

**PDF link:** https://arxiv.org/pdf/2611.09769v1

**Abstract:**

Animation is pervasive on the Web, the CSS animation property alone appears on over three-quarters of webpages. Yet existing webpage code generation benchmarks target static screenshots, user-triggered interactions, or isolated motion graphics, leaving the ability of multimodal large language models (MLLMs) and coding agents to reconstruct complete animated webpages largely unexplored. To fill this gap, we introduce AnimWeb-Bench, the first benchmark for animated webpage code generation from videos. It comprises 124 real-world webpages spanning 7 application domains and 33 animation types, with 91.9% of pages combining multiple types, each paired with a reference video and the static assets of the original webpage. We further propose a human-aligned, two-dimensional evaluation protocol: Static Appearance Fidelity measures structure, text, color, and visual similarity on aligned keyframes, while Animation Fidelity tracks UI components across frames and compares their position, size, velocity, and appearance with those in the reference video. Evaluating 14 MLLMs and three coding agents reveals: (1) reproducing webpage animations is substantially more difficult than reproducing static appearance; (2) explicit frame inspection and render feedback improve the reconstruction quality of coding agents; and (3) rapid, continuous changes are harder to reproduce than discrete state transitions. Our code and dataset are available at https://starry1001.github.io/AnimWeb-Bench-website/ .

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis.

---

### 4. Assessing the Impact of Retrieval-Augmented Generation on Algorithmic Problem-Solving

**Authors:** Gabriel Souza Baggio, Gabriel Machado Lunardi, Guilherme Medeiros Machado, Subhankar Maity, Faiza Belbachir, José Palazzo Moreira de Oliveira

**Published:** 2026-11-06

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 23

**Venue importance score included:** 0

**arXiv ID:** 2611.09791v1

**Paper link:** http://arxiv.org/abs/2611.09791v1

**PDF link:** https://arxiv.org/pdf/2611.09791v1

**Abstract:**

Competitive programming problems pose distinctive challenges for Large Language Models, as they demand not only proficient code generation but also advanced algorithmic reasoning. This study presents a Retrieval-Augmented Generation approach specifically designed to enhance the capacity of Large Language Models to address such problems. Our approach integrates an embedding-based retrieval mechanism and a similarity search algorithm to identify analogous problems within a knowledge database, employing a dynamically adjusted threshold to mitigate retrieval noise. We conducted an evaluation using the CodeContests dataset, focusing on the test split problems that exhibit similarity to instances from the training split. The experimental framework considered three conditions: (i) problems provided solely with their original descriptions, (ii) problems supplemented with randomly selected examples from the training split, and (iii) problems augmented with similar examples retrieved through the proposed method. In addition, we incorporated a Min-K membership inference analysis to examine whether the generated code solutions were influenced by potential memorization of training data within the evaluated Large Language Models. This complementary perspective enables a deeper understanding of model behavior by distinguishing genuine generalization through retrieval from implicit recall of pretraining samples. Performance was assessed using both pass rates and the CodeForces Elo rating of the problems. The results provide empirical evidence that similarity-based retrieval substantially enhances Large Language Models performance in competitive programming scenarios, offering an scalable framework for improving code generation in algorithmic problem-solving contexts.

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis. It may help with cross-city, cross-region, or cross-sensor generalization.

---

### 5. Dual Architecture Fusion Vehicle Lidar 3D Target Detection

**Authors:** Muyun Li, Weizheng Jin, Yuan Sun

**Published:** 2026-11-06

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 23

**Venue importance score included:** 0

**DOI:** 10.1109/CAIBDA70336.2026.11621474

**arXiv ID:** 2611.09664v1

**Paper link:** http://arxiv.org/abs/2611.09664v1

**PDF link:** https://arxiv.org/pdf/2611.09664v1

**Abstract:**

In this paper, a 3D backbone network (SpconvTransformer) based on the fusion of convolutional architecture branch and Transformer architecture branch is proposed. The convolution branch uses 3D sparse convolution and submanifold convolution to learn local voxel features and semantic information, and the Transformer branch uses the self-attention mechanism to model the remote relationship between voxels, uses the broad receptive field to capture rich context information, and complementing the advantages of the two architectures by fusing the local features extracted from the two branches and the global features solves the problem of limited receptive fields of 3D convolutional neural networks. The experimental results show that the average accuracy of SpconvTransformer in 3D object detection and bird's-eye view detection tasks reaches 81.45% and 88.09%, respectively, and the average directional similarity reaches 91.10%, which is significantly better than other existing algorithms.

**Why this may be relevant:**

It may be useful for LiDAR-based tree inventory, urban structure mapping, or 3D geospatial analysis.

---

### 6. Fixed-point acceleration on Neural Wasserstein manifolds

**Authors:** Vitalii Aksenov, Sebastian Gutierrez Hernandez

**Published:** 2026-11-06

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 22

**Venue importance score included:** 0

**arXiv ID:** 2611.09723v1

**Paper link:** http://arxiv.org/abs/2611.09723v1

**PDF link:** https://arxiv.org/pdf/2611.09723v1

**Abstract:**

We propose a fixed-point acceleration method for optimization over probability measures, applicable to a variety of machine learning problems. We represent probability measures as pushforwards of a reference distribution through a neural network map and equip the parameter space with the induced pullback Wasserstein metric. This geometric structure allows natural gradient descent to be interpreted as a fixed-point iteration on a Riemannian manifold. We accelerate this iteration using Riemannian Anderson mixing method, which exploits historical residuals to capture approximate second-order information without forming Hessians. In the present parametric setting, the manifold is represented by Euclidean coordinates endowed with a point-dependent metric, simplifying retraction and vector transport. We evaluate the method on multimodal sampling, PDE-based inverse problems, aggregation dynamics, Bayesian logistic regression, and generative modeling. Across the tested tasks, Anderson mixing reduces the number of natural-gradient iterations and achieves competitive performance relative to SGD and Adam in terms of both loss-gradient evaluations and wall-clock time. These results suggest that fixed-point acceleration is an efficient tool for improving the computational efficiency of training on parametric Wasserstein methods.

**Why this may be relevant:**

It matched the geospatial machine learning search criteria and may be worth screening.

---

### 7. FIND: Frequency Invariance Disentanglement for Test-Time Adaptation in LiDAR 3D Detection

**Authors:** Dongxiao Li, Zixuan Hu, Ling-Yu Duan

**Published:** 2026-11-06

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 22

**Venue importance score included:** 0

**arXiv ID:** 2611.09170v1

**Paper link:** http://arxiv.org/abs/2611.09170v1

**PDF link:** https://arxiv.org/pdf/2611.09170v1

**Abstract:**

LiDAR-based 3D Object Detection (L3OD) is a fundamental 3D perception task, yet its performance is often compromised by domain shifts arising from diverse sensor configurations and environmental conditions. Existing Test-Time Adaptation (TTA) methods primarily leverage self-supervision in the spatial domain, yet they frequently confound semantic content with domain style due to the sparse, non-Euclidean nature of point clouds. To overcome this limitation, we propose FIND (Frequency INvariance Disentanglement), a novel TTA framework that precisely disentangles domain-invariant content from domain-specific interference within the frequency domain. Our methodology utilizes B-Spline fitting to construct locally adaptive filters integrated into a dual-stream architecture: an Invariant Stream extracts robust features to guide pseudo-labeling, while a Specific Stream enforces consistency against domain perturbations. By combining invariance-driven alignment with stability-guided regularization, our approach dynamically extracts robust domain-invariant features while suppressing domain-specific interference. Extensive experiments on cross-dataset adaptation and robust corruption benchmarks demonstrate that FIND significantly outperforms state-of-the-art methods. The source code is publicly available at https://github.com/llldx03/FIND.

**Why this may be relevant:**

It may be useful for LiDAR-based tree inventory, urban structure mapping, or 3D geospatial analysis.

---

### 8. MV-IVF: Multi-Vector Retrieval via Multi-Vector Clustering

**Authors:** Kishen N Gowda, Laxman Dhulipala, Lars Gottesbüren, Rajesh Jayaram

**Published:** 2026-11-06

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 20

**Venue importance score included:** 0

**arXiv ID:** 2611.09040v1

**Paper link:** http://arxiv.org/abs/2611.09040v1

**PDF link:** https://arxiv.org/pdf/2611.09040v1

**Abstract:**

Multi-vector retrieval represents each query and document as a set of embeddings and scores relevance via fine-grained set-to-set interactions such as MaxSim (Chamfer similarity). This expressiveness improves retrieval quality over single-vector representations, but makes search substantially more expensive. Existing systems address this challenge primarily through proxy representations or filter-and-rerank pipelines that reduce candidate generation to single-vector search. We study the complementary direction of building a native IVF-style index directly over multi-vector data. We introduce MV-IVF, an inverted-file index for multi-vector retrieval built on MV-Lloyd, a new Lloyd-style algorithm for clustering point clouds under a Chamfer objective. Our key observation is that once point clouds are assigned to clusters, the center-update step reduces to standard single-vector clustering over the flattened embeddings in each cluster. This enables efficient construction of a hierarchical IVF tree with center point clouds at internal nodes. At query time, MV-IVF performs best-first beam search over the tree to identify promising leaf clusters, then scores the documents in those leaves. We further accelerate search using low-bit quantization, query compression, and cache-efficient batched search. We implement MV-IVF in MVSIC, an optimized C++ library and unified evaluation framework for multi-vector retrieval that includes several major approaches. Across BEIR and LoTTE text retrieval benchmarks, MV-IVF achieves strong latency--recall tradeoffs, the best batched throughput frontiers, and favorable build-time and index-size profiles. At $90\%$ Recall-$10$@$10$, MV-IVF achieves up to $8.03\times$ lower single-query latency and up to $173.5\times$ higher QPS than the baselines, demonstrating that native IVF-style indexing is practical and effective for scalable multi-vector retrieval.

**Why this may be relevant:**

It may be useful for LiDAR-based tree inventory, urban structure mapping, or 3D geospatial analysis. It connects to urban tree detection, canopy mapping, or vegetation analysis.

---

### 9. Extrapolation Matters: Sparse-Only Depth Completion Beyond LiDAR Coverage

**Authors:** Maximilian Jansen, Gasser Elazab, Praveen Kulkarni

**Published:** 2026-11-05

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 20

**Venue importance score included:** 0

**arXiv ID:** 2611.08782v1

**Paper link:** http://arxiv.org/abs/2611.08782v1

**PDF link:** https://arxiv.org/pdf/2611.08782v1

**Abstract:**

Extrapolation beyond LiDAR coverage is an important yet under-evaluated challenge of depth completion. In real camera--LiDAR systems, partial sensor overlap, occlusions, and limited field coverage often leave large image regions weakly observed or completely unobserved by LiDAR. Thus, we investigate depth completion in this beyond-coverage regime using only sparse supervision from raw single-sweep LiDAR, without dense depth labels, LiDAR accumulation, or pseudo-LiDAR generation. Our approach leverages a frozen monocular depth foundation model, lightweight per-frame alignment to sparse LiDAR geometry, and a refinement module that fuses the aligned prior with sparse LiDAR anchors to predict dense metric depth. To regularize learning under raw sparse supervision, we introduce a high-frequency normal-consistency loss defined as the image-space gradient of the per-pixel normal cosine discrepancy. This term penalizes spatial variation in scalar angular error; it does not directly match changes in neighboring normal vectors. We further introduce an evaluation protocol that explicitly separates LiDAR-supported and beyond-coverage regions, revealing extrapolative behavior that conventional depth-completion metrics can obscure. Our method achieves strong depth accuracy beyond LiDAR coverage while remaining competitive in LiDAR-covered regions, providing a practical way to deploy monocular foundation priors in multi-sensor systems.

**Why this may be relevant:**

It may help track foundation-model directions for Earth observation or geospatial AI. It may be useful for LiDAR-based tree inventory, urban structure mapping, or 3D geospatial analysis.

---

### 10. Lightweight Path-Aware Frontier Re-ranking for LiDAR-Based UAV Exploration

**Authors:** Duc Manh Do, Thanh Nguyen Canh, Ngoc Minh Do, Mai Thanh Thai, Xiem HoangVan

**Published:** 2026-11-06

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 15

**Venue importance score included:** 0

**arXiv ID:** 2611.09561v1

**Paper link:** http://arxiv.org/abs/2611.09561v1

**PDF link:** https://arxiv.org/pdf/2611.09561v1

**Abstract:**

Autonomous 3D exploration with UAVs requires efficient target selection under limited flight time and onboard computation. In conventional Euclidean-distance-based frontier pipelines, geometric distance may poorly represent the actual collision-free travel cost in cluttered environments, leading to inefficient frontier choices. This paper presents a lightweight path-aware frontier re-ranking method for LiDAR-based UAV exploration. The method first retains a small top-N set of promising frontier candidates using a lightweight utility function and then applies time-bounded RRT* planning to estimate their feasible path costs for re-ranking. The path generated for the selected frontier is further reused for navigation to reduce redundant global planning. Experiments in three warehouse-like environments show that the proposed method consistently produces shorter exploration trajectories than conventional frontier baselines, with traveled-distance reductions of up to 14.1%, while reducing exploration time by up to 9.5% in two environments and remaining competitive in the third. The method maintains map detail comparable to the conventional OctoMap-based baseline, demonstrating an effective trade-off between exploration efficiency and mapping quality.

**Why this may be relevant:**

It may be useful for LiDAR-based tree inventory, urban structure mapping, or 3D geospatial analysis.

---

