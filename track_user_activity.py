import logging

logging.basicConfig(filename='logs/activity.log', level=logging.INFO, format='%(asctime)s: %(message)s')

def track_activity():
    logging.info("User activity tracked")

if __name__ == "__main__":
    track_activity()
