export interface FlashcardStatus {
  Good: string;
  Average: string;
  Poor: string;
}

export interface Flashcard {
  id: number;
  question: string;
  answer: string;
  status: keyof FlashcardStatus;
}
