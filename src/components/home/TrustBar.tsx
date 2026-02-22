import { motion } from 'framer-motion';

const TrustBar = () => {
    const items = [
        "TBI Incubated Startup",
        "Science-First Formulation",
        "FSSAI Licensing In Progress",
        "100% Indian Ingredients",
        "Third-Party Testing Planned",
        "Zero Artificial Ingredients",
        "Clinical Study Protocol Ready",
        "Peer-Reviewed Formulation"
    ];

    // Duplicate items for seamless continuous scrolling
    const scrollItems = [...items, ...items, ...items];

    return (
        <section className="w-full py-8 border-y border-white/5 bg-obsidian/50 overflow-hidden relative">
            <div className="absolute left-0 top-0 bottom-0 w-24 z-10 bg-gradient-to-r from-obsidian to-transparent" />
            <div className="absolute right-0 top-0 bottom-0 w-24 z-10 bg-gradient-to-l from-obsidian to-transparent" />

            <div className="flex w-[300%] sm:w-[200%] md:w-[150%]">
                <motion.div
                    className="flex whitespace-nowrap items-center"
                    animate={{ x: ["0%", "-33.33%"] }}
                    transition={{
                        repeat: Infinity,
                        ease: "linear",
                        duration: 25,
                    }}
                >
                    {scrollItems.map((item, index) => (
                        <div
                            key={index}
                            className="flex items-center mx-8 group"
                        >
                            <span className="w-1.5 h-1.5 rounded-full bg-cyan-ethereal/50 mr-4" />
                            <span className="text-sm md:text-base font-semibold text-slate-ash/70 tracking-wider uppercase">
                                {item}
                            </span>
                        </div>
                    ))}
                </motion.div>
            </div>
        </section>
    );
};

export default TrustBar;
