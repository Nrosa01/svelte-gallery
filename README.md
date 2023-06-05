# What this

Personal page for hosting and displaying low quality copies of my drawings as a showcase for people to see, mainly aimed for people who intend to commission me but what to see more examples of my art, but also for people how just want a nice site to have a quick view at my art. I never upload the original files nor high quality copies of my drawings except for commissioners who get the original files. The files in this site are web, quality 80 and method 6.

# How this build

I used [Svelte](https://svelte.dev) + [TailwindCSS](https://tailwindcss.com) + JS with Vite as a bundler. Icons are from [Flaticon](https://www.flaticon.com/). Images are stored in ``/public``, but the json with its data is stored in /json. The json is generated with a python script that reads the files in ``/public/gallery``, it also converted it from PNG to .webp, made the filename lowercase and replaced spaces with underscores. The script is still in the repo because it's useful, although it's not used anymore. New images are added manually to the json so I can control where is the best spot for that art.

## Layout

Modern websites tend to use Masonry layout (Kofi gallery, Pinterest) to have a fancy layout that adapts to the contents and the container. I use an horizontal CSS only version of this layout for better readability of the gallery, this kind of horizontal Masonry layout is used by websites like Carrd and Devianart. You can check the code in ``/src/lib/Gallery.svelte``.

## Filter

I use a svelte store as a middleware. ToggleButtons modify the store, and images suscribes to these changes and make themselves visible or not depending on the tags they have. You can check the code in ``/src/lib/ToggleButton.svelte`` and ``/src/lib/Image.svelte``.

## Lazy loading

I use lazy attribute for ``html`` image tag, it's not the best option, but given all the gallery is between 3-4MB in total this works for now.

# How to run

```
npm install
npm run dev
```

# Dependencies

None, just Svelte and TailwindCSS.