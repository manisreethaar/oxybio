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
        <section className="w-full py-12 bg-obsidian relative">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="border border-white/10 rounded-2xl bg-charcoal/40 overflow-hidden relative py-5 shadow-2xl">
                    <div className="absolute left-0 top-0 bottom-0 w-16 z-10 bg-gradient-to-r from-charcoal/80 to-transparent pointer-events-none" />
                    <div className="absolute right-0 top-0 bottom-0 w-16 z-10 bg-gradient-to-l from-charcoal/80 to-transparent pointer-events-none" />

                    <div className="flex w-[300%] sm:w-[200%] md:w-[150%]">
                        <motion.div
                            className="flex whitespace-nowrap items-center will-change-transform"
                            animate={{ x: ["0%", "-33.33%"] }}
                            transition={{
                                repeat: Infinity,
                                ease: "linear",
                                duration: 25}}
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
                </div>
            </div>
        </section>
    );
};

export default TrustBar;
