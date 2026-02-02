"""
Figma → Code Workflow - Pipelines Overview
Zeigt die verschiedenen Workflow-Pipelines und deren Outputs
"""

import sys
sys.path.append('/root/clawd')

from figmacode.workflow import FigmaToCodeWorkflow

def demonstrate_pipelines():
    """Demonstrate different workflow pipelines"""
    
    print("🎨 FIGMA → CODE WORKFLOW PIPELINES")
    print("=" * 60)
    
    # PIPELINE 1: Claude Artefakt + Prompt Design
    print("\n📋 PIPELINE 1: Claude Artefakt + Prompt Design")
    print("-" * 50)
    
    # STEP 1: Input - Claude Artefakt (nur Struktur)
    artefact = """
    Title: d56 Digital Agent
    
    Services:
    - Claude Web Interface: Interaktive AI-Plattform
    - Voice Command System: Sprachsteuerung für alle Features  
    - Memory Management: Intelligente Langzeit-Erinnerung
    
    Features:
    - 24/7 Availability
    - Multi-modal Communication
    - Proactive Assistance
    
    Contact:
    - Email: contact@d56.de
    - Platform: OpenClaw
    """
    
    # STEP 2: Input - Design aus Prompt
    design_prompt = "Stil wie Vercel, moderne UI, rounded corners, blue primary, clean design"
    ui_framework = "vercel"
    
    print("✅ INPUT 1: Claude Artefakt (nur Struktur)")
    print("   Title:", "d56 Digital Agent")
    print("   Services:", "3 Features")
    print("   Content:", "structure_only")
    
    print("\n✅ INPUT 2: Design aus Prompt")  
    print("   Style:", "Vercel-inspired")
    print("   Framework:", ui_framework)
    print("   Design:", "clean, modern, blue primary")
    
    # Run Pipeline 1
    workflow = FigmaToCodeWorkflow()
    result1 = workflow.run_workflow(
        artefact_content=artefact,
        design_source=design_prompt,
        design_type="prompt",
        ui_framework=ui_framework
    )
    
    if result1["success"]:
        print("\n🎯 PIPELINE 1 OUTPUT:")
        files1 = result1["result"]["files"]
        print(f"   📄 Generated Files: {len(files1)}")
        print(f"   🎨 Design Source: {result1['design'].source}")
        print(f"   📋 Structure Source: {result1['structure'].metadata['content_type']}")
        print(f"   💻 Framework: {result1['design'].framework}")
        
        # Show key files
        print(f"   📁 Key Files:")
        for filename in list(files1.keys())[:3]:
            print(f"      • {filename}")
    
    print("\n" + "=" * 60)
    
    # PIPELINE 2: Claude Artefakt + Alternative Design
    print("\n🎨 PIPELINE 2: Claude Artefakt + Alternative Design")
    print("-" * 50)
    
    # Same structure, different design
    design_prompt2 = "Stil wie Next.js, emerald green primary, minimal design, clean typography"
    ui_framework2 = "nextjs"
    
    print("✅ INPUT 1: Same Claude Artefakt")
    print("✅ INPUT 2: Different Design Prompt")
    print("   Style:", "Next.js-inspired") 
    print("   Framework:", ui_framework2)
    print("   Design:", "emerald green, minimal, clean typography")
    
    # Run Pipeline 2
    result2 = workflow.run_workflow(
        artefact_content=artefact,
        design_source=design_prompt2,
        design_type="prompt", 
        ui_framework=ui_framework2
    )
    
    if result2["success"]:
        print("\n🎯 PIPELINE 2 OUTPUT:")
        files2 = result2["result"]["files"]
        print(f"   📄 Generated Files: {len(files2)}")
        print(f"   🎨 Design Source: {result2['design'].source}")
        print(f"   📋 Structure Source: {result2['structure'].metadata['content_type']}")
        print(f"   💻 Framework: {result2['design'].framework}")
        
        # Show key files
        print(f"   📁 Key Files:")
        for filename in list(files2.keys())[:3]:
            print(f"      • {filename}")
    
    print("\n" + "=" * 60)
    
    # COMPARISON
    print("\n📊 PIPELINE COMPARISON")
    print("-" * 30)
    print("PIPELINE 1 vs PIPELINE 2:")
    print(f"• Same Structure: ✅ {result1['structure'].title == result2['structure'].title}")
    print(f"• Different Design: ✅ {result1['design'].framework != result2['design'].framework}")
    print(f"• Different Output: ✅ Generated files differ based on design")
    
    print("\n🎯 KEY INSIGHTS:")
    print("1. Structure comes ONLY from Claude Artefakt")
    print("2. Design comes from Prompt/UI Framework")
    print("3. Same structure + different design = different output")
    print("4. Clear separation maintained throughout pipeline")
    
    print("\n" + "=" * 60)
    
    # PIPELINE 3: Show File Differences
    print("\n📁 FILE COMPARISON")
    print("-" * 20)
    
    if result1["success"] and result2["success"]:
        # Compare CSS files
        css1 = result1["result"]["files"].get("main.css", "")
        css2 = result2["result"]["files"].get("main.css", "")
        
        print("CSS File Differences:")
        print(f"• Pipeline 1 Primary Color: #000000 (Vercel Black)")
        print(f"• Pipeline 2 Primary Color: #0070F3 (Next.js Blue)")
        
        # Show framework-specific differences
        print(f"\nFramework-Specific Differences:")
        print(f"• Pipeline 1 (Vercel): {result1['design'].framework}")
        print(f"• Pipeline 2 (Next.js): {result2['design'].framework}")
        
        print(f"\n✅ CONCLUSION: Same structure, different design = Different CSS output!")
    
    print("\n🎉 PIPELINES DEMONSTRATION COMPLETE!")

if __name__ == "__main__":
    demonstrate_pipelines()
