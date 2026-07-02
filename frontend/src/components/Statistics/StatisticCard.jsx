function StatisticCard({ value, label }) {
  return (
    <div
      className="
        bg-white
        rounded-3xl
        p-8
        text-center
        shadow-md
        border border-slate-200
        transition-all
        duration-300
        hover:-translate-y-2
        hover:shadow-2xl
        hover:border-blue-200
      "
    >
      {/* Number */}
      <h3
        className="
          text-4xl
          md:text-5xl
          font-extrabold
          bg-gradient-to-r
          from-blue-600
          to-cyan-500
          bg-clip-text
          text-transparent
        "
      >
        {value}
      </h3>

      {/* Label */}
      <p
        className="
          mt-4
          text-slate-600
          font-medium
          text-base
        "
      >
        {label}
      </p>
    </div>
  );
}

export default StatisticCard;