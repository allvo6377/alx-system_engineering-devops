#!/usr/bin/env ruby
#create a Ruby one argument and pass it to a regular expression matching method

puts ARGV[0].scan(/^\d{10,10}$/).join
