import { AlertCircle, EyeOff, Globe2 } from 'lucide-react';
import { motion } from 'framer-motion';

const Problem = () => {
    const stats = [
        { label: "Imported Supplements", value: "₹2000+", source: "Monthly Cost Burden" },
        { label: "Bioavailability Blocked", value: "High Phytic", source: "Raw Indian Grain Profiles" },
        { label: "Generic Extraction", value: "Single Method", source: "Competitor Market Default" }
    ];

    const cards = [
        {
            icon: <AlertCircle className="w-8 h-8 text-cyan-ethereal mb-4" />,
            title: "Market Gap",
            description: "India's functional mushroom beverage category does not exist in an accessible format. The current market is imported dry supplements at ₹500–2,000/month — designed for consumers who already have disposable income and product literacy. Our target consumer is a 18–28 year old student or young professional."
        },
        {
            icon: <EyeOff className="w-8 h-8 text-cyan-ethereal mb-4" />,
            title: "Scientific Gap & Extraction",
            description: "Most functional products apply a single generic extraction method across all species — scientifically inadequate given that each mushroom species has distinct thermal stability profiles for its primary bioactive. Additionally, no Indian brand currently documents phytic acid reduction via fermentation."
        },
        {
            icon: <Globe2 className="w-8 h-8 text-cyan-ethereal mb-4" />,
            title: "Price Gap",
            description: "The entire category is priced out of daily-use affordability. At ₹65–75 per 200ml, we are building for frequency — not occasional premium use. That requires a platform architecture where one production process serves multiple SKUs without inflating operational scale costs."
        }
    ];

    const cards = [
        {
            icon: <AlertCircle className="w-8 h-8 text-cyan-ethereal mb-4" />,
            title: "No time for real nutrition",
            description: "The average working professional has 22 minutes for lunch, often at their desk. Students skip meals before exams. Athletes eat whatever is convenient after training. The food system was not designed for how Indians actually live."
        },
        {
            icon: <EyeOff className="w-8 h-8 text-cyan-ethereal mb-4" />,
            title: "Existing products deceive you",
            description: "Most Indian health drinks are primarily sugar with token doses of vitamins your body cannot absorb. Cheap synthetic forms, under-dosed actives, misleading labels. The same brand sells better formulas in foreign markets. You deserve to know this."
        },
        {
            icon: <Globe2 className="w-8 h-8 text-cyan-ethereal mb-4" />,
            title: "Imported solutions do not fit India",
            description: "Products designed for Western nutritional deficiencies miss what Indian bodies need. They do not understand Ragi, Moringa, or Ashwagandha. They do not understand how Indians eat, work, or train. India needs an Indian solution."
        }
    ];

    return (
        <section id="problem" className="w-full py-20 md:py-32 relative bg-obsidian">
            {/* Subtle Background Elements */}
            <div className="absolute top-0 right-0 w-[500px] h-[500px] bg-cyan-seafoam/5 rounded-full blur-sm pointer-events-none" />

            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">

                {/* Header Section */}
                <div className="text-center md:text-left mb-20 max-w-3xl">
                    <motion.h2
                        
                        
                        
                        
                        className="text-3xl md:text-5xl font-heading font-extrabold text-white mb-6"
                    >
                        The initial problem is <span className="text-transparent bg-clip-text bg-gradient-to-r from-red-400 to-orange-400">functional access.</span>
                    </motion.h2>
                    <motion.p
                        
                        
                        
                        
                        className="text-lg text-slate-ash leading-relaxed"
                    >
                        We are targeting a market gap, a scientific methodology gap, and a price gap simultaneously.
                    </motion.p>
                </div>

                {/* Big Stats Row */}
                <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-20">
                    {stats.map((stat, i) => (
                        <div
                            
                            
                            
                            
                            key={i}
                            className="border-l-2 border-cyan-ethereal/50 pl-6 py-2"
                        >
                            <div className="text-5xl font-heading font-bold text-white mb-2">{stat.value}</div>
                            <div className="text-lg font-medium text-cyan-seafoam mb-1">{stat.label}</div>
                            <div className="text-xs text-slate-ash/60">Source: {stat.source}</div>
                        </div>
                    ))}
                </div>

                {/* 3 Problems Cards */}
                <div className="grid grid-cols-1 md:grid-cols-3 gap-6 lg:gap-8">
                    {cards.map((card, i) => (
                        <div
                            
                            
                            
                            
                            key={i}
                            className="glass-card p-8 group hover:bg-charcoal transition-colors duration-300"
                        >
                            <div className="bg-obsidian w-16 h-16 rounded-xl flex items-center justify-center mb-6 shadow-inner border border-white/5 group-hover:border-cyan-ethereal/30 transition-colors">
                                {card.icon}
                            </div>
                            <h3 className="text-2xl font-heading font-bold text-white mb-4">{card.title}</h3>
                            <p className="text-slate-ash/90 leading-relaxed text-sm md:text-base">
                                {card.description}
                            </p>
                        </div>
                    ))}
                </div>

            </div>
        </section>
    );
};

export default Problem;
