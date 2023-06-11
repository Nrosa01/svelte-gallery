<script>
    import CarouselGallery from "./CarouselGallery.svelte";
    import Image from "./Image.svelte";
  
    export let images;
    let carousel = null;
  
    function handleImageClick(event) {
      carousel.show(event.detail);
    }
  </script>
  
  <div class="w-full">
    <ul class="flex flex-wrap w-full h-fit">
      {#each images as image, index}
        <Image
          tags={image.tags}
          image={{...image, src: image.src.replace('gallery\\', 'thumbnails\\')}}
          {index}
          on:imageClick={handleImageClick}
        />
      {/each}
    </ul>
  </div>
  
  <CarouselGallery bind:this={carousel} {images} />
  