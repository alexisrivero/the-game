import React from 'react';
import { shallow } from 'enzyme';
import RatingEmpresa from './RatingEmpresa';
import * as Constants from '../Constants';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'

describe('<RatingEmpresa />', () => {
    it('renderea un elemento div', () => {
        const data = Constants.DATOS_PRUEBA_EMPRESA;
        const wrapper = shallow(<RatingEmpresa empresa={data} />);
        expect(wrapper.find('div').exists()).toBeTruthy();
        expect(wrapper.find(FontAwesomeIcon).length).toBe(5);
    });
});