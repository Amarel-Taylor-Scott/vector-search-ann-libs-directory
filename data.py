"""Vector Search & ANN Libraries Directory — curated registry.

A catalog of **approximate-nearest-neighbor (ANN) / vector-search libraries** —
the embeddable indexes and algorithms (HNSW graphs, trees, quantization) that
power similarity search.

This is distinct from vector *databases* (managed/serviceful storage engines) and
from *embedding models* (which produce the vectors): these are the libraries you
embed to build and query an index. Each entry records: name, org, category,
whether it is open source, its license, a short note, and a GitHub link.
Uncertain licenses/URLs are omitted.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class Category(Enum):
    graph_hnsw = "graph_hnsw"
    tree_quant = "tree_quant"
    other = "other"

    @property
    def label(self) -> str:
        return {
            "graph_hnsw": "Graph-Based (HNSW) Libraries",
            "tree_quant": "Tree & Quantization Libraries",
            "other": "Other ANN Libraries",
        }[self.value]


@dataclass(frozen=True)
class Tool:
    name: str
    org: str
    category: Category
    url: str               # GitHub repo
    open_source: bool
    license: str           # SPDX-ish id, or "Proprietary"
    note: str = ""
    tags: tuple[str, ...] = field(default_factory=tuple)


# ---------------------------------------------------------------------------
# Registry — curated, public ANN / vector-search libraries (links only).
# Licenses verified to best effort; uncertain ones omitted.
# ---------------------------------------------------------------------------
TOOLS: list[Tool] = [
    # --- Graph-based (HNSW) libraries ---
    Tool("hnswlib", "nmslib", Category.graph_hnsw,
         "https://github.com/nmslib/hnswlib", True, "Apache-2.0",
         note="Header-only HNSW implementation (C++/Python).",
         tags=("hnsw", "header-only", "popular")),
    Tool("nmslib", "nmslib", Category.graph_hnsw,
         "https://github.com/nmslib/nmslib", True, "Apache-2.0",
         note="Non-Metric Space Library — fast ANN across many methods.",
         tags=("ann", "non-metric")),
    Tool("Voyager", "Spotify", Category.graph_hnsw,
         "https://github.com/spotify/voyager", True, "Apache-2.0",
         note="HNSW-based nearest-neighbor library (Python & Java).",
         tags=("hnsw", "production")),
    Tool("usearch", "Unum", Category.graph_hnsw,
         "https://github.com/unum-cloud/usearch", True, "Apache-2.0",
         note="Compact, SIMD-accelerated HNSW engine across many languages.",
         tags=("hnsw", "simd", "multi-language")),
    Tool("NGT", "Yahoo Japan", Category.graph_hnsw,
         "https://github.com/yahoojapan/NGT", True, "Apache-2.0",
         note="Graph & tree-based ANN library (Neighborhood Graph and Tree).",
         tags=("graph", "tree")),

    # --- Tree & quantization libraries ---
    Tool("FAISS", "Meta", Category.tree_quant,
         "https://github.com/facebookresearch/faiss", True, "MIT",
         note="Efficient similarity search (IVF/PQ/HNSW, CPU & GPU).",
         tags=("ivf", "pq", "gpu", "popular")),
    Tool("Annoy", "Spotify", Category.tree_quant,
         "https://github.com/spotify/annoy", True, "Apache-2.0",
         note="Tree-based ANN with memory-mapped, static indexes.",
         tags=("trees", "mmap")),
    Tool("ScaNN", "Google", Category.tree_quant,
         "https://github.com/google-research/google-research/tree/master/scann", True, "Apache-2.0",
         note="Anisotropic vector quantization for high recall at speed.",
         tags=("quantization", "recall")),

    # --- Other ANN libraries ---
    Tool("PyNNDescent", "Leland McInnes", Category.other,
         "https://github.com/lmcinnes/pynndescent", True, "BSD-2-Clause",
         note="Approximate nearest-neighbor descent (pure Python / Numba).",
         tags=("python", "nn-descent")),
    Tool("DiskANN", "Microsoft", Category.other,
         "https://github.com/microsoft/DiskANN", True, "MIT",
         note="Disk-resident graph ANN for billion-scale datasets.",
         tags=("disk", "billion-scale")),
    Tool("SPTAG", "Microsoft", Category.other,
         "https://github.com/microsoft/SPTAG", True, "MIT",
         note="Space Partition Tree And Graph ANN library.",
         tags=("tree", "graph")),
]
