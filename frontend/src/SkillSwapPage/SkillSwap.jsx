import { useState } from "react";

const users = [
  {
    name: "Sophia Clark",
    offers: "Graphic Design",
    needs: "Photography",
    image: "https://randomuser.me/api/portraits/women/75.jpg",
  },
  {
    name: "Ethan Bennett",
    offers: "Web Development",
    needs: "Spanish Lessons",
    image: "https://randomuser.me/api/portraits/men/52.jpg",
  },
  {
    name: "Olivia Carter",
    offers: "Photography",
    needs: "Yoga Instruction",
    image: "https://randomuser.me/api/portraits/women/68.jpg",
  },
  {
    name: "Liam Davis",
    offers: "Spanish Lessons",
    needs: "Cooking Classes",
    image: "https://randomuser.me/api/portraits/men/60.jpg",
  },
];

export default function SkillSwapPage() {
  const [offered, setOffered] = useState("");
  const [wanted, setWanted] = useState("");

  return (
    <div className="bg-[#e9eef2] min-h-screen py-10 px-4 sm:px-10">
      <div className="max-w-5xl mx-auto bg-white rounded-2xl p-6">
        <h1 className="text-2xl font-bold mb-6">Find Skill Swaps</h1>

        {/* Filters */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-8">
          <select
            className="border border-gray-300 rounded-md p-2 text-sm"
            value={offered}
            onChange={(e) => setOffered(e.target.value)}
          >
            <option value="">Skill Offered</option>
            <option value="Graphic Design">Graphic Design</option>
            <option value="Web Development">Web Development</option>
            <option value="Photography">Photography</option>
            <option value="Spanish Lessons">Spanish Lessons</option>
          </select>

          <select
            className="border border-gray-300 rounded-md p-2 text-sm"
            value={wanted}
            onChange={(e) => setWanted(e.target.value)}
          >
            <option value="">Skill Wanted</option>
            <option value="Photography">Photography</option>
            <option value="Spanish Lessons">Spanish Lessons</option>
            <option value="Yoga Instruction">Yoga Instruction</option>
            <option value="Cooking Classes">Cooking Classes</option>
          </select>
        </div>

        {/* User Cards */}
        <div className="space-y-4">
          {users
            .filter(
              (u) =>
                (!offered || u.offers === offered) &&
                (!wanted || u.needs === wanted)
            )
            .map((user, index) => (
              <div
                key={index}
                className="flex justify-between items-center border rounded-lg p-4 shadow-sm"
              >
                <div>
                  <p className="font-semibold text-[#0d151c]">{user.name}</p>
                  <p className="text-sm text-gray-600">
                    Offers: <span className="text-blue-600">{user.offers}</span>, Needs: <span className="text-blue-600">{user.needs}</span>
                  </p>
                  <button className="mt-2 text-sm px-3 py-1 rounded bg-gray-100 text-gray-700 hover:bg-gray-200">
                    Request
                  </button>
                </div>
                <img
                  src={user.image}
                  alt={user.name}
                  className="w-20 h-20 rounded-md object-cover"
                />
              </div>
            ))}
        </div>

        {/* Pagination */}
        <div className="flex justify-center mt-10">
          <div className="flex items-center space-x-2 text-sm">
            <button className="px-2">&#60;</button>
            {[1, 2, 3, 4, 5].map((num) => (
              <button
                key={num}
                className={`px-3 py-1 rounded-full ${num === 1 ? "bg-gray-800 text-white" : "bg-gray-200"}`}
              >
                {num}
              </button>
            ))}
            <button className="px-2">&#62;</button>
          </div>
        </div>
      </div>
    </div>
  );
}
