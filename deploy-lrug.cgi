#!/usr/bin/env ruby

# This script should be installed at web webhook URL specified
# in .travis.yml

require 'fileutils'

TAR_URL = "https://github.com/lrug/lrug.org/releases/download/travis-release/lrug.org.tar.bz2"
BASE_DIR = "/home/lrug/sites/lrug.org/www/lrug_middleman/"
TMP_FILE = "/tmp/lrug.org.tar.bz2"

NEW_RELEASE = File.join(BASE_DIR, "releases", Time.now.strftime('%Y%m%d%H%M%S'))
OLDEST_RELEASE = Dir[File.join(BASE_DIR, "releases", "*")].sort.first
CURRENT_SYMLINK = File.join(BASE_DIR, "current")

# Download the archive
`curl -L -o #{TMP_FILE} #{TAR_URL}`

# Create the new release directory
FileUtils.mkdir_p(NEW_RELEASE)

# Extract the archive to the new release directory
`tar xjvf #{TMP_FILE} -C #{NEW_RELEASE}`

# Update the symlink
`ln -fsn #{NEW_RELEASE} #{CURRENT_SYMLINK}`

# Remove the oldest release
FileUtils.rm_rf(OLDEST_RELEASE)

puts "HTTP-Version: HTTP/1.0 200 OK"
puts
puts "OK"

exit(0)