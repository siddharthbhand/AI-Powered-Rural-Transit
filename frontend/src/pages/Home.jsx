import Navbar from "../components/Navbar/Navbar";
import Hero from "../components/Hero/Hero";
import Features from "../components/Features/Features";
import Statistics from "../components/Statistics/Statistics";
import Testimonials from "../components/Testimonials/Testimonials";
import Footer from "../components/Footer/Footer";

function Home() {
  return (
    <>
      <Navbar />
      <Hero />
      <Features />
      <Statistics />
      <Testimonials />
      <Footer />
    </>
  );
}

export default Home;

