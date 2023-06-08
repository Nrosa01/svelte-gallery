<script>
  import prices_shaded from "../json/prices_shaded.json";
  import prices_lined from "../json/prices_lined.json";
  import prices_posttf from "../json/prices_posttf.json";
  import Image from "./Image.svelte";
  import BackButton from "./BackButton.svelte";
    import Gallery from "./Gallery.svelte";

  const categories = [
    {
      title: "Shaded / Painting",
      description: "This is the kind of work I usually upload to social medias. It can be lined but I tend to prefer doing lineless. Fullbody.",
      prices: prices_shaded,
      basePrice: 50
    },
    {
      title: "LINED / MINIMAL SHADING",
      description: "This gets you a clean lined drawing with flat colours and some minimal shading. Fullbody",
      prices: prices_lined,
      basePrice: 30
    },
    {
      title: "POST TF DOODLE PAGE",
      description: "A simple 3-5 panel sequence showing a character already transformed reacting to his new body or in some situation due to it. These drawings are a flat style with minimal shading and they are a little more simplified than other of my drawings.Background isn't included",
      prices: prices_posttf,
      basePrice: 45
    }
  ];
</script>

<div class="w-full text-center items-center justify-center place-content-center flex flex-col">
  {#each categories as category}
    <section>
      <h2 class="title">{category.title}</h2>
      <p class="text-white xl:text-2xl text-lg font-bold quicksand xl:py-8 py-4">{category.description}</p>

      <Gallery images={category.prices} />

      <h3 class="text-white text-2xl font-bold quicksand pt-8">
        Base price starting at <span class="quicksand-bold">{category.basePrice}</span><span class="font-semibold font-sans">€</span>
      </h3>
      <hr class="my-12 h-0.5 border-t-0 bg-neutral-100/10" />
    </section>
  {/each}

  <section class="flex flex-col w-full items-center justify-center">
    <h2 class="title pb-8">Extras</h2>
    <div class="flex w-[50rem] text-beauty xl:text-2xl md:text-xl sm:text-base text-xs font-semibold justify-center">
      <div>
        <table>
          <thead>
            <tr>
              <th class="py-4 border-b-2 border-white/25 quicksand-bold">Addon</th>
              <th class="py-4 border-b-2 border-white/25 quicksand-bold">Price</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="py-4 border-b border-white/10 quicksand">Rough Background</td>
              <td class="py-4 border-b border-white/10 quicksand">15<span class="font-light font-sans">€</span></td>
            </tr>
            <tr>
              <td class="py-4 border-b border-white/10 quicksand">Background</td>
              <td class="py-4 border-b border-white/10 quicksand">30<span class="font-light font-sans">€</span></td>
            </tr>
            <tr>
              <td class="py-4 quicksand">Extra Character*</td>
              <td class="py-4 quicksand">Base price of the tier</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <p>
      <span class="block text-white text-sm font-bold quicksand xl:pt-8 pt-4">
        *Extra Character doesn't apply to Post TF Doodle Page category. Extra Character price may vary depending on the difficulty.
      </span>
      <span class="block text-white xl:text-xl text-lg font-bold quicksand xl:py-4 py-2">
        Feel free to DM me about any doubt or inquiry! <strong class="quicksand-bold">You can request things that aren't listed here.</strong>
      </span>
    </p>
  </section>

  <BackButton />
</div>
