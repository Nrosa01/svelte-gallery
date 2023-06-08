<script>
  import { onMount, createEventDispatcher } from 'svelte';
  import { fade } from "svelte/transition";
  import { tag } from "../assets/ToggleStore.js";

  export let image;
  export let tags;
  export let index;
  let enabled = true;

  const dispatch = createEventDispatcher();

  onMount(() => {
    tag.subscribe(value => {
      enabled = false;
      requestAnimationFrame(() => {
        enabled = value == "All" || tags.includes(value.toLowerCase());
      });
    });
  });

  function handleClick() {
    dispatch('imageClick', index);
  }
</script>

{#if enabled}
  <li class="lg:h-[25vh] h-[20vw] flex-grow m-2" in:fade="{{duration: 400}}">
    <img
      class="max-h-full min-w-full object-cover align-bottom rounded-xl"
      src="{image.src}"
      alt="{image.title}"
      loading="lazy"
      on:click="{handleClick}"
      on:keydown
    />
  </li>
{/if}
