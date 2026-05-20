# Weekly Geospatial ML Paper Digest

This repository automatically collects recent research papers related to **geospatial analysis**, **urban climate**, **urban planning**, **infrastructure mapping**, and **geospatial problem-solving using machine learning**.

The goal is to create a weekly digest of relevant papers from **arXiv** and **Semantic Scholar**, including paper titles, authors, abstracts, and links.

## Focus Areas

This automation prioritizes papers on:

- Geospatial machine learning and GeoAI
- Remote sensing and Earth observation
- Urban climate and urban heat
- Urban planning and built environment analysis
- Transportation and pedestrian infrastructure
- Road, sidewalk, and walkability mapping
- Tree canopy, vegetation, and land-cover analysis
- Satellite imagery, aerial imagery, LiDAR, and street-view imagery
- Computer vision for geospatial applications
- Foundation models for Earth observation
- Large language models for geospatial reasoning
- Vision-language models for remote sensing
- Self-supervised learning and domain adaptation for spatial data

## Data Sources

The current version uses two sources:

1. **Semantic Scholar Graph API**
2. **arXiv**

Semantic Scholar requires an API key. arXiv does not require an API key.

## Output

Each run creates or updates two files inside the `output/` folder:

```text
output/
├── geospatial_ml_papers.md
└── geospatial_ml_papers.json