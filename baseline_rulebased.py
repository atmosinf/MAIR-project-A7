class BaselineRuleBased:
    def __init__(self):
        # self.ack = ["kay", "okay "]#, "good", "thatll do"]
        # self.affirm = ["yes", "right", "correct"]
        # self.bye = ["bye", "goodbye"]
        # self.confirm = ["is it", "is there", "does it", "do they", "is that"]
        # self.deny = ["wrong", "dont"]
        # self.hello = ["hi", "hello"]
        # self.inform = ["north", "east", "south", "west", "cheap", "restaurant"]
        # self.negate = ["no", "not"]
        # self.null = ["sil", "cough", "unintelligible"]
        # self.repeat = ["again", "repeat", "go back", "back"]
        # self.reqalts = ["how about", "anything else", "are there any", "is there another"]
        # self.reqmore = ["more"]
        # self.request = ["address", "phone", "number", "expensive", "scottish", "asian", "fushion", "post code"]
        # self.restart = ["start over", "reset", "start again"]
        # self.thankyou = ["thank you"]
        self.ack = ['kay', 'okay']
        self.affirm = ['yes', 'right']
        self.bye = ['goodbye', 'bye']
        self.confirm = ['serve']
        self.deny = ['wrong', 'dont', 'not']
        self.hello = ['hi ', 'hello', 'halo']
        self.inform = ['north', 'east', 'south', 'west', 'restaurant', 'priced', 'any', 'scottish', 'bistro', 'cheap', 'expensive', 'town', 'looking', 'mediterranean', 'seafood'] 
        self.negate = ['no']
        self.null = ['sil', 'cough', 'background_speech']
        self.repeat = ['again', 'repeat', 'back']
        self.reqalts = ['how', 'about', 'else']
        self.reqmore = ['more']
        self.request = ['address', 'postcode', 'phone', 'post']
        self.restart = ['reset', 'start']
        self.thankyou = ['thank']

    def predict(self, data): 
        predicted_results = []

        for value in data:
            words_list = value.split(" ")

            ack_res = any(elem in words_list for elem in self.ack)
            affirm_res = any(elem in words_list for elem in self.affirm)
            bye_res = any(elem in words_list for elem in self.bye)
            confirm_res = any(elem in words_list for elem in self.confirm)
            deny_res = any(elem in words_list for elem in self.deny)
            hello_res = any(elem in words_list for elem in self.hello)
            inform_res = any(elem in words_list for elem in self.inform)
            negate_res = any(elem in words_list for elem in self.negate)
            null_res = any(elem in words_list for elem in self.null)
            repeat_res = any(elem in words_list for elem in self.repeat)
            reqalts_res = any(elem in words_list for elem in self.reqalts)
            reqmore_res = any(elem in words_list for elem in self.reqmore)
            request_res = any(elem in words_list for elem in self.request)
            restart_res = any(elem in words_list for elem in self.restart)
            thankyou_res = any(elem in words_list for elem in self.thankyou)

            if inform_res:
                predicted_results.append("inform")
            elif request_res:
                predicted_results.append("request")    
            elif thankyou_res:
                predicted_results.append("thankyou")
            elif reqalts_res:
                predicted_results.append("reqalts")
            elif null_res:
                predicted_results.append("null")
            elif affirm_res:
                predicted_results.append("affirm")
            elif negate_res:
                predicted_results.append("negate")
            elif bye_res:
                predicted_results.append("bye")
            elif confirm_res:
                predicted_results.append("confirm")
            elif hello_res:
                predicted_results.append("hello")
            elif repeat_res:
                predicted_results.append("repeat")
            elif ack_res:
                predicted_results.append("ack")
            elif deny_res:
                predicted_results.append("deny")
            elif restart_res:
                predicted_results.append("restart")
            elif reqmore_res:
                predicted_results.append("reqmore")
            else:
                predicted_results.append("inform")
                #print(value, [ack_res, affirm_res, bye_res, confirm_res, deny_res, hello_res, inform_res, negate_res, null_res, repeat_res, reqalts_res, reqmore_res, request_res, restart_res, thankyou_res])
            
        return predicted_results
        ...