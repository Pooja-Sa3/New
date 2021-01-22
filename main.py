from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
import stripe

app= Flask(__name__)
api= Api(app)


#arg to pass all data in JSON formet
payment_put_args= reqparse.RequestParser()
payment_put_args.add_argument("CreditCardNumber",type="str",help="It should be valid credit card number", required= True)
payment_put_args.add_argument("CardHolder",type="str",help="Please type name of Card holder", required=True)
payment_put_args.add_argument("ExpirationDate",type="datetime",help="Type a proper date", required=True)
payment_put_args.add_argument("Amount",type="decimal",help="Type a Positive amount", required= True)

#dict to store all data
payment={}


def abort_invalid_requests(CreditCardNumber, CardHolder, ExpirationDate, Amount):
    if CreditCardNumber or CardHolder or ExpirationDate or Amount == None:
        abort(400, "The request is invalid")
    else:
        return abort(400, "The request is invalid")


class Payment(Resource):

    def put(self, payment_id):
        args=payment_put_args.parse_args()
        payment[payment_id]=args
        if len(payment[CreditCardNumber])<16:
            return abort_invalid_requests
        if ExpirationDate< Date.today():
            return abort_invalid_requests
        if Amount<0:
            return abort_invalid_requests
        return payment[payment_id], 201



class CheapPaymentGateway.ToOne(Resource, Amount):
    def CheapPaymentGateway(self, Amount):
         if "Amount"<20:
            pass
class ExpensivePaymentGateway.ToOne(Resource, Amount):
     if (500>"Amount">20):
        def ExpensivePaymentGateway(self, Amount):
            try:
                session.execute()==True
                pass
            except:
                if session.execute()==False:
                    return CheapPaymentGateway
class PremiumPaymentGateway.ToOne(Resource, Amount):
     if "Amount">500:
        def PremiumPaymentGateway(self, Amount):
            if session.execute()==False:
                i=0
                while i<3:
                    PremiumPaymentGateway()
                    i+1
            else:
                return print("Session failed")




api.add_resource(Payment, "/payment/<int:payment_id>")


if __name__== "__main__":
    app.run(debug=True)