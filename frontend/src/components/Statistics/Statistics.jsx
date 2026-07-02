import StatisticCard from "./StatisticCard";

function Statistics() {
  const stats = [
    {
      value: "50K+",
      label: "Daily Passengers",
    },
    {
      value: "500+",
      label: "Smart Routes",
    },
    {
      value: "99%",
      label: "ETA Accuracy",
    },
    {
      value: "24×7",
      label: "Live Monitoring",
    },
  ];

  return (
    <section className="py-24 bg-gradient-to-b from-white to-slate-100">
      <div className="max-w-7xl mx-auto px-6 lg:px-8">
        {/* Heading */}
        <div className="text-center max-w-3xl mx-auto">
          <h2 className="text-4xl md:text-5xl font-bold text-slate-900">
            Trusted by Rural Communities
          </h2>

          <p className="mt-5 text-lg text-slate-600 leading-8">
            Real-time transport intelligence helping passengers,
            drivers and authorities across villages.
          </p>
        </div>

        {/* Statistics Grid */}
        <div className="mt-16 grid grid-cols-2 lg:grid-cols-4 gap-6">
          {stats.map((item) => (
            <StatisticCard
              key={item.label}
              value={item.value}
              label={item.label}
            />
          ))}
        </div>
      </div>
    </section>
  );
}

export default Statistics;