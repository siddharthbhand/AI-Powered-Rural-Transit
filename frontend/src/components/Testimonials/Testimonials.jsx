import TestimonialCard from "./TestimonialCard";

function Testimonials() {
  return (
    <section className="bg-white py-24">
      <div className="max-w-7xl mx-auto px-8">

        <div className="text-center">

          <h2 className="text-5xl font-bold text-slate-900">
            Loved by Rural Communities
          </h2>

          <p className="mt-6 text-xl text-slate-600">
            Hear what passengers, drivers and transport authorities say about our platform.
          </p>

        </div>

        <div className="grid lg:grid-cols-3 gap-8 mt-16">

          <TestimonialCard
            avatar="👨"
            name="Rahul Patil"
            role="Daily Passenger"
            feedback="Real-time tracking has made my daily travel much easier and more reliable."
          />

          <TestimonialCard
            avatar="👩"
            name="Sneha Kulkarni"
            role="Village Transport Officer"
            feedback="AI-powered analytics helped us optimize routes and reduce waiting time."
          />

          <TestimonialCard
            avatar="🧑"
            name="Amit Shinde"
            role="Bus Driver"
            feedback="The live dashboard keeps everything organized and improves communication."
          />

        </div>

      </div>
    </section>
  );
}

export default Testimonials;