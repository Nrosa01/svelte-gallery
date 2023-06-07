<script>
    import { onMount } from 'svelte';
    import { fade } from "svelte/transition";
    import { tag } from "../assets/ToggleStore.js";
  
    export let image;
    export let thumbnail;
    let enabled = true;
    let expanded = false;
  
    function toggleExpansion() {
      expanded = !expanded;
    }
  
    onMount(() => {
      
      tag.subscribe(value => {
        enabled = false;
        // wait 1 frame for the DOM to update then update enabled with the correct value
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
  </script>
  
  <svelte:window on:keydown="{escape}" />

  {#if enabled}
  <li class="lg:h-[25vh] h-[20vw] flex-grow m-2" in:fade="{{duration: 400}}">
    <img
      class="max-h-full min-w-full object-cover align-bottom rounded-xl"
      src="{thumbnail.src}"
      alt="{thumbnail.title}"
      loading="lazy"
      on:keydown
      on:click={toggleExpansion} />
  
    {#if expanded}
      <div class="fixed top-0 left-0 right-0 bottom-0 flex items-center justify-center bg-black bg-opacity-75 z-10" transition:fade="{{ duration: 125 }}" on:click={toggleExpansion} on:keydown>
        <img class="max-w-[90vw] max-h-[90vh]" src="{image.src}" alt="{image.alt}" loading="lazy">
      </div>
    {/if}
</li>
{/if}