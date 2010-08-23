require 'rubygems'
require 'sinatra'
require 'insightful'
require 'broadway'
require 'haml'
require 'json'
require 'open-uri'

configure do
  LOGGER = Logger.new("tmp/development.log") 
  LOGGER.level = Logger::INFO
end

helpers do
  def logger
    LOGGER
  end
end

helpers do
  include Insightful
  def nested_path(post)
    post.path
  end
end

this = File.expand_path(File.dirname(__FILE__))
SITE = Broadway.build(:source => "#{this}/_content", :settings => "#{this}/_config.yml")

enable :sessions
set :public, this
set :views, "views"

get "/" do
  "HELLO"
end

post "/" do
  
end

get "/*" do
  ""
end

not_found do
  ""
end