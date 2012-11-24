# Adapted from
# http://stackoverflow.com/questions/9053066/sorted-navigation-menu-with-jekyll-and-liquid

module Jekyll

  class SiteNavigation < Jekyll::Generator
    safe true
	priority :highest

    def generate(site)

        # First remove all invisible items (default: nil = show in nav)
        sorted = []
        site.pages.each do |page|
          sorted << page if page.data["show"] != false
        end

        # Then sort em according to weight
        sorted = sorted.sort{ |a,b| a.data["sortkey"] <=> b.data["sortkey"] } 

        # Debug info.
        puts "Sorted resulting navigation:  (use site.config['sorted_navigation']) "
        sorted.each do |p|
          puts p.inspect 
        end

        # Access this in Liquid using: site.navigation
        site.config["sorted"] = sorted		
    end
  end
end