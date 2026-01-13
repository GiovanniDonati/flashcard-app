import { Flashcard, FlashcardStatus } from "../components/interface/Flashcard";

const STORAGE_KEY = "@flashcards_data";

export const FlashcardService = () => {
  const getFlashcards = (): Flashcard[] => {
    const data = localStorage.getItem(STORAGE_KEY);
    return data ? JSON.parse(data) : [];
  };

  const addFlashcard = (flashcard: Flashcard) => {
    const list = getFlashcards();
    list.push(flashcard);
    localStorage.setItem(STORAGE_KEY, JSON.stringify(list));
  };

  const updateFlashcardStatus = (id: number, status: keyof FlashcardStatus) => {
    const list = getFlashcards();
    const index = list.findIndex((card) => card.id === id);
    if (index !== -1) {
      list[index].status = status;
      localStorage.setItem(STORAGE_KEY, JSON.stringify(list));
    }
  };

  const deleteFlashcard = (id: number) => {
    const list = getFlashcards();
    const newList = list.filter((card) => card.id !== id);
    localStorage.setItem(STORAGE_KEY, JSON.stringify(newList));
  };

  return {
    addFlashcard,
    getFlashcards,
    updateFlashcardStatus,
    deleteFlashcard,
  };
};