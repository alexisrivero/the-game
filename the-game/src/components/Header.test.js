import React from 'react';
import { shallow, mount} from 'enzyme';
import sinon from 'sinon';
import Header from './Header'

describe ('<Header />', () => {
    it('renderea un elemento div', () => {
        const wrapper = shallow(<Header />);
        expect(wrapper.find('div').exists()).toBeTruthy();
    });
});