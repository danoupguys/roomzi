/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["templates/*.html", "*/templates/*/*.html"],
  theme: {
    extend: {},
    fontFamily: {
      anjoman: ['anjoman'],
      vazir: ['Vazir']
    }
  },
  plugins: [],
}
