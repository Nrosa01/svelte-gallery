<script>
  import _data from "./json/data.json";
  import pfp from "/site/pfp.jpg";
  import twitter from "/site/twitter.png";
  import devianart from "/site/devianart.png";
  import telegram from "/site/telegram.png";
  import discord from "/site/discord.png";
  import Gallery from "./lib/Gallery.svelte";

  let data = _data
</script>

<section>
  <div class="fixed top-0 left-0 right-0 bottom-0 bg-gradient"></div>
</section>

<main class="relative">
  <div
    class="flex flex-col h-auto min-h-screen justify-center place-items-center">
    <div
      class="flex flex-col w-[85vw] bg-slate-900/75 justify-center place-items-center rounded-[4rem] my-8">
      <div class="w-[90%]">
        <section class="w-full">
          <div class="grid grid-cols-2 place-items-center xl:pb-4 pt-8">
            <div
              class="flex flex-row items-center w-full xl:h-20 h-10 justify-start gap-4 place-content-end">
              <img
                src="{pfp}"
                class="h-full p-1 rounded-full"
                alt="pfp" />
              <h1 class="xl:text-6xl text-2xl text-white font-bold">Rioni</h1>
            </div>

            <div
              class="flex flex-raw w-full xl:h-20 h-10 items-center place-content-end pr-4">
              <a href="https://twitter.com/rionisguild" class="flex h-full place-items-center">
                <img src="{twitter}" alt="twitter" class="h-[70%]"/>
              </a>
              <a href="https://www.deviantart.com/srioni" class="flex h-full place-items-center">
                <img src="{devianart}" alt="devianart" class="h-[70%]" />
              </a>
              <a href="https://t.me/rionisguild" class="flex h-full place-items-center">
                <img src="{telegram}" alt="telegram" class="h-[70%]" />
              </a>
              <a href="https://discordapp.com/users/490599226200424448" class="flex h-full place-items-center">
                <img src="{discord}" alt="discord" class="h-[70%] pl-2" />
              </a>
            </div>
          </div>
        </section>

        <section>
          <Gallery bind:images={data} />
        </section>

        <footer class="flex flex-col w-full h-fit pt-2 pb-4 xl:px-16 px-8">
          <h1 class="xl:text-sm text-xs text-slate-300 text-center pb-4">
            The characters and trademarks mentioned are the property of their respective owners.
            their respective owners. This content is used for illustrative purposes only and is not intended to
            infringe the copyrights of the mentioned owners.
          </h1>
          <a href="https://www.flaticon.com/free-icons/" class="text-slate-300 text-center xl:text-sm text-xs" title="discord icons">Icons created by Freepik - Flaticon</a>
        </footer>
      </div>
    </div>
  </div>
</main>
