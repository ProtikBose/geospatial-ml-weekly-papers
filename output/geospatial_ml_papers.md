# Weekly Geospatial ML Papers

**Search window:** 2026-06-29 to 2026-07-06

**Sources:** arXiv and Semantic Scholar

**Total selected papers:** 10

This digest focuses on geospatial analysis, urban climate, urban planning, infrastructure, and geospatial problem-solving using ML, computer vision, LLMs, VLMs, foundation models, self-supervised learning, and related methods.

Only papers from the selected top journals, conferences, or workshops are included by default. The venue importance score is included in **My Score**.

## Top Papers

### 1. Multi-scale vegetation cooling assessments for urban climate adaptation: a MAUP-informed NDVI–LST analysis in Shanghai

**Authors:** Ting Zhang, Jienan Ye, Ran Xu

**Published:** 2026-06-30

**Venue:** International Journal of Climate Change Strategies and Management

**Found via:** Semantic Scholar

**My Score:** 85

**Venue importance score included:** 0

**Semantic Scholar citations:** 0

**DOI:** 10.1108/ijccsm-02-2026-0083

**Paper link:** https://www.semanticscholar.org/paper/9f60249f6352dc6e0d56eaee642ed35d6192d575

**PDF link:** https://doi.org/10.1108/ijccsm-02-2026-0083

**Abstract:**

As climate warming and urban heat exposure continue to intensify, accurately identifying the cooling effect of vegetation is essential for developing effective urban climate adaptation strategies. However, the relationship between the Normalized Difference Vegetation Index (NDVI) and Land Surface Temperature (LST) is highly sensitive to spatial scale. Inappropriate scale selection may lead to misjudgments of urban cooling potential due to the Modifiable Areal Unit Problem (MAUP). This study aims to reveal the scale dependency of the NDVI–LST relationship and assess its implications for urban green space planning and climate adaptation decision-making. Taking Shanghai as a case study, this research constructs multi-scale grids while maintaining consistent spatial resolution of remote sensing data. Land use change information from 2000 to 2024 is integrated into the analysis. By combining the Random Forest model with the SHAP interpretation method, this study examines the statistical relationship, nonlinear response structure and variations in cooling turning points of NDVI–LST across different scales and land use contexts. This approach enables a systematic assessment of how spatial aggregation methods influence the identification of vegetation cooling effects. The results show that as the analysis scale shifts from coarse to fine, local heterogeneity and contextual effects are significantly enhanced. The nonlinear response structure of NDVI–LST and its cooling thresholds undergo systematic changes with scale. At coarse scales, local fluctuations are smoothed out and the overall response becomes more stable. At fine scales, nonlinear characteristics become more pronounced and spatial differences more prominent. From the MAUP perspective, scale selection not only affects the assessment of statistical correlations but may also introduce biases in evaluating the cooling efficiency of green spaces within climate adaptation planning. This study proposes a reusable multi-scale assessment framework from the MAUP perspective. It reveals the scale sensitivity of the NDVI–LST relationship and its contextual dependency across different land use backgrounds. The findings highlight the critical value of multi-scale information in urban green infrastructure planning and heat risk management. This provides methodological innovation and practical references for developing evidence-based urban climate adaptation strategies.

**Why this may be relevant:**

It is directly related to remote sensing or Earth observation workflows. It connects to urban tree detection, canopy mapping, or vegetation analysis. It is relevant to urban climate and heat-resilience research. It is related to urban planning, infrastructure, or built-environment analysis.

---

### 2. From Raw EO Data to AI-Ready Datasets: Lowering the Barrier to Geospatial Foundation Model Fine-Tuning

**Authors:** M. Santoro, E. Boldrini, S. Nativi, P. Mazzetti

**Published:** 2026-07-02

**Venue:** Remote Sensing

**Found via:** Semantic Scholar

**My Score:** 72

**Venue importance score included:** 10

**Semantic Scholar citations:** 0

**DOI:** 10.3390/rs18132152

**Paper link:** https://www.semanticscholar.org/paper/50f7e63b9fae24b226612ab1a27f634d0c513d07

**PDF link:** https://doi.org/10.3390/rs18132152

**Abstract:**

Geospatial foundation models are a new frontier in artificial intelligence, designed to understand and analyze spatial data at scale. Trained on huge sets of EO data, these models can support a wide range of applications—from monitoring natural disasters to guiding urban development and tracking climate change. To this aim, researchers and practitioners need to fine-tune the foundation models for specific tasks, utilizing a relatively small amount of additional data. As a result, geospatial foundation models are reshaping how we observe, manage, and protect our planet. Fine-tuning a geospatial foundation model requires carefully curated training datasets that reflect specific regions, time periods, or tasks—such as detecting deforestation or mapping urban growth. Yet preparing these datasets is often labor-intensive, involving steps like selecting relevant imagery, aligning spatial formats, and generating accurate labels. In practice, this means that the effectiveness of GFMs hinges on the availability of AI-ready data. This bottleneck limits the accessibility and scalability of GFMs for scientific and operational applications. In this work, we introduce a software library designed to automate these preparatory steps, streamlining the transformation of geospatial datasets into consistent, high-quality inputs for GFM fine-tuning. By reducing technical overhead and ensuring data readiness, the library enables faster, more reliable, and more inclusive adaptation of foundation models to local environmental challenges and specialized domain needs.

**Why this may be relevant:**

It appears in one of the selected top journals, conferences, or workshops. It may help track foundation-model directions for Earth observation or geospatial AI. It is directly related to remote sensing or Earth observation workflows.

---

### 3. TerraDiT-$Ω$: Unified Spatial Control for Satellite Image Synthesis with Any Geospatial Primitive

**Authors:** Brian Wei, Srikumar Sastry, Daniel Cher, Eric Xing, Nathan Jacobs

**Published:** 2026-06-30

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 52

**Venue importance score included:** 0

**arXiv ID:** 2606.31029v1

**Paper link:** http://arxiv.org/abs/2606.31029v1

**PDF link:** https://arxiv.org/pdf/2606.31029v1

**Abstract:**

Generative models have achieved remarkable progress, yet applying them to satellite imagery remains challenging. Unlike natural imagery, satellite scenes are structured by spatially complex and semantically distinct geometries. Prior work addresses this complexity by adapting natural image frameworks using dense rasters or sparse prompts, trading off annotation cost and fidelity while breaking compatibility with vector primitives commonly used to represent geographic information. We introduce TerraDiT-$Ω$, a unified spatial control framework that generates satellite imagery directly from any native geospatial primitive. By jointly leveraging precise annotations (polygons, polylines) and coarser ones (bounding boxes, points), the model supports controllable layouts across varying annotation budgets, broadening applicability to design tasks such as urban planning while remaining naturally compatible with end-to-end GeoAI workflows. To effectively leverage these primitives during generation, we propose Geometry-Aware Local Attention, a conditioning mechanism that injects explicit geometric cues into the attention space. Across all conditioning formats, our approach consistently outperforms both dense-control and sparse-control baselines. Furthermore, this flexibility enables controllable synthetic data augmentation using a single generative model, improving downstream performance on land-cover segmentation, object detection, road graph extraction, and scene classification. Code, data, and weights are available at https://github.com/mvrl/TerraDiT.

**Why this may be relevant:**

It is directly related to remote sensing or Earth observation workflows. It is related to urban planning, infrastructure, or built-environment analysis.

---

### 4. Interpretation-Oriented Cloud Removal via Observation-Anchored Residual Flow with Geo-Contextual Alignment

**Authors:** Ziyao Wang, Maonan Wang, Yucheng He, Xianping Ma, Ziyi Wang, Hongyang Zhang, Yirong Cheng, Man-on Pun

**Published:** 2026-07-02

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 51

**Venue importance score included:** 0

**arXiv ID:** 2607.02471v1

**Paper link:** http://arxiv.org/abs/2607.02471v1

**PDF link:** https://arxiv.org/pdf/2607.02471v1

**Abstract:**

Cloud removal (CR) is essential for optical remote sensing, serving as a prerequisite for reliable downstream interpretation, such as semantic segmentation and change detection. However, existing CR approaches often prioritize visual realism while overlooking their impact on subsequent analytical tasks, leading to semantic drift and degraded downstream performance. To address this issue, we propose Geo-Anchored Cloud Removal (GACR), a unified framework that jointly ensures faithful reconstruction and robust interpretability. At its core, GACR incorporates Observation-Anchored Residual Flow (OAR-Flow), which reformulates CR as a physically grounded residual inversion process. By anchoring the generative trajectory to the cloudy observation rather than pure noise, OAR-Flow enables fast, stable, and faithful reconstruction. To further preserve semantic structures critical for downstream interpretation, GACR integrates Geo-Contextual Prior Alignment (GCPA) to constrain the reconstruction within a semantic manifold induced by a Vision Foundation Model (VFM). Consequently, GACR strictly maintains the spatial-semantic integrity of complex landscapes. Extensive experiments across six CR datasets and twelve downstream tasks demonstrate that GACR produces superior reconstruction quality while consistently improving downstream task accuracy. The code is available at https://github.com/wzy6055/GACR.

**Why this may be relevant:**

It may help track foundation-model directions for Earth observation or geospatial AI. It is directly related to remote sensing or Earth observation workflows.

---

### 5. Physics-Informed Machine Learning for Agricultural Drought Prediction in Vidarbha, Maharashtra: A Multimodal Geospatial Fusion Framework for ESG

**Authors:** Anirudh Khajuria

**Published:** 2026-06-30

**Venue:** International Journal of Science and Research (IJSR)

**Found via:** Semantic Scholar

**My Score:** 43

**Venue importance score included:** 0

**Semantic Scholar citations:** 0

**DOI:** 10.21275/sr26629131639

**Paper link:** https://www.semanticscholar.org/paper/8efd2985b82091ee131afe3a7a23df53a58c852f

**PDF link:** https://www.ijsr.net/archive/v15i6/SR26629131639.pdf

**Abstract:**

: Vidarbha is one of the most drought-stricken areas of South Asia. This semi-arid agricultural belt in Maharashtra, India is characterised by extreme deficits in annual rainfall (up to 55% in some districts) and ongoing depletion of the groundwater supply, which poses a significant threat to the livelihoods of millions of small farmers. Drought monitoring methods currently used in traditional systems are based on large statistical indices that do not reflect the multi-scale localised variations in soil moisture, crop stress and aquifer depletion at the scale of the farm. In this work we present a Physics-Informed Neural Network (PINN) algorithm that integrates different forms of geospatial data (Sentinel-2 satellite imagery (at 10m resolution), India-WRIS piezometer time-series data, and IMD gridded rainfall fields) through a novel water-balance-constrained loss function, in an effort to produce accurate estimates of soil moisture and drought indices, at a recent time. Using this approach, we validate the model across five vulnerable districts in Vidarbha (Yavatmal, Amravati, Akola, Buldhana and Washim) over the time frame of 2018-2026 at the tehsil level. By providing a framework for transferability of this method, we anticipate that this approach can be adopted globally using large datasets acquired from the ERA5-Land and Copernicus Open Access Hub.

**Why this may be relevant:**

It is directly related to remote sensing or Earth observation workflows.

---

### 6. pykci: A Compact Urban Knowledge Graph for Semantic and Spatial Queries using LLMs

**Authors:** Huynh Duc An Son Nguyen, Lukas Arzoumanidis, Youness Dehbi

**Published:** 2026-07-02

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 42

**Venue importance score included:** 0

**arXiv ID:** 2607.01605v1

**Paper link:** http://arxiv.org/abs/2607.01605v1

**PDF link:** https://arxiv.org/pdf/2607.01605v1

**Abstract:**

CityGML, the OGC standard for modeling, storage, and exchange of semantic 3D city models, describes urban objects with detailed semantics, geometry, and topology. Yet this richness is difficult to query directly: CityGML's XML encoding is designed for exchange rather than analysis, and relational mappings expose it through schemas requiring expert knowledge. We present pykci (Python Knowledge Graph for Cities), an open-source system that transforms CityGML 2.0 datasets into a compact urban knowledge graph in Neo4j and makes it queryable in natural language. The graph schema covers all thematic feature modules of CityGML 2.0 across all levels of detail and is spatially indexed with an R-tree for efficient geometric retrieval. A complete end-to-end Python pipeline ingests CityGML datasets into the knowledge graph, exports them to OGC 3D Tiles for interactive visualization, and supports lossless round-trip export of all content back to CityGML. For querying, the graph is paired with a large language model through a model-agnostic text-to-Cypher mechanism: the graph schema is supplied as context, and the model translates natural-language questions into Cypher queries executed against the graph. We evaluate both a locally running open-weight model, which keeps sensitive city data on-premise, and a state-of-the-art commercial model for the most demanding spatial and semantic queries. Answers are grounded in exact city data rather than the model's parametric memory, reducing hallucination and providing auditable provenance for every response. We demonstrate the system on open-government CityGML LoD2 datasets from Hamburg, Germany, including complex semantic and spatial queries such as identifying roof surfaces suitable for greening. pykci enables urban planners, GIS practitioners, and citizens to interact with semantic 3D city models without expertise in query languages and database schemas.

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis. It connects to urban tree detection, canopy mapping, or vegetation analysis.

---

### 7. DemoPSD: Disagreement-Modulated Policy Self-Distillation

**Authors:** Yunhe Li, Hao Shi, Wenhao Liu, Mengzhe Ruan, Hanxu Hou, Zhongxiang Dai, Shuang Qiu, Linqi Song

**Published:** 2026-07-02

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 35

**Venue importance score included:** 0

**arXiv ID:** 2607.02502v1

**Paper link:** http://arxiv.org/abs/2607.02502v1

**PDF link:** https://arxiv.org/pdf/2607.02502v1

**Abstract:**

On-policy self-distillation (OPSD) has emerged as a practical method for training large language models (LLMs) to reason, where a single model acts as both the teacher and the student with different levels of information access. However, recent studies have found that the teacher's dense token-level supervision, conditioned on privileged information, can lead to overfitting to in-domain patterns, suppress exploration, and hurt cross-domain generalization, while also introducing a more fundamental issue: *privileged information leakage*, where the student encodes answer-dependent shortcuts that are unavailable at test time. We introduce **DemoPSD**, a novel framework that resolves such problems through the idea of *selective adoption of teacher guidance*. Instead of fitting the full teacher distribution, DemoPSD steers the student toward a *reverse-KL barycenter target*, a weighted geometric combination of the teacher and student distributions, that naturally balances learning from the teacher with preserving the student's own reasoning capacity. We measure the difference between their distributions and use such a discrepancy to adaptively control the blending at each token position. We provably show that DemoPSD achieves **(1)** *leakage attenuation*, i.e., effective mitigation of privileged information leakage; and **(2)** *exploration preservation*, i.e., preservation of exploration capacity under dense token-level distillation. Extensive experiments on SciKnowEval across four scientific fields show that DemoPSD outperforms both GRPO and SDPO while maintaining higher training entropy and robustly generalizing to out-of-distribution GPQA benchmarks.

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis. It may help with cross-city, cross-region, or cross-sensor generalization.

---

### 8. Bringing Agentic Search to Earth Observation Data Discovery

**Authors:** Minghan Yu, Youran Sun, Chugang Yi, Yixin Wen, Haizhao Yang

**Published:** 2026-07-02

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 28

**Venue importance score included:** 0

**arXiv ID:** 2607.02387v1

**Paper link:** http://arxiv.org/abs/2607.02387v1

**PDF link:** https://arxiv.org/pdf/2607.02387v1

**Abstract:**

NASA and its data centers hold thousands of geoscience datasets and tools like Worldview, Giovanni, the Science Discovery Engine, and Harmony. Finding the right one is hard even for domain experts. We present an agentic search system, deployed as a public service for the geoscience community, that takes a natural-language research query and returns the matching datasets and tools. We demonstrate that, in the era of large language models, the latent value of knowledge graphs (KGs) can be substantially amplified through agentic search. From the NASA Earth Observation Knowledge Graph (NASA EO-KG) we derive NASA-EO-Bench, an open benchmark of 47k query-dataset pairs (21k task-based queries). A neural scorer fine-tuned on NASA-EO-Bench beats cosine and BM25 baselines. Further combining it with BM25 via score fusion raises both Recall@10 (R@10) and MRR by over 5x. On top of this supervised pipeline, we add a zero-shot agentic reranking stage that, without any additional training, lifts MRR by 28% on a stratified N=200 subset, showing that LLM reasoning is complementary to supervised retrieval.

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis. It is directly related to remote sensing or Earth observation workflows.

---

### 9. Learning to Move Before Learning to Do: Task-Agnostic pretraining for VLAs

**Authors:** Junhao Shi, Siyin Wang, Xiaopeng Yu, Li Ji, Jingjing Gong, Xipeng Qiu

**Published:** 2026-07-02

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 16

**Venue importance score included:** 0

**arXiv ID:** 2607.02466v1

**Paper link:** http://arxiv.org/abs/2607.02466v1

**PDF link:** https://arxiv.org/pdf/2607.02466v1

**Abstract:**

Vision-Language-Action (VLA) models are fundamentally bottlenecked by the scarcity of expert demonstrations -- triplets of observations, instructions, and actions that are costly to collect at scale. We argue that this bottleneck stems from conflating two distinct learning objectives: acquiring physical competence (how to move) and acquiring semantic alignment (what to do). Crucially, only the latter requires language supervision. Building on this Decomposition Hypothesis, we propose Task-Agnostic Pretraining (TAP), a two-stage framework that first learns transferable motor priors from cheap, unlabeled interaction data -- including discarded off-task trajectories and autonomous robot play -- via a self-supervised Inverse Dynamics objective. A lightweight second stage then grounds these priors in language using minimal expert data. On the SIMPLER benchmark, TAP matches models trained on over 1M expert trajectories while using orders of magnitude less labeled data, yielding a 10% absolute gain over standard behavior cloning. On a real-world WidowX platform, TAP retains 25% success under camera perturbations where internet-scale baselines collapse to 0%, demonstrating that task-agnostic pretraining produces robust, transferable physical representations and offers a scalable path forward for Embodied AI.

**Why this may be relevant:**

It matched the geospatial machine learning search criteria and may be worth screening.

---

### 10. Open-Weather Robust 3D Detection via Dual-Critic Diffusion Alignment

**Authors:** Shuyao Li, Chuanxing Geng, Heyang Sun, Qiang Zhou, Jingjing Gu

**Published:** 2026-07-02

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 16

**Venue importance score included:** 0

**arXiv ID:** 2607.01983v1

**Paper link:** http://arxiv.org/abs/2607.01983v1

**PDF link:** https://arxiv.org/pdf/2607.01983v1

**Abstract:**

Robust 3D object detection under adverse weather remains a critical hurdle for autonomous driving. Despite progress with LiDAR-4D radar fusion, most methods are constrained by a closed-world assumption, implicitly requiring training and test weather to align in both type and severity. This premise fails in practice: the open-ended nature of weather, and even variations within a single type like rain, cause dramatically different LiDAR degradation patterns, leading to significant performance drops in unseen conditions. To address this, we present Dual-Critic Guided Diffusion Alignment (DCDA), a weather-agnostic framework that learns to recover degraded LiDAR features toward a clean manifold. Rather than modeling specific weather types, DCDA employs a 4D radar-conditioned diffusion process to progressively refine features, guided by two complementary critics. (i) A detection-guided critic, anchored by a pre-trained clean-weather model, ensures that the refined features retain object-level discriminability and localization accuracy. (ii) A weather adversarial critic enforces holistic distributional consistency with clean-weather representations. By aligning features through semantic and distributional constraints rather than explicit weather modeling, DCDA generalizes effectively to unseen weather types and severities without requiring paired data or weather labels. We further introduce a structured open-weather benchmark with held-out type-severity combinations and extensive experiments verify DCDA's advantages.

**Why this may be relevant:**

It may be useful for LiDAR-based tree inventory, urban structure mapping, or 3D geospatial analysis.

---

