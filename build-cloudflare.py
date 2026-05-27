import os
import re
import shutil

source_dir = 'en'
build_dir = 'build-en'

if os.path.exists(build_dir):
    shutil.rmtree(build_dir)
shutil.copytree(source_dir, build_dir)

# Ensure openapi.json exists in build_dir
openapi_src = os.path.join(source_dir, '.gitbook', 'assets', 'openapi.json')
openapi_dest = os.path.join(build_dir, '.gitbook', 'assets', 'openapi.json')
if os.path.exists(openapi_src):
    os.makedirs(os.path.dirname(openapi_dest), exist_ok=True)
    shutil.copy(openapi_src, openapi_dest)

# Regex patterns
openapi_start = re.compile(r'{%\s*openapi-operation\s+spec="[^"]+"\s+path="([^"]+)"\s+method="([^"]+)"\s*%}')
openapi_end = re.compile(r'{%\s*endopenapi-operation\s*%}')
openapi_link = re.compile(r'\[OpenAPI[^\]]*\]\(https://gitbook-x-prod-openapi[^\)]+\)')

rapidoc_script = '<script type="module" src="https://unpkg.com/rapidoc/dist/rapidoc-min.js"></script>'

for root, _, files in os.walk(build_dir):
    for file in files:
        if file.endswith('.md'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if '{% openapi-operation' in content:
                # Need to inject the script once if there are openapi blocks
                # We'll put it at the very top of the markdown file
                content = rapidoc_script + '\n\n' + content
                
                # Replace the start block with RapiDoc component
                # We use the raw GitHub URL to guarantee it resolves
                spec_url = "https://raw.githubusercontent.com/rssebambulidde/samabrainsai-docs/main/en/.gitbook/assets/openapi.json"
                
                def replace_start(match):
                    path = match.group(1)
                    method = match.group(2)
                    return f'<rapi-doc spec-url="{spec_url}" match-paths="{path}" match-type="exact" render-style="view" show-header="false" theme="dark" primary-color="#4CAF50"></rapi-doc>'
                
                content = openapi_start.sub(replace_start, content)
                content = openapi_end.sub('', content)
                content = openapi_link.sub('', content)
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)

print("Markdown conversion complete! GitBook syntax has been replaced with RapiDoc components.")
print("You can now build the site from the 'build-en' directory using: npx honkit build build-en")
