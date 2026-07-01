function TestimonialCard({
  name,
  role,
  feedback,
  avatar,
}) {
  return (
    <div
      className="
        bg-white
        rounded-3xl
        p-8
        shadow-md
        border
        border-slate-200
        transition-all
        duration-300
        hover:-translate-y-2
        hover:shadow-xl
      "
    >
      <div className="flex items-center gap-4">

        <div
          className="
            w-16
            h-16
            rounded-full
            bg-blue-100
            flex
            items-center
            justify-center
            text-3xl
          "
        >
          {avatar}
        </div>

        <div>
          <h3 className="font-bold text-xl">
            {name}
          </h3>

          <p className="text-slate-500">
            {role}
          </p>
        </div>

      </div>

      <p
        className="
          mt-6
          text-slate-600
          leading-8
        "
      >
        "{feedback}"
      </p>

      <div className="mt-6 text-yellow-500 text-xl">
        ⭐⭐⭐⭐⭐
      </div>
    </div>
  );
}

export default TestimonialCard;