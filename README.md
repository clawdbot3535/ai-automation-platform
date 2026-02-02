# 🎨 Figma → Code Workflow - Complete Implementation

## 🎯 **Kernprinzip**

**Claude Artefakt:** Nur **Struktur & Content**
- Services, Use Cases, Text, Layout-Struktur
- Navigation, Sections, Components-Struktur
- **NIE Design-Hints**

**Figma/Prompt:** Komplettes **UI Design**
- Farben, Typography, Spacing
- Button-Styles, Card-Designs, Layout-Details
- Visual Hierarchy, Animations

## 📁 **Projektstruktur**

```
figmacode/
├── README.md                           # 🚀 Projekt-Übersicht
├── FIGMA_TO_CODE_GUIDE.md             # 📋 Implementierungsanleitung
├── FIGMA_TO_CODE_FINAL.md             # ✅ Finale Implementierung
├── PIPELINE_COMPARISON.md             # 📊 Pipeline Demo Ergebnisse
├── examples/
│   └── simple_example.py              # 🧪 Funktionales Beispiel
├── config/
│   ├── __init__.py                    # 📦 Config Module
│   └── ui_frameworks.py              # 🎨 UI-Framework Konfiguration
└── workflow/
    ├── __init__.py                    # 📦 Workflow Module
    ├── main_workflow.py               # 🎯 Haupt-Workflow
    ├── structure_parser.py            # 📋 NUR Struktur aus Claude
    ├── design_extractor.py           # 🎨 Design aus Figma/Prompt
    └── code_generator.py              # 💻 Code-Generation
```

## 🔄 **Workflow-Pipeline**

```
Claude Artefakt (nur Struktur)
           ↓
Figma/Prompt Design
           ↓
Intelligente Kombination
           ↓
Code-Generation
           ↓
Website/Components
```

## 🛠️ **Installation & Usage**

```bash
# Install dependencies
pip install dataclasses typing-extensions

# Run example
python3 examples/simple_example.py

# Run pipeline demo
python3 pipelines_demo.py
```

## 💡 **Beispiel-Usage**

```python
from figmacode.workflow import FigmaToCodeWorkflow

# Claude Artefakt = NUR STRUKTUR
artefact = """
Title: d56 Digital Agent

Services:
- Claude Web Interface: Interaktive AI-Plattform
- Voice Command System: Sprachsteuerung
- Memory Management: Intelligente Langzeit-Erinnerung
"""

# Design aus PROMPT
design_prompt = "Stil wie Vercel, moderne UI, blue primary"
ui_framework = "vercel"

# Workflow ausführen
workflow = FigmaToCodeWorkflow()
result = workflow.run_workflow(
    artefact_content=artefact,
    design_source=design_prompt,
    design_type="prompt",
    ui_framework=ui_framework
)
```

## 🎛️ **UI-Frameworks verfügbar**

- `vercel` - Vercel-inspired Design
- `nextjs` - Next.js default styling  
- `default` - Clean default design

## 📊 **Pipeline Demo**

Das System wurde mit Pipeline-Demo getestet:

```
PIPELINE 1: Vercel Design → Primary Color: #000000 (Black)
PIPELINE 2: Next.js Design → Primary Color: #0070F3 (Blue)

✅ Bestätigt: Gleiche Struktur + Unterschiedliches Design = Anderer Output!
```

## 🚀 **Features**

✅ **Klare Trennung:** Claude = Struktur, Figma/Prompt = Design  
✅ **Modulare Architektur:** Workflow, Parser, Extractor, Generator  
✅ **UI-Framework Support:** Vercel, Next.js, Default  
✅ **Pipeline Demonstration:** Verschiedene Outputs möglich  
✅ **Comprehensive Documentation:** README, Guide, Demo  
✅ **Working Examples:** Funktionale Demos inklusive  

## 🔧 **Erweiterungsmöglichkeiten**

- **Figma API Integration:** Echte Design-Asset-Extraktion
- **React/Vue Templates:** Framework-spezifische Code-Generation
- **Advanced Features:** Animationen, Responsive Design, SEO
- **Additional UI Frameworks:** shadcn/ui, TailwindCSS Custom

## 📄 **Lizenz**

MIT License - Free to use and modify

---

**Das Projekt hat eine saubere Struktur und wir kennen uns aus! 🎯**
