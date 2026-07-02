function DashboardCard({
  title,
  value,
  valueColor,
}) {
  return (
    <div className="flex items-center justify-between rounded-2xl border border-slate-200 bg-white p-3 sm:p-4 transition-all duration-300 hover:shadow-md">

      {/* Left */}
      <div className="min-w-0">
        <p className="text-xs sm:text-sm text-slate-500">
          {title}
        </p>

        <h3
          className={`mt-1 text-2xl sm:text-4xl font-bold break-words ${valueColor}`}
        >
          {value}
        </h3>
      </div>

      {/* Right */}
      <div className="ml-3 flex h-10 w-10 flex-shrink-0 items-center justify-center rounded-xl bg-blue-100 text-xl sm:h-14 sm:w-14 sm:text-3xl">
        📊
      </div>

    </div>
  );
}

export default DashboardCard;