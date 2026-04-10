import { motion } from 'framer-motion';
import { ChevronRight, Sparkles } from 'lucide-react';

const Hero = () => {
    return (
        <section className="relative w-full pt-32 pb-20 md:pt-40 md:pb-32 overflow-hidden flex justify-center">
            {/* Background Glow */}
            <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-cyan-ethereal/20 rounded-full blur-sm opacity-50 pointer-events-none" />

            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 w-full">
                <div className="flex flex-col md:flex-row items-center gap-12 lg:gap-20">

                    {/* Left Column (Content) */}
                    <div className="flex-1 text-left w-full">

                        {/* Top Badges */}
                        <motion.div
                            initial={{ opacity: 0, y: 20 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ duration: 0.4, ease: [0.22, 1, 0.36, 1] }}
                            className="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-white/5 border border-white/10 mb-8 backdrop-blur-md"
                        >
                            <Sparkles className="w-4 h-4 text-cyan-ethereal" />
                            <span className="text-xs font-semibold tracking-wide text-white/90">
                                🌱 Phase 0 Lab Validation &bull; Incubated at DETI@ACE TBI &bull; Hosur
                            </span>
                        </motion.div>

                        {/* Headline */}
                        <motion.div
                            initial={{ opacity: 0, y: 20 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ duration: 0.4, delay: 0.1, ease: [0.22, 1, 0.36, 1] }}
                        >
                            <h1 className="text-4xl sm:text-5xl lg:text-7xl font-heading font-extrabold tracking-tight text-white leading-[1.1] mb-6">
                                உணவே மருந்து &mdash; "Food Is Medicine"<br />
<span className="bg-gradient-to-r from-cyan-ethereal to-cyan-seafoam bg-clip-text text-transparent">
Phase 0 Validation.
</span><br />
Validated by Science.
                            </h1>
                        </motion.div>

                        {/* Subtitle */}
                        <motion.p
                            initial={{ opacity: 0, y: 20 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ duration: 0.4, delay: 0.2, ease: [0.22, 1, 0.36, 1] }}
                            className="text-lg md:text-xl text-slate-ash leading-relaxed max-w-2xl mb-10"
                        >
                            India's first platform of naturally fermented functional beverages. Fermented indigenous grains. Species-specific medicinal mushroom extracts. Validating our extraction and probiotic models at TBI-DETI@ACE.</motion.p>

                        {/* CTAs (Vertically stacked on mobile, row on desktop) */}
                        <motion.div
                            initial={{ opacity: 0, y: 20 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ duration: 0.4, delay: 0.3, ease: [0.22, 1, 0.36, 1] }}
                            className="flex flex-col sm:flex-row gap-4 mb-12 w-full sm:w-auto"
                        >
                            <button className="w-full sm:w-auto group relative flex items-center justify-center gap-2 bg-cyan-ethereal text-obsidian font-bold text-lg px-8 py-4 rounded-xl shadow-[0_0_20px_rgba(102,252,241,0.4)] hover:shadow-[0_0_30px_rgba(102,252,241,0.6)] hover:bg-white transition-all duration-300">
                                Follow R&D Journey
                                <ChevronRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
                            </button>
                            <button className="w-full sm:w-auto flex items-center justify-center gap-2 bg-transparent text-white border border-slate-ash/30 font-bold text-lg px-8 py-4 rounded-xl hover:bg-white/5 transition-colors duration-300">
                                Read the Science
                            </button>
                        </motion.div>

                    </div>

                    {/* Right Column (Visual) - Hidden on smallest mobile, expands on tablet/desktop */}
                    <motion.div
                        initial={{ opacity: 0, scale: 0.9 }}
                        animate={{ opacity: 1, scale: 1 }}
                        transition={{ duration: 0.5, delay: 0.2, ease: [0.22, 1, 0.36, 1] }}
                        className="flex-1 w-full hidden md:flex justify-center"
                    >
                        <div className="relative w-full max-w-md aspect-square">
                            {/* Abstract scientific visual representation */}
                            <div className="absolute inset-0 rounded-full border border-white/10 animate-[spin_20s_linear_infinite]" />
                            <div className="absolute inset-4 rounded-full border border-cyan-ethereal/30 animate-[spin_15s_linear_infinite_reverse]" />
                            <div className="absolute inset-8 rounded-full border border-white/5 animate-[spin_10s_linear_infinite]" />

                            <div className="absolute inset-0 flex items-center justify-center">
                                <div className="w-40 h-40 rounded-full bg-gradient-to-br from-cyan-ethereal via-cyan-seafoam to-obsidian blur-sm opacity-40 animate-pulse" />
                                <div className="absolute w-32 h-32 rounded-full glass-card flex items-center justify-center shadow-2xl">
                                    <span className="font-heading font-bold text-4xl text-white">O<span className="text-cyan-ethereal">2</span></span>
                                </div>
                            </div>
                        </div>
                    </motion.div>

                </div>
            </div>
        </section>
    );
};

export default Hero;
