import FeatureCard from "./FeatureCard";

function Features() {
  return (
    <section className="bg-white py-16 sm:py-20 lg:py-24">

      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">

        <div className="text-center">

          <h2 className="text-3xl font-bold text-slate-900 sm:text-4xl lg:text-5xl">
            Everything Needed
            <br className="hidden sm:block" />
            {" "}for Rural Mobility
          </h2>

          <p className="mx-auto mt-5 max-w-3xl text-base leading-7 text-slate-600 sm:text-lg lg:text-xl">
            Our AI-powered platform helps passengers, drivers and
            transport authorities manage rural public transportation
            efficiently.
          </p>

        </div>

        <div className="mt-12 grid grid-cols-1 gap-6 sm:grid-cols-2 lg:mt-16 lg:grid-cols-4 lg:gap-8">

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