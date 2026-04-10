import Hero from '../components/home/Hero';
import TrustBar from '../components/home/TrustBar';
import Problem from '../components/home/Problem';
import Solution from '../components/home/Solution';
import Science from '../components/home/Science';
import PageTransition from '../components/layout/PageTransition';

const Index = () => {
    return (
        <PageTransition>
            <div className="w-full flex flex-col items-center">
                <Hero />
                <TrustBar />
                <Problem />
                <Solution />
                <Science />
            </div>
        </PageTransition>
    );
};

export default Index;
