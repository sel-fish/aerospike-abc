function avg_age(stream)
  count = 0
  sum = 0

  local function female(rec)
    return true
  end

  local function name_age(rec)
    return rec.age
  end

  local function avg(p1, p2)
    count = count + 1 
    sum = sum + p2
    return sum / count
  end

  return stream : filter(female) : map(name_age) : reduce(avg)
end
