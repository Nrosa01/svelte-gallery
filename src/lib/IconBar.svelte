<script>
  import twitter from "/site/twitter.webp";
  import devianart from "/site/devianart.webp";
  import telegram from "/site/telegram.webp";
  import discord from "/site/discord.webp";

  export let position = "end"
  export let maxWHeight = "20"
</script>

<div
  class="flex flex-raw w-full xl:h-{maxWHeight} h-10 max-h-fit items-center place-content-{position} pr-4">
  <a
    href="https://twitter.com/rionisguild"
    class="flex h-full place-items-center">
    <img src="{twitter}" alt="twitter" class="h-[70%]" />
  </a>
  <a
    href="https://www.deviantart.com/srioni"
    class="flex h-full place-items-center">
    <img src="{devianart}" alt="devianart" class="h-[70%]" />
  </a>
  <a href="https://t.me/rionisguild" class="flex h-full place-items-center">
    <img src="{telegram}" alt="telegram" class="h-[70%]" />
  </a>
  <a
    href="https://discordapp.com/users/490599226200424448"
    class="flex h-full place-items-center">
    <img src="{discord}" alt="discord" class="h-[70%] pl-2" />
  </a>
</div>
