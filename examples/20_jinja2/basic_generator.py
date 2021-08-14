from jinja2 import Environment, FileSystemLoader, StrictUndefined
import yaml


env = Environment(
    loader=FileSystemLoader("."),
    undefined=StrictUndefined
)
templ = env.get_template("cfg_template.txt")

with open("cfg_data.yaml") as f:
    data = yaml.safe_load(f)

for param in data:
    print(templ.render(param))
