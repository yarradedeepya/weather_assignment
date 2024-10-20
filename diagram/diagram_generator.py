# diagram/diagram_generator.py
def generate_diagram(json_data: dict) -> str:
    """Generate Mermaid JS tree view from JSON data."""
    lines = ["graph LR;"]  # Change TD to LR for vertical layout
    
    def parse_node(key, value, parent):
        node_id = f"{parent}_{key}".replace(".", "")
        lines.append(f"{parent} --> {node_id}[{key}]")
        if isinstance(value, dict):
            for k, v in value.items():
                parse_node(k, v, node_id)
        elif isinstance(value, list):
            for idx, item in enumerate(value):
                parse_node(str(idx), item, node_id)
        else:
            value_id = f"{node_id}_value".replace(".", "")
            lines.append(f"{node_id} --> {value_id}[{value}]")

    # Start parsing JSON response
    parse_node('root', json_data, 'weather_data')
    
    return '\n'.join(lines)

def create_html_diagram(json_data: dict, output_file="output.html"):
    """Creates an HTML file containing a Mermaid diagram."""
    mermaid_code = generate_diagram(json_data)
    with open(output_file, 'w') as f:
        f.write(f"""
        <html>
        <head>
            <script type="module">
                import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
                mermaid.initialize({{startOnLoad: true}});
            </script>
        </head>
        <body>
            <div class="mermaid">
                {mermaid_code}
            </div>
        </body>
        </html>
        """)
    print(f"Diagram saved as {output_file}")
