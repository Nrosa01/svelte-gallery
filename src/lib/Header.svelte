<script>
    import IconBar from "./IconBar.svelte";
    import pfp from "/site/pfp.jpg";

    let currently_home = false;
    const imgWrapperClass_home = "grid grid-rows-3 justify-center text-center place-items-center w-full font-black"
    const imgWrapperClass_not_home = "flex flex-row items-center w-full xl:h-20 min-h-10 h-fit justify-start gap-4 place-content-end"

    const img_home = "w-[12rem] max-w-fit -4 rounded-full box-border row-span-2"
    const img_not_home = "h-full min-h-[4rem] max-h-[6rem] p-1 rounded-full"

    const text_home = "text-home"
    const text_not_home = "xl:text-6xl text-5xl text-white font-black"

    $: imgWrapperClass  = currently_home ? imgWrapperClass_home : imgWrapperClass_not_home
    $: imgClass         = currently_home ? img_home : img_not_home
    $: textClass        = currently_home ? text_home : text_not_home

    //toggle currently home with l button function
    function toggle_home(event) {
        if (event.key === "l") {
            currently_home = !currently_home;
        }
    }
</script>

<svelte:window on:keydown={toggle_home} />

<style>
  .text-home {
    font-family: quicksand_bold;
    letter-spacing: 0.125rem;
    font-size: 3.5em;
    line-height: 1.375;
    text-transform: uppercase;
    color: #FF8CA8;
    -webkit-text-fill-color: #FF8CA8;
    font-weight: 900;
  }
</style>

<div class="flex flex-col items-center lg:flex-row xl:justify-center xl:pb-4 my-8 pt-8 overflow-hidden transition-all">
  <div class="{imgWrapperClass}">
    <img src="{pfp}" class="{imgClass}" alt="pfp" style="box-shadow: 0rem 1.75rem 2rem 0rem RGBA(28, 7, 54, 0.25)" />
    <h1 class="{textClass}">Rioni</h1>
  </div>

  {#if currently_home}
    <div class="flex justify-center max-w-xs text-center px-4">
        <p class="text-white text-sm sm:text-lg xl:text-2xl">
            Hi!! I'm Rioni, I'm a game developer and hobbyist artist. My art is focused around Pokemon, my OCs and cute creatures in general.
        </p>
    </div>
  {:else}
      <IconBar/>
  {/if}
</div>
