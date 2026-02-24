import { AlertCircle, EyeOff, Globe2 } from 'lucide-react';
import { motion } from 'framer-motion';

const Problem = () => {
    const stats = [
        { label: "Vitamin D Deficient", value: "73%", source: "ICMR National Nutrition Survey" },
        { label: "Skip ≥1 Meal/Day", value: "50%", source: "ASSOCHAM Health Survey" },
        { label: "Fail Label Claims", value: "68%", source: "CSE Report 2023" }
    ];

    const cards = [
        {
            icon: <AlertCircle className="w-8 h-8 text-cyan-ethereal mb-4" />,
            title: "No time for real nutrition",
            description: "The average working professional has 22 minutes for lunch, often at their desk. Students skip meals before exams. Athletes eat whatever is convenient after training. The food system was not designed for how Indians actually live."
        },
        {
            icon: <EyeOff className="w-8 h-8 text-cyan-ethereal mb-4" />,
            title: "Existing products deceive you",
            description: "Most Indian health drinks are primarily sugar with token doses of vitamins your body cannot absorb. Cheap synthetic forms, under-dosed actives, misleading labels. The same brand sells better formulas in foreign markets. You deserve to know this."
        },
        {
            icon: <Globe2 className="w-8 h-8 text-cyan-ethereal mb-4" />,
            title: "Imported solutions do not fit India",
            description: "Products designed for Western nutritional deficiencies miss what Indian bodies need. They do not understand Ragi, Moringa, or Ashwagandha. They do not understand how Indians eat, work, or train. India needs an Indian solution."
        }
    ];

    return (
        <section id="problem" className="w-full py-20 md:py-32 relative bg-obsidian">
            {/* Subtle Background Elements */}
            <div className="absolute top-0 right-0 w-[500px] h-[500px] bg-cyan-seafoam/5 rounded-full blur-[100px] pointer-events-none" />

            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">

                {/* Header Section */}
                <div className="text-center md:text-left mb-20 max-w-3xl">
                    <motion.h2
                        initial={{ opacity: 0, y: 20 }}
                        whileInView={{ opacity: 1, y: 0 }}
                        viewport={{ once: true}}
                        transition={{ duration: 0.5, ease: [0.22, 1, 0.36, 1] }}
                        className="text-3xl md:text-5xl font-heading font-extrabold text-white mb-6"
                    >
                        You are probably <span className="text-transparent bg-clip-text bg-gradient-to-r from-red-400 to-orange-400">nutritionally deficient.</span>
                    </motion.h2>
                    <motion.p
                        initial={{ opacity: 0, y: 20 }}
                        whileInView={{ opacity: 1, y: 0 }}
                        viewport={{ once: true}}
                        transition={{ duration: 0.5, delay: 0.1, ease: [0.22, 1, 0.36, 1] }}
                        className="text-lg text-slate-ash leading-relaxed"
                    >
                        Not because you are careless. Because modern Indian life makes proper nutrition almost impossible.
                    </motion.p>
                </div>

                {/* Big Stats Row */}
                <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-20">
                    {stats.map((stat, i) => (
                        <motion.div
                            initial={{ opacity: 0, y: 20 }}
                            whileInView={{ opacity: 1, y: 0 }}
                            viewport={{ once: true}}
                            transition={{ duration: 0.5, delay: i * 0.1, ease: [0.22, 1, 0.36, 1] }}
                            key={i}
                            className="border-l-2 border-cyan-ethereal/50 pl-6 py-2"
                        >
                            <div className="text-5xl font-heading font-bold text-white mb-2">{stat.value}</div>
                            <div className="text-lg font-medium text-cyan-seafoam mb-1">{stat.label}</div>
                            <div className="text-xs text-slate-ash/60">Source: {stat.source}</div>
                        </motion.div>
                    ))}
                </div>

                {/* 3 Problems Cards */}
                <div className="grid grid-cols-1 md:grid-cols-3 gap-6 lg:gap-8">
                    {cards.map((card, i) => (
                        <motion.div
                            initial={{ opacity: 0, y: 20 }}
                            whileInView={{ opacity: 1, y: 0 }}
                            viewport={{ once: true}}
                            transition={{ duration: 0.5, delay: 0.2 + (i * 0.1), ease: [0.22, 1, 0.36, 1] }}
                            key={i}
                            className="glass-card p-8 group hover:bg-charcoal transition-colors duration-300"
                        >
                            <div className="bg-obsidian w-16 h-16 rounded-xl flex items-center justify-center mb-6 shadow-inner border border-white/5 group-hover:border-cyan-ethereal/30 transition-colors">
                                {card.icon}
                            </div>
                            <h3 className="text-2xl font-heading font-bold text-white mb-4">{card.title}</h3>
                            <p className="text-slate-ash/90 leading-relaxed text-sm md:text-base">
                                {card.description}
                            </p>
                        </motion.div>
                    ))}
                </div>

            </div>
        </section>
    );
};

export default Problem;
