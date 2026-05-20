import os
import re
import json
import time
import hashlib
from pathlib import Path
from datetime import datetime, timedelta, timezone
from typing import Dict, List, Optional, Any

import requests
import arxiv
from dotenv import load_dotenv


# ============================================================
# Load local .env file
# ============================================================

load_dotenv()


# ============================================================
# API key
# ============================================================

SEMANTIC_SCHOLAR_API_KEY = os.getenv("SEMANTIC_SCHOLAR_API_KEY")


# ============================================================
# Settings
# ============================================================

DAYS_BACK = int(os.getenv("DAYS_BACK", "7"))
MAX_TOP_PAPERS = int(os.getenv("MAX_TOP_PAPERS", "10"))

SEMANTIC_SCHOLAR_SLEEP_SECONDS = float(
    os.getenv("SEMANTIC_SCHOLAR_SLEEP_SECONDS", "1.2")
)

ARXIV_SLEEP_SECONDS = float(
    os.getenv("ARXIV_SLEEP_SECONDS", "1.0")
)


# ============================================================
# Search terms
# ============================================================

SEARCH_TERMS = [
    # General geospatial AI / GeoAI
    "geospatial machine learning",
    "geospatial artificial intelligence",
    "spatial machine learning",
    "spatial artificial intelligence",
    "GeoAI",
    "geospatial deep learning",
    "geospatial foundation model",
    "geospatial large language model",
    "geospatial vision language model",
    "spatial data science machine learning",

    # Remote sensing / Earth observation
    "remote sensing machine learning",
    "remote sensing deep learning",
    "earth observation machine learning",
    "earth observation deep learning",
    "satellite imagery machine learning",
    "satellite imagery deep learning",
    "satellite imagery foundation model",
    "earth observation foundation model",
    "remote sensing foundation model",
    "multimodal remote sensing",
    "self-supervised learning remote sensing",
    "vision transformer remote sensing",
    "domain adaptation remote sensing",

    # Urban climate / heat / environment
    "urban climate machine learning",
    "urban heat remote sensing",
    "urban heat machine learning",
    "urban heat island deep learning",
    "land surface temperature machine learning",
    "heat exposure geospatial analysis",
    "urban microclimate machine learning",
    "thermal remote sensing urban climate",
    "urban vegetation cooling remote sensing",

    # Urban planning / infrastructure
    "urban planning machine learning",
    "urban infrastructure computer vision",
    "urban infrastructure mapping machine learning",
    "transportation infrastructure computer vision",
    "road extraction satellite imagery",
    "road network extraction deep learning",
    "sidewalk mapping computer vision",
    "pedestrian infrastructure computer vision",
    "walkability geospatial machine learning",
    "built environment machine learning",
    "urban form machine learning",

    # Trees / vegetation / land cover
    "tree detection remote sensing",
    "tree canopy LiDAR",
    "urban tree inventory remote sensing",
    "urban tree canopy machine learning",
    "vegetation mapping deep learning",
    "land cover classification deep learning",
    "land use classification machine learning",

    # Methods: CV, LLM, VLM, SSL, foundation models
    "computer vision geospatial analysis",
    "computer vision remote sensing",
    "large language model geospatial",
    "LLM geospatial analysis",
    "vision language model remote sensing",
    "VLM remote sensing",
    "foundation model geospatial",
    "foundation model urban planning",
    "self-supervised learning geospatial",
    "contrastive learning remote sensing",
    "multimodal learning geospatial",
]


# ============================================================
# Ranking terms
# ============================================================

PRIORITY_TERMS = {
    # Core geospatial / spatial analysis
    "geospatial": 7,
    "geoai": 8,
    "spatial analysis": 7,
    "spatial data": 5,
    "spatial data science": 7,
    "gis": 5,
    "geographic information system": 5,
    "spatiotemporal": 6,
    "spatial-temporal": 6,

    # Remote sensing / Earth observation
    "remote sensing": 7,
    "earth observation": 7,
    "satellite": 5,
    "satellite imagery": 7,
    "aerial imagery": 6,
    "uav": 5,
    "drone": 5,
    "lidar": 7,
    "point cloud": 6,
    "street view": 6,
    "street-level imagery": 6,

    # Urban climate and environmental applications
    "urban climate": 10,
    "urban heat": 10,
    "urban heat island": 10,
    "heat exposure": 9,
    "heat vulnerability": 8,
    "land surface temperature": 8,
    "thermal remote sensing": 8,
    "microclimate": 7,
    "climate resilience": 7,
    "urban vegetation": 7,
    "shade": 7,
    "cooling": 5,

    # Urban planning / infrastructure
    "urban planning": 10,
    "urban infrastructure": 9,
    "built environment": 8,
    "transportation infrastructure": 8,
    "road extraction": 8,
    "road network": 7,
    "sidewalk": 10,
    "pedestrian": 8,
    "pedestrian infrastructure": 10,
    "walkability": 8,
    "mobility": 5,
    "accessibility": 6,
    "land use": 7,
    "land cover": 7,
    "urban form": 7,
    "building footprint": 6,
    "impervious surface": 6,

    # Trees / vegetation
    "tree": 6,
    "tree canopy": 9,
    "tree inventory": 10,
    "urban tree": 9,
    "vegetation": 6,
    "green infrastructure": 8,

    # ML / AI methods
    "machine learning": 6,
    "deep learning": 6,
    "computer vision": 7,
    "foundation model": 10,
    "large language model": 9,
    "llm": 9,
    "vision language model": 9,
    "vlm": 9,
    "self-supervised": 8,
    "self-supervised learning": 8,
    "contrastive learning": 7,
    "vision transformer": 7,
    "transformer": 5,
    "multimodal": 8,
    "domain adaptation": 8,
    "domain generalization": 8,
    "transfer learning": 6,
    "segmentation": 6,
    "semantic segmentation": 7,
    "object detection": 6,
    "instance segmentation": 6,
    "change detection": 6,
    "graph neural network": 6,
    "gnn": 6,

    # Generalization / deployment
    "cross-city": 8,
    "cross-region": 7,
    "generalization": 6,
    "scalable": 5,
    "city-scale": 8,
    "large-scale": 5,
}


NEGATIVE_TERMS = {
    # Biology / medicine / microbiology
    "microbiology": -30,
    "biology": -20,
    "biological": -20,
    "bioinformatics": -25,
    "genomics": -30,
    "genome": -25,
    "protein": -30,
    "molecule": -30,
    "molecular": -30,
    "cell": -20,
    "cellular": -20,
    "clinical": -30,
    "medical": -30,
    "medical imaging": -35,
    "radiology": -30,
    "pathology": -30,
    "disease": -25,
    "cancer": -30,
    "drug discovery": -35,
    "pharmaceutical": -30,

    # Chemistry / materials
    "chemistry": -30,
    "chemical": -25,
    "molecular dynamics": -35,
    "catalyst": -25,
    "polymer": -25,
    "nanoparticle": -25,
    "battery": -20,
    "electrochemical": -25,
    "crystal": -20,

    # Privacy / security / cyber
    "privacy": -30,
    "security": -30,
    "cybersecurity": -35,
    "cryptography": -35,
    "encryption": -30,
    "attack": -25,
    "adversarial attack": -25,
    "malware": -35,
    "phishing": -35,
    "intrusion detection": -35,
    "network security": -35,
    "federated privacy": -25,

    # Other unrelated ML areas
    "stock market": -20,
    "financial": -20,
    "e-commerce": -15,
}


# ============================================================
# Utility functions
# ============================================================

def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def clean_text(text: Optional[str]) -> str:
    if not text:
        return ""

    text = str(text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = text.replace("\n", " ").replace("\r", " ")

    return " ".join(text.split())


def normalize_title(title: str) -> str:
    title = clean_text(title).lower()
    title = re.sub(r"[^a-z0-9]+", " ", title)

    return " ".join(title.split())


def parse_date(date_text: Optional[str]) -> Optional[datetime]:
    if not date_text:
        return None

    date_text = str(date_text).strip()

    for pattern in ["%Y-%m-%d", "%Y-%m", "%Y"]:
        try:
            dt = datetime.strptime(date_text, pattern)
            return dt.replace(tzinfo=timezone.utc)
        except ValueError:
            pass

    try:
        return datetime.fromisoformat(
            date_text.replace("Z", "+00:00")
        ).astimezone(timezone.utc)
    except Exception:
        return None


def date_in_window(
    date_text: Optional[str],
    start_date: datetime,
    end_date: datetime
) -> bool:
    dt = parse_date(date_text)

    if not dt:
        return False

    return start_date <= dt <= end_date


def paper_key(paper: Dict[str, Any]) -> str:
    doi = paper.get("doi")

    if doi:
        doi = doi.lower().replace("https://doi.org/", "").strip()
        return f"doi:{doi}"

    title = normalize_title(paper.get("title", ""))

    if title:
        return f"title:{title}"

    raw = json.dumps(paper, sort_keys=True)
    return "hash:" + hashlib.md5(raw.encode("utf-8")).hexdigest()


def paper_text(paper: Dict[str, Any]) -> str:
    return (
        f"{paper.get('title', '')} "
        f"{paper.get('abstract', '')} "
        f"{paper.get('venue', '')}"
    ).lower()


# ============================================================
# Filtering and scoring
# ============================================================

def is_excluded_paper(paper: Dict[str, Any]) -> bool:
    text = paper_text(paper)

    hard_exclusion_terms = [
        # Microbiology / biology / medicine
        "microbiology",
        "bioinformatics",
        "genomics",
        "genome",
        "protein",
        "molecule",
        "molecular",
        "cellular",
        "clinical",
        "medical imaging",
        "radiology",
        "pathology",
        "cancer",
        "drug discovery",

        # Chemistry / materials
        "chemistry",
        "chemical reaction",
        "molecular dynamics",
        "catalyst",
        "polymer",
        "nanoparticle",
        "electrochemical",

        # Privacy / security
        "privacy",
        "cybersecurity",
        "cryptography",
        "encryption",
        "malware",
        "phishing",
        "intrusion detection",
        "network security",
    ]

    return any(term in text for term in hard_exclusion_terms)


def is_relevant_geospatial_paper(paper: Dict[str, Any]) -> bool:
    text = paper_text(paper)

    geospatial_anchor_terms = [
        "geospatial",
        "geoai",
        "spatial analysis",
        "spatial data",
        "gis",
        "remote sensing",
        "earth observation",
        "satellite",
        "satellite imagery",
        "aerial imagery",
        "lidar",
        "point cloud",
        "street view",
        "street-level imagery",
        "urban",
        "city",
        "cities",
        "land cover",
        "land use",
        "built environment",
        "transportation infrastructure",
    ]

    method_or_problem_terms = [
        "machine learning",
        "deep learning",
        "computer vision",
        "foundation model",
        "large language model",
        "llm",
        "vision language model",
        "vlm",
        "nlp",
        "self-supervised",
        "contrastive learning",
        "transformer",
        "segmentation",
        "object detection",
        "classification",
        "prediction",
        "mapping",
        "urban climate",
        "urban heat",
        "urban planning",
        "infrastructure",
        "road",
        "sidewalk",
        "pedestrian",
        "tree",
        "vegetation",
        "transportation",
        "accessibility",
        "walkability",
    ]

    has_geospatial_anchor = any(term in text for term in geospatial_anchor_terms)
    has_method_or_problem = any(term in text for term in method_or_problem_terms)

    return has_geospatial_anchor and has_method_or_problem


def score_paper(paper: Dict[str, Any]) -> int:
    text = paper_text(paper)

    score = 0

    for term, weight in PRIORITY_TERMS.items():
        if term in text:
            score += weight

    for term, penalty in NEGATIVE_TERMS.items():
        if term in text:
            score += penalty

    # Metadata bonus
    if paper.get("doi"):
        score += 2

    if paper.get("pdf"):
        score += 1

    if len(paper.get("sources", [])) > 1:
        score += 3

    if len(paper.get("abstract", "")) > 300:
        score += 2

    # Topic-combination bonuses
    if "foundation model" in text and (
        "remote sensing" in text
        or "earth observation" in text
        or "geospatial" in text
    ):
        score += 12

    if ("large language model" in text or "llm" in text) and (
        "geospatial" in text
        or "urban planning" in text
        or "spatial" in text
    ):
        score += 10

    if ("vision language model" in text or "vlm" in text) and (
        "remote sensing" in text
        or "satellite" in text
        or "geospatial" in text
    ):
        score += 10

    if "lidar" in text and ("tree" in text or "canopy" in text):
        score += 10

    if "urban" in text and ("heat" in text or "climate" in text):
        score += 10

    if "urban planning" in text and (
        "machine learning" in text
        or "deep learning" in text
        or "foundation model" in text
    ):
        score += 8

    if "sidewalk" in text or "pedestrian infrastructure" in text:
        score += 10

    if "road extraction" in text or "road network" in text:
        score += 8

    if "domain adaptation" in text and (
        "remote sensing" in text
        or "satellite" in text
        or "geospatial" in text
    ):
        score += 8

    return score


# ============================================================
# Deduplication
# ============================================================

def merge_paper(
    existing: Dict[str, Any],
    new: Dict[str, Any]
) -> Dict[str, Any]:
    existing_sources = set(existing.get("sources", []))
    new_sources = set(new.get("sources", []))

    if existing.get("source"):
        existing_sources.add(existing["source"])

    if new.get("source"):
        new_sources.add(new["source"])

    existing["sources"] = sorted(existing_sources.union(new_sources))

    fields = [
        "title",
        "authors",
        "abstract",
        "published",
        "doi",
        "url",
        "pdf",
        "venue",
        "semantic_scholar_paper_id",
        "arxiv_id",
        "citation_count",
        "reference_count",
        "influential_citation_count",
    ]

    for field in fields:
        if not existing.get(field) and new.get(field):
            existing[field] = new[field]

    # Prefer longer abstract
    if len(new.get("abstract", "")) > len(existing.get("abstract", "")):
        existing["abstract"] = new["abstract"]

    return existing


def add_paper(
    papers: Dict[str, Dict[str, Any]],
    paper: Dict[str, Any]
) -> None:
    title = clean_text(paper.get("title", ""))

    if not title:
        return

    paper["title"] = title
    paper["abstract"] = clean_text(paper.get("abstract", ""))
    paper["authors"] = clean_text(paper.get("authors", ""))
    paper["venue"] = clean_text(paper.get("venue", ""))

    key = paper_key(paper)

    if key in papers:
        papers[key] = merge_paper(papers[key], paper)
    else:
        papers[key] = paper


# ============================================================
# Semantic Scholar search
# ============================================================

def search_semantic_scholar(
    start_date: datetime,
    end_date: datetime
) -> List[Dict[str, Any]]:
    if not SEMANTIC_SCHOLAR_API_KEY:
        raise RuntimeError(
            "SEMANTIC_SCHOLAR_API_KEY is not set. "
            "Create a .env file locally or add it as a GitHub Actions secret."
        )

    results = []

    headers = {
        "x-api-key": SEMANTIC_SCHOLAR_API_KEY
    }

    for term in SEARCH_TERMS:
        url = "https://api.semanticscholar.org/graph/v1/paper/search"

        params = {
            "query": term,
            "limit": 25,
            "fields": (
                "paperId,title,authors,abstract,year,publicationDate,url,venue,"
                "externalIds,openAccessPdf,citationCount,referenceCount,"
                "influentialCitationCount"
            ),
        }

        try:
            response = requests.get(
                url,
                params=params,
                headers=headers,
                timeout=30,
            )
        except requests.RequestException as error:
            print(f"[Semantic Scholar] Request error for '{term}': {error}")
            continue

        if response.status_code == 429:
            print("[Semantic Scholar] Rate limited. Sleeping 60 seconds...")
            time.sleep(60)
            continue

        if response.status_code != 200:
            print(
                f"[Semantic Scholar] Failed {response.status_code}: "
                f"{response.text[:300]}"
            )
            time.sleep(SEMANTIC_SCHOLAR_SLEEP_SECONDS)
            continue

        data = response.json().get("data", [])

        for item in data:
            pub_date = item.get("publicationDate")

            if not date_in_window(pub_date, start_date, end_date):
                continue

            external_ids = item.get("externalIds") or {}
            open_access_pdf = item.get("openAccessPdf") or {}

            authors = ", ".join(
                author.get("name", "")
                for author in item.get("authors", [])[:8]
                if author.get("name")
            )

            paper = {
                "source": "Semantic Scholar",
                "sources": ["Semantic Scholar"],
                "title": clean_text(item.get("title")),
                "authors": authors,
                "abstract": clean_text(item.get("abstract")),
                "published": pub_date,
                "doi": external_ids.get("DOI"),
                "url": item.get("url"),
                "pdf": open_access_pdf.get("url"),
                "venue": clean_text(item.get("venue")),
                "semantic_scholar_paper_id": item.get("paperId"),
                "arxiv_id": external_ids.get("ArXiv"),
                "citation_count": item.get("citationCount"),
                "reference_count": item.get("referenceCount"),
                "influential_citation_count": item.get(
                    "influentialCitationCount"
                ),
            }

            results.append(paper)

        print(f"[Semantic Scholar] '{term}' returned {len(data)} raw results.")
        time.sleep(SEMANTIC_SCHOLAR_SLEEP_SECONDS)

    return results


# ============================================================
# arXiv search
# ============================================================

def search_arxiv(
    start_date: datetime,
    end_date: datetime
) -> List[Dict[str, Any]]:
    results = []
    client = arxiv.Client()

    for term in SEARCH_TERMS:
        search = arxiv.Search(
            query=term,
            max_results=30,
            sort_by=arxiv.SortCriterion.SubmittedDate,
        )

        try:
            items = list(client.results(search))
        except Exception as error:
            print(f"[arXiv] Error for '{term}': {error}")
            continue

        for item in items:
            published = item.published

            if published.tzinfo is None:
                published = published.replace(tzinfo=timezone.utc)

            if not (start_date <= published <= end_date):
                continue

            arxiv_id = item.get_short_id()

            paper = {
                "source": "arXiv",
                "sources": ["arXiv"],
                "title": clean_text(item.title),
                "authors": ", ".join(
                    author.name for author in item.authors[:8]
                ),
                "abstract": clean_text(item.summary),
                "published": published.strftime("%Y-%m-%d"),
                "doi": item.doi,
                "url": item.entry_id,
                "pdf": item.pdf_url,
                "venue": "arXiv",
                "semantic_scholar_paper_id": "",
                "arxiv_id": arxiv_id,
                "citation_count": None,
                "reference_count": None,
                "influential_citation_count": None,
            }

            results.append(paper)

        print(f"[arXiv] '{term}' checked {len(items)} results.")
        time.sleep(ARXIV_SLEEP_SECONDS)

    return results


# ============================================================
# Output writing
# ============================================================

def why_relevant(paper: Dict[str, Any]) -> str:
    text = paper_text(paper)

    reasons = []

    if "foundation model" in text:
        reasons.append(
            "It may help track foundation-model directions for "
            "Earth observation or geospatial AI."
        )

    if "large language model" in text or "llm" in text:
        reasons.append(
            "It connects to the use of LLMs for spatial reasoning, "
            "urban planning, or geospatial analysis."
        )

    if "vision language model" in text or "vlm" in text:
        reasons.append(
            "It may be useful for multimodal geospatial understanding "
            "using image-text models."
        )

    if (
        "remote sensing" in text
        or "earth observation" in text
        or "satellite" in text
    ):
        reasons.append(
            "It is directly related to remote sensing or Earth observation workflows."
        )

    if "lidar" in text or "point cloud" in text:
        reasons.append(
            "It may be useful for LiDAR-based tree inventory, urban structure "
            "mapping, or 3D geospatial analysis."
        )

    if "tree" in text or "canopy" in text or "vegetation" in text:
        reasons.append(
            "It connects to urban tree detection, canopy mapping, or vegetation analysis."
        )

    if "urban heat" in text or "urban climate" in text or "heat" in text:
        reasons.append(
            "It is relevant to urban climate and heat-resilience research."
        )

    if (
        "urban planning" in text
        or "built environment" in text
        or "infrastructure" in text
    ):
        reasons.append(
            "It is related to urban planning, infrastructure, or built-environment analysis."
        )

    if (
        "sidewalk" in text
        or "pedestrian" in text
        or "road extraction" in text
        or "road network" in text
    ):
        reasons.append(
            "It may connect to pedestrian infrastructure, road extraction, "
            "transportation infrastructure, or walkability mapping."
        )

    if "domain adaptation" in text or "generalization" in text:
        reasons.append(
            "It may help with cross-city, cross-region, or cross-sensor generalization."
        )

    if not reasons:
        reasons.append(
            "It matched the geospatial machine learning search criteria "
            "and may be worth screening."
        )

    return " ".join(reasons)


def write_markdown_report(
    papers: List[Dict[str, Any]],
    start_date: datetime,
    end_date: datetime,
    output_file: Path
) -> None:
    with output_file.open("w", encoding="utf-8") as file:
        file.write("# Weekly Geospatial ML Papers\n\n")

        file.write(
            f"**Search window:** "
            f"{start_date.strftime('%Y-%m-%d')} to "
            f"{end_date.strftime('%Y-%m-%d')}\n\n"
        )

        file.write("**Sources:** arXiv and Semantic Scholar\n\n")
        file.write(f"**Total selected papers:** {len(papers)}\n\n")

        file.write(
            "This digest focuses on geospatial analysis, urban climate, "
            "urban planning, infrastructure, and geospatial problem-solving "
            "using ML, computer vision, LLMs, VLMs, foundation models, "
            "self-supervised learning, and related methods.\n\n"
        )

        if not papers:
            file.write("No matching papers found this week.\n")
            return

        file.write("## Top Papers\n\n")

        for index, paper in enumerate(papers, start=1):
            file.write(f"### {index}. {paper.get('title', 'Untitled')}\n\n")

            if paper.get("authors"):
                file.write(f"**Authors:** {paper['authors']}\n\n")

            if paper.get("published"):
                file.write(f"**Published:** {paper['published']}\n\n")

            if paper.get("venue"):
                file.write(f"**Venue:** {paper['venue']}\n\n")

            if paper.get("sources"):
                file.write(f"**Found via:** {', '.join(paper['sources'])}\n\n")

            file.write(f"** My Score:** {paper.get('score', 0)}\n\n")

            if paper.get("citation_count") is not None:
                file.write(
                    f"**Semantic Scholar citations:** "
                    f"{paper['citation_count']}\n\n"
                )

            if paper.get("doi"):
                file.write(f"**DOI:** {paper['doi']}\n\n")

            if paper.get("arxiv_id"):
                file.write(f"**arXiv ID:** {paper['arxiv_id']}\n\n")

            if paper.get("url"):
                file.write(f"**Paper link:** {paper['url']}\n\n")

            if paper.get("pdf"):
                file.write(f"**PDF link:** {paper['pdf']}\n\n")

            file.write("**Abstract:**\n\n")

            abstract = paper.get("abstract") or "No abstract available."
            file.write(f"{abstract}\n\n")

            file.write("**Why this may be relevant:**\n\n")
            file.write(f"{why_relevant(paper)}\n\n")

            file.write("---\n\n")


def write_json_report(
    papers: List[Dict[str, Any]],
    output_file: Path
) -> None:
    with output_file.open("w", encoding="utf-8") as file:
        json.dump(papers, file, indent=2, ensure_ascii=False)


# ============================================================
# Main workflow
# ============================================================

def collect_all_papers(
    start_date: datetime,
    end_date: datetime
) -> Dict[str, Dict[str, Any]]:
    all_papers: Dict[str, Dict[str, Any]] = {}

    source_functions = [
        search_semantic_scholar,
        search_arxiv,
    ]

    for function in source_functions:
        print(f"\n=== Searching {function.__name__} ===")

        try:
            results = function(start_date, end_date)
        except Exception as error:
            print(f"[ERROR] {function.__name__} failed: {error}")
            continue

        print(f"[{function.__name__}] Collected {len(results)} candidate papers.")

        for paper in results:
            add_paper(all_papers, paper)

    return all_papers


def main() -> None:
    end_date = now_utc()
    start_date = end_date - timedelta(days=DAYS_BACK)

    print("Weekly Geospatial ML Paper Search")
    print(
        f"Search window: "
        f"{start_date.strftime('%Y-%m-%d')} to "
        f"{end_date.strftime('%Y-%m-%d')}"
    )

    all_papers = collect_all_papers(start_date, end_date)

    print(f"\nTotal unique papers before scoring: {len(all_papers)}")

    for paper in all_papers.values():
        paper["score"] = score_paper(paper)

    ranked_papers = sorted(
        all_papers.values(),
        key=lambda paper: paper.get("score", 0),
        reverse=True,
    )

    ranked_papers = [
        paper
        for paper in ranked_papers
        if (
            paper.get("score", 0) > 0
            and is_relevant_geospatial_paper(paper)
            and not is_excluded_paper(paper)
        )
    ]

    top_papers = ranked_papers[:MAX_TOP_PAPERS]

    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    markdown_file = output_dir / "geospatial_ml_papers.md"
    json_file = output_dir / "geospatial_ml_papers.json"

    write_markdown_report(
        papers=top_papers,
        start_date=start_date,
        end_date=end_date,
        output_file=markdown_file,
    )

    write_json_report(
        papers=top_papers,
        output_file=json_file,
    )

    print(f"\nSaved Markdown report: {markdown_file}")
    print(f"Saved JSON report: {json_file}")
    print(f"Selected top papers: {len(top_papers)}")

    print("\nTop selected papers:")
    for index, paper in enumerate(top_papers, start=1):
        print(f"{index}. [{paper.get('score', 0)}] {paper.get('title')}")


if __name__ == "__main__":
    main()