<script>
    import { onMount } from 'svelte';
    import { fade } from "svelte/transition";
    import { tag } from "../assets/ToggleStore.js";
  
    const animationType = "motion-safe:animate-fadeIn";
    export let image;
    let li;
    const li_classes = "lg:h-[25vh] h-[20vw] flex-grow m-2";
    let enabled = true;
    let expanded = false;
  
    function toggleExpansion() {
      expanded = !expanded;
    }
  
    onMount(() => {
      // Cerrar la imagen expandida al presionar la tecla Escape
      document.addEventListener('keydown', (event) => {
        if (event.key === 'Escape') {
          expanded = false;
        }
      });

      // Ocultar o desocultar la imagen si coincide su tag con el tag activo o si el tag activo es "All"
      tag.subscribe(value => {
        enabled = false;
        // wait 1 frame for the DOM to update then update enabled with the correct value
        requestAnimationFrame(() => {
          enabled = value == "All" || image.tags.includes(value.toLowerCase());
        });

      });
    });
  </script>
  
  {#if enabled}
  <li class="{li_classes}" bind:this="{li}" in:fade="{{duration: 400}}">
    <img
      data-animate-type="{animationType}"
      class="max-h-full min-w-full object-cover align-bottom rounded-xl js-show-on-scroll"
      src="{image.src}"
      alt="{image.alt}"
      loading="lazy"
      on:keydown
      on:click={toggleExpansion} />
  
    {#if expanded}
      <div class="fixed top-0 left-0 right-0 bottom-0 flex items-center justify-center bg-black bg-opacity-75 z-10" transition:fade="{{ duration: 125 }}" on:click={toggleExpansion} on:keydown>
        <img class="max-w-[90vw] max-h-[90vh]" src="{image.src}" alt="{image.alt}"/>
      </div>
    {/if}
</li>
{/if}