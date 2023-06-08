<script>
  import _data from "./json/data.json";
  import Gallery from "./lib/Gallery.svelte";
  import FixedScrollUpButton from "./lib/FixedScrollUpButton.svelte";
  import Header from "./lib/Header.svelte";
  import HeaderBar from "./lib/HeaderBar.svelte";
  import { fade } from "svelte/transition";
  import Prices from "./lib/Prices.svelte";
  import { deactivateTag } from "./assets/ToggleStore.js";
    import Tos from "./lib/Tos.svelte";

  let currentHash = location.hash;

  function handleHashChange() {
    currentHash = location.hash;
    deactivateTag();
  }
</script>

<section>
  <FixedScrollUpButton></FixedScrollUpButton>
</section>

  <!-- <StickyBar/> -->

<svelte:window on:hashchange={handleHashChange} />

<main class="relative">
  <div
    class="flex flex-col h-auto min-h-screen justify-center place-items-center">
    <div
      class="flex flex-col min-w-[40vw] max-w-[85vw] min-h-fit bg-[#0000008C] justify-center place-items-center rounded-[4rem] my-8 overflow-clip">
      {#if currentHash === '' || currentHash === '#home'}
      <section class="w-[90%]" in:fade>
        <Header />
      </section>
      {:else}
        <HeaderBar />
      {/if}

      <div class="w-[90%]">
        {#if currentHash === '#gallery'}
        <section in:fade>
          <Gallery images={_data.filter((item) => !item.src.endsWith("$secret.webp"))} />
        </section>
        {:else if currentHash === '#prices'}
        <section in:fade>
          <hr class="mt-2 mb-4 h-0.5 border-t-0 bg-neutral-100/10" />
          <Prices />
        </section>
        {:else if currentHash === '#tos'}
        <section in:fade>
          <hr class="mt-2 mb-4 h-0.5 border-t-0 bg-neutral-100/10" />
          <Tos />
        </section>
        {/if}

        <footer class="flex flex-col w-full h-fit pt-2 pb-4 xl:px-16 px-8">
          <!-- <a href="https://www.flaticon.com/free-icons/" class="text-slate-300 text-center xl:text-sm text-xs" title="discord icons">Icons created by Flaticon</a> -->
        </footer>
      </div>
    </div>
  </div>
</main>
