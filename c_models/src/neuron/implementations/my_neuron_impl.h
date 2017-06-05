#ifndef _MY_NEURON_IMPL_H_
#define _MY_NEURON_IMPL_H_

#include <neuron/implementations/neuron_impl.h>

//! neuron_impl_t struct
typedef struct neuron_impl_t {
} neuron_impl_t;

//! Global variables
input_t gl_exc_input=0;
input_t exc_input_value=0;
input_t gl_inh_input=0;
input_t inh_input_value=0;

//! \brief Sets up the conversion of (voltage) inputs to current
//! \param[in] exc_value The value of the excitatory input before conversion
//! \param[in] inh_value The value of the inhibitory input before conversion
//! \param[in] input_type The input type pointer to the parameters
//! \param[in] voltage The voltage to use in conversion
//! \return None
static void neuron_impl_convert_inputs_to_current(
		input_t exc_value, input_t inh_value, input_type_pointer_t input_type,
		state_t voltage)
{
    exc_input_value = input_type_get_input_value(exc_value, input_type);
	inh_input_value = input_type_get_input_value(inh_value, input_type);

	neuron_impl_convert_excitatory_input_to_current(
			exc_input_value, input_type, voltage);
    input_type_set_inhibitory_multiplicator_value(gl_exc_input, input_type,
            		inh_input_value);
	neuron_impl_convert_inhibitory_input_to_current(
			inh_input_value, input_type, voltage);

}

//! \brief Sets up the conversion of an excitatory input to current
//! \param[in] exc_value The value of the excitatory input before conversion
//! \param[in] input_type The input type pointer to the parameters
//! \param[in] voltage The voltage to use in conversion
//! \return None
static void neuron_impl_convert_excitatory_input_to_current(
		input_t exc_input_value,
		input_type_pointer_t input_type, state_t voltage)
{
    gl_exc_input = input_type_convert_excitatory_input_to_current(
    		exc_input_value, input_type, voltage);
}

//! \brief Sets up the conversion of an inhibitory input to current
//! \param[in] inh_value The value of the inhibitory input before conversion
//! \param[in] input_type The input type pointer to the parameters
//! \param[in] voltage The voltage to use in conversion
//! \return None
static void neuron_impl_convert_inhibitory_input_to_current(
		input_t inh_input_value,
		input_type_pointer_t input_type, state_t voltage)
{
    gl_inh_input = input_type_convert_inhibitory_input_to_current(
    		inh_input_value, input_type, voltage);
}

//! \brief Gets the excitatory input value (after conversion)
//! \return The excitatory input value
static input_t neuron_impl_get_excitatory_input()
{
	return gl_exc_input;
}

//! \brief Gets the inhibitory input value (after conversion)
//! \return The inhibitory input value
static input_t neuron_impl_get_inhibitory_input()
{
	return gl_inh_input;
}

//! \brief Gets the value to be recorded as the excitatory value
//! return The excitatory value to be recorded
static input_t neuron_impl_get_recording_excitatory_value()
{
	return gl_exc_input;
}

//! \brief Gets the value to be recorded as the inhibitory value
//! return The inhibitory value to be recorded
static input_t neuron_impl_get_recording_inhibitory_value()
{
	return gl_inh_input;
}

#endif // _MY_NEURON_IMPL_H_
