/*
#########################################################################
#
# Copyright (C) 2019 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################
*/

import { createAction } from 'redux-actions';
import { fetch, formatNow } from '../../../utils';
import apiUrl from '../../../backend';
import { INTERVAL } from './constants';
import { minute } from '../../../constants';


const reset = createAction(INTERVAL, () => ({ interval: 10 * minute }));


export const begin = createAction(
  INTERVAL,
  (interval) => ({
    interval,
    status: 'pending',
  })
);


const success = createAction(
  INTERVAL,
  (interval, response) => ({
    interval,
    from: new Date(response.data.input_valid_from),
    to: new Date(response.data.input_valid_to),
    timestamp: formatNow(),
    status: 'success',
  }),
);


const fail = createAction(
  INTERVAL,
  error => ({
    status: 'error',
    error,
  })
);


const get = (interval) =>
  (dispatch) => {
    dispatch(begin(interval));
    const url = `${apiUrl}/metric_data/response.error.count/?last=${interval}&interval=${interval}`;
    fetch({ url })
      .then(response => {
        dispatch(success(interval, response));
        return response;
      })
      .catch(error => {
        dispatch(fail(error.message));
      });
  };

const actions = {
  reset,
  begin,
  success,
  fail,
  get,
};

export default actions;
