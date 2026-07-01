function Logo() {
  return (
    <div className="flex items-center gap-3 cursor-pointer">
      <div className="w-10 h-10 rounded-xl bg-blue-600 text-white flex items-center justify-center font-bold text-lg shadow-md">
        RT
      </div>

      <div>
        <h1 className="text-lg font-bold text-slate-900">
          RuralTransit AI
        </h1>

        <p className="text-xs text-slate-500">
          Smart Public Transport
        </p>
      </div>
    </div>
  );
}

export default Logo;