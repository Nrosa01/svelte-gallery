<script>
    import up_arrow from "/site/up_arrow.png";
  
    let showButton = false;
  
    function handleScroll() {
      const scrollThreshold = window.innerHeight * 0.25;
      showButton = window.pageYOffset > scrollThreshold;
    }
  
    function scrollToTop() {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  </script>
  
<svelte:window on:scroll={handleScroll} />

  <style>
    .fixed-button {
      position: fixed;
      bottom: 2rem;
      right: 2rem;
      opacity: 0;
      transition: opacity 0.3s;
    }
  
    .showButton {
      opacity: 1;
    }
  </style>
  
  <button
    class={`fixed-button xl:w-14 xl:p-3 w-10 p-[0.6rem] mr-4 z-10 bg-slate-900/75 rounded-full`}
    class:showButton
    on:click={scrollToTop}
    on:keydown
  >
    <img src="{up_arrow}" alt="up arrow"/>
  </button>
  