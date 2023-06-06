<script>
    import { fade, slide } from "svelte/transition";

  let isVisible = false;

  function handleScroll() {
    const scrollPosition = window.scrollY;
    const windowHeight = window.innerHeight;
    const scrollThreshold = windowHeight * 0.2; // 20% del viewheight

    isVisible = scrollPosition > scrollThreshold;
  }
</script>

<svelte:window on:scroll="{handleScroll}" />

{#if isVisible}
  <section class="fixed top-0 z-50 bg-white w-full" transition:fade={{duration:250}}>
    <!-- Contenido de la barra sticky -->
    h
  </section>
{/if}
