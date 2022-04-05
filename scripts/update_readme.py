import glob
import json
import os.path

from jinja2 import Environment, FileSystemLoader

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATEDIR = os.path.join(ROOT, 'templates')

challenges = []

# Get all directories in challenges with an info.json file
for f in glob.glob("challenges/*/info.json"):
    with open(f) as infofile:
        info = json.load(infofile)
        info["path"] = os.path.dirname(f)
        challenges.append(info)

# Sort the challenges by order
challenges = sorted(challenges, key=lambda d: d.get("order", 100))

jinjaEnv = Environment(loader=FileSystemLoader(TEMPLATEDIR))

readmeTemplate = jinjaEnv.get_template("readme.md.j2")
rendered = readmeTemplate.render(challenges=challenges)

with open(os.path.join(ROOT, "README.md"), "w") as readmeFile:
    readmeFile.write(rendered)
