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

hint_start = re.compile(r'{%\s*hint\s+style="([^"]+)"\s*%}')
hint_end = re.compile(r'{%\s*endhint\s*%}')

tabs_start = re.compile(r'{%\s*tabs\s*%}')
tabs_end = re.compile(r'{%\s*endtabs\s*%}')
tab_start = re.compile(r'{%\s*tab\s+title="([^"]+)"\s*%}')
tab_end = re.compile(r'{%\s*endtab\s*%}')

content_ref = re.compile(r'{%\s*content-ref\s+url="([^"]+)"\s*%}')
content_ref_end = re.compile(r'{%\s*endcontent-ref\s*%}')

rapidoc_script = '<script type="module" src="https://unpkg.com/rapidoc/dist/rapidoc-min.js"></script>'

for root, _, files in os.walk(build_dir):
    for file in files:
        if file.endswith('.md'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if '{% openapi-operation' in content:
                content = rapidoc_script + '\n\n' + content
                
                spec_url = "https://raw.githubusercontent.com/rssebambulidde/samabrainsai-docs/main/en/.gitbook/assets/openapi.json"
                
                def replace_openapi(match):
                    path = match.group(1)
                    return f'<rapi-doc spec-url="{spec_url}" match-paths="{path}" match-type="exact" render-style="view" show-header="false" theme="dark" primary-color="#4CAF50"></rapi-doc>'
                
                content = openapi_start.sub(replace_openapi, content)
                content = openapi_end.sub('', content)
                content = openapi_link.sub('', content)
            
            # Replace hints
            def replace_hint(match):
                style = match.group(1).upper()
                return f'> **{style}:** '
            content = hint_start.sub(replace_hint, content)
            content = hint_end.sub('', content)
            
            # Replace tabs
            content = tabs_start.sub('', content)
            content = tabs_end.sub('', content)
            content = tab_start.sub(r'**\1:**\n', content)
            content = tab_end.sub('\n', content)
            
            # Replace content refs
            content = content_ref.sub(r'[Reference](\1)', content)
            content = content_ref_end.sub('', content)
                
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

print("Markdown conversion complete! GitBook syntax has been replaced with generic alternatives.")
print("You can now build the site from the 'build-en' directory using: npx honkit build build-en")
