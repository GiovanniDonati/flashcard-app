const menu = [
  { name: "home", path: "/" },
  { name: "tags", path: "/tags" },
  { name: "collections", path: "/collections" },
  { name: "cards", path: "/cards" },
  { name: "settings", path: "/settings" },
];

const Sidebar = () => {
  return (
    <div className="flex flex-col h-screen w-52 bg-black border-r border-green-900/50 p-4 font-mono">
      <div className="px-2">
        <div className="text-green-500 text-xl font-bold flex items-center">
          <span className="mr-2 text-green-800 font-black">{">"}</span>
          Flashcards
          <span className="ml-1 w-2 h-5 bg-green-500 animate-pulse"></span>
        </div>
      </div>
      <span className="w-full h-0.5 bg-green-500 mb-4"></span>

      <nav className="space-y-1">
        {menu.map((item) => (
          <a
            key={item.path}
            href={item.path}
            className="group flex items-center px-3 py-2 rounded border border-transparent hover:border-green-500/30 hover:bg-green-500/10 transition-all duration-150"
          >
            <span className="text-green-800 mr-3 group-hover:text-green-400">
              $
            </span>

            <span className="text-green-600 group-hover:text-green-400 group-hover:translate-x-1 transition-transform">
              {item.name}
            </span>
          </a>
        ))}
      </nav>

      <div className="mt-auto pt-4 border-t border-green-900/30">
        <div className="flex justify-between text-[10px] text-green-900">
          <span>Giovanni Donati</span>
        </div>
      </div>
    </div>
  );
};

export default Sidebar;
