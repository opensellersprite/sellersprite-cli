"""Skills loader — discover and parse skill cards from data directory."""

from dataclasses import dataclass
from importlib.resources import files as pkg_files
from pathlib import Path


@dataclass
class SkillCard:
    name: str
    category: str
    path: Path
    content: str


def _get_skills_dir() -> Path:
    return Path(str(pkg_files("sellersprite_cli") / "skills"))


def load_skills() -> list[SkillCard]:
    """Load all skill cards from the package data directory."""
    skills_dir = _get_skills_dir()
    if not skills_dir.exists():
        return []

    cards: list[SkillCard] = []
    for category_dir in sorted(skills_dir.iterdir()):
        if not category_dir.is_dir() or category_dir.name.startswith("."):
            continue
        if category_dir.name == "README.md":
            continue
        for md_file in sorted(category_dir.glob("*.md")):
            content = md_file.read_text(encoding="utf-8")
            cards.append(SkillCard(
                name=md_file.stem,
                category=category_dir.name,
                path=md_file,
                content=content,
            ))
    return cards


def load_skills_index() -> str | None:
    """Load the skills README index."""
    readme = _get_skills_dir() / "README.md"
    if readme.exists():
        return readme.read_text(encoding="utf-8")
    return None


def get_skills_by_category() -> dict[str, list[SkillCard]]:
    """Group skills by category."""
    result: dict[str, list[SkillCard]] = {}
    for card in load_skills():
        result.setdefault(card.category, []).append(card)
    return result


CATEGORY_NAMES: dict[str, str] = {
    "comprehensive": "综合分析",
    "category-structure": "类目结构",
    "edge-opportunity": "机会捕捉",
    "keyword-trend": "关键词趋势",
    "new-product-burst": "新品爆发",
    "product-defect": "产品缺陷",
    "traffic-audit": "流量防伪",
}
