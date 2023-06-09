<script>
  import { fade, fly } from "svelte/transition";
  import { tag } from "../assets/ToggleStore.js";
  import { onMount } from "svelte";

  export let images;
  let currentIndex;
  let imageHTML;

  let expanded = false;
  let loaded = false;
  let currentImage = null;
  let currentTag = "All";
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
      flyX *= -1;
      requestAnimationFrame(() => {
        imageHTML.src = currentImage.src;
        imageHTML.alt = currentImage.title;
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
    // Check if the click was made on the element itself
    if (event.target === this) {
      closeImage();
    }
  }

  function handleKeyDown(event) {
    if (!expanded) return;

    if (event.key === "Escape") {
      closeImage();
    } else if (event.key === "ArrowLeft") {
      handleLeftArrow();
    } else if (event.key === "ArrowRight") {
      handleRightArrow();
    }
  }

  function handleTouchStart(event) {
    if (!expanded) return;

    if (event.touches.length === 1) {
      const t = event.touches[0];
      touch.startX = t.clientX;
      touch.startY = t.clientY;
    }
  }

  function handleTouchEnd(event) {
    if (!expanded) return;

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

  function findNextIndex(startIndex, increment) {
    let nextIndex = (startIndex + increment + images.length) % images.length;

    // Probably not the most efficient way to do this, like I'm doing a linear search that involves checking against an array for every image
    // If I have time later I'll cache the indices I already have in a map or something, just in case the users really use the carousel view
    while (
      currentTag !== "all" &&
      !images[nextIndex].tags.includes(currentTag)
    ) {
      nextIndex = (nextIndex + increment + images.length) % images.length;
    }

    return nextIndex;
  }

  function handleLeftArrow() {
    if (!expanded) return;

    currentIndex = findNextIndex(currentIndex, -1);
    flyX = 40;
    flyY = 0;
    show(currentIndex);
  }

  function handleRightArrow() {
    if (!expanded) return;

    currentIndex = findNextIndex(currentIndex, 1);
    flyX = -40;
    flyY = 0;
    show(currentIndex);
  }

  onMount(() => {
    tag.subscribe((value) => {
      currentTag = value.toLowerCase();
    });
  });
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
        class="fixed top-0 left-0 right-0 bottom-0 z-5 flex flex-col items-center justify-center text-white animate-pulse select-none"
        transition:fade="{{ delay: 100 }}">
        <img class="loading-image" alt="loading nahi" />
        <span class="paragraph">Loading...</span>
      </div>
    {:else}
      <div
        on:touchstart="{handleTouchStart}"
        on:touchend="{handleTouchEnd}"
        class="z-50">
        <button class="close-button-t" on:click="{closeImage}" transition:fade>
        </button>
        <img
          bind:this="{imageHTML}"
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
