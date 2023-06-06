<script>
  import _data from "./json/data.json";
  import Gallery from "./lib/Gallery.svelte";
  import FixedScrollUpButton from "./lib/FixedScrollUpButton.svelte";
  import Header from "./lib/Header.svelte";
  import resizeContainer from "./assets/resizeContainer";
  import { fade } from "svelte/transition";
  import HeaderBar from "./lib/HeaderBar.svelte";

  // Filter elements of the array whose src ends in $secret (temporary, those drawings have not been published yet but I ain't deleting them from the repo lmao)
  let data = _data.filter((item) => !item.src.endsWith("$secret.webp"))

  let toggle = false;

//toggle with l 
  window.addEventListener("keydown", (event) => {
    if (event.key === "l") {
      toggle = !toggle;
      resizeContainer(toggle);
    }
  });
</script>

<section>
  <FixedScrollUpButton></FixedScrollUpButton>
</section>

<main class="relative">
  <div
    class="flex flex-col h-auto min-h-screen justify-center place-items-center">
    <div
      class="flex flex-col min-w-[50vw] max-w-[85vw] min-h-fit bg-[#0000008C] justify-center place-items-center rounded-[4rem] my-8">
      <div class="w-[90%]">
        {#if !toggle}
        <section class="w-full">
          <Header />
        </section>
        {:else}
        <section class="w-full">
          <HeaderBar />
        </section>
        {/if}

        {#if toggle}
        <section>
          <Gallery bind:images={data} />
        </section>
        {/if}

        <footer class="flex flex-col w-full h-fit pt-2 pb-4 xl:px-16 px-8">
          <a href="https://www.flaticon.com/free-icons/" class="text-slate-300 text-center xl:text-sm text-xs" title="discord icons">Icons created by Flaticon</a>
        </footer>
      </div>
    </div>
  </div>
</main>
