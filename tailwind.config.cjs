const config = {
  content: ["./src/**/*.{html,js,svelte,ts}"],

  theme: {
    extend: {
      colors: {
        beauty: '#ff8ca8',
      },
      fontSize: {
        'xxs': '0.425rem', // Tamaño de texto xxs
      },
    },
  },

  plugins: [],
};

module.exports = config;
