import { motion, type Transition } from 'framer-motion';
import type { ReactNode } from 'react';

interface PageTransitionProps {
    children: ReactNode;
    className?: string;
}

const pageVariants = {
    initial: {
        opacity: 0,
        y: 10,
    },
    in: {
        opacity: 1,
        y: 0,
    },
    out: {
        opacity: 0,
        y: -10,
    },
};

const pageTransition: Transition = {
    type: 'tween',
    ease: [0.25, 1, 0.5, 1],
    duration: 0.5,
};

const PageTransition = ({ children, className = '' }: PageTransitionProps) => {
    return (
        <motion.div
            initial="initial"
            animate="in"
            exit="out"
            variants={pageVariants}
            transition={pageTransition}
            className={`w-full ${className}`}
        >
            {children}
        </motion.div>
    );
};

export default PageTransition;
