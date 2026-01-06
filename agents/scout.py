


from duckduckgo_search import DDGS

def scout_brand_mentions(brand_name: str):
    query = f"{brand_name} bad experience review"
    results = []

    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=5):
            results.append({
                "text": r["body"],
                "source": r["href"]
            })

    return results
