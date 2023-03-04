export class Component {
  // this equal to self
  constructor(options) {
    const { tagName, className, children, events, ...attrs } = options;

    this.tagName = tagName;
    this.className = className;
    this.children = children;
    this.events = events;
    this.attrs = attrs;
  }
}
