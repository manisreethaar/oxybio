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
                    <div
                        
                        
                        
                        className="inline-flex items-center justify-center w-16 h-16 rounded-2xl bg-charcoal border border-white/10 mb-6 shadow-[0_0_30px_rgba(102,252,241,0.15)]"
                    >
                        <Beaker className="w-8 h-8 text-cyan-ethereal" />
                    </div>
                    <motion.h2
                        
                        
                        
                        className="text-3xl md:text-5xl font-heading font-extrabold text-white mb-6"
                    >
                        So we built one. Meet <span className="text-cyan-ethereal">Oxygen.</span>
                    </motion.h2>
                    <motion.p
                        
                        
                        
                        
                        className="text-lg text-slate-ash leading-relaxed max-w-3xl mx-auto"
                    >
                        Three precision formulas. Each scientifically designed for a specific need. All built on the same uncompromising foundation: Indian ingredients, active nutrient forms, and doses that actually work.
                    </motion.p>
                </div>

                {/* Product Cards Grid - Vertically stacked on mobile, 3-col on desktop */}
                <div className="flex flex-col gap-12 mt-12">
                    {products.map((product, i) => (
                        <div
                            
                            
                            
                            
                            key={i}
                            className="bg-obsidian border-t-2 border-white pt-8 flex flex-col gap-6"
                        >
                            {/* Header Box */}
                            <div className="flex justify-between items-start flex-wrap gap-4">
                                <div>
                                    <div className="font-mono text-sm text-slate-ash/70 tracking-[0.1em] uppercase mb-2">
                                        0{i + 1} // {product.status}
                                    </div>
                                    <h3 className="font-heading font-bold text-5xl md:text-6xl text-white leading-none m-0">
                                        {product.name.replace('Project ', '')}
                                    </h3>
                                    <div className="font-semibold text-lg mt-2 text-white">
                                        {product.target}
                                    </div>
                                </div>
                            </div>

                            {/* Content Grid */}
                            <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
                                <div>
                                    <p className="text-xl leading-relaxed text-slate-ash/90 mb-6 font-medium">
                                        {product.tagline}
                                    </p>
                                    <ul className="space-y-4">
                                        {product.benefits.map((benefit, j) => (
                                            <li key={j} className="flex items-start text-base text-white font-medium">
                                                <span className="text-white mr-3 block mt-0.5 opacity-70">→</span>
                                                <span>{benefit}</span>
                                            </li>
                                        ))}
                                    </ul>
                                </div>

                                {/* Ingredients Box */}
                                <div className="bg-charcoal/40 p-8 rounded-2xl border border-white/10 flex flex-col justify-center">
                                    <div className="font-mono text-sm text-slate-ash/70 tracking-[0.05em] mb-4 uppercase">
                                        Formulation Stack
                                    </div>
                                    <p className="text-lg font-semibold leading-relaxed text-white m-0 tracking-tight">
                                        {product.ingredients}
                                    </p>
                                </div>
                            </div>
                        </div>
                    ))}

                    {/* Coming Soon Protein Bar */}
                    <div
                        
                        
                        
                        
                        className="bg-white text-obsidian rounded-[2rem] flex flex-col justify-center items-center text-center p-16 mt-4 shadow-2xl premium-transition hover:transform hover:scale-[1.01]"
                    >
                        <div className="absolute top-0 right-0 w-64 h-64 bg-cyan-ethereal/5 rounded-full blur-sm" />
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
                    </div>

                </div>
            </div>
        </section>
    );
};

export default Solution;
