<script>
    import { fade } from "svelte/transition";
    
    export let images;
    let currentIndex;
    
    let expanded = false;
    let loaded = false;
    
    $: currentImage = currentIndex !== -1 ? images[currentIndex] : null;
    
    $: {
      if (currentImage) {
        loadImage();
      }
    }
    
    function loadImage() {
      loaded = false;
      const img = new Image();
      img.src = currentImage.src;
      img.onload = () => {
        loaded = true;
      };
    }
    
    export function show(index) {
      currentIndex = index;
      expanded = true;
    }
    
    function closeImage() {
      expanded = false;
    }
    
    function handleKeyDown(event) {
      if (event.key === "Escape") {
        closeImage();
      }
    }
  </script>
  
  <svelte:window on:keydown="{handleKeyDown}" />
  
  {#if expanded}
    <div class="fixed top-0 left-0 right-0 bottom-0 flex items-center justify-center bg-black bg-opacity-75 z-10 backdrop-blur-sm" transition:fade="{{ duration: 125 }}">
      {#if !loaded}
        <div class="fixed top-0 left-0 right-0 bottom-0 z-10 flex flex-col items-center justify-center text-white animate-pulse select-none" transition:fade>
          <img class="loading-image" alt="loading nahi"/>
          <span class="paragraph">Loading...</span>
        </div>
      {:else}
    <div>
      <button class="close-button-t" on:click={closeImage}>
      </button>
        <img class="max-w-[90vw] max-h-[90vh] z-50 select-none" in:fade src="{currentImage.src}" alt="{currentImage.alt}" loading="lazy">
    </div>
      {/if}
    </div>
  {/if}
  