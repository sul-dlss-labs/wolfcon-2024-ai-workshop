import argparse
import datetime
import json
import pathlib

import markdown

from bs4 import BeautifulSoup
from jinja2 import DictLoader, Environment



base_template = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>AI Workflows for FOLIO - {{ title }}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <style>

    </style>
  </head>
  <body>
    <div class="header">
     <div class="container">
       <h1 style="color: #0a3a85; font-size: 3em;">WOLFcon 2024 - Understanding and Using AI Workflows with FOLIO</h1>
       <h3>23 September 2024</h3>
       <hr>
     </div>
    </div>
    <div class="container">
    {% block main %}{% endblock %}
    </div>
    <footer style="background-color: #0a3a85; color: white;" >
      <div class="container">Original Content by Jeremy Nelson &copy; 2024, <a href="https://github.com/jermnelson/wolfcon-02024-ai">Github</a></div>
    </footer> 
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
  </body>
</html>"""

html_template = """{% extends "base.html" %}
{% block main %}
      <div class="row">
        <article class="col-9">
         {{ content|safe }}
        </article>
        <div class="col-3">
          <h4>Navigation</h4>
          {{ page_navigation|safe }}
        </div>
      </div>
{% endblock %}
"""

quotes_carousel = """{% extends "base.html" %}

{% block main %}
<div class="row">
<div>
 <div id="carousel-ai-quotes" class="carousel slide" data-bs-ride="carousel">
  <div class="carousel-inner">
    {% for quote in quotes %}
    <div class="carousel-item {% if loop.first %}active{% endif %}">
      <figure class="d-block w-100">
        <blockquote class="blockquote">
         <p>{{ quote.quote| safe }}</p>
        </blockquote>
        <figcaption class="blockquote-footer">
         {{ quote.author }} on {{ quote.date }} from {{ quote.cite.type }} <cite title="{{ quote.cite.title }}">
          <a href="{{ quote.cite.link }}">{{ quote.cite.title }}</a></cite>
        </figcaption>
      </figure>
    </div>
    {% endfor %}
  </div>
 </div>
 <button class="carousel-control-prev" type="button" data-bs-target="#carousel-ai-quotes" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carousel-ai-quotes" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
 </div>
</div>
<div class="row">
  <div>
     <h2>Workshop</h2>
      {{ page_navigation|safe }}
  </div>
  <div>
     <h2>Prerequisites</h2>
  </div>
</div>
{% endblock %}
 """

jinja_env = Environment(
    loader=DictLoader(
        {
            "base.html": base_template,
            "topic.html": html_template,
            "home.html": quotes_carousel,
        }
    )
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

    home_template = jinja_env.get_template("home.html")


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
    html_template = jinja_env.get_template("topic.html")
    for row in base_dir.iterdir():
        if row.name in ["prep", ".ipynb_checkpoints", ".git", "notebooks"]:
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
