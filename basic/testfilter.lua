local function my_map_fn(record)
  return map {name=record.name, bin=record.bin}
end

function myfilter(stream, threshold)
    local function my_filter_fn(record)
        if record['bin'] < threshold then
            return true
        else
            return false
        end
    end
    return stream : filter(my_filter_fn) : map(my_map_fn)
end
