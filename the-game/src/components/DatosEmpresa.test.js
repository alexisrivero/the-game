import React from 'react';
import { shallow, mount} from 'enzyme';
import sinon from 'sinon';
import DatosEmpresa from './DatosEmpresa';

describe('<DatosEmpresa />', () => {
    it('renderea un elemento div', () => {
        const wrapper = shallow(<DatosEmpresa />);
        expect(wrapper.find('div').exists()).toBeTruthy();
    });
    it('renderea un elemento ul', () => {
        const wrapper = shallow(<DatosEmpresa />);
        expect(wrapper.find('ul').exists()).toBeTruthy();
    });
});