import React from 'react';
import { shallow, mount } from 'enzyme';
import Chorizo from './Chorizo';

describe('<Chorizo />', () => {
    it('renderea un elemento li', () => {
        const wrapper = mount(<Chorizo />);
        expect(wrapper.find('h1').exists()).toBeTruthy();
    });
});
//enzyme adentro jest afuera