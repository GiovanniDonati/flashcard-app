import Sidebar from "./Sidebar";
import Card from "./Card";

const Layout = () => {
  return (
    <div className="flex w-full h-screen bg-[#0a0a0a] font-mono">
      <Sidebar />
      <div className="flex-1 flex items-center justify-center p-10">
        <Card />
      </div>
    </div>
  );
};

export default Layout;
