"""Utilities for Scrapping News From Google"""

import requests
from bs4 import BeautifulSoup
from fastapi import HTTPException, status
from pydantic import ValidationError

from .models import News

BASE_URL = (
    "https://www.google.com/search?&start={start}&client=firefox-b-d"
    "&sca_esv=a30db985f4ecea9c&sxsrf=ADLYWIK8ZTWIdrLNHeoYITbuzabeobt2"
    "mA:1732880182922&q=pertanian&tbm=nws&source=lnms&fbs=AEQNm0DRkam6"
    "RZP7GtztEOLmt4oJmiAI3QJ-6ZQUalsYlC_NOOk15WNvF8ekLVxAd0FLqSe5QJ1OfS"
    "bfoznJIKO4-wLjuPDV3ajP_aomvfb8G3QmKpOntW7XgRLt__ZenW2iNqhSS0DmCvAJ"
    "v3z3J8MU5HA5S9Lwh14Wc7TLSlvK3d2_Yxg_Nt46SXVQMsCPBK2LukVzXR-z_C721Vr"
    "A_7-CbvzfR41H2w&sa=X&ved=2ahUKEwim7fbduYGKAxVtwjgGHe6ND9oQ0pQJegQIIxAB"
)


def get_content(url: str):
    """
    Get HTML content from google search news
    """
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            content = response.content
            return content

        raise HTTPException(
            status_code=status.HTTP_424_FAILED_DEPENDENCY,
            detail={"success": False, "error": "news service error"},
        )

    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_424_FAILED_DEPENDENCY,
            detail={"success": False, "error": f"{exc}"},
        ) from exc


def get_recent_news(start: int = 0):
    """Scrapping and get data from content"""
    content = get_content(BASE_URL.format(start=start))

    soup = BeautifulSoup(
        content,
        "html.parser",
    )

    results = []

    for result_item in soup.find_all("div", class_="xpd"):
        title_tag = result_item.find("h3")
        link_tag = result_item.find("a", href=True)
        publisher_tag = result_item.find("div", class_="sCuL3")
        time_tag = result_item.find("span", class_="r0bn4c")

        title = title_tag.text.strip().replace("\\n", " ") if title_tag else None
        link = (
            link_tag["href"].replace("/url?q=", "").split("&")[0] if link_tag else None
        )
        publisher = publisher_tag.text.strip() if publisher_tag else None
        time = time_tag.text.strip() if time_tag else None

        try:
            results.append(
                News.model_validate(
                    {
                        "title": title,
                        "link": link,
                        "publisher": publisher,
                        "time": time,
                    }
                )
            )
        except ValidationError:
            continue

    return results
