import React from 'react';
import { shallow, mount} from 'enzyme';
import App from './App';

test('render div inicial', () => {
  const wrapper = shallow(<App />);
  expect(wrapper.find('div').exists()).toBeTruthy();
});
