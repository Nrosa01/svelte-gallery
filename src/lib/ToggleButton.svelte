<script>
    import { onMount } from "svelte";
    import {tag, activateTag, deactivateTag} from "../assets/ToggleStore.js";

    export let text = "Toggle";
    export let enabled = false;

    function toggle() {
      enabled = text === "All" || !enabled;
        if (enabled)
            activateTag(text);
        else 
            deactivateTag();
    }

    onMount(() => {
      tag.subscribe(value => {
        if (value == text) {
          enabled = true;
        } else {
            enabled = false;
        }
      });
    });
  </script>
  
  <button
    class={`${enabled ? 'bg-blue-500 hover:bg-blue-700' : 'bg-gray-500 hover:bg-gray-700'} text-white font-bold py-2 px-4 rounded-full w-full text-xs xl:h-fit h-1 flex items-center justify-center`}
    on:click={toggle}>
    <span class="xl:text-base text-[0.5rem]">{text}</span>
  </button>
  