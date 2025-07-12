import { motion } from "framer-motion";
import {
  ArrowsRightLeftIcon,
  StarIcon,
  CheckBadgeIcon,
} from "@heroicons/react/24/outline";

export default function KeyFeatures() {
  const features = [
    {
      title: "Easy Skill Swapping",
      description: "Easily find and connect with others to swap skills and knowledge.",
      icon: <ArrowsRightLeftIcon className="w-8 h-8 text-[#0d151c]" />,
    },
    {
      title: "Community Ratings",
      description: "See ratings and reviews from other users to ensure quality and reliability.",
      icon: <StarIcon className="w-8 h-8 text-[#0d151c]" />,
    },
    {
      title: "Verified Experts",
      description: "Learn from verified experts in various fields.",
      icon: <CheckBadgeIcon className="w-8 h-8 text-[#0d151c]" />,
    },
  ];

  return (
    <div className="text-center bg-gray-50 px-4 py-16 mb-10">
      <h2 className="text-[#0d151c] text-[22px] font-bold leading-tight tracking-[-0.015em] pb-3">
        Key Features
      </h2>

      <div className="flex flex-col items-center gap-10">
        {/* Heading and Description */}
        <div className="flex flex-col items-center gap-4 max-w-2xl">
          <h1 className="text-[#0d151c] text-[28px] sm:text-[36px] font-bold sm:font-extrabold leading-tight tracking-tight">
            Unlock Your Potential
          </h1>
          <p className="text-[#0d151c] text-base font-normal leading-normal">
            Our platform offers a seamless experience for skill exchange, with community ratings and verified experts to ensure quality learning.
          </p>
        </div>

        {/* Features Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 w-full max-w-6xl">
          {features.map((feature, index) => (
            <motion.div
              key={index}
              className="flex flex-col items-center gap-3 rounded-xl border border-[#cedde8] bg-white shadow-md p-6 text-left"
              initial={{ opacity: 0, scale: 0.95 }}
              whileInView={{ opacity: 1, scale: 1 }}
              transition={{ duration: 0.5, delay: index * 0.2 }}
              viewport={{ once: true }}
            >
              <div>{feature.icon}</div>
              <div className="text-center">
                <h2 className="text-[#0d151c] text-base font-bold">{feature.title}</h2>
                <p className="text-[#49779c] text-sm">{feature.description}</p>
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </div>
  );
}
