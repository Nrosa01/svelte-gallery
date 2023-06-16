<script>
  import Gallery from "./Gallery.svelte";
  const prices_classes =
    "text-black xl:text-2xl text-xs font-bold quicksand py-2 bg-beauty px-4 rounded-full md:w-fit w-full";

  export let category;
</script>

<section>
  <h2 class="title">{category.title}</h2>
  <p class="text-white xl:text-base text-sm font-bold quicksand xl:py-8 py-4">
    {category.description}
  </p>

  <Gallery images="{category.images}" />

  <div class="w-full pt-8 flex justify-center gap-4 place-items-center">
    <ul class="flex flex-wrap w-full h-fit justify-center gap-4">
      {#each category.prices as price, index}
        <li class="md:w-fit w-full">
          <h3 class="{prices_classes}">
            {price.title} <span class="quicksand-bold">{price.price}</span><span
              class="font-semibold font-sans">€</span>
            {price.post_title}
          </h3>
        </li>
      {/each}
    </ul>
  </div>
  <hr class="my-12 h-0.5 border-t-0 bg-neutral-100/10" />
</section>
