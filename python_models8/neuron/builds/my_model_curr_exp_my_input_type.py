# main interface to use the spynnaker related tools.
# ALL MODELS MUST INHERIT FROM THIS
from spynnaker.pyNN.models.neuron.abstract_population_vertex \
    import AbstractPopulationVertex

from python_models8.neuron.input_types.my_input_type \
    import MyInputType
from python_models8.neuron.neuron_models.my_neuron_model \
    import MyNeuronModel
from spynnaker.pyNN.models.neuron.synapse_types.synapse_type_exponential\
    import SynapseTypeExponential
from spynnaker.pyNN.models.neuron.threshold_types.threshold_type_static\
    import ThresholdTypeStatic


class MyModelCurrExpMyInputTypeBase(AbstractPopulationVertex):

    # the maximum number of atoms per core that can be supported
    _model_based_max_atoms_per_core = 256

    # default parameters for this build. Used when end user has not entered any
    default_parameters = {
        'v_thresh': -50.0, 'tau_syn_E': 5.0, 'tau_syn_I': 5.0,
        'isyn_exc': 0.0, 'isyn_inh': 0.0,
        'i_offset': 0, 'my_parameter': -70.0,
        'my_multiplicator': 0.0, 'my_input_parameter': 0.0}

    initialize_parameters = {'v_init': None}

    def __init__(
            self, n_neurons, spikes_per_second=None, ring_buffer_sigma=None,
            incoming_spike_buffer_size=None, constraints=None, label=None,

            # neuron model parameters
            my_parameter=default_parameters['my_parameter'],
            i_offset=default_parameters['i_offset'],

            # threshold types parameters
            v_thresh=default_parameters['v_thresh'],

            # synapse type parameters
            tau_syn_E=default_parameters['tau_syn_E'],
            tau_syn_I=default_parameters['tau_syn_I'],
            isyn_exc=default_parameters['isyn_exc'],
            isyn_inh=default_parameters['isyn_inh'],

            # input type parameters
            my_multiplicator=(default_parameters['my_multiplicator']),
            my_input_parameter=(default_parameters['my_input_parameter']),

            # state variables
            v_init=None):

        # create neuron model class
        neuron_model = MyNeuronModel(
            n_neurons, i_offset, my_parameter)

        # create synapse type model
        synapse_type = SynapseTypeExponential(
            n_neurons, tau_syn_E, tau_syn_I, isyn_exc, isyn_inh)

        # create input type model
        input_type = MyInputType(
            n_neurons, my_multiplicator, my_input_parameter)

        # create threshold type model
        threshold_type = ThresholdTypeStatic(
            n_neurons, v_thresh)

        # create additional inputs
        additional_input = None

        # instantiate the sPyNNaker system by initialising
        #  the AbstractPopulationVertex
        AbstractPopulationVertex.__init__(

            # standard inputs, do not need to change.
            self, n_neurons=n_neurons, label=label,
            spikes_per_second=spikes_per_second,
            ring_buffer_sigma=ring_buffer_sigma,
            incoming_spike_buffer_size=incoming_spike_buffer_size,

            max_atoms_per_core=(
                MyModelCurrExpMyInputTypeBase.
                _model_based_max_atoms_per_core),

            # the various model types
            neuron_model=neuron_model, input_type=input_type,
            synapse_type=synapse_type, threshold_type=threshold_type,
            additional_input=additional_input,

            # the model a name (shown in reports)
            model_name="MyModelCurrExpMyInputType",

            # the matching binary name
            binary="my_model_curr_exp_my_input_type.aplx")

    @staticmethod
    def get_max_atoms_per_core():

        return (
            MyModelCurrExpMyInputTypeBase._model_based_max_atoms_per_core
        )

    @staticmethod
    def set_max_atoms_per_core(new_value):

        MyModelCurrExpMyInputTypeBase._model_based_max_atoms_per_core = \
            new_value

    @property
    def my_parameter(self):
        return self.default_parameters['my_parameter']

    @property
    def my_input_parameter(self):
        return self.default_parameters['my_input_parameter']

    @property
    def my_multiplicator(self):
        return self.default_parameters['my_multiplicator']
