import Button from "../UI/Button/Button";
import Dashboard from "../Dashboard/Dashboard";

function Hero() {
  return (
    <section className="bg-slate-100">
      <div className="max-w-7xl mx-auto px-8 py-20 grid md:grid-cols-2 gap-16 items-center">

        {/* Left Side */}
        <div>

          <span className="inline-block bg-blue-100 text-blue-700 font-semibold px-4 py-2 rounded-full">
            🚍 AI Powered Smart Mobility
          </span>

          <h1 className="mt-6 text-6xl font-bold text-slate-900 leading-tight">
            Smarter Public Transport
            <br />
            for Every Village.
          </h1>

          <p className="mt-8 text-xl text-slate-600 leading-8 max-w-xl">
            Track buses in real time, predict arrival using AI,
            optimize rural transportation and improve passenger
            experience with one intelligent platform.
          </p>

          <div className="mt-10 flex flex-wrap gap-4">
            <Button>
              🚍 Track Live Bus
            </Button>

            <Button variant="secondary">
              ▶ Watch Demo
            </Button>
          </div>

          <div className="mt-10 flex flex-wrap gap-6 text-slate-600 font-medium">
            <span>✅ AI Powered</span>
            <span>📍 Live GPS Tracking</span>
            <span>⏱ ETA Prediction</span>
          </div>

        </div>

        {/* Right Side */}
        <Dashboard />

      </div>
    </section>
  );
}

export default Hero;