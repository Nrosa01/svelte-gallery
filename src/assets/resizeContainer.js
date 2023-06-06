export default function resizeContainer(node) {
	function updateHeight() {
		const childrenHeight = [...node.children]
			.reduce((acc, item) => acc + item.offsetHeight, 0);
		node.style.setProperty('height', `${childrenHeight}px`);
	}
	
  const observer = new MutationObserver((mutations) => {
		updateHeight()
	});
  observer.observe(node, { characterData: true, subtree: true, childList: true });

  updateHeight();
	
	
  const shouldTransition = node.dataset.transition === 'true';

  if (shouldTransition) {
    node.style.setProperty('transition', 'width 500ms ease, height 500ms ease');
  } else {
    node.style.setProperty('transition', 'none');
  }
  
  return {
    destroy() {
      observer?.disconnect();
    },
  };
}