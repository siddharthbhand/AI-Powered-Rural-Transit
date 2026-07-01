import DashboardCard from "./DashboardCard";

function Dashboard() {
  return (
    <div className="bg-white rounded-3xl shadow-xl p-8">

      {/* Header */}
      <div className="flex items-center justify-between mb-6">

        <h3 className="text-2xl font-bold text-slate-800">
          Live Dashboard
        </h3>

        <span className="bg-green-100 text-green-700 px-4 py-2 rounded-full text-sm font-semibold">
          ● Live
        </span>

      </div>

      {/* Mini Map Preview */}
      <div className="bg-slate-100 rounded-2xl h-52 flex flex-col items-center justify-center border-2 border-dashed border-slate-300 mb-6">

        <div className="text-6xl">
          🗺️
        </div>

        <h4 className="mt-4 text-lg font-semibold text-slate-700">
          Live Bus Map Preview
        </h4>

        <p className="text-sm text-slate-500 mt-2">
          OpenStreetMap Integration Coming Soon
        </p>

      </div>

      {/* Statistics */}
      <div className="space-y-4">

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