import { useEffect, useState } from "react";
import { FlashcardService } from "../../service/FlashcardService";

const AddFlashcard = ({ setOpen }: { setOpen: (open: boolean) => void }) => {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const addflash = () => {
    FlashcardService().addFlashcard({
      id: FlashcardService().getFlashcards().length + 1,
      question,
      answer,
      status: "Average"
    });
    setQuestion("");
    setAnswer("");
  };

  useEffect(() => {
    console.log(FlashcardService().getFlashcards());
  }, []);

  return (
    <div className="flex absolute p-4 items-center justify-center w-full h-full bg-black/60 top-0 left-0 backdrop-blur-sm z-50">
      <div className="bg-[#0d140d] p-8 min-w-[400px] border border-green-500/30 rounded-sm shadow-[0_0_30px_rgba(34,197,94,0.15)] relative overflow-hidden">
        <form
          className="flex flex-col gap-5"
          onSubmit={(e) => {
            e.preventDefault();
            addflash();
            setOpen(false);
          }}
        >
          <h1 className="text-green-500 text-xl font-bold tracking-widest uppercase mb-2">
            Add Flashcard
          </h1>

          <div className="flex flex-col gap-2">
            <label className="text-green-700 text-xs font-semibold uppercase tracking-tighter">
              Question:
            </label>
            <input
              className="bg-black/40 border border-green-900 text-green-100 p-2 rounded-sm focus:outline-none focus:border-green-500 transition-colors placeholder:text-green-900/50"
              type="text"
              placeholder="Enter the question..."
              name="question"
              value={question}
              onChange={(e) => setQuestion(e.target.value)}
            />
          </div>

          <div className="flex flex-col gap-2">
            <label className="text-green-700 text-xs font-semibold uppercase tracking-tighter">
              Answer:
            </label>
            <input
              className="bg-black/40 border border-green-900 text-green-100 p-2 rounded-sm focus:outline-none focus:border-green-500 transition-colors placeholder:text-green-900/50"
              type="text"
              placeholder="Enter the answer..."
              name="answer"
              value={answer}
              onChange={(e) => setAnswer(e.target.value)}
            />
          </div>

          <div className="flex justify-between items-center w-full gap-2">
            <button
              type="button"
              onClick={() => setOpen(false)}
              className="w-full mt-2 bg-green-600/10 border border-green-500 text-green-500 py-2 font-bold uppercase hover:bg-green-500 hover:text-black transition-all duration-300 cursor-pointer"
            >
              Cancel
            </button>
            <button
              type="submit"
              className="w-full mt-2 bg-green-600/10 border border-green-500 text-green-500 py-2 font-bold uppercase hover:bg-green-500 hover:text-black transition-all duration-300 cursor-pointer"
            >
              Add Flashcard
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default AddFlashcard;