#!/usr/bin/env ruby
puts ARGV.join.scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).map(&:join).join(",")
