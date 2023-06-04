<script>
    import { onMount } from "svelte";
    import {tag, activateTag, deactivateTag} from "../assets/ToggleStore.js";

    export let text = "Toggle";
    export let color = 'blue';
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
        console.log("My Text: " + text + " Value: " + value)
        if (value == text) {
          enabled = true;
        } else {
          enabled = false;
        }
      });
    });
  </script>
  
  <button
    class={`${enabled ? 'bg-' + color + '-500 hover:bg-' + color + '-700' : 'bg-gray-500 hover:bg-gray-700'} text-white font-bold py-2 px-4 rounded-full`}
    on:click={toggle}
  >
    {text}
  </button>
  