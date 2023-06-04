import { writable } from 'svelte/store';

export const tag = writable("All");

export function activateTag(tagtolower) {
  tag.update(() => tagtolower);
}

export function deactivateTag() {
  tag.update(() => "All");
}
