import React from 'react';
import { shallow, mount} from 'enzyme';
import sinon from 'sinon';
import HeaderLogo from './HeaderLogo';

describe('<HeaderLogo />', () => {
    it('renderea un elemento div', () => {
        const wrapper = shallow(<HeaderLogo />);
        expect(wrapper.find('div').exists()).toBeTruthy();
    });
    it('renderea un elemento a', () => {
        const wrapper = shallow (<HeaderLogo />);
        expect(wrapper.find('div').exists()).toBeTruthy();
    });
    it('renderea un elemento img', () => {
        const wrapper = shallow (<HeaderLogo />);
        expect(wrapper.find('img').exists()).toBeTruthy();
    });
});