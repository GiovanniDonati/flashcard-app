import { useState } from "react";
import { Flashcard } from "./interface/Flashcard";

interface CardProps {
  flashcard: Flashcard;
}

const Card = ({ flashcard }: CardProps) => {
  const [turnOn, setTurnOn] = useState(false);

  return (
    <div className="space-y-2 mb-6">
      <div className="bg-[#0d140d] p-8 pb-4 min-w-[800px] border border-green-500/30 rounded-sm shadow-[0_0_20px_rgba(34,197,94,0.1)] relative overflow-hidden">
        <div className="absolute top-0 left-0 w-full h-6 bg-green-900/20 border-b border-green-500/20 flex items-center px-2 py-4 gap-1">
          <div className="w-3 h-3 rounded-full bg-green-900"></div>
          <div className="w-3 h-3 rounded-full bg-green-900"></div>
          <h1 className="p-2 font-mono text-xl text-green-400 drop-shadow-[0_0_5px_rgba(74,222,128,0.5)]">
            Flashcard #{flashcard.id}
          </h1>
        </div>
        <div>
          <p className="text-green-600 pt-4 tracking-tighter text-lg">
            {flashcard.question}
          </p>
          <div className="flex justify-end">
            <button
              onClick={() => setTurnOn(!turnOn)}
              className={`font-semibold mt-4 border p-2 py-1 text-green-600 border-green-600 bg-[#0d140d] ${turnOn && "bg-green-500 border-green-500 text-green-900"
                }`}
            >
              [ {turnOn ? "Hide Details" : "See Details"} ]
            </button>
          </div>
        </div>
      </div>

      {turnOn && (
        <div className="bg-[#0d140d] p-2 min-w-[500px] border border-green-500/30 rounded-sm shadow-[0_0_20px_rgba(34,197,94,0.1)] relative overflow-hidden">
          <div className="flex flex-col">
            <h1 className="p-2 mb-2 font-mono text-green-600 text-md">
              {flashcard.answer}
            </h1>
            <div className="flex justify-between space-x-2 shadow-[0_0_20px_rgba(34,197,94,0.1)] relative">
              <button className="hover:bg-red-500 hover:text-white font-semibold w-full p-2 font-mono text-green-600 border border-green-600">
                Poor
              </button>
              <button className="hover:bg-yellow-500 hover:text-black font-semibold w-full p-2 font-mono text-green-600 border border-green-600">
                Average
              </button>
              <button className="hover:bg-green-500 hover:text-green-800 font-semibold w-full p-2 font-mono text-green-600 border border-green-600">
                Good
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default Card;