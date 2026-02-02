"""
Figma → Code Workflow - Simple Example
Demonstriert die klare Trennung zwischen Struktur und Design
"""

import sys
sys.path.append('/root/clawd')

from figmacode.workflow import FigmaToCodeWorkflow

def run_example():
    """Example of clear structure/design separation"""
    
    # STEP 1: Claude Artefakt = NUR STRUKTUR
    artefact_content = """
    Title: d56 Büro für Gestaltung
    
    Services:
    - Web Development: Moderne Websites mit React/Next.js
    - UI/UX Design: Pixelgenaue Designs für alle Devices
    - Branding: Vollständige Markenidentität
    
    Use Cases:
    - 65% schnellere Ladezeiten
    - Mobile-First Design
    - SEO-optimierte Websites
    
    Contact:
    - Email: hello@d56.de
    - Website: https://d56.de
    """
    
    # STEP 2: Design aus PROMPT (oder Figma)
    design_prompt = "Stil wie Vercel, clean design, rounded corners, blue primary color"
    
    # STEP 3: UI Framework
    ui_framework = "vercel"
    
    # Initialize workflow
    workflow = FigmaToCodeWorkflow()
    
    # Run workflow
    result = workflow.run_workflow(
        artefact_content=artefact_content,
        design_source=design_prompt,
        design_type="prompt",
        ui_framework=ui_framework
    )
    
    if result["success"]:
        print("✅ Workflow erfolgreich!")
        print(f"📄 Generierte Dateien: {len(result['result']['files'])}")
        print(f"🎨 Design Quelle: {result['design'].source}")
        print(f"📋 Struktur Quelle: {result['structure'].metadata['content_type']}")
        
        # Show structure summary
        structure_summary = workflow.structure_parser.get_structure_summary(result["structure"])
        print(f"\n📋 Struktur (nur aus Claude Artefakt):")
        print(f"   Title: {structure_summary['title']}")
        print(f"   Sections: {structure_summary['section_count']}")
        
        # Show design summary  
        design_summary = workflow.design_extractor.get_design_summary(result["design"])
        print(f"\n🎨 Design (aus Prompt):")
        print(f"   Source: {design_summary['source']}")
        print(f"   Framework: {design_summary['framework']}")
        print(f"   Colors: {design_summary['color_count']}")
        
    else:
        print(f"❌ Workflow fehlgeschlagen: {result['error']}")

if __name__ == "__main__":
    run_example()
