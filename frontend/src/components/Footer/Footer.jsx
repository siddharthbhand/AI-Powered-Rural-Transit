function Footer() {
  return (
    <footer className="bg-slate-900 text-white py-16">
      <div className="max-w-7xl mx-auto px-8">

        <div className="grid md:grid-cols-4 gap-10">

          {/* Company */}

          <div>

            <h2 className="text-2xl font-bold">
              RuralTransit AI
            </h2>

            <p className="mt-4 text-slate-400 leading-7">
              AI-powered rural public transport platform improving mobility,
              accessibility and passenger experience.
            </p>

          </div>

          {/* Product */}

          <div>

            <h3 className="font-bold text-lg mb-4">
              Product
            </h3>

            <ul className="space-y-3 text-slate-400">

              <li>Live Tracking</li>

              <li>Smart Routes</li>

              <li>ETA Prediction</li>

              <li>Analytics</li>

            </ul>

          </div>

          {/* Company */}

          <div>

            <h3 className="font-bold text-lg mb-4">
              Company
            </h3>

            <ul className="space-y-3 text-slate-400">

              <li>About</li>

              <li>Contact</li>

              <li>Careers</li>

              <li>Privacy</li>

            </ul>

          </div>

          {/* Contact */}

          <div>

            <h3 className="font-bold text-lg mb-4">
              Contact
            </h3>

            <ul className="space-y-3 text-slate-400">

              <li>Pune, Maharashtra</li>

              <li>support@ruraltransit.ai</li>

              <li>+91 XXXXX XXXXX</li>

            </ul>

          </div>

        </div>

      </div>
    </footer>
  );
}

export default Footer;