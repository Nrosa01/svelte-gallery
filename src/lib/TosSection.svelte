<script>
  import BackButton from "./BackButton.svelte";
</script>

<div class="py-12">
  <div class="container mx-auto px-4">
    <h2 class="title-bold text-center mb-8">Terms of Service</h2>
    <p class="text-center text-white text-sm mb-8 quicksand">
      This is subject to change at any given point with no prior notice or
      possibility to claim. By commissioning me, Rioni, you agree to my Terms of
      Service.
    </p>

    <ul class="flex flex-wrap text-center quicksand">
      <li class="flex-grow xl:w-1/2 md:w-full xl:px-2 md:px-4 mb-8">
        <div class="xl:py-8 px-8 py-4">
          <h2 class="subtitle text-center mb-8">Will Draw</h2>
          <ul class=" text-white text-sm">
            <li>Pokemon OCs or Fanart</li>
            <li>Digimon OCs or Fanart</li>
            <li>Furry / Fursonas</li>
            <li>Any pokemon-like creature</li>
            <li>Post TF themed art</li>
            <li>Humans*</li>
            <li>Backgrounds</li>
            <li>NSFW*</li>
            <li>Up to 5 characters</li>
          </ul>
        </div>
      </li>

      <li class="flex-grow xl:w-1/2 md:w-full xl:px-2 md:px-4 mb-8">
        <div class="xl:py-8 px-8 py-4">
          <h2 class="subtitle text-center xl:mb-8 xl:mb-8 mb-4">Won't Draw</h2>
          <ul class=" text-white text-sm">
            <li>Mecha</li>
            <li>Gore</li>
            <li>Religious, political, ideological symbols</li>
            <li>Complex clothes</li>
          </ul>
        </div>
      </li>

      <li class="flex-grow w-full xl:w-1/2 xl:px-2 md:px-4 mb-8">
        <div class="xl:py-8 px-8 py-4">
          <h2 class="subtitle text-center mb-8">How to Order</h2>
          <p class="text-white text-sm xl:mb-8 mb-4">
            Send me a DM (<a href="https://twitter.com/rionisguild" class="link"
              >Twitter</a>
            or
            <a
              href="https://discordapp.com/users/490599226200424448"
              class="link">Discord</a
            >), or mail
            <a href="mailto:business@rioni.es" class="link">Rioni</a> with the following
            information:
          </p>
          <ul class=" text-white text-sm">
            <li>Commission type</li>
            <li>Character ref</li>
            <li>Pose / Drawing description</li>
            <li>Background (if any)</li>
          </ul>
          <p class="text-white text-sm mt-4">
            The more refs and info you provide, the better. But of course, if
            you don't have a clear idea of what you want, say you want a post tf
            art of your character but you don't know the pose, reaction, or
            setting. I'll try to come up with something that suits your
            character.
          </p>
        </div>
      </li>

      <li class="flex-grow w-full xl:w-1/2 xl:px-2 md:px-4 mb-8">
        <div class="xl:py-8 px-8 py-4">
          <h2 class="subtitle text-center mb-8">Process</h2>
          <p class="text-white text-sm">
            One or many rough sketches will be sent. Once the sketch is
            approved, payment must be done*. If you take advantage of this to
            get free sketches, I'll blacklist you. I'll send WIPs during the
            process. Changes can be requested, I encourage changes before an idea is agreed. 
            After a sketch is refined or lineart is done, changes might incur into additional costs depending on the complexity of the change.
            When payment time comes, I'll send you a paypal.me link.

            <br/>
            I reserve some artistic freedom, there are some things I draw in a specific way and won't change that.
          </p>
        </div>
      </li>

      <li class="flex-grow w-full xl:w-1/2 xl:px-2 md:px-4">
        <hr class="mt-2 mb-4 h-0.5 border-t-0 bg-neutral-100/10" />
        <div class="xl:py-8 px-8 py-4">
          <h2 class="subtitle text-center mb-8">Other Information</h2>
          <p class="text-white text-sm xl:mb-8 mb-4">
            ETA: 1-2 weeks<br />
            Non-commercial use<br />
            Payment is in Euros (€)<br />
            I save the right to post your drawing online as well as on my web. If
            you don't want your drawing to be public, you must tell me although that
            would incur into additional costs (20% more on the final price). I need a 2D ref, if possible unshaded.
            If the ref is 3D or I can't understand it well enough I will decline
            your commission.
          </p>
          <p class="text-white text-sm">
            Complex designs can incur into additional charges.<br />
            *I can draw humans, but I'm not really experienced with it. For post
            tf art, I can draw headshots. My struggles are complex body poses and
            hands.<br />
            All tiers are for fullbody, I'm not accepting headshots, but I do fullbodies as a secondary shot or complement to an existing fullbody drawing. All tiers have colour.<br />
            I reserve the right to decline a commission for any reason without having to explain it. <br />I'm not currently in a bad economic position so I will only take
            commissions that I really want to do. 
          </p>
          <br/>
          <p class="text-white text-sm">
            NSFW Terms:
            <label class="spoiler relative inline-block cursor-pointer">
              <!-- Checkbox to manage the spoiler without JS because I'm bored -->
              <input
                type="checkbox"
                class="absolute opacity-0 w-0 h-0 spoiler-checkbox" />

              <span class="spoiler-text relative z-10 text-transparent">
                I will only draw NSFW if I'm comfortable with it, just ask about
                it, I like a lots of kinks such as BDSM, size difference, pet
                play, watersports, forced, hypnosis, etc. NSFW prices are currently the same as
                for SFW art but this might change in the future, I'm still thinking about it.
                I won't draw underage characters in NSFW situations. You must be +18 to commission NSFW art, I will ask
                proof of this, I'm sorry if it's bothersome but I think it's necessary.
              </span>
              <span
                class="spoiler-cover absolute inset-0 bg-black/80 flex items-center justify-center transition-opacity duration-300 pointer-events-none">
                <div class="noise w-full h-full"></div>
              </span>
            </label>
          </p>
        </div>
      </li>
    </ul>

    <div class="w-full flex justify-center">
      <BackButton />
    </div>
  </div>
</div>

<style>
  .spoiler {
    position: relative;
    display: inline-block;
    cursor: pointer;
  }

  .spoiler-checkbox:checked ~ .spoiler-text {
    color: inherit;
  }

  .spoiler-checkbox:checked ~ .spoiler-cover {
    opacity: 0; 
  }

  .spoiler:hover .spoiler-cover {
    opacity: 0; 
  }

  .spoiler:hover .spoiler-text {
    color: inherit; 
  }

  .spoiler-text {
    transition: color 0.3s ease;
    color: transparent; 
  }

  .spoiler-cover {
    transition: opacity 0.3s ease;
    opacity: 1; 
  }

  @keyframes move {
    0% {
      transform: translate(0, 0);
    }
    100% {
      transform: translate(10px, 10px);
    }
  }
</style>
