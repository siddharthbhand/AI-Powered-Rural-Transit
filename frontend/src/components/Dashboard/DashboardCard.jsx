function DashboardCard({
  title,
  value,
  valueColor,
}) {
  return (
    <div className="flex items-center justify-between rounded-2xl border border-slate-200 bg-white p-3 sm:p-4 hover:shadow-md transition-all duration-300">

      <div>
        <p className="text-xs sm:text-sm text-slate-500">
          {title}
        </p>

        <h3 className={`text-2xl sm:text-4xl font-bold ${valueColor}`}>
          {value}
        </h3>
      </div>

      <div className="flex h-10 w-10 sm:h-14 sm:w-14 items-center justify-center rounded-xl bg-blue-100 text-xl sm:text-3xl">
        📊
      </div>

    </div>
  );
}

export default DashboardCard;