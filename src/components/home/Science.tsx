import { motion } from 'framer-motion';
import { Microscope, ShieldCheck, Activity, Check, X } from 'lucide-react';

const Science = () => {
    const pillars = [
        {
            icon: <Activity className="w-8 h-8 text-cyan-ethereal" />,
            title: "Active forms only",
            description: "Most products use the cheapest permitted form. We use: Methylcobalamin, Pyridoxal-5-Phosphate, 5-MTHF Folate, Albion TRAACS® Minerals.",
            highlight: "The difference: 3-4x better absorption."
        },
        {
            icon: <ShieldCheck className="w-8 h-8 text-cyan-ethereal" />,
            title: "Verified, not assumed",
            description: "Our Lion's Mane extract is verified at minimum 30% β-glucan content using the Megazyme AOAC method — the gold standard.",
            highlight: "Verified active compound content. Non-negotiable."
        },
        {
            icon: <Microscope className="w-8 h-8 text-cyan-ethereal" />,
            title: "Proving it, not just claiming it",
            description: "We have designed a clinical study for 135 participants across 8 weeks. Primary outcomes: Biomarkers + cognitive tests.",
            highlight: "Results will be published. Regardless of outcome."
        }
    ];

    const comparisons = [
        { label: "Vitamin B12", us: "Methylcobalamin (Active)", them: "Cyanocobalamin (Synthetic)" },
        { label: "Minerals", us: "Chelated (TRAACS®)", them: "Oxide/Sulfate forms" },
        { label: "Mushroom extracts", us: "Verified β-glucan", them: "Unverified weight" },
        { label: "Lab reports", us: "Public CoA", them: "No transparency" },
        { label: "Efficacy data", us: "Clinical study", them: "No efficacy data" },
        { label: "Suppliers", us: "Named sources", them: "Anonymous suppliers" }
    ];

    return (
        <section id="science" className="w-full py-20 md:py-32 bg-obsidian relative overflow-hidden">
            {/* Background Tech Lines */}
            <div className="absolute inset-0 opacity-5 pointer-events-none"
                style={{ backgroundImage: 'linear-gradient(rgba(255, 255, 255, 0.1) 1px, transparent 1px), linear-gradient(90deg, rgba(255, 255, 255, 0.1) 1px, transparent 1px)', backgroundSize: '40px 40px' }}
            />

            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">

                {/* Header */}
                <div className="text-center mb-20">
                    <motion.h2
                        
                        
                        
                        className="text-4xl md:text-6xl font-heading font-extrabold text-white mb-6"
                    >
                        We show our <span className="text-transparent bg-clip-text bg-gradient-to-r from-cyan-seafoam to-cyan-ethereal">work.</span>
                    </motion.h2>
                    <motion.p
                        
                        
                        
                        
                        className="text-lg md:text-xl text-slate-ash leading-relaxed max-w-3xl mx-auto"
                    >
                        Every formulation decision has a peer-reviewed reason. Every ingredient has a verified source. Every claim is something we can prove.
                    </motion.p>
                </div>

                {/* 3 Pillars Grid */}
                <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-24">
                    {pillars.map((pillar, i) => (
                        <div
                            
                            
                            
                            
                            key={i}
                            className="bg-charcoal/40 border border-white/5 p-8 rounded-3xl hover:border-cyan-ethereal/30 transition-colors"
                        >
                            <div className="bg-obsidian w-16 h-16 rounded-xl flex items-center justify-center mb-6 shadow-lg border border-white/5">
                                {pillar.icon}
                            </div>
                            <h3 className="text-2xl font-heading font-bold text-white mb-4">{pillar.title}</h3>
                            <p className="text-slate-ash leading-relaxed mb-6 block min-h-[100px]">
                                {pillar.description}
                            </p>
                            <div className="bg-cyan-ethereal/10 border border-cyan-ethereal/20 text-cyan-ethereal px-4 py-3 rounded-lg text-sm font-semibold">
                                {pillar.highlight}
                            </div>
                        </div>
                    ))}
                </div>

                {/* Data Comparison Section */}
                <div
                    
                    
                    
                    
                    className="bg-charcoal rounded-3xl border border-white/10 overflow-hidden shadow-2xl"
                >
                    {/* Top Banner highlight */}
                    <div className="bg-gradient-to-r from-cyan-seafoam/20 to-cyan-ethereal/20 border-b border-white/10 p-6 md:p-8 flex flex-col md:flex-row items-center justify-between gap-6">
                        <div>
                            <h4 className="text-2xl font-heading font-bold text-white mb-2">Absorption Difference</h4>
                            <p className="text-slate-ash text-sm">Standard mineral form (Oxide/Sulfate) = 8%</p>
                        </div>
                        <div className="text-right">
                            <div className="text-4xl font-heading font-extrabold text-cyan-ethereal mb-1">28%</div>
                            <p className="text-cyan-seafoam/80 text-sm font-bold uppercase tracking-widest">3.5x Better Absorption</p>
                        </div>
                    </div>

                    {/* Table */}
                    <div className="w-full">
                        <table className="w-full text-left border-collapse">
                            <thead>
                                <tr className="bg-obsidian/50 border-b border-white/5 text-slate-ash/70 text-sm uppercase tracking-wider font-semibold">
                                    <th className="p-6">Standard</th>
                                    <th className="p-6 text-white text-center border-l bg-cyan-ethereal/5 border-white/5">Oxygen Bioinnovations</th>
                                    <th className="p-6 text-center border-l border-white/5">Most Brands</th>
                                </tr>
                            </thead>
                            <tbody className="text-sm md:text-base">
                                {comparisons.map((row, idx) => (
                                    <tr key={idx} className="border-b border-white/5 hover:bg-white/5 transition-colors">
                                        <td className="p-6 font-medium text-slate-ash">{row.label}</td>
                                        <td className="p-6 text-center font-bold text-cyan-ethereal bg-cyan-ethereal/5 border-l border-white/5 flex items-center justify-center gap-2">
                                            <Check className="w-4 h-4" /> {row.us}
                                        </td>
                                        <td className="p-6 text-center text-slate-ash/60 border-l border-white/5 flex items-center justify-center gap-2">
                                            <X className="w-4 h-4 text-red-500/50" /> {row.them}
                                        </td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                </div>

            </div>
        </section>
    );
};

export default Science;
