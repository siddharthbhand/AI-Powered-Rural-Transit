function FeatureCard({ icon, title, description }) {
  return (
    <div
      className="
        rounded-3xl
        border
        border-slate-200
        bg-white
        p-6
        shadow-sm
        transition-all
        duration-300
        hover:-translate-y-2
        hover:shadow-xl
      "
    >
      <div
        className="
          flex
          h-16
          w-16
          items-center
          justify-center
          rounded-2xl
          bg-blue-100
          text-3xl
        "
      >
        {icon}
      </div>

      <h3 className="mt-6 text-xl font-bold text-slate-900">
        {title}
      </h3>

      <p className="mt-3 text-slate-600 leading-7">
        {description}
      </p>

      <button
        className="
          mt-6
          font-semibold
          text-blue-600
          transition
          hover:text-blue-800
        "
      >
        Learn More →
      </button>
    </div>
  );
}

export default FeatureCard;