<script>
  import prices_shaded from "../../../json/prices_shaded.json";
  import prices_lined from "../../../json/prices_lined.json";
  import prices_posttf from "../../../json/prices_posttf.json";
  import BackButton from "./BackButton.svelte";
  import PriceListing from "./PriceListing.svelte";

  const categories = [
    {
      title: "POST TF DOODLE PAGE",
      description:
        "A simple 3-5 panel sequence showing a character already transformed reacting to his new body or in some situation due to it. These drawings are a flat style with minimal shading and they are a kinda more simplified than other of my drawings. Simple Background is included in this tier.",
      images: prices_posttf,
      prices:
      [
        {
          title: "Base price starting at",
          price: "45",
          post_title: "",
        },
      ]
    },
    {
      title: "Shaded / Painting",
      description:
        "This is the kind of work I usually upload to social medias. It can be lined but I tend to prefer doing lineless. Fullbody.",
      images: prices_shaded,
      prices:
      [
        {
          title: "Base price starting at",
          price: "50",
          post_title: "per character",
        },
        {
          title: "Simple background",
          price: "+15",
          post_title: "",
        },
        {
          title: "Complex background",
          price: "+30",
          post_title: "",
        }
      ]
    },
    {
      title: "LINED / MINIMAL SHADING",
      description:
        "This gets you a clean lined drawing with flat colours and some minimal shading. Fullbody.",
      images: prices_lined,
      prices:
      [
        {
          title: "Base price starting at",
          price: "30",
          post_title: "per character",
        },
        {
          title: "Simple background",
          price: "+15",
          post_title: "",
        },
        {
          title: "Complex background",
          price: "+30",
          post_title: "",
        }
      ]
    },
  ];
</script>

<div
  class="w-full text-center items-center justify-center place-content-center flex flex-col">
  {#each categories as category, index}
    <PriceListing category="{category}" />
  {/each}

  <section class="flex flex-col w-full items-center justify-center">
    <p>
      <span class="block text-white text-sm font-bold quicksand">
        Extra Character price may vary depending on the difficulty.
      </span>
      <span
        class="block text-white xl:text-xl text-lg font-bold quicksand xl:py-4 py-2">
        Feel free to DM me about any doubt or inquiry! <strong
          class="quicksand-bold"
          >You can request things that aren't listed here.</strong>
      </span>
    </p>
  </section>

  <BackButton />
</div>
