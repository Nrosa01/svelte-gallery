<script>
  import { fade, fly } from "svelte/transition";

  export let images;
  let currentIndex;
  let container;

  let expanded = false;
  let loaded = false;
  let currentImage = null;

  function loadImage() {
    currentImage = images[currentIndex];
    loaded = false;
    const img = new Image();
    img.src = currentImage.src;
    img.onload = () => {
      loaded = true;
      requestAnimationFrame(() => {
        container.src = currentImage.src;
        container.alt = currentImage.title;
      });
    };
  }

  export function show(index) {
    currentIndex = index;
    expanded = true;
    loadImage();
  }

  function closeImage() {
    expanded = false;
  }

  function handleClickInside(event) {
    if (container && container.contains(event.target)) {
      closeImage();
    }
  }

  function handleKeyDown(event) {
    if (event.key === "Escape") {
      closeImage();
    }
  }

  function handleLeftArrow() {
    currentIndex = (currentIndex - 1 + images.length) % images.length;
    show(currentIndex);
  }

  function handleRightArrow() {
    currentIndex = (currentIndex + 1) % images.length;
    show(currentIndex);
  }
</script>

<svelte:window on:keydown="{handleKeyDown}" />

{#if expanded}
  <div
    class="fixed top-0 left-0 right-0 bottom-0 flex items-center justify-center bg-black bg-opacity-75 z-10 backdrop-blur-sm"
    transition:fade="{{ duration: 150 }}" on:click={handleClickInside}
    on:keydown>
    {#if !loaded}
      <div
        class="fixed top-0 left-0 right-0 bottom-0 z-10 flex flex-col items-center justify-center text-white animate-pulse select-none"
        transition:fade>
        <img class="loading-image" alt="loading nahi" />
        <span class="paragraph">Loading...</span>
      </div>
    {:else}
      <div>
        <button class="close-button-t" on:click="{closeImage}" transition:fade>
        </button>
        <img
          bind:this="{container}"
          class="max-w-[90vw] max-h-[90vh] z-50 select-none transition-transform duration-1000"
          loading="lazy"
          src="{currentImage.src}"
          alt="{currentImage.title}}"
          in:fly="{{ duration: 350, y: 20 }}"
          out:fly="{{ duration: 125, y: 20 }}"
          on:click={handleClickInside}
          on:keydown />
        <button
          class="left-arrow-t"
          on:click="{handleLeftArrow}"
          transition:fade>
        </button>
        <button
          class="right-arrow-t"
          on:click="{handleRightArrow}"
          transition:fade>
        </button>
      </div>
    {/if}
  </div>
{/if}
