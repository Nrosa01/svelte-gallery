<script>
  import prices_shaded from "../json/prices_shaded.json";
  import prices_lined from "../json/prices_lined.json";
  import prices_posttf from "../json/prices_posttf.json";
  import BackButton from "./BackButton.svelte";
  import PriceListing from "./PriceListing.svelte";

  const categories = [
    {
      title: "DOODLE/COMIC PAGE",
      description:
        "A simple 3-6 panel of a sequence of actions or just different drawing of your character. The characters are drawn simpler and looser than in other tiers, some minimal shading is included. A simple background is included in this tier. Examples show post tf comic because this previously called 'post tf doodle page', but really this can be anything you want. This tier also work for 2 character interactions and in general, it's suitable for any multi character drawing. The more characters, the looser and less detailed.",
      images: prices_posttf,
      prices:
      [
        {
          title: "Base price starting at",
          price: "45",
          post_title: "",
        },
        {
          title: "Rough shading",
          price: "+20",
          post_title: "",
        },
      ]
    },
    {
      title: "Fully Shaded / Painting",
      description:
        "This is the kind of work I usually upload to social medias. It's more polished than the previous tier. Can be either thin line, lineless or a mix of both. Fullbody.",
      images: prices_shaded,
      prices:
      [
        {
          title: "Base price starting at",
          price: "50",
          post_title: "per character",
        },
        {
          title: "Background",
          price: "+15",
          post_title: "",
        },
        // {
        //   title: "Complex background",
        //   price: "+30",
        //   post_title: "",
        // }
      ]
    },
    {
      title: "Simple shaded",
      description:
        "This gets you a semi clean line with some shading, usually only one shade layer and one light layer. Can be either thin line, lineless or a mix of both. Fullbody.",
      images: prices_lined,
      prices:
      [
        {
          title: "Base price starting at",
          price: "35",
          post_title: "per character",
        },
        {
          title: "Background",
          price: "+15",
          post_title: "",
        },
        // {
        //   title: "Complex background",
        //   price: "+30",
        //   post_title: "",
        // }
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
        More complex backgrounds may incur into additional charges.
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
