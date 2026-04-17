/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./index.html",
        "./src/**/*.{js,ts,jsx,tsx}",
    ],
    theme: {
        extend: {
            colors: {
                obsidian: '#0B0C10',
                charcoal: '#1F2833',
                cyan: {
                    ethereal: '#66FCF1',
                    seafoam: '#45A29E',
                },
                slate: {
                    ash: '#C5C6C7',
                }
            },
            fontFamily: {
                sans: ['Inter', 'Roboto', 'sans-serif'],
                heading: ['Outfit', 'Plus Jakarta Sans', 'sans-serif'],
            }
        },
    },
    plugins: [],
}
