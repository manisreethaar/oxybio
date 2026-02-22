import { useState } from 'react';
import { Menu, X } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

const Navbar = () => {
    const [isOpen, setIsOpen] = useState(false);

    return (
        <nav className="fixed w-full z-50 bg-obsidian/85 backdrop-blur-xl border-b border-white/5">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="flex justify-between items-center h-20">
                    <div className="flex-shrink-0 flex items-center">
                        <span className="font-heading font-extrabold text-2xl tracking-tighter text-white">
                            OXYGEN<span className="text-cyan-ethereal">.</span>
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
                        <a href="#science" className="text-sm font-medium text-slate-ash hover:text-white transition-colors">Science</a>
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
