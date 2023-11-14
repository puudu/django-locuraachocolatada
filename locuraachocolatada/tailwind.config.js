/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["./client/templates/**/*.html"],
    theme: {
        extend: {
            colors: {
                "custom-brown": "#3B200B",
                "custom-pink": "#F98497",
                "custom-dark-pink": "#B3556A",
            },
        },
    },
    plugins: [],
};
