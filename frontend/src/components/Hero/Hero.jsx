import Button from "../UI/Button/Button";
import Dashboard from "../Dashboard/Dashboard";

function Hero() {
  return (
    <section className="bg-slate-100">
      <div className="mx-auto grid max-w-7xl grid-cols-1 items-center gap-10 px-4 py-12 sm:px-6 sm:py-16 lg:grid-cols-2 lg:gap-16 lg:px-8 lg:py-20">

        {/* Left Side */}
        <div>

          {/* Badge */}
          <span className="inline-flex items-center rounded-full bg-blue-100 px-3 py-2 text-xs font-semibold text-blue-700 sm:px-4 sm:text-sm">
            🚍 AI Powered Smart Mobility
          </span>

          {/* Heading */}
          <h1 className="mt-6 text-4xl font-bold leading-tight text-slate-900 sm:text-5xl lg:text-6xl">
            Smarter Public
            <br />
            Transport
            <br />
            for Every Village.
          </h1>

          {/* Description */}
          <p className="mt-6 max-w-xl text-base leading-7 text-slate-600 sm:text-lg lg:text-xl">
            Track buses in real time, predict arrival using AI,
            optimize rural transportation and improve passenger
            experience with one intelligent platform.
          </p>

          {/* Buttons */}
          <div className="mt-8 flex flex-col gap-3 sm:flex-row sm:flex-wrap">

            <Button>
              🚍 Track Live Bus
            </Button>

            <Button variant="secondary">
              ▶ Watch Demo
            </Button>

          </div>

          {/* Features */}
          <div className="mt-8 flex flex-col gap-3 text-sm font-medium text-slate-600 sm:flex-row sm:flex-wrap sm:gap-6">

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