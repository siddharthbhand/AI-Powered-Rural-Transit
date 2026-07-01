import StatisticCard from "./StatisticCard";

function Statistics() {
  return (
    <section className="bg-slate-50 py-24">
      <div className="max-w-7xl mx-auto px-8">

        <div className="text-center">
          <h2 className="text-5xl font-bold text-slate-900">
            Trusted by Rural Communities
          </h2>

          <p className="mt-6 text-xl text-slate-600">
            Real-time transport intelligence powered by AI and live GPS.
          </p>
        </div>

        <div className="grid grid-cols-2 lg:grid-cols-4 gap-8 mt-16">

          <StatisticCard
            number="50K+"
            label="Daily Passengers"
          />

          <StatisticCard
            number="500+"
            label="Smart Routes"
          />

          <StatisticCard
            number="99%"
            label="ETA Accuracy"
          />

          <StatisticCard
            number="24×7"
            label="Live Monitoring"
          />

        </div>

      </div>
    </section>
  );
}

export default Statistics;