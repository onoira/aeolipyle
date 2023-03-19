// Copy paste this into the Developer Console on a workshop collection to
// generate a /urls file for use with utils/parse.py
var mods = jQuery('a[href^="https://steamcommunity.com/sharedfiles/filedetails/?id="] > .workshopItemTitle')

var modList = mods.map(function() {
  return {
    name: this.innerText,
    url: this.parentElement.href
  }
}).get()

var modListText = modList.map(function(mod) {
    return mod.name + '\n' + mod.url
}).join('\n')

var blob = new Blob([modListText], {type: 'text/plain'})
var url = URL.createObjectURL(blob)
var a = document.createElement('a')
a.download = 'urls'
a.href = url
a.click()
