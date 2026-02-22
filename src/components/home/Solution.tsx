import { motion } from 'framer-motion';
import { Beaker, Brain, Zap, Fingerprint } from 'lucide-react';

const Solution = () => {
    const products = [
        {
            id: "vitality",
            target: "Daily Deficiencies",
            name: "Project VITALITY",
            status: "Pre-Clinical Optimization",
            icon: <Fingerprint className="w-6 h-6 text-white" />,
            tagline: "For when you cannot eat well but refuse to function sub-optimally. An everyday nutritional baseline.",
            benefits: [
                "Covers 50% of your daily nutrient needs",
                "Sustained energy without sugar spikes",
                "Stress adaptation with KSM-66 Ashwagandha"
            ],
            ingredients: "Finger Millet, Ashwagandha KSM-66, Lion's Mane, Moringa, 22 Chelated Nutrients",
            gradient: "from-[#1a2a6c] to-[#b21f1f]" // Deep blue to red core
        },
        {
            id: "clarity",
            target: "Cognitive Fatigue",
            name: "Project CLARITY",
            status: "Sensory Trials & Taste Profiling",
            icon: <Brain className="w-6 h-6 text-white" />,
            tagline: "The honest alternative to high-sugar energy drinks. Built for sustained focus and the dreaded 3PM crash.",
            benefits: [
                "Clean focus without caffeine crash",
                "Memory and attention support (Lion's Mane)",
                "L-Theanine:Caffeine ratio 2.5:1 (clinically studied)"
            ],
            ingredients: "Lion's Mane, Bacopa Monnieri, L-Theanine, Natural Caffeine, Active B Vitamins",
            gradient: "from-cyan-900 to-cyan-500", // Ethereal cyan core
            featured: true
        },
        {
            id: "momentum",
            target: "Cellular Recovery",
            name: "Project MOMENTUM",
            status: "Formulation Finalized",
            icon: <Zap className="w-6 h-6 text-white" />,
            tagline: "An athletic recovery matrix built around ATP production and true muscle repair, rather than synthetic stimulation.",
            benefits: [
                "Faster muscle recovery (Kokum + Tart Cherry)",
                "ATP production support (Cordyceps militaris)",
                "Strength and endurance (Creatine HCl + Citrulline)"
            ],
            ingredients: "Cordyceps, Creatine HCl, Kokum Extract, L-Citrulline, Electrolytes",
            gradient: "from-[#45A29E] to-[#1F2833]" // Seafoam green to dark
        }
    ];

    return (
        <section id="products" className="w-full py-20 md:py-32 bg-[#08090C] relative">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">

                {/* Header */}
                <div className="text-center mb-20">
                    <motion.div
                        initial={{ opacity: 0, scale: 0.9 }}
                        whileInView={{ opacity: 1, scale: 1 }}
                        viewport={{ once: true }}
                        className="inline-flex items-center justify-center w-16 h-16 rounded-2xl bg-charcoal border border-white/10 mb-6 shadow-[0_0_30px_rgba(102,252,241,0.15)]"
                    >
                        <Beaker className="w-8 h-8 text-cyan-ethereal" />
                    </motion.div>
                    <motion.h2
                        initial={{ opacity: 0, y: 20 }}
                        whileInView={{ opacity: 1, y: 0 }}
                        viewport={{ once: true }}
                        className="text-3xl md:text-5xl font-heading font-extrabold text-white mb-6"
                    >
                        So we built one. Meet <span className="text-cyan-ethereal">Oxygen.</span>
                    </motion.h2>
                    <motion.p
                        initial={{ opacity: 0, y: 20 }}
                        whileInView={{ opacity: 1, y: 0 }}
                        viewport={{ once: true }}
                        transition={{ delay: 0.1 }}
                        className="text-lg text-slate-ash leading-relaxed max-w-3xl mx-auto"
                    >
                        Three precision formulas. Each scientifically designed for a specific need. All built on the same uncompromising foundation: Indian ingredients, active nutrient forms, and doses that actually work.
                    </motion.p>
                </div>

                {/* Product Cards Grid - Vertically stacked on mobile, 3-col on desktop */}
                <div className="grid grid-cols-1 lg:grid-cols-3 gap-8 mb-20">
                    {products.map((product, i) => (
                        <motion.div
                            initial={{ opacity: 0, y: 30 }}
                            whileInView={{ opacity: 1, y: 0 }}
                            viewport={{ once: true, margin: "-50px" }}
                            transition={{ delay: i * 0.15 }}
                            key={product.id}
                            className={`relative group rounded-3xl overflow-hidden glass-card transition-all duration-500 hover:-translate-y-2 ${product.featured ? 'border-cyan-ethereal/40 shadow-[0_0_40px_rgba(102,252,241,0.1)]' : 'border-white/5'}`}
                        >
                            {/* Product Card Glow Background */}
                            <div className={`absolute top-0 inset-x-0 h-40 bg-gradient-to-b ${product.gradient} opacity-20 group-hover:opacity-40 transition-opacity duration-500`} />

                            <div className="p-8 relative z-10 flex flex-col h-full">
                                <div className="flex justify-between items-start mb-6">
                                    <div className={`p-3 rounded-xl bg-obsidian border border-white/10 shadow-lg`}>
                                        {product.icon}
                                    </div>
                                    <span className="text-xs font-bold uppercase tracking-wider text-cyan-ethereal bg-cyan-ethereal/10 px-3 py-1 rounded-full">
                                        {product.target}
                                    </span>
                                </div>

                                <h3 className="text-2xl font-heading font-bold text-white mb-2">{product.name}</h3>

                                <div className="mb-4">
                                    <span className="text-[10px] uppercase tracking-widest text-slate-ash/50 font-bold block mb-1">Status</span>
                                    <div className="text-sm font-medium text-white/80 bg-white/5 inline-block px-2 py-1 rounded border border-white/5">
                                        {product.status}
                                    </div>
                                </div>

                                <p className="text-slate-ash text-sm leading-relaxed mb-6 font-medium">
                                    "{product.tagline}"
                                </p>

                                <div className="flex-grow">
                                    <span className="text-[10px] uppercase tracking-widest text-slate-ash/50 font-bold block mb-3">Key Benefits</span>
                                    <ul className="space-y-2 mb-6">
                                        {product.benefits.map((benefit, j) => (
                                            <li key={j} className="flex items-start text-sm text-slate-ash">
                                                <span className="text-cyan-seafoam mr-2 block mt-0.5">•</span>
                                                <span>{benefit}</span>
                                            </li>
                                        ))}
                                    </ul>
                                </div>

                                <div className="pt-6 border-t border-white/10 mt-auto">
                                    <span className="text-[10px] uppercase tracking-widest text-slate-ash/50 font-bold block mb-2">Core Stack</span>
                                    <p className="text-xs text-white/70 leading-relaxed font-medium">
                                        {product.ingredients}
                                    </p>
                                </div>
                            </div>
                        </motion.div>
                    ))}
                </div>

                {/* Sneak Peek / Coming Soon Bar */}
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    className="w-full bg-charcoal border border-white/10 rounded-2xl p-6 md:p-8 flex flex-col md:flex-row items-center justify-between gap-6 overflow-hidden relative"
                >
                    <div className="absolute top-0 right-0 w-64 h-64 bg-cyan-ethereal/5 rounded-full blur-[80px]" />
                    <div className="relative z-10 flex-1">
                        <div className="inline-block px-3 py-1 bg-white/5 border border-white/10 rounded-full text-xs font-bold tracking-wider text-cyan-seafoam mb-4">
                            COMING SOON
                        </div>
                        <h4 className="text-xl font-heading font-bold text-white mb-2">The Honest Protein Bar</h4>
                        <p className="text-slate-ash text-sm leading-relaxed mb-4 md:mb-0 max-w-2xl">
                            Real dates, real cashews, real pumpkin seeds. 300mg KSM-66 Ashwagandha in every bar. No fake protein. No compound chocolate. Coming alongside our drink range.
                        </p>
                    </div>
                    <div className="relative z-10 w-full md:w-auto flex flex-wrap gap-2 text-xs font-medium text-white/60">
                        <span className="bg-obsidian px-3 py-1.5 rounded-lg border border-white/5">Dates</span>
                        <span className="bg-obsidian px-3 py-1.5 rounded-lg border border-white/5">Cashews</span>
                        <span className="bg-obsidian px-3 py-1.5 rounded-lg border border-white/5">Ashwagandha</span>
                        <span className="bg-obsidian px-3 py-1.5 rounded-lg border border-white/5">Whey Isolate</span>
                    </div>
                </motion.div>

            </div>
        </section>
    );
};

export default Solution;
