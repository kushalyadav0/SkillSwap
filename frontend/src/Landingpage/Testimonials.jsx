import { useEffect, useState } from "react";
import { motion } from "framer-motion";

// Dummy API simulation
const fetchTestimonials = () =>
  new Promise((resolve) =>
    setTimeout(() => {
      resolve([
        {
          name: "Sarah M.",
          message:
            "I learned how to code from a fellow user and now I'm building my own website!",
          rating: 5,
        },
        {
          name: "David L.",
          message:
            "SkillSwap helped me find a language partner and I'm now fluent in Spanish.",
          rating: 4,
        },
        {
          name: "Emily R.",
          message:
            "I've been able to share my photography skills and help others pursue their passions.",
          rating: 5,
        }, {
          name: "David L.",
          message:
            "SkillSwap helped me find a language partner and I'm now fluent in Spanish.",
          rating: 4,
        },
        
      ]);
    }, 1000)
  );

const StarRating = ({ count }) => {
  return (
    <div className="flex gap-1 text-yellow-400 bg-gray-50 ">
      {Array(5)
        .fill()
        .map((_, idx) =>
          idx < count ? (
            <svg key={idx} className="w-4 h-4 fill-yellow-400" viewBox="0 0 24 24">
              <path d="M12 17.27L18.18 21 16.54 13.97 22 9.24 14.82 8.63 12 2 9.18 8.63 2 9.24 7.46 13.97 5.82 21z" />
            </svg>
          ) : (
            <svg key={idx} className="w-4 h-4 fill-gray-300" viewBox="0 0 24 24">
              <path d="M12 17.27L18.18 21 16.54 13.97 22 9.24 14.82 8.63 12 2 9.18 8.63 2 9.24 7.46 13.97 5.82 21z" />
            </svg>
          )
        )}
    </div>
  );
};

export default function Testimonials() {
  const [testimonials, setTestimonials] = useState([]);

  useEffect(() => {
    fetchTestimonials().then((data) => setTestimonials(data));
  }, []);

  return (
    <section className="bg-gray-50 mb-10">
      <h2 className="text-[#0d151c] text-[22px] font-bold tracking-tight mb-6 text-center">
        What Our Users Say
      </h2>

      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6 justify-center px-4">

        {testimonials.map((t, idx) => (
         <motion.div
  key={idx}
  initial={{ opacity: 0, y: 40 }}
  animate={{ opacity: 1, y: 0 }}
  transition={{ delay: idx * 0.2 }}
  className="w-full max-w-xs h-[300px] bg-white shadow-md rounded-xl p-4 flex flex-col justify-between gap-2"
>

            <div className="h-28 bg-gray-200 rounded-md" />
            <div className="flex flex-col gap-1">
              <p className="text-[#0d151c] font-semibold">{t.name}</p>
              <p className="text-[#49779c] text-sm">{t.message}</p>
              <StarRating count={t.rating} />
            </div>
          </motion.div>
        ))}
      </div>
    </section>
  );
}
