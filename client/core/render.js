export function render(obj) {
  const element = document.createElement(obj.tagName);
  element.className = obj.className;
  element.insertAdjacentHTML("beforeend", obj.children);
  element.addEventListener("click", obj.events);

  for (const key in obj.attrs) {
    const value = obj.attrs[key];
    element.setAttribute(key, value);
  }

  return element;
}
