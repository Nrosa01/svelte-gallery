<script>
  import Image from "./Image.svelte";
  import ToggleButton from "./ToggleButton.svelte";

  export let images;
  const tags = ["All", "Comms", "Pokemon", "PMD", "Transform", "Zorio", "Nahi", "Other"]
</script>


<div class="w-full px-1">
  <ul class="flex flex-wrap w-fit h-fit">
    {#each tags as tag, i}
    <li class="flex-grow xl:m-2 m-1">
    <ToggleButton text={tag} enabled={i == 0}/>
    </li>
  {/each}
  </ul>
</div>

<div class="w-full">
  <ul class="flex flex-wrap w-full h-fit">
    {#each images as i}
       <Image bind:image={i} />
    {/each}
  </ul>
</div>
