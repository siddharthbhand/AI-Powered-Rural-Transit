import FeatureCard from "./FeatureCard";

function Features() {
  return (
    <section className="bg-white py-24">

      <div className="max-w-7xl mx-auto px-8">

        <div className="text-center">

          <h2 className="text-5xl font-bold text-slate-900">
            Everything Needed for Rural Mobility
          </h2>

          <p className="mt-6 text-xl text-slate-600 max-w-3xl mx-auto">
            Our AI-powered platform helps passengers, drivers and transport
            authorities manage rural public transportation efficiently.
          </p>

        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8 mt-16">

          <FeatureCard
            icon="🚌"
            title="Live Bus Tracking"
            description="Track every bus in real time with GPS updates."
          />

          <FeatureCard
            icon="📍"
            title="Smart Routes"
            description="AI optimized routes for better connectivity."
          />

          <FeatureCard
            icon="⏱"
            title="ETA Prediction"
            description="Know accurate arrival time before leaving."
          />

          <FeatureCard
            icon="🤖"
            title="AI Analytics"
            description="Predict demand and improve transport planning."
          />

        </div>

      </div>

    </section>
  );
}

export default Features;