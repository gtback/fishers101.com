#!/usr/bin/env python

import jinja2
import markdown


def main():
    env = jinja2.Environment(loader=jinja2.FileSystemLoader("."))
    template = env.get_template("template.html.j2")

    with open("index.md") as source:
        contents = markdown.markdown(source.read())

    context = {
        "title": "Fishers101.com",
        "contents": contents,
    }

    print(template.render(context))


if __name__ == "__main__":
    main()
