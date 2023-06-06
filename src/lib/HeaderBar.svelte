<script>
    import IconBar from './IconBar.svelte';
    import pfp from '/site/pfp.jpg';

    const imgWrapperClass_not_home = "flex flex-row items-center w-full xl:h-20 min-h-10 h-fit justify-start gap-4 place-content-end"
    const img_not_home = "h-full min-h-[4rem] max-h-[6rem] p-1 rounded-full"
    const text_not_home = "xl:text-6xl text-5xl text-white font-black"
  </script>
  
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
      <div class="{imgWrapperClass_not_home}">
        <img src="{pfp}" class="{img_not_home}" alt="pfp" style="box-shadow: 0rem 1.75rem 2rem 0rem RGBA(28, 7, 54, 0.25)" />
        <h1 class="{text_not_home}" >Rioni</h1>
      </div>
    <div class="w-full" >
        <IconBar />
    </div>
  </div>
  