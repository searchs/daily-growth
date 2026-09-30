# Web scraping with Beautiful Soup

Consolidated from the historical `in-few-steps` repository.

## Install

```bash
uv add beautifulsoup4 requests
```

## Fetch and parse HTML

```python
import requests
from bs4 import BeautifulSoup

response = requests.get("https://example.com", timeout=15)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
```

## Extract links

```python
for link in soup.find_all("a"):
    print(link.get("href"))
```

## Extract a page title

```python
title = soup.find("title")
if title is not None:
    print(title.get_text(strip=True))
```

## Operational considerations

- Check the site's terms and robots policy before scraping.
- Set timeouts and handle HTTP errors.
- Rate-limit repeated requests.
- Prefer a documented API when one is available.
- Validate and normalise extracted data before downstream processing.
