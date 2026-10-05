# Weekly Geospatial ML Papers

**Search window:** 2026-09-28 to 2026-10-05

**Sources:** arXiv and Semantic Scholar

**Total selected papers:** 10

This digest focuses on geospatial analysis, urban climate, urban planning, infrastructure, and geospatial problem-solving using ML, computer vision, LLMs, VLMs, foundation models, self-supervised learning, and related methods.

Only papers from the selected top journals, conferences, or workshops are included by default. The venue importance score is included in **My Score**.

## Top Papers

### 1. On-Orbit Execution of a Geospatial Foundation Model

**Authors:** Andrew Du, Roberto del Prete, Alejandro D. Mousist, Fabrice Marre, C. Seubert, Gabriele Meoni, Tat-Jun Chin

**Published:** 2026-10-01

**Venue:** Remote Sensing

**Found via:** Semantic Scholar

**My Score:** 58

**Venue importance score included:** 10

**Semantic Scholar citations:** 0

**DOI:** 10.3390/rs18193371

**Paper link:** https://www.semanticscholar.org/paper/621b91eadfb425ec2b4ccb85df3495e95de9d214

**PDF link:** https://doi.org/10.3390/rs18193371

**Abstract:**

Geospatial foundation models (GeoFMs) offer broad generalisation across Earth observation (EO) tasks, particularly under data-limited conditions. However, their large model size and computational requirements remain major barriers to deployment on resource-constrained space hardware. To address this challenge, we develop compact variants of a GeoFM designed to preserve downstream task performance while enabling onboard execution. The models are evaluated across five downstream EO tasks and validated on two representative flight-computing environments. The results show that compression substantially reduces model size (1157.03 MB to 73.30 MB; approximately 16×) and enables execution on resource-constrained hardware (FP32-to-FP16 conversion for the Myriad-2 resulted in differences of no more than 0.21 percentage points across all reported task-level performance metrics), while task-head adaptation improves performance on mission-domain imagery under limited supervision. We further demonstrate on-orbit execution of the compact GeoFM using the IMAGIN-e payload aboard the International Space Station, where inference was performed on a preloaded curated dataset under orbital computing conditions. These findings establish a practical pathway for translating large pretrained GeoFMs into resource-efficient onboard implementations and expand the feasibility of onboard artificial intelligence for future EO missions.

**Why this may be relevant:**

It appears in one of the selected top journals, conferences, or workshops. It may help track foundation-model directions for Earth observation or geospatial AI. It is directly related to remote sensing or Earth observation workflows.

---

### 2. AI-Assisted Planning for Sustainable Urbanism: Mapping Urban Livability in a Contemporary American City through Tree Coverage

**Authors:** Kunth Shah, Edwin Flores

**Published:** 2026-09-29

**Venue:** Journal of Contemporary Urban Affairs

**Found via:** Semantic Scholar

**My Score:** 41

**Venue importance score included:** 0

**Semantic Scholar citations:** 0

**DOI:** 10.25034/ijcua.2026.v10n2-5

**Paper link:** https://www.semanticscholar.org/paper/ba8cef396c062effcff5a2c115a8141595966f65

**PDF link:** https://doi.org/10.25034/ijcua.2026.v10n2-5

**Abstract:**

This study explores the integration of artificial intelligence, spatial analysis, and urban design to evaluate and enhance urban livability while addressing socio-economic and environmental vulnerabilities in contemporary cities. Using Austin, Texas, as a case study, the research combines ArcGIS-based spatial analysis with AI-assisted modeling to examine environmental, socio-economic, and infrastructural datasets, with urban tree canopy coverage serving as a key indicator of neighborhood health and equity. A hexagonal tessellation grid is developed to break down census tract data into standardized spatial units. This allows vulnerability scores to be calculated and correlated with tree coverage. Machine-learning techniques, including regression-based predictive modeling, are applied to identify patterns of vulnerability and forecast future urban conditions using survey-based and real-time data inputs. The findings demonstrate that an integrated GIS–AI workflow effectively reveals socio-spatial disparities in urban livability, paving the way for sustainable urban design, scientific zoning strategies, and informed form-based coding interventions.

**Why this may be relevant:**

It connects to urban tree detection, canopy mapping, or vegetation analysis.

---

### 3. On-Board Anomaly Detection for Efficient Marine Environmental Monitoring

**Authors:** Thomas Goudemant, Clotilde Szywala, Benjamin Francesconi, Michelle Aubrun, Yves Bobichon, Marjorie Bellizzi, Adrien Girard

**Published:** 2026-10-02

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 38

**Venue importance score included:** 0

**DOI:** 10.5281/zenodo.13850918

**arXiv ID:** 2610.03649v1

**Paper link:** http://arxiv.org/abs/2610.03649v1

**PDF link:** https://arxiv.org/pdf/2610.03649v1

**Abstract:**

Marine ecosystems are impacted by various threats such as oil spills, algal blooms, and sediment floods, which disrupt habitats, wildlife, and human activities. Advances in satellite imagery and Artificial Intelligence (AI) have enhanced our capabilities for early detection and mitigation of such hazards. In this paper, we propose a marine event detection pipeline for Earth observation satellites equipped with multi- or hyperspectral sensors. Our approach includes a self-supervised neural network encoder that compresses satellite images into a reduced latent space, enabling efficient onboard processing. A machine learning anomaly detection model identifies deviations from normal sea patterns to detect environmental anomalies. We compare its performance against traditional algorithms such as Isolation Forest, One-Class Support Vector Machine and Local Outlier Factors. Our lightweight, resource-efficient pipeline is optimized for deployment on satellites with limited computational resources, ranging from embedded CPUs to AI hardware accelerators. By prioritizing the transmission of critical information, our solution enhances system responsiveness and optimizes satellite communication bandwidth. Demonstrated through current integration across multiple missions, including European Space Agency's (ESA) Phisat-2 mission and Microsoft/Thales Alenia Space IMAGIN-e mission, our pipeline aims to improve marine environmental monitoring by providing timely alerts and efficient data reduction.

**Why this may be relevant:**

It is directly related to remote sensing or Earth observation workflows.

---

### 4. A Vision-Language Model (VLM)-based Pipeline for End-to-End Procedural Modeling of Field-Grown Maize from Point Clouds

**Authors:** Mozhgan Hadadi, Talukder Z. Jubery, Adarsh Krishnamurthy, Baskar Ganapathysubramanian

**Published:** 2026-10-02

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 32

**Venue importance score included:** 0

**arXiv ID:** 2610.03468v1

**Paper link:** http://arxiv.org/abs/2610.03468v1

**PDF link:** https://arxiv.org/pdf/2610.03468v1

**Abstract:**

Editable 3D models of field-grown crops support high-throughput phenotyping and in silico breeding trials, but building them from scanned point clouds requires organ-level segmentation and fitting. Procedural generators can turn an organ-level parameter set into an analysis-suitable 3D model, but obtaining that set requires hours of manual tuning per plant or segmentation models trained on species-specific labels. We present an automated pipeline that reconstructs procedural maize models from raw 3D point clouds without manual tuning or species-specific training data. A multimodal vision-language model (VLM) annotates leaf midlines in rendered orthographic views. Deterministic geometric algorithms back-project the annotations onto the point cloud, merge them into 3D leaves by cross-view consensus, and grow the midlines to full blades on an orientation-weighted surface graph. Measured organ parameters populate a plant descriptor for a Non-Uniform Rational B-Spline (NURBS)-based procedural model generator. Each leaf surface is then refined against its scan points by differentiable NURBS fitting. The pipeline reached a median whole-plant Chamfer distance of 5.4 mm on 100 genotypically diverse field-grown maize plants from the MaizeField3D dataset. The reconstructions were closer to the scans than those of an earlier semi-automated pipeline based on manual annotations. The pipeline recovered 1,017 of 1,023 (99.4%) curated reference leaves at an intersection-over-union of at least 0.5 without using those labels as input. These results show that VLM annotations become usable organ-level measurements when downstream geometric stages can correct them. This makes automated generation of editable 3D plant assets feasible at the scale of modern phenotyping experiments.

**Why this may be relevant:**

It may be useful for multimodal geospatial understanding using image-text models. It may be useful for LiDAR-based tree inventory, urban structure mapping, or 3D geospatial analysis.

---

### 5. CLIMB: Confidence-Guided Complementary Evidence for Multimodal Retrieval-Augmented Generation

**Authors:** Hang Gao, Wujiang Xu, Zhixing Zhang, Kai Mei, Jingyi Yang, Dimitris N. Metaxas

**Published:** 2026-10-02

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 29

**Venue importance score included:** 0

**arXiv ID:** 2610.03421v1

**Paper link:** http://arxiv.org/abs/2610.03421v1

**PDF link:** https://arxiv.org/pdf/2610.03421v1

**Abstract:**

Multimodal large language models (MLLMs) have shown strong visual reasoning abilities, but knowledge-intensive visual question answering often requires external textual evidence beyond the image and the model's parametric knowledge. Existing multimodal RAG systems commonly rely on Top-$K$ retrieval or reranking, which may return redundant passages and provide limited control over whether an answer update is sufficiently supported by the retrieved evidence. We propose \textit{CLIMB}, a training-free inference-time framework for multimodal RAG. CLIMB first constructs a compact complementary evidence pool using an MMR-style objective that balances query relevance and passage-level redundancy. It then performs confidence-controlled refinement within this fixed pool: an R/E/C critic scores passages by relevance, evidence specificity, and cross-modal alignment, while an evidence-grounded confidence estimator accepts an updated answer only when the estimated confidence increases. This design provides a simple stopping criterion and reduces unnecessary refinement without modifying the underlying retriever or MLLM. Experiments on Encyclopedic-VQA and InfoSeek show that CLIMB consistently improves over retrieval-augmented multimodal baselines. Ablations further indicate that complementary pooling, critic-based scoring, and iterative confidence-controlled refinement each contribute to the final performance.

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis.

---

### 6. Decoding the Functional Roles of Register and High-Norm Patch Tokens in Vision Transformers

**Authors:** Neel Varma, Andrew Rufail, Dipika Khullar, Vasu Sharma

**Published:** 2026-10-02

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 28

**Venue importance score included:** 0

**arXiv ID:** 2610.03698v1

**Paper link:** http://arxiv.org/abs/2610.03698v1

**PDF link:** https://arxiv.org/pdf/2610.03698v1

**Abstract:**

Self-supervised Vision Transformers (ViTs), such as DINOv2, learn rich visual representations, but the functions of their internal tokens remain poorly understood. Recent architectures introduce dedicated register tokens to reduce high-norm out- lier patch tokens that emerge in background re- gions, yet the semantic and functional roles of both token types have not been fully established. In this paper, we analyze these roles by training sparse autoencoders (SAEs) on register-token and outlier-token activations in DINOv2. Using an automated interpretability pipeline, UMAP clus- tering, and CLIP-space cross-checks, we find that register-token features are more strongly associ- ated with high-level semantic concepts. Outlier- token features, by contrast, are more often associ- ated with lower-level structural, background, and texture-dominant patterns. Causal ablations fur- ther reveal a substantial functional asymmetry: disrupting top-activating register-derived features produces a 48.17% drop in representation cosine similarity, whereas disrupting outlier-derived fea- tures produces only a 0.31% drop. Together, our results provide evidence for token specialization in self-supervised ViTs.

**Why this may be relevant:**

It matched the geospatial machine learning search criteria and may be worth screening.

---

### 7. ForestQuery: Boundary-Aware and Spatially Anchored Query Learning for Unified Forest Point Cloud Segmentation

**Authors:** Zhihao Zhan, Le Tao, Yifei Tian, Xin Liu, Jie Yuan

**Published:** 2026-10-02

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 28

**Venue importance score included:** 0

**arXiv ID:** 2610.03403v1

**Paper link:** http://arxiv.org/abs/2610.03403v1

**PDF link:** https://arxiv.org/pdf/2610.03403v1

**Abstract:**

Forest point cloud segmentation is fundamental for fine-grained 3D forest scene understanding, yet remains challenging due to irregular tree structures, severe occlusions, density variations, and ambiguous instance boundaries. Recent query-based forest segmentation methods have shown promise for unified semantic and instance prediction, but they still insufficiently exploit forest-specific spatial structure and account for boundary uncertainty. In this paper, we propose ForestQuery, a boundary-aware and spatially anchored query learning framework for unified forest point cloud segmentation. ForestQuery enhances instance and semantic query learning through two complementary designs. Specifically, boundary uncertainty is explicitly modeled to guide reliable instance query construction and modulate query optimization through adaptive loss reweighting. Meanwhile, spatially anchored semantic query enhancement (SA-SQE) introduces learnable 3D anchors encoding forest vertical stratification priors to enrich semantic queries with explicit spatial references. We evaluate ForestQuery on multiple public forest point cloud benchmarks and a self-collected annotated real-world dataset. Extensive experiments demonstrate consistent improvements in both individual-tree segmentation and semantic segmentation across diverse forest scenes. Code and data are publicly available at https://zhan994.github.io/ForestQuery

**Why this may be relevant:**

It may be useful for LiDAR-based tree inventory, urban structure mapping, or 3D geospatial analysis. It connects to urban tree detection, canopy mapping, or vegetation analysis.

---

### 8. Objects Without Morphisms: What LLMs for Mathematics Do Not Represent

**Authors:** Yanli Wang, Suijin Wang, Xiaopeng Yuan, Haohan Wang

**Published:** 2026-10-02

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 26

**Venue importance score included:** 0

**arXiv ID:** 2610.03551v1

**Paper link:** http://arxiv.org/abs/2610.03551v1

**PDF link:** https://arxiv.org/pdf/2610.03551v1

**Abstract:**

Large language models (LLMs) have reached expert-level performance on competition mathematics largely through the volume of search placed around them: candidate solutions are sampled in quantity and retained only when an external criterion accepts them. Such a procedure improves the outcome that survives it while leaving untouched what the model represents. We examine that question where no external criterion exists: translating statements between the dialects of neighbouring subfields, where fidelity turns on the level of generality at which content is asserted. The source leaves that level implicit in its vocabulary, so a faithful translation must recover it from the relation between the theories. We introduce an instrument that codes truth, content and scope in separate blind queues, with a judge-free measure of whether a rewrite states the hypothesis implicit in its source, and establish its sensitivity with a planted-positive control. Across seven models from four families, translating towards the general framing widens the domain of quantification in 60.6% of rewrites and narrows it in none; translating towards the concrete framing narrows it in 28.3% and widens it in 0.3%. The hypothesis that would prevent it is stated in 21.6% of model rewrites and 4.2% of human statements. Capability does not govern the asymmetry: it appears in every model tested, and the most capable widens least. It replicates on the half of the benchmark held out by a pre-registered rule, and on statements written by mathematicians. Instructing a model to state every hypothesis it requires raises that rate but not its sensitivity to direction. We argue that these systems have acquired an object-level correspondence between subfield vocabularies without the constraint under which a translation between theories carries hypotheses to hypotheses.

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis.

---

### 9. From Wildfire Severity to Snow Persistence: A Multisource GeoAI Study of the 2020 Creek Fire

**Authors:** Parastoo Farajpoor, Mohammadreza Narimani

**Published:** 2026-09-28

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 15

**Venue importance score included:** 0

**arXiv ID:** 2609.36345v1

**Paper link:** http://arxiv.org/abs/2609.36345v1

**PDF link:** https://arxiv.org/pdf/2609.36345v1

**Abstract:**

Accurate prediction of post-fire snow conditions does not necessarily establish how wildfire changed those conditions. We developed an explainable geospatial artificial intelligence framework combining multisource Earth observations, meteorological information, and matched before-after comparisons to examine seasonal snow persistence following the 2020 Creek Fire in California's Sierra Nevada. Harmonized Landsat Sentinel-2 observations were used to estimate the fraction of clear-sky observations containing snow during October-July for eleven water years, 2016-2026, on a 500 m analysis grid. We matched 3,778 snow-zone cells inside the fire perimeter to comparable unburned controls using terrain and pre-fire snow conditions; absolute standardized mean differences after matching were no greater than 0.047. HLS persistence agreed closely with MODIS, with a mean annual spatial correlation of 0.947. The landscape-average before-after control-impact contrast was +0.0017, with a year-level 95% confidence interval of -0.023 to +0.027. A stronger response emerged in the highest burn-severity class, where observed persistence increased by 0.026 relative to matched controls, equivalent to 2.6 percentage points. Under 5 km spatial cross-validation, XGBoost predicted raw post-fire persistence with an out-of-fold coefficient of determination of 0.811, whereas predictive skill for the fire-adjusted anomaly reached 0.046. Elevation and temperature together accounted for 65.7% of mean absolute model attribution. These findings distinguish a severity-associated optical snow response from the terrain-climate relationships that dominate predictive skill. Combining matched comparisons with explainable GeoAI provides a practical framework for forest monitoring that separates accurate environmental mapping from inference about disturbance effects.

**Why this may be relevant:**

It is directly related to remote sensing or Earth observation workflows.

---

### 10. A Residual Tree Gaussian Process Modeling Framework for High-Dimensional Data

**Authors:** Pulong Ma, Li Ma

**Published:** 2026-10-02

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 14

**Venue importance score included:** 0

**arXiv ID:** 2610.02893v1

**Paper link:** http://arxiv.org/abs/2610.02893v1

**PDF link:** https://arxiv.org/pdf/2610.02893v1

**Abstract:**

With the advance of measurement technologies and increasing computing power, large spatial data with heterogeneous structures are often collected over high-dimensional domains. Existing Gaussian process (GP) models and computational strategies are often inadequate for analyzing such datasets in multi-dimensional domains. To address these challenges, we develop a Bayesian residual tree GP methodology called ResTGP for large spatial data with potentially heterogeneous structures in multi-dimensional domains. The key idea is to decompose a Gaussian process at a cascade of resolutions along a dyadic tree through iteratively computing predictive and residual processes so that the residual process on each tree node, both interior and leaf, becomes sufficient for the finer-level dependency within that node. This allows characterization of the underlying covariance structure in a flexible, multi-scale manner while achieving divide-and-conquer on the data domain, which leads to computational efficiency. To allow efficient tree inference, we introduce a computational strategy for Bayesian inference based on recursive message passing, which scales linearly with the sample size given the tree. This paper also proves posterior consistency of the model for estimating continuous functions in a nonparametric regression framework. Extensive numerical examples and the storm surge application confirm the advantages of the proposed method.

**Why this may be relevant:**

It connects to urban tree detection, canopy mapping, or vegetation analysis.

---

