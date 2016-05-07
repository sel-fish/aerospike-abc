function init(rec, sender, receiver)
    if aerospike:exists(rec) then
        return 0
    end

    rec.sender = sender
    rec.receiver = receiver
    rec.messages = list()
    return aerospike:create(rec)
end

function send(rec, message)
    local messages = rec.messages
    list.append(messages, message)

    rec.messages = messages
    aerospike:update(rec)

    return list.size(messages)
end

function receive(rec)
    local messages = rec.messages

    rec.messages = list()
    aerospike:update(rec)

    return messages
end
