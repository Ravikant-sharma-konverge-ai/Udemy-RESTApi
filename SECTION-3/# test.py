from flask import Flask, jsonify ,request , render_template #jsonify helps to recive json data and send it

app = Flask(__name__)

stores = [
{'name': 'my wonder store',
  'items':[{'name':'my item','price': 15.99}]
  }]

      #POST used to recive data by api and use to send data by browser
      #GET use to send data back only and use to ask and get data from browser

@app.route('/')
def home():
    return render_template('index.html')      

@app.route('/store', methods=['POST'] )  #POST  /store data: {name:}
def create_store():
    request_data = request.get_json()  # this will get the data come with the POST request and use it as a dic
    new_store = {
        'name': request_data['name'],
        'item':[]
    }
    stores.append(new_store)
    return jsonify(new_store)  #will return this so that browser know we have created the store


@app.route('/store/<string:name>')  #GET  /store/<string:name>  #'http://127.0.0.1:5000/store/some_name
def get_store(name):
    for store in stores:
        return jsonify(store)

    return jsonify({'message':'store not found'})



@app.route('/store')  #GET  /store
def get_stores():
    return jsonify({'stores':stores})

@app.route('/store.<string:name>/item',methods=['POST'])  #POST  /store/<string:name>/item  {name:,price:}
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name']==name:
            new_item = {
                'name':request_data['name'],
                'item': request_data['price']
            }
            
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'store not found'})        
@app.route('/store/<string:name>/item')  #GET /store/<string:name>/item
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'item':store['item']})

    return jsonify({'message':'store not found'})        


app.run(port=5000)

