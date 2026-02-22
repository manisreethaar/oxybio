import { useState } from 'react';
import { Menu, X, ChevronDown } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

const Navbar = () => {
    const [isOpen, setIsOpen] = useState(false);

    return (
        <nav className="fixed w-full z-50 bg-obsidian/85 backdrop-blur-xl border-b border-white/5">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="flex justify-between items-center h-20">
                    <div className="flex-shrink-0 flex items-center">
                        <span className="font-heading font-extrabold text-2xl tracking-tighter text-white">
                            Oxygen Bioinnovations<span className="text-cyan-ethereal">.</span>
                        </span>
                    </div>

                    <div className="md:hidden flex items-center">
                        <button
                            onClick={() => setIsOpen(!isOpen)}
                            className="text-white p-2 -mr-2 rounded-lg focus:outline-none focus:ring-2 focus:ring-cyan-ethereal/50 min-h-[48px] min-w-[48px] flex items-center justify-center transition-colors"
                            aria-label="Toggle menu"
                        >
                            {isOpen ? <X size={28} /> : <Menu size={28} />}
                        </button>
                    </div>

                    <div className="hidden md:flex space-x-8 items-center">
                        <a href="#problem" className="text-sm font-medium text-slate-ash hover:text-white transition-colors">The Problem</a>
                        <a href="#products" className="text-sm font-medium text-slate-ash hover:text-white transition-colors">Products</a>

                        <div className="relative group py-6">
                            <a href="#science" className="text-sm font-medium text-slate-ash hover:text-white transition-colors flex items-center gap-1">
                                Science
                                <ChevronDown className="w-3 h-3 group-hover:rotate-180 transition-transform" />
                            </a>

                            <div className="absolute top-[100%] left-1/2 -translate-x-1/2 w-[340px] bg-[#0a0a0c]/95 backdrop-blur-2xl border border-white/10 rounded-2xl p-6 shadow-[0_30px_60px_rgba(0,0,0,0.5),inset_0_0_0_1px_rgba(255,255,255,0.05)] opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-400 ease-[cubic-bezier(0.16,1,0.3,1)] pointer-events-none group-hover:pointer-events-auto flex gap-6 transform translate-y-2 group-hover:translate-y-0 scale-98 group-hover:scale-100">
                                {/* Hover bridge */}
                                <div className="absolute -top-6 left-0 w-full h-6" />

                                <div className="bg-gradient-to-br from-white/5 to-white/10 p-5 rounded-xl border border-white/5 min-w-[140px] flex-shrink-0">
                                    <div className="text-2xl mb-3">🔬</div>
                                    <h4 className="text-sm font-bold text-white mb-1">Clinical Proof</h4>
                                    <p className="text-xs text-slate-ash leading-relaxed">Data-driven formulas.</p>
                                </div>

                                <div className="flex flex-col justify-center gap-2">
                                    <a href="#problem" className="text-sm font-medium text-slate-ash hover:text-white transition-all hover:translate-x-1 group/link">
                                        The Problem <span className="opacity-0 -translate-x-2 group-hover/link:opacity-100 group-hover/link:translate-x-0 transition-all inline-block ml-1">→</span>
                                    </a>
                                    <a href="#science" className="text-sm font-medium text-slate-ash hover:text-white transition-all hover:translate-x-1 group/link">
                                        Absorption <span className="opacity-0 -translate-x-2 group-hover/link:opacity-100 group-hover/link:translate-x-0 transition-all inline-block ml-1">→</span>
                                    </a>
                                    <a href="#science" className="text-sm font-medium text-slate-ash hover:text-white transition-all hover:translate-x-1 group/link">
                                        Ingredient Data <span className="opacity-0 -translate-x-2 group-hover/link:opacity-100 group-hover/link:translate-x-0 transition-all inline-block ml-1">→</span>
                                    </a>
                                </div>
                            </div>
                        </div>
                        <button className="bg-cyan-ethereal text-obsidian font-bold px-6 py-2.5 rounded-full hover:bg-cyan-ethereal/90 transition-all hover:scale-105 active:scale-95 shadow-[0_0_15px_rgba(102,252,241,0.3)]">
                            Join Waitlist
                        </button>
                    </div>
                </div>
            </div>

            <AnimatePresence>
                {isOpen && (
                    <motion.div
                        initial={{ opacity: 0, y: -20 }}
                        animate={{ opacity: 1, y: 0 }}
                        exit={{ opacity: 0, y: -20 }}
                        transition={{ duration: 0.2 }}
                        className="md:hidden absolute top-20 left-0 w-full bg-charcoal/95 backdrop-blur-xl border-b border-white/10 shadow-2xl"
                    >
                        <div className="px-6 py-8 flex flex-col space-y-6">
                            <a href="#problem" className="text-xl font-heading font-semibold text-white tracking-tight" onClick={() => setIsOpen(false)}>The Problem</a>
                            <a href="#products" className="text-xl font-heading font-semibold text-white tracking-tight" onClick={() => setIsOpen(false)}>Products</a>
                            <a href="#science" className="text-xl font-heading font-semibold text-white tracking-tight" onClick={() => setIsOpen(false)}>Science</a>
                            <div className="pt-6 mt-6 border-t border-white/10">
                                <button className="w-full bg-cyan-ethereal text-obsidian font-bold py-4 rounded-xl text-lg hover:bg-cyan-ethereal/90 transition-all shadow-[0_4px_20px_rgba(102,252,241,0.25)]">
                                    Join Waitlist
                                </button>
                            </div>
                        </div>
                    </motion.div>
                )}
            </AnimatePresence>
        </nav>
    );
};

export default Navbar;
