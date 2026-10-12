# Weekly Geospatial ML Papers

**Search window:** 2026-10-05 to 2026-10-12

**Sources:** arXiv and Semantic Scholar

**Total selected papers:** 10

This digest focuses on geospatial analysis, urban climate, urban planning, infrastructure, and geospatial problem-solving using ML, computer vision, LLMs, VLMs, foundation models, self-supervised learning, and related methods.

Only papers from the selected top journals, conferences, or workshops are included by default. The venue importance score is included in **My Score**.

## Top Papers

### 1. Revisiting the Task of Building Damage Assessment by Satellite Imaging

**Authors:** Anthony Cioppa, Virgile Blua, Sébastien Piérard, Pietro Ceccato, Marc Van Droogenbroeck

**Published:** 2026-10-09

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 81

**Venue importance score included:** 0

**arXiv ID:** 2610.13857v1

**Paper link:** http://arxiv.org/abs/2610.13857v1

**PDF link:** https://arxiv.org/pdf/2610.13857v1

**Abstract:**

Natural disasters such as earthquakes, tropical storms, and floods cause extensive damage to buildings, and rapid, reliable damage maps are essential to guide emergency response. Automating this task, referred to as building damage assessment (BDA), from satellite imagery, has become an active research topic at the intersection of remote sensing, computer vision, and machine learning, particularly since supervised deep learning methods were shown to outperform earlier handcrafted approaches. Yet, despite a decade of intense activity and the release of several large-scale datasets, the field lacks a shared foundation. This chapter revisits the task of BDA from first principles, organized around three pillars: data, evaluation, and methods. We first clarify the candidate task for- mulations and argue for a sensor-agnostic, instance-based definition that tolerates missing pre-event imagery. We then review existing datasets along the axes of sensing modality, temporal configuration, and geographic coverage. On the evaluation side, we show that prevailing practices, largely based on a single aggregate score, are theoretically fragile, and we lay the foundations of a more informative, ranking-based, multi-score protocol. We further review methods ranging from task-specific deep networks to recent Earth observation foundation models, noticing that generalization to unseen events and regions remains an open difficulty. Finally, we discuss how these elements can inform the organization of a BDA challenge, including cross-validation, challenge, and private data-sharing setups designed to build trust between developers and users.

**Why this may be relevant:**

It may help track foundation-model directions for Earth observation or geospatial AI. It is directly related to remote sensing or Earth observation workflows. It may help with cross-city, cross-region, or cross-sensor generalization.

---

### 2. GeoFitBench-LLM: A Benchmark for Assessing Large Language Models' Capabilities in Geospatial Data Requirements Elicitation for Geo-Analytic Tasks

**Authors:** Amirhossein Vahdat, Thierry Badard, Luc Lamontagne

**Published:** 2026-10-08

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 53

**Venue importance score included:** 0

**DOI:** 10.5281/zenodo.20129011

**arXiv ID:** 2610.12669v1

**Paper link:** http://arxiv.org/abs/2610.12669v1

**PDF link:** https://arxiv.org/pdf/2610.12669v1

**Abstract:**

Large language models are becoming central to GeoAI systems, yet their evaluation rarely considers the elicitation of geospatial data requirements. This omission is critical as retrieval oriented geo-analytic tasks cannot be supported reliably without first identifying the necessary datasets and constraints. GeoFitBench-LLM is introduced as a benchmark for assessing whether LLMs can infer the datasets, the supporting resources and the constraints required by geo-analytic requests in natural language. The benchmark is structured around two reasoning dimensions, Spatio-Temporal Relational and Semantic Grounding, reflecting long-standing challenges in geospatial information retrieval and related natural language tasks. Ground truth requirements are encoded in a fixed, provider-independent schema for reproducible evaluation of resource identification and attribute-level specification. Experiments on seven models under minimal prompting indicate that identifying the necessary resources is often achievable, with GPT-5.4 Thinking achieving the best result by recovering the complete set of resources in 66.67% of benchmark requests. Results further indicate that accurate fitness-for-use specification remains more difficult as inferential demands increase.

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis.

---

### 3. Shortcut Learning in Geospatial Foundation Model Embeddings for Cross-Disaster Damage Assessment

**Authors:** Ali Shibli, Andrea Nascetti, Yifang Ban

**Published:** 2026-10-09

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 45

**Venue importance score included:** 0

**arXiv ID:** 2610.13766v1

**Paper link:** http://arxiv.org/abs/2610.13766v1

**PDF link:** https://arxiv.org/pdf/2610.13766v1

**Abstract:**

Geospatial foundation models can support disaster damage assessment, but high accuracy on familiar disasters may hide shortcut learning: prediction from event or scene characteristics rather than evidence that transfers to a new disaster. We study embeddings from TerraMind, Prithvi-EO-2.0, DOFA, and DINOv3 on the multi-disaster datasets xView2 and BRIGHT. Holding out an entire disaster, instead of randomly splitting image tiles, reduces mean balanced accuracy from 0.807 to 0.638 on xView2 and from 0.818 to 0.568 on BRIGHT. Four sets of tests examine what information supports prediction: event and acquisition context, before/after image inputs, building count, and correct image pairing. Pre-event images remain predictive, and a classifier given only the annotated number of buildings reaches balanced accuracy of 0.629 and 0.653. Combining before/after features performs best on average on xView2, but does not improve over pre-only features on BRIGHT. Shuffling image pairs within the same disaster and damage class causes modest losses. Motivated by these findings, we test whether feature transformations learned only from training disasters improve generalization to unseen disasters. These transformations improve performance, with supervised contrastive learning performing best on xView2 and PCA on BRIGHT. Our results highlight the importance of evaluation on unseen domains for assessing model robustness and show that simple feature-level transformations can improve generalization. Code and experiments can be found at https://github.com/alishibli97/gfm-shortcut-learning.

**Why this may be relevant:**

It may help track foundation-model directions for Earth observation or geospatial AI. It may help with cross-city, cross-region, or cross-sensor generalization.

---

### 4. Anaximander: Interactively Running Geospatial Deep Learning Models on Any Compute Backend

**Authors:** satej soman, Akram Zaytar, G. Tadesse, G. Hacheme, M. S. Danish, I. Becker-Reshef, Rahul Dodhia, J. Ferres

**Published:** 2026-10-06

**Found via:** Semantic Scholar

**My Score:** 44

**Venue importance score included:** 0

**Semantic Scholar citations:** 0

**arXiv ID:** 2610.09085

**Paper link:** https://www.semanticscholar.org/paper/e51007fc3b142b4a770cc53327946c52445f9191

**Abstract:**

Applying deep learning models to satellite imagery from within geographic information systems (GIS) remains high-friction for remote sensing practitioners. Models arrive in incompatible formats and target different compute environments, from local workstations to serverless cloud services. As a result, every evaluation demands custom deployment, tiling, and georeferencing code before a single prediction reaches the analyst's map. This friction discourages systematic comparison in a domain where model choice directly affects operational outcomes such as field delineation, crop monitoring, and disaster response. We present Anaximander, an open-source system that unifies model source and compute location choice behind one interactive interface. The system's backend is an inference server that loads models from multiple commonly-used sources and serves them on any accessible compute backend. The server provides session management and model caching, and streams results back per tile. The backend is paired with a QGIS plugin that drives tiling, result reassembly, georeferencing, and real-time per-tile status visualization. An additional user-interface path injects layer legends as prompts into vision-language models. We demonstrate the system in a code-free side-by-side comparison of three heterogeneous models on an agricultural field delineation task: gpt-image-1 via a cloud API, Segment Anything Model 3 (SAM3) on a remote GPU, and DelineateAnything on a local CPU. The inference backend and protocol are open-source and available at https://github.com/microsoft/nxmndr.

**Why this may be relevant:**

It is directly related to remote sensing or Earth observation workflows.

---

### 5. PlacePulse: Learning Transferable Place Representations from Structural Geographic Data

**Authors:** Lucía García-Duarte, Miguel Álvarez, Diego Vicente, Javier Pérez Trufero, Javier de la Torre

**Published:** 2026-10-09

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 35

**Venue importance score included:** 0

**arXiv ID:** 2610.13390v1

**Paper link:** http://arxiv.org/abs/2610.13390v1

**PDF link:** https://arxiv.org/pdf/2610.13390v1

**Abstract:**

Geospatial machine learning often depends on task-specific feature engineering over large collections of sociodemographic, business, and environmental variables. Geospatial foundation models offer reusable representations of place, but leading approaches typically encode dynamic signals, such as mobility and search activity, or visual signals from satellite imagery. Few models represent the static structural composition of places (who lives and works there, which businesses operate there, and which risks they face) as transferable embeddings at fine spatial resolution. We introduce PlacePulse, a structural geospatial foundation model that compresses 572 attributes, expanded to 2,288 inputs through H3 neighborhood aggregates, into 256-dimensional unit-norm embeddings for 1,055,537 H3 resolution-7 cells in the United States. We also introduce a reusable two-axis benchmark that separates intrinsic representation quality from downstream predictive utility across multiple targets and spatial supports. Intrinsically, the embeddings reconstruct standardized inputs with mean $R^2 = 0.853$, use 251 of 256 approximately decorrelated dimensions, and show strong spatial organization, with Moran's $I = 0.93$ on the leading principal component and autocorrelation persisting beyond the input radius. Extrinsically, across 74 held-out targets from 12 external sources and four spatial supports, PlacePulse outperforms a dimensionality-matched feature-selection baseline on targets unrelated to the training inputs and is competitive with Google's Population Dynamics Foundation Model, leading on health, economic, election, economic-mobility and social-vulnerability outcomes, with relative strengths that vary by domain. These findings position structural composition as a distinct and complementary modality for geospatial foundation models, not simply a fallback where behavioral or imagery data are unavailable.

**Why this may be relevant:**

It may help track foundation-model directions for Earth observation or geospatial AI. It is directly related to remote sensing or Earth observation workflows.

---

### 6. MeshBind: Point-to-Mesh Binding for Non-Rigid Scene Flow Automatic Annotation

**Authors:** Yinqi Chen, E Li, Shuaijun Wang, Weiyuan Peng, Meiying Zhang, Qi Hao

**Published:** 2026-10-09

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 28

**Venue importance score included:** 0

**arXiv ID:** 2610.12895v1

**Paper link:** http://arxiv.org/abs/2610.12895v1

**PDF link:** https://arxiv.org/pdf/2610.12895v1

**Abstract:**

Scene flow estimation is essential for many autonomous driving (AD) and robotic applications, but obtaining ground-truth scene flow for non-rigid objects such as pedestrians is highly difficult. We present MeshBind, an automatic annotation method that uses mesh models to generate per-point scene flow for non-rigid objects. The novelty of this work is threefold: 1) developing a multi-view module that reconstructs an articulated mesh model from six surround cameras and registers it to the LiDAR frame; 2) developing a local-frame binding technique that attaches each point to the mesh via a per-triangle tangent-normal frame, invariant under rigid motion yet adaptive to articulated deformation; 3) developing a three-layer flow registration pipeline that combines ego-vehicle motion compensation, box binding, and mesh binding to produce full-scene per-point flow. We implement MeshBind in SF-Studio, an interactive annotation tool that visualises flow and allows human mesh corrections with automatic recomputation. We also release SFB (SUScape-Flow Benchmark), a large-scale benchmark built on the public SUScape dataset, covering 41k frames with per-point non-rigid pedestrian annotations and a Rigid/Semi-Rigid/Non-Rigid evaluation protocol. Experiments show that fine-tuning on SFB reduces three-way endpoint error (EPE) by 2-3x, and brings non-rigid EPE to the same level as rigid EPE.

**Why this may be relevant:**

It may be useful for LiDAR-based tree inventory, urban structure mapping, or 3D geospatial analysis. It may connect to pedestrian infrastructure, road extraction, transportation infrastructure, or walkability mapping.

---

### 7. An Annealing-based Quantum Neural Network with Discrete Wavelet Transforms for Enhanced Air Pollution Nowcasting

**Authors:** Otto Menegasso Pires, André Saimon, Daniela Herrmann, Prashant Kumar, Marcelo Moret, Erick Giovani Sperandio Nascimento

**Published:** 2026-10-09

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 25

**Venue importance score included:** 0

**arXiv ID:** 2610.13882v1

**Paper link:** http://arxiv.org/abs/2610.13882v1

**PDF link:** https://arxiv.org/pdf/2610.13882v1

**Abstract:**

Air pollution poses a significant threat to public health, exacerbated by the rapid industrialization and urbanization of modern society. While traditional deep learning offers predictive capabilities, recent advancements in quantum machine learning (QML) present a compelling alternative. Here, we introduce a scalable hybrid framework that integrates variational quantum circuits with quantum annealing. Leveraging a neuromorphic quantum computing platform to transcend the qubit limitations of the NISQ era, we model particulate matter (PM$_{2.5}$) dynamics using high-density urban data from the UK. We demonstrate that our Quantum Neural Networks (QNNs) exhibit an intrinsic resilience to input volatility, significantly outperforming classical baselines (MLP and LSTM) on raw, high-entropy environmental data. Furthermore, we successfully scaled the model to 172 qubits, observing a synergistic enhancement when coupled with wavelet decomposition that achieves state-of-the-art predictive fidelity. These findings establish a critical benchmark for quantum utility, proving that scalable, neuromorphic quantum machine learning can now address complex, non-linear real-world problems.

**Why this may be relevant:**

It matched the geospatial machine learning search criteria and may be worth screening.

---

### 8. Hide and Seek: HIDE Concepts to SEEK explanations for black box models

**Authors:** Bhanu Tokas, Rahul Nair, Rockwell Jackson, Hannah Kerner

**Published:** 2026-10-09

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 20

**Venue importance score included:** 0

**arXiv ID:** 2610.13935v1

**Paper link:** http://arxiv.org/abs/2610.13935v1

**PDF link:** https://arxiv.org/pdf/2610.13935v1

**Abstract:**

Interpreting machine learning model predictions is a central challenge, particularly for black-box vision models. Concept-based attribution methods interpret models using human-understandable concepts. Existing concept-based methods can only interpret classification and regression models. They require access to model weights or large concept-annotated datasets, and most methods cannot provide image-level attribution. We propose Hide and Seek (HnS), a new method for concept-level attribution that does not require access to model weights or labeled concept datasets. HnS can interpret a wide range of vision models. Given a concept and image set, HnS retrieves concept-aligned images using a vision-language model, localizes the concept within each image, masks the localized region, and measures attribution from the change in the black-box model's output between the original and masked images. This enables faithful attribution by directly measuring the model's behavior and supporting local attributions. We validated HnS on CelebA and COCO-Stuff. Compared to existing methods, HnS showed better agreement with ground-truth attributions. We demonstrated the applicability of HnS on diverse tasks, including image captioning and satellite image segmentation, where no existing concept attribution method can be used. We provided our anonymous code in the supplementary material.

**Why this may be relevant:**

It is directly related to remote sensing or Earth observation workflows.

---

### 9. MOSAIC: Multi-Scale Object-Centric Slot Adaptation with Image-Guided Prototype Conditioning for Remote Sensing Image Super-Resolution

**Authors:** Liuqian Wang, Hanyu Xie, Rongzhen Zhao, Qi Ming, Chunjie Ma, Wentao Chao, Yufei Gao, Chengming Liu

**Published:** 2026-10-09

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 20

**Venue importance score included:** 0

**arXiv ID:** 2610.13547v1

**Paper link:** http://arxiv.org/abs/2610.13547v1

**PDF link:** https://arxiv.org/pdf/2610.13547v1

**Abstract:**

Pretrained diffusion Transformers provide powerful generative priors for image restoration, yet adapting them to structure-sensitive tasks remains challenging. Existing methods mainly rely on dense low-resolution features as conditions, which often entangle salient objects with dominant backgrounds and provide limited abstraction for recurring structures across scales and samples. We propose MOSAIC, an object-centric representation learning framework that learns compact structural conditions for generative model adaptation. MOSAIC organizes degraded observations into structural slots that capture complementary object-level and layout-level evidence, integrates them across resolutions, and retrieves recurring priors from a shared prototype memory to complement incomplete image-specific information. The resulting representations are injected into selected layers of a frozen diffusion Transformer through lightweight residual modulation, preserving its pretrained generative prior. We instantiate MOSAIC for remote sensing image super-resolution, where small objects, repetitive structures, and large-scale variation provide a challenging testbed. Experiments on UCMerced, AID, and RSSCN7 show consistent PSNR improvements across $\times 2$ and $\times 4$ settings and favorable LPIPS results at $\times 4$. Qualitative results further demonstrate improved preservation of small objects, structural boundaries, and repetitive spatial patterns.

**Why this may be relevant:**

It is directly related to remote sensing or Earth observation workflows.

---

### 10. How Many Significant LISA?: A multiple testing correction

**Authors:** Giuseppe Arbia, Francesca Cardile, Vincenzo Nardelli, Niccolò Salvini

**Published:** 2026-10-09

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 18

**Venue importance score included:** 0

**arXiv ID:** 2610.13472v1

**Paper link:** http://arxiv.org/abs/2610.13472v1

**PDF link:** https://arxiv.org/pdf/2610.13472v1

**Abstract:**

In spatial data analysis, global measures of spatial correlation provide useful insights into the general spatial patterns, but fail to capture local variations. Local Indicators of Spatial Association (LISA) address this limitation by identifying local clusters and spatial outliers, offering valuable applications in many fields of research such as public health, urban planning and environmental monitoring, to name only a few. However, the application of LISA tools in hypothesis testing is undermined by the presence of the multiple testing problem which dramatically increases the risk of committing Type I errors especially when dealing with very large datasets. Standard corrections procedure (like, e. g., Bonferroni and Benjamini-Hochberg procedures) fail to consider the spatial dependence among the various LISA tests and, furthermore, they are overly conservative. This paper proposes an adjustment that, by incorporating the notion of the "effective sample size", improves statistical inference balancing false discovery rate control and statistical power.

**Why this may be relevant:**

It is related to urban planning, infrastructure, or built-environment analysis.

---

