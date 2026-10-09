def search_ddg(query: str, num_results: int = 5) -> str:
    """Searches DuckDuckGo and returns concise summaries of top results.
    
    Args:
        query: The search query string
        num_results: Number of results to return (default: 5, max: 10)
        
    Returns:
        Formatted string with bullet points of top results, each with title and brief summary
        
    Examples:
        {"query": "who invented the lightbulb", "num_results": 3}
    """
    from duckduckgo_search import DDGS
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=min(num_results, 10)))
            if not results:
                return "No results found"

            summaries = []
            for r in results:
                title = r['title'] #以最后一个 . 为界，取它左边的部分，常用于去除文件扩展名。
                snippet = r['body'][:200].rsplit('.', 1)[0] + '.' ##"a.b.c.d".rsplit('.', 1)[0] # 'a.b.c' ##第一个参数 '.'：以点号作为分隔符  第二个参数 1：最多只分割 1 次
                summaries.append(f"• {title}\n  {snippet}")
            return "\n\n".join(summaries)
    except Exception as e:
        return f"Error: {str(e)}" 


def search_brave(query: str, num_results: int = 5) -> str:
    """Searches Brave and returns concise summaries of top results.
    
    Args:
        query: The search query string
        num_results: Number of results to return (default: 5, max: 10)
        
    Returns:
        Formatted string with bullet points of top results, each with title, source, and brief summary
        
    Examples:
        {"query": "who invented the lightbulb", "num_results": 3}
    """
    from brave import Brave
    from typing import List, Dict, Any
    try:
        brave = Brave()
        results = brave.search(q=query, count=min(num_results, 10)) # type: ignore
        results: List[Dict[str, Any]] = results.web_results # type: ignore
        if not results:
            return "No results found"

        summaries = []
        for r in results:
            header = f"{r['profile']['name']} ({r['profile']['long_name']})"
            title = r['title']
            snippet = r['description'] #[:200].rsplit('.', 1)[0] + '.'
            summaries.append(f"•  {header}\n   {title}\n   {snippet}")
        return "\n\n".join(summaries)
    except Exception as e:
        return f"Error: {str(e)}"

