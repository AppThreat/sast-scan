import logging

import lib.config as config


def track(track_obj):
    """
    Method to send a track message to the telemetry api
    :param track_obj:
    :return:
    """
    # Check if telemetry is disabled
    disable_telemetry = config.get("DISABLE_TELEMETRY", False)
    if disable_telemetry == "true" or disable_telemetry == "1":
        disable_telemetry = True
    else:
        disable_telemetry = False
    if track_obj and not disable_telemetry:
        # configure your telemetry api server here
        logging.debug(track_obj)
