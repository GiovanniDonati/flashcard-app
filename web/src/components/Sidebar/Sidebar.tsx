import {
  Home,
  LayoutList,
  LibraryBigIcon,
  Menu,
  Settings,
  UserCircle2,
  ChevronLeft,
} from "lucide-react";
import { useState } from "react";

const menu = [
  { name: "home", path: "/", icon: <Home size={20} /> },
  {
    name: "collections",
    path: "/collections",
    icon: <LibraryBigIcon size={20} />,
  },
  { name: "categories", path: "/categories", icon: <LayoutList size={20} /> },
  { name: "settings", path: "/settings", icon: <Settings size={20} /> },
];

const Sidebar = () => {
  const [isOpen, setIsOpen] = useState(true);

  return (
    <div
      className={`flex flex-col h-screen bg-black border-r border-green-900/50 p-4 font-mono transition-all duration-300 ${
        isOpen ? "w-64" : "w-20 items-center"
      }`}
    >
      <div className="flex items-center justify-between mb-8">
        {isOpen && (
          <div className="text-green-500 text-xl tracking-tighter font-semibold flex items-center overflow-hidden whitespace-nowrap">
            <span className="mr-2 text-green-800 font-black">{">"}</span>
            Flashcards
            <span className="ml-1 w-2 h-5 bg-green-500 animate-pulse"></span>
          </div>
        )}
        <button
          onClick={() => setIsOpen(!isOpen)}
          className="text-green-500 hover:bg-green-500/10 p-1 rounded transition-colors"
        >
          {isOpen ? <ChevronLeft /> : <Menu />}
        </button>
      </div>
      <nav className="space-y-2 flex-grow">
        {menu.map((item) => {
          const isActive = false;

          return (
            <a
              key={item.path}
              href={item.path}
              className={`group flex items-center px-3 py-2 rounded border transition-all duration-150 ${
                isActive
                  ? "border-green-500 bg-green-500/20 text-green-400"
                  : "border-transparent text-green-600 hover:border-green-500/30 hover:bg-green-500/10 hover:text-green-400"
              }`}
            >
              {!isOpen && <div className="mx-auto">{item.icon}</div>}
              {isOpen && (
                <>
                  <span className="text-green-800 mr-3 group-hover:text-green-400">
                    $
                  </span>
                  <span className="capitalize text-lg flex-grow group-hover:translate-x-1 transition-transform">
                    {item.name}
                  </span>
                </>
              )}

              {isOpen && (
                <span className="opacity-0 group-hover:opacity-100 text-[10px] text-green-800 transition-opacity">
                  [ENTER]
                </span>
              )}
            </a>
          );
        })}
      </nav>

      <div className="mt-auto pt-4 border-t border-green-900/30 overflow-hidden">
        <div
          className={`flex items-center gap-3 text-green-700 ${
            !isOpen && "justify-center"
          }`}
        >
          <UserCircle2 className="min-w-[24px]" />
          {isOpen && (
            <div className="flex flex-col">
              <span className="text-xs font-bold text-green-500 truncate">
                Giovanni Donati
              </span>
              <span className="text-[10px] uppercase tracking-tighter">
                Status: Online
              </span>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default Sidebar;
