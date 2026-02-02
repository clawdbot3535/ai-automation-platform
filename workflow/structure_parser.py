"""
Figma → Code Workflow - Structure Parser
Extrahiert NUR Struktur aus Claude Artefakt (kein Design!)
"""

import re
from typing import Dict, List, Optional, Any
from dataclasses import dataclass

@dataclass
class Component:
    """Component structure without styling"""
    name: str
    content: str
    children: List['Component'] = None
    properties: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.children is None:
            self.children = []
        if self.properties is None:
            self.properties = {}

@dataclass
class PageStructure:
    """Complete page structure from Claude Artefact"""
    title: str
    description: str
    sections: List[Component]
    navigation: Optional[Component] = None
    footer: Optional[Component] = None
    metadata: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}

class StructureParser:
    """Parses Claude Artefact and extracts ONLY structure"""
    
    def __init__(self):
        self.logger = None  # Will be set by main workflow
    
    def parse(self, artefact_content: str) -> PageStructure:
        """
        Parse Claude Artefact and extract structure
        
        Args:
            artefact_content: Raw Claude artefact content
            
        Returns:
            PageStructure with ONLY structural elements
        """
        if not isinstance(artefact_content, str):
            raise ValueError("Artefact content must be string")
        
        # Clean content
        cleaned_content = self._clean_content(artefact_content)
        
        # Extract basic metadata
        title = self._extract_title(cleaned_content)
        description = self._extract_description(cleaned_content)
        
        # Extract sections
        sections = self._extract_sections(cleaned_content)
        
        # Extract navigation and footer
        navigation = self._extract_navigation(cleaned_content)
        footer = self._extract_footer(cleaned_content)
        
        return PageStructure(
            title=title,
            description=description,
            sections=sections,
            navigation=navigation,
            footer=footer,
            metadata={
                "source": "claude_artefact",
                "content_type": "structure_only",
                "extracted_at": "current_timestamp"
            }
        )
    
    def _clean_content(self, content: str) -> str:
        """Clean and normalize artefact content"""
        # Remove HTML tags if any
        content = re.sub(r'<[^>]+>', '', content)
        
        # Normalize whitespace
        content = re.sub(r'\n\s*\n', '\n\n', content)
        
        # Remove excessive whitespace
        content = re.sub(r'[ \t]+', ' ', content)
        
        return content.strip()
    
    def _extract_title(self, content: str) -> str:
        """Extract page title"""
        # Look for title patterns
        title_patterns = [
            r'Title:\s*(.+?)(?:\n|$)',
            r'#\s*(.+?)(?:\n|$)',
            r'Name:\s*(.+?)(?:\n|$)',
            r'Site Name:\s*(.+?)(?:\n|$)'
        ]
        
        for pattern in title_patterns:
            match = re.search(pattern, content, re.IGNORECASE | re.MULTILINE)
            if match:
                return match.group(1).strip()
        
        # Fallback: use first non-empty line
        lines = [line.strip() for line in content.split('\n') if line.strip()]
        return lines[0] if lines else "Untitled Page"
    
    def _extract_description(self, content: str) -> str:
        """Extract page description"""
        description_patterns = [
            r'Description:\s*(.+?)(?:\n\n|\n(?=[A-Z])|$)',
            r'Summary:\s*(.+?)(?:\n\n|\n(?=[A-Z])|$)',
            r'About:\s*(.+?)(?:\n\n|\n(?=[A-Z])|$)'
        ]
        
        for pattern in description_patterns:
            match = re.search(pattern, content, re.IGNORECASE | re.DOTALL)
            if match:
                return match.group(1).strip()
        
        return ""
    
    def _extract_sections(self, content: str) -> List[Component]:
        """Extract main sections from content"""
        sections = []
        
        # Look for section patterns
        section_patterns = [
            r'(?:^|\n)(?:Section|Service|Feature|About|Contact)\s*\n(.*?)(?=\n(?:Section|Service|Feature|About|Contact|\n[A-Z]|$))',
            r'(?:^|\n)##\s*(.+?)\n(.*?)(?=\n##|\n(?=[A-Z])|$)'
        ]
        
        for pattern in section_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE | re.DOTALL | re.MULTILINE)
            for title, content_block in matches:
                component = Component(
                    name=title.strip(),
                    content=content_block.strip(),
                    properties={
                        "type": "section",
                        "extracted_from": "claude_artefact"
                    }
                )
                sections.append(component)
        
        # If no sections found, treat entire content as single section
        if not sections:
            sections = [
                Component(
                    name="Main Content",
                    content=content,
                    properties={
                        "type": "main_content",
                        "extracted_from": "claude_artefact"
                    }
                )
            ]
        
        return sections
    
    def _extract_navigation(self, content: str) -> Optional[Component]:
        """Extract navigation structure"""
        nav_patterns = [
            r'(?:^|\n)Navigation\s*\n(.*?)(?:\n\n|\n[A-Z]|$)',
            r'(?:^|\n)Menu\s*\n(.*?)(?:\n\n|\n[A-Z]|$)'
        ]
        
        for pattern in nav_patterns:
            match = re.search(pattern, content, re.IGNORECASE | re.DOTALL)
            if match:
                return Component(
                    name="Navigation",
                    content=match.group(1).strip(),
                    properties={
                        "type": "navigation",
                        "extracted_from": "claude_artefact"
                    }
                )
        
        return None
    
    def _extract_footer(self, content: str) -> Optional[Component]:
        """Extract footer structure"""
        footer_patterns = [
            r'(?:^|\n)Footer\s*\n(.*?)(?:\n\n|\n[A-Z]|$)',
            r'(?:^|\n)Contact\s*\n(.*?)(?:\n\n|\n[A-Z]|$)'
        ]
        
        for pattern in footer_patterns:
            match = re.search(pattern, content, re.IGNORECASE | re.DOTALL)
            if match:
                return Component(
                    name="Footer",
                    content=match.group(1).strip(),
                    properties={
                        "type": "footer",
                        "extracted_from": "claude_artefact"
                    }
                )
        
        return None
    
    def get_structure_summary(self, structure: PageStructure) -> Dict[str, Any]:
        """Get summary of extracted structure"""
        return {
            "title": structure.title,
            "has_description": bool(structure.description),
            "section_count": len(structure.sections),
            "has_navigation": structure.navigation is not None,
            "has_footer": structure.footer is not None,
            "metadata": structure.metadata,
            "sections": [
                {
                    "name": section.name,
                    "content_length": len(section.content),
                    "properties": section.properties
                }
                for section in structure.sections
            ]
        }

# Export classes
__all__ = ["StructureParser", "PageStructure", "Component"]
