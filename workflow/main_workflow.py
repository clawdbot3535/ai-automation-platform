"""
Figma → Code Workflow - Main Orchestrator
Orchestriert den gesamten Workflow zwischen Claude Artefakt und Design-Quellen
"""

import logging
from typing import Dict, Optional, Any
from pathlib import Path

from .structure_parser import StructureParser
from .design_extractor import DesignExtractor  
from .code_generator import CodeGenerator

class FigmaToCodeWorkflow:
    """Main workflow orchestrator for Figma → Code conversion"""
    
    def __init__(self, config: Optional[Dict] = None):
        self.logger = logging.getLogger(__name__)
        self.config = config or {}
        
        # Initialize components
        self.structure_parser = StructureParser()
        self.design_extractor = DesignExtractor()
        self.code_generator = CodeGenerator()
        
        self.logger.info("FigmaToCodeWorkflow initialized")
    
    def run_workflow(self, 
                    artefact_content: str,
                    design_source: Optional[str] = None,
                    design_type: str = "prompt",
                    ui_framework: str = "vercel") -> Dict[str, Any]:
        """
        Main workflow execution
        
        Args:
            artefact_content: Claude artefact with structure only
            design_source: Figma URL or prompt description  
            design_type: "figma" or "prompt"
            ui_framework: UI framework style (vercel, nextjs, shadcn, etc.)
            
        Returns:
            Dictionary with workflow results
        """
        self.logger.info("Starting Figma → Code workflow")
        
        try:
            # STEP 1: Parse Structure (Claude Artefakt)
            self.logger.info("Step 1: Parsing structure from Claude Artefact")
            structure = self.structure_parser.parse(artefact_content)
            
            # STEP 2: Extract Design (Figma or Prompt)
            self.logger.info(f"Step 2: Extracting design from {design_type}")
            design = self.design_extractor.extract(
                design_source=design_source,
                design_type=design_type,
                ui_framework=ui_framework,
                structure_context=structure
            )
            
            # STEP 3: Generate Code
            self.logger.info("Step 3: Generating code")
            result = self.code_generator.generate(
                structure=structure,
                design=design,
                config=self.config
            )
            
            self.logger.info("Workflow completed successfully")
            return {
                "success": True,
                "structure": structure,
                "design": design,
                "result": result,
                "workflow_time": "calculated_time"
            }
            
        except Exception as e:
            self.logger.error(f"Workflow failed: {e}")
            return {
                "success": False,
                "error": str(e),
                "workflow_time": "failed"
            }
    
    def validate_inputs(self, artefact_content: str, design_source: Optional[str], design_type: str) -> bool:
        """Validates workflow inputs"""
        if not artefact_content:
            self.logger.error("No artefact content provided")
            return False
            
        if design_type == "figma" and not design_source:
            self.logger.error("Figma URL required for figma design type")
            return False
            
        if design_type == "prompt" and not design_source:
            self.logger.error("Prompt description required for prompt design type")
            return False
            
        return True

# Export main orchestrator
__all__ = ["FigmaToCodeWorkflow"]
