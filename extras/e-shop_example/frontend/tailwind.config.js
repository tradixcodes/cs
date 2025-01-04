/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        primary: "#DAA520",
        secondary: "#f42c37",
        brandYellow: "#fdc62e", //this is for the watch.png
        brandGreen: "#2dcc6f",
        brandBlue: "#1376f4",
        brandRed: "#892066",
        brandPink:"#A41045",
        brandWhite: "#eeeeee",
        champagneGold: '#F7E7CE', //primary
        yellowGold:'#F9D45B', //main actions to call
        myGrey:'#0C2639', //secondary also other actions to call
      },
      container: {
        center: true,
        padding: {
          DEFAULT: "1rem",
          sm: "3rem" ,
        },
      },
    },
  },
  plugins: [],
}

