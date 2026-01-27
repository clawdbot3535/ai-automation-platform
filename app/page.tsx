export default function Home() {
  return (
    <main className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      <div className="container mx-auto px-4 py-16">
        {/* Header */}
        <div className="text-center mb-16">
          <h1 className="text-5xl font-bold text-gray-900 mb-4">
            AI Automation Platform
          </h1>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto">
            Intelligent business process automation platform that streamlines workflows 
            and enhances productivity through cutting-edge AI technology.
          </p>
        </div>

        {/* Services Section */}
        <div className="mb-16">
          <h2 className="text-3xl font-bold text-center text-gray-900 mb-8">
            Our Core Services
          </h2>
          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
            {/* Email Support Service */}
            <div className="bg-white rounded-lg shadow-lg p-6 hover:shadow-xl transition-shadow">
              <div className="text-blue-600 text-3xl mb-4">📧</div>
              <h3 className="text-xl font-semibold mb-2">Email Support Service</h3>
              <p className="text-gray-600">
                Automated email response and support ticket management with AI-powered insights.
              </p>
            </div>

            {/* CRM Integration Service */}
            <div className="bg-white rounded-lg shadow-lg p-6 hover:shadow-xl transition-shadow">
              <div className="text-green-600 text-3xl mb-4">🤝</div>
              <h3 className="text-xl font-semibold mb-2">CRM Integration Service</h3>
              <p className="text-gray-600">
                Seamless integration with your existing CRM systems for unified customer management.
              </p>
            </div>

            {/* Document Generation Service */}
            <div className="bg-white rounded-lg shadow-lg p-6 hover:shadow-xl transition-shadow">
              <div className="text-purple-600 text-3xl mb-4">📄</div>
              <h3 className="text-xl font-semibold mb-2">Document Generation Service</h3>
              <p className="text-gray-600">
                Automated document creation, formatting, and distribution based on templates.
              </p>
            </div>

            {/* Workflow Automation Service */}
            <div className="bg-white rounded-lg shadow-lg p-6 hover:shadow-xl transition-shadow">
              <div className="text-orange-600 text-3xl mb-4">⚡</div>
              <h3 className="text-xl font-semibold mb-2">Workflow Automation Service</h3>
              <p className="text-gray-600">
                Custom workflow creation and automation to streamline your business processes.
              </p>
            </div>
          </div>
        </div>

        {/* Use Cases Section */}
        <div className="mb-16">
          <h2 className="text-3xl font-bold text-center text-gray-900 mb-8">
            Key Use Cases
          </h2>
          <div className="grid md:grid-cols-2 gap-8">
            {/* Email Support Automation */}
            <div className="bg-white rounded-lg shadow-lg p-8">
              <div className="text-red-500 text-4xl mb-4">🎯</div>
              <h3 className="text-2xl font-semibold mb-4">Email-Support-Automation</h3>
              <p className="text-gray-600 mb-4">
                Automate customer support responses, categorize inquiries, and route tickets 
                to the appropriate teams with intelligent routing.
              </p>
              <ul className="space-y-2 text-gray-600">
                <li className="flex items-center">
                  <span className="text-green-500 mr-2">✓</span>
                  Automated response generation
                </li>
                <li className="flex items-center">
                  <span className="text-green-500 mr-2">✓</span>
                  Intelligent ticket routing
                </li>
                <li className="flex items-center">
                  <span className="text-green-500 mr-2">✓</span>
                  Priority classification
                </li>
              </ul>
            </div>

            {/* Customer Relationship Management */}
            <div className="bg-white rounded-lg shadow-lg p-8">
              <div className="text-blue-500 text-4xl mb-4">👥</div>
              <h3 className="text-2xl font-semibold mb-4">Customer-Relationship-Management</h3>
              <p className="text-gray-600 mb-4">
                Streamline customer interactions, track engagement, and automate follow-up 
                processes to enhance customer satisfaction.
              </p>
              <ul className="space-y-2 text-gray-600">
                <li className="flex items-center">
                  <span className="text-green-500 mr-2">✓</span>
                  Automated follow-ups
                </li>
                <li className="flex items-center">
                  <span className="text-green-500 mr-2">✓</span>
                  Customer journey tracking
                </li>
                <li className="flex items-center">
                  <span className="text-green-500 mr-2">✓</span>
                  Predictive analytics
                </li>
              </ul>
            </div>

            {/* Document Generation Workflow */}
            <div className="bg-white rounded-lg shadow-lg p-8">
              <div className="text-purple-500 text-4xl mb-4">📋</div>
              <h3 className="text-2xl font-semibold mb-4">Document-Generation-Workflow</h3>
              <p className="text-gray-600 mb-4">
                Create, format, and distribute documents automatically based on predefined 
                templates and data sources.
              </p>
              <ul className="space-y-2 text-gray-600">
                <li className="flex items-center">
                  <span className="text-green-500 mr-2">✓</span>
                  Template-based generation
                </li>
                <li className="flex items-center">
                  <span className="text-green-500 mr-2">✓</span>
                  Automated distribution
                </li>
                <li className="flex items-center">
                  <span className="text-green-500 mr-2">✓</span>
                  Version control
                </li>
              </ul>
            </div>

            {/* Process Optimization Workflow */}
            <div className="bg-white rounded-lg shadow-lg p-8">
              <div className="text-orange-500 text-4xl mb-4">🚀</div>
              <h3 className="text-2xl font-semibold mb-4">Process-Optimization-Workflow</h3>
              <p className="text-gray-600 mb-4">
                Analyze and optimize existing business processes to reduce costs, 
                improve efficiency, and eliminate bottlenecks.
              </p>
              <ul className="space-y-2 text-gray-600">
                <li className="flex items-center">
                  <span className="text-green-500 mr-2">✓</span>
                  Process analysis
                </li>
                <li className="flex items-center">
                  <span className="text-green-500 mr-2">✓</span>
                  Bottleneck identification
                </li>
                <li className="flex items-center">
                  <span className="text-green-500 mr-2">✓</span>
                  Optimization recommendations
                </li>
              </ul>
            </div>
          </div>
        </div>

        {/* CTA Section */}
        <div className="text-center bg-white rounded-lg shadow-lg p-8">
          <h2 className="text-3xl font-bold text-gray-900 mb-4">
            Ready to Automate Your Business?
          </h2>
          <p className="text-xl text-gray-600 mb-8">
            Transform your business processes with AI-powered automation.
          </p>
          <div className="space-x-4">
            <button className="bg-blue-600 text-white px-8 py-3 rounded-lg font-semibold hover:bg-blue-700 transition-colors">
              Get Started
            </button>
            <button className="bg-gray-200 text-gray-800 px-8 py-3 rounded-lg font-semibold hover:bg-gray-300 transition-colors">
              Learn More
            </button>
          </div>
        </div>
      </div>
    </main>
  )
}