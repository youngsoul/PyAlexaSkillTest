from pyalexaskill.AlexaBaseHandler import AlexaBaseHandler


class AlexaDeploymentTestHandler(AlexaBaseHandler):
    """
    Sample concrete implementation of the AlexaBaseHandler to test the
    deployment scripts and process.
    All on_ handlers call the same test response changing the request type
    spoken.
    """

    def __init__(self):
        super(self.__class__, self).__init__()


    def _test_response(self, msg):
        session_attributes = {}
        card_title = "Test Response"
        card_output = "Test card output"
        speech_output = "Welcome to the Python Alexa Test Deployment.  {0}.  It seems to have worked".format(
            msg)
        # If the user either does not reply to the welcome message or says something
        # that is not understood, they will be prompted again with this text.
        reprompt_text = "Reprompt text for the Alexa Test Deployment"
        should_end_session = True

        speechlet = self._build_speechlet_response(card_title, card_output, speech_output, reprompt_text,
                                                   should_end_session)

        return self._build_response(session_attributes, speechlet)


    def on_processing_error(self, event, context, exc):
        return self._test_response("Request type on processing error")


    def on_launchrequest(self, launch_request, session):
        return self._test_response("Request type on launch")


    def on_session_started(self, session_started_request, session):
        return self._test_response("Request type on session started")


    def on_intent(self, intent_request, session):
        return self._test_response("Request type on intent")


    def on_session_ended(self, session_end_request, session):
        return self._test_response("Request type on session end")

    def on_sayhellointent_intent(self, intent_request, session ):
        return self._test_response("I just wanted to say hello")
