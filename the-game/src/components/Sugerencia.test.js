import React from "react";
import { shallow, mount } from "enzyme";
import Sugerencia from "./Sugerencia";

describe("<Sugerencia />", () => {
  it("renderea un elemento div", () => {
    const wrapper = mount(<Sugerencia />);
    expect(wrapper.find("div").exists()).toBeTruthy();
  });
  it("renderea un elemento ul", () => {
    const wrapper = shallow(<Sugerencia />);
    expect(wrapper.find("div").exists()).toBeTruthy();
  });
  it("renderea un elemento span", () => {
    const wrapper = shallow(<Sugerencia />);
    expect(wrapper.find("span").exists()).toBeTruthy();
  });
});
