<script>
    import Gallery from "./Gallery.svelte";

    export let images;
    export let title;
</script>

<section class="flex flex-col w-full h-fit justify-center text-center place-items-center mt-2">
    <p class="text-slate-300"><span>{title}</span></p>
    <Gallery bind:images={images} />
  </section> 