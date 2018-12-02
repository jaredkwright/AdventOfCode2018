input = 
  File.stream!('../input.txt')
  |> Stream.map(&String.trim_trailing(&1) |> String.to_integer)
  |> Enum.to_list

frequency = Enum.reduce(input, 0, fn(frequency_change, acc) -> acc + frequency_change end)

IO.puts 'frequency: #{frequency}'
