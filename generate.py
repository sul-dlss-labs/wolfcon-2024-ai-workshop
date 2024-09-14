import argparse
import datetime
import json
import pathlib

import markdown

from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader 

jinja_env = Environment(
    loader=FileSystemLoader("templates")
)

area_order = [
    {"title": "Introduction to WOLFcon AI Pre-conference Workshop", "link": "/intro-pre-conference/index.html" },
    {"title": "General Overview of AI and Machine Learning for Libraries", "link": "/types-of-ai-ml-relevant-to-libraries/index.html"},
    {"title": "Ethical Considerations on using AI and Machine Learning for Libraries", "link": "/ethical-considerations-ai-ml-for-libraries/index.html"},
    {"title": "Exploring Large Language Models", "link": "/exploring-llms/index.html"},
    {"title": "FOLIO AI Use Cases", "link": "/folio-ai-use-cases/index.html"},
    {"title": "Next Steps for Adopting AI and Machine Learning in FOLIO", "link": "/next-steps-for-adopting-ai-and-ml-in-folio/index.html"},
    {"title": "Recommended Resources for Further Learning", "link": "/recommended-resources-for-further-learning/index.html"} 
]

def generate_page_navigation(lookup, area_title, topic_title, public=False):
    nav_html = "<ol>"
    for area in area_order:
        area_link = area['link']
        if public:
            area_link = f"/wolfcon-2024-ai-workshop{area_link}"
        if area['title'] == area_title:
            nav_html += f"""<li><a href="{area_link}">{area_title}</a><ul>"""
            for link, title in lookup.items():
                if title == topic_title:
                    nav_html += f"""<li><strong>{topic_title}</strong></li>"""
                else:
                    nav_html += f"""<li><a href="{link}">{title}</a></li>"""
            nav_html += "</ul></li>"
        else:
            nav_html += f"""<li><a href="{area_link}">{area['title']}</a></li>"""
    nav_html += "</ol>"
    return nav_html
                

def get_title(html):
    soup = BeautifulSoup(html, "html.parser")
    h1 = soup.find("h1")
    return h1.text

def navigation_lookup(index):
    lookup = {}
    soup = BeautifulSoup(markdown.markdown(index.read_text()), "html.parser")
    area_title = soup.find("h1").text
    topics = soup.find_all("li")
    for topic in topics:
        link = topic.find("a")
        if link is None:
            continue
        lookup[link.attrs['href']] = link.text
    return lookup

def home_page(is_public=False):
    quotes_path = pathlib.Path("quotes.json")
    with quotes_path.open() as fo:
        quotes=json.load(fo)

    home_template = jinja_env.get_template("quotes-carousel.html")

    page_navigation = "<ol>"
    for area in area_order:
        link = area['link']
        if is_public:
            link = f"/wolfcon-2024-ai-workshop{link}"
        page_navigation += f"""<li><a href="{link}">{area['title']}</a></li>""" 
    page_navigation += "</ol>"

    index_html = home_template.render(
        quotes=quotes,
        title="Home Page",
        page_navigation=page_navigation
    )
  
    index_path = pathlib.Path("index.html")
    index_path.write_text(index_html)
    

def html_pages(is_public=False):
    base_dir = pathlib.Path(".")
    
    for row in base_dir.iterdir():
        if row.name in ["prep", ".ipynb_checkpoints", ".git", "notebooks", "templates"]:
            continue
        if row.is_dir():
            index = row / "index.md"
            area_title = get_title(markdown.markdown(index.read_text()))
            print(f"Generates pages for {area_title}")
            nav_lookup = navigation_lookup(index)
            for page in row.glob("*.md"):
                page_output = row / f"{page.stem}.html"     
                #topic_html = markdown.markdown(page.read_text(), extensions=['footnotes', 'attr_list', 'fenced_code'])
                topic_html = markdown.markdown(page.read_text(), extensions=['extra'])
                page_title = get_title(topic_html)
                match page.stem:

                    case "i-ching-exercise":
                        html_template = jinja_env.get_template("i-ching.html")

                    case _:
                        html_template = jinja_env.get_template("topic.html")
 
                page_html = html_template.render(
                    content=topic_html,
                    title=page_title,
                    page_navigation=generate_page_navigation(nav_lookup, area_title, page_title, is_public)
                )

                    
 
                with page_output.open("w+") as fo:
                    fo.write(page_html)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--public", help="support for Github pages")
    args = parser.parse_args()
    current = datetime.datetime.now()
    print(f"Generating HTML from Markdown content at {current}")
    html_pages(args.public)
    home_page(args.public)
