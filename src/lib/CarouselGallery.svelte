<script>
    import { fade, fly } from "svelte/transition";
    
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
  <div class="fixed top-0 left-0 right-0 bottom-0 flex items-center justify-center bg-black bg-opacity-75 z-10 backdrop-blur-sm" transition:fade="{{ duration: 150 }}">
    {#if !loaded}
    <div class="fixed top-0 left-0 right-0 bottom-0 z-10 flex flex-col items-center justify-center text-white animate-pulse select-none" transition:fade>
          <img class="loading-image" alt="loading nahi"/>
      <span class="paragraph">Loading...</span>
    </div>
    {:else}
    <div>
      <button class="close-button-t" on:click={closeImage}>
      </button>
      <img class="max-w-[90vw] max-h-[90vh] z-50 select-none {expanded ? "translate-y-0" : "translate-y-10"} transition-transform duration-1000 " src="{currentImage.src}" alt="{currentImage.alt}" loading="lazy"  in:fly="{{ duration: 350, y: 20 }}" out:fly="{{ duration: 125, y: 20 }}">
      <button class="left-arrow fixed top-1/2 left-2 transform -translate-y-1/2 p-2 text-white z-50">
        <span class="left-arrow-icon"></span>
      </button>
      <button class="right-arrow fixed top-1/2 right-2 transform -translate-y-1/2 p-2 text-white z-50">
        <span class="right-arrow-icon"></span>
      </button>
    </div>
    {/if}
  </div>
  {/if}
  