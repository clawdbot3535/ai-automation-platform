"""
Figma → Code Workflow - Config Module
Initialisiert Konfigurationssystem für Workflow
"""

from .ui_frameworks import UI_FRAMEWORKS, get_available_frameworks, get_framework_config

class Config:
    """Configuration management for Figma → Code workflow"""
    
    def __init__(self):
        self.ui_frameworks = UI_FRAMEWORKS
    
    def get_default_settings(self) -> dict:
        """Get default workflow settings"""
        return {
            "framework": "react",
            "language": "typescript", 
            "styling": "tailwindcss",
            "ui_framework": "vercel",
            "design_source": "prompt",  # or "figma"
            "output_format": "html",     # or "react", "vue"
            "include_components": True,
            "generate_docs": True,
            "validate_output": True
        }
    
    def get_available_frameworks(self) -> list:
        """Get list of available UI frameworks"""
        return get_available_frameworks()
    
    def get_ui_framework_config(self, framework: str) -> dict:
        """Get configuration for specific UI framework"""
        return get_framework_config(framework)

# Create global config instance
config = Config()

# Export
__all__ = ["config", "Config"]
