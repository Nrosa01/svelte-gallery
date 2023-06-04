<script>
    import Image from "./Image.svelte";

  export let images;
  let div;
  let ul;

  let li_classes = "lg:h-[25vh] h-[20vw] flex-grow m-2";
</script>

<div bind:this={div}>
  <ul class="flex flex-wrap w-full h-fit" bind:this={ul}>
    {#each images as i, index}
      <li class="{li_classes}">
       <Image bind:image={i} />
      </li>
    {/each}
  </ul>
</div>
