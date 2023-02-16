# Copyright (c) 2017 The University of Manchester
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pyNN.spiNNaker as sim
from .nwt_testbase import NwtTestBase
from python_models8.neuron.builds.my_model_curr_exp_my_additional_input \
    import MyModelCurrExpMyAdditionalInput

# Set the number of neurons to simulate
n_neurons = 1

# Set the run time of the execution
run_time = 1000


class TestMyModelCurrExpMyAdditionalInput(NwtTestBase):

    def do_run(self):
        sim.setup(timestep=1.0)
        input_pop = sim.Population(
            1, sim.SpikeSourceArray(range(0, run_time, 100)), label="input")
        test_pop = sim.Population(
            1, MyModelCurrExpMyAdditionalInput(
                my_neuron_parameter=-70.0, i_offset=0.0,
                my_additional_input_parameter=0.05),
            label="my_model_my_additional_input_pop")
        test_pop.record(['spikes', 'v'])
        sim.Projection(
            input_pop, test_pop, sim.AllToAllConnector(),
            receptor_type='excitatory',
            synapse_type=sim.StaticSynapse(weight=2.0))
        sim.run(run_time)
        neo = test_pop.get_data('all')
        sim.end()
        self.check_results(
            neo, [19, 47, 75, 102, 125, 153, 181, 205, 231, 259, 287, 309,
                  336, 364, 392, 413, 441, 469, 497, 517, 545, 573, 601, 623,
                  651, 679, 704, 729, 757, 785, 807, 834, 862, 890, 911, 939,
                  967, 995])

    def test_do_run(self):
        self.runsafe(self.do_run)
