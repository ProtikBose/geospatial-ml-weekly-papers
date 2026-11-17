# Weekly Geospatial ML Papers

**Search window:** 2026-11-09 to 2026-11-16

**Sources:** arXiv and Semantic Scholar

**Total selected papers:** 10

This digest focuses on geospatial analysis, urban climate, urban planning, infrastructure, and geospatial problem-solving using ML, computer vision, LLMs, VLMs, foundation models, self-supervised learning, and related methods.

Only papers from the selected top journals, conferences, or workshops are included by default. The venue importance score is included in **My Score**.

## Top Papers

### 1. DySENSE: Dynamic Spatiotemporal ENergy Synthesis and Emulation with Satellite Imagery

**Authors:** Kailai Sun, Zijie Gao, Mingyi He, Can Rong, Alok Prakash, Baoshen Guo, Shenhao Wang, Jinhua Zhao

**Published:** 2026-11-13

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 46

**Venue importance score included:** 0

**arXiv ID:** 2611.17878v1

**Paper link:** http://arxiv.org/abs/2611.17878v1

**PDF link:** https://arxiv.org/pdf/2611.17878v1

**Abstract:**

Cities account for over two-thirds of the world's energy and more than 70% of global carbon dioxide emissions. City energy is essential for achieving the 2050 net-zero target and the UN's Sustainable Development Goals 7 and 11. Although existing studies have made progress, they are limited by data and methodological gaps. Existing studies are largely predictive for existing cities rather than generative for future cities; fine-grained, aligned monthly dynamic energy data are scarce; and existing GenAI models struggle to generate dynamic urban functional monthly energy. We present DySENSE, a joint multimodal GenAI framework that synthesizes static urban satellite imagery together with spatially aligned, dynamic monthly building energy consumption maps. We decouple long-term static urban morphology from short-term dynamic energy consumption. By conditioning on static urban land use, DySENSE can generate realistic, diverse and new static urban imagery with aligned energy maps. By conditioning on dynamic monthly and climate prompts, DySENSE can jointly generate dynamic, monthly energy consumption maps while keeping the urban morphology static. Experiments across four cities (New York, Washington, Norfolk, Busan) demonstrated that DySENSE can generate annotated high-fidelity synthetic energy data using less than 25% labelled data, boosting downstream prediction performance by 8% mIoU, and achieving strong energy dynamic consistency. Compared to existing methods, DySENSE significantly improved prediction performance (8.7% accuracy) and reduced prediction error (9%-18% CVRMSE, ASHRAE). DySENSE offers an effective foundation for energy-efficient cities, peak-load analysis, building performance simulation and dynamic demand response for city, energy, and building science. The data and code: https://huggingface.co/datasets/skl24/MUSE2 and https://github.com/kailaisun/DySENSE

**Why this may be relevant:**

It is directly related to remote sensing or Earth observation workflows.

---

### 2. Multi-level latent-diffusion adaptation for cross-region point cloud segmentation of ancient terraces

**Authors:** Sina Mohammadi, Roderik Lindenbergh, Javier Ruiz-Pérez, Marco Madella, Sebastian Fajardo

**Published:** 2026-11-13

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 43

**Venue importance score included:** 0

**arXiv ID:** 2611.18033v1

**Paper link:** http://arxiv.org/abs/2611.18033v1

**PDF link:** https://arxiv.org/pdf/2611.18033v1

**Abstract:**

Automated lidar feature detection from lidar point clouds can support archaeological surveys, but models trained in one landscape may transfer poorly to another because of differences in terrain, vegetation, acquisition characteristics, and feature morphology. We address this problem for cross-region detection of ancient terraces using transductive unsupervised domain adaptation that exploits an unlabelled target survey. We propose MELD (Multi-level Embedding-space Latent Diffusion), which trains separate diffusion denoisers on target-domain representations at four hierarchical PointNet++ feature levels. These target distribution priors are then used to refine source representations during supervised training and target representations during inference, allowing adaptation to act directly on the multi-scale features consumed by the segmentation decoder. We additionally investigate local geometric descriptors derived from K-nearest-neighbour neighbourhoods, including surface normals, slope, and aspect. MELD is evaluated bidirectionally between the Teyuna and Miraflores lidar surveys in the Sierra Nevada de Santa Marta, Colombia, against a source-only model and nine configurations of established domain adaptation approaches. MELD raises F1 over the source-only model from 0.397 to 0.459 for Teyuna-to-Miraflores transfer and from 0.557 to 0.594 in the reverse direction, achieving the highest F1 among the evaluated adaptation methods in both directions. Adding local geometry further raises F1 to 0.542 and 0.606, respectively. Multi-level ablation shows that refining all four PointNet++ levels provides the strongest performance in both directions. These results show that explicit modelling of target feature distributions in hierarchical point cloud feature space, complemented by local geometry, provides an effective route to cross-region archaeological mapping without target labels.

**Why this may be relevant:**

It may be useful for LiDAR-based tree inventory, urban structure mapping, or 3D geospatial analysis. It connects to urban tree detection, canopy mapping, or vegetation analysis. It may help with cross-city, cross-region, or cross-sensor generalization.

---

### 3. Measuring Public Participation in Local Government: An Audio-Based Instrument for Classifying Speakers in City Council Meetings

**Authors:** Menglin Liu, J. Sophia Wang, Ge Shi

**Published:** 2026-11-13

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 40

**Venue importance score included:** 0

**arXiv ID:** 2611.18072v1

**Paper link:** http://arxiv.org/abs/2611.18072v1

**PDF link:** https://arxiv.org/pdf/2611.18072v1

**Abstract:**

How much does the public actually speak in local government? Despite sustained interest in democratic participation, we lack large-scale measures of public voice at the local level, because the underlying record -- audio of open meetings -- has been prohibitively costly to convert into data. We contribute a measurement instrument: an audio-analysis pipeline that classifies each speaker in a city council meeting as an elected official or a member of the public directly from audio, and aggregates these labels into validated measures of participation such as floor-time share. The pipeline first segments each recording by speaker, then classifies each speaker with a multimodal large language model (MLLM), using the meeting's own temporal structure (neighboring speakers, iterative refinement, and a majority vote across three classifiers) as supporting components. We collect 1,618 recordings from seven U.S. cities (2017-2023); after diarization and quality control, the analytic corpus is 1,565 meetings from five cities. The task is non-trivial: audio quality is uneven, members of the public speak informally and are often introduced only briefly, and speech frequently overlaps. Even so, segmentation reaches 89% accuracy (mean pairwise kappa=0.84), and the classifier reaches 87.7% accuracy (kappa=0.736, public-participant F1=0.832) on ground truth from five cities (N=1,761 speakers) -- agreement comparable to that among the human annotators themselves. At scale, members of the public receive a median of just 10% of floor time, the top speaker is an official in over 94% of meetings, and public participation declined over COVID-19 without recovering by 2023. The instrument measures participation directly from audio, without transcription or linkage to external voter or property records, establishing audio-as-data as a practical approach for the study of local politics.

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis.

---

### 4. Lens: Training-Free Semantic Search for Cross-Tile Object and Scene Retrieval in Satellite Imagery

**Authors:** Ata Akbari Asanjan, Anit Upadhyaya, Jeremy Kravitz, Subash Yeggina

**Published:** 2026-11-13

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 35

**Venue importance score included:** 0

**arXiv ID:** 2611.18251v1

**Paper link:** http://arxiv.org/abs/2611.18251v1

**PDF link:** https://arxiv.org/pdf/2611.18251v1

**Abstract:**

We developed Lens, a training-free system for semantic object and scene search across large satellite mosaics that requires no detector trained for the class of interest. Lens represents each tile with a frozen, self-supervised vision transformer (DINOv3), removes the positional bias in its dense features by projecting them onto the subspace orthogonal to a positional basis estimated once from a constant image, and centers the debiased features on the mean feature computed across the whole area before comparison. Lens forms a query by averaging the centered features of a small neighborhood of patches around a chosen point, or of an entire tile for scene-level search, and matches it against the index by cosine similarity. It stores the centered patch features in a byte-quantized similarity index that supports real-time range search over a mosaic of thousands of patches, and a coarser whole-tile embedding index for scene-level retrieval. A guided upsampling network (AnyUp) runs once per tile to recover pixel-accurate boundaries beyond the native feature grid, and the result is cached so later queries reuse it. We evaluated Lens on the 5,128-tile DFC2020 test set and ran it as an interactive tool on five Sentinel-2 areas spanning agricultural, industrial, and desert terrain; the pipeline is not tied to a specific sensor. On DFC2020 a single click reaches 0.09 to 0.80 pixel F1 across eight land-cover classes at the per-class best threshold, with a mean F1 of 0.39, and it beats a pairwise INSID3 baseline on six of the eight classes at roughly four hundred times lower query cost. Indexing 1.31 million patches takes 169 s on one CPU thread, and a click returns a rendered overlay in 6 to 10 ms.

**Why this may be relevant:**

It is directly related to remote sensing or Earth observation workflows.

---

### 5. WeightBench: Evaluating Language Models as Weight-Space Programmers

**Authors:** Aayush Marasini, Barsat Khadka, Nick Rahimi

**Published:** 2026-11-13

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 26

**Venue importance score included:** 0

**arXiv ID:** 2611.18553v1

**Paper link:** http://arxiv.org/abs/2611.18553v1

**PDF link:** https://arxiv.org/pdf/2611.18553v1

**Abstract:**

Recent work shows that large language models (LLMs) can operate directly on the parameters of other neural networks. They can read what a network was trained to do, fix a network that fails, and write working networks from scratch, all without gradient descent. This capability has been termed Weight-Space Programming (WSP). Exploring this new paradigm systematically requires a robust benchmark. We introduce WEIGHTBENCH, a benchmark that evaluates LLMs of increasing capability on 42 WSP tasks across five tracks: reading, fixing and writing weights, recognizing edits that are impossible, and data-free compression. The networks whose weights the LLMs read and edit range from 2K-parameter control policies to 7B-parameter language models. Experimental benchmark results show that frontier agents can already read small networks and write working control policies without ever running them, but cannot yet patch language models, compress them without data, or tell an impossible edit from a hard one. On all 42 tasks, Claude Opus 5.5 reaches a macro score of 0.535 (Sonnet 5.5 0.466, Haiku 5.5 0.402, DeepSeek v4-flash 0.215); on the 38 tasks it was run on, GPT-6.1-sol reaches 0.568 against Opus's 0.546. Code, the task registry, our OS-level sandbox harness, and the live leaderboard are publicly available at https://github.com/Aayush-Marasini/WeightBench.

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis.

---

### 6. Few-Shot Open-Set Hyperspectral Pixel-Wise Classification with Spatial Aware Label Propagation

**Authors:** Matheus Pereira, Jefersson Santos, Laurent Najman

**Published:** 2026-11-13

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 26

**Venue importance score included:** 0

**arXiv ID:** 2611.17974v1

**Paper link:** http://arxiv.org/abs/2611.17974v1

**PDF link:** https://arxiv.org/pdf/2611.17974v1

**Abstract:**

Pixelwise classification of hyperspectral images (HSI) is a fundamental task in remote sensing, but its deployment in real-world applications is often limited by the scarcity of labeled data and the presence of unknown classes at inference time. In this work, we propose Few-shot Open-set hyperspectral recognition from Self-Supervised Learning training (FOSSeL), a unified framework for few-shot, open-set hyperspectral pixelwise classification that does not require supervised training. The proposed approach first leverages self-supervised learning to construct a discriminative feature space from unlabeled data. Then, given a small set of labeled seed pixels, class predictions are obtained through spatially-aware graph-based label propagation over superpixel representations, enabling the joint exploitation of spectral similarity and spatial consistency. To address the open-set scenario, we introduce simple yet effective strategies to identify pixels that do not belong to the known classes. We evaluate FOSSeL on three benchmark hyperspectral datasets under multiple few-shot settings. The results show that the proposed framework achieves competitive or superior performance compared to fully supervised methods while maintaining robustness in the presence of unknown classes. These findings highlight the potential of combining self-supervised feature learning with graph-based inference for practical HSI analysis in low-annotation and open-world scenarios.

**Why this may be relevant:**

It is directly related to remote sensing or Earth observation workflows.

---

### 7. WeatherDreamer: Learning a World Model from Multimodal Earth Observations

**Authors:** Kate Duffy, Elise Penn, Tristan Ballard, August Posch, Thomas J. Vandal

**Published:** 2026-11-13

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 24

**Venue importance score included:** 0

**arXiv ID:** 2611.18393v1

**Paper link:** http://arxiv.org/abs/2611.18393v1

**PDF link:** https://arxiv.org/pdf/2611.18393v1

**Abstract:**

Machine learning weather models now rival operational global forecasts but still start from analyses produced by separate, expensive data assimilation (DA) systems, which for global models are typically updated every six hours. Observation-to-observation models avoid this dependence, but most omit the recursive filtering cycle that lets DA systems carry a background state through sparse, irregular observations. We introduce WeatherDreamer, a world model that learns this cycle end-to-end from 18 global observing systems, without reanalysis. It infers a latent state from observations, carries it forward hour by hour with learned dynamics, corrects it each hour with new observations, and can predict what any of its observing systems would measure at any location. At held-out stations, its ensembles beat NOAA's Global Ensemble Forecast System (GEFS) for temperature, dew point and wind out to 12 h and are better calibrated than GEFS and the ECMWF ensemble. Precipitation, cloud-top height and solar irradiance, never inputs at inference, are inferred with skill matching or exceeding operational products at short leads. Against the first guess of NOAA's Gridpoint Statistical Interpolation (GSI) DA system, WeatherDreamer's short-range departures are within 10% of GSI's at surface stations and within 25% for moisture-sensitive microwave channels, but up to five times larger for temperature-sounding channels. Never given observation errors, its learned update assumes errors close to known instrument and retrieval errors of microwave sounders and scatterometer winds. WeatherDreamer also separates viewing geometry from atmospheric state, recovering 83-96% of observed limb darkening and producing seamless nadir-view imagery. Producing an hourly global analysis in about 1.5 minutes on one GPU, WeatherDreamer shows that assimilation and forecasting can be learned together directly from observations.

**Why this may be relevant:**

It is directly related to remote sensing or Earth observation workflows.

---

### 8. WaferTetris: Efficient Freeform Mapping on Wafer-Scale Accelerators

**Authors:** Dayou Du, Congjie He, Andrew Boutros, Luo Mai, Vaughn Betz, Jianyi Cheng

**Published:** 2026-11-13

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 22

**Venue importance score included:** 0

**arXiv ID:** 2611.18527v1

**Paper link:** http://arxiv.org/abs/2611.18527v1

**PDF link:** https://arxiv.org/pdf/2611.18527v1

**Abstract:**

Wafer-scale accelerators offer massive compute capacity through hundreds of thousands of processing elements (PEs) interconnected across a single wafer, but realizing this potential requires efficient application mapping. Their scale makes programming these systems and mapping applications onto them challenging. Existing approaches rely on template-based mappings to maintain productivity, but these templates restrict the mapping design space. In particular, they impose fixed geometric layouts over the PE grid, often leaving compute and memory resources underutilized. In this work, we present WaferTetris, a system that removes these geometric restrictions through freeform mapping. Its Tetris-like strategy flexibly packs computation across the wafer, improving PE utilization and usable memory capacity while preserving PE-task code. We develop a recurrence-based throughput model that captures branch-and-join dependencies to guide spatial parallelism, and an architecture model with per-color gates that enable existing FPGA place-and-route algorithms to enforce WSE routing constraints. We evaluate WaferTetris on Cerebras WSE-3 using LLM decoding and scientific stencil benchmarks. For LLM decoding, it achieves up to $4.42\times$ the system throughput of a template-based automatic mapping baseline on the same fabric size. Compared with the manually optimized WaferLLM, WaferTetris supports $1.8\times$ the context length for LLaMA3.1-8B (80k versus 44k), while delivering equal or higher per-user throughput at matched context lengths, up to $1.10\times$.

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis.

---

### 9. MaskSCD: Bitemporal Mask Classification for Semantic Change Detection in Remote Sensing Images

**Authors:** Weikang Yu, Pedram Ghamisi

**Published:** 2026-11-13

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 21

**Venue importance score included:** 0

**arXiv ID:** 2611.18350v1

**Paper link:** http://arxiv.org/abs/2611.18350v1

**PDF link:** https://arxiv.org/pdf/2611.18350v1

**Abstract:**

Semantic change detection (SCD) identifies where the land surface has changed and which land-cover transition has taken place. Most deep SCD networks predict the change map and the land-cover map of each date with separate per-pixel decoders. These outputs need not agree, so a pixel can be labeled as changed although it has the same class at both dates, and per-pixel decisions fragment objects. We present MaskSCD, which formulates SCD as the mask classification of a bitemporal label-pair image. Each bitemporal segment, a region of constant land-cover class pair, is predicted as one mask shared by both dates together with one class per date, and the change map is derived from the predicted class pair. This formulation keeps the change and semantic maps consistent and the label space linear in the number of classes. A bitemporal masked-attention transformer decoder implements it by reading each segment in both images and relating the two readings, and a bitemporal fusion pyramid provides per-date and change-aware features. MaskSCD is evaluated on SECOND, Landsat-SCD and Hi-UCD, which span 0.1 to 30 m resolution and four to nine land-cover classes, against fourteen recent SCD models re-trained under one protocol. MaskSCD achieves the best separated kappa, semantic change $F_1$ and transition $F_1$ on all three datasets and exceeds the strongest competitor by about five points in mean separated kappa. It produces no contradictory change pixels, which account for nearly 30% of the predicted change of some multi-task networks. The code is available at https://github.com/EricYu97/MaskSCD.

**Why this may be relevant:**

It is directly related to remote sensing or Earth observation workflows.

---

### 10. CoPre-MoE: Consolidating and Preserving MoE for Multimodal Continual Instruction Tuning

**Authors:** Tao Hu, Ling-Xiang Zhang, Da-Wei Zhou

**Published:** 2026-11-13

**Venue:** arXiv

**Found via:** arXiv

**My Score:** 20

**Venue importance score included:** 0

**arXiv ID:** 2611.18417v1

**Paper link:** http://arxiv.org/abs/2611.18417v1

**PDF link:** https://arxiv.org/pdf/2611.18417v1

**Abstract:**

Multimodal continual instruction tuning requires multimodal large language models to sequentially acquire new capabilities without catastrophic forgetting. Mixture-of-experts (MoE) architectures offer a promising way to mitigate task interference through expert specialization and combination. However, while existing MoE-based methods avoid overwriting shared parameters by allocating separate experts for each task, this progressive expansion incurs severe cross-task redundancy and linear parameter growth. Specifically, experts across tasks often learn overlapping functions alongside task-specific capabilities. For instance, ScienceQA and TextVQA both locate relevant image regions. To curb parameter redundancy without inducing forgetting, we propose Consolidating and Preserving MoE (CoPre-MoE). For each incoming task, CoPre-MoE first learns task-specific MoE to capture specialized capabilities. To eliminate redundancy and reduce parameter growth across tasks, we design a shared-and-private expert architecture. Specifically, we first evaluate functional overlap to selectively consolidate overlapping experts across tasks into a fixed-capacity generic expert pool. We then factorize the remaining task-specific experts into shared projection bases and compact task-specific cores within a private expert pool. To mitigate forgetting, we construct the router by pairing each expert with learnable retrieval keys, where historical keys remain frozen during continual updates while newly added keys are regularized with an orthogonality penalty. At inference, input-dependent routing dynamically combines both pools without test-time task labels. Extensive experiments demonstrate that CoPre-MoE achieves superior performance while substantially reducing parameter overhead.

**Why this may be relevant:**

It connects to the use of LLMs for spatial reasoning, urban planning, or geospatial analysis.

---

