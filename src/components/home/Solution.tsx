import { motion } from 'framer-motion';
import { Beaker, Brain, Zap, Fingerprint } from 'lucide-react';

const Solution = () => {
    const products = [
        {
            id: "clarity",
            target: "Cognitive Focus and Neural Support",
            name: "Project CLARITY",
            status: "Phase 1 Planned",
            icon: <Brain className="w-6 h-6 text-white" />,
            tagline: "The Cognitive Protocol",
            benefits: [
                "Lion's Mane (Hericium erinaceus) hot-water extract",
                "Standardised for Hericenones and Erinacines",
                "Delivered on a fermented Ragi + Karuppu Kavuni base"
            ],
            ingredients: "Fermented Millet, Fermented Black Rice, Lion's Mane Extract, In-situ GABA",
            gradient: "from-cyan-900 to-cyan-500",
            featured: true
        },
        {
            id: "momentum",
            target: "Cellular Energy & Performance",
            name: "Project MOMENTUM",
            status: "Phase 1 Planned",
            icon: <Zap className="w-6 h-6 text-white" />,
            tagline: "The Physical Endurance Protocol",
            benefits: [
                "Cordyceps militaris hot-water extract",
                "Standardised for Cordycepin content",
                "Non-stimulant cellular oxygenation substrates"
            ],
            ingredients: "Fermented Millet, Fermented Black Rice, Cordyceps militaris Extract",
            gradient: "from-[#45A29E] to-[#1F2833]"
        },
        {
            id: "vitality",
            target: "Immune-Pathway Modulation",
            name: "Project VITALITY",
            status: "Phase 1 Planned",
            icon: <Fingerprint className="w-6 h-6 text-white" />,
            tagline: "The Immune-Resilience Protocol",
            benefits: [
                "Reishi (Ganoderma lucidum) hot-water extract",
                "Standardised for Beta-Glucan content",
                "Phytic-acid reduced formulation for optimal absorption"
            ],
            ingredients: "Fermented Millet, Fermented Black Rice, Reishi Extract",
            gradient: "from-[#1a2a6c] to-[#b21f1f]"
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

                    </div>
            </div>
        </section>
    );
};

export default Solution;
