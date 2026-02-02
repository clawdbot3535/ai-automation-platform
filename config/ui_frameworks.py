"""
Figma → Code Workflow - UI Framework Configuration
Definiert Design-Prompts für verschiedene UI-Frameworks
"""

# UI Framework Design Templates
UI_FRAMEWORKS = {
    "vercel": {
        "name": "Vercel-inspired Design",
        "description": "Clean, minimal design inspired by Vercel's aesthetic",
        "colors": {
            "primary": "#000000",
            "secondary": "#666666",
            "background": "#FFFFFF",
            "surface": "#F8F9FA",
            "text": "#000000",
            "text_secondary": "#666666",
            "accent": "#0070F3"
        },
        "typography": {
            "primary_font": "Inter",
            "secondary_font": "Inter",
            "code_font": "JetBrains Mono",
            "sizes": {
                "h1": {"size": "3.5rem", "weight": "700"},
                "h2": {"size": "2.5rem", "weight": "600"},
                "h3": {"size": "2rem", "weight": "600"},
                "body": {"size": "1.125rem", "weight": "400"},
                "small": {"size": "0.875rem", "weight": "400"}
            }
        },
        "components": {
            "buttons": {
                "primary": {
                    "background": "#000000",
                    "color": "#FFFFFF",
                    "padding": "12px 24px",
                    "border_radius": "6px",
                    "transition": "all 0.2s ease"
                },
                "secondary": {
                    "background": "transparent",
                    "color": "#000000",
                    "border": "1px solid #000000",
                    "padding": "12px 24px",
                    "border_radius": "6px"
                }
            },
            "cards": {
                "default": {
                    "background": "#FFFFFF",
                    "padding": "32px",
                    "border_radius": "8px",
                    "shadow": "0 4px 12px rgba(0,0,0,0.1)"
                }
            }
        },
        "layout": {
            "container": {
                "max_width": "1200px",
                "margin": "0 auto",
                "padding": "0 24px"
            },
            "grid": {
                "display": "grid",
                "gap": "32px"
            },
            "sections": {
                "padding": "120px 0"
            }
        },
        "effects": {
            "shadows": {
                "sm": "0 2px 8px rgba(0,0,0,0.1)",
                "md": "0 4px 16px rgba(0,0,0,0.15)",
                "lg": "0 8px 32px rgba(0,0,0,0.1)"
            },
            "transitions": {
                "default": "all 0.2s ease",
                "slow": "all 0.3s ease"
            }
        },
        "spacing": {
            "scale": {
                "0": "0px",
                "1": "4px",
                "2": "8px",
                "3": "12px",
                "4": "16px",
                "5": "20px",
                "6": "24px",
                "8": "32px",
                "10": "40px",
                "12": "48px",
                "16": "64px",
                "20": "80px",
                "24": "96px",
                "32": "128px"
            },
            "responsive": {
                "sm": "640px",
                "md": "768px",
                "lg": "1024px",
                "xl": "1280px"
            }
        }
    },
    
    "nextjs": {
        "name": "Next.js Default Styling",
        "description": "Clean design following Next.js default patterns",
        "colors": {
            "primary": "#0070F3",
            "secondary": "#666666",
            "background": "#FFFFFF",
            "surface": "#F8F9FA",
            "text": "#000000",
            "text_secondary": "#666666",
            "accent": "#0070F3"
        },
        "typography": {
            "primary_font": "Inter",
            "secondary_font": "Inter",
            "code_font": "JetBrains Mono",
            "sizes": {
                "h1": {"size": "3rem", "weight": "700"},
                "h2": {"size": "2.25rem", "weight": "600"},
                "h3": {"size": "1.875rem", "weight": "600"},
                "body": {"size": "1rem", "weight": "400"},
                "small": {"size": "0.875rem", "weight": "400"}
            }
        },
        "components": {
            "buttons": {
                "primary": {
                    "background": "#0070F3",
                    "color": "#FFFFFF",
                    "padding": "10px 20px",
                    "border_radius": "6px",
                    "transition": "all 0.2s ease"
                },
                "secondary": {
                    "background": "#6B7280",
                    "color": "#FFFFFF",
                    "padding": "10px 20px",
                    "border_radius": "6px"
                }
            },
            "cards": {
                "default": {
                    "background": "#FFFFFF",
                    "padding": "24px",
                    "border_radius": "8px",
                    "border": "1px solid #E5E7EB"
                }
            }
        },
        "layout": {
            "container": {
                "max_width": "1200px",
                "margin": "0 auto",
                "padding": "0 24px"
            },
            "grid": {
                "display": "grid",
                "gap": "24px"
            },
            "sections": {
                "padding": "80px 0"
            }
        },
        "effects": {
            "shadows": {
                "sm": "0 1px 3px rgba(0,0,0,0.1)",
                "md": "0 4px 6px rgba(0,0,0,0.1)",
                "lg": "0 10px 15px rgba(0,0,0,0.1)"
            },
            "transitions": {
                "default": "all 0.2s ease"
            }
        },
        "spacing": {
            "scale": {
                "0": "0px",
                "1": "4px",
                "2": "8px",
                "3": "12px",
                "4": "16px",
                "5": "20px",
                "6": "24px",
                "8": "32px",
                "10": "40px",
                "12": "48px",
                "16": "64px",
                "20": "80px",
                "24": "96px"
            },
            "responsive": {
                "sm": "640px",
                "md": "768px",
                "lg": "1024px",
                "xl": "1280px"
            }
        }
    },
    
    "shadcn": {
        "name": "shadcn/ui Components",
        "description": "Design system using shadcn/ui components and patterns",
        "colors": {
            "primary": "#000000",
            "secondary": "#F5F5F5",
            "background": "#FFFFFF",
            "surface": "#FAFAFA",
            "text": "#000000",
            "text_secondary": "#666666",
            "accent": "#0070F3"
        },
        "typography": {
            "primary_font": "Inter",
            "secondary_font": "Inter",
            "code_font": "JetBrains Mono",
            "sizes": {
                "h1": {"size": "2.25rem", "weight": "700"},
                "h2": {"size": "1.875rem", "weight": "600"},
                "h3": {"size": "1.5rem", "weight": "600"},
                "body": {"size": "1rem", "weight": "400"},
                "small": {"size": "0.875rem", "weight": "400"}
            }
        },
        "components": {
            "buttons": {
                "primary": {
                    "background": "#000000",
                    "color": "#FFFFFF",
                    "padding": "8px 16px",
                    "border_radius": "6px",
                    "transition": "all 0.2s ease"
                },
                "secondary": {
                    "background": "#F5F5F5",
                    "color": "#000000",
                    "padding": "8px 16px",
                    "border_radius": "6px"
                }
            },
            "cards": {
                "default": {
                    "background": "#FFFFFF",
                    "padding": "24px",
                    "border_radius": "8px",
                    "border": "1px solid #E5E7EB"
                }
            }
        },
        "layout": {
            "container": {
                "max_width": "1200px",
                "margin": "0 auto",
                "padding": "0 24px"
            },
            "grid": {
                "display": "grid",
                "gap": "24px"
            },
            "sections": {
                "padding": "64px 0"
            }
        },
        "effects": {
            "shadows": {
                "sm": "0 1px 2px rgba(0,0,0,0.05)",
                "md": "0 4px 6px rgba(0,0,0,0.07)",
                "lg": "0 10px 15px rgba(0,0,0,0.1)"
            },
            "transitions": {
                "default": "all 0.2s ease"
            }
        },
        "spacing": {
            "scale": {
                "0": "0px",
                "1": "4px",
                "2": "8px",
                "3": "12px",
                "4": "16px",
                "5": "20px",
                "6": "24px",
                "8": "32px",
                "10": "40px",
                "12": "48px",
                "16": "64px",
                "20": "80px",
                "24": "96px"
            },
            "responsive": {
                "sm": "640px",
                "md": "768px",
                "lg": "1024px",
                "xl": "1280px"
            }
        }
    },
    
    "tailwind": {
        "name": "Custom TailwindCSS",
        "description": "Custom TailwindCSS design with flexible theming",
        "colors": {
            "primary": "#3B82F6",
            "secondary": "#6B7280",
            "background": "#FFFFFF",
            "surface": "#F8FAFC",
            "text": "#1F2937",
            "text_secondary": "#6B7280",
            "accent": "#10B981"
        },
        "typography": {
            "primary_font": "Inter",
            "secondary_font": "Inter",
            "code_font": "JetBrains Mono",
            "sizes": {
                "h1": {"size": "3rem", "weight": "700"},
                "h2": {"size": "2.5rem", "weight": "600"},
                "h3": {"size": "2rem", "weight": "600"},
                "body": {"size": "1.125rem", "weight": "400"},
                "small": {"size": "0.875rem", "weight": "400"}
            }
        },
        "components": {
            "buttons": {
                "primary": {
                    "background": "#3B82F6",
                    "color": "#FFFFFF",
                    "padding": "12px 24px",
                    "border_radius": "8px",
                    "transition": "all 0.2s ease"
                },
                "secondary": {
                    "background": "#6B7280",
                    "color": "#FFFFFF",
                    "padding": "12px 24px",
                    "border_radius": "8px"
                }
            },
            "cards": {
                "default": {
                    "background": "#FFFFFF",
                    "padding": "24px",
                    "border_radius": "12px",
                    "shadow": "0 4px 6px rgba(0,0,0,0.05)"
                }
            }
        },
        "layout": {
            "container": {
                "max_width": "1200px",
                "margin": "0 auto",
                "padding": "0 24px"
            },
            "grid": {
                "display": "grid",
                "gap": "24px"
            },
            "sections": {
                "padding": "96px 0"
            }
        },
        "effects": {
            "shadows": {
                "sm": "0 1px 2px rgba(0,0,0,0.05)",
                "md": "0 4px 6px rgba(0,0,0,0.1)",
                "lg": "0 10px 15px rgba(0,0,0,0.1)"
            },
            "transitions": {
                "default": "all 0.2s ease"
            }
        },
        "spacing": {
            "scale": {
                "0": "0px",
                "1": "4px",
                "2": "8px",
                "3": "12px",
                "4": "16px",
                "5": "20px",
                "6": "24px",
                "8": "32px",
                "10": "40px",
                "12": "48px",
                "16": "64px",
                "20": "80px",
                "24": "96px"
            },
            "responsive": {
                "sm": "640px",
                "md": "768px",
                "lg": "1024px",
                "xl": "1280px"
            }
        }
    },
    
    "default": {
        "name": "Default Clean Design",
        "description": "Simple, clean design suitable for most projects",
        "colors": {
            "primary": "#000000",
            "secondary": "#666666",
            "background": "#FFFFFF",
            "surface": "#F8F9FA",
            "text": "#000000",
            "text_secondary": "#666666",
            "accent": "#0070F3"
        },
        "typography": {
            "primary_font": "Inter",
            "secondary_font": "Inter",
            "code_font": "JetBrains Mono",
            "sizes": {
                "h1": {"size": "2.5rem", "weight": "700"},
                "h2": {"size": "2rem", "weight": "600"},
                "h3": {"size": "1.5rem", "weight": "600"},
                "body": {"size": "1rem", "weight": "400"},
                "small": {"size": "0.875rem", "weight": "400"}
            }
        },
        "components": {
            "buttons": {
                "primary": {
                    "background": "#000000",
                    "color": "#FFFFFF",
                    "padding": "12px 24px",
                    "border_radius": "6px",
                    "transition": "all 0.2s ease"
                },
                "secondary": {
                    "background": "transparent",
                    "color": "#000000",
                    "border": "1px solid #000000",
                    "padding": "12px 24px",
                    "border_radius": "6px"
                }
            },
            "cards": {
                "default": {
                    "background": "#FFFFFF",
                    "padding": "24px",
                    "border_radius": "8px",
                    "border": "1px solid #E5E7EB"
                }
            }
        },
        "layout": {
            "container": {
                "max_width": "1200px",
                "margin": "0 auto",
                "padding": "0 24px"
            },
            "grid": {
                "display": "grid",
                "gap": "24px"
            },
            "sections": {
                "padding": "80px 0"
            }
        },
        "effects": {
            "shadows": {
                "sm": "0 1px 3px rgba(0,0,0,0.1)",
                "md": "0 4px 6px rgba(0,0,0,0.1)",
                "lg": "0 10px 15px rgba(0,0,0,0.1)"
            },
            "transitions": {
                "default": "all 0.2s ease"
            }
        },
        "spacing": {
            "scale": {
                "0": "0px",
                "1": "4px",
                "2": "8px",
                "3": "12px",
                "4": "16px",
                "5": "20px",
                "6": "24px",
                "8": "32px",
                "10": "40px",
                "12": "48px",
                "16": "64px",
                "20": "80px",
                "24": "96px"
            },
            "responsive": {
                "sm": "640px",
                "md": "768px",
                "lg": "1024px",
                "xl": "1280px"
            }
        }
    }
}

def get_available_frameworks() -> List[str]:
    """Get list of available UI frameworks"""
    return list(UI_FRAMEWORKS.keys())

def get_framework_config(framework: str) -> Dict:
    """Get configuration for specific UI framework"""
    return UI_FRAMEWORKS.get(framework, UI_FRAMEWORKS["default"])

def list_framework_names() -> Dict[str, str]:
    """Get framework names and descriptions"""
    return {
        key: config["name"] 
        for key, config in UI_FRAMEWORKS.items()
    }

def get_framework_description(framework: str) -> str:
    """Get description for specific framework"""
    return UI_FRAMEWORKS.get(framework, {}).get("description", "Unknown framework")

# Export all
__all__ = ["UI_FRAMEWORKS", API_TOKEN_PLACEHOLDER, API_TOKEN_PLACEHOLDER, API_TOKEN_PLACEHOLDER, API_TOKEN_PLACEHOLDER]
