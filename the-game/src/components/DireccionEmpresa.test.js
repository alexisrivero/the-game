import React from 'react';
import { shallow, mount} from 'enzyme';
import sinon from 'sinon';
import DireccionEmpresa from './DireccionEmpresa';

describe ('<DireccionEmpresa />', () => {
    it('renderea un elementi li', () => {
        const wrapper = shallow(<DireccionEmpresa />);
        expect(wrapper.find('li').exists()).toBeTruthy();
    });
});