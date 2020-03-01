import React from 'react';
import { shallow, mount} from 'enzyme';
import sinon from 'sinon';
import DatosEmpresa from './DatosEmpresa';

describe('<DatosEmpresa />', () => {
    it('renderea un elemento div', () => {
        const wrapper = shallow(<DatosEmpresa empresa="" />);
        expect(wrapper.find('div').exists()).toBeTruthy();
    });
});