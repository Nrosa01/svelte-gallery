<script>
    import Image from "./Image.svelte";

    export let images;
</script>

<div class="w-full">
    <ul class="flex flex-wrap w-full h-fit">
      {#each images as i}
         <Image image={i} thumbnail={{...i, src: i.src.replace('gallery\\', 'thumbnails\\')}}  />
      {/each}
    </ul>
  </div>