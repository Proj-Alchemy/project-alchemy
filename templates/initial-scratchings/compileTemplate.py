from jinja2 import Template

var = {'HOSTNAME':'THIS_IS_A_HOSTNAME',
		'DOMAINNAME':'THE DOMAINNAME'}


# Loading Template
with open("Junos-scratchings") as file:
  data = file.read()
template = Template(data)

# render template
print(template.render(var))
