import { motion } from 'framer-motion';
import { Microscope, ShieldCheck, Activity } from 'lucide-react';

const Science = () => {
    const pillars = [
        {
            icon: <Activity className="w-8 h-8 text-cyan-ethereal" />,
            title: "Layer 01 / Fermentation",
            description: "Traditional Indian grain substrates contain high phytic acid. Controlled Lactic Acid Bacteria fermentation enzymatically degrades phytic acid through phytase activity, improving native mineral bioavailability.",
            highlight: "■ PUBLISHED — Coulibaly et al. (2011)"
        },
        {
            icon: <ShieldCheck className="w-8 h-8 text-cyan-ethereal" />,
            title: "Layer 02 / GABA Biosynthesis",
            description: "Certain L. plantarum strains carry the GAD enzyme to convert glutamic acid to GABA in situ. This is our primary near-term innovation target.",
            highlight: "◆ PLANNED — Characterisation underway at TBI-DETI@ACE"
        },
        {
            icon: <Microscope className="w-8 h-8 text-cyan-ethereal" />,
            title: "Layer 03 / Specific Extraction",
            description: "Each mushroom species has a distinct thermal stability profile. A single generic extraction method cannot simultaneously optimise for Hericenones, Cordycepin, and Beta-Glucans. We use targeted hot-water fruiting body extraction.",
            highlight: "● PLAUSIBLE — Based on species-specific literature"
        }
    ];

    return (
        <section id="science" className="w-full py-20 md:py-32 bg-obsidian relative overflow-hidden">
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
                        Every formulation decision has a peer-reviewed reason. Every claim is labelled: PUBLISHED, PLAUSIBLE, or PLANNED. We do not claim our own lab has validated what only published literature supports — yet.
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

            </div>
        </section>
    );
};

export default Science;
