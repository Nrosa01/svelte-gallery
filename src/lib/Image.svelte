<script>
  import { onMount } from 'svelte';
  import { fade } from "svelte/transition";
  import { tag } from "../assets/ToggleStore.js";

  export let image;
  export let thumbnail;
  let enabled = true;
  let expanded = false;
  let loaded = false; // Variable para controlar el estado de carga

  function toggleExpansion() {
    expanded = !expanded;
    if (expanded && !loaded) {
      loadImage();
    }
  }

  onMount(() => {
    tag.subscribe(value => {
      enabled = false;
      requestAnimationFrame(() => {
        enabled = value == "All" || image.tags.includes(value.toLowerCase());
      });
    });
  });

  function escape(event) {
    if (event.key === 'Escape') {
      expanded = false;
    }
  }

  function loadImage() {
    console.log("Loading image")
    const img = new Image();
    img.src = image.src;
    img.onload = () => {
      loaded = true;
    };
  }
</script>

<svelte:window on:keydown="{escape}" />

{#if enabled}
  <li class="lg:h-[25vh] h-[20vw] flex-grow m-2" in:fade="{{duration: 400}}">
    <img
      class="max-h-full min-w-full object-cover align-bottom rounded-xl"
      src="{thumbnail.src}"
      alt="{thumbnail.title}"
      loading="lazy"
      on:click="{toggleExpansion}"
      on:keydown
    />
  
    {#if expanded}
      <div class="fixed top-0 left-0 right-0 bottom-0 flex items-center justify-center bg-black bg-opacity-75 z-10 backdrop-blur-sm" transition:fade="{{ duration: 125 }}" on:click="{toggleExpansion}" on:keydown>
        {#if !loaded}
          <div class="fixed top-0 left-0 right-0 bottom-0 z-10 flex flex-col items-center justify-center text-white animate-pulse" transition:fade>
            <img class="loading-image" alt="loading nahi"/>
            <span class="paragraph">Loading...</span>
          </div>
        {:else}
          <img class="max-w-[90vw] max-h-[90vh] z-50" in:fade src="{image.src}" alt="{image.alt}" loading="lazy">
        {/if}
      </div>
    {/if}
  </li>
{/if}
