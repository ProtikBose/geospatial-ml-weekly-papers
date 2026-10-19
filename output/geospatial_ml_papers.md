# Weekly Geospatial ML Papers

**Search window:** 2026-10-12 to 2026-10-19

**Sources:** arXiv and Semantic Scholar

**Total selected papers:** 10

This digest focuses on geospatial analysis, urban climate, urban planning, infrastructure, and geospatial problem-solving using ML, computer vision, LLMs, VLMs, foundation models, self-supervised learning, and related methods.

Only papers from the selected top journals, conferences, or workshops are included by default. The venue importance score is included in **My Score**.

## Top Papers

### 1. GeoReason: Bridging Logical Reasoning and Spatial Fidelity in Remote Sensing Segmentation

**Authors:** Cheng Fan, Han Wu, Tingzhang Luo, Minjing Dong, Yehui Tang, Jianyuan Guo

**Published:** 2026-10-16

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 52

**Venue importance score included:** 0

**arXiv ID:** 2610.23416v1

**Paper link:** http://arxiv.org/abs/2610.23416v1

**PDF link:** https://arxiv.org/pdf/2610.23416v1

**Abstract:**

Multimodal Large Language Models (MLLMs) have significantly advanced instruction-driven perception through the "Embedding-as-Mask" paradigm. However, extending this capability to Remote Sensing (RS) reasoning segmentation remains exceptionally challenging under cluttered geographical contexts and extreme scale variations, often leading to Spatial Fidelity Degradation and Target Misidentification. We identify a critical yet underexplored bottleneck: the sequential alienation of the segmentation token [SEG] from its initial visual grounding within the autoregressive generation paradigm. Produced only at the end of long reasoning chains, [SEG] relies on visual evidence that has been progressively diluted by linguistic abstraction and autoregressive noise. This information decay is particularly catastrophic for RS targets with minuscule pixel footprints, where even marginal fidelity loss leads to localization failure. To address these bottlenecks, we propose GeoReason, a novel framework designed to fortify logical deduction and preserve spatial integrity. First, we introduce an Anticipatory Prior mechanism that injects the [SEG] token directly into the initial user query, shifting it from a terminal output to a primary condition. This paradigm shift transforms the token into a persistent spatial anchor, preventing information decay during long-form linguistic inference. Second, we enhance visual reasoning via a Location-aware Chain-of-Thought (CoT) that enforces coarse-to-fine localization using bounding boxes, coupled with a Latent Patch-to-Token Alignment (PTA) Loss that explicitly aligns the latent segmentation token with physical RS textures. Extensive experiments demonstrate that GeoReason consistently outperforms state-of-the-art methods on the Earthreason and RRSIS-D benchmarks. Code is available at https://github.com/Fanc0126/GeoReason.

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis. It is directly related to remote sensing or Earth observation workflows.

---

### 2. Aero‐VLM: Vision‐Language Guided Oriented Aircraft Detection for Remote Sensing Imagery

**Authors:** Faryal Aurooj Nasir, Khurram Khurshid, Syeda Khan, Madiha Tahir, Waqas ur Rahman, Syed Ali Irtaza

**Published:** 2026-10-13

**Venue:** Expert systems

**Found via:** Semantic Scholar

**My Score:** 51

**Venue importance score included:** 0

**Semantic Scholar citations:** 0

**DOI:** 10.1111/exsy.70450

**Paper link:** https://www.semanticscholar.org/paper/2b2a81ca407175d0adbb824dc70b9e87acf3b66b

**PDF link:** https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/exsy.70450

**Abstract:**

Fine‐grained aircraft detection in remote sensing (RS) imagery is challenged by limited labelled data, domain shifts, high intra‐class similarity and complex environmental conditions. Conventional detectors rely heavily on dense supervision, whereas vision–language models (VLMs) often lack the geometric precision required for accurate localization in aerial scenes. To address these challenges, we propose Aero‐VLM, a hybrid CNN–Transformer framework that combines self‐supervised visual representation learning with pretrained vision–language semantic embeddings for data‐efficient fine‐grained aircraft detection. An oriented detection head with knowledge distillation is integrated with the vision–language representation to improve geometric localization and support efficient inference. We further introduce Aero‐RSI, a 10,000‐image high‐resolution benchmark comprising ten visually similar aircraft categories for fine‐grained detection. Aero‐VLM achieves 64.6% mAP@50 in zero‐shot evaluation on unseen classes, outperforming CLIP, BLIP‐2, Grounding DINO and VisionLLM by up to 44.1 percentage points. With only 10 labelled samples per class, Aero‐VLM improves mAP@50 by 16.1 percentage points, whereas competing models achieve gains of less than 10 percentage points. Cross‐domain evaluation on DOTA, MTARSI and FAIR1M demonstrates strong generalization without additional fine‐tuning, with Aero‐VLM achieving gains of up to 11.0 percentage points over CNN‐based detectors and up to 46.0 percentage points over adapted VLMs. Under full supervision, Aero‐VLM achieves 90.2% mAP@50, exceeding YOLOv11s by 2.5 percentage points and Grounding DINO by 39.7 percentage points. Despite a 33% increase in inference latency relative to YOLOv11s, Aero‐VLM requires approximately 45% less inference time than Grounding DINO, demonstrating a favourable accuracy–efficiency trade‐off.

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis. It may be useful for multimodal geospatial understanding using image-text models. It is directly related to remote sensing or Earth observation workflows. It may help with cross-city, cross-region, or cross-sensor generalization.

---

### 3. FloodVLM-Pix: Language-Guided Pixel-Level Flood Understanding

**Authors:** Chengyang Zhang, Zhihao Wang, Zhiyu Long, Xueqian Wang, Quanming Yao, Wei Wu, Gang Li

**Published:** 2026-10-16

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 40

**Venue importance score included:** 0

**arXiv ID:** 2610.23377v1

**Paper link:** http://arxiv.org/abs/2610.23377v1

**PDF link:** https://arxiv.org/pdf/2610.23377v1

**Abstract:**

As climate change intensifies, floods are becoming more frequent and destructive, making accurate flood understanding an urgent priority. However, existing vision-language models perform poorly on flood-related tasks, suffering from attentional bias and inaccurate descriptions of flood magnitude. To bridge this gap, we construct the first large-scale remote sensing flood multi-modal benchmark that supports language-level flood understanding and pixel-level flood segmentation. The benchmark contains 131,200 flood image patches and corresponding 443,100 textual descriptions for flood severity and evolution. Based on this benchmark, we propose FloodVLM-Pix, a language-guided pixel-level flood understanding model that includes a flood prior module and a multi-temporal flood pixel decoder to achieve accurate flood understanding. The flood prior module automatically distills sub-region flood spatial priors and inputs priors into FloodVLM-Pix, solving the attentional bias problem in flood language understanding. The flood pixel decoder introduces a novel general-specific feature fusion mechanism to address performance degradation caused by interference (e.g., clouds or mountain shadows) during flood segmentation. Experiments on FloodVL-Pix demonstrate that FloodVLM-Pix improves both flood description quality and pixel-level flood segmentation performance compared with state-of-the-art VLMs and flood segmentation models. Our code and data will be released at https://github.com/Haomiaoyanmeng/FloodPix.

**Why this may be relevant:**

It may be useful for multimodal geospatial understanding using image-text models. It is directly related to remote sensing or Earth observation workflows.

---

### 4. ShadowCast: On-the-Fly Context-Aware Shadow Augmentation for Remote Sensing Image Segmentation

**Authors:** Yechan Kim, Dongho Yoon, Jongmin Joo, JongHyun Park, Moongu Jeon

**Published:** 2026-10-16

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 29

**Venue importance score included:** 0

**arXiv ID:** 2610.23440v1

**Paper link:** http://arxiv.org/abs/2610.23440v1

**PDF link:** https://arxiv.org/pdf/2610.23440v1

**Abstract:**

Shadows cast by elevated objects alter the spectral appearance and obscure the boundaries of objects in remote sensing images, thereby degrading semantic segmentation performance. Most existing approaches handle shadows as degradations to be detected and removed, requiring additional costs from dedicated networks and shadow-specific annotations. We propose ShadowCast, which takes the opposite approach: it synthesizes shadows and injects them during training for remote sensing segmentation. It extracts masks of elevated objects, such as buildings and trees, directly from the segmentation labels and estimates an image-specific cast-shadow direction cue by probing the brightness around them. It then projects synthetic shadows along the inferred cast-shadow direction, requiring no learned network and no acquisition metadata. Experiments on three widely used remote sensing benchmarks, Vaihingen, Potsdam, and LoveDA, show that ShadowCast consistently outperforms the baseline across diverse state-of-the-art segmentation architectures. Moreover, it brings additional performance gains when combined with standard augmentation and regularization techniques, indicating that stochastic shadow injection serves as a simple and complementary augmentation strategy for remote sensing segmentation.

**Why this may be relevant:**

It is directly related to remote sensing or Earth observation workflows. It connects to urban tree detection, canopy mapping, or vegetation analysis.

---

### 5. Neural Expansion: A Unified Mechanism for How Deep Neural Networks Generalize

**Authors:** Chashi Mahiul Islam, Samuel Jacob Chacko, Mao Nishino, Canlin Zhang, Xiuwen Liu

**Published:** 2026-10-16

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 20

**Venue importance score included:** 0

**arXiv ID:** 2610.23716v1

**Paper link:** http://arxiv.org/abs/2610.23716v1

**PDF link:** https://arxiv.org/pdf/2610.23716v1

**Abstract:**

Deep neural networks demonstrate remarkable generalization despite being highly over-parameterized, challenging traditional statistical learning theories. While several theoretical paradigms such as margin-based bounds, PAC-Bayesian analyses, and neural tangent kernels provide global explanations, they often lack mechanistic insight into how generalization emerges from training dynamics. We introduce Neural Expansion, a unified geometric framework that characterizes generalization through the expansion of directionally-selective ray coverage in the input space. Using Generalization Intervals (GIs), we quantify direction-specific regions around training samples where the model's predictions remain stable. Our extensive empirical studies across diverse architectures and datasets reveal that training leads to progressive expansion of ray coverage, particularly along directions with low Jacobian singular values. This mechanism helps explain a large fraction of correctly classified test inputs, adversarial examples, and even mislabeled or out-of-distribution samples through the geometry of ray coverage rather than instance-level memorization. By connecting input-space curvature to predictive behavior, our framework provides a mechanistic foundation that complements existing global theories of deep learning.

**Why this may be relevant:**

It may help with cross-city, cross-region, or cross-sensor generalization.

---

### 6. Fluid-Spatiotemporal Stochastic Geometry for Information Flow in Non-Stationary Fields: Kinematics and Field Reconstruction

**Authors:** Wen-Yu Dong, Weiwei Jiang, Song Zhao, Qi Bi, Sheng Chen

**Published:** 2026-10-16

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 19

**Venue importance score included:** 0

**arXiv ID:** 2610.23277v1

**Paper link:** http://arxiv.org/abs/2610.23277v1

**PDF link:** https://arxiv.org/pdf/2610.23277v1

**Abstract:**

Classical stochastic geometry primarily addresses forward analysis by prescribing spatial point-process laws and mobility models. It does not directly address the inverse problem of recovering directional macroscopic transport from aggregate density evolution in non-stationary spatial networks. This paper develops the kinematic foundation of fluid-spatiotemporal stochastic geometry (F-STSG), representing an evolving mobile population by an intensity field under an assumed continuum limit while retaining the network infrastructure as a discrete spatial measure. We formulate macroscopic transport reconstruction as an inverse boundary value problem. Under a strictly positive bounded intensity and compatible source and boundary data, an instantaneous weighted minimum-energy criterion selects a unique velocity representative from the admissible class. The reconstruction reduces to a weighted elliptic Neumann problem and separates density-identifiable transport from weighted-solenoidal circulation that is not identifiable from density evolution alone. We further derive the information flux, interface transport, velocity-divergence relation, and centroid dynamics. Numerical experiments examine reconstruction consistency and sensitivity, while the public New Era of Urban Traffic Monitoring with Aerial Footage (pNEUMA) dataset provides held-out validation of internal transport. A separate unmanned aerial vehicle (UAV) study evaluates the centroid as a causal downstream control reference under observation delay, motion constraints, and execution perturbations.

**Why this may be relevant:**

It is related to urban planning, infrastructure, or built-environment analysis.

---

### 7. Beyond the Benchmark: Conditioning, Domains and Failure Modes of Qwen3-TTS

**Authors:** Séverin Baroudi, Yanis Labrak, Petr Motlicek, Hervé Bredin, Ricard Marxer

**Published:** 2026-10-16

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 17

**Venue importance score included:** 0

**arXiv ID:** 2610.23678v1

**Paper link:** http://arxiv.org/abs/2610.23678v1

**PDF link:** https://arxiv.org/pdf/2610.23678v1

**Abstract:**

Qwen3-TTS reports state-of-the-art zero-shot voice cloning, but its technical report leaves open how the model should be conditioned, how it behaves outside read speech, and how it fails. We characterise its two cloning interfaces, in-context learning (ICL) and X-Vector, against Chatterbox, XTTS-v2 and F5-TTS on read, meeting, emotional and air-traffic-control (ATC) speech, using eighteen objective measures, an LLM judge, a spoofing countermeasure and a listening test. Neither interface dominates: ICL clones timbre more closely from correctly transcribed references, X-Vector clones timing, and ICL degrades sharply when a short reference transcript is wrong. Domain explains four times more variance than system choice. Qwen3-TTS leads on intelligibility and pitch register but trails on prosody, and the objective measures rank systems differently from listeners. An off-the-shelf countermeasure flags its clones no more often than genuine recordings, and on ATC radio it fails for every system. Code and audio are released.

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis.

---

### 8. The Italian lawmaking process: a unified and structured dataset

**Authors:** Matilde Contestabile, Chiara Ferrara, Giovanni Parrillo, Lorenzo Emer, Andrea Vandin

**Published:** 2026-10-16

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 17

**Venue importance score included:** 0

**arXiv ID:** 2610.23741v1

**Paper link:** http://arxiv.org/abs/2610.23741v1

**PDF link:** https://arxiv.org/pdf/2610.23741v1

**Abstract:**

The Italian legislative process is documented in detailed parliamentary records hosted in institutional websites. However, much of this information is available only as unstructured text, limiting its systematic reuse. We applied a controlled, systematic LLM-based extraction procedure, validated against manually annotated records, to convert these texts into ordered and dated events including, e.g., bill introduction, committee examination, plenary examination, and approval. The resulting dataset reconstructs the procedural histories of all 5346 Italian laws enacted between 1985 and 2026, spanning parliamentary terms IX to XIX, for overall 101413 events. Each event records the activity, date, and chamber, with additional procedural details where available. The dataset supports research in the emerging fields of computational legal and legislative studies, potentially combined with process-oriented data science methods to examine procedural paths and legislative timing across parliamentary terms.

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis.

---

### 9. ScoutRoute: Efficient Mixture-of-Experts Routing Using Internal Language Model Signals

**Authors:** Rajdeep Pandhare, Delzaan Bharucha

**Published:** 2026-10-16

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 17

**Venue importance score included:** 0

**arXiv ID:** 2610.23443v1

**Paper link:** http://arxiv.org/abs/2610.23443v1

**PDF link:** https://arxiv.org/pdf/2610.23443v1

**Abstract:**

Efficient expert routing is a fundamental challenge in Mixture-of-Experts (MoE) systems, particularly for heterogeneous collections of independently trained Large Language Mod els (LLMs). Existing routing approaches typically rely on jointly trained gating networks, prompt-based predictors, or computationally expensive multi-model inference, limiting their flexibility and efficiency. This paper presents ScoutRoute, a lightweight post-hoc routing framework that predicts expert competence using internal language model signals extracted from a single forward pass through an inexpensive scout model. Hidden-state representations are used to estimate cross-model competence through lightweight logistic probes, while logit-derived confidence measures are incorporated within a domain-aware routing strategy for efficient expert selec tion without modifying the underlying language models. ScoutRoute isevaluatedon fiveopen-weightlanguagemodels across fourbenchmark datasets covering mathematical reasoning, code generation, commonsense reasoning, and multidis ciplinary knowledge. Experimental results show that ScoutRoute consistently outperforms individual routing signals while requiring only a single scout-model inference. The proposed competence probes also achieve superior calibration compared with conventional confidence measures, demonstrating that internal language model representations provide transferable information for accurate and efficient expert routing across heterogeneous language models

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis.

---

### 10. FlexUMM: Flexible Representation Learning for Unified Multimodal Models

**Authors:** Yinyi Luo, Haoyue Bai, Yi Ge, Nilton Cesar Rojas Vales, Marios Savvides, Jindong Wang

**Published:** 2026-10-15

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 17

**Venue importance score included:** 0

**arXiv ID:** 2610.22682v1

**Paper link:** http://arxiv.org/abs/2610.22682v1

**PDF link:** https://arxiv.org/pdf/2610.22682v1

**Abstract:**

Unified multimodal models (UMMs) can integrate understanding and generation within a single backbone. However, it is commonly known that these two capabilities can cause conflicting representations, leading to a central question: how representation and computation should be shared across functionalities? Existing UMMs often rely on a largely fixed structure, where different inputs and functionalities follow the same depth and parameter-sharing pattern. We argue that this assumption is too restrictive: more effective unification requires sharing the computation that supports cross-functional communication while specializing the capacity that becomes task- or input-specific. We introduce FlexUMM, a flexible UMM framework that dynamically decides when to preserve shared computation, when to route specialized capacity, and when to stop further processing. Evidence shows that this flexible allocation improves UMMs along two complementary axes. It improves accuracy by reducing harmful competition between functionalities, and it improves efficiency by avoiding unnecessary computation once an input representation is sufficiently mature. Beyond simple architectural unification from the pre-trained models, FlexUMM works as a model-agnostic, functional plug-in to make existing UMMs more unified, stronger, and efficient. Code is available at: https://github.com/AIFrontierLab/TorchUMM/tree/main/src/umm/post_training/flexumm.

**Why this may be relevant:**

It connects to urban tree detection, canopy mapping, or vegetation analysis.

---

