function StatisticCard({ number, label }) {
  return (
    <div
      className="
        bg-white
        rounded-3xl
        shadow-md
        p-8
        text-center
        border
        border-slate-200
        transition-all
        duration-300
        hover:-translate-y-2
        hover:shadow-xl
      "
    >
      <h3 className="text-5xl font-bold text-blue-600">
        {number}
      </h3>

      <p className="mt-4 text-lg text-slate-600">
        {label}
      </p>
    </div>
  );
}

export default StatisticCard;