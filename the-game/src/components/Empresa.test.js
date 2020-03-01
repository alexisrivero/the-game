import React from 'react';
import { shallow, mount } from 'enzyme';
import Empresa from './Empresa';

describe('<Empresa />', () => {
    it('renderea un elemento li', () => { 
        const wrapper = shallow(<Empresa />);
        expect(wrapper.find('li').exists()).toBeTruthy();
    });
});