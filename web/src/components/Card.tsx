const Card = () => {
  return (
    <div className="bg-[#0d140d] p-8 pb-4 min-w-[500px] border border-green-500/30 rounded-sm shadow-[0_0_20px_rgba(34,197,94,0.1)] relative overflow-hidden">
      <div className="absolute top-0 left-0 w-full h-6 bg-green-900/20 border-b border-green-500/20 flex items-center px-2 py-4 gap-1">
        <div className="w-2 h-2 rounded-full bg-green-900"></div>
        <div className="w-2 h-2 rounded-full bg-green-900"></div>
        <h1 className=" p-2 font-mono text-green-400 drop-shadow-[0_0_5px_rgba(74,222,128,0.5)]">
          Java Collection
        </h1>
      </div>
      <div>
        <p className="text-green-900 pt-2 tracking-tighter">
          How the command to build a project in Java?
        </p>
        <div className="flex justify-end">
          <button className="text-green-800 font-semibold mt-4 bg-green-500 p-2 py-1">
            [ See Details ]
          </button>
        </div>
      </div>
    </div>
  );
};

export default Card;
