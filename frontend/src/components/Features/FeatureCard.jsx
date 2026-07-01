function FeatureCard({ icon, title, description }) {
  return (
    <div
      className="
        bg-white
        rounded-3xl
        p-8
        border
        border-slate-200
        shadow-sm
        transition-all
        duration-300
        hover:-translate-y-3
        hover:shadow-2xl
        hover:border-blue-500
      "
    >
      <div className="w-16 h-16 rounded-2xl bg-blue-100 flex items-center justify-center text-4xl">
        {icon}
      </div>

      <h3 className="mt-6 text-2xl font-bold text-slate-900">
        {title}
      </h3>

      <p className="mt-4 text-slate-600 leading-7">
        {description}
      </p>

      <button
        className="
          mt-8
          font-semibold
          text-blue-600
          hover:text-blue-700
          transition
        "
      >
        Learn More →
      </button>
    </div>
  );
}

export default FeatureCard;