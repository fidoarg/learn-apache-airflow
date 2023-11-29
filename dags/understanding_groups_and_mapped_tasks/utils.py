from custom.logging import logger

def generate_input(number_of_inputs, **context):

  return [{f'value_to_compute': i+1} for i in range(number_of_inputs)]

def compute_input(value_to_compute):
  logger.info(f"Value to compute {value_to_compute}")
  if not value_to_compute % 2:
    logger.info("Number is even")
    return True
  else:
    logger.error("Number is odd")
    raise Exception("Number is odd")