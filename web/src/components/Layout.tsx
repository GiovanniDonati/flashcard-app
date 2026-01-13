import Sidebar from "./Sidebar";
import Card from "./Card";
import AddFlashcard from "./modal/AddFlashcard";
import { useEffect, useState } from "react";
import { FlashcardService } from "../service/FlashcardService";
import { Flashcard } from "../components/interface/Flashcard";

const Layout = () => {
  const [flashcards, setFlashcards] = useState<Flashcard[]>([]);
  const [isOpenModalFlashcard, setIsOpenModalFlashcard] = useState<boolean>(false);

  const loadData = () => {
    const data = FlashcardService().getFlashcards();
    setFlashcards(data);
  };

  useEffect(() => {
    loadData();
  }, [isOpenModalFlashcard]);

  return (
    <div className="flex w-full h-screen bg-[#0a0a0a] font-mono relative overflow-hidden">
      <Sidebar />
      <button
        className="absolute right-8 top-4 bg-green-500 hover:bg-green-600 text-black font-bold p-2 px-4 rounded-sm z-10"
        onClick={() => setIsOpenModalFlashcard(true)}
      >
        Add Flashcard
      </button>

      <div className="flex-1 overflow-y-auto p-10 mt-12 flex flex-col items-center">
        {flashcards.length > 0 ? (
          flashcards.map((card) => (
            <Card key={card.id} flashcard={card} />
          ))
        ) : (
          <p className="text-green-800 text-2xl mt-20">No flashcards found. Create one!</p>
        )}
      </div>

      {isOpenModalFlashcard && (
        <AddFlashcard setOpen={setIsOpenModalFlashcard} />
      )}
    </div>
  );
};

export default Layout;