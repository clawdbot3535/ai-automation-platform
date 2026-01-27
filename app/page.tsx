export default function Home() {
  const services = [
    {
      icon: "⚡",
      title: "Rapid Softwareentwicklung",
      description: "Von der Idee zum MVP in Tagen statt Monaten. AI-gestützte Entwicklung beschleunigt jeden Schritt des Prozesses.",
      tags: ["MVP in 2 Wochen", "Iterativ", "Kosteneffizient"]
    },
    {
      icon: "🎨", 
      title: "Vibe-Coding",
      description: "Beschreiben Sie Ihre Vision in natürlicher Sprache. Unsere AI transformiert Konzepte in funktionierenden Code.",
      tags: ["Natural Language", "Design-to-Code", "Prototyping"]
    },
    {
      icon: "🧠",
      title: "RAG-Systeme", 
      description: "Retrieval-Augmented Generation für präzise, kontextbezogene Antworten aus Ihren Unternehmensdaten.",
      tags: ["Wissensbasis", "Dokumentensuche", "Präzision"]
    },
    {
      icon: "💬",
      title: "AI-Chatbots",
      description: "Intelligente Konversationsagenten für Support, Sales und interne Prozesse. 24/7 verfügbar.",
      tags: ["Multi-Channel", "Multilingual", "Integration"]
    }
  ];

  const useCases = [
    {
      number: "01",
      title: "Kundenservice-Automatisierung",
      metric: "-65% Response-Zeit",
      description: "AI-Chatbot bearbeitet Tier-1-Anfragen, eskaliert komplexe Fälle automatisch an Mitarbeiter.",
      details: ["Automated response generation", "Intelligent ticket routing", "Priority classification"]
    },
    {
      number: "02", 
      title: "Dokumentenanalyse & Extraktion",
      metric: "10x schneller",
      description: "RAG-System durchsucht tausende Dokumente in Sekunden und liefert präzise Antworten mit Quellenangabe.",
      details: ["Template-based generation", "Automated distribution", "Version control"]
    },
    {
      number: "03",
      title: "Interne Tools & Dashboards", 
      metric: "2 Wochen Entwicklung",
      description: "Maßgeschneiderte Anwendungen durch Vibe-Coding – beschreiben Sie, was Sie brauchen, wir liefern.",
      details: ["Custom development", "Rapid prototyping", "Agile delivery"]
    },
    {
      number: "04",
      title: "Workflow-Automatisierung",
      metric: "80% weniger manuell", 
      description: "Verbinden Sie Ihre Systeme mit intelligenten Automatisierungen, die lernen und sich anpassen.",
      details: ["System integration", "Intelligent automation", "Adaptive learning"]
    }
  ];

  const processSteps = [
    {"step": "1", "title": "Discovery", "items": ["Anforderungsanalyse", "Prozess-Mapping", "ROI-Schätzung"]},
    {"step": "2", "title": "Konzept", "items": ["Lösungsarchitektur", "Wireframes", "Tech-Stack"]},
    {"step": "3", "title": "Entwicklung", "items": ["Agile Sprints", "Kontinuierliches Feedback", "Testing"]},
    {"step": "4", "title": "Launch", "items": ["Deployment", "Training", "Support & Iteration"]}
  ];

  const techStack = ["OpenAI", "Anthropic", "n8n", "LangChain", "Pinecone", "Vercel", "Supabase", "React", "Node.js", "Python", "Docker", "AWS"];

  return (
    <main className="min-h-screen bg-zinc-50 font-sans">
      {/* Grid Overlay */}
      <div className="fixed inset-0 pointer-events-none opacity-[0.03]" 
           style={{backgroundImage: 'linear-gradient(#000 1px, transparent 1px), linear-gradient(90deg, #000 1px, transparent 1px)', backgroundSize: '40px 40px'}} />
      
      {/* Header */}
      <header className="relative border-b-2 border-zinc-200 bg-white">
        <div className="max-w-6xl mx-auto px-6 py-4 flex items-center justify-between">
          <div className="px-6 py-2 border-2 border-dashed border-zinc-400 bg-zinc-100/50">
            <span className="font-mono font-bold text-zinc-700">d56</span>
          </div>
          
          <nav className="hidden md:flex gap-8">
            {['Services', 'Use Cases', 'Prozess', 'Kontakt'].map((item, i) => (
              <a key={i} href="#" className="font-mono text-sm text-zinc-600 hover:text-emerald-600 transition-colors">
                {item}
              </a>
            ))}
          </nav>
          
          <div className="px-4 py-2 bg-zinc-900 border-zinc-900">
            <span className="font-mono text-sm text-white">CTA Button</span>
          </div>
        </div>
      </header>

      {/* Hero Section */}
      <section className="relative py-24 border-b-2 border-zinc-200">
        <div className="max-w-6xl mx-auto px-6">
          <div className="grid md:grid-cols-2 gap-12 items-center">
            <div>
              <div className="inline-block bg-emerald-100 text-emerald-700 font-mono text-xs px-3 py-1 mb-6 border border-emerald-300">
                AI-AUTOMATISIERUNG FÜR B2B
              </div>
              <h1 className="text-4xl md:text-5xl font-bold text-zinc-900 leading-tight mb-6">
                Automatisieren Sie<br />
                <span className="text-emerald-600">intelligenter,</span><br />
                nicht härter.
              </h1>
              <p className="text-lg text-zinc-600 mb-8 leading-relaxed">
                Von Rapid Prototyping bis zu komplexen RAG-Systemen – wir transformieren Ihre Geschäftsprozesse mit maßgeschneiderten AI-Lösungen.
              </p>
              <div className="flex flex-wrap gap-4">
                <button className="bg-zinc-900 text-white font-mono px-6 py-3 hover:bg-emerald-600 transition-colors">
                  Erstgespräch vereinbaren
                </button>
                <button className="border-2 border-zinc-300 text-zinc-700 font-mono px-6 py-3 hover:border-zinc-900 transition-colors">
                  Use Cases ansehen
                </button>
              </div>
            </div>
            
            <div className="border-2 border-dashed border-zinc-400 bg-zinc-100/50 aspect-square flex items-center justify-center">
              <div className="text-center p-8">
                <div className="grid grid-cols-2 gap-4 mb-4">
                  {['⚡', '🧠', '🎨', '💬'].map((icon, i) => (
                    <div key={i} className="w-16 h-16 bg-white border-2 border-zinc-300 flex items-center justify-center text-2xl mx-auto">
                      {icon}
                    </div>
                  ))}
                </div>
                <p className="font-mono text-xs text-zinc-500 mt-4">
                  [Animierte Grafik / Illustration]
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Services Section */}
      <section className="py-20 bg-white border-b-2 border-zinc-200">
        <div className="max-w-6xl mx-auto px-6">
          <div className="mb-12">
            <span className="font-mono text-xs text-emerald-600 tracking-wider">SERVICES</span>
            <h2 className="text-3xl font-bold text-zinc-900 mt-2">
              Was wir für Sie entwickeln
            </h2>
          </div>
          
          <div className="grid md:grid-cols-2 gap-6">
            {services.map((service, i) => (
              <div key={i} className="group relative bg-white border-2 border-zinc-300 p-6 hover:border-emerald-500 hover:shadow-lg transition-all duration-300">
                <div className="absolute top-0 right-0 w-16 h-16 bg-zinc-100 flex items-center justify-center text-2xl group-hover:bg-emerald-500 group-hover:text-white transition-all">
                  {service.icon}
                </div>
                <div className="pr-16">
                  <h3 className="font-mono text-lg font-bold text-zinc-900 mb-2">{service.title}</h3>
                  <p className="text-sm text-zinc-600 leading-relaxed mb-4">{service.description}</p>
                  <div className="flex flex-wrap gap-2">
                    {service.tags.map((tag, i) => (
                      <span key={i} className="text-xs font-mono bg-zinc-100 text-zinc-700 px-2 py-1 border border-zinc-300">
                        {tag}
                      </span>
                    ))}
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Use Cases Section */}
      <section className="py-20 border-b-2 border-zinc-200">
        <div className="max-w-6xl mx-auto px-6">
          <div className="grid md:grid-cols-2 gap-16">
            <div>
              <span className="font-mono text-xs text-emerald-600 tracking-wider">USE CASES</span>
              <h2 className="text-3xl font-bold text-zinc-900 mt-2 mb-6">
                Konkrete Anwendungen
              </h2>
              <div className="border-2 border-dashed border-zinc-400 bg-zinc-100/50 aspect-video flex items-center justify-center">
                <span className="font-mono text-sm text-zinc-500">[Screenshot / Demo-Video]</span>
              </div>
            </div>
            
            <div>
              {useCases.map((useCase, i) => (
                <div key={i} className="flex gap-6 items-start py-6 border-b border-zinc-200 last:border-0">
                  <div className="flex-shrink-0 w-12 h-12 bg-emerald-500 text-white font-mono text-xl font-bold flex items-center justify-center">
                    {useCase.number}
                  </div>
                  <div className="flex-1">
                    <div className="flex items-baseline gap-4 mb-2">
                      <h4 className="font-mono font-bold text-zinc-900">{useCase.title}</h4>
                      <span className="text-emerald-600 font-mono text-sm font-bold">{useCase.metric}</span>
                    </div>
                    <p className="text-sm text-zinc-600 mb-3">{useCase.description}</p>
                    <ul className="space-y-1">
                      {useCase.details.map((detail, i) => (
                        <li key={i} className="flex items-center text-xs text-zinc-500">
                          <span className="text-green-500 mr-2">✓</span>
                          {detail}
                        </li>
                      ))}
                    </ul>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* Process Section */}
      <section className="py-20 bg-white border-b-2 border-zinc-200">
        <div className="max-w-6xl mx-auto px-6">
          <div className="text-center mb-16">
            <span className="font-mono text-xs text-emerald-600 tracking-wider">PROZESS</span>
            <h2 className="text-3xl font-bold text-zinc-900 mt-2">
              Von der Idee zur Lösung
            </h2>
          </div>
          
          <div className="grid md:grid-cols-4 gap-8">
            {processSteps.map((step, i) => (
              <div key={i} className="relative">
                <div className="flex items-center gap-4 mb-4">
                  <div className="w-10 h-10 rounded-full border-2 border-zinc-400 flex items-center justify-center font-mono font-bold text-zinc-600">
                    {step.step}
                  </div>
                  <h4 className="font-mono font-bold text-zinc-900">{step.title}</h4>
                </div>
                <div className="ml-5 pl-9 border-l-2 border-dashed border-zinc-300 pb-8">
                  {step.items.map((item, i) => (
                    <div key={i} className="flex items-center gap-2 text-sm text-zinc-600 mb-2">
                      <div className="w-1.5 h-1.5 bg-emerald-500"></div>
                      {item}
                    </div>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Tech Stack */}
      <section className="py-20 border-b-2 border-zinc-200">
        <div className="max-w-6xl mx-auto px-6">
          <div className="text-center mb-12">
            <span className="font-mono text-xs text-emerald-600 tracking-wider">TECHNOLOGIE</span>
            <h2 className="text-3xl font-bold text-zinc-900 mt-2">
              Unser Stack
            </h2>
          </div>
          
          <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-4">
            {techStack.map((tech, i) => (
              <div key={i} className="py-4 text-center border-2 border-dashed border-zinc-400 bg-zinc-100/50">
                <span className="font-mono text-sm text-zinc-600">{tech}</span>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-24 bg-zinc-900">
        <div className="max-w-4xl mx-auto px-6 text-center">
          <h2 className="text-3xl md:text-4xl font-bold text-white mb-6">
            Bereit für den nächsten Schritt?
          </h2>
          <p className="text-zinc-400 text-lg mb-8 max-w-2xl mx-auto">
            Lassen Sie uns in einem kostenlosen Erstgespräch herausfinden, wie AI-Automatisierung Ihr Unternehmen transformieren kann.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <button className="bg-emerald-500 text-white font-mono px-8 py-4 text-lg hover:bg-emerald-400 transition-colors">
              Termin vereinbaren
            </button>
            <button className="border-2 border-zinc-600 text-zinc-300 font-mono px-8 py-4 text-lg hover:border-zinc-400 hover:text-white transition-colors">
              Kontakt aufnehmen
            </button>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="py-12 bg-zinc-900 border-t border-zinc-800">
        <div className="max-w-6xl mx-auto px-6">
          <div className="grid md:grid-cols-4 gap-8 text-zinc-400 text-sm">
            <div>
              <div className="px-4 py-2 mb-4 border-2 border-dashed border-zinc-600 bg-zinc-800/50">
                <span className="font-mono text-white">d56</span>
              </div>
              <p className="text-zinc-500">
                Büro für Gestaltung<br />
                Donnersdorf, Germany
              </p>
            </div>
            
            <div>
              <h4 className="font-mono text-white mb-4">Services</h4>
              <ul className="space-y-2">
                {services.map((service, i) => (
                  <li key={i}><a href="#" className="hover:text-emerald-400 transition-colors">{service.title}</a></li>
                ))}
              </ul>
            </div>
            
            <div>
              <h4 className="font-mono text-white mb-4">Ressourcen</h4>
              <ul className="space-y-2">
                {['Blog', 'Case Studies', 'Dokumentation', 'FAQ'].map((item, i) => (
                  <li key={i}><a href="#" className="hover:text-emerald-400 transition-colors">{item}</a></li>
                ))}
              </ul>
            </div>
            
            <div>
              <h4 className="font-mono text-white mb-4">Kontakt</h4>
              <div className="p-4 border-2 border-dashed border-zinc-600 bg-zinc-800/50">
                <div className="space-y-2 font-mono text-xs">
                  <div className="text-zinc-500">[E-Mail]</div>
                  <div className="text-zinc-500">[Telefon]</div>
                  <div className="text-zinc-500">[Social Links]</div>
                </div>
              </div>
            </div>
          </div>
          
          <div className="mt-12 pt-8 border-t border-zinc-800 flex flex-col md:flex-row justify-between items-center gap-4">
            <p className="text-zinc-500 text-xs font-mono">
              © 2025 d56 Büro für Gestaltung. Alle Rechte vorbehalten.
            </p>
            <div className="flex gap-6 text-xs font-mono text-zinc-500">
              <a href="#" className="hover:text-white">Impressum</a>
              <a href="#" className="hover:text-white">Datenschutz</a>
              <a href="#" className="hover:text-white">AGB</a>
            </div>
          </div>
        </div>
      </footer>
    </main>
  )
}