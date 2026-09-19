/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        dark: {
          900: '#0a0a1a',
          800: '#0f0f23',
          700: '#1a1a2e',
          600: '#1f1f3a',
          500: '#2a2a4a',
        },
        accent: {
          purple: '#7b2ff7',
          cyan: '#00d2ff',
          pink: '#ff2d95',
        }
      },
      backgroundImage: {
        'gradient-main': 'linear-gradient(135deg, #7b2ff7, #00d2ff)',
        'gradient-card': 'linear-gradient(135deg, #1a1a2e, #12122a)',
      }
    },
  },
  plugins: [],
}
