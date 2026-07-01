function DashboardCard({
  title,
  value,
  valueColor = "text-blue-600",
}) {
  return (
    <div className="flex items-center justify-between bg-slate-50 border border-slate-200 rounded-2xl p-5 hover:shadow-lg transition-all duration-300">

      <div>
        <p className="text-sm text-slate-500">
          {title}
        </p>

        <h2 className={`mt-2 text-3xl font-bold ${valueColor}`}>
          {value}
        </h2>
      </div>

      <div className="w-14 h-14 rounded-2xl bg-blue-100 flex items-center justify-center text-2xl">
        📊
      </div>

    </div>
  );
}

export default DashboardCard;