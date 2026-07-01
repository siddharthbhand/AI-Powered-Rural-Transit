import DashboardCard from "./DashboardCard";

function Dashboard() {
  return (
    <div className="w-full rounded-3xl bg-white p-4 sm:p-6 lg:p-8 shadow-xl">

      {/* Header */}
      <div className="mb-6 flex items-center justify-between">
        <h3 className="text-xl sm:text-2xl font-bold text-slate-800">
          Live Dashboard
        </h3>

        <span className="rounded-full bg-green-100 px-3 py-1 text-xs sm:text-sm font-semibold text-green-700">
          ● Live
        </span>
      </div>

      {/* Map Preview */}
      <div className="mb-6 flex h-40 sm:h-52 flex-col items-center justify-center rounded-2xl border-2 border-dashed border-slate-300 bg-slate-100">

        <div className="text-4xl sm:text-6xl">
          🗺️
        </div>

        <h4 className="mt-3 text-base sm:text-lg font-semibold text-slate-700 text-center">
          Live Bus Map Preview
        </h4>

        <p className="mt-2 text-center text-xs sm:text-sm text-slate-500 px-3">
          OpenStreetMap Integration Coming Soon
        </p>

      </div>

      {/* Dashboard Cards */}
      <div className="space-y-3 sm:space-y-4">
        <DashboardCard
          title="Active Buses"
          value="124"
          valueColor="text-blue-600"
        />

        <DashboardCard
          title="Routes Covered"
          value="38"
          valueColor="text-green-600"
        />

        <DashboardCard
          title="ETA Accuracy"
          value="96%"
          valueColor="text-orange-500"
        />
      </div>

    </div>
  );
}

export default Dashboard;