# -*- coding: utf-8 -*-

from jinja2 import Template
import json

with open('ligatures.json', 'r') as file:
    ligatures = json.load(file)

with open('ligatures.fea.jinja2', 'r') as file:
    template = Template(file.read())

with open('ligatures.fea', 'w') as file:
    file.write(template.render({'ligatures': ligatures}))
