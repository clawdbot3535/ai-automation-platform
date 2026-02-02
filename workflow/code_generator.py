"""
Figma → Code Workflow - Code Generator
Generiert Code basierend auf Struktur (Claude Artefakt) und Design (Figma/Prompt)
"""

import logging
from typing import Dict, List, Optional, Any
from pathlib import Path

from ..workflow.structure_parser import PageStructure
from ..workflow.design_extractor import DesignAssets

class CodeGenerator:
    """Generates code from structure and design"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def generate(self, 
                structure: PageStructure,
                design: DesignAssets,
                config: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Generate complete website code
        
        Args:
            structure: Parsed structure from Claude Artefact
            design: Extracted design from Figma or Prompt
            config: Additional configuration
            
        Returns:
            Dictionary with generated files and metadata
        """
        self.logger.info("Starting code generation")
        
        if not config:
            config = {}
        
        # Configuration
        framework = config.get("framework", "react")
        language = config.get("language", "typescript")
        styling = config.get("styling", "tailwindcss")
        
        try:
            # Generate main components
            files = {}
            
            # Generate main page
            files["index.html"] = self._generate_html(structure, design)
            files["main.css"] = self._generate_css(design)
            files["app.js"] = self._generate_javascript(structure, design)
            
            # Generate configuration files
            if framework == "react":
                files["package.json"] = self._generate_package_json(design)
                files["tailwind.config.js"] = self._generate_tailwind_config(design)
            
            # Generate component files
            component_files = self._generate_components(structure, design)
            files.update(component_files)
            
            # Generate documentation
            files["README.md"] = self._generate_readme(structure, design)
            
            self.logger.info(f"Generated {len(files)} files")
            
            return {
                "success": True,
                "files": files,
                "metadata": {
                    "structure_title": structure.title,
                    "design_source": design.source,
                    "framework": framework,
                    "styling": styling,
                    "generated_at": "current_timestamp"
                }
            }
            
        except Exception as e:
            self.logger.error(f"Code generation failed: {e}")
            return {
                "success": False,
                "error": str(e),
                "files": {}
            }
    
    def _generate_html(self, structure: PageStructure, design: DesignAssets) -> str:
        """Generate HTML structure"""
        
        # Convert design colors to CSS
        color_css = self._colors_to_css(design.colors)
        typography_css = self._typography_to_css(design.typography)
        layout_css = self._layout_to_css(design.layout)
        
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{structure.title}</title>
    <link rel="stylesheet" href="main.css">
</head>
<body>
    {self._generate_navigation(structure.navigation, design)}
    
    <main>
        {self._generate_sections(structure.sections, design)}
    </main>
    
    {self._generate_footer(structure.footer, design)}
    
    <script src="app.js"></script>
</body>
</html>"""
        
        return html
    
    def _generate_css(self, design: DesignAssets) -> str:
        """Generate CSS styles from design"""
        
        css = f"""/* Generated CSS from Design Assets */
/* Source: {design.source} | Framework: {design.framework} */

:root {{
{self._css_variables(design)}
}}

/* Reset and Base Styles */
* {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}}

body {{
    font-family: {design.typography.get('primary_font', 'Inter')};
    line-height: 1.6;
    color: {design.colors.get('text', '#000000')};
    background-color: {design.colors.get('background', '#FFFFFF')};
}}

/* Typography */
{self._generate_typography_styles(design.typography)}

/* Components */
{self._generate_component_styles(design.components)}

/* Layout */
{self._generate_layout_styles(design.layout)}

/* Spacing */
{self._generate_spacing_styles(design.spacing)}

/* Effects */
{self._generate_effect_styles(design.effects)}
"""
        
        return css
    
    def _generate_javascript(self, structure: PageStructure, design: DesignAssets) -> str:
        """Generate JavaScript functionality"""
        
        js = f"""// Generated JavaScript for {structure.title}
// Design Source: {design.source}

// Navigation functionality
function initNavigation() {{
    // Add navigation logic here
    console.log('Navigation initialized for {structure.title}');
}}

// Smooth scrolling
function initSmoothScrolling() {{
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {{
        anchor.addEventListener('click', function (e) {{
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({{
                behavior: 'smooth'
            }});
        }});
    }});
}}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {{
    initNavigation();
    initSmoothScrolling();
    console.log('{structure.title} initialized');
}});
"""
        
        return js
    
    def _generate_components(self, structure: PageStructure, design: DesignAssets) -> Dict[str, str]:
        """Generate component files"""
        components = {}
        
        # Generate component for each section
        for i, section in enumerate(structure.sections):
            component_name = f"component_{i+1}_{section.name.lower().replace(' ', '_')}"
            components[f"components/{component_name}.html"] = self._generate_section_component(section, design)
        
        return components
    
    def _generate_section_component(self, section, design: DesignAssets) -> str:
        """Generate HTML for a section component"""
        
        # Get component styling
        card_style = design.components.get('cards', {}).get('default', {})
        
        component = f"""<!-- {section.name} Component -->
<section class="section" id="{section.name.lower().replace(' ', '-')}">
    <div class="container">
        <div class="card" style="
            background: {card_style.get('background', '#FFFFFF')};
            padding: {card_style.get('padding', '24px')};
            border-radius: {card_style.get('border_radius', '8px')};
            {self._border_style(card_style)}
        ">
            <h2 class="section-title">{section.name}</h2>
            <div class="section-content">
                {self._format_content(section.content)}
            </div>
        </div>
    </div>
</section>"""
        
        return component
    
    def _generate_package_json(self, design: DesignAssets) -> str:
        """Generate package.json for React projects"""
        
        package_json = {
            "name": f"{design.source}-website",
            "version": "1.0.0",
            "description": f"Generated website from {design.source}",
            "scripts": {
                "dev": "next dev",
                "build": "next build",
                "start": "next start",
                "lint": "next lint"
            },
            "dependencies": {
                "next": "^14.0.0",
                "react": "^18.0.0",
                "react-dom": "^18.0.0",
                "tailwindcss": "^3.0.0",
                "autoprefixer": "^10.0.0",
                "postcss": "^8.0.0"
            },
            "devDependencies": {
                "@types/react": "^18.0.0",
                "@types/node": "^20.0.0",
                "typescript": "^5.0.0"
            }
        }
        
        import json
        return json.dumps(package_json, indent=2)
    
    def _generate_tailwind_config(self, design: DesignAssets) -> str:
        """Generate TailwindCSS configuration"""
        
        config = f"""// Generated Tailwind Config
// Based on {design.source} design system

module.exports = {{
  content: [
    './pages/**/*.{{js,ts,jsx,tsx,mdx}}',
    './components/**/*.{{js,ts,jsx,tsx,mdx}}',
    './app/**/*.{{js,ts,jsx,tsx,mdx}}',
  ],
  theme: {{
    extend: {{
      colors: {{
        primary: {{
          DEFAULT: '{design.colors.get('primary', '#000000')}',
        }},
        secondary: {{
          DEFAULT: '{design.colors.get('secondary', '#666666')}',
        }},
        accent: '{design.colors.get('accent', '#0070F3')}',
      }},
      fontFamily: {{
        sans: ['{design.typography.get('primary_font', 'Inter')}'],
        mono: ['{design.typography.get('code_font', 'JetBrains Mono')}'],
      }},
      spacing: {{
{self._spacing_scale_to_css(design.spacing)}
      }},
    }},
  }},
  plugins: [],
}}"""
        
        return config
    
    def _generate_readme(self, structure: PageStructure, design: DesignAssets) -> str:
        """Generate README.md"""
        
        readme = f"""# {structure.title}

Generated website from {design.source} design system.

## Description

{structure.description}

## Design System

- **Source:** {design.source}
- **Framework:** {design.framework or 'Custom'}
- **Generated:** {design.source} → Website Code

## Structure

This website includes:

"""
        
        for section in structure.sections:
            readme += f"- {section.name}\n"
        
        readme += f"""
## Features

- Responsive design
- Modern CSS with {design.source} styling
- Accessible components
- SEO optimized

## Usage

1. Open `index.html` in a web browser
2. Customize colors and content as needed
3. Deploy to your preferred hosting platform

## Customization

### Colors
Edit the CSS variables in `main.css`:

```css
:root {{
  --primary-color: {design.colors.get('primary', '#000000')};
  --secondary-color: {design.colors.get('secondary', '#666666')};
  --background-color: {design.colors.get('background', '#FFFFFF')};
}}
```

### Content
Edit the HTML structure in `index.html` to modify content.

### Styling
Modify `main.css` to adjust the visual design.
"""
        
        return readme
    
    # Helper methods for CSS generation
    def _colors_to_css(self, colors: Dict[str, str]) -> str:
        """Convert color palette to CSS"""
        css_lines = []
        for name, color in colors.items():
            css_lines.append(f"  --color-{name}: {color};")
        return "\n".join(css_lines)
    
    def _typography_to_css(self, typography: Dict[str, Any]) -> str:
        """Convert typography to CSS"""
        css = f"""
/* Typography */
h1, h2, h3, h4, h5, h6 {{
  font-weight: 600;
  line-height: 1.2;
  margin-bottom: 1rem;
}}

h1 {{ font-size: {typography.get('sizes', {}).get('h1', {}).get('size', '3rem')}; }}
h2 {{ font-size: {typography.get('sizes', {}).get('h2', {}).get('size', '2.5rem')}; }}
h3 {{ font-size: {typography.get('sizes', {}).get('h3', {}).get('size', '2rem')}; }}

body {{
  font-size: {typography.get('sizes', {}).get('body', {}).get('size', '1rem')};
  font-weight: {typography.get('sizes', {}).get('body', {}).get('weight', '400')};
}}
"""
        return css
    
    def _layout_to_css(self, layout: Dict[str, Any]) -> str:
        """Convert layout to CSS"""
        container = layout.get('container', {})
        grid = layout.get('grid', {})
        
        css = f"""
/* Layout */
.container {{
  max-width: {container.get('max_width', '1200px')};
  margin: 0 auto;
  padding: 0 {container.get('padding', '24px')};
}}

.grid {{
  display: grid;
  gap: {grid.get('gap', '24px')};
}}

.sections {{
  padding: {layout.get('sections', {}).get('padding', '80px 0')};
}}
"""
        return css
    
    def _generate_typography_styles(self, typography: Dict[str, Any]) -> str:
        """Generate typography CSS styles"""
        sizes = typography.get('sizes', {})
        
        css = ""
        for tag, props in sizes.items():
            if tag == 'h1':
                css += f"h1 {{ font-size: {props.get('size', '3rem')}; font-weight: {props.get('weight', '700')}; }}\n"
            elif tag == 'h2':
                css += f"h2 {{ font-size: {props.get('size', '2.25rem')}; font-weight: {props.get('weight', '600')}; }}\n"
            elif tag == 'h3':
                css += f"h3 {{ font-size: {props.get('size', '1.875rem')}; font-weight: {props.get('weight', '600')}; }}\n"
            elif tag == 'body':
                css += f"body {{ font-size: {props.get('size', '1rem')}; font-weight: {props.get('weight', '400')}; }}\n"
            elif tag == 'small':
                css += f".text-small {{ font-size: {props.get('size', '0.875rem')}; font-weight: {props.get('weight', '400')}; }}\n"
        
        return css
    
    def _generate_component_styles(self, components: Dict[str, Any]) -> str:
        """Generate component CSS styles"""
        css = ""
        
        # Buttons
        buttons = components.get('buttons', {})
        for button_type, styles in buttons.items():
            css += f".btn-{button_type} {{\n"
            for prop, value in styles.items():
                if prop == 'border_radius':
                    css += f"  border-radius: {value};\n"
                elif prop == 'padding':
                    css += f"  padding: {value};\n"
                else:
                    css += f"  {prop.replace('_', '-')}: {value};\n"
            css += "}\n\n"
        
        # Cards
        cards = components.get('cards', {})
        for card_type, styles in cards.items():
            css += f".card-{card_type} {{\n"
            for prop, value in styles.items():
                css += f"  {prop.replace('_', '-')}: {value};\n"
            css += "}\n\n"
        
        return css
    
    def _generate_layout_styles(self, layout: Dict[str, Any]) -> str:
        """Generate layout CSS styles"""
        container = layout.get('container', {})
        grid = layout.get('grid', {})
        
        css = f""".container {{
  max-width: {container.get('max_width', '1200px')};
  margin: 0 auto;
  padding: 0 {container.get('padding', '24px')};
}}

.grid {{
  display: grid;
  gap: {grid.get('gap', '24px')};
}}

.section {{
  padding: {layout.get('sections', {}).get('padding', '80px 0')};
}}
"""
        return css
    
    def _generate_spacing_styles(self, spacing: Dict[str, Any]) -> str:
        """Generate spacing CSS styles"""
        scale = spacing.get('scale', {})
        
        css = "/* Spacing Utilities */\n"
        for name, value in scale.items():
            css += f".m-{name} {{ margin: {value}; }}\n"
            css += f".p-{name} {{ padding: {value}; }}\n"
            css += f".mx-{name} {{ margin-left: {value}; margin-right: {value}; }}\n"
            css += f".my-{name} {{ margin-top: {value}; margin-bottom: {value}; }}\n"
            css += f".px-{name} {{ padding-left: {value}; padding-right: {value}; }}\n"
            css += f".py-{name} {{ padding-top: {value}; padding-bottom: {value}; }}\n\n"
        
        return css
    
    def _generate_effect_styles(self, effects: Dict[str, Any]) -> str:
        """Generate effects CSS styles"""
        css = "/* Effects */\n"
        
        # Shadows
        shadows = effects.get('shadows', {})
        for name, value in shadows.items():
            css += f".shadow-{name} {{ box-shadow: {value}; }}\n"
        
        # Transitions
        transitions = effects.get('transitions', {})
        for name, value in transitions.items():
            css += f".transition-{name} {{ transition: {value}; }}\n"
        
        return css
    
    def _css_variables(self, design: DesignAssets) -> str:
        """Generate CSS custom properties"""
        variables = []
        
        # Colors
        for name, color in design.colors.items():
            variables.append(f"  --color-{name}: {color};")
        
        # Typography
        variables.append(f"  --font-primary: {design.typography.get('primary_font', 'Inter')};")
        variables.append(f"  --font-code: {design.typography.get('code_font', 'JetBrains Mono')};")
        
        return "\n".join(variables)
    
    def _spacing_scale_to_css(self, spacing: Dict[str, Any]) -> str:
        """Convert spacing scale to CSS"""
        scale = spacing.get('scale', {})
        css_lines = []
        
        for name, value in scale.items():
            css_lines.append(f"        '{name}': '{value}',")
        
        return "\n".join(css_lines)
    
    def _generate_navigation(self, navigation, design: DesignAssets) -> str:
        """Generate navigation HTML"""
        if not navigation:
            return ""
        
        return f"""
    <nav class="navigation">
        <div class="container">
            <div class="nav-content">
                <h1 class="nav-title">{navigation.name}</h1>
                <div class="nav-links">
                    {self._format_content(navigation.content)}
                </div>
            </div>
        </div>
    </nav>"""
    
    def _generate_sections(self, sections, design: DesignAssets) -> str:
        """Generate sections HTML"""
        html_parts = []
        
        for section in sections:
            card_style = design.components.get('cards', {}).get('default', {})
            html_parts.append(f"""
        <section class="section" id="{section.name.lower().replace(' ', '-')}">
            <div class="container">
                <div class="card" style="
                    background: {card_style.get('background', '#FFFFFF')};
                    padding: {card_style.get('padding', '24px')};
                    border-radius: {card_style.get('border_radius', '8px')};
                ">
                    <h2 class="section-title">{section.name}</h2>
                    <div class="section-content">
                        {self._format_content(section.content)}
                    </div>
                </div>
            </div>
        </section>""")
        
        return "\n".join(html_parts)
    
    def _generate_footer(self, footer, design: DesignAssets) -> str:
        """Generate footer HTML"""
        if not footer:
            return ""
        
        return f"""
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                {self._format_content(footer.content)}
            </div>
        </div>
    </footer>"""
    
    def _format_content(self, content: str) -> str:
        """Format content text to HTML"""
        # Simple formatting - convert line breaks to paragraphs
        lines = content.split('\n')
        formatted_lines = []
        
        for line in lines:
            line = line.strip()
            if line:
                if line.startswith('- ') or line.startswith('* '):
                    formatted_lines.append(f"<li>{line[2:]}</li>")
                elif len(line) > 100:
                    formatted_lines.append(f"<p>{line}</p>")
                else:
                    formatted_lines.append(f"<p>{line}</p>")
        
        return "\n".join(formatted_lines)
    
    def _border_style(self, card_style: Dict[str, str]) -> str:
        """Extract border style from card properties"""
        border = card_style.get('border', '')
        if border:
            return f"border: {border};"
        return ""

# Export classes
__all__ = ["CodeGenerator"]
