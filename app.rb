require 'rubygems'
require 'sinatra'
#require 'insightful'
require 'broadway'
require 'haml'
require 'json'

this = File.expand_path(File.dirname(__FILE__))
SITE = Broadway.build(:source => "#{this}/_content", :settings => "#{this}/_config.yml")

enable :sessions
set :public, this
set :views, "views"

get "/" do
  "HELLO"
end

post "/" do
  puts "=== REQUEST ==="
  puts request.inspect
  puts "=== PARAMS ==="
  puts params.inspect
  ""
end

get "/*" do
  ""
end

not_found do
  ""
end