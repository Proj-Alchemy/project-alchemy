from jinja2 import Template
import yaml

template_file = '../junos.j2'
variable_file = 'variableExample.yml'

with open(variable_file) as file:
  var = yaml.load(file, Loader=yaml.FullLoader)

# Loading Template
with open(template_file) as file:
  data = file.read()
template = Template(data)

# render template
print(template.render(var))
