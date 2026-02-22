const Footer = () => {
    return (
        <footer className="w-full bg-obsidian border-t border-white/5 py-12 md:py-16">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col items-center">
                <span className="font-heading font-bold text-3xl tracking-tighter text-white mb-6">
                    OXYGEN<span className="text-cyan-ethereal">.</span>
                </span>
                <p className="text-slate-ash text-center text-sm max-w-md mb-8">
                    Ancient Ingredients. Modern Science. No Compromise. India's first precision nutrition system.
                </p>
                <div className="text-slate-ash/60 text-xs">
                    &copy; {new Date().getFullYear()} Oxygen Bioinnovations. All rights reserved.
                </div>
            </div>
        </footer>
    );
};

export default Footer;
