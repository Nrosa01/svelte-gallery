<script>
    import { onMount } from "svelte";
    import {tag, activateTag, deactivateTag} from "../assets/ToggleStore.js";

    export let text = "Toggle";
    export let enabled = false;

    function toggle() {
      enabled = !enabled;
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
    class={`${enabled ? 'bg-blue-500 hover:bg-blue-700' : 'bg-gray-500 hover:bg-gray-700'} text-white font-bold py-2 px-4 rounded-full`}
    on:click={toggle}>
    {text}
  </button>
  