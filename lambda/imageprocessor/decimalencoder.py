import decimal
import json


# This is a workaround for: http://bugs.python.org/issue16535
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        print(obj)
        if isinstance(obj, float):
            return "TEST"
        # return json.JSONEncoder.default(self, obj)
        return super(DecimalEncoder, self).default(obj)


class DecimalEncoder2(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)


# Usage:

def test():
    jsonobj = [{'Name': 'Furniture', 'Confidence': 99.51287841796875, 'Instances': [], 'Parents': []},
               {'Name': 'Apparel', 'Confidence': 98.47100830078125, 'Instances': [], 'Parents': []},
               {'Name': 'Clothing', 'Confidence': 98.47100830078125, 'Instances': [], 'Parents': []},
               {'Name': 'Chair', 'Confidence': 98.32756042480469, 'Instances': [], 'Parents': [{'Name': 'Furniture'}]},
               {'Name': 'Couch', 'Confidence': 98.24298095703125, 'Instances': [], 'Parents': [{'Name': 'Furniture'}]},
               {'Name': 'Face', 'Confidence': 97.6850814819336, 'Instances': [], 'Parents': [{'Name': 'Person'}]},
               {'Name': 'Person', 'Confidence': 97.6850814819336, 'Instances': [{'BoundingBox': {
                   'Width': 0.8288427591323853, 'Height': 0.9112775325775146, 'Left': 0.13426895439624786,
                   'Top': 0.0756368339061737}, 'Confidence': 96.98030853271484}], 'Parents': []},
               {'Name': 'Human', 'Confidence': 97.6850814819336, 'Instances': [], 'Parents': []},
               {'Name': 'Interior Design', 'Confidence': 90.20105743408203, 'Instances': [],
                'Parents': [{'Name': 'Indoors'}]},
               {'Name': 'Indoors', 'Confidence': 90.20105743408203, 'Instances': [], 'Parents': []},
               {'Name': 'Man', 'Confidence': 85.92283630371094, 'Instances': [], 'Parents': [{'Name': 'Person'}]},
               {'Name': 'Cushion', 'Confidence': 81.70794677734375, 'Instances': [], 'Parents': []},
               {'Name': 'Bed', 'Confidence': 73.4072494506836, 'Instances': [{'BoundingBox': {
                   'Width': 0.9909370541572571, 'Height': 0.6240440607070923, 'Left': 0.0, 'Top': 0.3738726079463959},
                   'Confidence': 73.4072494506836}],
                'Parents': [{'Name': 'Furniture'}]},
               {'Name': 'Portrait', 'Confidence': 64.9622802734375, 'Instances': [],
                'Parents': [{'Name': 'Face'}, {'Name': 'Photography'}, {'Name': 'Person'}]},
               {'Name': 'Photography', 'Confidence': 64.9622802734375, 'Instances': [],
                'Parents': [{'Name': 'Person'}]},
               {'Name': 'Photo', 'Confidence': 64.9622802734375, 'Instances': [], 'Parents': [{'Name': 'Person'}]},
               {'Name': 'T-Shirt', 'Confidence': 64.92982482910156, 'Instances': [], 'Parents': [{'Name': 'Clothing'}]},
               {'Name': 'Pillow', 'Confidence': 62.49704360961914, 'Instances': [], 'Parents': [{'Name': 'Cushion'}]},
               {'Name': 'Beard', 'Confidence': 61.7859992980957, 'Instances': [],
                'Parents': [{'Name': 'Face'}, {'Name': 'Person'}]},
               {'Name': 'Home Decor', 'Confidence': 58.2867546081543, 'Instances': [], 'Parents': []},
               {'Name': 'Undershirt', 'Confidence': 57.798091888427734, 'Instances': [],
                'Parents': [{'Name': 'Clothing'}]}, {'Name': 'Smile', 'Confidence': 53.017940521240234, 'Instances': [],
                                                     'Parents': [{'Name': 'Face'}, {'Name': 'Person'}]}]
    jstr = json.dumps(
        json.loads(
            json.dumps(
                jsonobj), parse_float=lambda x: round(float(x), 2)))

    jstr = json.dumps(
        json.loads(
            json.dumps(
                jsonobj), parse_float=lambda x: str(round(float(x), 5))))
    print("Json as Str: {}".format(jstr))

def test2():
    # d = decimal.Decimal("42.5")
    # print("Convert from Decimal 42.5 to Float {}".format(json.dumps(d, cls=DecimalEncoder2)))
    fvar = {"x": 90.7898}
    fs = '{"x": 90.7898}'
    s = json.dumps(
        json.loads(
            json.dumps(fvar), parse_float=decimal.Decimal
        )
    )
    print("Convert from float 80.5678 to Decimal {}".format(s))


test()
