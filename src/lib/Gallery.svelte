<script>
    import Image from "./Image.svelte";
    import ToggleButton from "./ToggleButton.svelte";

  export let images;
  const tags = ["All", "Comms", "Pokemon", "PMD", "Zorio", "Transform", "Nahi", "Other"]
</script>

<div class="flex flex-wrap  w-fit min-h-20 max-h-fit place-items-center justify-start gap-4 p-2">
    {#each tags as tag, i}
      <ToggleButton text={tag} enabled={i == 0}/>
    {/each}
</div>

<div class="w-full">
  <ul class="flex flex-wrap w-full h-fit">
    {#each images as i}
       <Image bind:image={i} />
    {/each}
  </ul>
</div>
