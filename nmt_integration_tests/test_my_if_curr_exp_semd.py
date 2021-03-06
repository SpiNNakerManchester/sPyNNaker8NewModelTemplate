# Copyright (c) 2017-2019 The University of Manchester
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import spynnaker8 as sim
from .nwt_testbase import NwtTestBase
from python_models8.neuron.builds.my_if_curr_exp_sEMD import MyIFCurrExpSEMD

# Set the run time of the execution
run_time = 1000


class TestMyIFCurrExpSEMD(NwtTestBase):

    def do_run(self):
        sim.setup(timestep=1.0)
        input_pop = sim.Population(
            1, sim.SpikeSourceArray(range(0, run_time, 100)), label="input")
        test_pop = sim.Population(
            1, MyIFCurrExpSEMD(my_multiplicator=0.0,
                               my_inh_input_previous=0.0),
            label="my_if_curr_exp_semd_pop")
        test_pop.record(['spikes', 'v'])
        sim.Projection(
            input_pop, test_pop, sim.AllToAllConnector(),
            receptor_type='excitatory',
            synapse_type=sim.StaticSynapse(weight=5.0))
        sim.run(run_time)
        neo = test_pop.get_data('all')
        sim.end()
        self.check_results(neo, [7, 107, 207, 307, 407,
                                 507, 607, 707, 807, 907])

    def test_do_run(self):
        self.runsafe(self.do_run)
