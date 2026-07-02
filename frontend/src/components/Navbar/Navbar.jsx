import { useState } from "react";
import Logo from "../Logo/Logo";
import Button from "../UI/Button/Button";
import navLinks from "./navLinks";

function Navbar() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <header className="sticky top-0 z-50 border-b border-slate-200 bg-white/90 shadow-sm backdrop-blur-md">
      <div className="mx-auto flex h-20 max-w-7xl items-center justify-between px-4 sm:px-6 lg:px-8">

        <Logo />

        {/* Desktop Navigation */}
        <nav className="hidden items-center gap-10 lg:flex">
          {navLinks.map((link) => (
            <a
              key={link.name}
              href={link.href}
              className="font-medium text-slate-700 transition hover:text-blue-600"
            >
              {link.name}
            </a>
          ))}
        </nav>

        {/* Desktop Buttons */}
        <div className="hidden items-center gap-4 lg:flex">
          <Button variant="secondary">
            Login
          </Button>

          <Button>
            Get Started
          </Button>
        </div>

        {/* Mobile Toggle */}
        <button
          onClick={() => setIsOpen(!isOpen)}
          className="rounded-lg p-2 text-3xl text-slate-800 transition hover:bg-slate-100 lg:hidden"
          aria-label="Toggle Menu"
        >
          {isOpen ? "✕" : "☰"}
        </button>

      </div>

      {/* Mobile Menu */}
      {isOpen && (
        <div className="border-t border-slate-200 bg-white shadow-lg lg:hidden">

          <nav className="flex flex-col gap-5 px-6 py-6">

            {navLinks.map((link) => (
              <a
                key={link.name}
                href={link.href}
                onClick={() => setIsOpen(false)}
                className="text-lg font-medium text-slate-700 transition hover:text-blue-600"
              >
                {link.name}
              </a>
            ))}

            <div className="flex flex-col gap-4 pt-4">

              <Button variant="secondary">
                Login
              </Button>

              <Button>
                Get Started
              </Button>

            </div>

          </nav>

        </div>
      )}
    </header>
  );
}

export default Navbar;