
# expand FOO.zip into /FOO/files
#
require 'shellwords'
require 'find'
require 'pathname'
require 'fileutils'
zip_file_paths = []
Find.find('.') do |path|
	if path =~ /.*\.zip$/
	  dpath  = File.dirname(path) + "/" + File.basename(path, ".zip")
	  cmd = "unzip -d "+ dpath.shellescape  + " " + path.shellescape 
	  system cmd
	end
end
