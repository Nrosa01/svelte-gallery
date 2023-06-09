<script>
  import { fade, fly } from "svelte/transition";

  export let images;
  let currentIndex;
  let container;

  let expanded = false;
  let loaded = false;
  let currentImage = null;
  let touch = { startX: 0, startY: 0 };
  let flyX = 0;
  let flyY = 20;

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
    flyX = 0;
    flyY = 20;
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
    } else if (event.key === "ArrowLeft") {
      handleLeftArrow();
    } else if (event.key === "ArrowRight") {
      handleRightArrow();
    }
  }

  function handleTouchStart(event) {
    if (event.touches.length === 1) {
      const t = event.touches[0];
      touch.startX = t.clientX;
      touch.startY = t.clientY;
    }
  }

  function handleTouchEnd(event) {
    if (event.changedTouches.length === 1) {
      const t = event.changedTouches[0];
      const deltaX = t.clientX - touch.startX;
      const deltaY = t.clientY - touch.startY;
      const absDeltaX = Math.abs(deltaX);
      const absDeltaY = Math.abs(deltaY);

      if (absDeltaX > absDeltaY) {
        if (deltaX > 0) {
          handleLeftArrow();
        } else {
          handleRightArrow();
        }
      }
    }
  }

  function handleLeftArrow() {
    currentIndex = (currentIndex - 1 + images.length) % images.length;
    flyX = -40
    flyY = 0
    show(currentIndex);
  }

  function handleRightArrow() {
    currentIndex = (currentIndex + 1) % images.length;
    flyX = 40
    flyY = 0
    show(currentIndex);
  }
</script>

<svelte:window on:keydown="{handleKeyDown}" />

{#if expanded}
  <div
    class="fixed top-0 left-0 right-0 bottom-0 flex items-center justify-center bg-black bg-opacity-75 z-10 backdrop-blur-sm"
    transition:fade="{{ duration: 150 }}"
    on:click="{handleClickInside}"
    on:keydown>
    {#if !loaded}
      <div
        class="fixed top-0 left-0 right-0 bottom-0 z-10 flex flex-col items-center justify-center text-white animate-pulse select-none"
        transition:fade>
        <img class="loading-image" alt="loading nahi" />
        <span class="paragraph">Loading...</span>
      </div>
    {:else}
      <div on:touchstart="{handleTouchStart}" on:touchend="{handleTouchEnd}">
        <button class="close-button-t" on:click="{closeImage}" transition:fade>
        </button>
        <img
          bind:this="{container}"
          class="max-w-[90vw] max-h-[90vh] z-50 select-none transition-transform duration-1000"
          loading="lazy"
          src="{currentImage.src}"
          alt="{currentImage.title}}"
          in:fly="{{ duration: 350, y: flyY, x: flyX }}"
          out:fly="{{ duration: 125, y: flyY * 4, x: flyX }}"
          on:click="{handleClickInside}"
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
