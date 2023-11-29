from custom.logging import logger

def log_successful_run(msg, **context):

  logger.info(msg= msg)

  return f"msg logged successfully"
