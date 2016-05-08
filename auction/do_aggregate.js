const Aerospike = require('aerospike')

var namespace='test'
var set='auction'

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
    do_aggregate(client)
  }
})

function do_aggregate(client) {
  var query = client.query(namespace, set)
  query.apply('get_trans_sum', 'trans_sum_by_years', [], null, function(error, result) {
    if (error) {
      console.log(error)
    } else {
      console.log(result)
    }
  })
}

