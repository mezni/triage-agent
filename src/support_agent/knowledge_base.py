import json
from pathlib import Path

from support_agent.models import KnowledgeArticle

KNOWLEDGE_BASE_PATH = Path("data/knowledge_base.json")


def load_knowledge_base() -> list[KnowledgeArticle]:
    data = json.loads(
        KNOWLEDGE_BASE_PATH.read_text()
    )

    return [
        KnowledgeArticle.model_validate(item)
        for item in data
    ]


def search_knowledge_base(
    query: str,
    category: str | None = None,
) -> list[KnowledgeArticle]:
    articles = load_knowledge_base()

    query_words = set(
        query.lower().split()
    )

    results = []

    for article in articles:
        if category and article.category != category:
            continue

        searchable_text = (
            f"{article.title} "
            f"{article.content}"
        ).lower()

        score = sum(
            1
            for word in query_words
            if word in searchable_text
        )

        if score > 0:
            results.append(
                (score, article)
            )

    results.sort(
        key=lambda item: item[0],
        reverse=True,
    )

    return [
        article
        for _, article in results
    ]