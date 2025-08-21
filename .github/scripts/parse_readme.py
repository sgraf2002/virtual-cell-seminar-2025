import re, json

with open("README.md", "r") as f:
    content = f.read()

sections = re.split(r"\n(?=[A-Z][A-Za-z ]+\n)", content)
papers = {}
for sec in sections:
    lines = [l.strip() for l in sec.strip().splitlines() if l.strip()]
    if not lines: 
        continue
    header = lines[0]
    entries = []
    for l in lines[1:]:
        match = re.match(r"(.+?):\s+(https?://\S+)", l)
        if match:
            entries.append({"title": match.group(1), "url": match.group(2)})
    if entries:
        papers[header] = entries

with open("papers.json", "w") as f:
    json.dump(papers, f, indent=2)
