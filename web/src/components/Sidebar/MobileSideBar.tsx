import {
  Home,
  LayoutList,
  LibraryBigIcon,
  Settings,
  UserCircle2,
} from "lucide-react";

const menu = [
  {
    name: "collections",
    path: "/collections",
    icon: <LibraryBigIcon size={20} />,
  },
  { name: "categories", path: "/categories", icon: <LayoutList size={20} /> },
  { name: "home", path: "/", icon: <Home size={20} /> },
  { name: "settings", path: "/settings", icon: <Settings size={20} /> },
];

const MobileSidebar = () => {
  const currentPath = "/";

  return (
    <div className="fixed bottom-0 left-0 z-50 w-full h-16 bg-black/90 backdrop-blur-md border-t border-green-900/50 px-4 font-mono">
      <nav className="flex h-full items-center justify-between">
        {menu.map((item) => {
          const isActive = currentPath === item.path;

          return (
            <a
              key={item.path}
              href={item.path}
              className={`flex flex-col items-center justify-center flex-1 py-1 transition-all duration-200 ${
                isActive
                  ? "text-green-400 bg-green-500/10 rounded-sm border-green-500 border-x border-green-500"
                  : "text-green-700 hover:text-green-500 border-green-500"
              }`}
            >
              <div className={`p-1 rounded-lg transition-colors`}>
                {item.icon}
              </div>
              <span className="text-[10px] uppercase mt-1 font-bold">
                {item.name}
              </span>
            </a>
          );
        })}

        <div className="flex flex-col items-center justify-center flex-1 text-green-700">
          <UserCircle2 size={20} />
          <span className="text-[10px] uppercase mt-1 font-bold">Profile</span>
        </div>
      </nav>
    </div>
  );
};

export default MobileSidebar;
