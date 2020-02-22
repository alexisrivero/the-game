import React from 'react';
import { shallow, mount } from 'enzyme';
import sinon from 'sinon';
import Footer from './Footer';

describe('</Footer />', () => {
    it('renderea un elemento div', () => {
        const wrapper = shallow(<Footer />);
        expect(wrapper.find('div').exists()).toBeTruthy();
    });
});