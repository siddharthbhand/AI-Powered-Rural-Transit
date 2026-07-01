import Logo from "../Logo/Logo";
import Button from "../UI/Button/Button";
import navLinks from "./navLinks";

function Navbar() {
  return (
    <header className="sticky top-0 z-50 bg-white/90 backdrop-blur-md border-b border-slate-200 shadow-sm">
      <div className="max-w-7xl mx-auto flex items-center justify-between px-4 sm:px-6 lg:px-8 py-4">

        {/* Logo */}
        <Logo />

        {/* Desktop Navigation */}
        <nav className="hidden lg:flex items-center gap-10">
          {navLinks.map((link) => (
            <a
              key={link.name}
              href={link.href}
              className="font-medium text-slate-700 transition-colors duration-300 hover:text-blue-600"
            >
              {link.name}
            </a>
          ))}
        </nav>

        {/* Desktop Buttons */}
        <div className="hidden md:flex items-center gap-4">
          <Button variant="secondary">
            Login
          </Button>

          <Button>
            Get Started
          </Button>
        </div>

        {/* Mobile Menu Button (Coming in Phase 11.2) */}
        <button
          className="md:hidden p-2 rounded-lg hover:bg-slate-100 transition"
          aria-label="Open Menu"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            className="w-7 h-7 text-slate-700"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
            strokeWidth="2"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              d="M4 6h16M4 12h16M4 18h16"
            />
          </svg>
        </button>

      </div>
    </header>
  );
}

export default Navbar;