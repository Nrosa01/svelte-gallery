<script>
    import { onMount } from 'svelte';
  
    let showButton = false;
  
    onMount(() => {
      window.addEventListener('scroll', handleScroll);
      return () => {
        window.removeEventListener('scroll', handleScroll);
      };
    });
  
    function handleScroll() {
      const scrollThreshold = window.innerHeight * 0.01;
      showButton = window.pageYOffset > scrollThreshold;
    }
  
    function scrollToTop() {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  </script>
  
  <style>
    .fixed-button {
      position: fixed;
      bottom: 2rem;
      right: 2rem;
      opacity: 0;
      transition: opacity 0.3s;
    }
  
    .show-button {
      opacity: 1;
    }
  </style>
  
  <button
    class={`fixed-button ${showButton ? 'show-button' : ''} w-14 mr-4 z-10 bg-slate-900/75 rounded-full p-2`}
    on:click={scrollToTop}
    on:keydown
  >
    <img src="/site/up_arrow.png" alt="up arrow"/>
  </button>
  