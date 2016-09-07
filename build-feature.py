# -*- coding: utf-8 -*-

from jinja2 import Template
import json

# Load data
with open('data.json', 'r') as file:
    data = json.load(file)

# Load template file
with open('ligatures.fea.jinja2', 'r') as file:
    template = Template(file.read())

# Render feature file
with open('ligatures.fea', 'w') as file:
    file.write(template.render(data))
