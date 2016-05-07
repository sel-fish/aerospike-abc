const Aerospike = require('aerospike')

var namespace='test'
var set='auction'
var primary_key="1"

console.log(require.resolve('aerospike'))

var client = Aerospike.client({
    hosts: [
        { addr: "127.0.0.1", port: 3000 }
    ],
    log: {
        level: Aerospike.log.INFO
    },
    policies: {
        timeout: 2000
    }
})

client.connect(function (error) {
  if (error) {
    // handle failure
    console.log('Connection to Aerospike cluster failed!')
  } else {
    // handle success
    console.log('Connection to Aerospike cluster succeeded!')
    do_put(client)
  }
})

function do_put(client) {
  var key = new Aerospike.Key(namespace, set, primary_key)

	// Record to be written to the database
	var rec = {
      u: 'wade',
      v: [ { t: [ { ts: 906000490, price: 1, qty: 1 } ] } ]
	}

  var policy = {
    // key: Aerospike.policy.key.SEND
  }

	client.put(key, rec, {}, policy, function (error) {
	  if (error) {
	      console.log('error: %s', error.message)
	  } else {
	    console.log('Record written to database successfully.')
	  }
	})
}

