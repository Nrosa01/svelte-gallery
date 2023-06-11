const config = {
  content: ["./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}"],

  theme: {
    extend: {
      colors: {
        beauty: "#ff8ca8",
        beautylink: "#fcb0c3",
      },
      fontSize: {
        xxs: "0.425rem", // Tamaño de texto xxs
      },
    },
  },

  plugins: [],
};

module.exports = config;
