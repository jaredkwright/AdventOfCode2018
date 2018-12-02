defmodule Scanner do
  def repeats?(frequency, frequency_set) do
    MapSet.member?(frequency_set, frequency)
  end

  def process_change(frequency_delta, frequency) do
    frequency + frequency_delta
  end

  def compute([], frequency, frequency_set, original_inputs) do
    compute(original_inputs, frequency, frequency_set, original_inputs)
  end

  def compute([frequency_delta | remaining_inputs], frequency, frequency_set, original_inputs) do
    new_frequency = process_change(frequency_delta, frequency)
    if repeats?(new_frequency, frequency_set) do
      new_frequency
    else
      new_set = MapSet.put(frequency_set, frequency)
      compute(remaining_inputs, new_frequency, new_set, original_inputs)
    end
  end

  def synchronize(inputs) do
    frequency_set = MapSet.new()
    compute(inputs, 0, frequency_set, inputs)
  end
end

input =
  File.stream!('../input.txt')
  |> Stream.map(&String.trim_trailing(&1) |> String.to_integer)
  |> Enum.to_list

first_repeating_frequency = Scanner.synchronize(input)
IO.puts 'input sequence first reaches #{first_repeating_frequency} twice'
