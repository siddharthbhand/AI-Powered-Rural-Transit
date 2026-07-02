import Button from "../UI/Button/Button";
import Dashboard from "../Dashboard/Dashboard";

function Hero() {
  return (
    <section className="bg-slate-100">
      <div className="mx-auto max-w-7xl grid grid-cols-1 lg:grid-cols-2 items-center gap-10 lg:gap-16 px-4 sm:px-6 lg:px-8 py-12 sm:py-16 lg:py-20">

        {/* Left Side */}
        <div>

          {/* Badge */}
          <span className="inline-flex items-center rounded-full bg-blue-100 px-3 py-2 text-xs sm:text-sm font-semibold text-blue-700">
            🚍 AI Powered Smart Mobility
          </span>

          {/* Heading */}
          <h1 className="mt-6 text-4xl sm:text-5xl lg:text-6xl font-extrabold leading-tight text-slate-900">
            Smarter Public
            <br />
            Transport
            <br />
            for Every Village.
          </h1>

          {/* Description */}
          <p className="mt-6 max-w-xl text-base sm:text-lg lg:text-xl leading-8 text-slate-600">
            Track buses in real time, predict arrival using AI,
            optimize rural transportation and improve passenger
            experience with one intelligent platform.
          </p>

          {/* Buttons */}
          <div className="mt-8 flex flex-col sm:flex-row gap-4">

            <Button>
              🚍 Track Live Bus
            </Button>

            <Button variant="secondary">
              ▶ Watch Demo
            </Button>

          </div>

          {/* Features */}
          <div className="mt-8 flex flex-col sm:flex-row sm:flex-wrap gap-3 sm:gap-6 text-sm font-medium text-slate-600">

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