import React from 'react';
import { shallow } from 'enzyme';
import RatingEmpresa from './RatingEmpresa';
import * as Constants from '../Constants';

describe('<RatingEmpresa />', () => {
    it('renderea un elemento div', () => {
        const data = Constants.DATOS_PRUEBA_EMPRESA;
        const wrapper = shallow(<RatingEmpresa empresa={data} />);
        expect(wrapper.find('div').exists()).toBeTruthy();
        expect(wrapper.find('svg')) que sean 5;
    });
});