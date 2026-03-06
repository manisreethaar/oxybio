import { MapPin, Mail, Phone, Linkedin, Twitter, Instagram } from 'lucide-react';

const Footer = () => {
    return (
        <footer className="w-full bg-white border-t border-slate-200 py-16">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="grid grid-cols-1 md:grid-cols-12 gap-12">
                    {/* Left Column: Brand & Contact */}
                    <div className="md:col-span-5 flex flex-col space-y-10">
                        <div>
                            <a href="/" className="block">
                                <img src="/assets/images/logo-full.png" alt="Oxygen Bioinnovations" className="h-9 w-auto block" />
                            </a>
                            <p className="text-slate-500 italic text-sm mt-4">
                                Precision nutrition for every ambitious Indian.
                            </p>
                            <p className="text-slate-600 text-sm mt-4 max-w-sm leading-relaxed font-medium">
                                India's first honest precision nutrition system. Built on millet, mushrooms, and real science.
                            </p>

                            <div className="flex gap-4 mt-6">
                                <a href="#" className="w-10 h-10 rounded-full border border-slate-200 flex items-center justify-center text-slate-500 hover:border-[#0D8A74] hover:text-[#0D8A74] transition-colors">
                                    <Linkedin className="w-4 h-4" />
                                </a>
                                <a href="#" className="w-10 h-10 rounded-full border border-slate-200 flex items-center justify-center text-slate-500 hover:border-[#0D8A74] hover:text-[#0D8A74] transition-colors">
                                    <Twitter className="w-4 h-4" />
                                </a>
                                <a href="#" className="w-10 h-10 rounded-full border border-slate-200 flex items-center justify-center text-slate-500 hover:border-[#0D8A74] hover:text-[#0D8A74] transition-colors">
                                    <Instagram className="w-4 h-4" />
                                </a>
                            </div>
                        </div>

                        <div>
                            <h4 className="font-heading font-bold text-lg text-obsidian mb-5">Contact Us</h4>
                            <div className="flex flex-col space-y-4">
                                <div className="flex items-start gap-3 text-slate-600 text-sm font-medium">
                                    <MapPin className="w-5 h-5 text-[#0D8A74] flex-shrink-0 mt-0.5" />
                                    <span>Cabin D, Technology Business Incubator,<br />Adhiyamaan College of Engineering Campus, Dr<br />MGR Nagar, Hosur, tamil nadu - 635130</span>
                                </div>
                                <div className="flex items-center gap-3 text-slate-600 text-sm font-medium">
                                    <Mail className="w-5 h-5 text-[#0D8A74] flex-shrink-0" />
                                    <span>info@oxygenbioinnovations.com</span>
                                </div>
                                <div className="flex items-center gap-3 text-slate-600 text-sm font-medium">
                                    <Phone className="w-5 h-5 text-[#0D8A74] flex-shrink-0" />
                                    <span>+91 (800) 123-4567</span>
                                </div>
                            </div>
                        </div>
                    </div>

                    {/* Quick Links */}
                    <div className="md:col-span-2 md:col-start-7">
                        <h4 className="font-heading font-bold text-lg text-obsidian mb-6">Quick Links</h4>
                        <ul className="flex flex-col space-y-4">
                            <li><a href="#about" className="text-sm font-medium text-slate-500 hover:text-[#0D8A74] transition-colors">About Us</a></li>
                            <li><a href="#science" className="text-sm font-medium text-slate-500 hover:text-[#0D8A74] transition-colors">Our Science</a></li>
                            <li><a href="#ingredients" className="text-sm font-medium text-slate-500 hover:text-[#0D8A74] transition-colors">Ingredients</a></li>
                            <li><a href="#blog" className="text-sm font-medium text-slate-500 hover:text-[#0D8A74] transition-colors">Blog</a></li>
                        </ul>
                    </div>

                    {/* Get In Touch */}
                    <div className="md:col-span-2">
                        <h4 className="font-heading font-bold text-lg text-obsidian mb-6">Get In Touch</h4>
                        <ul className="flex flex-col space-y-4">
                            <li><a href="#contact" className="text-sm font-medium text-slate-500 hover:text-[#0D8A74] transition-colors">Contact Us</a></li>
                            <li><a href="#careers" className="text-sm font-medium text-slate-500 hover:text-[#0D8A74] transition-colors">Careers</a></li>
                        </ul>
                    </div>

                    {/* Legal */}
                    <div className="md:col-span-2">
                        <h4 className="font-heading font-bold text-lg text-obsidian mb-6">Legal</h4>
                        <ul className="flex flex-col space-y-4">
                            <li><a href="#privacy" className="text-sm font-medium text-slate-500 hover:text-[#0D8A74] transition-colors">Privacy Policy</a></li>
                            <li><a href="#terms" className="text-sm font-medium text-slate-500 hover:text-[#0D8A74] transition-colors">Terms & Conditions</a></li>
                        </ul>
                    </div>
                </div>

                {/* CIN & Copyright */}
                <div className="mt-16 pt-8 border-t border-slate-200 text-center text-sm text-slate-500">
                    &copy; 2026 Oxygen Bioinnovations Private Limited with CIN: U72100TZ2026PTC038160. All rights reserved.
                </div>
            </div>
        </footer>
    );
};

export default Footer;
