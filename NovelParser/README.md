<!-- TOC -->
* [NovelParser](#novelparser)
  * [1. Crawl the Raw Data](#1-crawl-the-raw-data)
  * [2. Purging and Formatting](#2-purging-and-formatting)
  * [3. Create EPUB with Pandoc](#3-create-epub-with-pandoc)
  * [4. Convert to AZW3 with Calibre](#4-convert-to-azw3-with-calibre)
<!-- TOC -->

# NovelParser

Recently I've been reading an old web novel.
Instead of reading online staring at my phone screen/monitor, I'd prefer using my Kindle E-reader which might be better for my eyes.
A broad search on the internet does not give me a satisfying ebook format of this novel, so I've decided to make my own.
Here I make a record of how I crawled novel contents from the web and then parsed it into an ebook for reading on Kindle.

You can check out the web novel [here (in Chinese)](https://www.ddxss.cc/book/2517/) if you're interested.

## 1. Crawl the Raw Data

Use [Web Scraper](https://webscraper.io/), you can import the following sitemap:

```json
{
  "_id": "ddxss",
  "startUrl": [
    "https://www.ddxss.cc/book/2517/"
  ],
  "selectors": [
    {
      "id": "title-link",
      "parentSelectors": [
        "_root"
      ],
      "type": "SelectorLink",
      "selector": ".listmain dl > dd a, .dd_hide a",
      "multiple": true,
      "linkType": "linkFromHref"
    },
    {
      "id": "chapter-text",
      "parentSelectors": [
        "title-link"
      ],
      "type": "SelectorText",
      "selector": "div.Readarea",
      "multiple": false,
      "regex": ""
    }
  ]
}
```

Then you should be able to extract a `.csv` file containing the novel chapter titles and chapter contents.

## 2. Purging and Formatting

Filter the chapter contents, remove ads and unnecessary line breaks.

Format the chapters in the following structure:

```markdown
% Book Name
% Author Name

# Chapter 1

Content.

# Chapter 2

Content.

...
```

- EPUB format reference: [Creating an ebook with pandoc](https://pandoc.org/epub.html)

Run the script to do so:

```shell
python main.py
```

## 3. Create EPUB with Pandoc

```shell
pandoc book.md -o book.epub
```

## 4. Convert to AZW3 with Calibre

Nothing special, just use [Calibre](https://calibre-ebook.com/) GUI.
