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
                        <span className="font-heading font-extrabold text-2xl tracking-tighter text-white flex items-center">
                            Oxygen <span className="font-['Quicksand'] tracking-normal font-bold ml-1.5 opacity-90 pb-0.5">Bioinnovations</span><span className="text-cyan-ethereal">.</span>
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

                            <div className="absolute top-[100%] left-1/2 -translate-x-1/2 w-[700px] bg-white rounded-3xl p-3 shadow-[0_40px_100px_rgba(0,0,0,0.3)] opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-400 ease-[cubic-bezier(0.16,1,0.3,1)] pointer-events-none group-hover:pointer-events-auto flex transform translate-y-3 group-hover:translate-y-0 scale-95 group-hover:scale-100 mt-2">
                                {/* Hover bridge */}
                                <div className="absolute -top-6 left-0 w-full h-8" />

                                {/* Left Pane */}
                                <div className="w-[45%] bg-[#FFF8F0] p-8 rounded-2xl border border-orange-900/5 flex flex-col justify-center relative overflow-hidden group/pane">
                                    <div className="absolute top-0 right-0 w-40 h-40 bg-orange-500/5 rounded-full blur-3xl -mr-10 -mt-10 transition-transform group-hover/pane:scale-150 duration-700" />
                                    <div className="mb-5">
                                        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#F59E0B" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                                            <path d="M10 2v6.5l-7 10.5C2.5 19.8 3.2 21 4.5 21h15c1.3 0 2-.8 1.5-2L14 8.5V2" />
                                            <path d="M8.5 2h7" />
                                            <path d="M14 6h-4" />
                                            <path d="M5.5 16h13" />
                                        </svg>
                                    </div>
                                    <h4 className="text-xl font-bold text-obsidian mb-3 tracking-tight">Evidence-Based</h4>
                                    <p className="text-sm text-slate-600 leading-relaxed font-medium">
                                        We formulate with clinical precision and indigenous botanical wisdom.
                                    </p>
                                </div>

                                {/* Right Pane */}
                                <div className="w-[55%] p-8 flex flex-col justify-center gap-6">
                                    <a href="#problem" className="group/link block p-3 -m-3 rounded-xl hover:bg-slate-50 transition-colors">
                                        <h5 className="text-base font-bold text-obsidian mb-1 flex items-center gap-2 group-hover/link:text-[#0D8A74] transition-colors">
                                            The Problem
                                            <span className="opacity-0 -translate-x-2 group-hover/link:opacity-100 group-hover/link:translate-x-0 transition-all text-[#0D8A74]">→</span>
                                        </h5>
                                        <p className="text-sm text-slate-500 font-medium">
                                            Understand the nutritional breakdown in urban India.
                                        </p>
                                    </a>

                                    <a href="#ingredients" className="group/link block p-3 -m-3 rounded-xl hover:bg-slate-50 transition-colors">
                                        <h5 className="text-base font-bold text-obsidian mb-1 flex items-center gap-2 group-hover/link:text-[#0D8A74] transition-colors">
                                            Ingredients Index
                                            <span className="opacity-0 -translate-x-2 group-hover/link:opacity-100 group-hover/link:translate-x-0 transition-all text-[#0D8A74]">→</span>
                                        </h5>
                                        <p className="text-sm text-slate-500 font-medium">
                                            Deep dive into every component of our formulations.
                                        </p>
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
