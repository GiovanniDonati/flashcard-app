import Sidebar from "./Sidebar/Sidebar";
import MobileSidebar from "./Sidebar/MobileSideBar";
import Card from "./Card";
import AddFlashcard from "./modal/AddFlashcard";
import { useEffect, useState } from "react";
import { FlashcardService } from "../service/FlashcardService";
import { Flashcard } from "../components/interface/Flashcard";

const mobile = window.innerWidth <= 480;

const Layout = () => {
  const [flashcards, setFlashcards] = useState<Flashcard[]>([]);
  const [isOpenModalFlashcard, setIsOpenModalFlashcard] =
    useState<boolean>(false);

  const loadData = () => {
    const data = FlashcardService().getFlashcards();
    setFlashcards(data);
  };

  useEffect(() => {
    loadData();
  }, [isOpenModalFlashcard]);

  return (
    <div className="sm:flex w-full h-screen bg-[#0a0a0a] font-mono">
      {mobile ? <MobileSidebar /> : <Sidebar />}
      <div className={`p-10 flex-1 flex items-center justify-center`}>
        <button
          className="fixed max-sm:bottom-20 sm:bottom-6 right-6 bg-green-600 text-green-900 font-bold px-4 py-2 rounded-full shadow-lg hover:bg-green-500 z-10"
          onClick={() => setIsOpenModalFlashcard(true)}
        >
          +
        </button>
        <Card flashcard={flashcards[0]} />
      </div>

      {isOpenModalFlashcard && (
        <AddFlashcard setOpen={setIsOpenModalFlashcard} />
      )}
    </div>
  );
};

export default Layout;
