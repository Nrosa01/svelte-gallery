<script>
  import prices_shaded from "../../../json/prices_shaded.json";
  import prices_lined from "../../../json/prices_lined.json";
  import prices_posttf from "../../../json/prices_posttf.json";
  import BackButton from "./BackButton.svelte";
  import Gallery from "./Gallery.svelte";

  const categories = [
    {
      title: "POST TF DOODLE PAGE",
      description:
        "A simple 3-5 panel sequence showing a character already transformed reacting to his new body or in some situation due to it. These drawings are a flat style with minimal shading and they are a kinda more simplified than other of my drawings. Simple Background is included in this tier.",
      prices: prices_posttf,
      basePrice: 45,
    },
    {
      title: "Shaded / Painting",
      description:
        "This is the kind of work I usually upload to social medias. It can be lined but I tend to prefer doing lineless. Fullbody.",
      prices: prices_shaded,
      basePrice: 50,
    },
    {
      title: "LINED / MINIMAL SHADING",
      description:
        "This gets you a clean lined drawing with flat colours and some minimal shading. Fullbody.",
      prices: prices_lined,
      basePrice: 30,
    },
  ];
</script>

<div
  class="w-full text-center items-center justify-center place-content-center flex flex-col">
  {#each categories as category, index}
    <section>
      <h2 class="title">{category.title}</h2>
      <p
        class="text-white xl:text-2xl text-lg font-bold quicksand xl:py-8 py-4">
        {category.description}
      </p>

      <Gallery images="{category.prices}" />

      <div class="w-full pt-8 flex justify-center gap-4">
      {#if index > 0}
        <h3 class="text-black text-2xl font-bold quicksand py-4 bg-beauty px-4 rounded-full w-fit">
          Base price starting at <span class="quicksand-bold"
          >{category.basePrice}</span
          ><span class="font-semibold font-sans">€</span> per character
        </h3>
        <h3 class="text-black text-2xl font-bold quicksand py-4 bg-beauty px-4 rounded-full w-fit">
          Simple background <span class="quicksand-bold"
          >15</span
          ><span class="font-semibold font-sans">€</span>
        </h3>
        <h3 class="text-black text-2xl font-bold quicksand py-4 bg-beauty px-4 rounded-full w-fit">
          Complex background <span class="quicksand-bold"
          >30</span
          ><span class="font-semibold font-sans">€</span>
        </h3>
        {:else}
        <h3 class="text-black text-2xl font-bold quicksand py-4 bg-beauty px-4 rounded-full w-fit">
          Base price starting at <span class="quicksand-bold"
          >{category.basePrice}</span
          ><span class="font-semibold font-sans">€</span>
        </h3>
        {/if}
      </div>
      <hr class="my-12 h-0.5 border-t-0 bg-neutral-100/10" />
    </section>
  {/each}

  <section class="flex flex-col w-full items-center justify-center">
    <p>
      <span class="block text-white text-sm font-bold quicksand">
        Extra Character price may vary depending on the difficulty.
      </span>
      <span
        class="block text-white xl:text-xl text-lg font-bold quicksand xl:py-4 py-2">
        Feel free to DM me about any doubt or inquiry! <strong
          class="quicksand-bold"
          >You can request things that aren't listed here.</strong>
      </span>
    </p>
  </section>

  <BackButton />
</div>
