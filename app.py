from src.logger import logging

def main():

    try:
        logging.info("Starting the application")

        logging.info("Step 1: Initializing application")
        x = 5
        y = 2

        logging.info(f"Step 2: Performing operation: x={x}, y={y}")
        result = x + y

        logging.info(f"Step 3: Operation result: {result}")

        if result > 10:
            logging.warning(f"Step 4: Result {result} is greater than 10")
        else:
            logging.error(f"Step 4: Result {result} is less then 10")

    except Exception as e:

        logging.error("An error occurred in the main function", exc_info=True)
        raise e
    
if __name__ == "__main__":
    logging.info("="*50)
    logging.info("Application Run Started")
    logging.info("="*50)

    try:
        main()
        logging.info("Application completed successfully")
    except Exception as e:
        logging.error("Application failed", exc_info=True)
    finally:
        logging.info("="*50)
        logging.info("Application execution has ended")
        logging.info("="*50)
