<script>
  import { fade } from "svelte/transition";
  import IconBar from "./IconBar.svelte";

  let backdrop = false;

  function handleScroll() {
    const scrollPosition = window.scrollY;
    const windowHeight = window.innerHeight;
    const scrollThreshold = windowHeight * 0.1; // 20% del viewheight

    backdrop = scrollPosition > scrollThreshold;
  }
</script>

<svelte:window on:scroll="{handleScroll}" />

<section
  class="w-full sticky top-0 flex justify-center backdrop-blur-xl"
  class:backdrop
  in:fade>
  <div class="grid grid-cols-2 place-items-center xl:pb-4 pt-8 w-[90%]">
    <div
      class="flex flex-row items-center w-full xl:h-20 h-10 justify-start gap-4 place-content-end">
      <a href="#home" class="h-full"><img class="h-full p-1 rounded-full site-image" alt="pfp" /></a>
      <h1 class="xl:text-6xl text-2xl text-white quicksand font-bold">Rioni</h1>
    </div>

    <IconBar />
  </div>
</section>

<style>
  .backdrop {
    --tw-backdrop-blur: blur(8px);
    backdrop-filter: brightness(0.25) var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);
    box-shadow: 0 25px 50px -12px rgb(0, 0, 0);
  }
</style>
